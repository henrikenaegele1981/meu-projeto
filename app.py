"""Meu Estúdio: planejar, agendar e postar no Instagram (e depois TikTok) pelo seu PC."""
from __future__ import annotations

import logging
import secrets
import os
import socket
import subprocess
import sys
import threading
import time
import uuid
import webbrowser
from datetime import datetime, timedelta
from pathlib import Path

from flask import (Flask, abort, flash, redirect, render_template, request,
                   send_from_directory, url_for)

import armazenamento as db
import atualizar
import instagram
import vigia

PORTA = 5252
ENDERECO = f"http://localhost:{PORTA}"
VIDEOS_ACEITOS = {".mp4", ".mov"}
FOTOS_ACEITAS = {".jpg", ".jpeg", ".png", ".webp"}
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024  # vídeos de até 1 GB


# ---------- ajudantes ----------

@app.template_filter("data")
def formatar_data(texto: str | None) -> str:
    if not texto:
        return ""
    d = datetime.fromisoformat(texto)
    return f"{DIAS[d.weekday()]}, {d:%d/%m/%Y} às {d:%H:%M}"


@app.context_processor
def variaveis_globais():
    return {"ig": db.carregar_config().get("instagram")}


def _ler_collabs(texto: str) -> list[str]:
    nomes = [n.strip().lstrip("@") for n in texto.replace(";", ",").replace(" ", ",").split(",")]
    return [n for n in nomes if n][:3]  # o Instagram aceita até 3 collabs


def _ler_formulario(post_existente: dict | None = None) -> dict:
    legenda = request.form.get("legenda", "").strip()
    quando = request.form.get("quando", "").strip()
    redes = [r for r in request.form.getlist("redes") if r in ("instagram",)]
    erros = []
    try:
        quando_dt = datetime.fromisoformat(quando)
    except ValueError:
        erros.append("Escolha o dia e a hora da postagem.")
        quando_dt = None
    if not redes:
        erros.append("Marque pelo menos uma rede.")
    if len(legenda) > 2200:
        erros.append("A legenda passou de 2.200 caracteres (limite do Instagram).")

    arquivo = request.files.get("arquivo")
    tem_arquivo_novo = bool(arquivo and arquivo.filename)
    extensao = Path(arquivo.filename).suffix.lower() if tem_arquivo_novo else ""
    if tem_arquivo_novo and extensao not in VIDEOS_ACEITOS | FOTOS_ACEITAS:
        erros.append("O arquivo precisa ser vídeo (.mp4 ou .mov) ou foto (.jpg, .png ou .webp).")
    if not tem_arquivo_novo and not post_existente:
        erros.append("Escolha o vídeo ou a foto.")

    for e in erros:
        flash(e, "erro")
    if erros:
        return {}
    dados = {
        "legenda": legenda,
        "quando": quando_dt.isoformat(timespec="minutes"),
        "redes": redes,
        "collabs": _ler_collabs(request.form.get("collabs", "")),
    }
    if tem_arquivo_novo:
        if extensao in FOTOS_ACEITAS:
            try:
                nome = _salvar_foto(arquivo)
            except ValueError as e:
                flash(str(e), "erro")
                return {}
            dados["tipo"] = "foto"
        else:
            nome = f"{uuid.uuid4().hex}{extensao}"
            arquivo.save(db.MIDIA / nome)
            dados["tipo"] = "reel"
        dados["arquivo"] = nome
        dados["nome_original"] = arquivo.filename
    return dados


def _salvar_foto(arquivo) -> str:
    """Guarda a foto como JPEG (o Instagram só aceita JPEG) e confere o formato."""
    nome = f"{uuid.uuid4().hex}.jpg"
    destino = db.MIDIA / nome
    try:
        from PIL import Image
    except ImportError:
        if Path(arquivo.filename).suffix.lower() not in (".jpg", ".jpeg"):
            raise ValueError("Para usar PNG ou WEBP, rode o instalar.bat de novo "
                             "(ou salve a imagem como JPG).")
        arquivo.save(destino)
        return nome
    try:
        imagem = Image.open(arquivo.stream)
        imagem.load()
    except Exception:
        raise ValueError("Não consegui abrir essa imagem. Tente salvar como JPG.")
    largura, altura = imagem.size
    proporcao = largura / altura
    if proporcao < 0.8 - 0.01 or proporcao > 1.91 + 0.01:
        raise ValueError(
            f"A foto tem {largura}×{altura}. O Instagram só aceita de 4:5 (vertical, ex.: 1080×1350) "
            "até 1,91:1 (horizontal, ex.: 1080×566). Recorte a imagem e tente de novo."
        )
    if imagem.mode != "RGB":
        fundo = Image.new("RGB", imagem.size, (255, 255, 255))
        fundo.paste(imagem, mask=imagem.convert("RGBA").split()[-1])
        imagem = fundo
    if largura > 1440:
        imagem = imagem.resize((1440, round(1440 / proporcao)))
    imagem.save(destino, "JPEG", quality=92)
    return nome


def _apagar_video(post: dict) -> None:
    if post.get("arquivo"):
        (db.MIDIA / post["arquivo"]).unlink(missing_ok=True)


# ---------- telas ----------

@app.route("/")
def inicio():
    return redirect(url_for("agenda"))


@app.route("/configuracoes")
def configuracoes():
    return render_template("configuracoes.html", pagina="config")


@app.post("/configuracoes/instagram")
def salvar_instagram():
    token = request.form.get("token", "").strip()
    ig_id = "".join(c for c in request.form.get("ig_id", "") if c.isdigit())
    if not token:
        flash("Cole o token do Instagram.", "erro")
        return redirect(url_for("configuracoes"))
    try:
        dados = instagram.conta(token, ig_id)
    except instagram.ErroInstagram as e:
        flash(f"A Meta não aceitou esse token: {e}", "erro")
        return redirect(url_for("configuracoes"))
    agora = datetime.now()
    conexao = {
        "token": token,
        "tipo": dados["tipo"],
        "user_id": str(dados["user_id"]),
        "username": dados.get("username") or f"conta {dados['user_id']}",
        "renovado_em": agora.isoformat(timespec="seconds"),
        "expira_em": None,
    }
    if dados["tipo"] == "instagram":
        conexao["expira_em"] = (agora + timedelta(days=60)).isoformat(timespec="seconds")
    with db.trava:
        cfg = db.carregar_config()
        cfg["instagram"] = conexao
        db.salvar_config(cfg)
    flash(f"Instagram conectado: @{conexao['username']}", "ok")
    return redirect(url_for("configuracoes"))


@app.post("/configuracoes/instagram/renovar")
def renovar_instagram():
    vigia.renovar_instagram(forcar=True)
    ig = db.carregar_config().get("instagram") or {}
    if ig.get("aviso"):
        flash(ig["aviso"], "erro")
    else:
        flash("Token renovado. Vale por mais 60 dias.", "ok")
    return redirect(url_for("configuracoes"))


@app.post("/configuracoes/instagram/desconectar")
def desconectar_instagram():
    with db.trava:
        cfg = db.carregar_config()
        cfg.pop("instagram", None)
        db.salvar_config(cfg)
    flash("Instagram desconectado.", "ok")
    return redirect(url_for("configuracoes"))


@app.route("/agenda")
def agenda():
    fila = sorted(db.carregar_fila(), key=lambda p: p["quando"])
    abertos = [p for p in fila if p["status"] != "publicado"]
    publicados = sorted((p for p in fila if p["status"] == "publicado"),
                        key=lambda p: p.get("publicado_em") or p["quando"], reverse=True)
    sugestao = (datetime.now() + timedelta(hours=1)).replace(minute=0).isoformat(timespec="minutes")
    return render_template("agenda.html", pagina="agenda", abertos=abertos,
                           publicados=publicados[:20], sugestao=sugestao)


@app.post("/agenda")
def agendar():
    dados = _ler_formulario()
    if not dados:
        return redirect(url_for("agenda"))
    post = {"id": uuid.uuid4().hex[:10], "status": "agendado", "erro": None,
            "resultados": {}, "criado_em": vigia.agora_texto(), **dados}
    with db.trava:
        fila = db.carregar_fila()
        fila.append(post)
        db.salvar_fila(fila)
    oque = "Foto" if post.get("tipo") == "foto" else "Reel"
    flash(f"{oque} agendado para {formatar_data(post['quando'])}.", "ok")
    return redirect(url_for("agenda"))


@app.route("/agenda/<post_id>/editar", methods=["GET", "POST"])
def editar(post_id):
    post = db.buscar_post(post_id) or abort(404)
    if post["status"] in ("postando", "publicado"):
        flash("Esse post não pode mais ser editado.", "erro")
        return redirect(url_for("agenda"))
    if request.method == "POST":
        dados = _ler_formulario(post_existente=post)
        if not dados:
            return redirect(url_for("editar", post_id=post_id))
        if "arquivo" in dados:
            _apagar_video(post)
            dados["resultados"] = {}
        db.atualizar_post(post_id, status="agendado", erro=None, **dados)
        flash("Post atualizado.", "ok")
        return redirect(url_for("agenda"))
    return render_template("editar.html", pagina="agenda", post=post)


@app.post("/agenda/<post_id>/cancelar")
def cancelar(post_id):
    post = db.buscar_post(post_id) or abort(404)
    if post["status"] == "postando":
        flash("Esse post está sendo enviado agora; espere terminar.", "erro")
        return redirect(url_for("agenda"))
    db.remover_post(post_id)
    _apagar_video(post)
    flash("Post removido da fila.", "ok")
    return redirect(url_for("agenda"))


@app.post("/agenda/<post_id>/tentar")
def tentar_de_novo(post_id):
    post = db.buscar_post(post_id) or abort(404)
    if post["status"] == "erro":
        agora = datetime.now().isoformat(timespec="minutes")
        db.atualizar_post(post_id, status="agendado", erro=None, quando=min(post["quando"], agora))
        flash("Vai tentar de novo em alguns segundos.", "ok")
    return redirect(url_for("agenda"))


@app.route("/midia/<nome>")
def midia(nome):
    return send_from_directory(db.MIDIA, nome)


@app.route("/em-breve/<secao>")
def em_breve(secao):
    return render_template("em_breve.html", pagina=secao)


# ---------- ligar o app ----------

def _porta_ocupada() -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", PORTA)) == 0


def _chave_secreta() -> str:
    with db.trava:
        cfg = db.carregar_config()
        if not cfg.get("chave_secreta"):
            cfg["chave_secreta"] = secrets.token_hex(32)
            db.salvar_config(cfg)
        return cfg["chave_secreta"]


# ---------- atualizacao automatica ----------

VERIFICAR_ATUALIZACAO_A_CADA = 6 * 3600  # segundos
ESTE_ARQUIVO = str(Path(__file__).resolve())


@app.post("/_sair")
def sair():
    """Fecha o app (usado pela versao nova para substituir a antiga). So aceita do proprio PC."""
    if request.remote_addr != "127.0.0.1" or request.headers.get("X-Meu-Estudio") != "1":
        abort(403)
    if _alguem_postando():
        return "postando", 409  # nunca fecha no meio de uma postagem
    threading.Timer(0.5, os._exit, args=(0,)).start()
    return "ok"


def _esperar_porta_livre(segundos: float) -> bool:
    fim = time.time() + segundos
    while time.time() < fim:
        if not _porta_ocupada():
            return True
        time.sleep(0.5)
    return not _porta_ocupada()


def _fechar_versao_aberta() -> None:
    import urllib.request
    try:
        pedido = urllib.request.Request(f"{ENDERECO}/_sair", data=b"", method="POST",
                                        headers={"X-Meu-Estudio": "1"})
        urllib.request.urlopen(pedido, timeout=5).read()
    except Exception:  # noqa: BLE001 - versao antiga nao tem /_sair
        pass
    _esperar_porta_livre(15)


def _alguem_postando() -> bool:
    return any(p.get("status") == "postando" for p in db.carregar_fila())


def _reiniciar_em_nova_janela() -> None:
    """Abre a versao nova e fecha esta (usado quando a atualizacao chega com o app aberto)."""
    sem_console = Path(sys.executable).name.lower() == "pythonw.exe"
    flags = 0
    if os.name == "nt":
        flags = subprocess.DETACHED_PROCESS if sem_console else subprocess.CREATE_NEW_CONSOLE
    subprocess.Popen([sys.executable, ESTE_ARQUIVO, "--sem-navegador", "--sem-atualizar",
                      "--reiniciando"], cwd=str(Path(ESTE_ARQUIVO).parent), creationflags=flags)
    print("\nO Meu Estudio foi atualizado e reabriu em outra janela. Pode fechar esta.")
    os._exit(0)


def _vigiar_atualizacoes() -> None:
    while True:
        time.sleep(VERIFICAR_ATUALIZACAO_A_CADA)
        if atualizar.verificar_e_aplicar():
            while _alguem_postando():  # nunca reinicia no meio de uma postagem
                time.sleep(60)
            _reiniciar_em_nova_janela()


def main() -> None:
    if "--reiniciando" in sys.argv:
        _esperar_porta_livre(20)
    if "--sem-atualizar" not in sys.argv and atualizar.verificar_e_aplicar():
        # Codigo novo baixado: fecha a versao antiga (se estiver aberta) e abre a nova.
        if _porta_ocupada():
            _fechar_versao_aberta()
        args = [a for a in sys.argv[1:] if a != "--sem-atualizar"]
        sys.exit(subprocess.call([sys.executable, ESTE_ARQUIVO, *args, "--sem-atualizar"]))

    abrir_navegador = "--sem-navegador" not in sys.argv
    if _porta_ocupada():  # já está aberto: só mostra a tela
        if abrir_navegador:
            webbrowser.open(ENDERECO)
        return
    db.preparar_pastas()
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(db.ARQ_LOG, encoding="utf-8"), logging.StreamHandler()],
    )
    app.secret_key = _chave_secreta()
    vigia.iniciar()
    threading.Thread(target=_vigiar_atualizacoes, name="atualizacoes", daemon=True).start()
    print(f"Meu Estúdio rodando em {ENDERECO} (dados em {db.DADOS})")
    if abrir_navegador:
        threading.Timer(1.5, webbrowser.open, args=(ENDERECO,)).start()
    app.run(host="127.0.0.1", port=PORTA, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()

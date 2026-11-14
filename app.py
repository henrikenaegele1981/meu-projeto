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

from flask import (Flask, abort, flash, jsonify, redirect, render_template, request,
                   send_from_directory, session, url_for)

import armazenamento as db
import atualizar
import instagram
import nuvem
import vigia

PORTA = 5252
ENDERECO = f"http://localhost:{PORTA}"
VIDEOS_ACEITOS = {".mp4", ".mov"}
FOTOS_ACEITAS = {".jpg", ".jpeg", ".png", ".webp"}
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 * 1024  # vídeos de até 1 GB

if db.NUVEM:
    # Na nuvem (Vercel): a chave vem das variáveis de ambiente e o site pede senha.
    app.secret_key = os.environ.get("FLASK_SECRET") or secrets.token_hex(32)
    app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_SAMESITE="Lax",
                      PERMANENT_SESSION_LIFETIME=timedelta(days=30))
    SENHA = os.environ.get("SENHA_ESTUDIO") or ""
    LIVRES = {"login", "static", "saude"}

    @app.before_request
    def pedir_senha():
        if request.endpoint in LIVRES or session.get("entrou"):
            return None
        if request.path.startswith("/api/"):
            return jsonify(erro="faça login"), 401
        return redirect(url_for("login", proxima=request.path))

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            if SENHA and secrets.compare_digest(request.form.get("senha", ""), SENHA):
                session.permanent = True
                session["entrou"] = True
                destino = request.args.get("proxima") or "/"
                return redirect(destino if destino.startswith("/") else "/")
            flash("Senha errada.", "erro")
        return render_template("login.html", pagina="login")

    @app.route("/sair")
    def sair_da_conta():
        session.clear()
        return redirect(url_for("login"))

    @app.route("/saude")
    def saude():
        return "ok"


# ---------- ajudantes ----------

@app.template_filter("data")
def formatar_data(texto: str | None) -> str:
    if not texto:
        return ""
    d = datetime.fromisoformat(texto)
    return f"{DIAS[d.weekday()]}, {d:%d/%m/%Y} às {d:%H:%M}"


@app.context_processor
def variaveis_globais():
    if db.NUVEM and not session.get("entrou"):
        return {"ig": None, "nuvem": True}
    return {"ig": db.carregar_config().get("instagram"), "nuvem": db.NUVEM}


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
    enviado = request.form.get("enviado", "").strip()  # nuvem: o navegador já mandou ao Supabase
    nome_enviado = request.form.get("nome_original", "").strip()
    if enviado and not _nome_seguro(enviado):
        enviado = ""
    tem_arquivo_novo = bool(enviado or (arquivo and arquivo.filename))
    nome_original = (nome_enviado or enviado) if enviado else (arquivo.filename if tem_arquivo_novo else "")
    extensao = Path(nome_original).suffix.lower() if tem_arquivo_novo else ""
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
                if enviado:
                    import io
                    origem = io.BytesIO(nuvem.baixar(enviado))
                    nome = _salvar_foto(origem, nome_original)
                    db.apagar_midia(enviado)
                else:
                    nome = _salvar_foto(arquivo.stream, arquivo.filename)
            except (ValueError, nuvem.ErroNuvem) as e:
                if enviado:
                    db.apagar_midia(enviado)
                flash(str(e), "erro")
                return {}
            dados["tipo"] = "foto"
        else:
            if enviado:
                nome = enviado
            else:
                nome = f"{uuid.uuid4().hex}{extensao}"
                db.preparar_pastas()
                arquivo.save(db.MIDIA / nome)
            dados["tipo"] = "reel"
        dados["arquivo"] = nome
        dados["nome_original"] = nome_original
    return dados


def _nome_seguro(nome: str) -> bool:
    base, ext = os.path.splitext(nome)
    return (len(base) == 32 and all(c in "0123456789abcdef" for c in base)
            and ext.lower() in VIDEOS_ACEITOS | FOTOS_ACEITAS)


def _salvar_foto(fluxo, nome_original: str) -> str:
    """Guarda a foto como JPEG (o Instagram só aceita JPEG) e confere o formato."""
    import io
    nome = f"{uuid.uuid4().hex}.jpg"
    try:
        from PIL import Image
    except ImportError:
        if Path(nome_original).suffix.lower() not in (".jpg", ".jpeg"):
            raise ValueError("Para usar PNG ou WEBP, rode o instalar.bat de novo "
                             "(ou salve a imagem como JPG).")
        db.salvar_midia(nome, fluxo.read(), "image/jpeg")
        return nome
    try:
        imagem = Image.open(fluxo)
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
    saida = io.BytesIO()
    imagem.save(saida, "JPEG", quality=92)
    db.salvar_midia(nome, saida.getvalue(), "image/jpeg")
    return nome


def _apagar_video(post: dict) -> None:
    db.apagar_midia(post.get("arquivo"))


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
    agora = db.agora()
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
    sugestao = (db.agora() + timedelta(hours=1)).replace(minute=0).isoformat(timespec="minutes")
    return render_template("agenda.html", pagina="agenda", abertos=abertos,
                           publicados=publicados[:20], sugestao=sugestao)


@app.post("/agenda")
def agendar():
    dados = _ler_formulario()
    if not dados:
        return redirect(url_for("agenda"))
    post = {"id": uuid.uuid4().hex[:10], "status": "agendado", "erro": None,
            "resultados": {}, "criado_em": db.agora_texto(), **dados}
    db.adicionar_post(post)
    oque = "Foto" if post.get("tipo") == "foto" else "Reel"
    flash(f"{oque} agendado para {formatar_data(post['quando'])}.", "ok")
    return redirect(url_for("agenda"))


@app.route("/agenda/<post_id>/editar", methods=["GET", "POST"])
def editar(post_id):
    post = db.buscar_post(post_id) or abort(404)
    if post["status"] in ("postando", "processando", "publicando", "publicado"):
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
    if post["status"] in ("postando", "processando", "publicando"):
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
        agora = db.agora().isoformat(timespec="minutes")
        db.atualizar_post(post_id, status="agendado", erro=None, quando=min(post["quando"], agora))
        flash("Vai tentar de novo em alguns segundos.", "ok")
    return redirect(url_for("agenda"))


@app.route("/midia/<nome>")
def midia(nome):
    if db.NUVEM:
        return redirect(nuvem.url_publica(nome))
    return send_from_directory(db.MIDIA, nome)


@app.post("/api/link-de-envio")
def link_de_envio():
    """Nuvem: devolve um link para o navegador mandar o vídeo/foto direto ao Supabase."""
    if not db.NUVEM:
        abort(404)
    extensao = Path(request.form.get("nome", "")).suffix.lower()
    if extensao not in VIDEOS_ACEITOS | FOTOS_ACEITAS:
        return jsonify(erro="O arquivo precisa ser vídeo (.mp4 ou .mov) ou foto (.jpg, .png ou .webp)."), 400
    nome = f"{uuid.uuid4().hex}{extensao}"
    try:
        return jsonify(nome=nome, url=nuvem.link_de_envio(nome))
    except nuvem.ErroNuvem as e:
        return jsonify(erro=str(e)), 502


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

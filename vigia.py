"""Vigia em segundo plano: confere a fila a cada 15 segundos e posta na hora certa."""
from __future__ import annotations

import logging
import threading
import time
from datetime import datetime, timedelta

import armazenamento as db
import instagram

INTERVALO = 15
RENOVAR_A_CADA = timedelta(days=30)  # o token vale 60 dias; renovamos com folga

log = logging.getLogger("vigia")


def agora_texto() -> str:
    return datetime.now().isoformat(timespec="seconds")


# ---------- token do Instagram ----------

def renovar_instagram(forcar: bool = False) -> None:
    cfg = db.carregar_config()
    ig = cfg.get("instagram")
    if not ig or not ig.get("token"):
        return
    if ig.get("tipo") == "facebook":
        return  # token do Facebook/usuario do sistema: nao usa a renovacao do Instagram
    renovado = datetime.fromisoformat(ig.get("renovado_em", agora_texto()))
    if not forcar and datetime.now() - renovado < RENOVAR_A_CADA:
        return
    try:
        novo = instagram.renovar_token(ig["token"])
    except instagram.ErroInstagram as e:
        ig["aviso"] = f"Não consegui renovar o token: {e}"
        log.warning(ig["aviso"])
    else:
        ig["token"] = novo["access_token"]
        ig["renovado_em"] = agora_texto()
        segundos = int(novo.get("expires_in") or 60 * 24 * 3600)
        ig["expira_em"] = (datetime.now() + timedelta(seconds=segundos)).isoformat(timespec="seconds")
        ig.pop("aviso", None)
        log.info("Token do Instagram renovado.")
    with db.trava:
        cfg_atual = db.carregar_config()
        cfg_atual["instagram"] = ig
        db.salvar_config(cfg_atual)


# ---------- postagem ----------

def _postar_instagram(post: dict) -> dict:
    ig = db.carregar_config().get("instagram") or {}
    if not ig.get("token"):
        raise instagram.ErroInstagram("Instagram não conectado. Vá em Configurações e cole o token.")
    arquivo = db.MIDIA / post["arquivo"]
    if not arquivo.exists():
        raise instagram.ErroInstagram("O arquivo do post sumiu da pasta de dados.")
    url = instagram.hospedar_temporario(arquivo)
    publicar = instagram.publicar_foto if post.get("tipo") == "foto" else instagram.publicar_reel
    return publicar(ig["token"], ig["user_id"], url, post.get("legenda", ""),
                    post.get("collabs") or None, ig.get("tipo"))


def postar(post: dict) -> None:
    db.atualizar_post(post["id"], status="postando", erro=None)
    resultados = dict(post.get("resultados") or {})
    erros = []
    for rede in post.get("redes", []):
        if (resultados.get(rede) or {}).get("ok"):
            continue  # já saiu nessa rede numa tentativa anterior
        try:
            if rede == "instagram":
                feito = _postar_instagram(post)
            else:
                raise instagram.ErroInstagram(f"{rede} ainda não está disponível.")
            resultados[rede] = {"ok": True, **feito}
        except Exception as e:  # noqa: BLE001 - qualquer falha vira mensagem na fila
            log.exception("Falha ao postar %s no %s", post["id"], rede)
            resultados[rede] = {"ok": False, "erro": str(e)}
            erros.append(f"{rede.capitalize()}: {e}")
        db.atualizar_post(post["id"], resultados=resultados)

    if erros:
        db.atualizar_post(post["id"], status="erro", erro=" | ".join(erros))
    else:
        db.atualizar_post(post["id"], status="publicado", erro=None, publicado_em=agora_texto())


def ciclo() -> None:
    renovar_instagram()
    agora = datetime.now()
    pendentes = sorted(
        (p for p in db.carregar_fila() if p.get("status") == "agendado"),
        key=lambda p: p["quando"],
    )
    for post in pendentes:
        if datetime.fromisoformat(post["quando"]) <= agora:
            # relê do disco: pode ter sido editado ou cancelado enquanto outro postava
            atual = db.buscar_post(post["id"])
            if atual and atual.get("status") == "agendado":
                postar(atual)


def recuperar_interrompidos() -> None:
    """Se o app fechou no meio de uma postagem, não repete sozinho (evita post duplicado)."""
    for post in db.carregar_fila():
        if post.get("status") == "postando":
            db.atualizar_post(
                post["id"], status="erro",
                erro="O app foi fechado enquanto postava. Confira no Instagram se saiu; "
                     "se não saiu, clique em “Tentar de novo”.",
            )


def _laco() -> None:
    while True:
        try:
            ciclo()
        except Exception:  # noqa: BLE001 - o vigia nunca pode morrer
            log.exception("Erro no vigia")
        time.sleep(INTERVALO)


def iniciar() -> None:
    recuperar_interrompidos()
    threading.Thread(target=_laco, name="vigia", daemon=True).start()

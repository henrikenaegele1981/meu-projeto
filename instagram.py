"""Conversa com a API oficial do Instagram (login do Instagram, graph.instagram.com)."""
from __future__ import annotations

import json
import time
from pathlib import Path

import requests

API = "https://graph.instagram.com/v21.0"
HOSPEDAGEM = "https://litterbox.catbox.moe/resources/internals/api.php"
TEMPO_LIMITE = 60
ESPERA_PROCESSAMENTO = 15 * 60  # máximo que esperamos o Instagram processar o vídeo


class ErroInstagram(Exception):
    pass


def _resposta(resp: requests.Response) -> dict:
    try:
        dados = resp.json()
    except ValueError:
        raise ErroInstagram(f"Resposta inesperada do Instagram (HTTP {resp.status_code}).")
    if resp.status_code >= 400 or "error" in dados:
        erro = dados.get("error") or {}
        msg = erro.get("error_user_msg") or erro.get("message") or f"HTTP {resp.status_code}"
        raise ErroInstagram(msg)
    return dados


def _get(caminho: str, token: str, **params) -> dict:
    params["access_token"] = token
    try:
        return _resposta(requests.get(f"{API}/{caminho}", params=params, timeout=TEMPO_LIMITE))
    except requests.RequestException as e:
        raise ErroInstagram(f"Sem conexão com o Instagram: {e}")


def _post(caminho: str, token: str, **dados) -> dict:
    dados["access_token"] = token
    try:
        return _resposta(requests.post(f"{API}/{caminho}", data=dados, timeout=TEMPO_LIMITE))
    except requests.RequestException as e:
        raise ErroInstagram(f"Sem conexão com o Instagram: {e}")


def conta(token: str) -> dict:
    """Devolve {'user_id': ..., 'username': ...} da conta dona do token."""
    dados = _get("me", token, fields="user_id,username")
    if not dados.get("user_id"):
        dados["user_id"] = dados.get("id")
    return dados


def renovar_token(token: str) -> dict:
    """Troca o token por um novo de 60 dias. Devolve {'access_token', 'expires_in'}."""
    try:
        resp = requests.get(
            "https://graph.instagram.com/refresh_access_token",
            params={"grant_type": "ig_refresh_token", "access_token": token},
            timeout=TEMPO_LIMITE,
        )
    except requests.RequestException as e:
        raise ErroInstagram(f"Sem conexão com o Instagram: {e}")
    return _resposta(resp)


def hospedar_temporario(caminho: Path) -> str:
    """Sobe o vídeo no litterbox (some sozinho em 1 hora) só para o Instagram buscar."""
    try:
        with open(caminho, "rb") as arquivo:
            resp = requests.post(
                HOSPEDAGEM,
                data={"reqtype": "fileupload", "time": "1h"},
                files={"fileToUpload": (Path(caminho).name, arquivo)},
                timeout=900,
            )
    except requests.RequestException as e:
        raise ErroInstagram(f"Não consegui subir o vídeo na hospedagem temporária: {e}")
    url = resp.text.strip()
    if resp.status_code != 200 or not url.startswith("http"):
        raise ErroInstagram(f"A hospedagem temporária recusou o vídeo: {url[:200]}")
    return url


def publicar_reel(token: str, user_id: str, video_url: str, legenda: str,
                  collabs: list[str] | None = None) -> dict:
    """Cria o container, espera ficar FINISHED e publica. Devolve {'id', 'link'}."""
    campos = {"media_type": "REELS", "video_url": video_url, "caption": legenda,
              "share_to_feed": "true"}
    if collabs:
        campos["collaborators"] = json.dumps(collabs)
    container = _post(f"{user_id}/media", token, **campos)["id"]

    prazo = time.time() + ESPERA_PROCESSAMENTO
    while True:
        estado = _get(container, token, fields="status_code,status")
        codigo = estado.get("status_code")
        if codigo == "FINISHED":
            break
        if codigo in ("ERROR", "EXPIRED"):
            raise ErroInstagram(
                f"O Instagram recusou o vídeo ({codigo}): {estado.get('status') or 'sem detalhes'}. "
                "Confira se é MP4/MOV, vertical, de 3 s a 15 min."
            )
        if time.time() > prazo:
            raise ErroInstagram("O Instagram demorou mais de 15 minutos para processar o vídeo.")
        time.sleep(10)

    media_id = _post(f"{user_id}/media_publish", token, creation_id=container)["id"]
    try:
        link = _get(media_id, token, fields="permalink").get("permalink")
    except ErroInstagram:
        link = None
    return {"id": media_id, "link": link}

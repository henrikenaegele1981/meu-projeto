"""Conversa com a API oficial do Instagram.

Aceita os dois tipos de token que a Meta gera:
- "instagram": token do login do Instagram (apps antigos), servidor graph.instagram.com;
- "facebook": token do login unificado / usuario do sistema (apps novos), servidor graph.facebook.com.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import requests

API = "https://graph.instagram.com/v21.0"
API_FACEBOOK = "https://graph.facebook.com"  # sem versao: usa a versao padrao do app
SERVIDORES = {"instagram": API, "facebook": API_FACEBOOK}
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


def _base(tipo: str | None) -> str:
    return SERVIDORES.get(tipo or "instagram", API)


def _get(caminho: str, token: str, tipo: str | None = None, **params) -> dict:
    params["access_token"] = token
    try:
        return _resposta(requests.get(f"{_base(tipo)}/{caminho}", params=params, timeout=TEMPO_LIMITE))
    except requests.RequestException as e:
        raise ErroInstagram(f"Sem conexão com o Instagram: {e}")


def _post(caminho: str, token: str, tipo: str | None = None, **dados) -> dict:
    dados["access_token"] = token
    try:
        return _resposta(requests.post(f"{_base(tipo)}/{caminho}", data=dados, timeout=TEMPO_LIMITE))
    except requests.RequestException as e:
        raise ErroInstagram(f"Sem conexão com o Instagram: {e}")


def _contas_das_paginas(token: str) -> list[dict]:
    """Contas do Instagram ligadas as Paginas do Facebook que o token enxerga."""
    try:
        paginas = _get("me/accounts", token, "facebook",
                       fields="instagram_business_account{id,username}").get("data") or []
    except ErroInstagram:
        return []
    contas = []
    for pagina in paginas:
        conta_ig = pagina.get("instagram_business_account")
        if conta_ig and conta_ig.get("id"):
            contas.append({"user_id": str(conta_ig["id"]), "username": conta_ig.get("username", ""),
                           "tipo": "facebook"})
    return contas


def _conta_facebook(token: str, ig_id: str | None) -> dict:
    if ig_id:
        try:
            dados = _get(ig_id, token, "facebook", fields="id,username")
            return {"user_id": str(dados.get("id") or ig_id), "username": dados.get("username", ""),
                    "tipo": "facebook"}
        except ErroInstagram as e:
            if "nonexisting field" not in str(e):
                raise
        # A Meta nao deixou ler o @ por esse ID: tenta achar a conta pelas Paginas do token.
        contas = _contas_das_paginas(token)
        if len(contas) == 1:
            return contas[0]
        for c in contas:
            if c["user_id"] == ig_id:
                return c
        dados = _get(ig_id, token, "facebook", fields="id")
        return {"user_id": str(dados.get("id") or ig_id), "username": "", "tipo": "facebook"}
    contas = _contas_das_paginas(token)
    if contas:
        return contas[0]
    raise ErroInstagram(
        "O token foi aceito, mas não achei a conta do Instagram. Preencha o campo "
        "“ID da conta do Instagram” (o número que aparece embaixo do seu @ no painel da Meta)."
    )


def conta(token: str, ig_id: str | None = None) -> dict:
    """Descobre de quem e o token. Devolve {'user_id', 'username', 'tipo'}.

    Tenta primeiro como token do login do Instagram; se nao der, como token do Facebook
    (login unificado / usuario do sistema).
    """
    ig_id = (ig_id or "").strip() or None
    try:
        dados = _get("me", token, "instagram", fields="user_id,username")
        return {"user_id": str(dados.get("user_id") or dados.get("id")),
                "username": dados.get("username", ""), "tipo": "instagram"}
    except ErroInstagram as erro_instagram:
        try:
            return _conta_facebook(token, ig_id)
        except ErroInstagram as erro_facebook:
            if "não achei a conta" in str(erro_facebook):
                raise
            raise ErroInstagram(
                f"{erro_facebook} (como token do Instagram: {erro_instagram})"
            ) from erro_facebook


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
                  collabs: list[str] | None = None, tipo: str | None = None) -> dict:
    """Cria o container, espera ficar FINISHED e publica. Devolve {'id', 'link'}."""
    campos = {"media_type": "REELS", "video_url": video_url, "caption": legenda,
              "share_to_feed": "true"}
    if collabs:
        campos["collaborators"] = json.dumps(collabs)
    container = _post(f"{user_id}/media", token, tipo, **campos)["id"]

    prazo = time.time() + ESPERA_PROCESSAMENTO
    while True:
        estado = _get(container, token, tipo, fields="status_code,status")
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

    media_id = _post(f"{user_id}/media_publish", token, tipo, creation_id=container)["id"]
    try:
        link = _get(media_id, token, tipo, fields="permalink").get("permalink")
    except ErroInstagram:
        link = None
    return {"id": media_id, "link": link}

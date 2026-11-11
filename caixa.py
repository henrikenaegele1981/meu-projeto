"""Caixa de entrada: posts agendados de fora do PC (pelo Claude) via GitHub.

O Claude publica um arquivo fila.json na branch `caixa` do repositorio. O app confere a cada minuto
e coloca na Agenda os posts novos, que depois sao publicados normalmente com o token do app.

Formato de fila.json:
[
  {"id": "nmecha-1", "tipo": "foto" | "reel", "quando": "2026-11-11T15:00",
   "legenda": "...", "midia": "https://.../post.jpg", "collabs": ["amigo"],
   "cancelado": false}
]
"""
from __future__ import annotations

import json
import logging
import urllib.request
import uuid
from datetime import datetime, timedelta

import armazenamento as db

URL_CAIXA = "https://raw.githubusercontent.com/henrikenaegele1981/meu-projeto/caixa/fila.json"
TEMPO_LIMITE = 60
ATRASO_MAXIMO = timedelta(hours=2)  # post que chega muito atrasado nao sai sozinho

log = logging.getLogger("caixa")


def _baixar(url: str) -> bytes:
    pedido = urllib.request.Request(url, headers={"User-Agent": "MeuEstudio", "Cache-Control": "no-cache"})
    with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE) as resp:
        return resp.read()


def _importados(cfg: dict) -> list[str]:
    return list(cfg.get("caixa_importados") or [])


def conferir() -> int:
    """Traz para a Agenda os posts novos da caixa. Devolve quantos entraram."""
    try:
        itens = json.loads(_baixar(f"{URL_CAIXA}?t={int(datetime.now().timestamp())}"))
    except Exception as e:  # noqa: BLE001 - sem internet ou caixa vazia: tenta depois
        log.debug("Caixa indisponível: %s", e)
        return 0
    if not isinstance(itens, list):
        return 0

    cfg = db.carregar_config()
    importados = _importados(cfg)
    novos = 0
    for item in itens:
        chave = str(item.get("id") or "")
        if not chave:
            continue
        if item.get("cancelado"):
            _cancelar(chave)
            continue
        if chave in importados:
            continue
        try:
            post = _montar_post(item)
        except Exception as e:  # noqa: BLE001
            log.warning("Não consegui importar %s da caixa: %s", chave, e)
            continue
        with db.trava:
            fila = db.carregar_fila()
            fila.append(post)
            db.salvar_fila(fila)
            cfg = db.carregar_config()
            cfg["caixa_importados"] = (_importados(cfg) + [chave])[-500:]
            db.salvar_config(cfg)
        importados.append(chave)
        novos += 1
        log.info("Post %s importado da caixa para %s.", chave, post["quando"])
    return novos


def _montar_post(item: dict) -> dict:
    tipo = "reel" if item.get("tipo") == "reel" else "foto"
    quando = datetime.fromisoformat(item["quando"])
    db.preparar_pastas()
    nome = f"{uuid.uuid4().hex}{'.mp4' if tipo == 'reel' else '.jpg'}"
    (db.MIDIA / nome).write_bytes(_baixar(item["midia"]))
    agora = datetime.now()
    atrasado = quando < agora - ATRASO_MAXIMO
    return {
        "id": uuid.uuid4().hex[:10],
        "tipo": tipo,
        "status": "erro" if atrasado else "agendado",
        "erro": ("Chegou pela caixa depois do horário marcado. Confira e clique em "
                 "“Tentar de novo” se ainda quiser postar.") if atrasado else None,
        "resultados": {},
        "criado_em": agora.isoformat(timespec="seconds"),
        "legenda": str(item.get("legenda") or "")[:2200],
        "quando": quando.isoformat(timespec="minutes"),
        "redes": ["instagram"],
        "collabs": [str(c).lstrip("@") for c in (item.get("collabs") or [])][:3],
        "arquivo": nome,
        "nome_original": item["midia"].rsplit("/", 1)[-1],
        "origem": "caixa",
        "caixa_id": str(item["id"]),
    }


def _cancelar(chave: str) -> None:
    for post in db.carregar_fila():
        if post.get("caixa_id") == chave and post.get("status") in ("agendado", "erro"):
            db.remover_post(post["id"])
            if post.get("arquivo"):
                (db.MIDIA / post["arquivo"]).unlink(missing_ok=True)
            log.info("Post %s cancelado pela caixa.", chave)

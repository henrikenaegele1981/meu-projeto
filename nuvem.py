"""Conversa com o Supabase (banco e armazenamento de mídia) quando o app roda na nuvem (Vercel).

Ligado quando existem as variáveis SUPABASE_URL e SUPABASE_SERVICE_KEY. A chave de serviço só
fica no servidor (variável de ambiente da Vercel), nunca vai para o navegador.
"""
from __future__ import annotations

import os
from urllib.parse import quote

import requests

URL = (os.environ.get("SUPABASE_URL") or "").rstrip("/")
CHAVE = os.environ.get("SUPABASE_SERVICE_KEY") or ""
BUCKET = os.environ.get("SUPABASE_BUCKET") or "midia"
ATIVO = bool(URL and CHAVE)
TEMPO_LIMITE = 30


class ErroNuvem(Exception):
    pass


def _cabecalhos(extra: dict | None = None) -> dict:
    h = {"apikey": CHAVE, "Authorization": f"Bearer {CHAVE}"}
    h.update(extra or {})
    return h


def _checar(resp: requests.Response):
    if resp.status_code >= 400:
        raise ErroNuvem(f"Supabase respondeu HTTP {resp.status_code}: {resp.text[:300]}")
    if not resp.content:
        return None
    try:
        return resp.json()
    except ValueError:
        return resp.text


# ---------- banco (PostgREST) ----------

def selecionar(tabela: str, **params) -> list[dict]:
    resp = requests.get(f"{URL}/rest/v1/{tabela}", params=params, headers=_cabecalhos(),
                        timeout=TEMPO_LIMITE)
    return _checar(resp) or []


def inserir(tabela: str, linhas, upsert: bool = False) -> list[dict]:
    prefer = "return=representation"
    if upsert:
        prefer += ",resolution=merge-duplicates"
    resp = requests.post(f"{URL}/rest/v1/{tabela}", json=linhas,
                         headers=_cabecalhos({"Prefer": prefer}), timeout=TEMPO_LIMITE)
    return _checar(resp) or []


def alterar(tabela: str, valores: dict, **filtros) -> list[dict]:
    """PATCH com filtros do PostgREST (ex.: id="eq.abc"). Devolve as linhas alteradas."""
    resp = requests.patch(f"{URL}/rest/v1/{tabela}", params=filtros, json=valores,
                          headers=_cabecalhos({"Prefer": "return=representation"}),
                          timeout=TEMPO_LIMITE)
    return _checar(resp) or []


def apagar(tabela: str, **filtros) -> None:
    resp = requests.delete(f"{URL}/rest/v1/{tabela}", params=filtros, headers=_cabecalhos(),
                           timeout=TEMPO_LIMITE)
    _checar(resp)


# ---------- armazenamento de mídia ----------

def url_publica(nome: str) -> str:
    return f"{URL}/storage/v1/object/public/{BUCKET}/{quote(nome)}"


def link_de_envio(nome: str) -> str:
    """Link assinado para o navegador enviar o arquivo direto ao Supabase (sem passar pela Vercel,
    que limita o tamanho das requisições)."""
    resp = requests.post(f"{URL}/storage/v1/object/upload/sign/{BUCKET}/{quote(nome)}",
                         headers=_cabecalhos(), json={}, timeout=TEMPO_LIMITE)
    dados = _checar(resp) or {}
    caminho = dados.get("url") or ""
    if not caminho:
        raise ErroNuvem("O Supabase não gerou o link de envio.")
    return f"{URL}/storage/v1{caminho}"


def enviar(nome: str, conteudo: bytes, tipo_conteudo: str) -> None:
    resp = requests.post(f"{URL}/storage/v1/object/{BUCKET}/{quote(nome)}", data=conteudo,
                         headers=_cabecalhos({"Content-Type": tipo_conteudo, "x-upsert": "true"}),
                         timeout=300)
    _checar(resp)


def baixar(nome: str) -> bytes:
    resp = requests.get(f"{URL}/storage/v1/object/{BUCKET}/{quote(nome)}", headers=_cabecalhos(),
                        timeout=300)
    if resp.status_code >= 400:
        raise ErroNuvem(f"Não achei o arquivo {nome} no Supabase (HTTP {resp.status_code}).")
    return resp.content


def existe(nome: str) -> bool:
    resp = requests.head(url_publica(nome), timeout=TEMPO_LIMITE)
    return resp.status_code == 200


def remover(nome: str) -> None:
    resp = requests.delete(f"{URL}/storage/v1/object/{BUCKET}", headers=_cabecalhos(),
                           json={"prefixes": [nome]}, timeout=TEMPO_LIMITE)
    if resp.status_code >= 400 and resp.status_code != 404:
        _checar(resp)

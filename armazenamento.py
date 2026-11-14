"""Onde e como o Meu Estúdio guarda os dados.

- No PC: arquivos JSON em %LOCALAPPDATA%\\MeuEstudio (nunca na pasta do código).
- Na nuvem (Vercel): tabelas e armazenamento do Supabase (ver nuvem.py e nuvem/schema.sql).
"""
from __future__ import annotations

import json
import os
import threading
from datetime import datetime
from pathlib import Path

import nuvem

NUVEM = nuvem.ATIVO


def _pasta_dados() -> Path:
    personalizada = os.environ.get("MEU_ESTUDIO_DADOS")
    if personalizada:
        return Path(personalizada)
    if NUVEM:
        return Path("/tmp/meu-estudio")  # só para arquivos temporários
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
        return Path(base) / "MeuEstudio"
    return Path.home() / ".meu-estudio"


DADOS = _pasta_dados()
MIDIA = DADOS / "midia"
ARQ_CONFIG = DADOS / "config.json"   # tokens e chaves ficam SÓ aqui
ARQ_FILA = DADOS / "fila.json"
ARQ_LOG = DADOS / "estudio.log"

# Uma trava só para todos os arquivos: o site e o vigia mexem neles ao mesmo tempo.
trava = threading.RLock()


def agora() -> datetime:
    """Hora local do usuário, sem fuso (como o formulário envia).

    No PC é a hora do Windows. Na nuvem o servidor fica em UTC, então usamos FUSO
    (padrão America/Sao_Paulo)."""
    fuso = os.environ.get("FUSO") or ("America/Sao_Paulo" if NUVEM else "")
    if not fuso:
        return datetime.now()
    from zoneinfo import ZoneInfo
    return datetime.now(ZoneInfo(fuso)).replace(tzinfo=None)


def agora_texto() -> str:
    return agora().isoformat(timespec="seconds")


def preparar_pastas() -> None:
    MIDIA.mkdir(parents=True, exist_ok=True)


def _ler(caminho: Path, padrao):
    with trava:
        if not caminho.exists():
            return padrao
        try:
            return json.loads(caminho.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return padrao


def _gravar(caminho: Path, dados) -> None:
    with trava:
        caminho.parent.mkdir(parents=True, exist_ok=True)
        temporario = caminho.with_suffix(".tmp")
        temporario.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(temporario, caminho)  # troca de uma vez: nunca deixa o arquivo pela metade


# ---------- configurações ----------

def carregar_config() -> dict:
    if NUVEM:
        linhas = nuvem.selecionar("estudio_config", chave="eq.config", select="valor")
        return dict(linhas[0]["valor"]) if linhas else {}
    return _ler(ARQ_CONFIG, {})


def salvar_config(cfg: dict) -> None:
    if NUVEM:
        nuvem.inserir("estudio_config", {"chave": "config", "valor": cfg}, upsert=True)
        return
    _gravar(ARQ_CONFIG, cfg)


# ---------- fila de posts ----------
# Na nuvem cada post é uma linha: `status` e `quando` ficam em colunas (para filtrar e para
# "reservar" um post sem risco de postar duas vezes) e o resto vai em `dados`.

def _linha(post: dict) -> dict:
    return {"id": post["id"], "status": post.get("status", "agendado"),
            "quando": post.get("quando"), "dados": post}


def _post(linha: dict) -> dict:
    post = dict(linha.get("dados") or {})
    post["id"] = linha["id"]
    post["status"] = linha.get("status") or post.get("status")
    return post


def carregar_fila() -> list[dict]:
    if NUVEM:
        return [_post(l) for l in nuvem.selecionar("estudio_posts", select="*", order="quando")]
    return _ler(ARQ_FILA, [])


def salvar_fila(fila: list[dict]) -> None:
    if NUVEM:
        if fila:
            nuvem.inserir("estudio_posts", [_linha(p) for p in fila], upsert=True)
        ids = {p["id"] for p in fila}
        for post in carregar_fila():
            if post["id"] not in ids:
                nuvem.apagar("estudio_posts", id=f"eq.{post['id']}")
        return
    _gravar(ARQ_FILA, fila)


def adicionar_post(post: dict) -> None:
    if NUVEM:
        nuvem.inserir("estudio_posts", _linha(post))
        return
    with trava:
        fila = carregar_fila()
        fila.append(post)
        salvar_fila(fila)


def buscar_post(post_id: str) -> dict | None:
    if NUVEM:
        linhas = nuvem.selecionar("estudio_posts", id=f"eq.{post_id}", select="*")
        return _post(linhas[0]) if linhas else None
    return next((p for p in carregar_fila() if p["id"] == post_id), None)


def atualizar_post(post_id: str, **campos) -> dict | None:
    with trava:
        if NUVEM:
            post = buscar_post(post_id)
            if not post:
                return None
            post.update(campos)
            nuvem.alterar("estudio_posts", {"status": post["status"], "quando": post.get("quando"),
                                            "dados": post}, id=f"eq.{post_id}")
            return post
        fila = carregar_fila()
        for post in fila:
            if post["id"] == post_id:
                post.update(campos)
                salvar_fila(fila)
                return post
    return None


def reservar_post(post_id: str, de: str, para: str) -> dict | None:
    """Troca o status de `de` para `para` só se ninguém trocou antes. Evita post duplicado
    quando duas execuções do vigia rodam ao mesmo tempo."""
    if NUVEM:
        linhas = nuvem.alterar("estudio_posts", {"status": para}, id=f"eq.{post_id}",
                               status=f"eq.{de}")
        if not linhas:
            return None
        return atualizar_post(post_id, status=para)
    with trava:
        post = buscar_post(post_id)
        if not post or post.get("status") != de:
            return None
        return atualizar_post(post_id, status=para)


def remover_post(post_id: str) -> dict | None:
    if NUVEM:
        removido = buscar_post(post_id)
        nuvem.apagar("estudio_posts", id=f"eq.{post_id}")
        return removido
    with trava:
        fila = carregar_fila()
        restante = [p for p in fila if p["id"] != post_id]
        removido = next((p for p in fila if p["id"] == post_id), None)
        salvar_fila(restante)
        return removido


# ---------- arquivos de mídia ----------

def salvar_midia(nome: str, conteudo: bytes, tipo_conteudo: str = "application/octet-stream") -> None:
    if NUVEM:
        nuvem.enviar(nome, conteudo, tipo_conteudo)
        return
    preparar_pastas()
    (MIDIA / nome).write_bytes(conteudo)


def apagar_midia(nome: str | None) -> None:
    if not nome:
        return
    if NUVEM:
        try:
            nuvem.remover(nome)
        except nuvem.ErroNuvem:
            pass
        return
    (MIDIA / nome).unlink(missing_ok=True)

"""Onde e como o Meu Estúdio guarda os dados (arquivos JSON fora da pasta do código)."""
from __future__ import annotations

import json
import os
import threading
from pathlib import Path


def _pasta_dados() -> Path:
    personalizada = os.environ.get("MEU_ESTUDIO_DADOS")
    if personalizada:
        return Path(personalizada)
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
    return _ler(ARQ_CONFIG, {})


def salvar_config(cfg: dict) -> None:
    _gravar(ARQ_CONFIG, cfg)


# ---------- fila de posts ----------

def carregar_fila() -> list[dict]:
    return _ler(ARQ_FILA, [])


def salvar_fila(fila: list[dict]) -> None:
    _gravar(ARQ_FILA, fila)


def buscar_post(post_id: str) -> dict | None:
    return next((p for p in carregar_fila() if p["id"] == post_id), None)


def atualizar_post(post_id: str, **campos) -> dict | None:
    with trava:
        fila = carregar_fila()
        for post in fila:
            if post["id"] == post_id:
                post.update(campos)
                salvar_fila(fila)
                return post
    return None


def remover_post(post_id: str) -> dict | None:
    with trava:
        fila = carregar_fila()
        restante = [p for p in fila if p["id"] != post_id]
        removido = next((p for p in fila if p["id"] == post_id), None)
        salvar_fila(restante)
        return removido

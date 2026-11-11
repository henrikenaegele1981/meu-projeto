"""Atualiza o Meu Estudio sozinho a partir do GitHub (branch meu-estudio).

So usa a biblioteca padrao do Python, para funcionar mesmo se algo quebrar.
Os seus dados (token, fila, videos) ficam em outra pasta e nunca sao tocados.
"""
from __future__ import annotations

import io
import json
import logging
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path

REPO = "henrikenaegele1981/meu-projeto"
BRANCH = "meu-estudio"
URL_VERSAO = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"
URL_ZIP = "https://codeload.github.com/" + REPO + "/zip/{sha}"
PASTA = Path(__file__).resolve().parent
ARQ_VERSAO = PASTA / ".versao"
TEMPO_LIMITE = 30

log = logging.getLogger("atualizar")


def _baixar(url: str, aceitar: str = "*/*") -> bytes:
    pedido = urllib.request.Request(url, headers={"User-Agent": "MeuEstudio", "Accept": aceitar})
    with urllib.request.urlopen(pedido, timeout=TEMPO_LIMITE) as resp:
        return resp.read()


def versao_local() -> str:
    try:
        return ARQ_VERSAO.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


def ultima_versao() -> str:
    dados = json.loads(_baixar(URL_VERSAO, "application/vnd.github+json"))
    return dados["sha"]


def _aplicar(sha: str) -> list[str]:
    """Baixa o codigo da versao `sha` e copia por cima. Devolve os arquivos que mudaram."""
    pacote = zipfile.ZipFile(io.BytesIO(_baixar(URL_ZIP.format(sha=sha))))
    mudaram = []
    for item in pacote.infolist():
        partes = Path(item.filename).parts[1:]  # tira a pasta "meu-projeto-<sha>/"
        if item.is_dir() or not partes or any(p.startswith(".git") or p == ".." for p in partes):
            continue
        destino = PASTA.joinpath(*partes)
        conteudo = pacote.read(item)
        if destino.exists() and destino.read_bytes() == conteudo:
            continue  # igual: nao mexe (importante para o .bat que esta rodando)
        destino.parent.mkdir(parents=True, exist_ok=True)
        temporario = destino.with_name(destino.name + ".novo")
        temporario.write_bytes(conteudo)
        temporario.replace(destino)
        mudaram.append("/".join(partes))
    return mudaram


def _instalar_dependencias() -> None:
    python = Path(sys.executable)
    if python.name.lower() == "pythonw.exe" and python.with_name("python.exe").exists():
        python = python.with_name("python.exe")
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    resultado = subprocess.run(
        [str(python), "-m", "pip", "install", "-q", "-r", str(PASTA / "requirements.txt")],
        capture_output=True, text=True, creationflags=flags,
    )
    if resultado.returncode != 0:
        log.warning("pip falhou: %s", (resultado.stderr or resultado.stdout)[-500:])


def verificar_e_aplicar() -> bool:
    """Procura versao nova e instala. Devolve True se atualizou. Nunca levanta erro."""
    try:
        sha = ultima_versao()
        if sha == versao_local():
            return False
        print("Baixando atualizacao do Meu Estudio...")
        mudaram = _aplicar(sha)
        if "requirements.txt" in mudaram:
            print("Instalando o que a versao nova precisa...")
            _instalar_dependencias()
        ARQ_VERSAO.write_text(sha, encoding="utf-8")
        log.info("Atualizado para %s (%d arquivos).", sha[:7], len(mudaram))
        print(f"Meu Estudio atualizado ({len(mudaram)} arquivos).")
        return bool(mudaram)
    except Exception as e:  # noqa: BLE001 - sem internet etc.: segue com a versao atual
        log.warning("Nao consegui procurar atualizacao: %s", e)
        print("Nao consegui procurar atualizacao agora; abrindo a versao atual.")
        return False


if __name__ == "__main__":
    verificar_e_aplicar()

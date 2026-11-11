"""Agenda (ou cancela/remove) um post na caixa de entrada do Meu Estudio (branch `caixa` no GitHub).

O app no PC do usuario confere a caixa a cada minuto e publica com o proprio token.

Exemplos:
  python agendar_caixa.py agendar --id nmecha-2026-11-11 --midia foto.webp \
      --legenda legenda.txt --quando 2026-11-11T14:00 [--collabs amigo,outro] [--tipo foto|reel]
  python agendar_caixa.py cancelar --id nmecha-2026-11-11
  python agendar_caixa.py remover --id nmecha-2026-11-11      # depois de publicado
  python agendar_caixa.py listar
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime
from pathlib import Path

REPO = "henrikenaegele1981/meu-projeto"
BRANCH = "caixa"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"
AUTOR = ["-c", "user.name=henrikenaegele1981",
         "-c", "user.email=henrikenaegele1981@users.noreply.github.com"]
RODAPE = ("\n\nCo-Authored-By: Claude <noreply@anthropic.com>")


def git(*args: str, cwd: Path) -> str:
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def clonar() -> Path:
    pasta = Path(tempfile.mkdtemp(prefix="caixa-"))
    git("clone", "-q", "--depth", "1", "-b", BRANCH, f"https://github.com/{REPO}", str(pasta), cwd=pasta.parent)
    return pasta


def ler_fila(pasta: Path) -> list[dict]:
    arq = pasta / "fila.json"
    return json.loads(arq.read_text(encoding="utf-8")) if arq.exists() else []


def gravar_e_enviar(pasta: Path, fila: list[dict], mensagem: str) -> None:
    (pasta / "fila.json").write_text(json.dumps(fila, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    git("add", "-A", cwd=pasta)
    if not git("status", "--porcelain", cwd=pasta).strip():
        print("Nada mudou na caixa.")
        return
    git(*AUTOR, "commit", "-q", "-m", mensagem + RODAPE, cwd=pasta)
    for tentativa in range(4):
        try:
            git("push", "-q", "origin", BRANCH, cwd=pasta)
            return
        except subprocess.CalledProcessError:
            time.sleep(2 ** (tentativa + 1))
    raise SystemExit("Não consegui enviar para o GitHub.")


def preparar_foto(origem: Path, destino: Path) -> None:
    """Converte para JPEG e confere a proporcao aceita no feed (4:5 ate 1,91:1)."""
    try:
        from PIL import Image
    except ImportError:
        if origem.suffix.lower() not in (".jpg", ".jpeg"):
            raise SystemExit("Instale o Pillow (pip install pillow) ou use uma imagem .jpg.")
        shutil.copy(origem, destino)
        return
    im = Image.open(origem)
    largura, altura = im.size
    proporcao = largura / altura
    if not 0.79 <= proporcao <= 1.92:
        raise SystemExit(f"A imagem tem {largura}x{altura}; o feed aceita de 4:5 (1080x1350) a 1,91:1. Recorte antes.")
    if im.mode != "RGB":
        fundo = Image.new("RGB", im.size, (255, 255, 255))
        fundo.paste(im, mask=im.convert("RGBA").split()[-1])
        im = fundo
    if largura > 1440:
        im = im.resize((1440, round(1440 / proporcao)))
    im.save(destino, "JPEG", quality=92)


def esperar_publico(url: str, conferir) -> bool:
    for _ in range(12):
        try:
            with urllib.request.urlopen(f"{url}?t={time.time_ns()}", timeout=20) as r:
                if conferir(r.read()):
                    return True
        except Exception:  # noqa: BLE001 - CDN do GitHub ainda nao atualizou
            pass
        time.sleep(5)
    return False


def agendar(a: argparse.Namespace) -> None:
    datetime.fromisoformat(a.quando)  # valida o formato AAAA-MM-DDTHH:MM
    legenda = Path(a.legenda).read_text(encoding="utf-8").strip() if Path(a.legenda).exists() else a.legenda
    if len(legenda) > 2200:
        raise SystemExit(f"A legenda tem {len(legenda)} caracteres; o limite do Instagram é 2.200.")
    pasta = clonar()
    fila = ler_fila(pasta)
    if any(i["id"] == a.id for i in fila):
        raise SystemExit(f"Já existe um post com id {a.id}. Use outro id (o app nunca reimporta um id).")
    tipo = a.tipo or ("reel" if Path(a.midia).suffix.lower() in (".mp4", ".mov") else "foto")
    nome = f"{a.id}{'.mp4' if tipo == 'reel' else '.jpg'}"
    if tipo == "reel":
        shutil.copy(a.midia, pasta / nome)
    else:
        preparar_foto(Path(a.midia), pasta / nome)
    fila.append({"id": a.id, "tipo": tipo, "quando": a.quando, "legenda": legenda,
                 "midia": f"{RAW}/{nome}",
                 "collabs": [c.strip().lstrip("@") for c in (a.collabs or "").split(",") if c.strip()][:3],
                 "cancelado": False})
    gravar_e_enviar(pasta, fila, f"Caixa: agenda {a.id} para {a.quando}")
    ok = esperar_publico(f"{RAW}/fila.json", lambda b: a.id.encode() in b) and \
        esperar_publico(f"{RAW}/{nome}", lambda b: len(b) > 1000)
    print(("OK: " if ok else "ENVIADO, mas o link público ainda não respondeu: ") +
          f"{a.id} ({tipo}) para {a.quando}, {len(legenda)} caracteres. Mídia: {RAW}/{nome}")


def cancelar(a: argparse.Namespace) -> None:
    pasta = clonar()
    fila = ler_fila(pasta)
    for item in fila:
        if item["id"] == a.id:
            item["cancelado"] = True
    gravar_e_enviar(pasta, fila, f"Caixa: cancela {a.id}")
    print(f"{a.id} marcado como cancelado (o app tira da Agenda em até 1 minuto, se ainda não saiu).")


def remover(a: argparse.Namespace) -> None:
    pasta = clonar()
    fila = [i for i in ler_fila(pasta) if i["id"] != a.id]
    for arq in pasta.glob(f"{a.id}.*"):
        arq.unlink()
    gravar_e_enviar(pasta, fila, f"Caixa: remove {a.id} (já publicado)")
    print(f"{a.id} removido da caixa.")


def listar(_: argparse.Namespace) -> None:
    for i in ler_fila(clonar()):
        print(f"{i['id']:30} {i['tipo']:5} {i['quando']}  {'CANCELADO' if i.get('cancelado') else ''}")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="acao", required=True)
    ag = sub.add_parser("agendar")
    ag.add_argument("--id", required=True, help="nome único, ex.: assunto-AAAA-MM-DD")
    ag.add_argument("--midia", required=True, help="imagem (.jpg/.png/.webp) ou vídeo (.mp4/.mov)")
    ag.add_argument("--legenda", required=True, help="arquivo .txt (UTF-8) ou o próprio texto")
    ag.add_argument("--quando", required=True, help="horário de Brasília, AAAA-MM-DDTHH:MM")
    ag.add_argument("--collabs", default="")
    ag.add_argument("--tipo", choices=["foto", "reel"])
    for nome in ("cancelar", "remover"):
        sub.add_parser(nome).add_argument("--id", required=True)
    sub.add_parser("listar")
    a = p.parse_args()
    {"agendar": agendar, "cancelar": cancelar, "remover": remover, "listar": listar}[a.acao](a)


if __name__ == "__main__":
    main()

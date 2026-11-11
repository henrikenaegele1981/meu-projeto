#!/usr/bin/env bash
# Baixa um Reel/TikTok/YouTube de referência, gera a folha de quadros e transcreve a fala.
# Uso: bash baixar_referencia.sh URL NOME [PASTA]
# Saída: PASTA/NOME.mp4, NOME.info.json, folha_NOME.jpg (1 quadro a cada 6 s), NOME.txt (transcrição)
set -euo pipefail
URL="$1"; NOME="$2"; PASTA="${3:-ref}"; AQUI="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$PASTA"; cd "$PASTA"
for i in 1 2 3; do
  if python3 -m yt_dlp --no-warnings -q -f "bv*+ba/b" --merge-output-format mp4 --write-info-json -o "$NOME.%(ext)s" "$URL" 2>err.txt; then break; fi
  echo "tentativa $i falhou: $(tail -c 160 err.txt)"; [ "$i" = 3 ] && exit 1; sleep 120   # Instagram limita acesso anônimo: espere e tente de novo
done
python3 - "$NOME" <<'PY'
import json, sys
d = json.load(open(sys.argv[1] + ".info.json"))
print("canal:", d.get("uploader"), "| curtidas:", d.get("like_count"), "| duração:", d.get("duration"))
print("legenda:", (d.get("description") or "")[:400].replace("\n", " / "))
PY
ffmpeg -v error -y -i "$NOME.mp4" -vf "fps=1/6,scale=216:-1,tile=10x3" -frames:v 1 "folha_$NOME.jpg"
"${VENV_PY:-/tmp/claude-0/voz/.venv/bin/python}" "$AQUI/transcrever.py" "$NOME.mp4"
echo "pronto: $PASTA/folha_$NOME.jpg e $PASTA/$NOME.txt"

#!/usr/bin/env bash
# Prepara uma pasta de trabalho para um vídeo novo (rode uma vez por sessão/pasta).
# Uso: bash preparar_ambiente.sh PASTA_DO_VIDEO
# Instala: d3, mapas do mundo, fontes (Inter etc.) via npm na pasta; yt-dlp; Python 3.11 com faster-whisper.
# Requer rede para npm/PyPI/Hugging Face (o ambiente "meu-projeto" tem internet liberada).
set -euo pipefail
PASTA="$1"; AQUI="$(cd "$(dirname "$0")" && pwd)"; SKILL="$(dirname "$AQUI")"
mkdir -p "$PASTA"; cd "$PASTA"
[ -f package.json ] || npm init -y >/dev/null
npm i -s d3@7 topojson-client@3 world-atlas@2 @fontsource/inter@5 @fontsource/montserrat@5 >/dev/null 2>&1
cp "$AQUI"/quadros.js "$AQUI"/render_par.js "$AQUI"/alinhar.py .
cp -n "$SKILL"/assets/modelo-jose.html video.html
python3 -m yt_dlp --version >/dev/null 2>&1 || pip install -q --break-system-packages -U yt-dlp
VENV=/tmp/claude-0/voz/.venv
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m pip install -q --break-system-packages uv >/dev/null 2>&1 || true
  ~/.local/bin/uv venv -q -p 3.11 "$VENV"
fi
"$VENV/bin/python" -c "import faster_whisper" 2>/dev/null || ~/.local/bin/uv pip install -q -p "$VENV/bin/python" faster-whisper
fc-list | grep -qi "Noto Color Emoji" || echo "AVISO: sem fonte de emoji colorido (apt-get install fonts-noto-color-emoji)"
echo "pronto em $PASTA: video.html (modelo do José), quadros.js, render_par.js, alinhar.py"
echo "Python com Whisper: $VENV/bin/python  (exporte VENV_PY=$VENV/bin/python para os outros scripts)"

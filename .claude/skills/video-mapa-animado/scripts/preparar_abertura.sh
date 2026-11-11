#!/usr/bin/env bash
# Prepara o trecho de vídeo de terceiro que abre o vídeo (ex.: fala de um político).
# Uso: bash preparar_abertura.sh clip.mp4 DURACAO_SEG [CORTE_ALTURA] [PASTA]
#   CORTE_ALTURA: fração da altura a manter a partir do topo (padrão 0.60), para tirar legendas queimadas
#                 que o vídeo original costuma ter no meio/baixo. Confira na folha de quadros antes.
# Saída: PASTA/f_0001.jpg… (30 fps, 720 px de largura), PASTA/palavras.json (tempo de cada palavra),
#        PASTA/audio.wav. No modelo, preencha CFG.abertura.total com o número de quadros e dur com a duração.
set -euo pipefail
CLIP="$1"; DUR="$2"; CORTE="${3:-0.60}"; PASTA="${4:-abertura}"
mkdir -p "$PASTA"
ffmpeg -v error -y -i "$CLIP" -t "$DUR" -vf "fps=30,crop=iw:ih*$CORTE:0:0,scale=720:-2" -q:v 3 "$PASTA/f_%04d.jpg"
ffmpeg -v error -y -i "$CLIP" -t "$DUR" -vn -ar 48000 -ac 2 "$PASTA/audio.wav"
"${VENV_PY:-/tmp/claude-0/voz/.venv/bin/python}" - "$CLIP" "$PASTA/palavras.json" <<'PY'
import json, sys
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, _ = m.transcribe(sys.argv[1], language="pt", word_timestamps=True)
w = [{"w": x.word.strip(), "ini": round(x.start, 3), "fim": round(x.end, 3)} for s in segs for x in s.words if x.word.strip()]
json.dump(w, open(sys.argv[2], "w"), ensure_ascii=False)
print(" ".join(f"{x['w']}({x['ini']})" for x in w))
PY
echo "quadros: $(ls "$PASTA"/f_*.jpg | wc -l)  (use esse número em CFG.abertura.total)"

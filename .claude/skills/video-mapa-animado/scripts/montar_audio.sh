#!/usr/bin/env bash
# Monta o áudio final: [abertura] + narração do ElevenLabs + trilha de fundo com "ducking"
# (a trilha abaixa sozinha quando a voz fala e volta nas pausas).
# Uso: bash montar_audio.sh narracao.mp3 saida.wav [abertura.wav DUR_ABERTURA] [trilha.(mp3|mp4|wav) VOLUME]
#   Sem abertura, passe "" 0. DUR_ABERTURA: segundos da abertura (a narração entra 0,35 s depois, igual ao modelo).
#   VOLUME: volume base da trilha (padrão 0.22). A trilha repete em loop até o fim.
# Trocar só o áudio de um vídeo já renderizado (sem renderizar de novo):
#   ffmpeg -i video.mp4 -i saida.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest final.mp4
set -euo pipefail
NARR="$1"; SAIDA="$2"; AB="${3:-}"; DAB="${4:-0}"; TRILHA="${5:-}"; VOL="${6:-0.22}"
ATRASO=$(python3 -c "print(int((float('$DAB')+0.35)*1000) if '$AB' else 300)")
DN=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$NARR")
DUR=$(python3 -c "print(round($DN+$ATRASO/1000+2.5,2))")
ENTR=(-i "$NARR")
FIL="[0:a]aresample=48000,adelay=${ATRASO}|${ATRASO},apad,atrim=0:${DUR}[voz];"
VOZ="[voz]"; AB_ROT=""; N=1
if [ -n "$AB" ]; then
  ENTR+=(-i "$AB")
  FIL+="[$N:a]aresample=48000,atrim=0:${DAB},afade=t=out:st=$(python3 -c "print(max(0,$DAB-0.25))"):d=0.25[ab];"
  AB_ROT="[ab]"; N=$((N+1))
fi
if [ -n "$TRILHA" ]; then
  ENTR+=(-stream_loop -1 -i "$TRILHA")
  FIL+="[$N:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:${DUR},volume=${VOL},afade=t=in:d=1.5,afade=t=out:st=$(python3 -c "print($DUR-2.5)"):d=2.5[tr];"
  FIL+="[voz]asplit=2[voz1][vozsc];[tr][vozsc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[trd];"
  MIX="[voz1]${AB_ROT}[trd]"
else
  MIX="[voz]${AB_ROT}"
fi
NIN=$(echo "$MIX" | grep -o '\[' | wc -l)
FIL+="${MIX}amix=inputs=${NIN}:duration=longest:normalize=0,alimiter=limit=0.95[a]"
ffmpeg -v error -y "${ENTR[@]}" -filter_complex "$FIL" -map "[a]" -ac 2 -t "$DUR" "$SAIDA"
echo "áudio: $SAIDA ($(ffprobe -v error -show_entries format=duration -of csv=p=0 "$SAIDA") s)"

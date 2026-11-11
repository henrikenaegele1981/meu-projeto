"""Alinha o áudio do ElevenLabs ao texto do roteiro: tempo de cada palavra e de cada parágrafo (cena)."""
import json, re, sys, difflib, unicodedata
from faster_whisper import WhisperModel
roteiro_md, audio, saida = sys.argv[1:4]
s = open(roteiro_md, encoding="utf-8").read()
# Narração: arquivo .txt inteiro; ou, num .md, o primeiro bloco ```text ... ```; ou o trecho entre
# "## Parte 1" e "## Parte 2" (formato dos roteiros entregues ao usuário).
if roteiro_md.endswith(".txt"):
    texto = s.strip()
elif "```text" in s:
    texto = s.split("```text", 1)[1].split("```", 1)[0].strip()
else:
    ini = s.index("## Parte 1"); ini = s.index("\n\n", ini)
    texto = s[ini:s.index("## Parte 2")].replace("---", "").strip()
pars = [p.strip() for p in texto.split("\n\n") if p.strip()]
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = m.transcribe(audio, language="pt", word_timestamps=True, initial_prompt=texto[:600])
ouv = [{"w": w.word.strip(), "ini": w.start, "fim": w.end} for sg in segs for w in sg.words if w.word.strip()]
norm = lambda x: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFD", x.lower()).encode("ascii", "ignore").decode())
rot = [(i, w) for i, p in enumerate(pars) for w in p.split()]
sm = difflib.SequenceMatcher(None, [norm(w) for _, w in rot], [norm(o["w"]) for o in ouv], autojunk=False)
t = [None] * len(rot)
for a, b, n in sm.get_matching_blocks():
    for k in range(n): t[a + k] = (ouv[b + k]["ini"], ouv[b + k]["fim"])
ok = sum(1 for x in t if x)
for j in range(len(rot)):
    if t[j] is None:
        ant = next((t[k][1] for k in range(j - 1, -1, -1) if t[k]), 0.0)
        pk = next((k for k in range(j + 1, len(rot)) if t[k]), None)
        prox = t[pk][0] if pk is not None else info.duration
        falt = (pk if pk is not None else len(rot)) - j
        passo = max(prox - ant, 0.1) / (falt + 1)
        t[j] = (ant + passo * 0.5, ant + passo)
palavras = [{"w": w, "ini": round(a, 3), "fim": round(b, 3), "p": i} for (i, w), (a, b) in zip(rot, t)]
cenas = []
for i, p in enumerate(pars):
    ws = [x for x in palavras if x["p"] == i]
    cenas.append({"ini": ws[0]["ini"], "fala": p})
for i, c in enumerate(cenas):
    c["fim"] = cenas[i + 1]["ini"] if i + 1 < len(cenas) else info.duration + 2.5
json.dump({"cenas": cenas, "palavras": palavras, "duracao": info.duration + 2.5}, open(saida, "w"), ensure_ascii=False, indent=1)
print(f"{len(pars)} parágrafos, {len(rot)} palavras, {ok} casadas com o áudio, duração {info.duration:.1f}s")

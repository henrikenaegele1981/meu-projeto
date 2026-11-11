import sys
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
for f in sys.argv[1:]:
    segs, _ = m.transcribe(f, language="pt", vad_filter=True)
    with open(f.rsplit(".",1)[0] + ".txt", "w", encoding="utf-8") as out:
        for s in segs:
            out.write(f"[{s.start:6.1f}-{s.end:6.1f}] {s.text.strip()}\n")
    print("ok", f)

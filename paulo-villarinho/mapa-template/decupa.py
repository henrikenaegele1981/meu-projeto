import numpy as np, json, subprocess
db=np.load('db.npy'); DUR=56.738
cuts=[(0.00,0.70),(1.27,2.17),(3.13,3.74),(9.53,9.78),(4.45,5.15),(7.86,8.22),(10.54,11.98),(19.03,19.42),(36.72,38.02),(45.44,46.12),(20.80,21.08)]
def snap(t,lo,hi):
    a=max(0,int((t+lo)*100));b=min(len(db)-1,int((t+hi)*100))
    return (a+int(np.argmin(db[a:b+1])))/100
cuts=sorted(cuts)
ref=[]
for s,e in cuts:
    s2 = 0.0 if s==0 else snap(s,-0.04,0.08); e2=snap(e,-0.08,0.03)
    ref.append((s2,e2))
keep=[];prev=0
for s,e in ref:
    if s>prev: keep.append((prev,s))
    prev=e
keep.append((prev,DUR))
print('cortes',ref); 
newdur=sum(b-a for a,b in keep);print('duração nova',round(newdur,2))
json.dump(keep,open('keep.json','w'))
f=[];labels=[]
for i,(a,b) in enumerate(keep):
    f.append(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={b-a-0.015:.3f}:d=0.015[s{i}]");labels.append(f"[s{i}]")
fc=";".join(f)+";"+"".join(labels)+f"concat=n={len(keep)}:v=0:a=1,highpass=f=70,afftdn=nf=-42:nr=12,agate=threshold=0.012:ratio=3:attack=5:release=120,loudnorm=I=-14:TP=-1.5:LRA=7[out]"
subprocess.run(["ffmpeg","-loglevel","error","-y","-i","narracao.mp3","-filter_complex",fc,"-map","[out]","-ar","48000","narracao-limpa.wav"],check=True)

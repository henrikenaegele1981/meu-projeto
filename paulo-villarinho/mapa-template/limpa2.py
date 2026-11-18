import json,subprocess,wave,numpy as np,sys
src,stt,out=sys.argv[1:4]
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",src,"-ac","1","-ar","44100","m.wav"],check=True)
w=wave.open('m.wav');x=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768;DUR=len(x)/44100
h=441;db=20*np.log10(np.array([np.sqrt(np.mean(x[i:i+h]**2)+1e-12) for i in range(0,len(x)-h,h)]))
W=[w for w in json.load(open(stt))['words'] if w['type']!='spacing']
cuts=[]
for a,b in zip(W,W[1:]):
    g=b['start']-a['end']
    if g>0.42: cuts.append((a['end']+0.18,b['start']-0.14))
cuts+= [tuple(map(float,c.split(':'))) for c in sys.argv[4:]]
def snap(t,lo,hi):
    i=max(0,int((t+lo)*100));j=min(len(db)-1,int((t+hi)*100));return (i+int(np.argmin(db[i:j+1])))/100
cuts=sorted((snap(s,-0.05,0.05),snap(e,-0.05,0.05)) for s,e in cuts)
keep=[];prev=max(0,W[0]['start']-0.08)
for s,e in cuts:
    if s>prev: keep.append((prev,s))
    prev=max(prev,e)
keep.append((prev,min(DUR,W[-1]['end']+0.4)))
f=[];L=[]
for i,(a,b) in enumerate(keep):
    f.append(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.012,afade=t=out:st={max(0,b-a-0.015):.3f}:d=0.015[s{i}]");L.append(f"[s{i}]")
fc=";".join(f)+";"+"".join(L)+f"concat=n={len(keep)}:v=0:a=1,highpass=f=70,afftdn=nf=-45:nr=8,loudnorm=I=-14:TP=-1.5:LRA=7[o]"
subprocess.run(["ffmpeg","-loglevel","error","-y","-i",src,"-filter_complex",fc,"-map","[o]","-ar","48000",out],check=True)
print(len(cuts),'cortes; duração',round(sum(b-a for a,b in keep),2))

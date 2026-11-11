import json, sys, urllib.request, urllib.parse, time
UA={"User-Agent":"Mozilla/5.0 (compatible; video-editorial/1.0)"}
def busca(q,n=8):
    u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({"q":q,"page_size":n,"license_type":"commercial,modification","mature":"false"})
    with urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30) as r: d=json.load(r)
    return [{"titulo":x.get("title"),"url":x.get("url"),"w":x.get("width"),"h":x.get("height"),"fonte":x.get("source"),
             "credito":f'{(x.get("creator") or "autor desconhecido")[:40]} · {x.get("license","").upper()} {x.get("license_version") or ""} · {x.get("source")}'} for x in d.get("results",[])]
res={}
for k,q in json.loads(sys.argv[1]).items():
    try: res[k]=busca(q)
    except Exception as e: res[k]=[{"erro":str(e)}]
    time.sleep(1.5)
json.dump(res,open("busca_fotos.json","w"),ensure_ascii=False,indent=1)
for k,v in res.items():
    print("==",k); [print("  ",(x.get("titulo") or "")[:55],x.get("w"),"x",x.get("h"),"|",x.get("credito","")[:60],"|",x.get("erro","")) for x in v[:5]]

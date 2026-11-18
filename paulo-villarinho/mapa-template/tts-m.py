import json,urllib.request,base64,ssl,sys
B=json.load(open('blocks.json'))
text="\n\n".join(B)
body=json.dumps({"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.5,"similarity_boost":0.75,"style":0.1,"use_speaker_boost":True}}).encode()
req=urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/bJrNspxJVFovUxNBQ0wh/with-timestamps?output_format=mp3_44100_192",data=body,headers={"xi-api-key":"proxy-injected","Content-Type":"application/json"})
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
try: r=json.load(urllib.request.urlopen(req,context=ctx,timeout=180))
except urllib.error.HTTPError as e: print(e.code,e.read()[:500]);sys.exit(1)
open('narracao-marcelo.mp3','wb').write(base64.b64decode(r['audio_base64']))
al=r['alignment'];json.dump(al,open('align-m.json','w'))
starts=[];pos=0
for b in B:
    i=text.index(b,pos);starts.append(al['character_start_times_seconds'][i]);pos=i+len(b)
print("starts",[round(s,2) for s in starts],"end",round(al['character_end_times_seconds'][-1],2))
json.dump(starts,open('starts-m.json','w'))

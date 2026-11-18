import json,urllib.request,base64,ssl,sys
text,out,prev,nxt,speed=sys.argv[1:6]
d={"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.5,"similarity_boost":0.75,"style":0.1,"use_speaker_boost":True,"speed":float(speed)}}
if prev: d["previous_text"]=prev
if nxt: d["next_text"]=nxt
req=urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/bJrNspxJVFovUxNBQ0wh?output_format=mp3_44100_192",data=json.dumps(d).encode(),headers={"xi-api-key":"proxy-injected","Content-Type":"application/json"})
open(out,'wb').write(urllib.request.urlopen(req,context=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt"),timeout=120).read())

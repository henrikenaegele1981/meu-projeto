import json,urllib.request,ssl,sys
B=json.load(open('blocks.json'));text="\n\n".join(B)
d={"text":text,"model_id":"eleven_multilingual_v2","voice_settings":{"stability":0.55,"similarity_boost":0.8,"style":0.1,"use_speaker_boost":True,"speed":1.0}}
req=urllib.request.Request("https://api.elevenlabs.io/v1/text-to-speech/SlkxMsaHrKW7FqWihl4o?output_format=mp3_44100_192",data=json.dumps(d).encode(),headers={"xi-api-key":"proxy-injected","Content-Type":"application/json"})
open(sys.argv[1],'wb').write(urllib.request.urlopen(req,context=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt"),timeout=180).read())

const {chromium}=require('playwright'),http=require('http'),fs=require('fs'),path=require('path');
const [,,pagina,saida,...tempos]=process.argv;
const srv=http.createServer((q,r)=>{const f=path.join(__dirname,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);return r.end();}r.writeHead(200,{'Content-Type':f.endsWith('.html')?'text/html':f.endsWith('.json')?'application/json':f.endsWith('.woff2')?'font/woff2':'text/javascript'});r.end(d);});}).listen(8766);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('pageerror',e=>console.log('ERRO',e.message));
await p.goto('http://127.0.0.1:8766/'+pagina);await p.waitForFunction('window.pronto',null,{timeout:20000});await p.evaluate(()=>document.fonts.ready);
for(const t of tempos){await p.evaluate(t=>render(t),+t);await p.screenshot({path:`${saida}_${t}.jpg`,type:'jpeg',quality:85});}
await b.close();srv.close();})();

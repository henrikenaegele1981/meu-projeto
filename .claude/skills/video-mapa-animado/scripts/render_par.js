// Renderiza em paralelo: node render_par.js pagina.html saida.mp4 audio.wav [workers]
const {chromium}=require('playwright'),http=require('http'),fs=require('fs'),path=require('path'),{execSync}=require('child_process');
const [,,pagina,saida,audio,nw='4']=process.argv; const FPS=30, W=+nw, dir=path.join(__dirname,'q_'+path.basename(saida,'.mp4'));
const tipos={'.html':'text/html','.json':'application/json','.woff2':'font/woff2','.jpg':'image/jpeg','.png':'image/png','.js':'text/javascript'};
const srv=http.createServer((q,r)=>{const f=path.join(__dirname,decodeURIComponent(q.url.split('?')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);return r.end();}r.writeHead(200,{'Content-Type':tipos[path.extname(f)]||'application/octet-stream'});r.end(d);});}).listen(8768);
(async()=>{ fs.rmSync(dir,{recursive:true,force:true}); fs.mkdirSync(dir);
  const b=await chromium.launch(); const abre=async()=>{const p=await b.newPage({viewport:{width:1080,height:1920}}); p.on('pageerror',e=>console.log('ERRO',e.message));
    await p.goto('http://127.0.0.1:8768/'+pagina); await p.waitForFunction('window.pronto',null,{timeout:30000}); await p.evaluate(()=>document.fonts.ready); return p;};
  const p0=await abre(); const dur=await p0.evaluate(()=>window.DURACAO); const n=Math.round(dur*FPS); const ps=[p0]; for(let i=1;i<W;i++) ps.push(await abre());
  let feitos=0; const t0=Date.now();
  await Promise.all(ps.map(async(p,w)=>{ for(let i=w;i<n;i+=W){ await p.evaluate(t=>render(t),i/FPS); await p.screenshot({path:`${dir}/${String(i).padStart(5,'0')}.jpg`,type:'jpeg',quality:90}); if(++feitos%600===0) console.log('quadros',feitos,'/',n, Math.round((Date.now()-t0)/1000)+'s'); } }));
  await b.close(); srv.close();
  execSync(`ffmpeg -v error -y -framerate ${FPS} -i ${dir}/%05d.jpg -i ${audio} -filter_complex "[1:a]apad[a]" -map 0:v -map "[a]" -c:v libx264 -preset medium -crf 21 -maxrate 6M -bufsize 12M -pix_fmt yuv420p -c:a aac -b:a 192k -t ${dur} ${saida}`);
  fs.rmSync(dir,{recursive:true,force:true}); console.log('ok',saida,dur.toFixed(1)+'s', Math.round((Date.now()-t0)/1000)+'s de render'); })();

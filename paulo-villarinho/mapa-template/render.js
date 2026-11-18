const {chromium}=require('playwright');
const [dir,w,n]=[process.argv[2],+process.argv[3],+process.argv[4]];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+dir+'/mapa/index.html');const D=await p.evaluate(()=>DUR);const F=Math.round(D*30);
for(let f=w;f<F;f+=n){await p.evaluate(t=>render(t),f/30);await p.screenshot({path:`${dir}/frames/f${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92});}
await b.close();})();

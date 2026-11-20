const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
p.on('console',m=>console.log('console',m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('http://127.0.0.1:8765/index.html');await p.evaluate(()=>window.ready);
for(const t of process.argv.slice(2)){await p.evaluate(t=>window.renderAt(t),+t);await p.screenshot({path:`test/t_${t}.jpg`,type:'jpeg',quality:80});}
await b.close();})();

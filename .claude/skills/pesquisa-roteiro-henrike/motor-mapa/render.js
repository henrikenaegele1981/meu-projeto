const {chromium}=require('playwright');
const [,,from,to,out,port]=process.argv;
(async()=>{const b=await chromium.launch({args:['--disable-web-security','--allow-file-access-from-files']});
 const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:1});
 await p.goto(`http://127.0.0.1:${port||8765}/index.html`);await p.evaluate(()=>window.ready);
 for(let f=+from;f<+to;f++){await p.evaluate(t=>window.renderAt(t),f/30);
   await p.screenshot({path:`${out}/${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:93});}
 await b.close();})();

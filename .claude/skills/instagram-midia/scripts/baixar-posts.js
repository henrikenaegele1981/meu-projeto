// Uso: node baixar-posts.js <pasta-de-saida>
// Lê <pasta>/codes.json (gerado por listar-posts.js), abre a página pública de
// incorporação de cada post (/p/<código>/embed/captioned/) e baixa as imagens,
// inclusive as de dentro dos carrosséis, em <pasta>/posts/<código>-<n>.jpg.
// Obs.: o HTML do embed também traz imagens de posts relacionados; confira a grade.
const { chromium } = require('playwright');
const fs = require('fs');
const out = process.argv[2];
if (!out) { console.error('uso: node baixar-posts.js <pasta>'); process.exit(1); }
const codes = JSON.parse(fs.readFileSync(`${out}/codes.json`));
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 540, height: 900 } });
  fs.mkdirSync(`${out}/posts`, { recursive: true });
  for (const code of codes) {
    const p = await ctx.newPage();
    try {
      await p.goto(`https://www.instagram.com/p/${code}/embed/captioned/`, { waitUntil: 'networkidle', timeout: 45000 });
      await p.waitForTimeout(1000);
      const html = await p.content();
      const urls = [...new Set([...html.matchAll(/https:\\?\/\\?\/[a-z0-9.-]*cdninstagram\.com\\?\/v\\?\/t51\.[^"'\s)]+/g)]
        .map((m) => m[0].replace(/\\\//g, '/').replace(/&amp;/g, '&').replace(/\\u0026/g, '&')))]
        .filter((u) => !u.includes('s150x150') && !u.includes('t51.82787-19') && !u.includes('t51.2885-19'));
      const legenda = (await p.$eval('.Caption', (e) => e.innerText).catch(() => '')).slice(0, 140).replace(/\n/g, ' ');
      let n = 0;
      const vistos = new Set();
      for (const u of urls) {
        const id = (u.match(/\/(\d+_\d+_\d+_n)\./) || [])[1];
        if (!id || vistos.has(id)) continue;
        vistos.add(id);
        const r = await ctx.request.get(u);
        if (r.status() !== 200) continue;
        const buf = await r.body();
        if (buf.length < 15000) continue;
        fs.writeFileSync(`${out}/posts/${code}-${n++}.jpg`, buf);
      }
      console.log(code, 'imagens:', n, '|', legenda);
    } catch (e) { console.log(code, 'erro', e.message.slice(0, 80)); }
    await p.close();
  }
  await b.close();
})();

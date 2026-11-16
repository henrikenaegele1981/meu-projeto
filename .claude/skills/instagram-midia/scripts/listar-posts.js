// Uso: node listar-posts.js <perfil> <pasta-de-saida>
// Abre o perfil público no Chromium (sem login), rola a página e salva os códigos
// dos posts visíveis (normalmente os 3 fixados + 9 recentes) em <pasta>/codes.json.
const { chromium } = require('playwright');
const fs = require('fs');
const [perfil, out] = process.argv.slice(2);
if (!perfil || !out) { console.error('uso: node listar-posts.js <perfil> <pasta>'); process.exit(1); }
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 }, locale: 'pt-BR',
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36' });
  const p = await ctx.newPage();
  await p.goto(`https://www.instagram.com/${perfil}/`, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await p.waitForTimeout(4000);
  const codes = new Set();
  for (let i = 0; i < 8; i++) {
    (await p.$$eval('a[href*="/p/"], a[href*="/reel/"]', (xs) => xs.map((x) => x.getAttribute('href'))))
      .forEach((h) => codes.add(h.split('/').filter(Boolean).slice(-1)[0]));
    await p.mouse.wheel(0, 2500);
    await p.waitForTimeout(1500);
  }
  await p.screenshot({ path: `${out}/perfil.png` });
  fs.writeFileSync(`${out}/codes.json`, JSON.stringify([...codes]));
  console.log('posts encontrados:', codes.size, JSON.stringify([...codes]));
  await b.close();
})();

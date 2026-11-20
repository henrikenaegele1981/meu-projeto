# Formato: Reel de mapa animado

Modelo validado: Reel "Trump, Putin e Xi em Shenzhen" (nov/2026), feito a partir da referência @worldhistorynetwork3106 ("A New Yalta?"). O código pronto está em `../motor-mapa/`.

## Visual
- **Fundo:** mapa de satélite diurno. Use o Natural Earth `NE1_HR_LC_SR_W` (21600×10800, domínio público), cortado em 8 blocos de 6000 px, mais uma versão de 4096 px para os planos abertos.
- **País em destaque:** magenta `#c4189a` com contorno branco. Contornos do Natural Earth `ne_50m_admin_0_countries.geojson`, pelo campo `ADM0_A3`.
- **Câmera:** viaja entre países e cidades, com zoom suave (interpolação em escala logarítmica). Pinos pulsando nas cidades e rotas tracejadas.
- **Cartões escuros:** fundo `#0b0d17` com gradiente; etiqueta vermelha no topo (kicker); título em caixa alta Poppins 800/900; palavra ou número grande colorido embaixo.
- **Retratos em círculo** com anel colorido nas cores do país, e o nome numa etiqueta embaixo.
- **Prova na tela:**
  - print da manchete numa moldura branca inclinada, com "Reprodução: veículo · data";
  - vídeo em moldura arredondada, com "Vídeo: fonte";
  - foto com "Foto: fonte (licença)".
- **Carimbos:** NÃO PROCEDE, MEIA VERDADE, FALA DE UM, NÃO EXISTE, e um verde para o que é confirmado.
- **Legenda queimada:** branca, de 2 a 3 palavras, Poppins 800 com contorno preto, sincronizada palavra por palavra.
- **Selo fixo** com a foto e o @ do perfil, no rodapé da área segura, nunca no topo.
- **Movimento a cada 5 segundos.**

## Área segura (1080×1920)
- Nada nos 250 px do topo nem nos 480 px de baixo.
- Margem esquerda de pelo menos 70 px.
- Da metade da tela para baixo, deixar 160 px livres à direita.
- Conteúdo principal entre y 270 e y 1150. Legenda em y ≈ 1190. Selo em y ≈ 1316.

## Material
- **Vídeo e foto reais, com crédito.**
  - Fotos do Kremlin: CC BY 4.0, crédito "Kremlin.ru".
  - Casa Branca: domínio público.
  - Reagan Library: domínio público.
  - Wikimedia Commons: conferir a licença de cada arquivo.
  - Vídeo oficial: canais públicos, com crédito (ex.: "Vídeo: CGTN").
- **Imagem de IA nunca passa por real.** O próprio Reel de referência usava uma imagem de IA dos três líderes à mesa, publicada antes do encontro.
- **Prints:** Playwright, com viewport de celular ou 1080 de largura. Feche os banners e recorte só a manchete e o subtítulo.
- **Vídeo:** extraia os quadros a 30 fps (`ffmpeg -vf fps=30,scale=1280:-2`) e registre em `assets/video/frames.json` no formato `{nome:{n,dir}}`.

## Sincronia
1. **Áudio:** de preferência gerado pelo Henrike no ElevenLabs (modelo v4 no painel dele).
2. **Transcrição:** passe o áudio pelo speech-to-text do ElevenLabs (scribe_v1) para obter o tempo de cada palavra.
3. **Legendas:** agrupe de 2 a 3 palavras, quebrando na pontuação, e salve em `captions.json`.
4. **Cenas:** cada uma começa no tempo da frase que a pede. Monte a lista de cenas (#, tempo, narração, o que aparece, material) e peça aprovação antes de renderizar.

## Renderização
1. **Servidor local:** `python3 -m http.server 8765` na pasta do motor.
2. **Quadros de teste:** `node snap.js 1.5 8 15 …` gera os quadros em `test/`. Monte uma folha de contato e confira antes do render final.
3. **Render completo:** 4 processos em paralelo, com `node render.js <inicio> <fim> frames 8765`.
4. **Encode:** `ffmpeg -framerate 30 -i frames/%05d.jpg -i narracao.mp3 -c:v libx264 -crf 19 -pix_fmt yuv420p -c:a aac -b:a 192k -shortest -movflags +faststart`.
5. **Duração:** uma narração de 2 minutos leva cerca de 15 a 20 minutos para renderizar.

## Capa (1080×1920)
O modelo é `motor-mapa/capa.html`:
- fundo de mapa escuro;
- duas etiquetas no topo, uma vermelha e uma com contorno;
- título em duas cores, branco mais amarelo, em forma de pergunta;
- a foto real numa moldura inclinada;
- carimbo embaixo dos rostos, nunca cobrindo ninguém;
- uma linha de promessa;
- o selo do perfil.

Confira o recorte 3:4 da grade (y 240 a 1680): todo o texto precisa estar dentro dele.

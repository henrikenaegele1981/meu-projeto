# Motor do mapa animado

Este é o motor que renderizou o Reel "Shenzhen" (nov/2026). Para um vídeo novo:

1. Crie uma pasta de trabalho e copie para ela estes arquivos.
2. Monte a pasta `assets/` com:
   - `assets/mapa/`: os 8 blocos `tile_i_j.jpg`, gerados do Natural Earth NE1_HR_LC_SR_W (21600×10800, redimensionado para 24000×12000 e cortado em blocos de 6000), mais `world4096.jpg` e `countries.geojson` (ne_50m_admin_0_countries).
   - `assets/fontes/`: a Poppins em woff2 e o `fonts.css`, tirados do Google Fonts.
   - `assets/fotos/`, `assets/prints/` e `assets/video/`: este último com `frames_<nome>/0001.jpg…` e o `frames.json`.
   - `assets/jose.jpg` → troque pela foto do perfil e atualize o caminho no `index.html`.
3. Gere o `captions.json` a partir da transcrição do áudio (scribe_v1, com o tempo de cada palavra).
4. Em `index.html`, edite:
   - `CAM`: a câmera, no formato [tempo, longitude, latitude, largura em graus];
   - `HL`: os países em destaque, no formato [código, início, fim, cor];
   - os pinos e as rotas em `drawMap`;
   - as camadas `layer(início, fim, html, atualização)`, que são as cenas.
5. Rode `python3 -m http.server 8765`, depois `node snap.js <tempos>` para os quadros de teste, depois `render.js` em 4 processos em paralelo, e por fim o encode com ffmpeg.

Os passos completos estão em `../referencias/formato-mapa-animado.md`.

# Identidade visual do José (@josehenriquenaegele)

Tirada do Reel dele com 133 mil curtidas (apagão mundial, nov/2026) e aprovada pelo usuário.
O `assets/modelo-jose.html` já implementa tudo isto. Use este arquivo para conferir e para criar cenas novas.

## Mapa (fundo de todas as cenas)
- Mapa-múndi em projeção de Mercator, com zoom e deslocamento suaves entre as cenas (câmera em `CAM`).
- **Oceano azul-marinho escuro e terra verde-oliva com textura granulada** (filtro `#textura`).
- **Três climas de cor**, trocados com transição de 1 s conforme o sentido da cena (`climaDe`):
  - **neutro:** oceano marinho `rgb(14,34,58)`, terra verde `rgb(118,140,96)`. Usado no fato e no contexto.
  - **negativo:** oceano vinho `rgb(38,20,40)`, terra sépia `rgb(150,128,90)`. Usado em "a mentira", no Estado, nos impostos e nos juros.
  - **positivo:** oceano verde-água `rgb(10,52,52)`, terra verde-clara `rgb(104,160,110)`. Usado na solução, no Paraguai e na CTA.
- **País em destaque:** preenchimento neon translúcido com contorno brilhante (filtro `#neon`). Ciano `#2fd6e8` para o neutro, verde `#2fe37a` para o positivo, vermelho `#ff2d3d` para o negativo. Bandeira em emoji por cima, quando couber.
- Vinheta escura nas bordas.

## Textos
- **Fonte:** Inter (800/900 nos títulos e legendas, 600 nos textos menores) com Noto Color Emoji.
- **Legenda da fala:** centro e embaixo (`top:1210px`; na abertura em quadro, `1400px`), **caixa alta, 76 px, peso 900, branca**, sombra escura. Mostra blocos de 2 a 4 palavras sincronizados com a voz (`blocos()`).
  - A palavra-chave do bloco (a mais longa) vai em **amarelo `#ffd21f`**.
  - As palavras negativas (`NEG`: imposto, juros, governo, Estado, explora…) vão em **vermelho `#ff2d3d`**.
- **Etiqueta no alto (`pillC(250,…)`):** caixa escura arredondada (`rgba(10,14,22,.86)`) com **contorno neon**. Vermelho é o padrão; também há `verde`, `ciano` e `ouro`. Texto branco 38 px, peso 800, com emoji no começo (ex.: "🇧🇷 ASSAÍ • BALANÇO 2025").
- **Pílulas de dado (`pill(x,y,…)`):** o mesmo estilo, posicionadas sobre o mapa, entrando com um pequeno "pulo" (`back`).
- **Cards de fonte (`card`):** caixa escura arredondada no estilo de post de rede social. Avatar com emoji, nome em negrito, linha cinza de fonte, texto com destaque amarelo e alerta em vermelho ("⚠️ sem fonte…" ou "✅ documento auditado").
- **Marca d'água:** `@josehenriquenaegele` pequena, cinza, no canto inferior direito.

## Elementos
- **Emojis** como ícones surgindo sobre o mapa (`emo`): 💰🪙❓💥🏛️🏢👷🛒🔒⛓️🇧🇷🇵🇾.
- **Barras de dados** dentro de um card escuro, com cores neon e brilho (funcionários em ciano, juros e impostos em vermelho, donos em amarelo).
- **Contas:** card escuro com o resultado grande em amarelo ou vermelho ("= R$ 460/mês").

## Abertura com vídeo de terceiro (aprovada assim)
- O trecho fica **dentro de um quadro** (840×896, cantos arredondados, contorno neon vermelho, leve rotação de -1,2°), **sobre o mapa azul e verde**. Etiqueta "🎙️ NOME • CARGO" no alto e legenda logo abaixo do quadro.
- Corte a parte de baixo do vídeo original, onde ficam as legendas queimadas (`preparar_abertura.sh`, `CORTE_ALTURA` em torno de 0.60).
- Nunca tela cheia com faixa escura cobrindo legenda: o usuário preferiu o quadro.

## Área segura do Reels (do prompt mestre; confira em toda prévia)
- Nada importante nos **250 px do topo** (as etiquetas ficam a partir de y=250).
- Margem esquerda de pelo menos 70 px.
- **160 px da direita livres** da metade da tela para baixo (ícones do Instagram).
- **480 px de baixo livres** (legenda do Instagram): nada importante abaixo de y≈1440.
- A legenda karaokê fica em y≈1200–1350 e a marca d'água em y≈1575.

## Efeitos que o Henrike pede ("deixar ilustrativo")
- Chips que entram com pop.
- Carimbos tortos com tremida ("LOJA FECHADA", "O ESTADO").
- Chuva de 💸 ou moedas.
- Bonequinhos 👷 enchendo a tela.
- Barras crescendo.
- Carrinho atravessando uma ponte.
- Etiqueta balançando.
- Pontos de interrogação flutuando.
- **Flash branco curto (alpha 0,3, 0,15 s) na troca de cena.**
- CTA pulsando com ondas.
- Cada tela fica mais tempo: nada de pisca-pisca nem troca rápida demais.
- Cards com foto ou vídeo de apoio (Pinterest), com borda branca arredondada, sombra e zoom leve, no miolo, sem cobrir a legenda. **Não use foto de pessoa pública baixada da internet:** peça ao Henrike.
- Mapa: além do verde-oliva aprovado, o prompt mestre também prevê **mapa-múndi noturno com luzes de cidades** (#0c1630). Use **ida e volta no mapa** (ex.: Brasília → Lima → Assunção). Destaques em ciano #38e1ff, vermelho #ff4b4b ou amarelo #ffd23f.
- **Mix de cores**, não tudo azul.

## Tela final padrão (formato G)
Fundo escuro, bandeira do Paraguai, **"PARAGUAI SEM FILTRO"** ("SEM FILTRO" em destaque), "viver • trabalhar •
empreender", pílula com **paraguaisemfiltro.com** e **"LINK NA BIO"**.

## O que NÃO é da identidade do José (não usar)
- Papel envelhecido, pergaminho, polaroides com fita, letra com serifa em itálico. Isso é do estilo "mapa antigo" do Felipe Dantas: serve de modelo de narrativa, não de visual.
- Fotos de banco de imagens como elemento principal. No estilo do José, prefira mapa, emoji, card e pílula.

---
name: video-mapa-animado
description: Fábrica de vídeos de mapa animado (Reels/TikTok verticais 1080×1920, 1 a 3 min) na identidade visual do José (@josehenriquenaegele) — modelar roteiro a partir de um vídeo de referência, checar números em fonte oficial, entregar texto para o ElevenLabs, alinhar a voz, animar mapa/cards/emojis/legendas, abertura com trecho de vídeo de terceiro, trilha com ducking, render em paralelo e publicação. Use sempre que o usuário pedir vídeo animado, vídeo de mapa, "no estilo desse Reel", modelar um vídeo, roteiro para ElevenLabs, ou mandar link de Reel/TikTok de referência ou áudio do ElevenLabs para montar — mesmo que não diga "mapa".
---

# Vídeo de mapa animado

Transforma um assunto e um vídeo de referência num Reel animado pronto para publicar, no padrão que o
José aprovou. O usuário não é técnico e quer **resultado rápido e bem acabado**. Faça você mesmo tudo o
que der, peça só o que só ele pode dar e **mostre prévias antes de gastar render**.

Antes de começar, leia **`references/licoes.md`**. Ele traz as correções do usuário, que valem para sempre.

## Fluxo (detalhes e comandos em `references/processo.md`)

1. **Preparar a pasta:** `scripts/preparar_ambiente.sh PASTA` (npm, fontes, yt-dlp, Whisper).
2. **Estudar as referências:** `scripts/baixar_referencia.sh URL nome` gera o vídeo, a folha de quadros e a transcrição.
   Separe o *modelo de narrativa* (de quem fez a referência) da *identidade visual* (sempre a do José,
   em `references/identidade-jose.md`).
3. **Roteiro:** fórmula, medidas e checagem de fatos em `references/roteiro.md`, com exemplo completo em
   `assets/exemplo-roteiro-patrao.md`. Entregue o texto num bloco de código, pronto para o ElevenLabs.
   Siga os princípios do José (skill `estudio-jose`): nem liberal nem socialista, Igreja em uma frase,
   documento e não pessoas.
4. **Voz:** o usuário grava no **ElevenLabs** com a voz dele e manda o MP3. Não clone voz nem use gerador local.
5. **Abertura (opcional):** `scripts/preparar_abertura.sh clip.mp4 DUR CORTE` gera os quadros sem as legendas
   queimadas, as palavras com tempo e o áudio.
6. **Alinhar:** `alinhar.py roteiro narracao.mp3 tempos.json`. Cada parágrafo vira uma cena, e a legenda usa o texto exato.
7. **Cenas:** edite `video.html` (cópia de `assets/modelo-jose.html`): `CFG`, `CAM`, `climaDe`, `NEG` e um
   `case` por parágrafo em `cena()`. O exemplo do Assaí já está lá como molde.
8. **Prévia:** `node quadros.js video.html prev/c t1 t2 …` com 4 a 6 quadros. Olhe e **mande ao usuário para aprovar**.
9. **Áudio:** `scripts/montar_audio.sh narracao abertura trilha` monta abertura, voz e trilha com ducking.
10. **Render:** `node render_par.js video.html final.mp4 audio_final.wav 4` leva uns 8 min para 3 min de vídeo.
11. **Conferir:** folha de quadros e 40 quadros seguidos da abertura (não pode piscar). Depois entregue o MP4 e a
    legenda (skill `estudio-jose` + agente `revisor-legendas`).
12. **Publicar:** caixa de entrada do Meu Estúdio (`estudio-jose/scripts/agendar_caixa.py … --tipo reel`).

## Regras que não podem falhar
- **A cena é função do tempo:** nada de estado entre quadros, senão o render em paralelo quebra.
- **O `render()` espera as imagens carregarem.** Se tirar, a abertura volta a piscar.
- **Legenda sem sobrepor rosto, quadro ou card;** nada cortado fora da tela. Confira na folha antes de entregar.
- **Números só de fonte oficial**, com a tabela de conferência salva junto do roteiro.
- **Créditos:** "estimativas" na etiqueta quando o dado não for oficial; a fala de terceiro só entre aspas se conferida no vídeo original.

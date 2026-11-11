# Lições do primeiro vídeo ("O patrão lucra bilhões?", nov/2026)

O que o usuário corrigiu ou cobrou, e o que funcionou. Leia antes de começar um vídeo novo.

## Voz
- **Nada de clonar voz** dentro desta sessão (testamos o Chatterbox e o usuário achou ruim).
- **Nada de voz de gerador local**, como o Kokoro: "ficou horrível".
- **O certo:** você entrega o roteiro e **o usuário grava no ElevenLabs com a voz dele** e manda o MP3. Você alinha e monta.

## Visual
- O usuário quer **um modelo de narrativa** (ex.: Felipe Dantas), mas **sempre a identidade visual do José** (mapa azul e verde, neon, emojis, legenda amarela e branca). Não copie o visual do criador de referência.
- **Abertura:** o trecho do terceiro **dentro de um quadro**, sobre o mapa. O usuário rejeitou a tela cheia.
- **Erro que já aconteceu:** o vídeo da abertura **piscava**, porque o quadro era capturado antes de a imagem carregar. Corrigido com o `render()` esperando `img.decode()`.
- **Erros de enquadramento** que irritaram:
  - legenda em cima do rosto ou do quadro;
  - barra de texto cortada fora da tela;
  - a legenda queimada do vídeo original aparecendo atrás da nossa.
  - **Sempre confira a folha de quadros antes de entregar.**
- **Legenda da tela com o texto exato do roteiro.** A transcrição automática errou "arrecada" como "a recada".

## Velocidade e processo
- O usuário achou lento. O que resolveu:
  - **prévia de 4 a 6 quadros antes do render completo**;
  - **render em paralelo** (7 a 8 min em vez de 15 a 20);
  - trocar só o áudio sem renderizar de novo.
- **Não liste o que o usuário precisa fazer quando você mesmo pode fazer.** Ele quer resultado. Peça só o que só ele pode dar: o áudio do ElevenLabs, os arquivos de vídeo que a rede bloqueia e as aprovações.

## Conteúdo
- **Princípios do José:** nem liberal nem socialista. Menos imposto, sim, mas com argumento de justiça e Doutrina Social, nunca com discurso liberal. "O Estado explora os dois": o rico na empresa e o pobre no consumo.
- **A Igreja numa frase, sutil.** Rerum Novarum (o Estado é injusto quando, a título de impostos, tira mais do que é justo) funcionou bem.
- **CTA:** o vídeo termina no Paraguai, com o **Paraguai Sem Filtro • link na bio**.
- **Números:** sempre do balanço oficial, nunca da imprensa (o lucro "pré-IFRS16" da imprensa é diferente do oficial).

## Fotos e fontes de mídia
- Instagram e YouTube bloqueiam servidores de nuvem depois de alguns acessos. Se travar, peça o arquivo ao usuário.
- Fotos de licença livre: Openverse (`scripts/buscar_fotos.py`). Fotos do Flickr baixam sem problema; Wikimedia limita (erro 429).
- Na identidade do José, quase não se usa foto: prefira mapa, emoji, card e pílula.

## Ainda a melhorar (o usuário disse que "é só o começo")
- Mais movimento de câmera e transições entre as cenas.
- Trilha sonora mixada em todo vídeo (o usuário mandou uma trilha; use `montar_audio.sh`).
- Biblioteca de cenas prontas (mapa com rota, contador, linha do tempo, comparação de dois países) para montar mais rápido.
- Possível: script que gera a lista de `case` de cena a partir de uma tabela do roteiro.

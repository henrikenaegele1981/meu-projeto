# Processo completo, passo a passo

Pasta de trabalho sugerida: `<scratchpad>/videos/<nome-do-video>/`. Os scripts de render servem os arquivos a
partir da própria pasta, então **`video.html`, `tempos.json`, `abertura/`, `node_modules` e os scripts
ficam todos juntos**.

## 0. Preparar
```bash
bash <skill>/scripts/preparar_ambiente.sh PASTA
export VENV_PY=/tmp/claude-0/voz/.venv/bin/python
```
A rede da sessão precisa de internet liberada para Instagram, YouTube, Hugging Face e sites de RI. O ambiente
"meu-projeto" já tem acesso livre. Se a sessão estiver em outro ambiente, peça a mudança com as
ferramentas de ambiente.

## 1. Referências
```bash
bash <skill>/scripts/baixar_referencia.sh URL nome PASTA/ref
```
- Olhe a `folha_nome.jpg` (um quadro a cada 6 s) e leia `nome.txt` (a transcrição).
- Instagram: depois de alguns downloads, ele bloqueia o acesso anônimo (exige login). O script espera e tenta de novo. YouTube costuma pedir "não sou robô" a servidores. Se falhar, peça ao usuário o arquivo (ssstik.io para TikTok e Instagram).
- Separe **o modelo de narrativa** (ex.: Felipe Dantas) da **identidade visual** (sempre a do José; veja `identidade-jose.md`).

## 2. Roteiro
- Siga `roteiro.md`: fórmula, de 430 a 480 palavras e números por extenso.
- Cheque os números na fonte oficial e monte a tabela de conferência.
- Entregue ao usuário **o texto pronto para colar no ElevenLabs**, num bloco de código, e o arquivo `.md` com as cenas.
- O usuário grava no **ElevenLabs com a voz dele** e manda o MP3.

## 3. Abertura (se houver vídeo de terceiro)
```bash
bash <skill>/scripts/preparar_abertura.sh clip.mp4 10.4 0.60 PASTA/abertura
```
Confira na folha de quadros onde estão as legendas queimadas e ajuste o corte. Preencha `CFG.abertura`
(`total`, `dur`, `rotulo`) no `video.html`.

## 4. Alinhar a voz ao roteiro
```bash
$VENV_PY alinhar.py roteiro.md narracao.mp3 tempos.json
```
- A narração é lida de um `.txt` (o arquivo inteiro), ou de um `.md` (o primeiro bloco ` ```text `, ou o trecho entre "## Parte 1" e "## Parte 2", formato de `assets/exemplo-roteiro-patrao.md`).
- A saída mostra quantas palavras casaram. Esperado: mais de 98%. Se for menos, o texto gravado é diferente do roteiro: atualize o roteiro com o que foi falado.
- Cada parágrafo vira uma cena (`T.cenas[i]`); as legendas usam o **texto exato do roteiro** com os tempos do áudio.

## 5. Escrever as cenas
No `video.html`:
- **`CAM`**: a câmera do mapa por cena (`[longitude, latitude, escala]`). A transição entre cenas é automática.
- **`climaDe(ci)`**: qual cena é neutra, negativa ou positiva.
- **Destaques de país:** `brOn`/`pyOn` em `mapa()`. Para outros países, adicione como `BR`/`PY`.
- **`cena(ci,…)`**: um `case` por parágrafo, usando `pillC`, `pill`, `emo`, `card` e as barras. Os `case` do exemplo (Assaí) servem de molde.
- **`NEG`**: palavras que ficam vermelhas na legenda.

## 6. Prévia antes de renderizar (sempre)
```bash
node quadros.js video.html prev/c 4 15.8 55 103 139
```
Monte uma folha com 4 a 6 quadros (meio de cenas diferentes), **olhe** e **mande ao usuário para aprovar o visual**. Só
depois renderize o vídeo inteiro. Isso evita renders de 8 minutos jogados fora.

## 7. Áudio
```bash
bash <skill>/scripts/montar_audio.sh narracao.mp3 audio_final.wav abertura/audio.wav 10.4 trilha.mp4 0.22
```
A trilha (arquivo de música ou vídeo do usuário) repete em loop e **abaixa sozinha quando a voz fala**. Sem trilha, omita os dois últimos argumentos.

## 8. Render
```bash
node render_par.js video.html final.mp4 audio_final.wav 4
```
- Usa 4 navegadores em paralelo: cerca de 7 a 8 min para um vídeo de 3 min (5.000 quadros).
- A cena **não pode depender do quadro anterior**: tudo é calculado a partir de `t` e `lt` (tempo dentro da cena). Isso permite renderizar em paralelo.
- O `render()` devolve uma Promise que espera as imagens carregarem. **Isso evita o vídeo da abertura piscar.** Não remova.

## 9. Conferir e entregar
- Folha de quadros do vídeo final (`ffmpeg -ss t -frames:v 1` em 15 pontos) e 40 quadros seguidos da abertura, para ver que não pisca.
- Duração, tamanho (fica em torno de 20 MB) e volume (`volumedetect`, média em torno de -20 dB).
- Mande o MP4 com `SendUserFile`, mais a legenda do post (skill `estudio-jose`, revisada pelo agente `revisor-legendas`).

## 10. Publicar
Pela caixa de entrada do Meu Estúdio (`estudio-jose/scripts/agendar_caixa.py agendar --midia final.mp4 --tipo reel …`). O MP4 precisa ter menos de 100 MB (limite do GitHub).

## Trocar só a trilha ou o áudio de um vídeo pronto (sem renderizar de novo)
```bash
ffmpeg -i final.mp4 -i audio_novo.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -shortest final_com_trilha.mp4
```

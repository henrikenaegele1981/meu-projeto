# Meu Estúdio: instruções para o Claude

Este repositório é o **Meu Estúdio**, um app Flask que roda no PC do usuário (Windows) em
`http://localhost:5252` e agenda posts no Instagram (Reels e fotos) pela API oficial da Meta.
Quem usa: José Henrique Naegele (@josehenriquenaegele), editor católico tradicional.

## Agendar posts (tarefa mais comum)

O app precisa estar aberto (`iniciar.bat`) e o PC ligado na hora marcada. Para agendar, envie o
formulário da Agenda com `curl` (vem no Windows):

```bash
curl -s -o NUL -w "%{http_code}" -F "arquivo=@C:\caminho\imagem.jpg" -F "legenda=<C:\caminho\legenda.txt" -F "quando=2026-11-11T14:00" -F "redes=instagram" -F "collabs=" http://localhost:5252/agenda
```

- `arquivo`: vídeo (`.mp4`/`.mov`, vertical, 3 s a 15 min) vira **Reel**; foto (`.jpg`, `.png`, `.webp`)
  vira **post estático**. Fotos precisam ter proporção entre 4:5 (1080×1350) e 1,91:1; quadrada serve;
  9:16 (story) é recusada. O app converte a foto para JPEG.
- `legenda`: use `<arquivo.txt` (UTF-8) para não quebrar acentos e emojis. Máximo 2.200 caracteres.
- `quando`: horário local do PC, formato `AAAA-MM-DDTHH:MM`.
- `collabs`: até 3 @ separados por vírgula, ou vazio.
- A resposta é um redirecionamento (302). **Sempre confirme** abrindo `GET /agenda` e procurando o post
  na fila com status `agendado`. Erros de validação aparecem como aviso no topo dessa página.
- Antes de agendar, confira em `/configuracoes` se o Instagram está conectado.
- Depois do horário, confira em `/agenda` se o status virou `publicado` (com link) ou `erro` (com a mensagem).

## Agendar de fora do PC (caixa de entrada)

Quando o Claude não está no PC (ex.: sessão na nuvem), ele agenda pela **caixa de entrada**: a branch
`caixa` deste repositório tem `fila.json` e as mídias. O app (`caixa.py`) confere
`https://raw.githubusercontent.com/henrikenaegele1981/meu-projeto/caixa/fila.json` a cada minuto e
coloca na Agenda os itens novos (marcados "agendado pelo Claude"), que saem com o token do próprio app.

```json
[{"id": "nome-unico", "tipo": "foto", "quando": "2026-11-11T15:00", "legenda": "...",
  "midia": "https://raw.githubusercontent.com/henrikenaegele1981/meu-projeto/caixa/arquivo.jpg",
  "collabs": [], "cancelado": false}]
```

- `id` nunca se repete (o app guarda os já importados). Para mudar um post: marque o antigo com
  `"cancelado": true` e crie outro `id`. Foto em JPEG 4:5 (1080×1350) ou quadrada; reel em MP4.
- O repositório é público: o conteúdo fica visível até ser publicado. Depois de publicado, tire da caixa.
- O app precisa estar aberto no PC. Post que chega mais de 2 h atrasado entra como "erro" (não sai sozinho).

## Regras

- **Nunca** leia, mostre ou copie o token do Instagram. Ele fica em `%LOCALAPPDATA%\MeuEstudio\config.json`;
  não edite esse arquivo nem `fila.json` à mão. Use sempre a interface/rotas do app.
- Legendas: siga **sempre** o guia de estilo abaixo e mostre a legenda ao usuário antes de agendar,
  a menos que ele já tenha aprovado o texto.
- Código: o app se atualiza sozinho a partir da branch `meu-estudio` do GitHub (`atualizar.py`).
  Mudanças no código devem ir para essa branch; mudanças feitas só no PC são sobrescritas na próxima atualização.

## Estrutura do código

- `app.py`: rotas (Agenda, Configurações), upload de vídeo/foto, atualização automática.
- `vigia.py`: confere a fila a cada 15 s e publica na hora.
- `instagram.py`: API da Meta (token do login do Instagram em graph.instagram.com, ou token de
  usuário do sistema/login unificado em graph.facebook.com com o ID da conta, que começa com 1784).
- `armazenamento.py`: dados em `%LOCALAPPDATA%\MeuEstudio\` (nunca na pasta do código).
- `atualizar.py`: baixa a versão nova do GitHub ao abrir e a cada 6 horas.

# Guia de estilo das legendas

> **Prioridade:** se a skill `jose-paraguai-sem-filtro` (prompt mestre do perfil) estiver disponível, ela vale
> sobre este guia. Resumo do que mudou: legenda de 900 a 1.400 caracteres em primeira pessoa; CTA do
> diagnóstico gratuito em paraguaisemfiltro.com (link na bio); até 5 hashtags (#paraguai #morarnoparaguai
> #paraguaisemfiltro + 2 do tema); 2 mensagens de WhatsApp redigidas junto de cada post; roteiro de vídeo
> entregue só como copy corrida. Críticas à esquerda, ao STF e ao comunismo são permitidas (atos, não honra).

Quem escreve: católico fiel à sã doutrina e à Tradição da Igreja; contra o americanismo; não é de
direita nem de esquerda; não é trumpista, bolsonarista, liberal nem socialista. **Toda legenda segue a
Doutrina Social da Igreja e o magistério anterior ao Concílio Vaticano II.**

### Persona e tom
- Escreva como um editor católico tradicional, pai de família, que lê a atualidade à luz da doutrina perene da Igreja. O tom é técnico e profundo, a narrativa é fluida e envolvente, sério sem ser panfletário e firme sem agressividade pessoal.
- A tese de fundo de quase toda legenda: o Ocidente esqueceu Deus, e a crise moral, familiar e social é consequência espiritual desse esquecimento. A resposta é a volta à doutrina e à Tradição da Igreja, não a um partido.

### Estrutura (legenda longa, ~1.700–2.000 caracteres, máximo absoluto 2.200)
1. **Cena concreta** (1–2 frases visuais) que prende o leitor.
2. **O fato**, sóbrio e verificado ("Segundo a imprensa alemã...").
3. **Ampliação**: "Não é um caso isolado." Mostre o fato como sintoma da crise do Ocidente.
4. **Diagnóstico**: relativismo, laicismo, agenda woke como fruto do esquecimento de Deus.
5. **O que a Igreja ensina**: documento, papa ou catecismo, em paráfrase ou citação conferida. Termine o parágrafo doutrinário na afirmação firme, sem ressalvas pastorais.
6. **Frase-síntese forte** (aforismo curto).
7. **Pergunta ao público** + 👇.
8. **5–7 hashtags** no fim (ex.: #IgrejaCatólica #Fé #Ocidente #Tradição + tema).

### Formato alternativo (card noticioso)
"🚨 URGENTE: [notícia em uma frase]" + um parágrafo de contexto + **pergunta retórica final em negrito** (ex.: "A crise do Ocidente chegou: não pode mais ser cristão na Alemanha?").

### Vocabulário preferido
Deus, Cristo Rei, Igreja, doutrina, Tradição, fé, verdade, ordem natural, família, lei moral, Ocidente, cristandade, raiz e frutos, relativismo, laicismo, modernismo, liberalismo, socialismo, agenda woke, crise espiritual. Emojis com parcimônia (👇, 🚨, ⚔️).

### Sempre
- Cite **documentos, não pessoas**: "Pio XI, *Quadragesimo Anno* (1931)", "Catecismo de São Pio X", "*Casti Connubii*". Use o gênero certo (Testem = carta apostólica; Syllabus = lista de proposições condenadas anexa à *Quanta Cura*; Lamentabili = decreto).
- Dê preferência ao magistério pré-Vaticano II e à Doutrina Social (*Rerum Novarum*, *Quadragesimo Anno*, *Divini Redemptoris*, *Quas Primas*, *Libertas*, *Immortale Dei*, *Pascendi*, *Casti Connubii*, Catecismo Romano, Catecismo de São Pio X). Use o CIC de 1992 só quando ele apenas reafirma o ensino tradicional.
- Ponha entre aspas só o que foi conferido no texto oficial. Caso contrário, faça paráfrase sem aspas e sem número de parágrafo duvidoso.
- Rejeite **ao mesmo tempo** o liberalismo (filosófico, político e econômico) e o socialismo/comunismo.

### Nunca
- Nunca cite pensadores ou personalidades pelo nome (filósofos, papas pós-conciliares como autores, influenciadores, políticos) como autoridade.
- Nunca diga a denominação religiosa das pessoas da notícia; escreva "cristão", "fiel", "grupo cristão".
- Nunca use discurso pluralista: "Estado laico", "liberdade religiosa" como ideal, "todas as fés são válidas", "respeitar todas as crenças".
- Nunca se alinhe a direita ou esquerda, Trump, Bolsonaro, Lula, liberais, conservadores americanos ou socialistas. Nunca trate os EUA como modelo.
- Nunca use "americanismo" como sinônimo de "anti-EUA". No sentido de Leão XIII, é a acomodação da fé ao mundo moderno (calar ou atenuar a doutrina, exaltar virtudes naturais e ativismo, separação Igreja-Estado como ideal).
- Nunca apresente proposição do Syllabus como ensino. Escreva "Pio IX condenou a proposição de que...".
- Nunca escreva "a Igreja condenou o capitalismo" sem matiz. Condenam-se o liberalismo econômico, a usura e a "ditadura econômica" (QA 101 ressalva que o regime capital-trabalho não é vicioso por natureza).
- Nunca inclua frases de acolhimento pastoral que diluam a doutrina moral (ex.: a linha do CIC sobre "respeito, compaixão e delicadeza"). Pare na afirmação doutrinária.
- Nunca afirme como fato que o Vaticano II "revogou" ou "confirmou" um ensino anterior.
- Nunca chame de "dogma" o que é ensino encíclico.
- Nunca use as fontes do canal "História Mal Contada" (Brasil Paralelo, Olavo de Carvalho etc.); o canal não tem relação com José.

### Checklist antes de publicar
1. A notícia foi checada em pelo menos uma fonte jornalística confiável (data, nomes, o que de fato aconteceu)?
2. A legenda tem ≤ 2.200 caracteres (ideal 1.700–2.000)?
3. Nenhum pensador ou pessoa foi citado como autoridade? A denominação das pessoas da notícia foi omitida?
4. Toda citação entre aspas foi conferida no texto oficial (vatican.va ou edição impressa)? Os números de parágrafo conferem com a edição citada?
5. A legenda condena liberalismo e socialismo sem se alinhar a nenhum lado político?
6. Não há linguagem de Estado laico ou pluralismo religioso?
7. A estrutura segue cena → fato → ampliação → diagnóstico → doutrina → frase forte → pergunta → hashtags?

### Legenda de referência (aprovada pelo usuário)

> O parágrafo doutrinário é paráfrase de documentos pré-conciliares. Só use aspas e números de
> parágrafo depois de conferir no texto oficial (vatican.va ou edição impressa).

```text
Um jogador de joelhos no gramado, braços abertos, olhos voltados para o céu. Na Alemanha de hoje, essa imagem deixou de ser vista como gratidão e passou a ser tratada como problema.

Segundo a imprensa alemã, a Federação Alemã de Futebol vai conversar com Felix Nmecha por causa da sua ligação com um grupo cristão, acusado por emissoras do país de defender posições contrárias ao aborto e à agenda LGBTQ.

Não é um caso isolado. É o retrato de um continente que esqueceu de Deus. A Europa, que ergueu catedrais, universidades e hospitais à sombra da cruz, esvaziou as igrejas e achou que poderia manter os frutos depois de arrancar a raiz. Não pôde. Sem Deus, aquilo que foi construído sobre Ele começou a ruir: a moral, a família, o próprio sentido da vida.

E o vazio não ficou vazio. No lugar da verdade, entrou o relativismo, que não reconhece nada como definitivo e transforma o desejo de cada um na única medida de todas as coisas.

O movimento woke é o fruto mais recente dessa árvore. Ele não se contenta em discordar da fé cristã: quer que ela se cale, peça desculpas e se adapte. Quem crê no que a Igreja sempre ensinou passa a ser investigado, como se a fé fosse uma ameaça.

E o que a Igreja ensina é claro. Na encíclica Casti Connubii (1930), Pio XI condena como crime gravíssimo tirar a vida do inocente no seio materno, e nenhuma razão pode justificá-lo. E o Catecismo de São Pio X coloca o pecado impuro contra a natureza entre os pecados que bradam ao Céu e clamam a Deus por vingança.

A crise do Ocidente não é política nem econômica. É espiritual. Uma civilização que esquece de Deus acaba esquecendo de si mesma.

E você, acredita que o Ocidente ainda tem volta? 👇

#FelixNmecha #Alemanha #Cristianismo #IgrejaCatólica #Fé #Ocidente #Woke
```

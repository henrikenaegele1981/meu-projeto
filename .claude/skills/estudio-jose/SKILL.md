---
name: estudio-jose
description: Instagram do José Henrique Naegele (@josehenriquenaegele), editor católico tradicional — escrever legendas no tom dele (fiéis à doutrina pré-Vaticano II e à Doutrina Social da Igreja, sem citar pessoas) e agendar/publicar posts pelo app Meu Estúdio (Reels e fotos), inclusive de uma sessão na nuvem pela caixa de entrada no GitHub. Use sempre que o usuário falar em legenda, post, Reel, foto para o Instagram, agendar/programar post, "Meu Estúdio", notícia para comentar, crise da Igreja ou do Ocidente para postar — mesmo que não diga "Instagram" nem "José".
---

# Estúdio do José

Duas tarefas, quase sempre juntas: **escrever a legenda** no tom do José e **agendar o post** no
Meu Estúdio. O José não é programador: fale simples, em português, e faça você mesmo tudo o que der
daqui, em vez de passar passos técnicos para ele.

## 1. Legenda

Antes de escrever, leia `references/guia-estilo.md`. Ele traz quem o José é, as correções que ele
já fez (e que valem para sempre), a estrutura, o que sempre e nunca fazer, a base doutrinal segura e
uma legenda aprovada como modelo.

O essencial, para não esquecer:
- Tom técnico e profundo, narrativa com storytelling: cena concreta → fato → "não é um caso isolado"
  → crise do Ocidente que esqueceu Deus → o que a Igreja ensina → frase forte → pergunta + 👇 →
  5–7 hashtags. 1.700–2.000 caracteres (máximo 2.200).
- Autoridade é a **Igreja** (encíclicas e catecismos anteriores ao Concílio Vaticano II e a Doutrina
  Social), **nunca pessoas** (pensadores, papas como autores, políticos). Não diga a confissão de
  quem está na notícia.
- Nem direita nem esquerda: condene liberalismo e socialismo; nada de Trump, Bolsonaro, Lula, EUA
  como modelo, nem discurso de "Estado laico"/"liberdade religiosa"/"todas as fés".
- Parágrafo doutrinário termina na afirmação firme, sem ressalva pastoral.
- Citação entre aspas ou com número de parágrafo só se foi conferida no texto oficial; senão,
  paráfrase.
- Confira a notícia numa fonte antes; se não conseguir, avise e escreva "segundo a imprensa…".

Mostre a legenda com a contagem de caracteres. Quando o José corrigir, aplique sem rediscutir.

## 2. Agendar

Leia `references/operacao.md` (como o sistema funciona, formatos aceitos e erros já resolvidos).

- **Sessão na nuvem** (o normal aqui): use `scripts/agendar_caixa.py agendar ...`. Ele converte a
  foto, envia para a caixa no GitHub e confere o link. O app no PC importa em até 1 minuto e publica
  com o token dele. Precisa do app aberto e do PC ligado na hora.
- **Sessão no PC do José**: envie o formulário para `http://localhost:5252/agenda` (comando no
  `operacao.md`) e confira a fila.

Antes de agendar: confirme o horário (`TZ=America/Sao_Paulo date`), use um `id` novo
(`assunto-AAAA-MM-DD`) e garanta que o mesmo post não foi agendado à mão no app (sairia duas vezes).
Depois: diga ao José o horário, lembre que o app precisa estar aberto e peça para ele avisar se a
Agenda mostrar "erro". Depois de publicado, rode `remover` para tirar o post da caixa pública.

Nunca peça o token no chat e nunca tente lê-lo: ele fica só no PC.

# Roteiro de vídeo de mapa animado

## Fórmula (modelada no Reel do Felipe Dantas sobre a Bahia, 570 mil curtidas)

1. **[Abertura opcional]** De 5 a 12 s de um vídeo de terceiro com a frase que vai ser rebatida (ex.: político). A narração começa logo depois.
2. **"Imagine…"** Descreva o caso como um mistério: um lugar ou uma empresa que tinha tudo.
3. **"Pela lógica…, deveria ser…, certo?"**
4. **A revelação:** "Esse lugar é…" / "Essa empresa é…" + o contraste.
5. **"Mas como…?"**
6. **"Para entender, basta olhar para / seguir…"**
7. **Os dados, um a um** (cada número é uma cena).
8. **Uma conta concreta com um personagem** ilustrativo (ex.: "o seu Antônio, repositor"). Use números divididos por pessoa e por mês.
9. **A virada / tese** (ex.: "Muita gente pensa que… Mas a conta mostra outra coisa: …").
10. **A doutrina, numa frase só**, sutil: documento pré-conciliar em paráfrase (ex.: Rerum Novarum).
11. **"Olhe para os dois lados…"**: o contraste final (ex.: Brasil contra Paraguai).
12. **"O pior é que muita gente não conhece…"**
13. **CTA:** para o José, normalmente o **Paraguai Sem Filtro, link na bio**. Senão, "Para entender o Brasil de verdade, siga este perfil".

## Medidas
- **2 min 30 s a 3 min = cerca de 430 a 480 palavras** de narração (o ElevenLabs fala de 150 a 170 palavras por minuto), mais a abertura.
- **Um parágrafo por cena**: o `alinhar.py` transforma cada parágrafo do roteiro numa cena. Parágrafos curtos dão cortes rápidos.
- **Números escritos por extenso** no texto do ElevenLabs ("oitenta e quatro bilhões e meio"). Na tela, eles aparecem em algarismos.
- **Frases curtas e diretas, em segunda pessoa** ("imagine", "olhe", "faz a conta").

## Princípios do José (valem para o roteiro também)
- Ele é **nem liberal nem socialista**. Pode defender menos imposto e mais liberdade econômica para quem produz, mas **sem discurso liberal**: o argumento é de justiça (o homem e a família vêm antes do Estado; o Estado não pode tirar mais do que é justo).
- Quando criticar, **critique o Estado** e, se for o caso, o socialismo e o liberalismo juntos. Nunca use partido ou políticos como autoridade.
- **A Igreja em uma frase, sutil**, citando o documento e não pensadores (ver o guia de estilo da skill `estudio-jose`).
- Pode citar o nome de quem está sendo rebatido (ex.: a deputada), se o usuário quiser. O revisor costuma sugerir "uma deputada federal" para não parecer briga partidária.

## Checagem de fatos (obrigatória)
- **Números de empresa:** use o balanço oficial (Demonstração do Valor Adicionado e DRE) no site de relações com investidores. Muitos estão em `api.mziq.com`. Baixe o PDF, extraia com `pdftotext -layout` e procure "Valor adicionado", "Impostos, taxas e contribuições" e "Lucro líquido do exercício".
  - Cuidado com o lucro "pré-IFRS16" da imprensa: o oficial é o da DRE (no caso do Assaí, R$ 497 mi contra R$ 699 mi gerencial).
- **Números de país** (carga tributária etc.): se só houver estimativa de imprensa, escreva "estimativas" na etiqueta.
- **Frase de terceiro:** só entre aspas se você conferiu no vídeo original (transcreva o clipe com Whisper).
- Guarde uma tabela "número → de onde veio" junto do roteiro, para responder nos comentários.

## Exemplo completo
`assets/exemplo-roteiro-patrao.md`: "O patrão lucra bilhões?", com o Assaí, a tese de que o Estado explora os dois, a Rerum Novarum, o Paraguai e a CTA do Paraguai Sem Filtro. É o roteiro do vídeo aprovado, com as 26 cenas e a conferência dos números.

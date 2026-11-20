# Método de pesquisa

## Princípio
**O que importa não é onde se pesquisa. É como se reage ao que se encontra.**

O jornalismo de hoje muitas vezes não informa: ele dá a opinião sobre a informação. O trabalho tem três passos:
1. Separar o fato da opinião.
2. Ir ao documento original.
3. Achar o número ou a linha que a narrativa escondeu.

O exemplo modelo é o caso Banco do Brasil e agro (nov/2026):
- **Manchete:** "a culpa é do agro".
- **Balanço do banco:** inadimplência de 6,92% no agro, contra 9,14% na pessoa física e 16,35% no cartão de crédito.

A narrativa partiu de um dado verdadeiro e construiu uma conclusão falsa. É esse tipo de diferença que se procura.

## Antes de buscar: filtre
- Ferramentas de busca e IA tendem a mostrar primeiro a grande mídia e as referências de quem as construiu. Por isso o filtro vem antes da busca.
- Comece pelo **documento**, não pela manchete.

## Hierarquia de fontes
| Nível | O que é | Exemplos | Como usar |
|---|---|---|---|
| 1. Documento primário (de qualquer país) | O papel ou o vídeo de onde sai o fato | Balanço e release de empresa; nota oficial; lei e projeto (Câmara, Senado, Diário Oficial); processo (STF, tribunais); artigo científico; vídeo integral de discurso; transcrição oficial (Planalto, Casa Branca, Kremlin); Constituição; tratado | **Base do conteúdo.** Vai na etiqueta da tela. |
| 2. Dado técnico | Órgão ou entidade que mede um setor | IBGE, BCB, Tesouro, Receita, FGC, Cepea, CNA, FPA, CNC, Embrapa, EIA, NOAA, FAS | Usar dizendo **quem é e que interesse tem** (a FPA é a bancada do agro). |
| 3. Imprensa factual | Matéria que só noticia, sem tese | Agência Brasil para atos e números; imprensa setorial; agências de notícias; imprensa estrangeira séria | **Ponte** para achar o documento. Aproveitar o fato, nunca a opinião. |
| 4. Imprensa de opinião (de qualquer lado) | Coluna, editorial, manchete com tese | Grande mídia; também a mídia alinhada | **Não é fonte.** É objeto de análise e de desconstrução. |
| 5. Redes e caça-clique | Post sem autoria, "fonte da dark web", "a IA confirmou" | Posts no X, portais de clique, quem vende kit ou ouro | Só como objeto do desmentido. |

## Passo a passo da apuração
1. **Junte as manchetes** que circulam sobre o tema, da esquerda e da direita.
2. **Ache o documento** de cada afirmação: texto oficial, transcrição, balanço, lei, vídeo integral.
3. **Monte a tabela manchete × documento:** procede, meia verdade, não procede, não existe.
4. **Ache o número escondido**, aquele que vira o gancho ou a virada.
5. **Pergunte quem ganha:** quem lucra com a narrativa e quem a lei ou o acordo favorece. Os candidatos de sempre são bancos e sistema financeiro, lobbies, partidos, governos, ONGs e organismos internacionais. Mostre com documento: quem é o autor, quem financiou, quem fez lobby, quem se beneficia do texto.
6. **Monte a linha do tempo** com datas.
7. **Escreva cada dado com fonte, link e data.** Quando as fontes divergirem, mostre as duas versões.
8. **Feche a lista ⚠️ CONFIRMAR** com o que veio de fonte única, de veículo menos confiável, sem data ou de citação que não foi conferida na página.

## Cuidados que já pegaram erros reais
- **Citação:** só literal, com data e lugar. Se a fala existe só em paráfrase, use as palavras reais da pessoa, tiradas do vídeo original. Exemplo: a frase "a mulher moderna não menstrua…" atribuída a uma deputada não tinha registro; a fala real estava em outro programa, com outras palavras.
- **Aspas que são paráfrase:** não pôr entre aspas.
- **Corte que muda o sentido:** "optaram por não pagar" sem o "parte dos" na frente generaliza a fala.
- **Crédito errado na tela:** o número é de quem o calculou (FPA), não de quem foi citado ao lado (Cepea).
- **Métricas misturadas:** séries diferentes não entram na mesma curva. Idade embrionária contada da fecundação não se mistura com idade gestacional.
- **Proporção invertida:** 45,6% de um lado significa que **54,4%** vieram do outro, ou seja, "mais da metade", e não "quase metade".
- **Dado velho:** sempre buscar a última divulgação.
- **Arredondamentos:** os EUA têm 3 interconexões elétricas, não 4. O ataque à rede da Ucrânia afetou 225 mil consumidores, não 200 mil casas. O estreito de Taiwan tem 130 km no ponto mais estreito; 180 km é a média.
- **Origem única onde houve várias:** um boato raramente nasce de um post só. Rastreie todas as origens.
- **Omissão que o adversário explora:** inclua o fato contrário e mostre por que ele não muda a conclusão.
- **Quem é só "citado"** em investigação não é acusado. Use o termo da fonte.
- **Erratas pequenas da grande mídia:** quando houver, mostre lado a lado a notícia falsa e a errata, com data e alcance de cada uma.

## Ferramentas no ambiente (aprendido na prática)
- **Reels do Instagram:** o yt-dlp baixa um por vez; o perfil inteiro exige login. Se der limite de acesso, espere e repita mais devagar.
- **Transcrição:** speech-to-text do ElevenLabs (scribe_v1) devolve o texto e o tempo de cada palavra.
- **Fontes na tela de um vídeo:** extraia os quadros a cada 4 segundos com ffmpeg, monte uma folha de contato e leia as etiquetas.
- **YouTube:** costuma pedir verificação contra robô. Use o vídeo oficial em outro site (ex.: o site da CGTN) ou a transcrição oficial.
- **Estadão e Poder360** bloqueiam a leitura automática. Folha e O Globo, muitas vezes, só por reprodução em outros veículos. Avise quando a fonte foi lida dessa forma.
- **Wikimedia e NASA** às vezes limitam downloads. Para mapas, use o Natural Earth (domínio público).

## Formato de entrega da apuração
1. Resumo de 5 linhas.
2. Fatos numerados, cada um com fonte, link e data.
3. Divergências entre fontes.
4. Ponte com outro país, quando houver comparação institucional útil, sempre com fonte oficial ou jornal local confiável.
5. Lista ⚠️ CONFIRMAR.

Salve em `henrike/apuracoes/AAAA-MM-DD_tema.md`.

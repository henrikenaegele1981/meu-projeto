# F1: base de dados dos processados pelo 8 de janeiro de 2023

Apuração de 21/11/2026 para José Henrique Naegele. Método: `04-agente-pesquisador.md`, com o documento primário (STF) como base e a imprensa usada só como ponte ou como objeto de desconstrução.

**Arquivos desta frente**
- `F1_condenados.csv`: 124 condenados nominais, com nº da AP, data, crimes, pena, regime, multa, situação, fonte e data da fonte. Há uma coluna extra, `pena_meses`, para os cálculos.
- `F1_reus_denunciados_2023.csv`: 1.360 réus nominais. São as denúncias recebidas pelo STF entre abril e agosto de 2023, com o inquérito (4921 = incitadores/acampamento; 4922 = executores) e a fonte. A última coluna marca os 75 nomes que também aparecem no CSV de condenados.

**Convenções**
- **[CONFIRMAR]** marca dado de fonte única ou de fonte não oficial.
- "Nota STF" significa uma notícia de noticias.stf.jus.br.
- "Relatório" significa o PDF do Gabinete do Min. Alexandre de Moraes publicado no site do STF.

---

## 0. Resumo executivo

1. **Saldo oficial mais recente publicado no site do STF (29/04/2026):**
   - 1.402 "responsabilizados";
   - 552 são **ANPP** (acordos, não condenações), 39,4%;
   - 419 têm penas convertidas em restritivas de direitos (crimes menores), 29,9%;
   - 431 têm penas privativas de liberdade (crimes graves + núcleos), 30,7%;
   - 190 presos.
2. **Saldo de 19/11/2026:**
   - 1.535 responsabilizados: 598 ANPP + 482 crimes menos graves + 426 crimes graves + 29 núcleos;
   - 200 presos;
   - 1.927 denúncias.
   - Esses números saíram na imprensa (Brasil 247 e réplicas) atribuídos ao gabinete de Moraes. **Não há nota nem PDF desse balanço no site do STF** (verifiquei a API do portal de notícias até 20/11/2026). **[CONFIRMAR]**
3. **O número que a manchete esconde.** "1.400 condenados" soma acordos e condenações. Nos 850 com pena aplicada (abril/2026):
   - **47,6% receberam até 1 ano**, substituído por restritivas de direitos;
   - **41,5% receberam 14 anos ou mais**;
   - quase não há meio-termo: só 5,2% ficam entre 1 e 12 anos.
   - A pena-padrão dos executores é 14 anos (213 réus), depois 17 anos (58) e 16a6m (57).
4. **Lista nominal pública.** O STF publicou nomes e penas réu a réu só até fev/2024 (os 71 primeiros condenados) e nos núcleos. A partir de fev/2024 as notas trazem só os números das APs. Cobertura obtida: 124 nomes, cerca de 13% dos 937 condenados (1.535 − 598 ANPP), e 100% dos núcleos e da cúpula da PMDF.

---

## 1. Números oficiais: série histórica

### 1.1 Prisões de 8 e 9/1/2023

| Item | Número | Fonte (data) |
|---|---|---|
| Presos em flagrante **dentro dos prédios e na Praça dos Três Poderes** em 8/1 | **243** (161 homens, 82 mulheres) | Nota STF "8 de janeiro: a resposta imediata do STF" (03/01/2024): https://noticias.stf.jus.br/postsnoticias/8-de-janeiro-a-resposta-imediata-do-stf-aos-atos-antidemocraticos/ |
| Conduzidos do **acampamento do QG do Exército** à Academia Nacional de Polícia em 9/1 | **1.927** | idem; também no balanço do relator de 13/09/2023: https://noticias.stf.jus.br/postsnoticias/relator-divulga-balanco-dos-processos-relacionados-aos-atos-antidemocraticos-de-8-1/ |
| Total de prisões em 8 e 9/1 | **2.170** | Nota STF, 03/01/2024 |
| Liberados no mesmo dia (idosos, mães de crianças, comorbidades) | **775** | Notas STF de 13/09/2023 e 03/01/2024 |
| Audiências de custódia (11 a 17/1/2023) | 1.397, com **938 preventivas** e **459 liberdades provisórias** | Balanço STF de 13/09/2023 |
| Liberdades provisórias entre 27/2 e 16/3/2023 | 680 | idem |
| Presos em 13/09/2023 | 117 | idem |
| Presos preventivamente em jan/2024 | 66 | Nota STF, 03/01/2024 |

**Inconsistência no próprio STF.** A nota de 07/01/2024 (https://noticias.stf.jus.br/postsnoticias/relator-no-stf-tomou-mais-de-6-mil-decisoes-em-2023-sobre-8-de-janeiro/) fala em "1.929 conduzidos" e "1.397 detidos". A de 03/01/2024 fala em 1.927 conduzidos, dos quais 1.152 ficaram presos. A conta 1.927 − 775 = 1.152 fecha. A dos 1.397 não fecha: a diferença provável são os 243 presos de 8/1 (1.152 + 243 = 1.395), mas isso é inferência minha.

**A imprensa repete números próximos, mas com outro recorte.**
- A PF liberou 599 pessoas "por questões humanitárias" em 10/1/2023 e manteve 527 presas (O Povo, 10/01/2023): https://www.opovo.com.br/noticias/politica/2023/01/10/amp/atos-golpistas-pf-libera-599-por-questoes-humanitarias-e-mantem-527-presos.html
- Agência Brasil (07/01/2025) usa "2.172 presos em flagrante".

### 1.2 Denúncias, réus, condenações, acordos e absolvições: evolução

| Data do balanço | Denúncias | Condenados | ANPP | Total "responsabilizados" | Absolvidos | Presos | Fonte |
|---|---|---|---|---|---|---|---|
| 13/09/2023 | 1.345 recebidas (1.113 no INQ 4921 suspensas para ANPP; 232 no INQ 4922) | 0 (julgamentos começam em 14/9) | 0 | — | — | 117 | Nota STF 13/09/2023 |
| 03/01/2024 | 1.354 ações penais | 30 | 38 | — | — | 66 | Nota STF 03/01/2024 |
| 08/11/2024 | — | — | — | 741 | — | — | Nota STF 08/11/2024: https://noticias.stf.jus.br/postsnoticias/741-golpistas-acusados-pela-pgr-de-crimes-pelo-8-1-ja-foram-responsabilizados-penalmente/ |
| 07/01/2025 | — | 371 (225 graves, 146 menos graves) | 527 (R$ 1,7 mi arrecadados) | 898 | 5 | 71 cumprindo pena + 30 aguardando trânsito; **122 foragidos** | Nota STF: https://noticias.stf.jus.br/postsnoticias/em-dois-anos-stf-responsabilizou-898-pessoas-por-atos-antidemocraticos-de-8-de-janeiro/ |
| 12/08/2025 | 1.628 ações penais abertas (518 graves, 1.110 menos graves) | 638 (279 graves, 359 menos graves) | 552 | 1.190 | **10** | 29 preventivos + 112 definitivos + 44 em domiciliar; **61 extradições pedidas** | Nota STF: https://noticias.stf.jus.br/postsnoticias/atos-antidemocraticos-de-8-1-1-190-pessoas-ja-foram-responsabilizadas/ |
| 08/01/2026 | — | 391 graves + 415 menos graves + 29 núcleos (= 835) | **564** | 1.399 | 2 nos núcleos | **179** (detalhe em 1.3) | Nota e relatório STF: https://noticias.stf.jus.br/postsnoticias/atos-antidemocraticos-de-8-de-janeiro-stf-avanca-na-responsabilizacao-dos-envolvidos/ · PDF: https://noticias.stf.jus.br/wp-content/uploads/2026/01/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro_de_2026_ONLINE_FINAL.pdf |
| **29/04/2026** (último no site do STF) | **1.878** recebidas (1.160 incitadores, 628 executores, 31 núcleos); 67 em recebimento; 177 investigações; 144 arquivamentos | 402 graves + 419 menos graves + 29 núcleos (= 850) | **552** | **1.402** | 2 nos núcleos | **190** | Nota: https://noticias.stf.jus.br/postsnoticias/stf-divulga-balanco-atualizado-sobre-investigacoes-e-condenacoes-por-atos-antidemocraticos/ · PDF: https://noticias.stf.jus.br/wp-content/uploads/2026/04/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro____29-4-26-15h34.pdf |
| 19/11/2026 **[CONFIRMAR]** | 1.927 recebidas; 20 em recebimento; 121 investigações; 179 arquivamentos | 426 graves + 482 menos graves + 29 núcleos (= 937) | **598** (382 cumpridos, 216 em curso) | **1.535** | não informado (a Revista Oeste falaria em 17; página bloqueada, não verificado) | **200** (13,03%) | Brasil 247, 19/11/2026: https://www.brasil247.com/brasil/relatorio-do-stf-registra-200-presos-por-acoes-golpistas-e-1-535-reus-ja-responsabilizados · réplica: https://www.plantaobrasil.net/noticias/164573-stf-contabiliza-1-535-responsabilizados-por-ataques-golpistas-de-8-de-janeiro |

**Pontos a confirmar antes de gravar**
- **Os ANPP caíram de 564 (jan/2026) para 552 (abr/2026).** O relatório não explica: pode ser rescisão de acordos ou recontagem. **[CONFIRMAR]**
- **Os "condenados" mudam conforme o veículo.** "1.399/1.402 condenados" é a soma do STF, que inclui os ANPP. Quem fez acordo confessou, mas não foi condenado: o ANPP extingue a punibilidade quando é cumprido. A Gazeta do Povo (07/01/2026) dá "810 condenados" e a O Povo (08/01/2026) dá "1.039 condenados (497 à prisão, 542 com penas alternativas)". Nenhum dos dois bate com o relatório.
- **A pena de Bolsonaro difere entre documentos do STF.** A nota de 08/01/2026 diz "27 anos e 6 meses". A nota do julgamento (11/09/2025), o relatório de abril/2026 e a nota de 03/07/2026 dizem **27 anos e 3 meses**. Use 27a3m.
- **PGR.** Não localizei balanço próprio da PGR no período: o limite de buscas da sessão acabou. Os números de denúncias acima são as denúncias da PGR recebidas, contadas pelo STF.

### 1.3 Presos hoje: regime, domiciliar e tornozeleira

**08/01/2026: 179 presos** (relatório STF; detalhe por Congresso em Foco, 08/01/2026: https://www.congressoemfoco.com.br/noticia/115383/8-de-janeiro-veja-perfil-dos-presos-tres-anos-apos-os-ataques)

| Situação | Pessoas |
|---|---|
| Regime fechado com condenação definitiva | 114 |
| Domiciliar com condenação definitiva | 15 |
| Domiciliar após sentença | 22 |
| Domiciliar antes da condenação | 13 |
| Preventiva | 8 |
| Preventiva decorrente de condenação | 7 |

**29/04/2026: 190 presos** (10,12% dos réus), segundo o relatório STF.

| Tipo | Situação | Pessoas |
|---|---|---|
| 169 definitivos | Regime fechado | 111 |
| | Semiaberto | 3 |
| | Domiciliar | 55 |
| 21 processuais | Preventivas | 5 |
| | Preventiva em decorrência da condenação | 1 |
| | Domiciliares antes do trânsito em julgado | 15 |

**19/11/2026: 200 presos** (Brasil 247) **[CONFIRMAR]**
- 183 definitivos;
- 17 processuais: 7 preventivas e 10 domiciliares.

**Tornozeleira**
- Não há contagem oficial atual.
- Até jan/2025, os 146 condenados por crimes menores usavam tornozeleira por um ano (nota STF de 07/01/2025).
- Em 27/04/2026, 19 condenados com mais de 60 anos passaram à domiciliar humanitária com tornozeleira (nota STF: https://noticias.stf.jus.br/postsnoticias/stf-concede-prisao-domiciliar-humanitaria-a-19-condenados-por-atos-ligados-a-tentativa-de-golpe-de-estado/).
- Em 27/12/2025, nove condenados dos núcleos 2 a 4 também foram para a domiciliar com tornozeleira.

**Contraste oficial × associações.** A Gazeta do Povo (07/01/2026), com dados de familiares, falava em "pelo menos 101 presos" e "36 em domiciliar" (https://www.gazetadopovo.com.br/vida-e-cidadania/tres-anos-do-81-mais-de-100-seguem-presos-e-centenas-sao-procuradas/). O STF, no dia seguinte, dava 179. A diferença provavelmente vem do critério: o STF inclui a cúpula do golpe e as domiciliares. Isso é inferência minha.

### 1.4 Foragidos

| Data | Número | Fonte |
|---|---|---|
| 13/09/2023 | 22 foragidos | STF |
| 07/01/2025 | **122 foragidos**; extradição pedida para metade, após rompimento da tornozeleira e saída do país | STF |
| 12/08/2025 | 61 extradições pedidas, sob sigilo | STF |
| nov/2024 | Justiça argentina ordenou a prisão de 61 foragidos | Folha PE: https://www.folhape.com.br/politica/justica-da-argentina-ordena-prisao-de-61-foragidos-do-8-de-janeiro/372818/ |
| jun/2024 | PF identificou 65 condenados que pediram asilo na Argentina | O Antagonista: https://oantagonista.com.br/brasil/pf-identifica-65-condenados-do-8-de-janeiro-na-argentina/ **[CONFIRMAR]** |
| dez/2025 | Argentina decidiu extraditar 5 brasileiros presos lá, com recurso cabível | SBT News: https://sbtnews.sbt.com.br/noticia/mundo/justica-da-argentina-decide-pela-extradicao-de-foragidos-do-8-de-janeiro **[CONFIRMAR]** |
| mar/2026 | Um condenado a 13 anos obteve refúgio na Argentina | Diário do Comércio: https://diariodocomercio.com.br/mix/apos-ser-condenado-a-13-anos-de-prisao-brasileiro-foge-para-a-argentina-e-consegue-liberdade/ **[CONFIRMAR]** |
| jan/2026 | "Mais de 230 foragidos", segundo associações | Gazeta do Povo, 07/01/2026 **[CONFIRMAR]** |
| 25/11/2025 | Alexandre Ramagem foragido **nos EUA**, mandado de prisão no BNMP | Nota STF: https://noticias.stf.jus.br/postsnoticias/ap-2668-stf-determina-cumprimento-imediato-da-pena-dos-sete-reus-do-nucleo-1-da-tentativa-de-golpe/ |

**Destino dos foragidos.** O destino dominante, pela imprensa, é a **Argentina**. Não achei número oficial por país, nem registro de foragidos no **Paraguai**: pesquisar em ABC Color e Última Hora numa próxima rodada.

### 1.5 Mortos

- **Cleriston Pereira da Cunha ("Clezão")**, 46 anos. Morreu em 20/11/2023 na Papuda, após mal súbito no banho de sol. Era réu preso sem julgamento. Fontes: Agência Brasil (https://agenciabrasil.ebc.com.br/justica/noticia/2023-11/preso-pelo-8-de-janeiro-tem-mal-subito-e-morre-no-presidio-da-papuda) e CNN Brasil. É o único morto sob custódia confirmado.
- O STF esclareceu, em 23/01/2024, que outro detento morto de meningite na Papuda **não era preso do 8/1** (https://noticias.stf.jus.br/postsnoticias/stf-esclarece-que-detento-que-faleceu-de-meningite-na-papuda-nao-era-preso-de-8-1/).
- **A Asfav (Associação dos Familiares e Vítimas do 8 de Janeiro) contabiliza 8 réus ou condenados mortos até 27/03/2026.** Fonte: Gazeta do Povo, 28/03/2026 (https://www.gazetadopovo.com.br/republica/morre-jose-eder-lisboa-condenado-8-de-janeiro-argentina/). **[CONFIRMAR: fonte associativa, sem óbito oficial listado pelo STF]**

| Nome | O que se sabe |
|---|---|
| Cleriston Pereira da Cunha | Papuda, 20/11/2023 |
| Éder Parecido Jacinto | Morte divulgada em 04/03/2024; estava em liberdade provisória |
| Kleber de Freitas | — |
| Antônio Marques da Silva | 29/10/2023, acidente de trabalho |
| Giovani (ou Giovanni) Carlos dos Santos | 24/01/2024, São José dos Campos-SP, queda de árvore |
| Jony Figueiredo da Silva | — |
| José Fernando Honorato de Azevedo | — |
| José Éder Lisboa | 64 anos, foragido; morreu na Argentina, por Guillain-Barré |

As datas de Éder, Antônio e Giovani vêm da Gazeta do Povo, 04/03/2024: https://www.gazetadopovo.com.br/vida-e-cidadania/reu-do-8-1-morre-apos-seis-meses-de-liberdade-provisoria-causa-da-morte-nao-foi-revelada/

### 1.6 ANPP: o que o acordo exige

O acordo foi oferecido só a quem respondia por incitação (CP 286) e associação criminosa (CP 288): "acampados em frente aos quartéis, mas não há provas de que tenham participado da tentativa de golpe" (nota STF de 12/08/2025).

**Exigências comuns**
- confissão;
- serviços à comunidade;
- multa;
- proibição de redes sociais abertas;
- curso presencial "Democracia, Estado de Direito e Golpe de Estado", de 12 h, do MPF;
- não cometer novo crime.

**Como as condições variaram**

| Data | Serviços à comunidade | Multa | Fonte |
|---|---|---|---|
| dez/2023 (38 primeiros acordos) | 300 h | sim | https://noticias.stf.jus.br/postsnoticias/stf-valida-38-acordos-e-concede-liberdade-provisoria-a-46-acusados-pelos-atos-golpistas-de-8-1/ |
| jan/2025 | 150 h | — | Nota STF |
| ago/2025 | — | R$ 5 mil | Nota STF |
| fev/2026 (dois militares do Núcleo 3) | 340 h | R$ 20 mil | https://noticias.stf.jus.br/postsnoticias/stf-homologa-acordo-entre-pgr-e-dois-militares-do-nucleo-3-da-tentativa-de-golpe/ |

**Arrecadação.** R$ 1,7 milhão até jan/2025 (STF). Cerca de R$ 3 milhões até o fim de 2025, segundo a Gazeta do Povo **[CONFIRMAR]**.

**Quem recusou o acordo** e foi condenado por crimes menores recebeu (nota STF de 18/10/2024: https://noticias.stf.jus.br/postsnoticias/stf-tem-maioria-para-condenar-mais-15-denunciados-por-atos-antidemocraticos-que-rejeitaram-acordo-para-encerrar-acao/):
- 1 ano de reclusão, substituído por 225 h de serviços;
- curso;
- proibição de sair da comarca e de usar redes sociais;
- passaporte retido;
- multa de 10 salários mínimos;
- rateio de R$ 5 milhões de danos morais coletivos;
- **perda da primariedade**.

Quem descumpriu cautelares (tornozeleira, comparecimento) recebeu **2 anos e 5 meses**, sem substituição.

### 1.7 Fato novo: Lei da Dosimetria (Lei 15.402/2026)

- **Maio de 2026:** a lei foi promulgada depois da derrubada do veto. Ela altera o cálculo das penas.
- **09/05/2026:** Moraes **suspendeu a aplicação da lei às execuções do 8/1** até o Plenário julgar as ADIs 7966 e 7967 (nota STF: https://noticias.stf.jus.br/postsnoticias/relator-suspende-aplicacao-da-lei-da-dosimetria-a-execucoes-penais-no-stf/).
- **Julgamento marcado:** Plenário virtual de **4 a 15/12/2026**, para as ADIs 7966 a 7969. Fonte: Congresso em Foco, https://www.congressoemfoco.com.br/noticia/131752/moraes-libera-processos-da-lei-da-dosimetria-para-julgamento **[CONFIRMAR: a data não aparece em nota do STF até 20/11]**.
- **Posições:** a PGR defendeu a constitucionalidade da lei. A AGU a questionou.
- **Impacto:** as penas da tabela abaixo podem mudar em dezembro.

---

## 2. Lista nominal: o que é público e o que foi montado

**Fontes procuradas**
- **Encontrado:** o portal de notícias do STF, lido pela API pública do WordPress, com 8.228 notícias de 08/01/2023 a 20/11/2026 lidas e 1.072 ligadas ao tema.
- **Bloqueado:** o portal processual (portal.stf.jus.br) e o de transparência devolvem 403 (firewall).
- **Sem resposta útil:** a API de jurisprudência deu erro.
- **Não encontrado:** planilha consolidada em GitHub ou veículo, e lista completa em Wikipédia ou imprensa. O limite de buscas web acabou antes de vasculhar Metrópoles, Poder360 e a Asfav: fica para uma próxima rodada.

**Até quando o STF publicou nomes**
- Nomes **e** penas réu a réu: só de 14/09/2023 a 15/02/2024, ou seja, os 71 primeiros condenados, todos executores.
- Depois disso, só os números das APs ("Foram julgados os réus nas APs 1061, 1062…"). Exceções:
  - casos de repercussão (Fátima de Tubarão, Débora);
  - os núcleos e a PMDF;
  - a lista de 19 domiciliares humanitárias (27/04/2026), com nome e pena total.

### 2.1 `F1_condenados.csv`: 124 nomes

| Bloco | Nomes | Fonte |
|---|---|---|
| Executores julgados no Plenário (set/2023 a fev/2024) | 71 | Notas STF, com AP e pena de cada um |
| Outros executores nominais (Fátima de Tubarão; João de Oliveira Antunes Neto; Débora) | 3 | Notas STF |
| Domiciliares humanitárias de 27/04/2026 (EP + pena total) | 13 novos (6 já estavam na lista) | Nota STF |
| Imprensa (Antônio Cláudio Alves Ferreira, AP 2331; Ana Priscila Silva de Azevedo; José Éder Lisboa) | 3 | **[CONFIRMAR]** |
| Núcleo 1, AP 2668 (11/09/2025) | 8 | Nota STF |
| Núcleo 4, AP 2694 (21/10/2025) | 7 | Nota STF |
| Núcleo 3, AP 2696 (18/11/2025) | 9 (dois depois trocaram a pena por ANPP) | Nota STF |
| Núcleo 2, AP 2693 (16/12/2025) | 5 | Nota STF |
| Cúpula da PMDF, AP 2417 (05/12/2025) | 5 | Nota STF |

**Notas sobre os nomes**
- O réu da AP 2331 (o relógio de D. João VI) aparece sem nome na nota do STF. O nome vem da imprensa.
- Alguns nomes dos núcleos estão abreviados como na nota do STF ("Carlos Rocha", "Reginaldo Abreu", "Marcelo Bormevet", "Marília Alencar"). Não completei de memória.

**Cobertura**
- 124 de **937** condenados com pena: 13,2% (base de 19/11/2026, **[CONFIRMAR]**).
- 124 de 850: 14,6% (base de 29/04/2026).
- Por grupo:
  - **núcleos: 29/29 (100%)**;
  - **PMDF: 5/5 (100%)**;
  - executores (crimes graves): 90 de 426, ou 21%;
  - crimes menos graves: **0 de 482** (o STF nunca publicou esses nomes).

**Viés da amostra.** Os nomes conhecidos são dos primeiros julgamentos, os mais duros: mediana de 16a6m. A amostra **não** representa os condenados a 1 ano.

**Lacunas.** Cidade, UF e idade só aparecem em casos pontuais, porque as notas do STF quase nunca informam.
- Apucarana-PR, 24 anos (Mateus Lázaro);
- São Carlos-SP, 64 anos (José Éder);
- SC (Fátima);
- BA (Débora);
- "mais de 60" para os 19 da domiciliar humanitária;
- Iraci Nagoshi, 73 anos, pela Gazeta do Povo.

### 2.2 `F1_reus_denunciados_2023.csv`: 1.360 nomes (bônus)

São as listas de "denúncias aceitas" publicadas pelo STF em nove blocos, de 25/04 a 21/08/2023.
- **1.113** no INQ 4921 (incitação e associação: o pessoal do acampamento). Bate exatamente com as "1.113 ações suspensas para ANPP" do balanço de 13/09/2023.
- **233** no INQ 4922 (executores). O balanço fala em 232.
- 14 em petições conexas.

Isso permite, por exemplo, verificar se uma pessoa citada num vídeo era do acampamento ou da invasão.

**Limitação.** Os blocos 5 e 6 (381 nomes) estão atribuídos ao INQ 4921 pela nota de pauta, porque a nota de aceite não separa por inquérito. Há 2 nomes repetidos entre blocos (Edna Dias Sales; José Paulo Alfonso Barros). Não somei as denúncias de 2024 a 2026.

---

## 3. Estatísticas

### 3.1 Universo completo: tabela oficial de penas (relatório STF de 29/04/2026, 1.402 réus)

**Distribuição dos 850 condenados com pena**

| Faixa | Réus | % dos 850 |
|---|---|---|
| até 1 ano (inclui 1 caso de 3 meses) | 405 | 47,6% |
| > 1 a 4 anos (22 com 2a5m por descumprir cautelar) | 27 | 3,2% |
| > 4 a 8 anos | 6 | 0,7% |
| > 8 a < 12 anos | 11 | 1,3% |
| 12 a < 14 anos (42 com 13a6m) | 48 | 5,6% |
| **14 a < 16 anos (213 com 14a)** | **216** | **25,4%** |
| 16 a < 18 anos (58 com 17a; 57 com 16a6m) | 123 | 14,5% |
| 18 anos ou mais (todos dos núcleos) | 14 | 1,6% |
| ANPP (fora da conta) | 552 | — |

**Resumo**
- **Mínimo:** 3 meses.
- **Máximo:** 27 anos e 3 meses (Bolsonaro).
- **Mediana dos 850:** cerca de 2 anos e 5 meses. A distribuição é bimodal: 1 ano ou 14 anos ou mais.
- **Mediana dos 419 com pena acima de 3 anos ("graves"):** 14 anos.
- **Média dos 850:** 7,85 anos.
- **Penas de 14 anos ou mais:** **353 réus**, ou **41,5% dos condenados com pena** e **25,2% dos 1.402 "responsabilizados"**.
- **Penas acima de 18 anos:** 14 réus, **todos dos núcleos** (relatório de janeiro/2026).
- **Executores comuns** (sem cargo e sem núcleo): a nota STF de 07/01/2025 dava penas de 3 anos a 17 anos e 6 meses. A tabela de abr/2026 não tem nenhuma pena de 17a6m, e o teto fora dos núcleos aparece em 17 anos. **[CONFIRMAR]**

**Por que a pena-padrão mudou**
- **Plenário (set/2023 a fev/2024):** sem maioria na dosimetria, prevaleceu o "voto médio" de Zanin, com 16a6m para quem invadiu e 13a6m para casos atenuados.
- **A partir de mar/2024:** a régua passa a 17 anos ou 14 anos.
- **Desde dez/2023:** as ações novas foram para a 1ª Turma, por emenda regimental.

### 3.2 Idade e sexo: só para os presos (o STF não publica a idade de todos os réus)

Relatório de 08/01/2026, 179 presos (preventivas + preventivas por condenação + definitivas):

| Faixa | Presos |
|---|---|
| até 30 anos | 8 |
| 31 a 40 anos | 38 |
| 41 a 50 anos | **52** |
| 51 a 60 anos | 41 |
| 61 a 65 anos | 20 |
| 66 a 70 anos | 13 |
| mais de 70 anos | 7 |

- **Pessoas com mais de 60 anos:** 40, ou 22%.
- **Sexo:** 49 mulheres (27%) e 130 homens.
- **Inconsistência no PDF.** A tabela de domiciliares (50) repete o rótulo "66 a 70 anos" e soma por cima dos 179. **[CONFIRMAR no PDF]**
- **Relatório de abril/2026:** traz tabelas parecidas para os 190 presos. A extração do PDF ficou embaralhada e precisa de conferência visual antes de citar faixa por faixa.

### 3.3 UF

**Nenhum balanço oficial traz a UF de origem.** Na amostra nominal só há UF em menos de 10 casos, o que é insuficiente para estatística. Caminho para obter: pedido via LAI ao STF, ou a Defensoria Pública da União (DPU), que atuou em parte das defesas.

### 3.4 Amostra nominal (CSV, n = 124), com o viés descrito em 2.1

- Mediana de 16a6m.
- 93 dos 124 (75%) com 14 anos ou mais.
- Penas mais frequentes: 16a6m (45), 13a6m (19), 17a (12), 14a (12).
- 29 estão hoje em domiciliar, segundo a fonte de status citada em cada linha.

---

## 4. Votos divergentes típicos

| Ministro | Proposta | Exemplos (nota STF) |
|---|---|---|
| **Nunes Marques** (revisor no Plenário) | Absolvia de golpe de Estado (359-L/M) e de associação criminosa armada por falta de prova individualizada: "nenhuma testemunha afirma que tenha praticado ato de violência". Condenava só por **dano qualificado e deterioração de patrimônio tombado**, com cerca de **2 anos e 6 meses**. Em vários casos absolvia de tudo ou desclassificava para **incitação ao crime (CP 286)**. Fixava danos morais coletivos em **R$ 100 mil**, contra R$ 30 milhões. Na fase de denúncia, votou pela **incompetência do STF** (réus sem foro). Votou pela absolvição dos que recusaram o ANPP. | AP 1060 Aécio (14/09/2023): https://noticias.stf.jus.br/postsnoticias/stf-condena-primeiro-reu-pelos-atos-antidemocraticos-de-8-1/ · APs 1505/1109/1413 (03/10/2023) · APs 1064/1067/1082/1147 (27/10/2023) · recusas de ANPP (18/10/2024) |
| **André Mendonça** | Condenava **só por abolição violenta do EDD (359-L)**, por entender que ela absorve o golpe de Estado. Às vezes somava a associação criminosa armada. Em Aécio, pena de **7a1m de reclusão + 10m de detenção, em regime aberto**. Absolvia de tudo quem não tinha prova de participação na invasão (APs 1082, 1147, 1134, 1426). Pediu destaque, levando o caso ao Plenário físico, em APs como 1129, 1144 e 1063. Na denúncia, também votou pela incompetência. | Mesmas notas |
| **Luís Roberto Barroso** | Divergência técnica: o **golpe de Estado absorve a abolição violenta** (o inverso de Mendonça). Afastava o 359-L. Pena de cerca de **10 anos + 1a6m** no caso Aécio. | idem |
| **Cristiano Zanin** (e Fachin) | Acompanhava as condenações, mas propunha **penas menores**: 15 anos para Aécio, e 16a6m ou 13a6m no lugar de 17 ou 14. Seu "voto médio" virou a pena oficial de 2023 até o início de 2024. | Notas de 20/10, 27/10 e 13/11/2023 |
| **Cármen Lúcia e Fachin** | Na AP 1380 (réu indígena), propuseram aplicar o Estatuto do Índio (redução de 1/6 e semiliberdade). Ficaram vencidos. | https://noticias.stf.jus.br/postsnoticias/stf-condena-mais-14-reus-por-atos-antidemocraticos-de-8-1/ (08/04/2024) |
| **Luiz Fux** (1ª Turma, 2025) | **Ponto de virada:** acompanhou Moraes nas primeiras condenações (2023) e depois passou a divergir. No caso Débora, propôs **1 ano e 6 meses só por dano**, contra 14 anos. Pediu vista e levantou incompetência e a remessa ao Plenário. No **Núcleo 1**, anulava o processo (incompetência, cerceamento de defesa), **absolveu 6 de 8** e condenou Cid e Braga Netto só por 359-L. Sustentou que "acampamentos, faixas e aglomerações são manifestações políticas e não configuram crime" e que o golpe exige deposição de governo constituído. Absolveu **todos os 7 do Núcleo 4**. | Débora (07/05/2025): https://noticias.stf.jus.br/postsnoticias/stf-condena-mais-42-pessoas-por-participacao-nos-atos-antidemocraticos-de-8-1/ · Núcleo 1 (10/09/2025): https://noticias.stf.jus.br/postsnoticias/ministro-luiz-fux-absolve-seis-reus-na-acao-sobre-golpe-de-estado/ · Núcleo 4 (21/10/2025) |

### Absolvições nominais confirmadas pelo STF

| Nome ou caso | Data | Motivo | Fonte |
|---|---|---|---|
| Geraldo Filipe da Silva, AP 1423 | 15/03/2024 | Morador de rua apanhando de manifestantes; falta de provas, com a PGR a favor da absolvição | https://noticias.stf.jus.br/postsnoticias/atos-antidemocraticos-mais-14-reus-sao-condenados-pelo-stf/ |
| Réu da AP 1373, sem nome | out/2024 | Situação de rua | — |
| Réu da AP 2556, sem nome | mar/2025 | Inimputável: psicose; tratamento ambulatorial | — |
| Gen. Estevam Cals Theophilo Gaspar de Oliveira (Núcleo 3) | — | Delação de Cid sem corroboração | — |
| Delegado Fernando de Sousa Oliveira (Núcleo 2) | — | — | — |
| Maj. Flávio Silvestre de Alencar e Ten. Rafael Pereira Martins (PMDF) | — | — | — |

- **Absolvidos por julgamento:** 3 na nota de fev/2024, absolvidos só de dano e deterioração (presos a caminho da Praça).
- **Total oficial:** 10 até ago/2025, mais 2 dos núcleos e 2 da PMDF no fim de 2025.

---

## 5. Onde a narrativa e o número se separam (matéria-prima para roteiro)

**1. "STF condenou 1.400 pessoas".**
- O número verdadeiro é **1.402 responsabilizados** (abr/2026).
- Desses, **552 não foram condenados**: fizeram acordo com confissão.
- Dos 850 condenados, **405 pegaram até 1 ano** convertido em serviço comunitário.
- A pena de prisão longa (14 anos ou mais) atinge **353 pessoas**.
- Os dois lados usam o "1.400": um para dizer "a democracia respondeu", o outro para dizer "1.400 presos políticos". Nenhum dos dois é o retrato.

**2. "Penas de 14 a 17 anos para quem só estava lá".**
- O STF fundamenta na tese do **crime multitudinário** (autoria coletiva).
- As notas mostram que os 14 a 17 anos recaíram sobre os 243 presos dentro ou junto dos prédios e sobre outros identificados por câmera ou DNA.
- Os do acampamento (INQ 4921, 1.113 réus) receberam ANPP ou 1 ano.
- O ponto que se sustenta é outro: **a soma de cinco crimes por pessoa**, inclusive golpe **e** abolição juntos. Três ministros (Mendonça, Barroso, Fux) entenderam que um absorve o outro, o que reduziria a pena. Isso é questão de dosimetria e está na pauta da Lei da Dosimetria.

**3. "Presos políticos às centenas".**
- Oficialmente são 179 a 200 presos.
- Mais de 1/4 em domiciliar.
- 22% com mais de 60 anos (jan/2026).

**4. Foragidos.**
- STF: 122 (jan/2025).
- Associações: "mais de 230" (jan/2026).
- A Argentina de Milei é o destino que a imprensa documenta.

**5. Mortes.**
- Uma morte sob custódia: Cleriston. Ele tinha pedido de liberdade pendente.
- A Asfav fala em 8 óbitos de réus e condenados ao todo. A maioria morreu fora da prisão e sem nexo comprovado.

---

## 6. Pendências e próximos passos

1. Conferir o balanço de 19/11/2026 no PDF original, que ainda não foi publicado no site do STF.
2. Pedir via LAI ao STF a lista de réus com UF e idade, e a lista de foragidos por país. Tentar a consulta processual de cada AP de um computador sem bloqueio do firewall.
3. Buscar a lista da Asfav e reportagens de Metrópoles e Poder360 com nomes posteriores a fev/2024. O limite de buscas web desta sessão acabou: é preciso nova rodada.
4. Resultado das ADIs da Lei da Dosimetria (4 a 15/12/2026): recalcular a seção 3.
5. Conferir no PDF de abril/2026 a tabela de idade dos 190 presos.

## Fontes principais

**Primárias: STF**
- Relatório de 29/04/2026 (PDF): https://noticias.stf.jus.br/wp-content/uploads/2026/04/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro____29-4-26-15h34.pdf
- Relatório de 08/01/2026 (PDF): https://noticias.stf.jus.br/wp-content/uploads/2026/01/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro_de_2026_ONLINE_FINAL.pdf
- Notas STF citadas acima, uma por linha do CSV.
- API do portal: https://noticias.stf.jus.br/wp-json/wp/v2/postsnoticias

**Imprensa, como ponte ou contraste** (cada uma citada no ponto em que é usada)
- Brasil 247 e Plantão Brasil
- Gazeta do Povo
- Correio 24 Horas: https://www.correio24horas.com.br/brasil/de-debora-do-batom-a-clezao-veja-quem-esta-preso-solto-e-morto-entre-os-condenados-por-moraes-pelo-8-de-janeiro-apos-tres-anos-1026
- O Povo: https://www.opovo.com.br/noticias/politica/2026/01/08/atos-de-8-de-janeiro-o-que-aconteceu-e-quem-foi-condenado.html
- Congresso em Foco
- Agência Brasil
- Jornal Grande Bahia: https://jornalgrandebahia.com.br/2026/01/stf-conclui-julgamentos-do-8-de-janeiro-condena-1-399-reus-e-mantem-179-presos-tres-anos-apos-atos-golpistas/

# FRENTE 1: SPLIT PAYMENT (reforma tributária)
Pesquisa de pauta para @josehenriquenaegele · apurado em 21/11/2026
Regra usada: documento primário primeiro (nível 1). A imprensa entra só como ponte (nível 3) ou como objeto de desconstrução (nível 4/5).
Legenda: **[OK]** conferido no documento primário · **[PONTE]** só imprensa, sem ato oficial localizado · **[CONFIRMAR]** não fechou, não gravar como fato.

---

## 0. O que as buscas pedem (autocomplete Google/YouTube)
Os sinais de busca mais fortes, que pautam os ganchos:
- **Prazo:** "adiado para 2027 / 2028", "ficou para 2028", "começa quando", "será obrigatório / opcional", "opcional em 2027"
- **Quem é afetado:** "afeta pessoa física", "afeta mei", "simples nacional", "maquininha", "no pix", "split payment pix", "imposto pix split payment"
- **Comparação:** "maior que o pix", "deu certo em outros países", "quais países usam", "eua"
- **Política:** "quem aprovou", "quem votou a favor", "de quem foi a ideia", "flavio bolsonaro", "daniela marques" (Daniella Marques, coordenadora econômica da campanha de Flávio)
- **Pix / Receita:** "imposto pix é verdade", "imposto pix fato ou fake", "imposto sobre pix 2026/2027", "receita federal controla pix", "receita federal cruza dados pix", "normativa receita federal pix pdf"

---

## 1. O que é o split payment na lei

### 1.1 Base legal [OK]
- **EC 132/2023** criou o IBS (estados e municípios) e a CBS (União), que substituem ICMS, ISS, PIS, Cofins e parte do IPI.
- **LC 214, de 16/01/2025** (origem: PLP 68/2024), **arts. 31 a 35**: "Do Recolhimento na Liquidação Financeira (split payment)".
  - Texto: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
- **LC 227, de 13/01/2026** (DOU de 14/01/2026; origem: PLP 108/2024) criou o Comitê Gestor do IBS e reescreveu partes dos arts. 31 a 33.
  - Senado: https://www12.senado.leg.br/noticias/materias/2026/01/14/reforma-tributaria-lei-cria-comite-gestor-do-ibs-e-define-regras-do-imposto

### 1.2 O que dizem os artigos [OK, redação vigente no Planalto]
- **Art. 31, caput:** os prestadores de serviço de pagamento eletrônico e as instituições operadoras de sistemas de pagamento "deverão segregar e recolher ao Comitê Gestor do IBS e à RFB, no momento da liquidação financeira da transação", o IBS e a CBS.
  - **Tradução:** o banco ou a maquininha separa o imposto no instante em que o dinheiro cai e o envia direto ao governo. A empresa recebe só o líquido.
- **Art. 31, §3º:** vale também para participantes e arranjos "que não estão sujeitos à regulação do Banco Central do Brasil".
- **Art. 31, §1º (redação da LC 227/2026):** há dois procedimentos, o **padrão** (art. 32) e o **simplificado** (art. 33).
- **Art. 32, procedimento padrão (o "inteligente"):**
  - quem inicia o pagamento informa os valores de IBS e CBS vinculados à nota fiscal;
  - antes de liberar o dinheiro, o prestador consulta o sistema da RFB e do CGIBS e recolhe só o débito que ainda não foi pago (§3º);
  - se a consulta falhar, recolhe pelo valor informado, e o governo devolve o excedente em até **3 dias úteis** (§4º).
- **Art. 33, procedimento simplificado:**
  - é **opcional** (caput reescrito pela LC 227/2026);
  - aplica um **percentual preestabelecido** sobre o valor da operação (§1º). O CGIBS fixa o do IBS e a RFB, o da CBS, e esse percentual "não guarda relação com o débito efetivo" (§2º);
  - devolução do excedente em até 3 dias úteis após a apuração (§4º);
  - o ato conjunto pode **impor** o simplificado enquanto o padrão não funcionar (§6º).
- **Art. 34:**
  - o recolhimento ocorre na data da liquidação; em venda parcelada, por parcela;
  - a antecipação de recebíveis não muda a obrigação;
  - os bancos **não** são responsáveis tributários.
- **Art. 35:**
  - a União e o CGIBS bancam o sistema;
  - para compras de **quem não é contribuinte do regime regular** (consumidor final, PF), o split deve entrar **simultaneamente nos principais meios de pagamento do varejo** (§§1º e 3º);
  - ato conjunto define a **implantação gradual** e "pode prever hipóteses facultativas" (§2º).

### 1.3 Modalidades nos manuais oficiais [OK]
Fonte: **Manual de Operações do Split Payment, v1.0.1, set/2026** (CGIBS + RFB), https://www.cgibs.gov.br/upload/arquivos/202609/24101007-split-payment-manual-de-operacoes-v1-0-1.pdf

| Modelo | Arranjos | Como funciona |
|---|---|---|
| **Inteligente** | Pix Estático, TED, TEF (iniciados pelo pagador) | O valor do imposto é "integralmente determinado pelo originador" e não há correção do governo. |
| **Super Inteligente** | Boleto, Pix Dinâmico, Pix Automático (iniciados pelo recebedor) | O recebedor informa o valor, e o governo pode ajustá-lo até a baixa da transação. |
| **Simplificado** | Fora da Fase 1 | Usa um percentual fixo. |

O Recolhimento pelo Adquirente (RAD) também fica fora da Fase 1.

Todos os documentos técnicos estão em https://www.cgibs.gov.br/split-payment (manuais de Integração v1.1.1, Operações, Tempos, Segurança, Redes e Habilitação, e OpenAPI).

### 1.4 Cronograma atual: houve adiamento?
- **[OK] Testes:** Comunicado RFB de **30/09/2026**. Testes de integração entre os PSPs e a Plataforma Pública começaram em **15/10/2026**, em ambiente controlado.
  - Nenhuma transação é processada de forma definitiva, e não há multa nos testes.
  - Os demais PSPs se inscrevem a partir de **16/11/2026**.
  - Link: https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/setembro/comunicado-5
- **[OK] Fase 1, "B2B Opcional"** (Manual de Operações v1.0.1):
  - o split "aplica-se exclusivamente a operações entre Pessoas Jurídicas";
  - é **facultativo para quem origina** a transação: "Se os campos não forem preenchidos, a transação prossegue sem split";
  - a adaptação é **obrigatória para todo banco e PSP** dos arranjos.
  - O manual não traz a data de produção, que fica num "Plano de Implantação" à parte. **[CONFIRMAR]** se esse plano já foi publicado.
- **[PONTE] Obrigatoriedade adiada de 2027 para 2028:**
  - anunciada pela Receita em **30/08/2026**;
  - porta-voz: Juliano Neves, subsecretário de Gestão Corporativa;
  - frase: "Ninguém vai ser obrigado enquanto não estiver disponível para todos os meios de pagamento";
  - motivo: mais de 200 instituições precisam adaptar seus sistemas.
  - ISTOÉ Dinheiro, 30/08/2026: https://istoedinheiro.com.br/receita-federal-adia-split-payment-para-2028
  - Contábeis, 01/09/2026: https://www.contabeis.com.br/noticias/79144/split-payment-obrigatoriedade-deve-comecar-em-2028/
  - **Não localizei ato oficial (portaria ou ato conjunto RFB/CGIBS no DOU) com a data de 2028.** Até agora é **previsão anunciada, não norma**. Na tela: "Receita anunciou, ainda sem ato publicado". **[CONFIRMAR antes de gravar]**
- **Resumo honesto:**
  - 2026: só testes;
  - 2027: split opcional, só entre empresas, por Pix, boleto e TED. Cartão fica de fora da Fase 1;
  - 2028: obrigatório no B2B (previsão);
  - até 2033: chega ao consumo (B2C), conforme a imprensa. Para a data do B2C, **[CONFIRMAR]** em ato oficial.

---

## 2. Quem é afetado

| Público | O que diz o documento | Status |
|---|---|---|
| **Pessoa física pagando outra PF (Pix entre pessoas)** | Fora do split. O Manual diz: "A experiência dos usuários Pessoa Física não é alterada… não há novos campos a preencher, novas telas de confirmação ou alterações em comprovantes". No Pix Estático, TED e TEF, "o Pagador PF não consegue realizar transações com split". | [OK] Fase 1 |
| **PF pagando empresa (boleto, Pix Dinâmico/QR de cobrança)** | Pode pagar uma cobrança já criada com split, "sem visibilidade dos campos de CBS, IBS". O imposto já estava no preço, e a PF não paga nada a mais. | [OK] Fase 1 |
| **PF no futuro (B2C)** | O art. 35, §1º manda o split entrar nos principais meios do varejo para compras de não contribuintes. Então **vai chegar na compra da PF**, mas como separação do imposto que já está embutido no preço, não como imposto novo. | [OK] lei; data [CONFIRMAR] |
| **Empresas do regime regular (Lucro Real/Presumido)** | São o alvo principal. Recebem o líquido; o imposto vai direto ao Fisco. | [OK] |
| **Simples Nacional** | A LC 214 não exclui o Simples nos arts. 31 a 35. A Fase 1 vale para "PJs regularmente inscritas no CNPJ", sem distinção de regime. A Receita, citada pela imprensa, diz que o Simples escolhe entre o DAS unificado e o regime híbrido. Como ficará o Simples nas fases obrigatórias depende de ato conjunto. | [CONFIRMAR]: as fontes divergem |
| **MEI** | Paga valor fixo de CBS/IBS no DAS e não gera crédito; segundo a Receita (via imprensa), "fica fora da estrutura de repasse de créditos". Exposição inicial indireta. | [PONTE] |
| **Pix** | Entra na Fase 1, mas só entre empresas. Segundo a Receita (ISTOÉ, 30/08/2026), as transferências eletrônicas vêm primeiro e o Pix Estático depois. | [OK] manual + [PONTE] ordem |
| **Cartão (crédito, débito, pré-pago) e maquininha** | **Fora da Fase 1.** Manual: "fora do escopo desta fase, tais como cartões de crédito, débito e pré-pago; benefícios e vouchers… criptomoedas e meios não eletrônicos". | [OK] |
| **Marketplace e plataforma digital** | O Senado manteve as plataformas no split (PLP 68, 12/12/2024). A plataforma que inicia o pagamento informa os dados e, se o recebedor não informar, inclui a vinculação no documento fiscal (art. 32, §2º-A, LC 227/2026). | [OK] |
| **Dinheiro vivo** | Fora ("meios não eletrônicos"). | [OK] Fase 1 |
| **Bancos** | Adaptação obrigatória. O governo estuda pagar **R$ 0,39 por transação** aos bancos (ver item 3). | [PONTE] |

---

## 3. Críticos x defensores, e os números

### 3.1 Defensores (governo)
- **Argumento:** combater a sonegação e as empresas de fachada (o "noteiro" que emite nota, recebe e some). Segundo o governo, a arrecadação mais garantida permite uma alíquota menor.
  - Ministério da Fazenda, "Split Payment e Reforma Tributária: um salto para a modernidade fiscal" (maio/2025): https://www.gov.br/fazenda/pt-br/assuntos/noticias/2025/Maio/split-payment-e-reforma-tributaria-um-salto-para-a-modernidade-fiscal
  - Bernard Appy, mar/2025, "mínima interferência nas práticas comerciais": https://www.gov.br/fazenda/pt-br/assuntos/noticias/2025/marco/split-payment-esta-sendo-desenvolvido-para-ter-minima-interferencia-nas-praticas-comerciais-ressalta-appy
- **Ministro Dario Durigan (Fazenda):** opor-se ao split "favorece quem frauda". **[CONFIRMAR]** a fala literal, a data e o vídeo; ela só apareceu em agregadores de busca.
- **Quanto se espera arrecadar:** **não há cálculo oficial publicado** do ganho específico do split. Circulam números que medem outra coisa:
  - "até R$ 150 bi/ano" (conjunto de controles da reforma);
  - R$ 400 a 500 bi (tributarista da ROIT);
  - IBPT, R$ 417 bi;
  - Sonegômetro do Sinprofaz, R$ 626 bi.
  - Os três últimos medem a **sonegação total**, não o efeito do split. **[CONFIRMAR / não usar como "ganho do split"]**

### 3.2 Críticos
1. **Capital de giro.** Hoje a empresa vende, recebe e paga o imposto em média uns 40 dias depois. Com o split, o imposto sai no ato.
   - Estimativas: até **R$ 117 bi** de capital de giro retirado do caixa, **R$ 32 a 38 bi/ano** de custo financeiro e cerca de **981 mil** empresas do Lucro Real/Presumido afetadas.
   - **Fonte fraca:** a Gazeta do Povo, 10/11/2026, não nomeia o estudo nem a consultoria (https://www.gazetadopovo.com.br/economia/reforma-tributaria-ameaca-o-capital-de-giro-de-quase-um-milhao-de-empresas/). **[CONFIRMAR autoria antes de usar]**
2. **Custo pago aos bancos ("quem ganha?").**
   - Proposta: **R$ 0,39 por transação** paga às instituições financeiras, sobre 1,3 a 1,5 bilhão de transações por ano.
   - Saiu de um grupo de trabalho da Fazenda com Febraban/Fin e CGU (reportagem do JOTA citada).
   - A conta dá **cerca de R$ 507 a 585 milhões/ano** (cálculo nosso). Seria paga como **crédito tributário em 10 anos, corrigido pela Selic**, ou seja, pelo Tesouro.
   - A **CGU questionou** a falta de memória de cálculo. A consultoria EY, a serviço dos bancos, estimou o custo entre R$ 0,46 e R$ 0,61.
   - ISTOÉ Dinheiro, 10/08/2026: https://istoedinheiro.com.br/custo-split-payment-reforma-tributaria-bancos-cgu
   - É uma **proposta, não tarifa vigente.** Não há cobrança de R$ 0,39 no Pix do consumidor. **[PONTE]**
3. **Privacidade e controle.**
   - Cada pagamento entre empresas passa a consultar, em tempo real, uma Plataforma Pública operada pela RFB e pelo CGIBS. A comunicação com os bancos "é realizada exclusivamente pela Núclea, não havendo opção de prestador" (Manual de Operações v1.0.1). O Estado passa a ver o pagamento **vinculado à nota fiscal**, no ato.
   - A lei não cria imposto sobre o Pix, mas cria a **infraestrutura** de controle transação a transação.
   - Isso é leitura crítica, não ilegalidade: dizer "na minha avaliação".
4. **Pequena empresa e Simples.** Tem menos caixa e crédito mais caro, e o percentual do modo simplificado "não guarda relação com o débito efetivo" (art. 33, §2º). Paga a mais e espera a devolução em 3 dias úteis.
5. **Precedente da CPMF.** Tributaristas temem a informalidade e a fuga para o dinheiro vivo (Gazeta, sem nome). **[opinião, não fato]**

### 3.3 Alíquota de referência (estimativas oficiais mais recentes) [OK / PONTE]
- **CBS 2027: 11,3%** (11,3468%), calculada pelo **TCU** em **28/10/2026**:
  - processo TC 006.529/2026-7, relator Vital do Rêgo; o número do acórdão (2933/2026) é **[CONFIRMAR]**;
  - redutor de 44,2% para compras públicas;
  - o Senado fixa por resolução até **15/12/2026** (PRS 50/2026, relator Eduardo Braga). Se não votar, vale o número do TCU;
  - por regra, a cobrança em 2027 fica em cerca de 11,2% (0,1 ponto a menos em 2027 e 2028);
  - Conjur, 28/10/2026: https://conjur.com.br/2026-out-28/tcu-propoe-aliquota-de-referencia-da-cbs-em-113-para-2027/
- **IBS: 18,7%** de referência, pela **Resolução CGIBS nº 14, de 29/07/2026**.
  - A mesma resolução projetava 27,91% no total (18,7 de IBS + 9,21 de CBS).
  - Link: https://www.cgibs.gov.br/upload/arquivos/202607/31144942-resoluc-ao-cgibs-n-14-de-29-de-julho-de-2026-proposta-percentual-ibs-cgibs-2027.pdf
  - Até 2028 o IBS é cobrado a apenas **0,1%** (teste).
- **Conta que vira gancho:** 11,3 + 18,7 = **30%**, contra a **trava de 26,5%** da LC 214.
  - Se a estimativa passar de 26,5%, o Executivo é obrigado a mandar projeto para reduzi-la.
  - A Fazenda já projetava 27,97% (ago/2024) e 28,1% (dez/2024).
  - **Cuidado:**
    - 30% é soma de estimativas de órgãos diferentes, com metodologias diferentes;
    - em 2027 o consumidor não paga 30%;
    - dizer "a referência calculada pelos próprios órgãos já passa de 26,5%".
  - "Maior IVA do mundo": a Hungria tem 27% de alíquota padrão. **[CONFIRMAR]** na tabela da OCDE ou da Comissão Europeia antes de usar.

### 3.4 Quem aprovou [OK]
- **Senado, 12/12/2024:** substitutivo do PLP 68/2024 aprovado por **49 a 19**. **Flávio Bolsonaro votou "não"**.
  - Lista nominal: https://legis.senado.leg.br/sdleg-getter/documento/download/07f4883d-9069-4308-ad2e-775dc5cc3aa3?ts=1793392489080&disposition=inline
- **Câmara:** votação final em dez/2024. Placar e data **[CONFIRMAR]** em dadosabertos.camara.leg.br.
- **Sanção:** Lula, LC 214 de 16/01/2025.
- **"De quem foi a ideia":** o split já existe na Itália e na Polônia. No Brasil, o modelo foi defendido pela Secretaria Extraordinária da Reforma Tributária, chefiada por **Bernard Appy**.
- **Flávio Bolsonaro e a eleição:**
  - em 06/08/2026, no podcast *Market Makers*, disse: "Teria que ter uma transição melhor, do meu ponto de vista" e "Você está contando com esse dinheiro para poder pagar o fornecedor daqui a 30 dias" (reformatributaria.com, 07/08/2026: https://www.reformatributaria.com/reforma-tributaria-nas-eleicoes/flavio-bolsonaro-defende-transicao-melhor-para-o-split-payment/);
  - em out/2026, Daniella Marques, coordenadora econômica da campanha, disse que "o split payment não terá continuidade" (SBT News: https://sbtnews.sbt.com.br/colunas/nova-economia/lula-flavio-bolsonaro-split-payment-reforma-tributaria; Gazeta, 10/10/2026). O fim do split não aparece explicitamente no plano registrado no TSE. Emenda de Flávio para suprimir o split: **[CONFIRMAR]**, número não localizado;
  - **resultado:** Lula foi reeleito em **25/10/2026** com 51,79% contra 48,21% (Agência Senado: https://www12.senado.leg.br/noticias/materias/2026/10/25/lula-2018vira2019-e-e-reeleito-para-quarto-mandato-de-presidente). A promessa de acabar com o split saiu da mesa, e **o mecanismo segue**. Posse em 05/01/2027.

---

## 4. Outros países

| País | Modelo | Fonte | Lição |
|---|---|---|---|
| **Itália** | *Scissione dei pagamenti* (art. 17-ter do DPR 633/1972), desde 2015, só nas **compras da administração pública**: o órgão público paga o IVA direto ao Fisco. É derrogação da Diretiva 2006/112/CE (art. 395). Prorrogada até **30/06/2029** pela Decisão de Execução (UE) 2026/1728, de 10/07/2026 (GUUE de 15/07/2026). Empresas do FTSE MIB saíram em 01/07/2025 (D.L. 84/2025). | IPSOA, 15/07/2026: https://www.ipsoa.it/documents/quotidiano/2026/07/15/split-payment-applicabile-30-giugno-2029 · ANCE: https://ance.it/2026/07/split-payment-via-libera-definitivo-della-ue-alla-proroga-fino-al-2029/ | Restrito ao governo comprador, não a toda a economia. Precisa de autorização especial da UE, porque **foge da regra do IVA europeu**. |
| **Polônia** | *Mechanizm podzielonej płatności*: voluntário desde 01/07/2018 e obrigatório desde 01/03/2019 em setores de risco (lista do anexo 15, faturas acima de 15 mil PLN). Autorizado pela Decisão (UE) 2019/310 e prorrogado pela Decisão (UE) 2025/373 até **28/02/2028**. **Diferença-chave:** o IVA vai para uma **conta-IVA em nome da própria empresa**, de uso restrito, e não direto ao governo. | EUR-Lex: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:52025PC0007 | Até no modelo mais duro da Europa o dinheiro **continua da empresa**. No Brasil ele sai para o Fisco. A data de 15 mil PLN e o anexo 15: **[CONFIRMAR]** no texto da lei polonesa. |
| **Romênia** | *Split TVA* (OUG 23/2017), em vigor de 01/10/2017, obrigatório desde 2018 para devedores e insolventes. A Comissão Europeia enviou carta formal em 2018 dizendo que violava o direito da UE. **Revogado em 01/02/2020** (OUG 78/2019, Monitorul Oficial de 23/12/2019). | PwC Romênia: https://www.pwc.ro/en/tax-legal/alerts/the-vatsplit-payment-mechanism--repealed-as-of-1-february-2020.html · CMS: https://cms.law/en/rou/legal-updates/Romania-repeals-controversial-VAT-split-payment-mechanism | **Exemplo de que não deu certo e foi abolido.** Falta o documento primário (Monitorul Oficial): **[CONFIRMAR]**. |
| **EUA** | Não têm IVA, só sales tax estadual. Não há split nacional. | (conhecimento geral) | Responde à busca "split payment eua". |
| **Brasil** | O primeiro a aplicar o split **em toda a economia**, B2B e depois B2C, com consulta em tempo real ao Fisco. | LC 214 e manuais do CGIBS | Diferente de tudo acima, pela escala. A frase "o maior do mundo" só entra com a ressalva de que é avaliação. |

Opcional: o *VAT gap* da Polônia caiu depois de 2017, segundo o relatório *VAT Gap* da Comissão Europeia. É um argumento dos defensores. **[CONFIRMAR]** os números no relatório.

---

## 5. Pix: a norma de jan/2025 e o boato de "taxar o Pix"

### 5.1 Linha do tempo [OK]
1. **IN RFB 2.219, de 17/09/2024:** ampliou a e-Financeira para fintechs e Pix.
   - Limites de informe: movimentação acima de **R$ 5 mil/mês (PF)** e **R$ 15 mil (PJ)**. **[CONFIRMAR]** os valores no texto da IN.
   - Entrou em vigor em 01/01/2025.
2. **Jan/2025:** viralizou o boato de que o "Pix vai ser taxado", com golpes de "taxa do Pix".
3. **IN RFB 2.247, de 15/01/2025** (DOU extra de 16/01): **revogou a 2.219**.
   - Texto: https://sintse.tse.jus.br/documentos/2025/Jan/16/diario-oficial-da-uniao-secao-1-edicao-extra/secretaria-especial-da-receita-federal-do-brasil-instrucao-normativa-no-2-247-de-15-de-janeiro-de
4. **MP 1.288, de 16/01/2025:**
   - proibia cobrar valor a mais no Pix em relação ao dinheiro e reforçava o sigilo;
   - **perdeu a eficácia em 02/06/2025 sem ser votada** (Ato Declaratório nº 48/2025 da Mesa do Congresso: https://www.planalto.gov.br/ccivil_03/_Ato2023-2026/2025/Congresso/adc-48-mpv1.288.htm).
5. **Jan/2026:** a Receita voltou a negar a taxação do Pix.
   - Fala atribuída ao secretário Robinson Barreirinhas: a Constituição veda tributo sobre movimentação financeira. **[CONFIRMAR]** a fala literal.
   - Diario de Pernambuco, jan/2026: https://www.diariodepernambuco.com.br/economia/2026/01/11705186-receita-federal-volta-a-negar-taxacao-do-pix-e-alerta-para-golpes.html

### 5.2 Como desmontar o boato (ligado ao split)
- O split **não é imposto novo** nem "imposto sobre o Pix". O Pix é só o trilho: o IBS e a CBS já estão no preço, e o split muda **quem recolhe e quando**.
- **Pix entre pessoas físicas:** fora (Manual de Operações v1.0.1).
- **Mas não é verdade que "não muda nada":**
  - a Receita passa a ter o pagamento **ligado à nota**, em tempo real;
  - o B2C virá por lei (art. 35, §1º);
  - a norma de 2025 caiu, mas a vontade de enxergar cada transação não caiu: voltou por outro caminho, por lei complementar aprovada no Congresso.
- **Tese do vídeo:** "não vão taxar o seu Pix; vão usar o Pix para ver e reter tudo o que passa pelo caixa das empresas".

---

## 6. Paraguai: o IVA e se existe algo parecido

### 6.1 IVA paraguaio [OK]
- **Lei 6.380/2019** (Modernización y Simplificación del Sistema Tributario Nacional), regulamentada pelo **Decreto 3.107, de 19/12/2019**. Órgão: **DNIT**, que sucedeu a SET.
- **Alíquotas:**
  - **10% geral**;
  - **5%** para a canasta familiar (arroz, macarrão, óleo, erva-mate, leite, ovos, farinha, sal iodado), aluguel residencial, remédios e outros.
  - Cartilha IVA DNIT, 24/06/2024: https://www.dnit.gov.py/documents/20123/224724/Cartilla%2BIVA%2B24%2B06%2B2024.pdf/2fc2b350-4bb8-f5cd-06ff-83f6b6d15750?t=1719584356809.pdf
  - Portal: https://www.dnit.gov.py/web/portal-institucional/iva
- **Comparação para a tela:** 10% no Paraguai contra cerca de 28 a 30% de referência no Brasil (IBS + CBS).

### 6.2 Existe split no Paraguai? Algo parecido, mas muito menor [OK, vigência a confirmar]
- **Decreto 3.107/2019, art. 39:** as administradoras e processadoras de cartão de crédito "deberán retener el IVA, aplicando el cero coma noventa mil novecientos nueve por ciento (0,90909%) sobre el monto total de las operaciones".
  - Texto: https://impuestospy.com/impuestos/decreto-n-3-107-2019 (transcrição secundária; o original está na DNIT).
- **A conta:** 0,90909% do valor equivale a **10% do IVA embutido** (IVA de 10/110 × 10%).
  - Ou seja, a processadora de cartão retém **um décimo** do imposto como **antecipação**, que o comércio abate na própria declaração mensal.
  - Os outros 90% ficam no caixa da empresa até o vencimento.
- Também existem a **percepção de IVA** em serviços digitais do exterior (Netflix e similares), feita pelas processadoras (Lei 6.380, arts. 84 e 90; **RG DNIT 76/2020**), e a retenção do IRE (RG 33/2020).
- **Contraste:**
  - Paraguai: retém cerca de 0,9% do valor, só no cartão, como antecipação;
  - Brasil: o modelo padrão separa **100% do imposto** em Pix, boleto e TED e o manda direto ao Fisco.
- **[CONFIRMAR]:**
  - se o art. 39 segue com a mesma alíquota (checar decretos posteriores na DNIT);
  - a afirmação de que o Paraguai **não tem split amplo**, que se baseia na ausência de norma localizada; checar no portal de resoluções da DNIT.
- Debate sobre unificar o IVA em 10%: a matéria que apareceu (Última Hora) é de **2019**, não atual. Não usar como notícia.

---

## 7. Três ângulos de roteiro (do bolso para o sistema)

### Ângulo 1: "O imposto vai sair antes do dinheiro chegar no seu caixa"
- **Público:** pequeno empresário e família que vive de comércio.
- **Ganchos:**
  - "A partir de 2027, o banco vai pegar o imposto da sua venda antes de você ver o dinheiro. E a lei já foi aprovada."
  - "Você vende hoje e paga o imposto daqui a 40 dias. Com o split payment, ele sai no mesmo segundo."
- **Roteiro:**
  1. Art. 31 da LC 214 na tela.
  2. Capital de giro: o dinheiro do fornecedor de 30 dias (citar a frase de Flávio só como registro, não como bandeira).
  3. Quem ganha: os bancos, com proposta de R$ 0,39 por transação e cerca de R$ 0,5 bi/ano em crédito tributário corrigido pela Selic; a CGU questionou.
  4. Paraguai: lá o cartão retém 0,9% como antecipação; aqui a separação é de 100%.
  5. Leitura: o Estado como sócio que recebe primeiro. Na linha da *Rerum Novarum* sobre propriedade, e com o critério implícito.
- **Confirmado:** art. 31; Fase 1 opcional e B2B; cartão fora da Fase 1; Decreto 3.107, art. 39.
- **[CONFIRMAR]:** R$ 117 bi (autoria do estudo); R$ 0,39 (proposta, não vigente); data de 2028 sem ato oficial.

### Ângulo 2: "Não vão taxar o seu Pix. Vão fazer algo maior"
- **Público:** pessoa física, que é a maior busca ("afeta pessoa física", "imposto pix é verdade", "maior que o pix").
- **Ganchos:**
  - "Lembra quando a Receita recuou da fiscalização do Pix? Ela não desistiu. Mudou de caminho."
  - "Seu Pix para a sua mãe não muda nada. Mas o resto muda."
- **Roteiro:**
  1. Jan/2025: IN 2.219, depois a revogação pela IN 2.247, e a MP 1.288, que caducou em 02/06/2025.
  2. O boato da "taxa do Pix" era falso, e dizer isso com clareza.
  3. Agora é lei complementar, não instrução normativa: cada pagamento entre empresas fica ligado à nota, em tempo real. Mostrar o trecho do manual "comunicação… exclusivamente pela Núclea".
  4. A PF fica fora na Fase 1, mas o art. 35, §1º manda chegar ao varejo.
  5. Leitura: o desmentido honesto ("não é imposto novo") junto com a crítica ao controle ("na minha avaliação").
- **Confirmado:** IN 2.219 e 2.247; MP 1.288 caducada; manual da PF; art. 35.
- **[CONFIRMAR]:** limites de R$ 5 mil e R$ 15 mil da IN 2.219; fala literal de Barreirinhas; data de entrada do B2C.

### Ângulo 3: "IVA de 30%? E quem votou nisso"
- **Público:** quem busca "quem aprovou", "flavio bolsonaro", "deu certo em outros países".
- **Ganchos:**
  - "Prometeram 26,5%. O TCU e o Comitê Gestor já calculam 30%."
  - "Isso foi testado na Romênia. Durou dois anos e foi revogado."
- **Roteiro:**
  1. CBS de 11,3% (TCU, 28/10/2026) mais IBS de 18,7% (Res. CGIBS 14/2026) contra a trava de 26,5%.
  2. Quem votou: Senado 49 a 19 em 12/12/2024, com a lista nominal na tela; a Câmara a confirmar.
  3. A campanha prometeu acabar com o split, Lula venceu em 25/10/2026 e o mecanismo fica.
  4. Lá fora:
     - Itália: só governo, com autorização especial da UE;
     - Polônia: o dinheiro fica numa conta da própria empresa;
     - Romênia: revogado em 2020;
     - Brasil: o mais amplo.
  5. Paraguai: IVA de 10%.
  6. Leitura: subsidiariedade (*Quadragesimo Anno*). Cobrar mais e controlar mais não é o mesmo que ordem justa.
- **Confirmado:** TCU 11,3%; Res. CGIBS 14/2026; trava de 26,5%; 49 a 19 com o "não" de Flávio; Itália até 2029; Polônia até 2028; Romênia revogada em 2020 (via PwC e CMS).
- **[CONFIRMAR]:**
  - que "30%" é soma de estimativas, não alíquota cobrada em 2027; dizer isso na tela;
  - número do acórdão do TCU;
  - placar da Câmara;
  - se o Senado votou o PRS 50/2026 até 15/12;
  - comparação "maior IVA do mundo" com a Hungria (27%).

---

## 8. Pendências antes de gravar (checklist)
1. Ato oficial (DOU) com a data de **obrigatoriedade em 2028**. Hoje é só anúncio da Receita de 30/08/2026.
2. "Plano de Implantação" do CGIBS com a data de produção da Fase 1 em 2027.
3. Tratamento do **Simples Nacional** nas fases obrigatórias (ato conjunto RFB/CGIBS).
4. Autoria do estudo de R$ 117 bi; status da proposta de R$ 0,39 e documento da CGU.
5. Acórdão TCU 2933/2026 (número) e votação do PRS 50/2026 no Senado (prazo de 15/12/2026).
6. Placar da Câmara do PLP 68/2024 (dez/2024).
7. Valores-limite da IN RFB 2.219/2024; fala literal de Barreirinhas (jan/2026) e de Durigan.
8. Paraguai: vigência do art. 39 do Decreto 3.107/2019 na DNIT.
9. Romênia: OUG 78/2019 no Monitorul Oficial. Polônia: limite de 15 mil PLN e anexo 15.

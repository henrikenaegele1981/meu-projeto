# Página do Fred Real Nutricionista

Site estático (HTML + CSS + JS, sem build), publicado pelo GitHub Pages.

| Endereço | O que é |
|---|---|
| `/` (`index.html`) | Página de vendas no formato da referência lp.pysemfronteiras.com: abertura com objetivos, quem cuida, "o que ninguém te conta", planos com abas por objetivo, etapas, resultados, perguntas e chamada final |
| `/diagnostico/` | Diagnóstico de 9 perguntas que indica o plano (Semestral, Trimestral ou Avulsa). Aceita `?objetivo=emagrecer\|massa\|definicao\|saude` para pular a 1ª pergunta |

Cores do Fred (preto, vermelho e branco). Fotos do Fred em `assets/`, tiradas dos posts públicos do Instagram.

## O que editar

WhatsApp, CRN, preços, planos e resultados ficam em **`config.js`**, usado pelas duas páginas.
Os textos das abas de objetivo ficam em `script.js` (`OBJETIVOS`); perguntas e textos do diagnóstico em `diagnostico/script.js`.

### Detalhes

- **`CONFIG.whatsapp`**: WhatsApp do Fred (já preenchido).
- **`CONFIG.crn`**: número do CRN (ainda `00000`).
- **`CONFIG.mostrarPrecos`**: `false` por padrão (o briefing pede valores só na conversa). Trocando para `true`,
  os preços aparecem nos cartões dos planos e no resultado do diagnóstico.
- **`CONFIG.webhook`** (opcional): endereço que recebe nome, WhatsApp, respostas e plano indicado.
- **`PLANOS`**: nome, duração, preço e itens de cada plano.
- **`PERGUNTAS`, `PERFIS`, `PONTOS`**: perguntas e textos do resultado do diagnóstico.
- A regra que escolhe o plano fica na função `indicarPlano`.

## Imagens (opcionais) em `assets/`

- `fred-sobre.jpg`: foto vertical (4:5) do Fred para a seção "Quem é o Fred".
- `og-image.jpg`: imagem 1200×630 que aparece quando o link é compartilhado.

## Decisões seguindo o briefing

- Preços escondidos por padrão; valores e condições na conversa com o Fred.
- Todos os botões levam ao WhatsApp **do Fred** (ele conduz a venda; a secretária agenda depois).
- Planos integrados com treino ficam de fora até a regularização no CREF.
- Sem depoimentos, números ou resultados inventados; aviso de que os resultados variam no rodapé.

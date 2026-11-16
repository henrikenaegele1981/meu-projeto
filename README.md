# Página do Fred Real Nutricionista

Site estático (HTML + CSS + JS, sem build), publicado pelo GitHub Pages.

| Endereço | O que é |
|---|---|
| `/` (`index.html`) | Página de vendas completa: história, método, acompanhamento, **diagnóstico que indica o plano**, planos, presencial x online, FAQ |
| `/diagnostico/` | Versão anterior: só o diagnóstico, em tela cheia (fundo escuro) |

Formatação inspirada na página de lançamento do Mapa da Fé Católica, com as cores do Fred (preto, vermelho e branco).

## O que editar (tudo no `script.js`, bloco `CONFIG` e logo abaixo)

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

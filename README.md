# Página de vendas — Fred Real Nutricionista

Página estática (HTML + CSS + JS, sem build). Para ver, basta abrir `index.html` no navegador.

## O que preencher antes de publicar

1. **`script.js` → bloco `CONFIG`**: WhatsApp do Fred, @ do Instagram e número do CRN.
   As mensagens pré-escritas do WhatsApp mudam conforme o botão (geral, planos, presencial, online).
2. **Imagens em `assets/`** (a página funciona sem elas, mas fica muito melhor com):
   - `logo-leao.png` — logo da cabeça de leão (fundo transparente)
   - `fred-hero.jpg` — foto horizontal do Fred, iluminação escura/cinematográfica (aparece à direita no topo)
   - `fred-sobre.jpg` — foto vertical (4:5) para a seção "Quem sou eu"
   - `og-image.jpg` — imagem 1200×630 que aparece quando o link é compartilhado
3. **Depoimentos**: a seção está desativada (comentário no `index.html`). Ativar só com
   depoimentos reais, autorizados por escrito e conferidos com as normas do CFN/CRN.

## Decisões seguindo o briefing

- Sem preços na página: valores só na conversa privada.
- Todos os botões levam ao WhatsApp **do Fred** (ele conduz a venda; a secretária só agenda depois).
- Sem menção ao serviço integrado de treino até a regularização no CREF.
- Sem promessas de resultado; aviso de que os resultados variam no rodapé.

## Publicar

Qualquer hospedagem estática serve (GitHub Pages, Netlify, Vercel). No GitHub Pages:
Settings → Pages → Deploy from a branch → escolher a branch e a pasta `/ (root)`.

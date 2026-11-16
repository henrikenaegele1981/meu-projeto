# Diagnóstico do Shape — Fred Real Nutricionista

Página de captação em formato de diagnóstico (quiz de 9 perguntas → dados → resultado → WhatsApp do Fred).
Estática (HTML + CSS + JS, sem build). Para ver, basta abrir `index.html` no navegador.

As perguntas e os textos do resultado ficam em `script.js` (`PERGUNTAS`, `PERFIS`, `PONTOS`) e podem ser editados sem mexer no resto.

## O que preencher antes de publicar

1. **`script.js` → bloco `CONFIG`**: WhatsApp do Fred e número do CRN.
2. **(Opcional) `CONFIG.webhook`**: endereço que recebe nome, WhatsApp e respostas de quem conclui o
   diagnóstico (Google Planilhas via Apps Script, Make, Zapier, n8n). Sem ele, o contato só chega
   quando a pessoa aperta "Mandar meu diagnóstico para o Fred" — o WhatsApp abre com as respostas já escritas.
3. **`assets/og-image.jpg`** — imagem 1200×630 que aparece quando o link é compartilhado.

## Decisões seguindo o briefing

- Sem preços na página: valores só na conversa privada.
- O resultado leva ao WhatsApp **do Fred** (ele conduz a venda; a secretária só agenda depois).
- Sem menção ao serviço integrado de treino até a regularização no CREF.
- Sem promessas de resultado; aviso de que os resultados variam no rodapé.

## Publicar

Qualquer hospedagem estática serve (GitHub Pages, Netlify, Vercel). No GitHub Pages:
Settings → Pages → Deploy from a branch → escolher a branch e a pasta `/ (root)`.

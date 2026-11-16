---
name: instagram-midia
description: Busca e baixa fotos de um perfil do Instagram (feed, carrosséis e, quando há navegador logado, destaques e stories) para usar em páginas e peças. Use sempre que o Henrike pedir fotos "do Instagram do cliente", "dos destaques" ou "dos pacientes" para um projeto.
---

# Fotos do Instagram para páginas e peças

Objetivo: o Henrike não deve precisar baixar nada na mão. Escolha o caminho conforme onde a sessão roda.

## 1. Descobrir onde estou

- **Sessão no computador do Henrike, com Claude in Chrome** (ferramentas `mcp__claude-in-chrome__*` ou `mcp__Claude_Browser__*`):
  use o navegador dele, que já está logado no Instagram. Vá para a seção 2.
- **Sessão na nuvem (Claude Code na web/app)**: não há navegador logado. Use a seção 3 (posts públicos)
  e, para destaques/stories/posts antigos, diga ao Henrike, numa frase, para abrir a mesma tarefa no
  Claude Desktop com o Chrome conectado. Não tente outro caminho de login.

## 2. Com navegador logado (caminho completo)

1. Carregue a skill do navegador correspondente (chrome-browser ou built-in-browser) antes do primeiro passo.
2. Abra `https://www.instagram.com/<perfil>/` numa aba nova.
3. **Destaques**: clique em cada capa de destaque; em cada story, tire screenshot ou pegue a URL da mídia
   (`img`/`video` com `src` em `cdninstagram.com`) e salve. Avance com a seta da direita.
4. **Feed completo**: role até o fim da grade; abra cada post e, em carrosséis, avance pelas setas.
5. Salve tudo numa pasta da tarefa (ex.: `scratchpad/ig/<perfil>/`) com nomes `destaque-<nome>-<n>.jpg`
   e `post-<código>-<n>.jpg`. Monte uma grade de miniaturas (PIL) para escolher rápido.

## 3. Sem login (sessão na nuvem): posts públicos

O Instagram sem login mostra só ~12 posts (3 fixados + 9 recentes) e nenhum destaque.
Funciona pela página pública de incorporação, aberta no Chromium do Playwright:

```bash
node .claude/skills/instagram-midia/scripts/listar-posts.js <perfil> <pasta>   # gera <pasta>/codes.json
node .claude/skills/instagram-midia/scripts/baixar-posts.js <pasta>            # baixa em <pasta>/posts/
```

- Chamadas diretas à API (`/api/v1/users/web_profile_info`) e WebFetch do perfil são bloqueadas
  (checagem de segurança da sessão / erro 429). Use só o navegador (scripts acima).
- O embed de cada post também traz imagens de posts relacionados: confira a grade e descarte repetidas.
- Rodando demorado (12 posts ≈ 2 min), deixe em segundo plano.

## 4. Nunca

- **Nunca peça senha do Instagram no chat**, nem cookies de sessão. Se o Henrike oferecer, recuse
  numa frase (fica gravado no histórico e o login de servidor dispara verificação/bloqueio da conta)
  e indique o caminho da seção 2.
- Não instale VNC/tela remota para o usuário logar: é bloqueado e expõe a conta.

## 5. Antes de publicar fotos de pessoas

- **Pacientes / antes e depois**: só com autorização por escrito do paciente e as normas do CRN/CFN
  conferidas. Pergunte uma vez ao Henrike; se ele confirmar, siga.
- Fotos do próprio profissional do perfil: ok usar; avise se for antes e depois dele mesmo.
- Recorte legendas, setas "ARRASTA" e marcas do Instagram; salve otimizadas em `assets/`
  (JPEG qualidade ~82, lado maior ≤ 1200 px).

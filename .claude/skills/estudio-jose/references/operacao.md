# Meu Estúdio: operação e problemas já resolvidos

## Como o sistema funciona

- **Meu Estúdio** é um app Flask que roda no notebook Windows do José, em `http://localhost:5252`,
  com o código em `github.com/henrikenaegele1981/meu-projeto` (branch `meu-estudio`, repositório
  **público**). Ele se atualiza sozinho ao abrir e a cada 6 horas (`atualizar.py`).
- Ele publica pela API oficial da Meta com um **token de usuário do sistema** (login unificado,
  servidor `graph.facebook.com`) e o **ID da conta do Instagram `17841407189368891`**. O token fica
  só no PC (`%LOCALAPPDATA%\MeuEstudio\config.json`); nenhuma sessão na nuvem tem esse token.
- O app confere a fila a cada 15 s e publica na hora. **Só publica se o PC estiver ligado e o app
  aberto.** Se estava fechado na hora, publica quando abrir (até 2 h de atraso; depois disso o post
  da caixa entra como "erro" para não sair fora de hora).
- Fuso: horário de Brasília/Assunção (UTC−3). Use `TZ=America/Sao_Paulo date` para saber a hora.

## Duas formas de agendar

**A. Sessão rodando no PC do José (local):** envie o formulário da Agenda.

```bash
curl -s -o NUL -w "%{http_code}" -F "arquivo=@C:\caminho\imagem.jpg" -F "legenda=<C:\caminho\legenda.txt" -F "quando=2026-11-11T14:00" -F "redes=instagram" -F "collabs=" http://localhost:5252/agenda
```

A resposta é 302. Confirme em `GET /agenda` que o post aparece como `agendado` (fotos com a
etiqueta "foto"). Use `legenda=<arquivo.txt` (UTF-8) para não quebrar acentos e emojis.

**B. Sessão na nuvem (o caso mais comum aqui):** use a caixa de entrada, com o script da skill.

```bash
python scripts/agendar_caixa.py agendar --id assunto-2026-11-12 --midia imagem.webp --legenda legenda.txt --quando 2026-11-12T14:00
python scripts/agendar_caixa.py listar
python scripts/agendar_caixa.py cancelar --id assunto-2026-11-12   # antes de sair
python scripts/agendar_caixa.py remover --id assunto-2026-11-12    # depois de publicado
```

O script converte a foto para JPEG, confere a proporção, envia para a branch `caixa` e espera o link
público responder. O app no PC importa em até 1 minuto e marca "agendado pelo Claude".
Cuidados:
- O `id` nunca pode se repetir (o app guarda os já importados). Para mudar um post: `cancelar` o
  antigo e `agendar` com outro `id`.
- O repositório é público: imagem e legenda ficam visíveis no GitHub até a publicação. Depois de
  confirmada a publicação, rode `remover`.
- **Não agende o mesmo post nos dois caminhos** (caixa e Agenda manual): ele sairia duas vezes.
- Se o app no PC ainda não tiver a versão com caixa (`caixa.py`), peça ao José para fechar e abrir o
  `iniciar.bat` (atualiza na hora).
- Não há como ver daqui se o post saiu: peça um print da Agenda ou confira o perfil no Instagram.

## Formatos aceitos

- **Foto (post estático):** JPG, PNG ou WEBP; proporção de 4:5 (1080×1350, o melhor) até 1,91:1;
  quadrada (1080×1080) também. Story (9:16) é recusada no feed.
- **Reel:** MP4 ou MOV, vertical, de 3 s a 15 min.
- Legenda: até 2.200 caracteres; collabs: até 3.

## Problemas já resolvidos (não repita os erros)

- **App novo da Meta não tem "API com login do Instagram".** Desde out/2026, apps novos usam o
  "login unificado": o botão "Gerar token" do painel falha e o login direto dá "Invalid platform
  app". O token certo vem de business.facebook.com → Usuários do sistema (usuário "meuestudio",
  com o app e o Instagram atribuídos, validade "Nunca").
- **ID errado:** o ID da conta do Instagram começa com **1784**. O número 2078586516169107 é o ID
  do **app** e não serve (o app agora recusa esse erro).
- **"A Meta não aceitou esse token" igual ao anterior depois de atualizar:** é a versão antiga ainda
  aberta. Feche todos os Python no Gerenciador de Tarefas e abra o `iniciar.bat`.
- **Business Suite pede aprovação de acesso:** a pessoa entrou com a conta do Instagram; as
  configurações exigem entrar com o **Facebook**.
- **Controle Remoto:** a pasta do PC aparece para a sessão na nuvem, mas o Windows não a oferece
  (`not_available`). Por isso existe a caixa de entrada. Uma sessão do Claude Code **local** no PC
  consegue usar o caminho A.
- **Rede da sessão na nuvem:** Instagram, Facebook, YouTube, vatican.va e os sites das editoras são
  bloqueados; `raw.githubusercontent.com` e o GitHub funcionam.

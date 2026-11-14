# Meu Estúdio na nuvem: o que falta (para a próxima sessão do Claude)

Objetivo: agendar e publicar posts sem depender do PC ligado.

## Como funciona
- **Supabase** guarda a fila (`estudio_posts`), a configuração e o token (`estudio_config`) e as mídias
  (bucket público `midia`, até 50 MB por arquivo no plano grátis). Ver `supabase/schema.sql`.
- **Função `publicar`** (Edge Function, `supabase/functions/publicar/index.ts`) publica no Instagram.
  O **pg_cron** do próprio Supabase chama essa função a cada minuto (`supabase/cron.sql`), com o
  cabeçalho `x-segredo` guardado no Vault.
- **Vercel** só hospeda a tela (Flask, `app.py`), protegida por `SENHA_ESTUDIO`. O navegador envia
  o arquivo direto ao Supabase (`static/envio.js`), porque a Vercel recusa requisições acima de 4,5 MB.
- Sem `SUPABASE_URL`/`SUPABASE_SERVICE_KEY`, o app roda no modo PC de antes (arquivos locais).

## Passos que faltam
1. Supabase (conector): criar o projeto "meu-estudio" (região São Paulo), rodar `supabase/schema.sql`,
   publicar a função `publicar` com verify_jwt desligado, criar os segredos da função
   `ESTUDIO_SEGREDO` (aleatório) e `FUSO=America/Sao_Paulo`, rodar `supabase/cron.sql`
   trocando `__REF__` e `__SEGREDO__`.
2. Vercel: pedir o token (request_credential para api.vercel.com) e publicar com
   `npx vercel deploy --prod` nesta branch. Variáveis: `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`,
   `SENHA_ESTUDIO`, `FLASK_SECRET` e `FUSO`.
3. O usuário entra no site, vai em Configurações e cola o token do Instagram e o ID da conta.
   Conferir se a Meta aceitou (aparece o @) e testar com um post de teste.
4. Avisar o usuário para não agendar o mesmo post no PC e na nuvem (são filas separadas).

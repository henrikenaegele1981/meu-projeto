-- Chama a função "publicar" a cada minuto. Troque __REF__ e __SEGREDO__ antes de rodar.
select vault.create_secret('__SEGREDO__', 'estudio_segredo')
where not exists (select 1 from vault.secrets where name = 'estudio_segredo');

select cron.schedule(
  'meu-estudio-publicar',
  '* * * * *',
  $$
  select net.http_post(
    url := 'https://__REF__.supabase.co/functions/v1/publicar',
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'x-segredo', (select decrypted_secret from vault.decrypted_secrets where name = 'estudio_segredo')
    ),
    body := '{}'::jsonb,
    timeout_milliseconds := 55000
  );
  $$
);

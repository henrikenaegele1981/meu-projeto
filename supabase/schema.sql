-- Meu Estúdio na nuvem: tabelas, armazenamento de mídia e o relógio que chama a função "publicar".
-- Só o servidor (chave de serviço) acessa: RLS ligado e nenhuma política pública.

create table if not exists public.estudio_config (
  chave text primary key,
  valor jsonb not null default '{}'::jsonb
);

create table if not exists public.estudio_posts (
  id text primary key,
  status text not null default 'agendado',
  quando text,                       -- hora local do usuário, "AAAA-MM-DDTHH:MM"
  dados jsonb not null default '{}'::jsonb,
  atualizado_em timestamptz not null default now()
);
create index if not exists estudio_posts_status_quando on public.estudio_posts (status, quando);

alter table public.estudio_config enable row level security;
alter table public.estudio_posts enable row level security;

-- Mídias públicas (o Instagram precisa buscar o arquivo por um link). 50 MB = limite do plano grátis.
insert into storage.buckets (id, name, public, file_size_limit)
values ('midia', 'midia', true, 52428800)
on conflict (id) do update set public = true, file_size_limit = excluded.file_size_limit;

create extension if not exists pg_cron;
create extension if not exists pg_net;

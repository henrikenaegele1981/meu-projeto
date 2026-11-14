// Meu Estúdio: função na nuvem que publica os posts agendados no Instagram.
// O Supabase (pg_cron) chama esta função a cada minuto. Não depende do PC nem da Vercel.
//
// Passos de cada post: agendado -> postando (cria o container no Instagram) -> processando
// (o Instagram baixa e processa o arquivo) -> publicando -> publicado, ou erro com a mensagem.

const SUPABASE_URL = Deno.env.get("SUPABASE_URL")!;
const CHAVE = Deno.env.get("ESTUDIO_SERVICE_KEY") || Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;
const SEGREDO = Deno.env.get("ESTUDIO_SEGREDO") || "";
const FUSO = Deno.env.get("FUSO") || "America/Sao_Paulo";
const BUCKET = "midia";
const SERVIDORES: Record<string, string> = {
  instagram: "https://graph.instagram.com/v21.0",
  facebook: "https://graph.facebook.com/v21.0",
};
const RENOVAR_A_CADA_MS = 30 * 24 * 3600 * 1000;
const ESPERA_PROCESSAMENTO_MS = 20 * 60 * 1000;
const TRAVADO_MS = 10 * 60 * 1000;

type Post = Record<string, any> & { id: string; status: string };
type Linha = { id: string; status: string; quando: string | null; dados: Post };

// ---------- hora local ----------

function agoraLocal(): string {
  // "AAAA-MM-DDTHH:MM:SS" no fuso do usuário (o formulário grava a hora local, sem fuso)
  const p = Object.fromEntries(
    new Intl.DateTimeFormat("en-CA", {
      timeZone: FUSO, year: "numeric", month: "2-digit", day: "2-digit",
      hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23",
    }).formatToParts(new Date()).map((x) => [x.type, x.value]),
  );
  return `${p.year}-${p.month}-${p.day}T${p.hour}:${p.minute}:${p.second}`;
}

function idadeMs(textoLocal?: string | null): number {
  if (!textoLocal) return Infinity;
  const agora = Date.parse(agoraLocal() + "Z");
  return agora - Date.parse(textoLocal.slice(0, 19) + "Z");
}

// ---------- Supabase ----------

async function rest(caminho: string, init: RequestInit = {}): Promise<any> {
  const resp = await fetch(`${SUPABASE_URL}/rest/v1/${caminho}`, {
    ...init,
    headers: {
      apikey: CHAVE, Authorization: `Bearer ${CHAVE}`, "Content-Type": "application/json",
      Prefer: "return=representation", ...(init.headers || {}),
    },
  });
  const texto = await resp.text();
  if (!resp.ok) throw new Error(`Supabase HTTP ${resp.status}: ${texto.slice(0, 300)}`);
  return texto ? JSON.parse(texto) : null;
}

async function postsCom(filtro: string): Promise<Post[]> {
  const linhas: Linha[] = await rest(`estudio_posts?select=*&${filtro}&order=quando`);
  return linhas.map((l) => ({ ...l.dados, id: l.id, status: l.status }));
}

/** Grava o post, mas só se o status ainda for `de` (ninguém mexeu nele no meio do caminho). */
async function trocar(post: Post, de: string, campos: Record<string, any>): Promise<Post | null> {
  const novo = { ...post, ...campos };
  const linhas = await rest(
    `estudio_posts?id=eq.${encodeURIComponent(post.id)}&status=eq.${encodeURIComponent(de)}`,
    {
      method: "PATCH",
      body: JSON.stringify({ status: novo.status, quando: novo.quando, dados: novo,
                             atualizado_em: new Date().toISOString() }),
    },
  );
  return linhas?.length ? novo : null;
}

async function config(): Promise<Record<string, any>> {
  const linhas = await rest("estudio_config?chave=eq.config&select=valor");
  return linhas?.[0]?.valor || {};
}

async function salvarConfig(cfg: Record<string, any>) {
  await rest("estudio_config", {
    method: "POST",
    headers: { Prefer: "return=minimal,resolution=merge-duplicates" },
    body: JSON.stringify({ chave: "config", valor: cfg }),
  });
}

function urlPublica(nome: string) {
  return `${SUPABASE_URL}/storage/v1/object/public/${BUCKET}/${encodeURIComponent(nome)}`;
}

async function apagarMidia(nome?: string) {
  if (!nome) return;
  await fetch(`${SUPABASE_URL}/storage/v1/object/${BUCKET}`, {
    method: "DELETE",
    headers: { apikey: CHAVE, Authorization: `Bearer ${CHAVE}`, "Content-Type": "application/json" },
    body: JSON.stringify({ prefixes: [nome] }),
  }).catch(() => {});
}

// ---------- Instagram ----------

class ErroInstagram extends Error {}

async function graph(ig: any, caminho: string, params: Record<string, string>, metodo = "GET") {
  const base = SERVIDORES[ig.tipo || "instagram"] || SERVIDORES.instagram;
  const corpo = new URLSearchParams({ ...params, access_token: ig.token });
  const resp = metodo === "GET"
    ? await fetch(`${base}/${caminho}?${corpo}`)
    : await fetch(`${base}/${caminho}`, { method: "POST", body: corpo });
  let dados: any;
  try {
    dados = await resp.json();
  } catch {
    throw new ErroInstagram(`Resposta inesperada do Instagram (HTTP ${resp.status}).`);
  }
  if (!resp.ok || dados.error) {
    const e = dados.error || {};
    throw new ErroInstagram(e.error_user_msg || e.message || `HTTP ${resp.status}`);
  }
  return dados;
}

async function renovarToken(cfg: Record<string, any>) {
  const ig = cfg.instagram;
  if (!ig?.token || ig.tipo === "facebook") return; // token de usuário do sistema não vence
  if (idadeMs(ig.renovado_em) < RENOVAR_A_CADA_MS) return;
  try {
    const resp = await fetch(
      `https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=${encodeURIComponent(ig.token)}`,
    );
    const novo = await resp.json();
    if (!resp.ok || novo.error) throw new Error(novo.error?.message || `HTTP ${resp.status}`);
    ig.token = novo.access_token;
    ig.renovado_em = agoraLocal();
    const vence = new Date(Date.parse(agoraLocal() + "Z") + (novo.expires_in || 5184000) * 1000);
    ig.expira_em = vence.toISOString().slice(0, 19);
    delete ig.aviso;
  } catch (e) {
    ig.aviso = `Não consegui renovar o token: ${(e as Error).message}`;
  }
  await salvarConfig({ ...(await config()), instagram: ig });
}

function camposDoPost(post: Post): Record<string, string> {
  const url = urlPublica(post.arquivo);
  const campos: Record<string, string> = post.tipo === "foto"
    ? { image_url: url, caption: post.legenda || "" }
    : { media_type: "REELS", video_url: url, caption: post.legenda || "", share_to_feed: "true" };
  if (post.collabs?.length) campos.collaborators = JSON.stringify(post.collabs);
  return campos;
}

function dicaDeFormato(post: Post) {
  return post.tipo === "foto"
    ? " Confira se a foto fica entre 4:5 (vertical) e 1,91:1 (horizontal)."
    : " Confira se é MP4/MOV, vertical, de 3 s a 15 min.";
}

// ---------- etapas ----------

async function falhar(post: Post, de: string, msg: string) {
  await trocar(post, de, {
    status: "erro", erro: msg,
    resultados: { ...(post.resultados || {}), instagram: { ok: false, erro: msg } },
  });
}

async function iniciar(post: Post, ig: any, log: string[]) {
  const meu = await trocar(post, "agendado", { status: "postando", erro: null, postando_desde: agoraLocal() });
  if (!meu) return; // outra execução já pegou
  try {
    if (!ig?.token) throw new ErroInstagram("Instagram não conectado. Vá em Configurações e cole o token.");
    const { id } = await graph(ig, `${ig.user_id}/media`, camposDoPost(meu), "POST");
    await trocar(meu, "postando", { status: "processando", container: id, container_desde: agoraLocal() });
    log.push(`${post.id}: container ${id} criado`);
  } catch (e) {
    await falhar(meu, "postando", `Instagram: ${(e as Error).message}`);
    log.push(`${post.id}: erro ${(e as Error).message}`);
  }
}

async function acompanhar(post: Post, ig: any, log: string[]) {
  try {
    const estado = await graph(ig, post.container, { fields: "status_code,status" });
    const codigo = estado.status_code;
    if (codigo === "ERROR" || codigo === "EXPIRED") {
      const msg = `Instagram: o Instagram recusou o arquivo (${codigo}): ${estado.status || "sem detalhes"}.${dicaDeFormato(post)}`;
      await falhar(post, "processando", msg);
      log.push(`${post.id}: ${msg}`);
      return;
    }
    if (codigo && codigo !== "FINISHED") {
      if (idadeMs(post.container_desde) > ESPERA_PROCESSAMENTO_MS) {
        await falhar(post, "processando", "Instagram: o Instagram demorou mais de 20 minutos para processar o arquivo.");
      }
      return; // ainda processando: confere no próximo minuto
    }
    const meu = await trocar(post, "processando", { status: "publicando" });
    if (!meu) return;
    try {
      const { id } = await graph(ig, `${ig.user_id}/media_publish`, { creation_id: post.container }, "POST");
      let link: string | null = null;
      try {
        link = (await graph(ig, id, { fields: "permalink" })).permalink || null;
      } catch { /* o link é só um extra */ }
      await trocar(meu, "publicando", {
        status: "publicado", erro: null, publicado_em: agoraLocal(),
        resultados: { ...(post.resultados || {}), instagram: { ok: true, id, link } },
      });
      await apagarMidia(post.arquivo); // o Instagram já tem a cópia dele
      log.push(`${post.id}: publicado ${link || id}`);
    } catch (e) {
      await falhar(meu, "publicando",
        `Instagram: ${(e as Error).message} Confira no Instagram se saiu; se não saiu, clique em “Tentar de novo”.`);
    }
  } catch (e) {
    log.push(`${post.id}: não consegui conferir (${(e as Error).message}), tento no próximo minuto`);
    if (idadeMs(post.container_desde) > ESPERA_PROCESSAMENTO_MS) {
      await falhar(post, "processando", `Instagram: ${(e as Error).message}`);
    }
  }
}

async function destravar(log: string[]) {
  // Se uma execução caiu no meio (raro), não repete sozinho para não duplicar o post.
  for (const post of await postsCom("status=in.(postando,publicando)")) {
    if (idadeMs(post.postando_desde || post.container_desde || post.criado_em) > TRAVADO_MS) {
      await falhar(post, post.status,
        "A postagem foi interrompida. Confira no Instagram se saiu; se não saiu, clique em “Tentar de novo”.");
      log.push(`${post.id}: destravado`);
    }
  }
}

async function ciclo(): Promise<string[]> {
  const log: string[] = [];
  const cfg = await config();
  await renovarToken(cfg);
  const ig = (await config()).instagram;
  await destravar(log);
  const agora = agoraLocal().slice(0, 16);
  for (const post of await postsCom(`status=eq.agendado&quando=lte.${agora}`)) await iniciar(post, ig, log);
  for (const post of await postsCom("status=eq.processando")) await acompanhar(post, ig, log);
  return log;
}

Deno.serve(async (req) => {
  if (!SEGREDO || req.headers.get("x-segredo") !== SEGREDO) {
    return new Response("proibido", { status: 403 });
  }
  try {
    const log = await ciclo();
    return Response.json({ ok: true, hora_local: agoraLocal(), log });
  } catch (e) {
    console.error(e);
    return Response.json({ ok: false, erro: (e as Error).message }, { status: 500 });
  }
});

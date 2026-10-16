/**
 * AI4Read routes for the khyang-lab Worker — REFERENCE IMPLEMENTATION for the site agent.
 * Wire it into web/worker/index.ts:   const r = await handleAI4Read(request, env, ctx); if (r) return r;
 * Contract: ../API.md. Dev mock with identical behaviour: ../dev/mock-server.mjs.
 *
 * Bindings / secrets (wrangler.jsonc + `wrangler secret put`):
 *   AI4READ_BUCKET   R2 bucket "ai4read" (posts/<slug>/... and _shared/...)
 *   AI4READ_DB       D1 database "ai4read" (schema: ../schema.sql)
 *   AI4READ_OWNERS   var, comma-separated owner emails (full access, sees all students' notes)
 *   ACCESS_TEAM      var, e.g. "khyang-lab" (→ https://khyang-lab.cloudflareaccess.com)
 *   ACCESS_AUD       var, the Access application AUD tag for /ai4read*
 *   VERTEX_PROJECT   var "playground-491901";  CLAUDE_MODEL var "claude-sonnet-5-5"
 *   Either  VERTEX_API_KEY (secret; only if the key test in HANDOFF §4 passes)
 *   or      CLAUDE_PROXY_URL (var) + CLAUDE_PROXY_SECRET (secret)  → Cloud Run proxy in ../proxy/
 *   ASK_PER_USER_DAY (var, default 40), ASK_SITE_DAY (var, default 300)
 */

export interface Env {
  AI4READ_BUCKET: R2Bucket; AI4READ_DB: D1Database;
  AI4READ_OWNERS: string; ACCESS_TEAM: string; ACCESS_AUD: string;
  VERTEX_PROJECT: string; CLAUDE_MODEL: string;
  VERTEX_API_KEY?: string; CLAUDE_PROXY_URL?: string; CLAUDE_PROXY_SECRET?: string;
  ASK_PER_USER_DAY?: string; ASK_SITE_DAY?: string;
}

const COLLS = new Set(["annotations", "notes", "guesses", "game", "diag"]);
const CSP = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob: data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'";
const SYSTEM = `You are the AI4Read tutor for a reader of a private study blog (an assistant professor in computational social science, or one of his students). Answer the reader's question about the post and the passage they selected.
- English at B2 level (some C1), short sentences, define terms at first use.
- Start with a concrete instance, then explain step by step; never skip a step; use small numbers.
- Ground factual claims in the post or the source brief provided in the conversation and give page references; keep the authors' hedges.
- If you need knowledge beyond these sources, say so clearly ("Beyond our sources: ...").
- Markdown is allowed; write inline math as $...$. About 250 words unless asked for more.`;

const json = (o: unknown, status = 200) => new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store" } });

export async function handleAI4Read(req: Request, env: Env, ctx: ExecutionContext): Promise<Response | null> {
  const url = new URL(req.url);
  const isPage = url.pathname === "/ai4read" || url.pathname.startsWith("/ai4read/");
  const isApi = url.pathname.startsWith("/api/ai4read/");
  if (!isPage && !isApi) return null;

  // 1) Identity: Cloudflare Access sits in front of /ai4read* and /api/ai4read*. Verify its JWT; never trust headers alone.
  const user = await accessUser(req, env);
  if (!user) return isApi ? json({ error: "not_signed_in" }, 401) : new Response("Sign-in required", { status: 401 });
  const role = env.AI4READ_OWNERS.split(",").map(s => s.trim().toLowerCase()).includes(user) ? "owner" : "student";

  if (isPage) return servePage(req, url, env);
  const parts = url.pathname.split("/").filter(Boolean); // ["api","ai4read",...]
  if (parts[2] === "me" && req.method === "GET") return json({ email: user, role });
  if (parts[2] === "db") return dbRoute(req, url, parts.slice(3), user, role, env);
  if (parts[2] === "ask" && req.method === "POST") return ask(req, user, role, env, ctx);
  return json({ error: "not_found" }, 404);
}

/* ---------------- pages and media from R2 (with Range for iOS audio) ---------------- */
async function servePage(req: Request, url: URL, env: Env): Promise<Response> {
  let key = url.pathname.replace(/^\/ai4read\/?/, "");
  if (key === "" ) key = "index.html";
  else if (key.endsWith("/")) key += "index.html";
  else if (!/\.[a-z0-9]+$/i.test(key)) return Response.redirect(url.origin + url.pathname + "/", 301);
  if (key.includes("..")) return new Response("Bad path", { status: 400 });
  const range = parseRange(req.headers.get("range"));
  const obj = await env.AI4READ_BUCKET.get(key, range ? { range } : undefined);
  if (!obj) return new Response("Not found", { status: 404 });
  const h = new Headers();
  obj.writeHttpMetadata(h);
  h.set("etag", obj.httpEtag);
  h.set("cache-control", "private, max-age=300");
  h.set("accept-ranges", "bytes");
  h.set("x-robots-tag", "noindex, nofollow");
  if (key.endsWith(".html")) h.set("content-security-policy", CSP);
  if (!h.get("content-type")) h.set("content-type", contentType(key));
  if (range && "offset" in range) {
    const start = range.offset!, end = start + (obj.range as any).length - 1;
    h.set("content-range", `bytes ${start}-${end}/${obj.size}`);
    h.set("content-length", String(end - start + 1));
    return new Response(obj.body, { status: 206, headers: h });
  }
  h.set("content-length", String(obj.size));
  return new Response(obj.body, { status: 200, headers: h });
}
function parseRange(v: string | null): R2Range | undefined {
  const m = v && /^bytes=(\d+)-(\d*)$/.exec(v.trim()); if (!m) return undefined;
  const start = +m[1]; return m[2] ? { offset: start, length: +m[2] - start + 1 } : { offset: start };
}
function contentType(k: string) {
  const e = k.split(".").pop()!.toLowerCase();
  return ({ html: "text/html; charset=utf-8", js: "text/javascript; charset=utf-8", css: "text/css; charset=utf-8", json: "application/json", mp3: "audio/mpeg", svg: "image/svg+xml", png: "image/png", woff2: "font/woff2" } as Record<string, string>)[e] || "application/octet-stream";
}

/* ---------------- per-user document store (D1) ---------------- */
async function dbRoute(req: Request, url: URL, p: string[], user: string, role: string, env: Env): Promise<Response> {
  const [post, coll, id] = p.map(decodeURIComponent);
  if (!post || !coll || !COLLS.has(coll) || !/^[\w.-]{1,120}$/.test(post) || (id && !/^[\w.:-]{1,200}$/.test(id))) return json({ error: "bad_path" }, 400);
  const D = env.AI4READ_DB;
  if (req.method === "GET" && !id) {
    const all = role === "owner" && url.searchParams.get("scope") === "all";
    const rs = all
      ? await D.prepare("SELECT id, user, data, updated_at FROM docs WHERE post=? AND coll=? AND deleted=0 ORDER BY updated_at").bind(post, coll).all()
      : await D.prepare("SELECT id, user, data, updated_at FROM docs WHERE post=? AND coll=? AND user=? AND deleted=0 ORDER BY updated_at").bind(post, coll, user).all();
    return json({ docs: rs.results.map((r: any) => ({ id: r.id, user: all ? r.user : undefined, data: JSON.parse(r.data), updatedAt: r.updated_at })) });
  }
  if (req.method === "GET" && id) {
    const r: any = await D.prepare("SELECT data, updated_at FROM docs WHERE post=? AND coll=? AND user=? AND id=? AND deleted=0").bind(post, coll, user, id).first();
    return json(r ? { id, data: JSON.parse(r.data), updatedAt: r.updated_at } : { id, data: null });
  }
  const body: any = req.method === "DELETE" ? null : await req.json().catch(() => null);
  const raw = body ? JSON.stringify(body.data ?? null) : "";
  if (raw.length > 200_000) return json({ error: "too_large" }, 413);
  const now = new Date().toISOString();
  if (req.method === "POST" && !id) {
    const nid = "d" + crypto.randomUUID().replace(/-/g, "").slice(0, 20);
    await D.prepare("INSERT INTO docs (post, coll, id, user, data, updated_at, deleted) VALUES (?,?,?,?,?,?,0)").bind(post, coll, nid, user, raw, now).run();
    return json({ id: nid, updatedAt: now });
  }
  if (req.method === "PUT" && id) {
    let data = body?.data ?? {};
    if (body?.merge) {
      const old: any = await D.prepare("SELECT data FROM docs WHERE post=? AND coll=? AND user=? AND id=?").bind(post, coll, user, id).first();
      data = { ...(old ? JSON.parse(old.data) : {}), ...data };
    }
    await D.prepare("INSERT INTO docs (post, coll, id, user, data, updated_at, deleted) VALUES (?,?,?,?,?,?,0) ON CONFLICT(post, coll, user, id) DO UPDATE SET data=excluded.data, updated_at=excluded.updated_at, deleted=0")
      .bind(post, coll, id, user, JSON.stringify(data), now).run();
    return json({ id, updatedAt: now });
  }
  if (req.method === "DELETE" && id) {
    await D.prepare("UPDATE docs SET deleted=1, updated_at=? WHERE post=? AND coll=? AND user=? AND id=?").bind(now, post, coll, user, id).run();
    return new Response(null, { status: 204 });
  }
  return json({ error: "method_not_allowed" }, 405);
}

/* ---------------- Ask Claude (Claude Sonnet on Vertex AI), streamed as SSE ---------------- */
async function ask(req: Request, user: string, role: string, env: Env, ctx: ExecutionContext): Promise<Response> {
  const body: any = await req.json().catch(() => null);
  const msgs = Array.isArray(body?.messages) ? body.messages : null;
  if (!msgs || !msgs.length || msgs.length > 24 || JSON.stringify(msgs).length > 180_000) return json({ error: "invalid_request" }, 400);
  const clean = msgs.map((m: any) => ({ role: m.role === "assistant" ? "assistant" : "user", content: String(m.content ?? "").slice(0, 120_000) }));
  if (clean[clean.length - 1].role !== "user") return json({ error: "invalid_request" }, 400);

  // Budget: per user per day and site-wide per day (JST day).
  const day = new Date(Date.now() + 9 * 3600e3).toISOString().slice(0, 10);
  const D = env.AI4READ_DB;
  const perUser = +(env.ASK_PER_USER_DAY || 40) * (role === "owner" ? 3 : 1), site = +(env.ASK_SITE_DAY || 300);
  const u: any = await D.prepare("SELECT count FROM usage WHERE day=? AND user=?").bind(day, user).first();
  const s: any = await D.prepare("SELECT SUM(count) AS n FROM usage WHERE day=?").bind(day).first();
  if ((u?.count || 0) >= perUser || (s?.n || 0) >= site) return json({ error: "rate_limited" }, 429);
  await D.prepare("INSERT INTO usage (day, user, count) VALUES (?,?,1) ON CONFLICT(day, user) DO UPDATE SET count=count+1").bind(day, user).run();

  const payload = {
    anthropic_version: "vertex-2023-10-16",
    max_tokens: 1500,
    stream: true,
    system: [{ type: "text", text: SYSTEM, cache_control: { type: "ephemeral" } }],
    messages: clean,
  };
  let upstream: Response;
  if (env.CLAUDE_PROXY_URL) {
    upstream = await fetch(env.CLAUDE_PROXY_URL, { method: "POST", headers: { "content-type": "application/json", "x-proxy-secret": env.CLAUDE_PROXY_SECRET || "" }, body: JSON.stringify(payload) });
  } else {
    const endpoint = `https://aiplatform.googleapis.com/v1/projects/${env.VERTEX_PROJECT}/locations/global/publishers/anthropic/models/${env.CLAUDE_MODEL}:streamRawPredict`;
    upstream = await fetch(endpoint, { method: "POST", headers: { "content-type": "application/json", "x-goog-api-key": env.VERTEX_API_KEY || "" }, body: JSON.stringify(payload) });
  }
  if (!upstream.ok || !upstream.body) {
    return json({ error: upstream.status === 429 ? "rate_limited" : "upstream_error" }, upstream.status === 429 ? 429 : 502);
  }
  // Convert Anthropic SSE → our minimal SSE: data: {"delta": "..."} … data: {"done": true}
  const { readable, writable } = new TransformStream();
  const w = writable.getWriter(), enc = new TextEncoder(), dec = new TextDecoder();
  ctx.waitUntil((async () => {
    const r = upstream.body!.getReader(); let buf = "";
    try {
      for (;;) {
        const { done, value } = await r.read(); if (done) break;
        buf += dec.decode(value, { stream: true });
        const lines = buf.split("\n"); buf = lines.pop() || "";
        for (const line of lines) {
          if (!line.startsWith("data:")) continue;
          let ev: any; try { ev = JSON.parse(line.slice(5)); } catch { continue; }
          if (ev.type === "content_block_delta" && ev.delta?.type === "text_delta") await w.write(enc.encode(`data: ${JSON.stringify({ delta: ev.delta.text })}\n\n`));
          if (ev.type === "message_delta" && ev.delta?.stop_reason === "max_tokens") await w.write(enc.encode(`data: {"truncated":true}\n\n`));
          if (ev.type === "error") await w.write(enc.encode(`data: ${JSON.stringify({ error: "upstream_error", message: ev.error?.message })}\n\n`));
        }
      }
      await w.write(enc.encode(`data: {"done":true}\n\n`));
    } finally { await w.close(); }
  })());
  return new Response(readable, { headers: { "content-type": "text/event-stream; charset=utf-8", "cache-control": "no-store" } });
}

/* ---------------- Cloudflare Access JWT verification ---------------- */
let JWKS: { keys: any[]; at: number } | null = null;
async function accessUser(req: Request, env: Env): Promise<string | null> {
  const tok = req.headers.get("cf-access-jwt-assertion"); if (!tok) return null;
  const [h, p, s] = tok.split("."); if (!h || !p || !s) return null;
  const head = JSON.parse(b64urlText(h)), pay = JSON.parse(b64urlText(p));
  if (!JWKS || Date.now() - JWKS.at > 3600e3) {
    const r = await fetch(`https://${env.ACCESS_TEAM}.cloudflareaccess.com/cdn-cgi/access/certs`);
    JWKS = { keys: ((await r.json()) as any).keys, at: Date.now() };
  }
  const jwk = JWKS.keys.find((k: any) => k.kid === head.kid); if (!jwk) return null;
  const key = await crypto.subtle.importKey("jwk", jwk, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["verify"]);
  const ok = await crypto.subtle.verify("RSASSA-PKCS1-v1_5", key, b64urlBytes(s), new TextEncoder().encode(`${h}.${p}`));
  const aud = Array.isArray(pay.aud) ? pay.aud : [pay.aud];
  if (!ok || !aud.includes(env.ACCESS_AUD) || pay.exp * 1000 < Date.now()) return null;
  return String(pay.email || "").toLowerCase() || null;
}
function b64urlBytes(s: string) { const b = atob(s.replace(/-/g, "+").replace(/_/g, "/") + "===".slice((s.length + 3) % 4)); return Uint8Array.from(b, c => c.charCodeAt(0)); }
function b64urlText(s: string) { return new TextDecoder().decode(b64urlBytes(s)); }

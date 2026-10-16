// Local stand-in for the Worker routes (same contract as worker/ai4read.ts), for testing the post pages.
// Usage: node dev/mock-server.mjs [port]   → http://localhost:8799/ai4read/<slug>/
// No auth (user "dev@local", role owner); "ask" streams a canned answer; data lives in memory.
import http from "node:http"; import fs from "node:fs"; import path from "node:path";
const ROOT = path.join(path.dirname(new URL(import.meta.url).pathname), "..", "dist");
const PORT = +(process.argv[2] || 8799);
const CSP = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob: data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'";
const T = { html: "text/html; charset=utf-8", js: "text/javascript; charset=utf-8", css: "text/css; charset=utf-8", json: "application/json", mp3: "audio/mpeg" };
const store = new Map(); // key post|coll|id -> {data, updatedAt}
const send = (res, code, obj) => { res.writeHead(code, { "content-type": "application/json" }); res.end(JSON.stringify(obj)); };
http.createServer(async (req, res) => {
  const u = new URL(req.url, "http://x"); const p = u.pathname;
  if (p.startsWith("/api/ai4read/")) {
    const parts = p.split("/").filter(Boolean).map(decodeURIComponent);
    let body = ""; for await (const c of req) body += c; const j = body ? JSON.parse(body) : null;
    if (parts[2] === "me") return send(res, 200, { email: "dev@local", role: "owner" });
    if (parts[2] === "db") {
      const [post, coll, id] = parts.slice(3); const pre = `${post}|${coll}|`; const now = new Date().toISOString();
      if (req.method === "GET" && !id) return send(res, 200, { docs: [...store].filter(([k]) => k.startsWith(pre)).map(([k, v]) => ({ id: k.slice(pre.length), data: v.data, updatedAt: v.updatedAt })) });
      if (req.method === "GET") { const v = store.get(pre + id); return send(res, 200, { id, data: v ? v.data : null }); }
      if (req.method === "POST") { const nid = "d" + Math.random().toString(36).slice(2, 12); store.set(pre + nid, { data: j.data, updatedAt: now }); return send(res, 200, { id: nid, updatedAt: now }); }
      if (req.method === "PUT") { const old = store.get(pre + id); store.set(pre + id, { data: j.merge && old ? { ...old.data, ...j.data } : j.data, updatedAt: now }); return send(res, 200, { id, updatedAt: now }); }
      if (req.method === "DELETE") { store.delete(pre + id); res.writeHead(204).end(); return; }
    }
    if (parts[2] === "ask") {
      res.writeHead(200, { "content-type": "text/event-stream" });
      const q = (j.messages.at(-1).content || "").slice(-80);
      for (const w of `**Mock answer.** You asked: “${q}”. A concrete instance first: $2^5=32$, so 5 yes/no questions find one of 32 cups.`.split(" ")) { res.write(`data: ${JSON.stringify({ delta: w + " " })}\n\n`); await new Promise(r => setTimeout(r, 15)); }
      res.end(`data: {"done":true}\n\n`); return;
    }
    return send(res, 404, { error: "not_found" });
  }
  if (!p.startsWith("/ai4read/")) { res.writeHead(404).end(); return; }
  let rel = p.replace(/^\/ai4read\//, ""); if (rel === "" || rel.endsWith("/")) rel += "index.html";
  let f = path.join(ROOT, rel); if (!fs.existsSync(f)) { const m2 = /^([^/]+)\/audio\/(.+)$/.exec(rel); if (m2) f = path.join(ROOT, "..", "..", "..", "posts", m2[1], "audio", m2[2]); }
  if (!f.startsWith(path.join(ROOT, "..", "..", "..")) || !fs.existsSync(f)) { res.writeHead(404).end("not found"); return; }
  const size = fs.statSync(f).size, ext = f.split(".").pop();
  const h = { "content-type": T[ext] || "application/octet-stream", "accept-ranges": "bytes", "cache-control": "no-store" };
  if (ext === "html") h["content-security-policy"] = CSP;
  const m = /^bytes=(\d+)-(\d*)$/.exec(req.headers.range || "");
  if (m) { const s = +m[1], e = m[2] ? +m[2] : size - 1; res.writeHead(206, { ...h, "content-range": `bytes ${s}-${e}/${size}`, "content-length": e - s + 1 }); fs.createReadStream(f, { start: s, end: e }).pipe(res); return; }
  res.writeHead(200, { ...h, "content-length": size }); fs.createReadStream(f).pipe(res);
}).listen(PORT, () => console.log(`mock on http://localhost:${PORT}/ai4read/`));

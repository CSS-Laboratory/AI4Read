// Writes dist/index.html: the private AI4Read shelf (list of posts), from dist/*/post.json.
import fs from "node:fs"; import path from "node:path";
const D = path.join(path.dirname(new URL(import.meta.url).pathname), "dist");
const posts = fs.readdirSync(D).filter(d => fs.existsSync(path.join(D, d, "post.json"))).map(d => JSON.parse(fs.readFileSync(path.join(D, d, "post.json"), "utf8"))).sort((a, b) => b.date.localeCompare(a.date));
const esc = s => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;");
fs.writeFileSync(path.join(D, "index.html"), `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex,nofollow"><title>AI4Read · Posts</title><link rel="stylesheet" href="_shared/shelf.css"></head><body><main>
<p class="eyebrow">AI4Read · private</p><h1>Posts</h1>
<ul>${posts.map(p => `<li><a href="${p.slug}/"><b>${esc(p.title)}</b></a><span>${esc(p.date)} · ${p.chapters} audio chapters</span><p>${esc(p.summary)}</p></li>`).join("")}</ul>
</main></body></html>`);
fs.writeFileSync(path.join(D, "_shared", "shelf.css"), `:root{--paper:#F4F5F2;--ink:#1F2733;--muted:#5D6672;--rule:#DADDD6;--stamp:#A3342B;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--paper:#15181D;--ink:#E6E8EA;--muted:#9AA3AE;--rule:#2E343D;--stamp:#E0796E;color-scheme:dark}}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.55 "IBM Plex Sans",system-ui,sans-serif;padding:24px max(16px,env(safe-area-inset-left)) 48px max(16px,env(safe-area-inset-right))}
main{max-width:40rem;margin:0 auto}.eyebrow{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--stamp)}
h1{font:600 34px/1.1 Georgia,serif;margin:6px 0 18px}ul{list-style:none;padding:0;display:grid;gap:16px}li{border-top:1px solid var(--rule);padding-top:12px}
a{color:var(--ink);text-decoration:none;font-size:19px}span{display:block;color:var(--muted);font-size:13px}p{margin:6px 0 0}`);
console.log(`index: ${posts.length} post(s)`);

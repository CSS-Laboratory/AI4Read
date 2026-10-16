// Build the post page: KaTeX -> MathML (no fonts/CSS needed), code + brief + chapters inlined.
// Usage: node build.mjs   (NODE_PATH=/tmp/kt/node_modules)
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const ROOTREQ = path.join(path.dirname(new URL(import.meta.url).pathname), "..", "..", "package.json");
const require = createRequire(fs.existsSync(path.join(path.dirname(ROOTREQ), "node_modules", "katex")) ? ROOTREQ : "/tmp/kt/");
const katex = require("katex");
const hljs = require("highlight.js/lib/core"); hljs.registerLanguage("python", require("highlight.js/lib/languages/python"));
const D = path.dirname(new URL(import.meta.url).pathname);
const rd = f => fs.readFileSync(path.join(D, f), "utf8");
let html = rd("src/content.html"); let errors = 0;
// Link every citation to its source entry (data-src). A cite without an author name inherits the last named source in the same section.
const KEYS = [[/Shannon 1948/,"shannon1948"],[/Shannon 1951/,"shannon1951"],[/Cover/,"cover"],[/Bengio/,"bengio"],[/Mikolov et al\. 2013a/,"mikolov2013a"],[/Mikolov et al\. 2013b/,"mikolov2013b"],[/Vaswani/,"vaswani"],[/Radford/,"radford"],[/Brown/,"brown"],[/Kaplan/,"kaplan"],[/Xie/,"xie"],[/Bender/,"bender"],[/Piantadosi/,"piantadosi"],[/Mahowald/,"mahowald"],[/Kosinski/,"kosinski"],[/Ullman/,"ullman"],[/Strachan/,"strachan"],[/Shapira/,"shapira"]];
const NAMES = [[/Shannon 1948|Shannon’s 1948|Shannon \(1948\)/g,"shannon1948"],[/Shannon 1951|Shannon \(1951\)/g,"shannon1951"],[/Cover (and|&amp;) Thomas/g,"cover"],[/Bengio/g,"bengio"],[/Mikolov, Yih|Mikolov et al\. 2013b/g,"mikolov2013b"],[/Mikolov(?!, Yih)/g,"mikolov2013a"],[/Vaswani|Transformer paper/g,"vaswani"],[/GPT-2|Radford/g,"radford"],[/GPT-3’s authors|GPT-3 paper|Brown et al/g,"brown"],[/Kaplan/g,"kaplan"],[/Xie/g,"xie"],[/Bender/g,"bender"],[/Piantadosi/g,"piantadosi"],[/Mahowald/g,"mahowald"],[/Kosinski/g,"kosinski"],[/Ullman/g,"ullman"],[/Strachan/g,"strachan"],[/Shapira/g,"shapira"]];
const citeLog = []; {
  const secStarts = [...html.matchAll(/<section id="([^"]+)"/g)].map(m => [m.index, m[1]]);
  const secAt = i => { let s = ["", 0]; for (const [p, id] of secStarts) if (p <= i) s = [id, p]; return s; };
  const lastNamed = {}; // section -> last key from a named cite
  html = html.replace(/<span class="cite">([^<]*)<\/span>/g, (m, txt, off) => {
    const [sec, sp] = secAt(off); let key = null, how = "named";
    const hit = KEYS.find(([re]) => re.test(txt));
    if (hit) key = hit[1];
    else { // nearest author mention in the prose before this cite, same section
      const before = html.slice(sp, off); let best = -1;
      for (const [re, k] of NAMES) { re.lastIndex = 0; let mm; while ((mm = re.exec(before))) if (mm.index > best) { best = mm.index; key = k; } }
      how = "prose"; if (!key) { key = lastNamed[sec] || null; how = "inherited"; }
    }
    if (hit) lastNamed[sec] = key;
    citeLog.push([sec, txt, key || "", how]);
    return key ? `<span class="cite" data-src="${key}" tabindex="0" role="button">${txt}</span>` : m; }); }
fs.writeFileSync(path.join(D, "review", "cite-map.tsv"), citeLog.map(r => r.join("\t")).join("\n"));

const render = (tex, display) => { try { return katex.renderToString(tex, { displayMode: display, output: "mathml", throwOnError: true, strict: "ignore" }); }
  catch (e) { errors++; console.error("KaTeX:", e.message, "\n  in:", tex); return `<code>${tex}</code>`; } };
html = html.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => `<div class="mjx">${render(t.trim(), true)}</div>`);
html = html.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => render(t.trim(), false));
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const code = { "code-1": "notebook/ex1_shannon_fn.py", "code-2": "notebook/ex2_attention.py", "code-3": "notebook/ex3_bits_per_char.py" };
for (const [id, f] of Object.entries(code)) html = html.replace(`<code id="${id}"></code>`, `<code id="${id}" class="hljs language-python">${hljs.highlight(rd(f), { language: "python" }).value}</code>`);
let chapters = [];
try { chapters = JSON.parse(rd("audio/chapters.json")).map(c => ({ id: c.id, title: c.title, dur: c.dur, src: `audio/${c.id}.mp3` })); } catch (e) { console.error("no chapters yet"); }
const brief = rd("source-brief.md").split("\n---\n").slice(1).join("\n---\n");
const out = `<title>What Does an LLM Know?</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
${rd("src/style.css")}
${rd("src/annotate.css")}
</style>
${html}
<script type="application/json" id="brief-data">${JSON.stringify(brief).replace(/</g, "\\u003c")}</script>
<script>window.CHAPTERS=${JSON.stringify(chapters)};</script>
<script>
${rd("src/app.js")}
</script>
<script>
${rd("src/figs.js")}
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.1.6/purify.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script>
${rd("src/annotate.js")}
</script>
`;
fs.writeFileSync(path.join(D, "index.html"), out);
console.log(`index.html ${(out.length / 1024).toFixed(0)} KB, math errors: ${errors}, chapters: ${chapters.length}`);

// ---------- Website build (khyang-lab.org/ai4read/<slug>/): external files only, strict-CSP friendly ----------
if (process.argv.includes("--site")) {
  const SLUG = path.basename(D);
  const SITE = path.join(D, "..", "..", "site", "ai4read");
  const OUT = path.join(SITE, "dist", SLUG), SH = path.join(SITE, "dist", "_shared");
  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, "audio"), { recursive: true }); fs.mkdirSync(path.join(SH, "lib"), { recursive: true });
  for (const f of fs.readdirSync(path.join(D, "audio"))) if (f.endsWith(".mp3") || f === "chapters.json") fs.copyFileSync(path.join(D, "audio", f), path.join(OUT, "audio", f));
  fs.writeFileSync(path.join(OUT, "post.css"), rd("src/style.css") + "\n" + rd("src/annotate.css"));
  fs.writeFileSync(path.join(OUT, "data.js"), `window.CHAPTERS=${JSON.stringify(chapters)};`);
  for (const f of ["app.js", "figs.js", "annotate.js"]) fs.copyFileSync(path.join(D, "src", f), path.join(OUT, f));
  fs.copyFileSync(path.join(SITE, "shared", "site-shim.js"), path.join(SH, "site-shim.js"));
  for (const [src, dst] of [["marked/marked.min.js", "marked.min.js"], ["dompurify/dist/purify.min.js", "purify.min.js"], ["katex/dist/katex.min.js", "katex.min.js"]])
    fs.copyFileSync(require.resolve(src.replace(/^(\w+)\/(.*)$/, "$1/$2")), path.join(SH, "lib", dst));
  const page = `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<meta name="ai4read-post" content="${SLUG}">
<title>What Does an LLM Know? · AI4Read</title>
<link rel="stylesheet" href="post.css">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}[hidden]{display:none!important}img{max-width:100%}</style>
</head><body>
${html}
<script type="application/json" id="brief-data">${JSON.stringify(brief).replace(/</g, "\\u003c")}</script>
<script src="/ai4read/_shared/site-shim.js"></script>
<script src="data.js"></script>
<script src="app.js"></script>
<script src="figs.js"></script>
<script src="/ai4read/_shared/lib/marked.min.js"></script>
<script src="/ai4read/_shared/lib/purify.min.js"></script>
<script src="/ai4read/_shared/lib/katex.min.js"></script>
<script src="annotate.js"></script>
</body></html>
`;
  fs.writeFileSync(path.join(OUT, "index.html"), page);
  const meta = { slug: SLUG, title: "What does an LLM know when it predicts the next word?", date: "2026-10-15", summary: "Next-word prediction through information theory, linear algebra, Bayesian inference, philosophy of meaning and theory of mind.", chapters: chapters.length, built: new Date().toISOString() };
  fs.writeFileSync(path.join(OUT, "post.json"), JSON.stringify(meta, null, 1));
  // context the Worker may use to ground "Ask Claude" server-side
  fs.writeFileSync(path.join(OUT, "context.json"), JSON.stringify({ slug: SLUG, brief }));
  console.log("site build →", OUT);
}

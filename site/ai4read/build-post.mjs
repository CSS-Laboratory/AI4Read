#!/usr/bin/env node
// Generic AI4Read post builder (posts 02+). Post 01 keeps its own build.mjs.
//   node site/ai4read/build-post.mjs posts/<slug> [--site] [--public] [--owner]
//   --site    legacy /ai4read/ build → site/ai4read/dist/<slug>/
//   --public  blog build for everyone → site/ai4read/dist-public/<slug>/ (served at /blog/<slug>/): English only,
//             no owner code (no annotate.js, notes, Ask-Claude, 中 audio), no /api/ai4read requests, indexable, canonical + OG
//   --owner   owner edition → site/ai4read/dist-owner/<slug>/ (served at /blog/_owner/<slug>/ behind Access):
//             full features, Chinese audio (audio-zh/) and Chinese text (zh/, from src/content-zh.html) when present
// Inputs in the post folder:
//   post.json            {title, short, num, date, summary, cites:[[regex,key],...], names:[[regex,key],...], code:{id:file}}
//   src/content.html     sections (template markup + component widgets)
//   src/extra.css|js     optional post-specific additions (prefer widgets; no custom JS from the writer)
//   source-brief.verified.md (or source-brief.md), audio/chapters.json
// Shared: site/ai4read/template/{style.css, annotate.css, core.js, common.js, annotate.js}, site/ai4read/components/widgets.{js,css}
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..", "..");
const require = createRequire(fs.existsSync(path.join(ROOT, "node_modules", "katex")) ? path.join(ROOT, "package.json") : "/tmp/kt/");
const katex = require("katex");
const hljs = require("highlight.js/lib/core"); hljs.registerLanguage("python", require("highlight.js/lib/languages/python"));
const D = path.resolve(process.argv[2] || "."); const SLUG = path.basename(D);
const TPL = path.join(ROOT, "site", "ai4read", "template"), CMP = path.join(ROOT, "site", "ai4read", "components");
const rd = (f, base = D) => fs.readFileSync(path.join(base, f), "utf8");
const has = (f) => fs.existsSync(path.join(D, f));
const cfg = JSON.parse(rd("post.json"));
let html = rd("src/content.html"); let errors = 0;
fs.mkdirSync(path.join(D, "review"), { recursive: true });

// citations → data-src (named cite, else nearest author mention earlier in the same section, else inherited)
const KEYS = (cfg.cites || []).map(([re, k]) => [new RegExp(re), k]);
const NAMES = (cfg.names || cfg.cites || []).map(([re, k]) => [new RegExp(re, "g"), k]);
function mapCites(h, log) {
  const secStarts = [...h.matchAll(/<section id="([^"]+)"/g)].map((m) => [m.index, m[1]]);
  const secAt = (i) => { let s = ["", 0]; for (const [p, id] of secStarts) if (p <= i) s = [id, p]; return s; };
  const lastNamed = {};
  return h.replace(/<span class="cite">([^<]*)<\/span>/g, (m, txt, off) => {
    const [sec, sp] = secAt(off); let key = null, how = "named";
    const hit = KEYS.find(([re]) => re.test(txt));
    if (hit) key = hit[1];
    else { const before = h.slice(sp, off); let best = -1;
      for (const [re, k] of NAMES) { re.lastIndex = 0; let mm; while ((mm = re.exec(before))) if (mm.index > best) { best = mm.index; key = k; } }
      how = "prose"; if (!key) { key = lastNamed[sec] || null; how = "inherited"; } }
    if (hit) lastNamed[sec] = key;
    log.push([sec, txt, key || "", how]);
    return key ? `<span class="cite" data-src="${key}" tabindex="0" role="button">${txt}</span>` : m; });
}
const citeLog = []; html = mapCites(html, citeLog);
fs.writeFileSync(path.join(D, "review", "cite-map.tsv"), citeLog.map((r) => r.join("\t")).join("\n"));
const unmapped = citeLog.filter((r) => !r[2]).length;
const missingSrc = [...new Set(citeLog.map((r) => r[2]).filter(Boolean))].filter((k) => !html.includes(`id="src-${k}"`));

function renderMath(html) {
  html = html.replace(/\\\[([\s\S]+?)\\\]/g, (_, t) => `<div class="mjx">${render(t.trim(), true)}</div>`);
  html = html.replace(/\\\(([\s\S]+?)\\\)/g, (_, t) => render(t.trim(), false));
  for (const [id, f] of Object.entries(cfg.code || {})) html = html.replace(`<code id="${id}"></code>`, `<code id="${id}" class="hljs language-python">${hljs.highlight(rd(f), { language: "python" }).value}</code>`);
  return html;
}
const render = (tex, display) => { try { return katex.renderToString(tex, { displayMode: display, output: "mathml", throwOnError: true, strict: "ignore" }); }
  catch (e) { errors++; console.error("KaTeX:", e.message, "\n  in:", tex); return `<code>${tex}</code>`; } };
html = renderMath(html);

let chapters = [];
try { chapters = JSON.parse(rd("audio/chapters.json")).map((c) => ({ id: c.id, title: c.title, dur: c.dur, src: `audio/${c.id}.mp3` })); } catch { console.error("no chapters yet"); }
const audioMB = has("audio/all.mp3") ? Math.round(fs.statSync(path.join(D, "audio/all.mp3")).size / 1e6) : 0;
// post.json "brief": list of brief files, most authoritative first (default: the single verified brief).
const briefFiles = cfg.brief || [has("source-brief.verified.md") ? "source-brief.verified.md" : "source-brief.md"];
const stripBody = (t) => t.split("\n---\n").slice(1).join("\n---\n") || t;
// Posts stand alone: drop brief lines that mention other posts, so the page tutor never cites them.
const noCross = (t) => t.split("\n").filter((l) => !/\bpost (0?\d+|one|two|three)\b/i.test(l)).join("\n");
const brief = (briefFiles.length > 1 ? `Several source briefs follow, most authoritative first. Where they differ, follow the earlier one and the post itself.\n\n` : "") +
  briefFiles.map((f) => `# ${f}\n\n` + noCross(stripBody(rd(f)))).join("\n\n");
const POST = { slug: SLUG, title: cfg.title, album: `Post ${String(cfg.num).padStart(2, "0")} · ${cfg.short}`, prefix: `ai4read-p${String(cfg.num).padStart(2, "0")}`,
  mp3Name: `AI4Read-${String(cfg.num).padStart(2, "0")}-${SLUG}.mp3`, audioMB };
const css = [rd("style.css", TPL), rd("annotate.css", TPL), rd("widgets.css", CMP), has("src/extra.css") ? rd("src/extra.css") : ""].join("\n");
const js = { core: rd("core.js", TPL), common: rd("common.js", TPL), widgets: rd("widgets.js", CMP), annotate: rd("annotate.js", TPL), extra: has("src/extra.js") ? rd("src/extra.js") : "" };
// Inlined scripts must not contain "</script" (it would end the <script> element early).
const inl = (t) => t.replace(/<\/script/gi, "<\\/script");
const dataJS = `window.POST=${JSON.stringify(POST)};window.CHAPTERS=${JSON.stringify(chapters)};`;
const briefTag = `<script type="application/json" id="brief-data">${JSON.stringify(brief).replace(/</g, "\\u003c")}</script>`;

const out = `<title>${cfg.short}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
${css}
</style>
${html}
${briefTag}
<script>${dataJS}</script>
<script>
${inl(js.core)}
</script>
<script>
${inl(js.widgets)}
</script>
<script>
${inl(js.common)}
${inl(js.extra)}
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dompurify/3.1.6/purify.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js"></script>
<script>
${inl(js.annotate)}
</script>
`;
fs.writeFileSync(path.join(D, "index.html"), out);
console.log(`index.html ${(out.length / 1024).toFixed(0)} KB · math errors ${errors} · chapters ${chapters.length} · cites ${citeLog.length} (unmapped ${unmapped}, missing source entries: ${missingSrc.join(",") || "none"})`);

if (process.argv.includes("--site")) {
  const SITE = path.join(ROOT, "site", "ai4read");
  const OUT = path.join(SITE, "dist", SLUG), SH = path.join(SITE, "dist", "_shared");
  fs.rmSync(OUT, { recursive: true, force: true });
  fs.mkdirSync(path.join(OUT, "audio"), { recursive: true }); fs.mkdirSync(path.join(SH, "lib"), { recursive: true });
  if (has("audio")) for (const f of fs.readdirSync(path.join(D, "audio"))) if (f.endsWith(".mp3") || f === "chapters.json") fs.copyFileSync(path.join(D, "audio", f), path.join(OUT, "audio", f));
  if (has("notebook")) { const nb = fs.readdirSync(path.join(D, "notebook")).filter((f) => f.endsWith(".ipynb") || f === "README.md");
    if (nb.length) { fs.mkdirSync(path.join(OUT, "notebook"), { recursive: true }); for (const f of nb) fs.copyFileSync(path.join(D, "notebook", f), path.join(OUT, "notebook", f)); } }
  fs.writeFileSync(path.join(OUT, "post.css"), css);
  fs.writeFileSync(path.join(OUT, "data.js"), dataJS);
  fs.writeFileSync(path.join(OUT, "app.js"), js.core);
  fs.writeFileSync(path.join(OUT, "figs.js"), js.common + "\n" + js.extra);
  fs.writeFileSync(path.join(OUT, "widgets.js"), js.widgets);
  fs.writeFileSync(path.join(OUT, "annotate.js"), js.annotate);
  fs.copyFileSync(path.join(SITE, "shared", "site-shim.js"), path.join(SH, "site-shim.js"));
  for (const [src, dst] of [["marked/marked.min.js", "marked.min.js"], ["dompurify/dist/purify.min.js", "purify.min.js"], ["katex/dist/katex.min.js", "katex.min.js"]])
    fs.copyFileSync(require.resolve(src), path.join(SH, "lib", dst));
  const page = `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<meta name="ai4read-post" content="${SLUG}">
<title>${cfg.short} · AI4Read</title>
<link rel="stylesheet" href="post.css">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}[hidden]{display:none!important}img{max-width:100%}</style>
</head><body>
${html}
${briefTag}
<script src="/ai4read/_shared/site-shim.js"></script>
<script src="data.js"></script>
<script src="app.js"></script>
<script src="widgets.js"></script>
<script src="figs.js"></script>
<script src="/ai4read/_shared/lib/marked.min.js"></script>
<script src="/ai4read/_shared/lib/purify.min.js"></script>
<script src="/ai4read/_shared/lib/katex.min.js"></script>
<script src="annotate.js"></script>
</body></html>
`;
  fs.writeFileSync(path.join(OUT, "index.html"), page);
  fs.writeFileSync(path.join(OUT, "post.json"), JSON.stringify({ slug: SLUG, title: cfg.title, date: cfg.date, summary: cfg.summary, chapters: chapters.length, built: new Date().toISOString() }, null, 1));
  fs.writeFileSync(path.join(OUT, "context.json"), JSON.stringify({ slug: SLUG, brief }));
  console.log("site build →", OUT);
}

// ---------------------------------------------------------------- blog builds (2026-11-28, website plan)
const SITE_DIR = path.join(ROOT, "site", "ai4read"), ORIGIN = "https://khyang-lab.org";
const escA = (t) => String(t || "").replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/</g, "&lt;");
function copyDir(src, dst, keep) { if (!fs.existsSync(src)) return 0; let n = 0; fs.mkdirSync(dst, { recursive: true });
  for (const f of fs.readdirSync(src)) if (keep(f)) { fs.copyFileSync(path.join(src, f), path.join(dst, f)); n++; } return n; }
function blogPage({ body, lang, shared, owner, head, scripts }) {   // the brief (Ask-Claude context) ships in the owner edition only
  return `<!doctype html>
<html lang="${lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
${head}
<meta name="ai4read-post" content="${SLUG}">
<link rel="stylesheet" href="${owner && lang === "zh" ? "../" : ""}post.css">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}[hidden]{display:none!important}img{max-width:100%}</style>
</head><body>
${body}
${owner ? briefTag : ""}
${scripts}
</body></html>
`;
}
function writeCommon(OUT, withAnnotate) {
  fs.writeFileSync(path.join(OUT, "post.css"), css);
  fs.writeFileSync(path.join(OUT, "data.js"), dataJS);
  fs.writeFileSync(path.join(OUT, "app.js"), js.core);
  fs.writeFileSync(path.join(OUT, "figs.js"), js.common + "\n" + js.extra);
  fs.writeFileSync(path.join(OUT, "widgets.js"), js.widgets);
  if (withAnnotate) fs.writeFileSync(path.join(OUT, "annotate.js"), js.annotate);
  copyDir(path.join(D, "audio"), path.join(OUT, "audio"), (f) => f.endsWith(".mp3") || f === "chapters.json");
  copyDir(path.join(D, "notebook"), path.join(OUT, "notebook"), (f) => f.endsWith(".ipynb") || f.endsWith(".py") || f === "README.md");
}
const PM = (() => { try { return JSON.parse(fs.readFileSync(path.join(ROOT, "site", "ai4read", "posts-meta.json"), "utf8")).posts.find((p) => p.slug === SLUG) || {}; } catch { return {}; } })();
for (const k of ["series", "field", "tags", "status", "published_at", "og_image"]) if (cfg[k] == null && PM[k] != null) cfg[k] = PM[k];   // older posts: metadata from posts-meta.json
const meta = { slug: SLUG, title: cfg.title, date: cfg.date, summary: cfg.summary, series: cfg.series || null, field: cfg.field || null,
  tags: cfg.tags || [], status: cfg.status || "draft", published_at: cfg.published_at || null,
  reading_minutes: Math.max(1, Math.round(html.replace(/<[^>]+>/g, " ").split(/\s+/).filter(Boolean).length / 200)),
  audio_minutes: Math.round(chapters.reduce((a, c) => a + (c.dur || 0), 0) / 60), og_image: cfg.og_image || null,
  chapters: chapters.length, built: new Date().toISOString() };
if (process.argv.includes("--public")) {
  const OUT = path.join(SITE_DIR, "dist-public", SLUG), SH = path.join(SITE_DIR, "dist-public", "_shared");
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true }); fs.mkdirSync(SH, { recursive: true });
  writeCommon(OUT, false);
  fs.copyFileSync(path.join(SITE_DIR, "shared", "site-shim-public.js"), path.join(SH, "site-shim-public.js"));
  if (cfg.og_image && has(cfg.og_image)) fs.copyFileSync(path.join(D, cfg.og_image), path.join(OUT, path.basename(cfg.og_image)));
  const url = `${ORIGIN}/blog/${SLUG}/`, og = cfg.og_image ? `${url}${path.basename(cfg.og_image)}` : null;
  const head = `<title>${escA(cfg.title)} · AI4Read · CSS Lab</title>
<meta name="description" content="${escA(cfg.summary)}">
<link rel="canonical" href="${url}">
<meta property="og:type" content="article"><meta property="og:title" content="${escA(cfg.title)}">
<meta property="og:description" content="${escA(cfg.summary)}"><meta property="og:url" content="${url}">${og ? `\n<meta property="og:image" content="${og}">` : ""}`;
  const scripts = `<script src="/blog/_shared/site-shim-public.js"></script>
<script src="data.js"></script>
<script src="app.js"></script>
<script src="widgets.js"></script>
<script src="figs.js"></script>`;
  fs.writeFileSync(path.join(OUT, "index.html"), blogPage({ body: html, lang: "en", owner: false, head, scripts }));
  fs.writeFileSync(path.join(OUT, "post.json"), JSON.stringify({ ...meta, url: `/blog/${SLUG}/` }, null, 1));
  const bad = fs.readFileSync(path.join(OUT, "index.html"), "utf8").match(/\/api\/ai4read|annotate\.js|audio-zh/g);
  if (bad) { console.error("public build contains owner references:", [...new Set(bad)]); process.exitCode = 1; }
  console.log("public build →", OUT);
}
if (process.argv.includes("--owner")) {
  const OUT = path.join(SITE_DIR, "dist-owner", SLUG), SH = path.join(SITE_DIR, "dist-owner", "_shared");
  fs.rmSync(OUT, { recursive: true, force: true }); fs.mkdirSync(OUT, { recursive: true }); fs.mkdirSync(path.join(SH, "lib"), { recursive: true });
  writeCommon(OUT, true);
  copyDir(path.join(D, "audio-zh"), path.join(OUT, "audio-zh"), (f) => f.endsWith(".mp3") || f === "chapters.json");
  fs.copyFileSync(path.join(SITE_DIR, "shared", "site-shim.js"), path.join(SH, "site-shim.js"));
  for (const [src, dst] of [["marked/marked.min.js", "marked.min.js"], ["dompurify/dist/purify.min.js", "purify.min.js"], ["katex/dist/katex.min.js", "katex.min.js"]])
    fs.copyFileSync(require.resolve(src), path.join(SH, "lib", dst));
  const S = "/blog/_owner/_shared";
  const scripts = (up) => `<script src="${S}/site-shim.js"></script>
<script src="${up}data.js"></script>
<script src="${up}app.js"></script>
<script src="${up}widgets.js"></script>
<script src="${up}figs.js"></script>
<script src="${S}/lib/marked.min.js"></script>
<script src="${S}/lib/purify.min.js"></script>
<script src="${S}/lib/katex.min.js"></script>
<script src="${up}annotate.js"></script>`;
  const head = (t) => `<meta name="robots" content="noindex,nofollow">\n<title>${escA(t)} · AI4Read (owner)</title>`;
  fs.writeFileSync(path.join(OUT, "index.html"), blogPage({ body: html, lang: "en", owner: true, head: head(cfg.short), scripts: scripts("") }));
  if (has("src/content-zh.html")) {   // owner-only Chinese text (WRITING §8b)
    const zlog = []; const zh = renderMath(mapCites(rd("src/content-zh.html"), zlog));
    fs.mkdirSync(path.join(OUT, "zh"), { recursive: true });
    const zch = chapters.map((c) => ({ ...c, src: "../" + c.src }));   // audio lives one level up
    fs.writeFileSync(path.join(OUT, "zh", "data.js"), `window.POST=${JSON.stringify({ ...POST, audioBase: "../", defaultLang: "zh" })};window.CHAPTERS=${JSON.stringify(zch)};`);
    fs.writeFileSync(path.join(OUT, "zh", "index.html"), blogPage({ body: zh, lang: "zh-Hans", owner: true, head: head(cfg.title_zh || cfg.short), scripts: scripts("../").replace('src="../data.js"', 'src="data.js"') }));
    console.log(`zh page · cites ${zlog.length} (unmapped ${zlog.filter((r) => !r[2]).length})`);
  }
  fs.writeFileSync(path.join(OUT, "post.json"), JSON.stringify({ ...meta, url: `/blog/_owner/${SLUG}/`, zh: has("src/content-zh.html") }, null, 1));
  fs.writeFileSync(path.join(OUT, "context.json"), JSON.stringify({ slug: SLUG, brief }));
  console.log("owner build →", OUT);
}

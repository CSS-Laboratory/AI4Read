// Build the post page: KaTeX -> MathML (no fonts/CSS needed), code + brief + chapters inlined.
// Usage: node build.mjs   (NODE_PATH=/tmp/kt/node_modules)
import fs from "fs"; import path from "path"; import { createRequire } from "module";
const require = createRequire("/tmp/kt/");
const katex = require("katex");
const hljs = require("highlight.js/lib/core"); hljs.registerLanguage("python", require("highlight.js/lib/languages/python"));
const D = path.dirname(new URL(import.meta.url).pathname);
const rd = f => fs.readFileSync(path.join(D, f), "utf8");
let html = rd("src/content.html"); let errors = 0;
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

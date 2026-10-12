// stdin: JSON [{"tex": "...", "display": bool}], stdout: JSON [{"i": n, "error": "..."}]
const katex = require("katex");
let buf = "";
process.stdin.on("data", d => (buf += d));
process.stdin.on("end", () => {
  const items = JSON.parse(buf), errs = [];
  items.forEach((it, i) => {
    try { katex.renderToString(it.tex, { displayMode: it.display, throwOnError: true, strict: "ignore", trust: false }); }
    catch (e) { errs.push({ i, error: String(e.message || e).slice(0, 200) }); }
  });
  process.stdout.write(JSON.stringify(errs));
});

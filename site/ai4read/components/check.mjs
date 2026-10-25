#!/usr/bin/env node
/* Compute and validate widget configs WITHOUT a browser, using the same code as the page.
 * The writer uses this to produce every number it puts in the text.
 *   node site/ai4read/components/check.mjs <file.json|file.html> [--values '{"p":0.3}'] [--seeds A,B] [--id cfg-id] [--hist]
 * - a .json file holds one config (with "type") or an array of configs
 * - an .html file: every [data-widget] with data-config / data-config-ref is checked
 * Exit code 1 if any config fails to parse or evaluate. */
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const W = require("./widgets.js");

const args = process.argv.slice(2);
const file = args.find((a) => !a.startsWith("--") && !/^[{\[]/.test(a) && !args[args.indexOf(a) - 1]?.startsWith("--"));
const opt = (k) => { const i = args.indexOf("--" + k); return i >= 0 ? args[i + 1] ?? true : null; };
if (!file) { console.error("usage: check.mjs <file.json|file.html> [--values JSON] [--seeds A,B] [--id cfg-id] [--hist]"); process.exit(2); }

const unesc = (s) => s.replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&amp;/g, "&");
function fromHTML(html) {
  const refs = {};
  for (const m of html.matchAll(/<script type="application\/json" id="([^"]+)">([\s\S]*?)<\/script>/g)) refs[m[1]] = m[2];
  const out = [];
  for (const m of html.matchAll(/<div[^>]*data-widget="([\w-]+)"[^>]*>/g)) {
    const tag = m[0], type = m[1];
    if (type === "switch") continue;
    const id = (/\sid="([^"]+)"/.exec(tag) || [])[1];
    const ref = (/data-config-ref="([^"]+)"/.exec(tag) || [])[1];
    const inl = (/data-config='([^']*)'/.exec(tag) || [])[1];
    const src = ref ? refs[ref] : inl ? unesc(inl) : null;
    out.push({ name: id || ref || `${type}#${out.length + 1}`, type, src });
  }
  return out;
}
let items;
const text = readFileSync(file, "utf8");
if (file.endsWith(".html")) items = fromHTML(text);
else { const j = JSON.parse(text); items = (Array.isArray(j) ? j : [j]).map((c, i) => ({ name: c.id || `${c.type}#${i + 1}`, type: c.type, src: JSON.stringify(c) })); }
if (opt("id")) items = items.filter((it) => it.name === opt("id"));

let bad = 0;
const values = opt("values") ? JSON.parse(opt("values")) : null;
const seeds = opt("seeds") ? String(opt("seeds")).split(",") : null;
for (const it of items) {
  try {
    if (it.src == null) throw new Error("no config found (data-config or data-config-ref)");
    const cfg = JSON.parse(it.src); const type = cfg.type || it.type;
    // validate every expression string in the config
    const exprs = [];
    (function walk(o, path) { if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) walk(v, path + "." + k);
      else if (typeof o === "string" && /(\.(derived|update|init|pre)\.|\.(value|expr|x|y|w|capital|steps|t)$)/.test(path) && !/^(label|title|caption|note)/.test(path)) exprs.push([path, o]); })(cfg, "");
    exprs.forEach(([p, e]) => { try { W.parse(e); } catch (er) { throw new Error(`${p}: ${er.message}`); } });
    const fn = W.compute[type];
    console.log(`\n■ ${it.name} (${type})`);
    if (!fn) { console.log("  static widget: parsed OK"); continue; }
    const r = type === "cascade" ? fn(cfg, values, seeds) : fn(cfg, values);
    if (r.readout) console.log("  readout: " + r.readout.replace(/\n/g, "\n           "));
    if (r.bars && r.bars.length) console.log("  bars: " + r.bars.map((b) => `${b.label}=${W.fmt(b.value, ".4f")}`).join(", "));
    if (r.table) r.table.forEach((row) => console.log("  row: " + row.join(" | ")));
    if (type === "cascade") console.log("  failed by round: " + JSON.stringify(r.round));
    if (r.hist && opt("hist")) Object.entries(r.hist).forEach(([k, v]) => console.log(`  ${k}: ${v.map((x) => W.fmt(x, ".4g")).join(" ")}`));
    const env = Object.fromEntries(Object.entries(r.env).filter(([, v]) => typeof v === "number").map(([k, v]) => [k, +v.toPrecision(6)]));
    console.log("  values: " + JSON.stringify(env));
    if (/⟨/.test(r.readout || "")) throw new Error("readout template error: " + r.readout);
    for (const [k, v] of Object.entries(r.env)) if (typeof v === "number" && !isFinite(v)) console.log(`  ! warning: ${k} = ${v}`);
  } catch (e) { bad++; console.log(`\n✗ ${it.name}: ${e.message}`); }
}
console.log(`\n${items.length - bad}/${items.length} widget configs OK`);
process.exit(bad ? 1 : 0);

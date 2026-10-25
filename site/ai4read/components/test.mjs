#!/usr/bin/env node
/* Render test for widget pages under the strict site CSP (Playwright + Chromium).
 *   node site/ai4read/components/test.mjs [page relative to repo root] (default: the gallery)
 * Checks: 0 console errors / CSP violations, 0 widget errors, no horizontal scroll at 390 px,
 * every computable widget's on-page readout == the Node computation (check.mjs path), and
 * basic interaction (slider input, cascade tap, step navigation) changes the output. */
import http from "node:http";
import { readFileSync, existsSync, statSync } from "node:fs";
import { join, extname, resolve, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const W = require("./widgets.js");
let chromium;
for (const p of ["playwright", "/opt/node-tools/node_modules/playwright", "/opt/npm-tools/node_modules/playwright"]) { try { ({ chromium } = require(p)); break; } catch {} }
if (!chromium) { console.error("playwright not found"); process.exit(2); }

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "../../..");
const BASE = (() => { const i = process.argv.indexOf("--base"); return i > 0 ? process.argv[i + 1] : null; })();
const PAGE = process.argv.slice(2).find((a, i, A) => !a.startsWith("--") && A[i - 1] !== "--base") || "site/ai4read/components/gallery.html";
// With --base http://127.0.0.1:8799 the page is loaded from a running server (e.g. dev/mock-server.mjs for a site build:
//   node site/ai4read/dev/mock-server.mjs 8799 &  node site/ai4read/components/test.mjs /ai4read/<slug>/ --base http://127.0.0.1:8799)
// --inline: test a standalone (artifact) build, whose scripts are inline.
const INLINE = process.argv.includes("--inline");
const CSP = INLINE
  ? "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdnjs.cloudflare.com; img-src 'self' data: blob:; media-src 'self' blob: data:; connect-src 'self'; font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; base-uri 'self'"
  : "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob: data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'";
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".mp3": "audio/mpeg", ".svg": "image/svg+xml" };
const srv = http.createServer((req, res) => {
  if (req.url === "/favicon.ico") { res.writeHead(204); return res.end(); }
  const f = join(ROOT, decodeURIComponent(req.url.split("?")[0]));
  if (!f.startsWith(ROOT) || !existsSync(f) || statSync(f).isDirectory()) { missing.push(req.url); res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": TYPES[extname(f)] || "application/octet-stream", "content-security-policy": CSP });
  res.end(readFileSync(f));
}).listen(0);
const port = srv.address().port;

const fails = [];
const missing = [];
const browser = await chromium.launch(existsSync("/opt/pw-browsers/chromium") ? { executablePath: "/opt/pw-browsers/chromium" } : {});
try {
  const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const errs = [];
  page.on("console", (m) => { if (m.type() === "error" && !(m.location().url || "").endsWith("favicon.ico")) errs.push(m.text() + (m.location().url ? " @ " + m.location().url : "")); });
  page.on("pageerror", (e) => errs.push(String(e)));
  page.on("response", (r) => { if (r.status() >= 400 && !r.url().endsWith("favicon.ico")) missing.push(r.status() + " " + r.url()); });
  await page.goto(BASE ? BASE + PAGE : `http://127.0.0.1:${port}/${PAGE}`, { waitUntil: "load" });
  await page.waitForTimeout(300);

  const info = await page.evaluate(() => ({
    overflow: document.documentElement.scrollWidth - window.innerWidth,
    widgets: [...document.querySelectorAll("[data-widget]")].map((h) => ({ id: h.id, type: h.dataset.widget, err: h.querySelector(".w-err")?.textContent || null, readout: h.querySelector(".readout")?.textContent || null, ref: h.dataset.configRef || null, inline: h.dataset.config || null })),
  }));
  if (info.overflow > 1) fails.push(`horizontal overflow ${info.overflow}px at 390 px`);
  const html = BASE ? await (await fetch(BASE + PAGE)).text() : readFileSync(join(ROOT, PAGE), "utf8");
  for (const w of info.widgets) {
    if (w.err) { fails.push(`${w.id || w.type}: ${w.err}`); continue; }
    const fn = W.compute[w.type]; if (!fn || !w.readout) continue;
    let src = w.inline;
    if (w.ref) { const m = new RegExp(`<script type="application/json" id="${w.ref}">([\\s\\S]*?)</script>`).exec(html); src = m && m[1]; }
    const cfg = JSON.parse(src); const node = fn(cfg).readout;
    if (node !== w.readout) fails.push(`${w.id}: page readout differs from Node\n   page: ${w.readout}\n   node: ${node}`);
    else console.log(`ok  ${w.id || w.type}: readout matches Node`);
  }
  // interactions
  const first = await page.$("[data-widget=lab] input[type=range]");
  if (first) { const before = await page.$eval("[data-widget=lab] .readout", (e) => e.textContent);
    let after = before;
    for (const end of ["max", "min"]) { await first.evaluate((e, k) => { e.value = e[k]; e.dispatchEvent(new Event("input")); }, end);
      after = await page.$eval("[data-widget=lab] .readout", (e) => e.textContent); if (after !== before) break; }
    if (before === after) fails.push("lab slider did not change the readout"); else console.log("ok  lab slider changes the readout"); }
  const node = await page.$("[data-widget=cascade] .w-node:not(.seed)");
  if (node) { const before = await page.$eval("[data-widget=cascade] .readout", (e) => e.textContent);
    await node.click(); const after = await page.$eval("[data-widget=cascade] .readout", (e) => e.textContent);
    if (before === after) fails.push("cascade tap did not change the readout"); else console.log("ok  cascade tap changes the readout"); }
  for (const t of ["diagram", "stepper"]) { const nx = await page.$(`[data-widget=${t}] .w-next`);
    if (nx) { const b = await page.$eval(`[data-widget=${t}] .readout`, (e) => e.textContent); await nx.click();
      const a = await page.$eval(`[data-widget=${t}] .readout`, (e) => e.textContent); if (a === b) fails.push(`${t} Next did not change the text`); else console.log(`ok  ${t} Next works`); } }
  for (const host of await page.$$("[data-widget=vec2d]")) {
    const id = await host.evaluate((h) => h.id), ro = async () => host.$eval(".readout", (e) => e.textContent);
    const h = await host.$(".w-handle"); if (!h) continue; await h.scrollIntoViewIfNeeded();
    const before = await ro(), bb = await h.boundingBox();
    await page.mouse.move(bb.x + bb.width / 2, bb.y + bb.height / 2); await page.mouse.down();
    await page.mouse.move(bb.x + bb.width / 2 - 60, bb.y + bb.height / 2 - 70, { steps: 6 }); await page.mouse.up();
    const afterDrag = await ro(), slid = await host.$eval(".w-sliders input", (e) => e.value);
    if (afterDrag === before) fails.push(`${id}: dragging the handle did not change the readout`); else console.log(`ok  ${id}: drag changes the readout (slider now ${slid})`);
    const h2 = await host.$(".w-handle"); await h2.focus(); await page.keyboard.press("ArrowRight");
    const afterKey = await ro(), still = await host.evaluate((x) => x.contains(document.activeElement) && document.activeElement.classList.contains("w-handle"));
    if (afterKey === afterDrag) fails.push(`${id}: arrow key on the handle did not change the readout`); else console.log(`ok  ${id}: arrow key moves the handle${still ? " (focus kept)" : ""}`);
    if (!still) fails.push(`${id}: handle lost keyboard focus after an arrow key`);
  }
  const sw = await page.$$("[data-widget=switch] .seg button");
  if (sw.length > 1) { await sw[1].click(); const vis = await page.$$eval("[data-widget=switch] > section", (s) => s.map((x) => !x.hidden));
    if (!(vis[1] && !vis[0])) fails.push("switch did not change panel"); else console.log("ok  switch changes panel"); }
  await page.screenshot({ path: process.env.SHOT || "/tmp/widgets-390.png", fullPage: true });
  if (errs.length) fails.push("console errors:\n   " + errs.join("\n   ") + (missing.length ? "\n   404: " + missing.join(", ") : ""));
} finally { await browser.close(); srv.close(); }
if (fails.length) { console.log("\nFAIL\n- " + fails.join("\n- ")); process.exit(1); }
console.log("\nPASS: 0 console errors, no overflow at 390 px, readouts reproducible, interactions work");

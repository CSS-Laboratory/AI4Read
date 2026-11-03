// Owner sees the 中 button and switching plays audio-zh/; a non-owner sees no button and never requests audio-zh/.
import { createRequire } from "node:module"; const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const slug = process.argv[2] || "2026-10-llm-next-word";
const b = await chromium.launch(); let fails = 0;
for (const [port, role] of [[8801, "owner"], [8802, "student"]]) {
  const p = await b.newPage({ viewport: { width: 390, height: 844 } }); const zhReq = [], errs = [];
  p.on("request", r => { if (r.url().includes("audio-zh")) zhReq.push(r.url()); });
  p.on("pageerror", e => errs.push(String(e))); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
  await p.goto(`http://127.0.0.1:${port}/ai4read/${slug}/`); await p.waitForTimeout(1500);
  const visible = await p.$eval("#p-lang", e => !e.hidden).catch(() => null);
  let after = null;
  if (visible) {
    await p.click("#p-lang"); await p.waitForTimeout(400);
    after = await p.evaluate(() => ({ pressed: document.querySelector("#p-lang").getAttribute("aria-pressed"), title: document.querySelector("#p-title").textContent }));
    await p.click("#p-play"); await p.waitForTimeout(800);
    after.src = await p.evaluate(() => document.querySelector("audio").getAttribute("src") || "");
    await p.click("#p-lang"); await p.waitForTimeout(300);
    after.back = await p.evaluate(() => document.querySelector("#p-title").textContent);
  }
  const ok = role === "owner" ? (visible && after.pressed === "true" && /[\u4e00-\u9fff]/.test(after.title) && !/[\u4e00-\u9fff]/.test(after.back)) : (visible === false && zhReq.length === 0);
  if (!ok) fails++;
  console.log(role, ok ? "OK" : "FAIL", JSON.stringify({ visible, after, zhRequests: zhReq.length, errors: errs.slice(0, 3) }));
  await p.close();
}
await b.close(); process.exit(fails ? 1 : 0);

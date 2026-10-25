/* AI4Read component library v1 — config-driven widgets for posts.
 * The writer agent composes widgets with JSON configs; it never writes JavaScript.
 * Usage in a post:  <div class="w" data-widget="lab" data-config='{...}'></div>
 *   or              <div class="w" data-widget="lab" data-config-ref="cfg-id"></div>
 *                   <script type="application/json" id="cfg-id">{...}</script>
 * Strict-CSP safe: no eval / new Function. Formulas use a small safe expression language (see README).
 * The pure functions (expr, compute*) also run in Node (check.mjs), so every number in the text
 * can be produced by the same code that drives the widget.
 */
(function (root) {
  "use strict";

  /* ================= expression language ================= */
  const FUN = {
    exp: Math.exp, ln: Math.log, log: Math.log, log2: Math.log2, log10: Math.log10, sqrt: Math.sqrt,
    abs: Math.abs, min: Math.min, max: Math.max, pow: Math.pow, floor: Math.floor, ceil: Math.ceil,
    round: Math.round, sign: Math.sign, sin: Math.sin, cos: Math.cos, tanh: Math.tanh,
    clamp: (x, a, b) => Math.min(b, Math.max(a, x)),
    sigmoid: (x) => 1 / (1 + Math.exp(-x)),
    fact: (n) => { let r = 1; for (let i = 2; i <= Math.round(n); i++) r *= i; return r; },
    comb: (n, k) => { let r = 1; for (let i = 1; i <= Math.round(k); i++) r = r * (n - k + i) / i; return r; },
  };
  const CONST = { pi: Math.PI, e: Math.E };

  function tokenize(s) {
    const out = []; let i = 0;
    while (i < s.length) {
      const c = s[i];
      if (/\s/.test(c)) { i++; continue; }
      const num = /^(\d+\.?\d*|\.\d+)(e[+-]?\d+)?/i.exec(s.slice(i));
      if (num) { out.push({ t: "n", v: parseFloat(num[0]) }); i += num[0].length; continue; }
      const id = /^[A-Za-z_][A-Za-z0-9_]*/.exec(s.slice(i));
      if (id) { out.push({ t: "id", v: id[0] }); i += id[0].length; continue; }
      const op = /^(<=|>=|==|!=|&&|\|\||[-+*/^(),<>?:!%])/.exec(s.slice(i));
      if (op) { out.push({ t: "op", v: op[0] }); i += op[0].length; continue; }
      throw new Error(`bad character '${c}' in expression: ${s}`);
    }
    return out;
  }
  const BP = { "?": 1, "||": 2, "&&": 3, "==": 4, "!=": 4, "<": 5, ">": 5, "<=": 5, ">=": 5, "+": 6, "-": 6, "*": 7, "/": 7, "%": 7, "^": 9 };
  function parse(src) {
    const tk = tokenize(String(src)); let p = 0;
    const peek = () => tk[p], next = () => tk[p++];
    const expect = (v) => { const t = next(); if (!t || t.v !== v) throw new Error(`expected '${v}' in: ${src}`); };
    function nud() {
      const t = next(); if (!t) throw new Error(`unexpected end: ${src}`);
      if (t.t === "n") return { k: "n", v: t.v };
      if (t.t === "id") {
        if (peek() && peek().v === "(") {
          next(); const args = [];
          if (peek() && peek().v !== ")") { do { args.push(expr(0)); } while (peek() && peek().v === "," && next()); }
          expect(")");
          if (t.v === "if") { if (args.length !== 3) throw new Error("if(c,a,b) needs 3 args"); return { k: "?", c: args[0], a: args[1], b: args[2] }; }
          if (!FUN[t.v]) throw new Error(`unknown function ${t.v}`);
          return { k: "f", f: t.v, a: args };
        }
        return { k: "v", v: t.v };
      }
      if (t.v === "(") { const e = expr(0); expect(")"); return e; }
      if (t.v === "-") return { k: "neg", a: expr(8) };
      if (t.v === "+") return expr(8);
      if (t.v === "!") return { k: "not", a: expr(8) };
      throw new Error(`unexpected '${t.v}' in: ${src}`);
    }
    function expr(rbp) {
      let left = nud();
      for (;;) {
        const t = peek(); if (!t || t.t !== "op" || !(t.v in BP)) break;
        const bp = BP[t.v]; if (bp <= rbp) break; next();
        if (t.v === "?") { const a = expr(0); expect(":"); const b = expr(0); left = { k: "?", c: left, a, b }; continue; }
        const right = expr(t.v === "^" ? bp - 1 : bp); // ^ is right-associative
        left = { k: "b", o: t.v, l: left, r: right };
      }
      return left;
    }
    const ast = expr(0); if (p < tk.length) throw new Error(`unexpected '${tk[p].v}' in: ${src}`);
    return ast;
  }
  function ev(n, env) {
    switch (n.k) {
      case "n": return n.v;
      case "v": if (n.v in env) return env[n.v]; if (n.v in CONST) return CONST[n.v]; throw new Error(`unknown variable ${n.v}`);
      case "neg": return -ev(n.a, env);
      case "not": return ev(n.a, env) ? 0 : 1;
      case "f": return FUN[n.f](...n.a.map((a) => ev(a, env)));
      case "?": return ev(n.c, env) ? ev(n.a, env) : ev(n.b, env);
      case "b": { const l = ev(n.l, env), r = ev(n.r, env);
        switch (n.o) { case "+": return l + r; case "-": return l - r; case "*": return l * r; case "/": return l / r; case "%": return l % r;
          case "^": return Math.pow(l, r); case "<": return +(l < r); case ">": return +(l > r); case "<=": return +(l <= r); case ">=": return +(l >= r);
          case "==": return +(l === r); case "!=": return +(l !== r); case "&&": return +(l && r); case "||": return +(l || r); } }
    }
    throw new Error("bad node");
  }
  const cache = new Map();
  function evalExpr(src, env) {
    if (typeof src === "number") return src;
    let a = cache.get(src); if (!a) { a = parse(src); cache.set(src, a); }
    return ev(a, env || {});
  }

  /* ================= formatting and templates ================= */
  function fmt(x, f) {
    if (typeof x !== "number" || !isFinite(x)) return String(x);
    f = f || "";
    let m;
    if ((m = /^(,)?\.(\d+)f$/.exec(f))) return m[1] ? x.toLocaleString("en-US", { minimumFractionDigits: +m[2], maximumFractionDigits: +m[2] }) : x.toFixed(+m[2]);
    if ((m = /^\.(\d+)%$/.exec(f))) return (x * 100).toFixed(+m[1]) + "%";
    if ((m = /^\.(\d+)e$/.exec(f))) return x.toExponential(+m[1]);
    if (f === ",") return Math.round(x).toLocaleString("en-US");
    if (f === "d") return String(Math.round(x));
    if ((m = /^\.(\d+)g$/.exec(f))) return String(+x.toPrecision(+m[1]));
    return String(+x.toPrecision(6));
  }
  /* "{expr}" or "{expr:fmt}" — fmt is the part after the LAST ':' if it looks like a format */
  function fill(tpl, env) {
    return String(tpl).replace(/\{([^{}]+)\}/g, (_, body) => {
      const m = /^(.*):((?:,)?\.\d+[f%eg]|,|d)$/.exec(body);
      const src = m ? m[1] : body, f = m ? m[2] : "";
      try { return fmt(evalExpr(src.trim(), env), f); } catch (e) { return `⟨${e.message}⟩`; }
    });
  }

  /* ================= pure compute functions (also used by check.mjs) ================= */
  function paramEnv(cfg, values) {
    const env = {};
    (cfg.params || []).forEach((p) => { env[p.id] = values && p.id in values ? +values[p.id] : +p.value; });
    Object.assign(env, cfg.constants || {});
    return env;
  }
  function derive(cfg, env) {
    for (const [k, src] of Object.entries(cfg.derived || {})) env[k] = evalExpr(src, env);
    return env;
  }
  function computeLab(cfg, values) {
    const env = derive(cfg, paramEnv(cfg, values));
    const bars = (cfg.bars && cfg.bars.items || []).map((b) => ({ label: fill(b.label, env), value: evalExpr(b.value, env) }));
    const table = cfg.table ? cfg.table.rows.map((r) => r.map((c) => (typeof c === "string" && c.startsWith("=") ? fmt(evalExpr(c.slice(1), env), cfg.table.fmt) : fill(String(c), env)))) : null;
    return { env, bars, table, readout: cfg.readout ? fill(cfg.readout, env) : "" };
  }
  function computePlot(cfg, values) {
    const env = derive(cfg, paramEnv(cfg, values));
    const X = cfg.x, n = cfg.samples || 120;
    const xs = [...Array(n + 1)].map((_, i) => X.log ? Math.pow(10, Math.log10(X.min) + (Math.log10(X.max) - Math.log10(X.min)) * i / n) : X.min + (X.max - X.min) * i / n);
    const curves = (cfg.curves || []).map((c) => ({ label: c.label || "", cls: c.style || "", pts: xs.map((x) => [x, evalExpr(c.expr, { ...env, x })]) }));
    const points = (cfg.points || []).map((pt) => ({ label: fill(pt.label || "", env), x: evalExpr(pt.x, env), y: evalExpr(pt.y, env) }));
    return { env, curves, points, readout: cfg.readout ? fill(cfg.readout, env) : "" };
  }
  function computeIterate(cfg, values) {
    const env0 = derive(cfg, paramEnv(cfg, values));
    const steps = Math.round(evalExpr(cfg.steps, env0));
    let s = {}; for (const [k, v] of Object.entries(cfg.init)) s[k] = evalExpr(v, env0);
    const hist = { t: [0] }; Object.keys(s).forEach((k) => (hist[k] = [s[k]]));
    const shocks = cfg.shocks || [];
    for (let t = 1; t <= steps; t++) {
      const env = { ...env0, ...s, t };
      const ns = {}; for (const [k, src] of Object.entries(cfg.update)) ns[k] = evalExpr(src, env);
      s = { ...s, ...ns };
      shocks.filter((sh) => evalExpr(sh.t, env0) === t).forEach((sh) => { for (const [k, src] of Object.entries(sh.set)) s[k] = evalExpr(src, { ...env0, ...s, t }); });
      hist.t.push(t); Object.keys(s).forEach((k) => { (hist[k] = hist[k] || []).push(s[k]); });
    }
    const env = { ...env0, ...s, t: steps };
    Object.keys(s).forEach((k) => { env["max_" + k] = Math.max(...hist[k]); env["min_" + k] = Math.min(...hist[k]); env["first_" + k] = hist[k][0]; });
    return { env, hist, readout: cfg.readout ? fill(cfg.readout, env) : "" };
  }
  /* Threshold cascade on an exposure network (toy, ours).
   * edge {from:A, to:B, w}: B is exposed to A — if A fails, B loses lgd*w.
   * A node fails when its accumulated loss >= its capital * capMult. Rounds are synchronous. */
  function computeCascade(cfg, values, seeds) {
    const env = derive(cfg, paramEnv(cfg, values));
    const lgd = "lgd" in env ? env.lgd : 1, capMult = "capMult" in env ? env.capMult : 1;
    const nodes = cfg.nodes.map((n) => n.id), cap = {}, loss = {}, round = {};
    cfg.nodes.forEach((n) => { cap[n.id] = evalExpr(n.capital, env) * capMult; loss[n.id] = 0; });
    let frontier = (seeds || cfg.seeds || []).slice(); frontier.forEach((id) => (round[id] = 0));
    let r = 0;
    while (frontier.length) {
      r++; const next = [];
      for (const f of frontier) for (const e of cfg.edges) if (e.from === f && !(e.to in round)) loss[e.to] += lgd * evalExpr(e.w, env);
      for (const id of nodes) if (!(id in round) && loss[id] >= cap[id] - 1e-12) { round[id] = r; next.push(id); }
      frontier = next;
    }
    const failed = Object.keys(round).length;
    const out = { ...env, failed, survivors: nodes.length - failed, rounds: Math.max(0, ...Object.values(round)), total: nodes.length };
    return { env: out, round, loss, cap, readout: cfg.readout ? fill(cfg.readout, out) : "" };
  }
  /* vec2d: vectors in the plane, a probe direction u, an optional shift (steering) of every point.
   * Env after compute: params, constants, `pre` (evaluated first), then for point i (1-based):
   * x_i, y_i (after the shift), s_i = u·(x_i, y_i); ux, uy (unit), vx, vy (shift), uv = u·v; then `derived`. */
  function computeVec2d(cfg, values) {
    const env = paramEnv(cfg, values);
    for (const [k, src] of Object.entries(cfg.pre || {})) env[k] = evalExpr(src, env);
    let ux = 1, uy = 0;
    if (cfg.probe) { ux = evalExpr(cfg.probe.x, env); uy = evalExpr(cfg.probe.y, env); const n = Math.hypot(ux, uy) || 1; if (cfg.probe.normalize !== false) { ux /= n; uy /= n; } }
    const vx = cfg.shift ? evalExpr(cfg.shift.x, env) : 0, vy = cfg.shift ? evalExpr(cfg.shift.y, env) : 0;
    Object.assign(env, { ux, uy, vx, vy, uv: ux * vx + uy * vy });
    const points = (cfg.points || []).map((pt, i) => {
      const x0 = evalExpr(pt.x, env), y0 = evalExpr(pt.y, env), sh = pt.fixed ? 0 : 1;
      const x = x0 + sh * vx, y = y0 + sh * vy, s = ux * x + uy * y;
      env["x" + (i + 1)] = x; env["y" + (i + 1)] = y; env["s" + (i + 1)] = s;
      return { x0, y0, x, y, s, label: fill(pt.label || "", env), group: pt.group || 0 };
    });
    env.n = points.length;
    for (const [k, src] of Object.entries(cfg.derived || {})) env[k] = evalExpr(src, env);
    const vectors = (cfg.vectors || []).map((v) => ({ x: evalExpr(v.x, env), y: evalExpr(v.y, env), fx: v.from ? evalExpr(v.from.x, env) : 0, fy: v.from ? evalExpr(v.from.y, env) : 0,
      label: fill(v.label || "", env), cls: v.cls || "c3", drag: v.drag || null, scale: v.scale || 1 }));
    return { env, points, vectors, readout: cfg.readout ? fill(cfg.readout, env) : "" };
  }
  const COMPUTE = { lab: computeLab, plot: computePlot, iterate: computeIterate, cascade: computeCascade, vec2d: computeVec2d };

  const API = { parse, evalExpr, fmt, fill, compute: COMPUTE, version: "1.0" };
  if (typeof module !== "undefined" && module.exports) { module.exports = API; return; }
  root.AI4W = API;

  /* ================= DOM rendering ================= */
  const doc = root.document;
  const esc = (t) => String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  const el = (tag, cls, html) => { const e = doc.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  let uid = 0;

  function frame(host, cfg) {
    host.classList.add("lab", "w-" + (cfg.type || host.dataset.widget));
    host.innerHTML = "";
    if (cfg.title) host.append(el("p", "lab-title", esc(cfg.title)));
    if (cfg.note) host.append(el("p", "lab-note", esc(cfg.note)));
  }
  function sliders(host, cfg, onChange) {
    const vals = {}; if (!cfg.params || !cfg.params.length) return vals;
    const wrap = el("div", "w-sliders");
    cfg.params.forEach((p) => {
      vals[p.id] = +p.value;
      const id = "w" + ++uid, row = el("div", "sl");
      row.innerHTML = `<label for="${id}">${esc(p.label || p.id)}</label><input type="range" id="${id}" min="${p.min}" max="${p.max}" step="${p.step || (p.max - p.min) / 100}" value="${p.value}"><output for="${id}"></output>`;
      const inp = row.querySelector("input"), out = row.querySelector("output");
      const show = () => { out.textContent = p.display ? fill(p.display, { [p.id]: +inp.value }) : fmt(+inp.value, p.fmt || ".2g"); };
      inp.addEventListener("input", () => { vals[p.id] = +inp.value; show(); onChange(); });
      show(); wrap.append(row);
    });
    host.append(wrap); return vals;
  }
  function presets(host, cfg, vals, apply) {
    if (!cfg.presets) return;
    const seg = el("div", "seg");
    cfg.presets.forEach((pr, i) => {
      const b = el("button", "", esc(pr.label)); b.type = "button"; b.setAttribute("aria-pressed", "false");
      b.addEventListener("click", () => {
        Object.entries(pr.values).forEach(([k, v]) => { vals[k] = v; const p = cfg.params.findIndex((q) => q.id === k); const inp = host.querySelectorAll(".w-sliders input")[p]; if (inp) { inp.value = v; inp.dispatchEvent(new Event("input")); } });
        seg.querySelectorAll("button").forEach((x) => x.setAttribute("aria-pressed", String(x === b))); apply();
      });
      seg.append(b);
    });
    host.append(seg);
  }
  function readout(host) { const r = el("p", "readout"); r.style.whiteSpace = "pre-line"; r.setAttribute("aria-live", "polite"); host.append(r); return r; }
  function caption(host, cfg) { if (cfg.caption) host.append(el("p", "lab-note w-cap", esc(cfg.caption))); }

  function barsHTML(items, cfg) {
    const mx = cfg.max != null ? cfg.max : Math.max(1e-12, ...items.map((b) => Math.abs(b.value)));
    return items.map((b, i) => `<div class="w-bar${cfg.highlight === i ? " hi" : ""}"><span class="w-bl">${esc(b.label)}</span><i style="width:${Math.max(0, Math.min(100, (b.value / mx) * 100))}%"></i><span class="w-bv">${fmt(b.value, cfg.fmt || ".2f")}</span></div>`).join("");
  }

  /* ---- lab: sliders + derived values + readout (+ bars, + table) ---- */
  function renderLab(host, cfg) {
    frame(host, cfg);
    let bars, table, ro;
    const upd = () => {
      const r = computeLab(cfg, vals);
      if (bars) bars.innerHTML = barsHTML(r.bars, cfg.bars);
      if (table) table.querySelector("tbody").innerHTML = r.table.map((row) => `<tr>${row.map((c) => `<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      if (ro) ro.textContent = r.readout;
    };
    const vals = sliders(host, cfg, upd);
    presets(host, cfg, vals, upd);
    if (cfg.bars) { bars = el("div", "w-bars"); host.append(bars); }
    if (cfg.table) { table = el("div", "w-table", `<table><thead><tr>${cfg.table.head.map((h) => `<th>${esc(h)}</th>`).join("")}</tr></thead><tbody></tbody></table>`); host.append(table); }
    if (cfg.readout) ro = readout(host);
    caption(host, cfg); upd();
  }

  /* ---- shared SVG axes ---- */
  function axes(cfg, W, H) {
    const X0 = 44, Y0 = H - 28, X1 = W - 18, Y1 = 14, X = cfg.x, Y = cfg.y;
    const sx = (v) => X.log ? X0 + (Math.log10(v) - Math.log10(X.min)) / (Math.log10(X.max) - Math.log10(X.min)) * (X1 - X0) : X0 + (v - X.min) / (X.max - X.min) * (X1 - X0);
    const sy = (v) => { const c = Y.log ? (Math.log10(Math.max(v, 1e-300)) - Math.log10(Y.min)) / (Math.log10(Y.max) - Math.log10(Y.min)) : (v - Y.min) / (Y.max - Y.min); return Y0 - Math.max(-0.05, Math.min(1.05, c)) * (Y0 - Y1); };
    const ticks = (A) => A.ticks || (A.log ? [...Array(Math.floor(Math.log10(A.max)) - Math.ceil(Math.log10(A.min)) + 1)].map((_, i) => Math.pow(10, Math.ceil(Math.log10(A.min)) + i)) : [0, 0.25, 0.5, 0.75, 1].map((f) => A.min + f * (A.max - A.min)));
    let b = `<line x1="${X0}" y1="${Y0}" x2="${X1}" y2="${Y0}" class="ax"/><line x1="${X0}" y1="${Y0}" x2="${X0}" y2="${Y1}" class="ax"/>`;
    ticks(X).forEach((v) => { b += `<line x1="${sx(v)}" y1="${Y0}" x2="${sx(v)}" y2="${Y0 + 4}" class="ax"/><text x="${sx(v)}" y="${Y0 + 15}" text-anchor="middle" class="ts">${esc(fmt(v, X.tickFmt || ".3g"))}</text>`; });
    ticks(Y).forEach((v) => { b += `<line x1="${X0}" y1="${sy(v)}" x2="${X1}" y2="${sy(v)}" class="grid"/><text x="${X0 - 5}" y="${sy(v) + 4}" text-anchor="end" class="ts">${esc(fmt(v, Y.tickFmt || ".3g"))}</text>`; });
    if (X.label) b += `<text x="${X1}" y="${H - 2}" text-anchor="end" class="ts">${esc(X.label)}</text>`;
    if (Y.label) b += `<text x="${X0 + 4}" y="${Y1 - 2}" text-anchor="start" class="ts">${esc(Y.label)}</text>`;
    return { b, sx, sy };
  }
  const CLS = ["c0", "c1", "c2", "c3", "c4"];
  function legend(items) { return items.length > 1 ? `<div class="w-legend">${items.map((l, i) => `<span><i class="${CLS[i % 5]}"></i>${esc(l)}</span>`).join("")}</div>` : ""; }

  /* ---- plot: curves y = f(x; params) + marked points ---- */
  function renderPlot(host, cfg) {
    frame(host, cfg); const W = 360, H = cfg.height || 200;
    const fig = el("div", "w-fig"); let ro;
    const upd = () => {
      const r = computePlot(cfg, vals), A = axes(cfg, W, H); let b = A.b;
      r.curves.forEach((c, i) => { b += `<polyline class="w-line ${CLS[i % 5]}" points="${c.pts.filter((p) => isFinite(p[1])).map((p) => `${A.sx(p[0]).toFixed(1)},${A.sy(p[1]).toFixed(1)}`).join(" ")}"/>`; });
      r.points.forEach((p) => { b += `<circle cx="${A.sx(p.x)}" cy="${A.sy(p.y)}" r="5" class="w-pt"/>` + (p.label ? `<text x="${A.sx(p.x) + 8}" y="${A.sy(p.y) - 8}" class="tn">${esc(p.label)}</text>` : ""); });
      fig.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="fig" role="img" aria-label="${esc(cfg.title || "plot")}">${b}</svg>` + legend(r.curves.map((c) => c.label).filter(Boolean));
      if (ro) ro.textContent = r.readout;
    };
    const vals = sliders(host, cfg, upd); presets(host, cfg, vals, upd);
    host.append(fig); if (cfg.readout) ro = readout(host); caption(host, cfg); upd();
  }

  /* ---- iterate: a discrete-time dynamical system, plotted over t ---- */
  function renderIterate(host, cfg) {
    frame(host, cfg); const W = 360, H = cfg.height || 200;
    const fig = el("div", "w-fig"); let ro;
    const upd = () => {
      const r = computeIterate(cfg, vals);
      const ycfg = { ...(cfg.y || {}) };
      if (ycfg.min == null || ycfg.max == null) { const all = cfg.series.flatMap((s) => r.hist[s.var]); ycfg.min = ycfg.min ?? Math.min(0, ...all); ycfg.max = ycfg.max ?? (Math.max(...all) * 1.05 || 1); }
      const A = axes({ x: { min: 0, max: r.hist.t.length - 1, label: (cfg.x && cfg.x.label) || "t", tickFmt: "d" }, y: ycfg }, W, H); let b = A.b;
      cfg.series.forEach((s, i) => { b += `<polyline class="w-line ${CLS[i % 5]}" points="${r.hist[s.var].map((v, t) => `${A.sx(t).toFixed(1)},${A.sy(v).toFixed(1)}`).join(" ")}"/>`; });
      (cfg.shocks || []).forEach((sh) => { const t = evalExpr(sh.t, r.env); b += `<line x1="${A.sx(t)}" y1="14" x2="${A.sx(t)}" y2="${H - 28}" class="w-shock"/>` + (sh.label ? `<text x="${A.sx(t) + 4}" y="26" class="tn">${esc(sh.label)}</text>` : ""); });
      fig.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="fig" role="img" aria-label="${esc(cfg.title || "time series")}">${b}</svg>` + legend(cfg.series.map((s) => s.label || s.var));
      if (ro) ro.textContent = r.readout;
    };
    const vals = sliders(host, cfg, upd); presets(host, cfg, vals, upd);
    host.append(fig); if (cfg.readout) ro = readout(host); caption(host, cfg); upd();
  }

  /* ---- cascade: tap a node to make it fail; watch losses spread ---- */
  function renderCascade(host, cfg) {
    frame(host, cfg); const W = 360, H = cfg.height || 240;
    const fig = el("div", "w-fig"); let ro, seeds = (cfg.seeds || []).slice();
    const pos = Object.fromEntries(cfg.nodes.map((n) => [n.id, n]));
    const upd = () => {
      const r = computeCascade(cfg, vals, seeds);
      let b = `<defs><marker id="wah${host.dataset.wid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ahd"/></marker></defs>`;
      cfg.edges.forEach((e) => { const a = pos[e.from], c = pos[e.to], dx = c.x - a.x, dy = c.y - a.y, d = Math.hypot(dx, dy) || 1, k = 20 / d;
        const w = evalExpr(e.w, r.env), hot = e.from in r.round;
        b += `<line x1="${a.x + dx * k}" y1="${a.y + dy * k}" x2="${c.x - dx * k}" y2="${c.y - dy * k}" class="w-edge${hot ? " hot" : ""}" stroke-width="${1 + Math.min(4, w)}" marker-end="url(#wah${host.dataset.wid})"/>`; });
      cfg.nodes.forEach((n) => { const f = n.id in r.round, sd = seeds.includes(n.id);
        b += `<g class="w-node${f ? " failed" : ""}${sd ? " seed" : ""}" data-id="${esc(n.id)}" tabindex="0" role="button" aria-label="${esc(n.label || n.id)}${f ? ", failed in round " + r.round[n.id] : ""}"><circle cx="${n.x}" cy="${n.y}" r="18"/><text x="${n.x}" y="${n.y + 4}" text-anchor="middle" class="t">${esc(n.label || n.id)}</text>`;
        b += `<text x="${n.x}" y="${n.y + 32}" text-anchor="middle" class="ts">${f ? (r.round[n.id] === 0 ? "shock" : "round " + r.round[n.id]) : `${fmt(r.loss[n.id], ".1f")}/${fmt(r.cap[n.id], ".1f")}`}</text></g>`; });
      fig.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="fig" role="img" aria-label="${esc(cfg.title || "network")}">${b}</svg>`;
      fig.querySelectorAll(".w-node").forEach((g) => { const tog = () => { const id = g.dataset.id; seeds = seeds.includes(id) ? seeds.filter((s) => s !== id) : [...seeds, id]; upd(); };
        g.addEventListener("click", tog); g.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); tog(); } }); });
      if (ro) ro.textContent = r.readout;
    };
    host.dataset.wid = ++uid;
    const vals = sliders(host, cfg, upd); presets(host, cfg, vals, upd);
    host.append(fig); if (cfg.readout) ro = readout(host); caption(host, cfg); upd();
  }

  /* ---- diagram: boxes and arrows; optional steps highlight parts in order ---- */
  function renderDiagram(host, cfg) {
    frame(host, cfg); const W = cfg.width || 360, H = cfg.height || 220;
    const fig = el("div", "w-fig"); const pos = Object.fromEntries(cfg.nodes.map((n) => [n.id, n]));
    let step = 0; const steps = cfg.steps || null; let ro;
    const edgePt = (n, tx, ty) => { const w = (n.w || 90) / 2, h = (n.h || 34) / 2, dx = tx - n.x, dy = ty - n.y; const s = Math.min(w / Math.abs(dx || 1e-9), h / Math.abs(dy || 1e-9)); return [n.x + dx * Math.min(1, s), n.y + dy * Math.min(1, s)]; };
    const draw = () => {
      const on = steps ? new Set(steps.slice(0, step + 1).flatMap((s) => s.show || [])) : null;
      const vis0 = (id) => !on || on.has(id) || !(steps.some((s) => (s.show || []).includes(id)));
      // preview: items of later steps are drawn faded instead of hidden, so the frame is never mostly blank
      const vis = (id) => vis0(id) || !!cfg.preview;
      const fade = (id) => (cfg.preview && !vis0(id) ? ' opacity="0.22"' : "");
      let b = `<defs><marker id="dah${host.dataset.wid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ahd"/></marker></defs>`;
      (cfg.edges || []).forEach((e, i) => { const id = e.id || `e${i}`; if (!vis(id)) return; const a = pos[e.from], c = pos[e.to]; const [x1, y1] = edgePt(a, c.x, c.y), [x2, y2] = edgePt(c, a.x, a.y);
        b += `<g${fade(id)}><line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="ar${e.dashed ? " dash" : ""}" marker-end="url(#dah${host.dataset.wid})"/>`;
        if (e.label) b += `<text x="${(x1 + x2) / 2 + (e.dx || 0)}" y="${(y1 + y2) / 2 - 4 + (e.dy || 0)}" text-anchor="middle" class="ts">${esc(e.label)}</text>`;
        b += `</g>`; });
      cfg.nodes.forEach((n) => { if (!vis(n.id)) return; const w = n.w || 90, h = n.h || 34, lines = String(n.label).split("\n");
        b += `<g${fade(n.id)}><rect x="${n.x - w / 2}" y="${n.y - h / 2}" width="${w}" height="${h}" rx="${n.round ? h / 2 : 5}" class="${n.kind || "bx"}"/>`;
        lines.forEach((l, i) => { b += `<text x="${n.x}" y="${n.y + 4 + (i - (lines.length - 1) / 2) * 13}" text-anchor="middle" class="t"${n.size ? ` font-size="${n.size}"` : ""}>${esc(l)}</text>`; });
        b += `</g>`; });
      (cfg.labels || []).forEach((l) => { b += `<text x="${l.x}" y="${l.y}" text-anchor="${l.a || "middle"}" class="${l.c || "ts"}">${esc(l.text)}</text>`; });
      fig.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="fig" role="img" aria-label="${esc(cfg.title || "diagram")}">${b}</svg>`;
      if (ro) ro.textContent = steps[step].text || "";
      if (nav) { nav.querySelector(".w-prev").disabled = step === 0; nav.querySelector(".w-next").disabled = step === steps.length - 1; nav.querySelector(".w-pos").textContent = `${step + 1} / ${steps.length}`; }
    };
    host.dataset.wid = ++uid; host.append(fig);
    let nav = null;
    if (steps) { nav = el("div", "w-nav", `<button type="button" class="w-prev">Back</button><span class="w-pos"></span><button type="button" class="w-next">Next</button>`);
      nav.querySelector(".w-prev").addEventListener("click", () => { step = Math.max(0, step - 1); draw(); });
      nav.querySelector(".w-next").addEventListener("click", () => { step = Math.min(steps.length - 1, step + 1); draw(); });
      host.append(nav); ro = readout(host); }
    caption(host, cfg); draw();
  }

  /* ---- stepper: walk through the rows of a worked table ---- */
  function renderStepper(host, cfg) {
    frame(host, cfg); let i = 0;
    const tbl = el("div", "w-table", `<table><thead><tr>${cfg.head.map((h) => `<th>${esc(h)}</th>`).join("")}</tr></thead><tbody>${cfg.rows.map((r) => `<tr>${r.map((c) => `<td>${esc(c)}</td>`).join("")}</tr>`).join("")}</tbody></table>`);
    const nav = el("div", "w-nav", `<button type="button" class="w-prev">Back</button><span class="w-pos"></span><button type="button" class="w-next">Next</button>`);
    host.append(tbl, nav); const ro = readout(host);
    const draw = () => { tbl.querySelectorAll("tbody tr").forEach((tr, k) => { tr.classList.toggle("now", k === i); tr.classList.toggle("later", k > i); });
      ro.textContent = (cfg.notes && cfg.notes[i]) || ""; nav.querySelector(".w-pos").textContent = `${i + 1} / ${cfg.rows.length}`;
      nav.querySelector(".w-prev").disabled = i === 0; nav.querySelector(".w-next").disabled = i === cfg.rows.length - 1; };
    nav.querySelector(".w-prev").addEventListener("click", () => { i = Math.max(0, i - 1); draw(); });
    nav.querySelector(".w-next").addEventListener("click", () => { i = Math.min(cfg.rows.length - 1, i + 1); draw(); });
    caption(host, cfg); draw();
  }

  /* ---- vec2d: draggable arrows over points; sliders stay for keyboard use and move with the drag ---- */
  function renderVec2d(host, cfg) {
    frame(host, cfg);
    const X = cfg.x || { min: -6, max: 6 }, Y = cfg.y || X, W = 360, M = 16;
    const k = (W - 2 * M) / (X.max - X.min), H = Math.round((Y.max - Y.min) * k + 2 * M);  // equal scale on both axes
    const sx = (v) => M + (v - X.min) * k, sy = (v) => H - M - (v - Y.min) * k;
    const fig = el("div", "w-fig"); let ro; host.dataset.wid = ++uid; const wid = host.dataset.wid;
    const grid = cfg.grid || 1, deg = Math.PI / 180;
    const pidx = (id) => (cfg.params || []).findIndex((q) => q.id === id);
    const setParam = (id, v) => { const i = pidx(id); if (i < 0) return; const p = cfg.params[i]; const st = +p.step || (p.max - p.min) / 100;
      v = Math.min(p.max, Math.max(p.min, Math.round((v - p.min) / st) * st + +p.min)); const inp = host.querySelectorAll(".w-sliders input")[i];
      if (inp && +inp.value !== v) { inp.value = v; inp.dispatchEvent(new Event("input")); } };
    const angleInto = (a, p) => { // put angle a (deg) into [p.min, p.max], choosing the nearer end on the circle when outside
      let x = ((a - p.min) % 360 + 360) % 360 + +p.min; if (x <= p.max) return x;
      const dMax = x - p.max, dMin = +p.min + 360 - x; return dMax < dMin ? +p.max : +p.min; };
    const upd = () => {
      const r = computeVec2d(cfg, vals);
      let b = `<defs>${CLS.map((c) => `<marker id="v${wid}${c}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="mk ${c}"/></marker>`).join("")}<clipPath id="vc${wid}"><rect x="${M}" y="${M}" width="${W - 2 * M}" height="${H - 2 * M}"/></clipPath></defs><g clip-path="url(#vc${wid})">`;
      for (let g = Math.ceil(X.min / grid) * grid; g <= X.max + 1e-9; g += grid) b += `<line x1="${sx(g)}" y1="${sy(Y.min)}" x2="${sx(g)}" y2="${sy(Y.max)}" class="${Math.abs(g) < 1e-9 ? "ax" : "grid"}"/>`;
      for (let g = Math.ceil(Y.min / grid) * grid; g <= Y.max + 1e-9; g += grid) b += `<line x1="${sx(X.min)}" y1="${sy(g)}" x2="${sx(X.max)}" y2="${sy(g)}" class="${Math.abs(g) < 1e-9 ? "ax" : "grid"}"/>`;
      if (cfg.tickLabels !== false) { const lab = (v) => String(+v.toFixed(3));
        for (let g = Math.ceil(X.min / grid) * grid; g <= X.max; g += grid) if (Math.abs(g) > 1e-9 && g > X.min + 1e-9 && g < X.max - 1e-9 && Math.abs(g % (cfg.tickEvery || 2 * grid)) < 1e-9) b += `<text x="${sx(g)}" y="${sy(0) + 13}" text-anchor="middle" class="ts">${lab(g)}</text>`;
        for (let g = Math.ceil(Y.min / grid) * grid; g <= Y.max; g += grid) if (Math.abs(g) > 1e-9 && g > Y.min + 1e-9 && g < Y.max - 1e-9 && Math.abs(g % (cfg.tickEvery || 2 * grid)) < 1e-9) b += `<text x="${sx(0) - 5}" y="${sy(g) + 4}" text-anchor="end" class="ts">${lab(g)}</text>`; }
      const L = (X.max - X.min) + (Y.max - Y.min), ux = r.env.ux, uy = r.env.uy;
      if (cfg.probe && cfg.probe.line !== false) b += `<line x1="${sx(-L * ux)}" y1="${sy(-L * uy)}" x2="${sx(L * ux)}" y2="${sy(L * uy)}" class="w-probe"/>`;
      if (cfg.probe && cfg.probe.boundary) { const c = typeof cfg.probe.boundary === "string" ? evalExpr(cfg.probe.boundary, r.env) : 0;
        b += `<line x1="${sx(c * ux - L * uy)}" y1="${sy(c * uy + L * ux)}" x2="${sx(c * ux + L * uy)}" y2="${sy(c * uy - L * ux)}" class="w-bound"/>`; }
      r.points.forEach((p) => {
        if (cfg.shift && cfg.shift.trail && (p.x !== p.x0 || p.y !== p.y0)) b += `<circle cx="${sx(p.x0)}" cy="${sy(p.y0)}" r="4" class="w-ghost g${p.group}"/><line x1="${sx(p.x0)}" y1="${sy(p.y0)}" x2="${sx(p.x)}" y2="${sy(p.y)}" class="w-trail"/>`;
        if (cfg.probe && cfg.probe.feet) b += `<line x1="${sx(p.x)}" y1="${sy(p.y)}" x2="${sx(p.s * ux)}" y2="${sy(p.s * uy)}" class="w-foot"/><circle cx="${sx(p.s * ux)}" cy="${sy(p.s * uy)}" r="2.5" class="w-footpt g${p.group}"/>`;
      });
      b += `</g>`;
      r.points.forEach((p) => { b += `<circle cx="${sx(p.x)}" cy="${sy(p.y)}" r="5" class="w-vpt g${p.group}"/>` + (p.label ? `<text x="${sx(p.x) + 7}" y="${sy(p.y) - 7}" class="tn">${esc(p.label)}</text>` : ""); });
      r.vectors.forEach((v, i) => { const tx = v.fx + v.scale * v.x, ty = v.fy + v.scale * v.y;
        if (Math.hypot(v.x, v.y) > 1e-9) b += `<line x1="${sx(v.fx)}" y1="${sy(v.fy)}" x2="${sx(tx)}" y2="${sy(ty)}" class="w-vec ${v.cls}" marker-end="url(#v${wid}${v.cls})"/>`;
        if (v.label) { const n = Math.hypot(v.x, v.y) || 1, ox = (v.x / n) * 14, oy = -(v.y / n) * 14;
          b += `<text x="${sx(tx) + ox}" y="${sy(ty) + oy + 4}" text-anchor="middle" class="w-vlab ${v.cls}">${esc(v.label)}</text>`; }
        if (v.drag) { const pa = v.drag.angle && cfg.params[pidx(v.drag.angle)], val = pa ? vals[pa.id] : null;
          b += `<circle cx="${sx(tx)}" cy="${sy(ty)}" r="16" class="w-handle ${v.cls}" data-vi="${i}" tabindex="0" role="slider" aria-label="${esc(v.drag.label || v.label || "drag")}"` +
            (pa ? ` aria-valuemin="${pa.min}" aria-valuemax="${pa.max}" aria-valuenow="${val}"` : "") + `/>`; } });
      rendering = true;
      fig.innerHTML = `<svg viewBox="0 0 ${W} ${H}" class="fig w-vec2d-svg" role="group" aria-label="${esc(cfg.title || "vectors")}">${b}</svg>`;
      if (focusVi != null) { const h = fig.querySelector(`.w-handle[data-vi="${focusVi}"]`); if (h) h.focus({ preventScroll: true }); }
      rendering = false;
      if (ro) ro.textContent = r.readout;
    };
    let dragVi = null, focusVi = null, rendering = false;
    const toData = (e) => { const svg = fig.querySelector("svg"), m = svg.getScreenCTM(); if (!m) return null;
      const pt = new DOMPoint(e.clientX, e.clientY).matrixTransform(m.inverse()); return [X.min + (pt.x - M) / k, Y.min + (H - M - pt.y) / k]; };
    const dragTo = (vi, d) => { const v = cfg.vectors[vi], dr = v.drag, sc = v.scale || 1; if (!d) return;
      const fx = v.from ? evalExpr(v.from.x, computeVec2d(cfg, vals).env) : 0, fy = v.from ? evalExpr(v.from.y, computeVec2d(cfg, vals).env) : 0;
      const dx = (d[0] - fx) / sc, dy = (d[1] - fy) / sc;
      if (dr.angle) { const p = cfg.params[pidx(dr.angle)]; setParam(dr.angle, angleInto(Math.atan2(dy, dx) / deg, p)); }
      if (dr.length) setParam(dr.length, Math.hypot(dx, dy) / (dr.lengthUnit || 1));
      if (dr.x) setParam(dr.x, dx); if (dr.y) setParam(dr.y, dy); };
    fig.addEventListener("pointerdown", (e) => { const h = e.target.closest && e.target.closest(".w-handle"); if (!h) return;
      e.preventDefault(); dragVi = +h.dataset.vi; focusVi = dragVi; fig.setPointerCapture(e.pointerId); host.classList.add("dragging"); dragTo(dragVi, toData(e)); });
    fig.addEventListener("pointermove", (e) => { if (dragVi == null) return; e.preventDefault(); dragTo(dragVi, toData(e)); });
    const end = (e) => { if (dragVi == null) return; dragVi = null; host.classList.remove("dragging"); try { fig.releasePointerCapture(e.pointerId); } catch (_) {} };
    fig.addEventListener("pointerup", end); fig.addEventListener("pointercancel", end);
    fig.addEventListener("keydown", (e) => { const h = e.target.closest && e.target.closest(".w-handle"); if (!h) return;
      const v = cfg.vectors[+h.dataset.vi], id = v.drag.angle || v.drag.x; if (!id) return; const p = cfg.params[pidx(id)], st = +p.step || 1;
      const dir = { ArrowRight: 1, ArrowUp: 1, ArrowLeft: -1, ArrowDown: -1 }[e.key]; if (!dir) return;
      e.preventDefault(); focusVi = +h.dataset.vi; setParam(id, vals[id] + dir * st); });
    fig.addEventListener("focusout", (e) => { if (!rendering && !fig.contains(e.relatedTarget)) focusVi = null; });
    host.append(fig); if (cfg.readout) ro = readout(host);
    const vals = sliders(host, cfg, upd); presets(host, cfg, vals, upd);
    caption(host, cfg); upd();
  }

  /* ---- switch: segmented buttons over child <section data-label="..."> panels ---- */
  function renderSwitch(host) {
    const panels = [...host.querySelectorAll(":scope > section[data-label]")]; if (!panels.length) return;
    host.classList.add("lab", "w-switch");
    const seg = el("div", "seg"); host.prepend(seg);
    const show = (k) => { panels.forEach((p, j) => (p.hidden = j !== k)); seg.querySelectorAll("button").forEach((b, j) => b.setAttribute("aria-pressed", String(j === k))); };
    panels.forEach((p, k) => { const b = el("button", "", esc(p.dataset.label)); b.type = "button"; b.addEventListener("click", () => show(k)); seg.append(b); });
    show(0);
  }

  const RENDER = { lab: renderLab, plot: renderPlot, iterate: renderIterate, cascade: renderCascade, diagram: renderDiagram, stepper: renderStepper, switch: renderSwitch, vec2d: renderVec2d };
  function config(host) {
    if (host.dataset.configRef) { const s = doc.getElementById(host.dataset.configRef); return s ? JSON.parse(s.textContent) : {}; }
    return host.dataset.config ? JSON.parse(host.dataset.config) : {};
  }
  function mountAll(rootEl) {
    (rootEl || doc).querySelectorAll("[data-widget]").forEach((host) => {
      if (host.dataset.mounted) return; host.dataset.mounted = "1";
      const type = host.dataset.widget;
      try {
        const cfg = config(host); cfg.type = cfg.type || type;
        if (!RENDER[type]) throw new Error(`unknown widget type '${type}'`);
        RENDER[type](host, cfg);
      } catch (e) {
        host.innerHTML = `<p class="w-err">Widget error (${esc(type)}): ${esc(e.message)}</p>`;
        if (root.console) console.error("[AI4W]", type, e);
      }
    });
  }
  API.mountAll = mountAll;
  if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", () => mountAll()); else mountAll();
})(typeof window !== "undefined" ? window : globalThis);

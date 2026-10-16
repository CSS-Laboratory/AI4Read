/* AI4Read site shim.
   On claude.ai the viewer provides window.claude.use("db" | "sample" | "downloads").
   On khyang-lab.org this file provides the same small API, backed by the Worker routes under /api/ai4read/.
   Contract: see site/ai4read/API.md. Load this file BEFORE the post's own scripts. */
(function () {
  "use strict";
  if (window.claude && typeof window.claude.use === "function") return; // inside claude.ai: keep the real one
  var POST = (document.querySelector('meta[name="ai4read-post"]') || {}).content || location.pathname.split("/").filter(Boolean)[1] || "unknown";
  var API = "/api/ai4read";
  function err(code, message) { var e = new Error(message || code); e.code = code; return e; }
  async function call(method, url, body) {
    var r;
    try { r = await fetch(url, { method: method, headers: body ? { "content-type": "application/json" } : {}, body: body ? JSON.stringify(body) : undefined, credentials: "same-origin" }); }
    catch (e) { throw err("unavailable", "offline"); }
    if (r.status === 401 || r.status === 403) throw err("not_granted", "sign in required");
    if (r.status === 429) throw err("rate_limited", "too many requests");
    if (!r.ok) throw err("unavailable", "HTTP " + r.status);
    return r.status === 204 ? null : r.json();
  }
  /* ---------------- db: Firestore-like subset used by the post ---------------- */
  function snapDoc(id, data) { return { id: id, exists: data != null, data: function () { return data == null ? undefined : JSON.parse(JSON.stringify(data)); }, metadata: { fromCache: false, hasPendingWrites: false } }; }
  function collection(name) {
    var base = API + "/db/" + encodeURIComponent(POST) + "/" + encodeURIComponent(name);
    function docRef(id) {
      var url = base + "/" + encodeURIComponent(id);
      return {
        id: id, path: name + "/" + id,
        get: async function () { var j = await call("GET", url); return snapDoc(id, j && j.data); },
        set: async function (data) { await call("PUT", url, { data: data, merge: false }); },
        update: async function (data) { await call("PUT", url, { data: data, merge: true }); },
        delete: async function () { await call("DELETE", url); },
        onSnapshot: function (next) { var stop = false; (async function loop() { while (!stop) { try { next(await docRef(id).get()); } catch (e) {} await new Promise(function (r) { setTimeout(r, 30000); }); } })(); return function () { stop = true; }; }
      };
    }
    async function list() {
      var j = await call("GET", base);
      var docs = (j.docs || []).map(function (d) { return snapDoc(d.id, d.data); });
      return { docs: docs, size: docs.length, empty: !docs.length, metadata: { fromCache: false, hasPendingWrites: false }, docChanges: function () { return docs.map(function (d, i) { return { type: "added", doc: d, oldIndex: -1, newIndex: i }; }); } };
    }
    var q = {
      path: name,
      doc: function (id) { return docRef(id || ("d" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8))); },
      add: async function (data) { var j = await call("POST", base, { data: data }); return docRef(j.id); },
      get: list,
      where: function () { return q; }, orderBy: function () { return q; }, limit: function () { return q; },
      onSnapshot: function (next, onError) {
        var stop = false, last = "";
        (async function loop() {
          while (!stop) {
            try { var s = await list(); var sig = JSON.stringify(s.docs.map(function (d) { return [d.id, d.data()]; })); if (sig !== last) { last = sig; next(s); } }
            catch (e) { if (onError) onError(e); }
            await new Promise(function (r) { setTimeout(r, 30000); });
          }
        })();
        return function () { stop = true; };
      }
    };
    return q;
  }
  var db = {
    collection: collection,
    doc: function (path) { var p = String(path).split("/"); return collection(p[0]).doc(p.slice(1).join("_")); }
  };
  /* ---------------- sample: Ask Claude through the Worker (streamed) ---------------- */
  async function sample(input, opts) {
    opts = opts || {};
    var messages = typeof input === "string" ? [{ role: "user", content: input }] : input;
    var r;
    try { r = await fetch(API + "/ask", { method: "POST", headers: { "content-type": "application/json" }, credentials: "same-origin", signal: opts.signal, body: JSON.stringify({ post: POST, messages: messages }) }); }
    catch (e) { if (e && e.name === "AbortError") throw err("cancelled"); throw err("unavailable", "offline"); }
    if (r.status === 401 || r.status === 403) throw err("not_granted");
    if (r.status === 429) throw err("rate_limited");
    if (!r.ok || !r.body) throw err("unavailable", "HTTP " + r.status);
    var reader = r.body.getReader(), dec = new TextDecoder(), buf = "", text = "", truncated = false;
    for (;;) {
      var chunk = await reader.read(); if (chunk.done) break;
      buf += dec.decode(chunk.value, { stream: true });
      var lines = buf.split("\n"); buf = lines.pop();
      for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim(); if (!line.startsWith("data:")) continue;
        var ev; try { ev = JSON.parse(line.slice(5)); } catch (e) { continue; }
        if (ev.delta) { text += ev.delta; if (opts.onText) opts.onText({ text: text, delta: ev.delta }); }
        if (ev.error) throw err(ev.error, ev.message);
        if (ev.truncated) truncated = true;
      }
    }
    return { text: text, truncated: truncated, modelTierApplied: "default", modelApplied: "claude-sonnet-5-5" };
  }
  sample.limits = async function () { return { maxPromptBytes: 180000 }; };
  sample.json = async function (input, opts) { var r = await sample(input, opts); return JSON.parse(r.text); };
  /* ---------------- downloads: a normal website can save files directly ---------------- */
  var downloads = {
    save: async function (req) {
      var blob = req.data instanceof Blob ? req.data : new Blob([req.data]);
      var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = req.filename || "download";
      document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
      return { status: "saved" };
    }
  };
  var caps = { db: db, sample: sample, downloads: downloads };
  window.claude = { use: async function (name) { return caps[name] || null; } };
})();

/* AI4Read public shim (blog build, 2026-11-28).
   Public readers get the same small window.claude API as the owner edition, but nothing leaves the browser:
   - db: kept in this browser's localStorage (guess-first answers, quiz state), never sent anywhere;
   - sample (Ask Claude): not available → null, so the page hides it;
   - user: never the owner, so owner features (Chinese audio, notes) stay hidden;
   - downloads: a normal file save.
   No request goes to /api/ai4read/*. Load this file BEFORE the post's own scripts. */
(function () {
  "use strict";
  if (window.claude && typeof window.claude.use === "function") return;
  var POST = (document.querySelector('meta[name="ai4read-post"]') || {}).content || "post";
  var KEY = "ai4read-public:" + POST;
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch (e) { return {}; } }
  function save(all) { try { localStorage.setItem(KEY, JSON.stringify(all)); } catch (e) {} }
  function copy(x) { return x == null ? undefined : JSON.parse(JSON.stringify(x)); }
  function snapDoc(id, data) { return { id: id, exists: data != null, data: function () { return copy(data); }, metadata: { fromCache: true, hasPendingWrites: false } }; }
  var listeners = {};
  function notify(name) { (listeners[name] || []).forEach(function (f) { try { f(); } catch (e) {} }); }
  function collection(name) {
    function docs() { return (load()[name]) || {}; }
    function put(id, data, merge) { var all = load(); var c = all[name] || {}; c[id] = merge ? Object.assign({}, c[id] || {}, data) : data; all[name] = c; save(all); notify(name); }
    function docRef(id) {
      return {
        id: id, path: name + "/" + id,
        get: async function () { return snapDoc(id, docs()[id]); },
        set: async function (data) { put(id, copy(data), false); },
        update: async function (data) { put(id, copy(data), true); },
        delete: async function () { var all = load(); if (all[name]) { delete all[name][id]; save(all); notify(name); } },
        onSnapshot: function (next) { var f = function () { next(snapDoc(id, docs()[id])); }; f(); (listeners[name] = listeners[name] || []).push(f); return function () { listeners[name] = (listeners[name] || []).filter(function (g) { return g !== f; }); }; }
      };
    }
    function list() {
      var d = docs(); var out = Object.keys(d).map(function (k) { return snapDoc(k, d[k]); });
      return { docs: out, size: out.length, empty: !out.length, metadata: { fromCache: true, hasPendingWrites: false },
        docChanges: function () { return out.map(function (x, i) { return { type: "added", doc: x, oldIndex: -1, newIndex: i }; }); } };
    }
    var q = {
      path: name,
      doc: function (id) { return docRef(id || ("d" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8))); },
      add: async function (data) { var id = "d" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8); put(id, copy(data), false); return docRef(id); },
      get: async function () { return list(); },
      where: function () { return q; }, orderBy: function () { return q; }, limit: function () { return q; },
      onSnapshot: function (next) { var f = function () { next(list()); }; f(); (listeners[name] = listeners[name] || []).push(f); return function () { listeners[name] = (listeners[name] || []).filter(function (g) { return g !== f; }); }; }
    };
    return q;
  }
  var db = { collection: collection, doc: function (p) { var s = String(p).split("/"); return collection(s[0]).doc(s.slice(1).join("_")); } };
  var downloads = {
    save: async function (req) {
      var blob = req.data instanceof Blob ? req.data : new Blob([req.data]);
      var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = req.filename || "download";
      document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 2000);
      return { status: "saved" };
    }
  };
  var user = { isOwner: async function () { return false; }, canEdit: async function () { return false; } };
  var caps = { db: db, sample: null, downloads: downloads, user: user };
  window.claude = { use: async function (name) { return caps[name] || null; } };
})();

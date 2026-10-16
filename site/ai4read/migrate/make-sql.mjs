// Turn exported artifact data (migrate/<slug>/<coll>/<id>.json) into SQL for the D1 "docs" table.
// Usage: node migrate/make-sql.mjs owner@example.com > migrate/seed.sql ; then: npx wrangler d1 execute ai4read --remote --file migrate/seed.sql
import fs from "node:fs"; import path from "node:path";
const user = (process.argv[2] || "").toLowerCase(); if (!user.includes("@")) { console.error("usage: make-sql.mjs <email>"); process.exit(1); }
const R = path.dirname(new URL(import.meta.url).pathname); const q = s => "'" + String(s).replace(/'/g, "''") + "'";
const now = new Date().toISOString(); const out = [];
for (const slug of fs.readdirSync(R).filter(d => fs.statSync(path.join(R, d)).isDirectory()))
  for (const coll of fs.readdirSync(path.join(R, slug)))
    for (const f of fs.readdirSync(path.join(R, slug, coll)).filter(f => f.endsWith(".json"))) {
      let data = JSON.parse(fs.readFileSync(path.join(R, slug, coll, f), "utf8")); if (data && data.data && Object.keys(data).length <= 4) data = data.data;
      out.push(`INSERT OR REPLACE INTO docs (post, coll, id, user, data, updated_at, deleted) VALUES (${q(slug)},${q(coll)},${q(f.slice(0, -5))},${q(user)},${q(JSON.stringify(data))},${q(data.updatedAt || now)},${data.deleted ? 1 : 0});`);
    }
console.log(out.join("\n"));

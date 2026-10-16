-- D1 database "ai4read"
CREATE TABLE IF NOT EXISTS docs (
  post TEXT NOT NULL,          -- post slug, e.g. 2026-10-llm-next-word
  coll TEXT NOT NULL,          -- annotations | notes | guesses | game | diag
  id TEXT NOT NULL,
  user TEXT NOT NULL,          -- verified Cloudflare Access email
  data TEXT NOT NULL,          -- JSON
  updated_at TEXT NOT NULL,    -- ISO time
  deleted INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (post, coll, user, id)
);
CREATE INDEX IF NOT EXISTS docs_by_post ON docs (post, coll, updated_at);
CREATE TABLE IF NOT EXISTS usage (
  day TEXT NOT NULL,           -- JST date
  user TEXT NOT NULL,
  count INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (day, user)
);

# Handoff · AI4Read private posts on khyang-lab.org

For: the agent that maintains khyang-lab.org (repo `MI&ME Unit`, `web/`). From: AI4Read quality lead (Claude). Date: 2026-10-16.
Owner: Kunhao Yang. **Ask Kunhao before any step that creates GCP or Cloudflare resources, changes IAM, or costs money.** The steps marked 🔑 are his to run or approve.

## 1. Goal
Serve AI4Read study posts (interactive HTML + audio) at `https://khyang-lab.org/ai4read/`, visible **only to Kunhao and the students he invites**. Notes and annotations are saved per person. "Ask Claude" is answered by **Claude Sonnet 5.5 on Vertex AI** (project `playground-491901`). This also fixes the audio problem in the claude.ai viewer: R2 media with `Range` support works on iPhone.

## 2. What is in this package (AI4Read repo, `site/ai4read/`)
| Path | What it is |
|---|---|
| `dist/` | Ready-to-upload files: `index.html` (the shelf), `_shared/` (`site-shim.js`, `lib/`, `shelf.css`), `2026-10-llm-next-word/` (post, scripts, css, 14 MP3s, `post.json`, `context.json`). Built by `node posts/<slug>/build.mjs --site` + `node site/ai4read/build-index.mjs`. |
| `API.md` | The contract between the pages and the Worker. **Read it first.** |
| `worker/ai4read.ts` | Reference implementation of all routes for `web/worker/index.ts`. Adapt it to the site's style; keep the behaviour. |
| `schema.sql` | D1 schema (`docs`, `usage`). |
| `proxy/` | Cloud Run proxy for Claude on Vertex. Uses the service's own service account, so **no service-account keys**. Only needed if §4 test A fails. |
| `dev/mock-server.mjs` | Local stand-in with the same contract (no auth, canned "ask"). Already used to test the pages under the strict CSP: audio plays with Range, db round trip works, streaming ask works, no CSP violations, no horizontal scroll at 390 px. |
| `migrate/` | Kunhao's existing notes, guesses and annotations exported from the claude.ai artifact, plus `make-sql.mjs`, which turns them into D1 inserts. |
| `publish-r2.sh` | Uploads `dist/` to R2 with correct content types. |

## 3. Architecture
```
browser ──► Cloudflare Access (khyang-lab.org/ai4read*, khyang-lab.org/api/ai4read*)  ← email one-time PIN, allow-list
         └► Worker khyang-lab: handleAI4Read()
              ├─ GET /ai4read/**        → R2 "ai4read" (Range → 206; CSP; noindex)
              ├─ /api/ai4read/db/**     → D1 "ai4read" (per-user docs)
              ├─ POST /api/ai4read/ask  → Claude Sonnet 5.5 on Vertex (streamRawPredict, global) → SSE
              └─ GET /api/ai4read/me    → {email, role}
```
Posts are **not** part of the Astro build and **not** in git. They live in R2, so publishing a post means uploading files, with no site rebuild. Nothing under `/ai4read` may appear in `dist/` of the Astro site, the sitemap, or the nav. A link in the nav is optional; Access protects the page either way.

## 4. Steps
1. **Read** `API.md`, `worker/ai4read.ts`, and this repo's `AGENTS.md`/`CLAUDE.md` rules (security history: no keys in client code).
2. **Access (protection)** 🔑. In Cloudflare Zero Trust, create one self-hosted application covering `khyang-lab.org/ai4read` and `khyang-lab.org/api/ai4read`.
   - Policy: *Allow* emails = Kunhao's address(es) + the students he names. Login method: one-time PIN by email.
   - Session duration: 30 days.
   - Record the **team name** and the application **AUD** tag as Worker vars `ACCESS_TEAM` and `ACCESS_AUD`.
   - (Check the current Zero Trust free-plan seat limit. It has been 50 users.)
   - Fallback only if Kunhao rejects Access: extend the existing `/ideas/` key system (hashed keys in KV, TTL). Issue each key with `scripts/idea_keys.py`, set an HttpOnly, Secure, SameSite=Strict signed session cookie, and use the key label as the user id. Keep the same API.
3. **Storage** 🔑: create R2 bucket `ai4read` (private, no public URL) and D1 database `ai4read`. Apply `schema.sql`. Add bindings `AI4READ_BUCKET` and `AI4READ_DB`, and the var `AI4READ_OWNERS` (Kunhao's Access email).
4. **Claude on Vertex.** Test before choosing how to authenticate.
   - **Test A (no new resources):** from a terminal, call the global `streamRawPredict` URL in `API.md` with the existing Worker Vertex key in the `x-goog-api-key` header (value read by Kunhao, never printed). Send a minimal body: `{"anthropic_version":"vertex-2023-10-16","max_tokens":20,"messages":[{"role":"user","content":"Say hi"}]}`.
     - If it returns 200, set the secret `VERTEX_API_KEY`, then **restrict that key or create a dedicated one** for the AI4Read route, with its own quota and budget alert.
     - If it returns 401 or 403 (Vertex API keys may not cover partner models), go to Test B.
   - **Test B** 🔑: deploy `proxy/` to Cloud Run with its own service account (`roles/aiplatform.user`). The commands are in `proxy/server.mjs`. Put the shared secret in Secret Manager. Set `CLAUDE_PROXY_URL` (var) and `CLAUDE_PROXY_SECRET` (Worker secret).
   - Keep the caps in `worker/ai4read.ts` (1,500 output tokens; 40 asks per student per day, 120 per owner, 300 site-wide). One ask costs roughly **$0.03–0.12** at Sonnet prices, depending on how much of the post is sent. Consider prompt caching for the post context.
   - Add a GCP budget alert for this route.
5. **Worker.** Merge `handleAI4Read()` into `web/worker/index.ts` before the existing routes.
   - Make sure `/ai4read/*` and `/api/ai4read/*` reach the Worker and are not answered by static assets or the 404 page. Use `assets.run_worker_first` for those patterns if needed.
   - Do not touch `/catspaw/`, `/ideas/`, or the Gemini budget object.
   - The `/ai4read` HTML responses carry their own CSP (in the reference code). Do not apply the site-wide CSP rewrite to them.
6. **Upload.** From `web/`: `bash <AI4Read>/site/ai4read/publish-r2.sh <AI4Read>/site/ai4read/dist`.
7. **Migrate notes** 🔑: `node migrate/make-sql.mjs <Kunhao's Access email> > seed.sql`, then `npx wrangler d1 execute ai4read --remote --file seed.sql`.
8. **Acceptance tests.** Run them on iPhone (Safari, the Chrome app, and the Claude app's in-app browser) and on Mac:
   1. Signed out: `/ai4read/` shows the Access login, not content. `curl` with no cookie gets the Access page.
   2. Signed in as Kunhao: the shelf lists the post, and the post renders with no console CSP errors.
   3. **Audio:** tap play, and it plays on iPhone. Seeking works (206 responses). "Keep all audio for the train" works. "Save as one MP3" downloads.
   4. **Annotate:** select text, then annotate → save note → reload → the highlight persists; edit it and delete it. Kunhao's migrated notes are visible.
   5. **Ask Claude:** the answer streams in and can be saved as a note. The 41st ask by a student on one day gets the "too many" message.
   6. Signed in as a test student: the student sees the post but not Kunhao's notes. Kunhao can list all notes with `?scope=all`.
   7. `x-robots-tag: noindex` is on every `/ai4read` response. Nothing from `/ai4read` is in the sitemap or the static `dist/`.
9. **Record.** Update `PROGRESS.md`/`COLD_START.md` (a new "AI4Read private posts" section: bindings, routes, how to publish a post, how to invite a student). Commit only the relevant files.

## 5. Inviting a student (after setup)
Add the student's email to the Access policy, then send them `https://khyang-lab.org/ai4read/`. They sign in with the PIN that arrives by email. To remove a student, delete their email from the policy and revoke their active session.

## 6. Future posts
AI4Read builds each post into `site/ai4read/dist/<slug>/` and refreshes `index.html`. Publishing is step 6 with a slug. Later, a writer-agent pipeline (AI4Read phase 2) may upload through a small authenticated "publish" route. That route is not part of this handoff.

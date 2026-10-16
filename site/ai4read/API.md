# AI4Read on khyang-lab.org — page ↔ Worker contract

The post pages are written once and run in two places: as a claude.ai artifact, and on khyang-lab.org. On claude.ai the viewer provides `window.claude.use(...)`. On the website, `/ai4read/_shared/site-shim.js` provides the same calls by talking to these Worker routes. All routes sit behind Cloudflare Access, and the Worker also checks the Access JWT.

## Pages and media (Cloudflare R2 bucket `ai4read`, served by the Worker)
| Path | R2 key | Notes |
|---|---|---|
| `GET /ai4read/` | `index.html` | the private shelf (list of posts) |
| `GET /ai4read/<slug>/` | `<slug>/index.html` | a post; the response carries the CSP below |
| `GET /ai4read/<slug>/<file>` | `<slug>/<file>` | `post.css`, `app.js`, `figs.js`, `annotate.js`, `data.js`, `post.json`, `context.json` |
| `GET /ai4read/<slug>/audio/<id>.mp3` | same | **must honour `Range` (206)**: iPhone audio needs it |
| `GET /ai4read/_shared/...` | same | `site-shim.js`, `lib/{marked,purify,katex}.min.js`, `shelf.css` |

Headers on every response: `cache-control: private, max-age=300`, `x-robots-tag: noindex, nofollow`, `accept-ranges: bytes`. HTML responses also get:
`default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; media-src 'self' blob: data:; connect-src 'self'; font-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'`
(`style-src 'unsafe-inline'` is needed because the interactive figures set inline styles. No inline scripts are used; the only inline `<script>` is a JSON data block, which CSP does not execute.)

## Identity
- `GET /api/ai4read/me` returns `{email, role}`. `role` is `"owner"` for emails in `AI4READ_OWNERS`, otherwise `"student"`.

## Per-user documents (D1 table `docs`; schema in `schema.sql`)
Collections: `annotations`, `notes`, `guesses`, `game`, `diag`. Every document belongs to the signed-in user. Owners can list everyone's documents with `?scope=all`.
| Method | Path | Body | Response |
|---|---|---|---|
| GET | `/api/ai4read/db/<slug>/<coll>` | none | `{docs:[{id, data, updatedAt}]}` |
| GET | `/api/ai4read/db/<slug>/<coll>/<id>` | none | `{id, data \| null, updatedAt}` |
| POST | `/api/ai4read/db/<slug>/<coll>` | `{data}` | `{id, updatedAt}` |
| PUT | `/api/ai4read/db/<slug>/<coll>/<id>` | `{data, merge: bool}` | `{id, updatedAt}`; `merge: true` is a shallow merge |
| DELETE | `/api/ai4read/db/<slug>/<coll>/<id>` | none | 204, soft delete |
Limits: id `[\w.:-]{1,200}`, data ≤ 200 KB. Errors: 400 `bad_path`, 401 `not_signed_in`, 413 `too_large`.

## Ask Claude
`POST /api/ai4read/ask` with body `{post, messages:[{role:"user"|"assistant", content}]}`. The last message must be from the user. At most 24 messages and 180 KB in total. The page itself puts the selected passage, the section text, the post and the source brief into the first user message.

The response is `text/event-stream`, one JSON object per `data:` line:
- `{"delta":"…"}` (repeated)
- `{"truncated":true}` (optional)
- `{"error":"upstream_error","message":"…"}` (optional)
- `{"done":true}` (always last)

Server side, the Worker:
- prepends a fixed system prompt;
- sends the request to Claude Sonnet 5.5 on Vertex AI (`publishers/anthropic/models/claude-sonnet-5-5:streamRawPredict`, project `playground-491901`, location `global`) with `max_tokens` 1500;
- enforces daily quotas: 40 per student, 120 per owner, 300 site-wide (JST day).

Errors: 429 `rate_limited`, 502 `upstream_error`, 400 `invalid_request`. The shim maps 401/403 to `not_granted`, so the page hides "Ask Claude".

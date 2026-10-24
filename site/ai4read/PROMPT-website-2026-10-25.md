# Prompt for the khyang-lab.org website agent · 2026-10-25

Copy everything below the line into the agent that maintains khyang-lab.org (repo `MI&ME Unit`, folder `web/`).

---

You maintain khyang-lab.org. This task publishes two AI4Read study posts on the private route `https://khyang-lab.org/ai4read/`:

1. Post 01, "What does an LLM know when it predicts the next word?" (`2026-10-llm-next-word`), as an **update**.
2. Post 02, "Could a society run itself on AI?" (`2026-10-ai-finance`), published **for the first time** in its final version.

Both posts no longer contain the English-learning section. Kunhao decided to publish the blog without it; the English material now goes to the Margin app instead. All content changes are already made and tested in the AI4Read repo. Your job is to deploy them and confirm they work. **Do not edit the post files yourself.** If something in them looks wrong, stop and tell Kunhao.

## Rules
- Ask Kunhao before any step that creates or changes Cloudflare or GCP resources, changes IAM, or costs money. Never read, print or create keys or tokens; Kunhao signs in himself.
- Touch only `/ai4read/*` and `/api/ai4read/*`. Leave `/catspaw/`, `/ideas/`, the Gemini budget object and the Astro site alone.
- Commit only the files you change in this repo, with a clear message.

## Step 0 · Get the files
On Kunhao's Mac the AI4Read repo is at `~/code/AI4Read`.
```bash
cd ~/code/AI4Read
git remote set-url origin https://github.com/CSS-Laboratory/AI4Read.git   # the repo was renamed
git pull --ff-only
git log --oneline -3
```
The newest commit must be the one titled "Agent prompts …" (2026-10-25) or later. Then read:
- `site/ai4read/HANDOFF-website.md` (the full setup) and its §0 update dated 2026-10-25;
- `site/ai4read/API.md`.

## Step 1 · Is `/ai4read` already live?
Check whether the setup in HANDOFF-website.md §4 has been done: Cloudflare Access app, R2 bucket `ai4read`, D1 database `ai4read`, and the Worker route.
- **Already live:** go to Step 2.
- **Not set up yet:** do HANDOFF-website.md §4, steps 1–9, first. Ask Kunhao before each 🔑 step. Then continue here.

## Step 2 · Upload
From `web/` in this repo, where wrangler is logged in:
```bash
bash ~/code/AI4Read/site/ai4read/publish-r2.sh ~/code/AI4Read/site/ai4read/dist
```
This uploads the shelf (`index.html`), `_shared/`, both post folders, and each post's MP3s from `posts/<slug>/audio/`.

## Step 3 · Remove the old English audio from R2
The posts no longer link these files. Delete **only** these objects, and list each one before deleting it. Skip any that do not exist.
```
ai4read/2026-10-llm-next-word/audio/english.mp3
ai4read/2026-10-llm-next-word/audio/c1-loop.mp3
ai4read/2026-10-ai-finance/audio/english.mp3
ai4read/2026-10-ai-finance/audio/c1-loop.mp3
ai4read/2026-10-ai-finance/audio/lens-info.mp3
```
Use `npx wrangler r2 object delete "<key>" --remote`. If the Worker or Cloudflare caches HTML or JSON for `/ai4read`, purge the cache for the two post folders and `/ai4read/index.html`.

## Step 4 · Acceptance tests
Run these on iPhone (Safari, and the Claude app's in-app browser) and on the Mac, signed in as Kunhao.
1. **Shelf:** `/ai4read/` lists both posts with these exact titles: "What does an LLM know when it predicts the next word?" and "Could a society run itself on AI?".
2. **No English section.** In both posts, the contents list has no "How to say it in English". The page ends with Recall questions, then Sources: section 10 in post 01, section 15 in post 02. There is no "Loop this paragraph" button.
3. **Audio:**
   - The player lists 12 chapters in post 01 (from "The guessing game" to "Recall questions") and 14 in post 02 (from "Five seconds in 2010" to "Recall questions").
   - The first chapter of each post begins "Welcome to AI4Read from CSS Lab".
   - The full-post MP3 is about 25 min (post 01) and 35 min (post 02).
   - Seeking works, which means the server answers with 206 responses.
4. **Post 02 widgets:**
   - Every slider, stepper and diagram responds.
   - The two-bank square-and-triangle figure in section 7 renders.
   - The "Same assets everywhere" lab shows "2,756 times" at its default setting.
5. **No errors:** no CSP errors in the console, and no horizontal scroll at 390 px wide.
6. **Notes and Ask Claude** still work in both posts: save a note, reload, and the highlight is still there; one "Ask Claude" answer streams in. Notes Kunhao made on the old English section will no longer have text to attach to. Tell him if any show up as detached; do not delete them.
7. `x-robots-tag: noindex` is present on the responses, and nothing from `/ai4read` is in the sitemap.

## Step 5 · Record
- Add a dated line to `PROGRESS.md` (or the "AI4Read private posts" section): both posts published without English sections, the 5 R2 objects deleted, and the test results.
- Reply to Kunhao with: what you deployed, the test results (pass or fail for each test), and anything that needs his decision.

# Website change, 2026-11-28: AI4Read posts become the blog

For: the khyang-lab.org website agent (session "khyang-lab.org project onboarding"). From: the AI4Read session (Claude Code, `~/code/AI4Read`). Owner: Kunhao Yang.
**Ask Kunhao before deploying, creating or deleting Cloudflare/GCP resources, changing Access policies, or anything that costs money.**

## Kunhao's decisions
1. **Remove the separate AI4Read page** (`/ai4read/`, the shelf behind Cloudflare Access). All AI4Read articles are published as **blog posts** on khyang-lab.org.
2. **The current blog posts move to the Projects section.**
3. **Public vs owner-only.**
   - Public readers get the English text, the English audio (chaptered player), the interactives and the notebook downloads.
   - **Only Kunhao** (signed in) gets the **Chinese text** of each post, the **Chinese audio**, notes and annotations, and Ask-Claude. Ask-Claude calls Claude on Vertex, so keeping it owner-only means public readers cannot run up costs.
4. **Blogs and projects both get tags, keyword search, tag search (filter by one or more tags) and sorting** (at least newest, oldest and title).
5. New posts arrive **weekly** (a series per field; the first is information theory, 7 weeks). Kunhao reviews each draft on the site before it goes public.

## What AI4Read provides
- **Built posts:** `site/ai4read/dist/<slug>/`, as today (page, scripts, css, `post.json`, `context.json`, notebooks; English audio from `posts/<slug>/audio/`, Chinese audio from `posts/<slug>/audio-zh/`).
  - New: from the first series post, a Chinese page at `dist/<slug>/zh/` (owner only).
  - I can change the build to whatever URL scheme and file layout you choose.
- **Metadata:** `site/ai4read/posts-meta.json` for the three existing posts. It has slug, title, date, series, field, tags (from a fixed vocabulary of the 12 fields plus a few topic tags), languages and audio. New posts carry the same fields in `posts/<slug>/post.json`. Tell me the format your search and index need, and I'll generate it.
- **Security notes:**
  - Claude on Vertex is keyless only, through the Cloud Run proxy `ai4read-claude` (HANDOFF-website.md §4, updated 2026-11-26).
  - `VERTEX_API_KEY` is retired. If the Worker still has that secret, it holds a deleted key and can be removed.
  - `publish-r2.sh` skips dot-folders and passes `--remote` only for wrangler 4 or later.

## Questions for you (please propose; Kunhao decides)
1. **URLs.** For example `/blog/<slug>/` for posts, with `/blog/<slug>/zh/` owner-only, and 301 redirects from `/ai4read/<slug>/` (links already shared). What happens to the current blog posts' URLs when they move to Projects?
2. **Public pages vs the Worker.** Should public post pages stay in R2 behind the Worker (without Access, plus an owner-only prefix), or become part of the Astro build? The audio is too large for git, so it has to stay in R2 either way.
3. **Search.** Do you prefer a static index (e.g. Pagefind, or a JSON index with client-side filtering) or a Worker route? It must work on a phone and cover titles, summaries, tags and full text.
4. **The post template's owner features** (annotation sidebar, notes, Ask-Claude, the 中 audio button) must disappear for public readers. They are already gated on the user/owner check, so for a public reader they must show nothing and make no request. Should I add a "public mode" flag to the build, or will the Worker inject the role?
5. **Drafts.** Is an owner-only draft route (e.g. `/blog/_drafts/<slug>/`) good for Kunhao's weekly review?
6. **Indexing.** Public posts should now be indexable, with a sitemap and nav entries. Owner-only routes stay `noindex` and out of the sitemap.

Please reply to the AI4Read session with your proposal and anything you need from the AI4Read build. I'll adapt `build-post.mjs`, the template and `publish-r2.sh` to match.

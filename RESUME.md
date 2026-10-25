---
name: ai4read-resume
description: How to resume the AI4Read project from scratch, in a new Claude session or on a new computer. Where everything lives, how to restore what is not on GitHub, current state and open tasks. Keep this file current; a copy lives in Google Drive (backup/) and in the claude.ai Project docs.
updated: 2026-10-26
---

# Resume AI4Read

## 1. Where everything lives
| What | Where |
|---|---|
| **Repo** (code, posts, audio, wiki/knowledge graph, digests, pipeline, prompts) | GitHub `CSS-Laboratory/AI4Read` (private). Mac working copy: `~/code/AI4Read`. **Never put a git repo inside Google Drive.** |
| **Library** (book and paper PDFs, read-only input) | Google Drive `My Drive/Book/AI4Read/library/<field>/` |
| **Backup of what is not on GitHub** | Google Drive `My Drive/Book/AI4Read/backup/`. It holds post sources (copyrighted PDFs, saved web pages, talk audio) as split `.tar.gz` parts, a `git bundle` of the repo, this guide, and `SHA256SUMS` |
| **Project docs** (seen by every claude.ai session in the Project) | claude.ai Project "AI4Read": charter, writing principles, phase 2 plan, digestion report, this guide |
| **Published pages** | claude.ai artifacts. Post 01: https://claude.ai/artifact/NLzvyjQQRxppys5yME6KU3 · Post 02 (v2, 2026-10-18): https://claude.ai/artifact/W2MqKGeotV685SzSdeE3ti · Post 03 (draft, 2026-10-25): https://claude.ai/artifact/HET5R8dYrWAVrLoAVSVT38 · Library page: https://claude.ai/artifact/Q2Dg4ffVMAjkg54QDa8rE2 |
| **Website** | khyang-lab.org/ai4read behind Cloudflare Access. Kunhao's website agent deploys from `site/ai4read/` (HANDOFF-website.md); files are built into `site/ai4read/dist/`. |
| **English app** | Margin (MeWiki). Packs are in `site/mewiki/packs/`; the agent imports them (HANDOFF-margin.md). |

## 2. Start a new session
1. Open the claude.ai Project "AI4Read" and start a session. Link it to the Mac in the desktop app if local files are needed.
2. Get the repo: `git clone https://github.com/CSS-Laboratory/AI4Read.git ai4read` (or use `~/code/AI4Read`).
3. Read in this order:
   1. `CLAUDE.md`
   2. `CHARTER.md` (mission, fields, template, policies)
   3. `WRITING.md` (how to explain; update it when a review shows a missing rule)
   4. `learner/state.md`
   5. `phase2/RUNBOOK.md`, `phase2/rubric.md` and `phase2/log.md`
   6. the newest post folder in `posts/`
4. Restore the post sources from Drive (they are gitignored on purpose):
   ```bash
   cd ai4read/posts/<slug>/sources
   cat "<Drive>/backup/sources/<slug>-sources.tar.gz.part-"* | tar xzf -
   shasum -a 256 -c "<Drive>/backup/SHA256SUMS"   # optional check
   ```
   If the repo itself is lost: `git clone "<Drive>/backup/repo/ai4read-<date>.bundle" ai4read` (if the bundle was split into parts, first run `cat ai4read-<date>.bundle.part-* > ai4read.bundle`). Restore tested on 2026-10-18: checksums OK, 88 source files extracted, bundle cloned.
5. Tools:
   - `npm install` (KaTeX, highlight.js, marked, DOMPurify)
   - Playwright with Chromium for the render test
   - ffmpeg and pdftotext (poppler)
   - `bash scripts/setup_tts.sh` (Kokoro TTS: `/tmp/ttsenv` and `/tmp/kmodel`)
6. Build and test a post:
   ```bash
   node site/ai4read/build-post.mjs posts/<slug> --site
   node site/ai4read/components/check.mjs posts/<slug>/src/content.html
   node site/ai4read/dev/mock-server.mjs 8799 &
   node site/ai4read/components/test.mjs /ai4read/<slug>/ --base http://127.0.0.1:8799
   node site/ai4read/components/test.mjs posts/<slug>/index.html --inline   # the artifact page
   python3 scripts/wordcount.py posts/<slug>/src/content.html
   /tmp/ttsenv/bin/python scripts/tts_post.py posts/<slug>     # audio, tagged "AI4Read from CSS Lab"
   ```
7. Publish the draft as a claude.ai artifact. Upload the page `posts/<slug>/index.html` with the files `audio/*.mp3` and these capabilities:
   - db, with rules for annotations, notes, guesses and diag (read and write: admin);
   - sample;
   - downloads.

   Keep each file under 16 MB (all.mp3 is encoded at 48 kb/s).

## 3. How a post is made (phase 2, as revised 2026-10-18)
- Claude writes. Independent agents check:
  - an Opus fact-checker and a Sonnet fact-checker, merged by union;
  - a Sonnet pedagogy critic, scoring blind against `phase2/rubric.md`.
- Gate: 0 critical, 0 major, and every criterion ≥ 4. After 3 rounds, Claude fixes the rest and audits the post in full.
- Kunhao reviews on his phone and leaves notes (annotations in the artifact db). Claude answers each note, revises, re-records only the changed audio chapters, and updates `WRITING.md` with any new rule.
- Back up after each milestone:
  1. `git push` (GitHub).
  2. On the Mac, run `git bundle create "<Drive>/backup/repo/ai4read-<date>.bundle" --all` from `~/code/AI4Read`.
  3. `bash scripts/backup_drive.sh` packs the post sources into 24 MB parts under `/mnt/user-data/outputs/ai4read-backup/`; copy them to `<Drive>/backup/sources/`.
- **Last full backup: 2026-10-18 evening** (repo d7d2793, bundle verified "complete history"; post 02 sources incl. the real CACM PDF; SHA256SUMS on Drive match the container).

## 4. Current state (2026-10-25)
- **Post 01** "What does an LLM know when it predicts the next word?": reviewed and final.
  - Open: re-record the audio for the changed chapters, including the new intro "Welcome to AI4Read from CSS Lab".
- **Post 02** "Could a society run itself on AI?" (v2, published 2026-10-18 to the same artifact URL).
  - Centred on an AI-automated society; Harari is a short hint with his lines in a fold-out; finance is the worked case. Five jobs: run, decide, check, declare, answer. Lenses: Ashby/Arora (check), N_eff and Haldane–May (decide), Searle (declare), Lupia–McCubbins (answer). Short answer with a verdict (ours, definition-dependent).
  - S5: three rounds (Opus + Sonnet fact-checks, Sonnet critic) plus a post-round-3 audit; reviews and responses in `posts/2026-10-ai-finance/review/v2-*`. Final: round 3 Opus 0 major, Sonnet 1 major (fixed); critic audit Lens 2b and §13 at 4.
  - Source: `src/content-v2.tpl.html` + `src/v2-blocks/` + v1 blocks, filled by `src/fill_v2.py` into `src/content.html`. Edit the template or a block, then run the fill script; never edit content.html by hand.
  - Audio 37 min re-recorded. English pack rebuilt. Waiting for Kunhao's notes (S8).
  - *Nexus*: only the Penguin sample and the Guardian extract are used; the re-attached PDF was the pirate copy and was deleted.
- **Post 03** "What Is a Hidden State? The Residual Stream, Read and Written" (interpretability strand 1, draft published 2026-10-25; awaiting Kunhao's notes, S8).
  - Kunhao's S0 decisions: next post (04) is **eigen-decomposition** (canon reading path item 1b, before *Directions*); post-training clause kept out of the lens; two lenses (linear algebra, information theory); draggable widget.
  - Sources (gitignored; Drive `backup/sources/2026-10-residual-stream-sources.tar.gz.part-*`): Olah 2020, Elhage 2021 (residual stream, virtual weights, no privileged basis only), Nanda glossary (new URL), MacKay 2003 p. 237 (multiple-access channel, free author PDF).
  - Pipeline: S1 14 units → S2 (1 critical, 9 major fixed) → S3/S4 → S5 three rounds, gate missed by one major after round 3 → meta-manager step-in (results.md denominator fixed; targeted fix pass; verify-3c and critic-3c PASS) → polish. Final: 7,324 words, 8 widgets, audio 43.4 min (12 chapters), English C1–C2 pack (two review rounds) and loop audio.
  - Notebooks `notebook/01_bus_gpt2.ipynb` (TransformerLens 4.3) and `02_bus_my_model.ipynb` (HF hooks; default Qwen3-1.7B-Base, run here with GPT-2 and tiny random Qwen3/Gemma 3), executed; numbers in `notebook/results.md`. Full-size Qwen3 run is for Kunhao's Mac.
  - New component: `vec2d` (draggable arrows, synced sliders, keyboard; 46 px hit area) and opt-in signed bars. W9 added to toyworlds.md. Wiki: `wiki-candidates.md` (candidates only).
  - Site dist and shelf rebuilt (`site/ai4read/dist/2026-10-residual-stream/`, with notebooks); deploy is Kunhao's website agent's step when he approves.
- **English packs are passage-centred (`/2`, 2026-10-26)**, at the Margin agent's request: one 140–190-word British-English passage per post (audio recorded by Margin's own TTS; our Kokoro recorder is a fallback), 8–12 expressions and 2–4 patterns anchored in it, fixes built on its sentences, gist and retell. Tools: `scripts/english_pack.py` (Margin's checks), `scripts/retired_ids.py`; fallback recorder `scripts/tts_english_passage.py`. Packs for posts 01–03 reviewed in two rounds; `retired-2026-10-26.json`; HANDOFF-margin §0. The /1 sources are archived as `english/english-pack1.json`.
- **English separated (2026-10-25).** Kunhao publishes the blogs without the English section. Both posts now end at Recall and Sources (no English audio chapters; post 01 about 25 min, post 02 about 35 min; both artifacts republished). English is a separate **C1–C2 pack** per post: source `posts/<slug>/english/english.json`, build `python3 scripts/english_pack.py posts/<slug>` → `site/mewiki/packs/<slug>.json` + `.md`, loop audio `scripts/tts_english_loop.py <slug>` → `site/mewiki/packs/audio/`. Old material archived in `posts/<slug>/english/*-v1.*`. Independent check: `posts/2026-10-ai-finance/review/english-packs-check.md` (two rounds, all critical and major fixed).
- **Waiting on Kunhao's agents:** `site/ai4read/PROMPT-website-2026-10-25.md` (publish post 02, update post 01, delete 5 stale R2 objects) and `site/mewiki/PROMPT-margin-2026-10-25.md` (import the C1–C2 packs; ask before suspending the 45 retired items).
- **Website and Margin:** handoff packages delivered; Kunhao's agents deploy. "Ask Claude" uses his Vertex key.
- **Rules:** WRITING.md v0.9 (recall tests only this post, checks must work on the page, define at first use, measured numbers carry their frame, "none of the sources" needs a search, commented-out HTML is not published text); v0.8 (§8: English is a separate C1–C2 pack, not part of the post); earlier v0.7 (adds: threshold words, verdict in the short answer, one point one ladder, quoted formulas still climb, purpose ≠ effect, quote referent, one source per sentence, glosses are claims, search before "never", keep the source's scope).
- **Tooling:** test both builds: the site build (`--base` with the mock server) and the artifact build (`test.mjs posts/<slug>/index.html --inline`). The artifact build had silently lost its widgets until 2026-10-18 (fixed in build-post.mjs).

## 5. Standing constraints (from Kunhao)
- Never handle passwords, tokens or keys, and never create service-account keys. Kunhao logs in himself.
- Ask before any action that creates, changes or deletes cloud resources or costs money.
- The library folder is read-only input. Never use shadow libraries.
- Never put a git repo inside Google Drive.
- Never overwrite digests marked `audited:` with pipeline output.
- Every audio file carries the source mark "AI4Read from CSS Lab".

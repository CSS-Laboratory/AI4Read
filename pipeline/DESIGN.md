---
name: digest-pipeline-design
description: Architecture, quality gates, budget, and resumability for the one-off digestion of the AI4Read library on Vertex AI. Read before touching pipeline code.
owner: Claude (cloud session) = quality lead; local Claude Code agent = engineer
budget_usd: 300 (hard stop at 280)
---

# Digest pipeline — design (v1)

## Goal
Turn every work in `My Drive/Book/AI4Read/library/` (~160 files, ~24,500 pages) into
progressive-disclosure wiki digests (`wiki/works/<work-id>/<unit-id>.md`) that follow
`DIGEST_SPEC.md`, with **verified correctness**, inside a **$300** budget,
**resumable** at any point.

## Roles
| Who | Does |
|---|---|
| **Local Claude Code agent** (on Kunhao's Mac) | GCP setup, pipeline code, running the jobs, committing results and status |
| **Claude, cloud session** (quality lead) | Owns the prompts in `pipeline/prompts/`, reviews the unit plan and each wave's samples, decides go / no-go |
| **Kunhao** | Approves GCP actions, logs in himself, approves gates, can pause from his phone |

Communication happens **through this repo** (GitHub `CSS-Laboratory/AI4Read`): code, `pipeline/STATUS.md`, `pipeline/control.json`, review notes in `pipeline/reviews/`.

## Model & endpoint
- `claude-sonnet-5-5` on Vertex AI, project `playground-491901`, **global** endpoint (regional endpoints cost +10%).
- **Batch prediction** (50% discount). Online requests only for tiny tests and single re-runs.
- Auth: Application Default Credentials from Kunhao's own `gcloud auth application-default login`. **No service-account key files.**

## Inputs per unit
A **unit** = one paper, or one book chapter (split chapters longer than ~35 pages into parts at section boundaries).
Each request contains:
1. System prompt = `pipeline/prompts/digest.md` (+ `DIGEST_SPEC.md` inlined).
2. Unit metadata (work id, unit id, title, fields, PDF page range, printed page labels if known).
3. The **text layer** of the pages (from `pdftotext -layout`), each page wrapped as
   `<page pdf="34" printed="12"> … </page>`.
4. **Page images** (JPEG, long side ≈ 1500 px, quality ≈ 80) for:
   - every page of scanned files (no text layer), and
   - every page that has math, tables, or figures, or a garbled text layer.
   Detect with a cheap heuristic (math symbols / LaTeX-like glyphs, OCR noise ratio, image area). When unsure, include the image. Prose-only pages go text-only.
5. HTML sources: cleaned text only.

Hard limits to verify early (Gate 0): max request size and max images per request in Vertex Claude **batch**. If a unit exceeds them, split it.

## Passes
| Pass | Model call | Output |
|---|---|---|
| P1 Digest | `prompts/digest.md` | digest markdown |
| P2 Verify | `prompts/verify.md`: same source pages + the P1 digest | JSON verdict (`pass` / `repair` / `fail`) + issue list; if `repair`, a full corrected digest |
| P3 Re-digest | only for `fail`: P1 again with the verifier's issue list appended | new digest → P2 again (max 2 loops, then `needs-human`) |
| P4 Work map | `prompts/work_index.md`: all accepted unit digests (L0–L2 only) of one work | `wiki/works/<work-id>/index.md` |

**Deterministic checks** after P1 and after P2 (no model call):
- frontmatter parses; all required sections present and in order;
- every `(p. N)` lies inside the unit's printed page range (allow ±2 for chapter openers);
- all `$…$` / `$$…$$` parse with KaTeX (node `katex.renderToString`, throwOnError);
- word counts in bounds (L1 ≤ 120 words; L2 has 5–10 bullets);
- no prompt text leaked; no "As an AI" filler.
A unit that fails deterministic checks after P2 goes back to P3.

## State machine (resumable)
Per unit, stored in `pipeline/state/units.jsonl` (one JSON line per state change, append-only; the latest line wins) and mirrored in SQLite if convenient:

`planned → p1_submitted → p1_done → p2_submitted → p2_done → (accepted | p3_queued → … ) | needs_human | skipped`

- Every record stores: `unit_id`, `content_hash` (of inputs), `spec_version`, `batch_job_id`, token usage, cost, timestamps.
- **Idempotent**: a unit is re-sent only if its state is not done for the current `spec_version` + `content_hash`.
- Raw batch inputs and outputs are kept in GCS (`gs://<bucket>/ai4read/…`) for audit.

## Pause / resume
- `pipeline/control.json` in the repo: `{"mode": "run" | "pause" | "stop", "max_spend_usd": 280, "next_wave": "…"}`.
- The runner `git pull`s and reads it **before every submission**. Kunhao (GitHub app on his phone) or the cloud session can flip it to `pause`.
- On pause: submit nothing new; jobs already running finish on GCP; the runner keeps collecting results.
- Mac asleep or offline: running batch jobs continue on GCP; the runner picks up their results when it next runs. Use `caffeinate -i` during active waves.
- `python -m pipeline status` prints state counts, spend, ETA; the runner also writes `pipeline/STATUS.md` and commits it after every poll cycle (at most every 15 min).

## Budget control
- Read the **actual** Vertex SKU price for Claude Sonnet 5.5 (input, output, batch) at Gate 0; store it in `pipeline/config.yaml`. Don't assume Anthropic list prices.
- Compute cost from each response's usage fields; keep a running total in state.
- **Before each wave**: forecast = (pages in wave) × (measured cost per page from previous waves). Refuse to submit if `spent + forecast > max_spend_usd`.
- Also create a GCP budget with alerts at $150 / $250 / $300 on the project (if the account has billing-budget permission; otherwise ask Kunhao to create it in the console).

Rough plan (to be re-forecast after the pilot wave): P1 ≈ $105, P2 ≈ $90–115, P3 + work maps ≈ $25 → **≈ $220–250**.

## Order of work (gates)
- **Gate 0 — setup**: ADC works; one tiny online call to Sonnet 5.5 succeeds; one tiny batch job (2 requests, one with an image) round-trips; real prices recorded. Commit `pipeline/STATUS.md`.
- **Gate 1 — unit plan**: `pipeline/units.csv` (work_id, unit_id, title, pdf_pages, printed_pages, n_pages, image_pages, est_tokens, tier, field). Chapter splitting uses the PDF outline when present, else the table of contents. **Stop and wait for the cloud session's review** (`pipeline/reviews/gate1.md`).
- **Gate 2 — pilot wave** (~12 units): must include `akerlof-1970-lemons/main` and `cover-2006-elements/ch02-entropy` (we have agent-made reference digests for both in `wiki/works/` — save the pipeline versions as `*.pipeline.md` so they don't overwrite them), plus one scanned file, one prose book chapter, one philosophy text, one long math chapter, one HTML source. **Stop and wait for review** (`pipeline/reviews/gate2.md`) and Kunhao's go.
- **Waves**: core-tier works first, then deep, then reference; ~80–120 units per wave. After each wave the cloud session samples ≥ 5% (stratified by field and type) and writes `pipeline/reviews/wave-N.md`. A wave with > 10% sampled units failing review is re-run with improved prompts before continuing.

## Outputs
- `wiki/works/<work-id>/<unit-id>.md` — accepted digest (frontmatter adds `verified: pass|repaired`, `verifier_issues: N`, `pipeline_version`).
- `wiki/works/<work-id>/index.md` — work map.
- `pipeline/state/` — state log; `pipeline/STATUS.md` — human-readable progress.
- Commit after each wave (message: `digest: wave N — X units accepted`).

## Non-goals
- No concept/instance node files yet (that is the Knowledge Manager's step, after digestion).
- No changes to the library folder in Google Drive (read-only input).

---
name: handoff-local-agent
description: Cold-start brief for the local Claude Code agent that builds and runs the digest pipeline on Kunhao's Mac.
---

# Cold-start brief: AI4Read digest pipeline engineer

You are the **engineer** for the AI4Read digest pipeline. A separate Claude session in the cloud is the **quality lead**: it owns the prompts and reviews results. Kunhao Yang (assistant professor, computational social science) owns the project, the GCP project and the budget.

## 0. Where you work
- The repo is `https://github.com/CSS-Laboratory/AI4Read`. Work in a clone on the **local disk**, e.g. `~/Projects/AI4Read`. **Never** put a git repo inside the Google Drive folder (Drive sync corrupts `.git`). If you were started inside the Drive folder, clone the repo to `~/Projects/AI4Read` and work there.
- The source library is **read-only** input:
  `~/Library/CloudStorage/GoogleDrive-yangkunhao93@gmail.com/My Drive/Book/AI4Read/library/<field>/<work-id>*.pdf|.html`
  (Some files end in `.pdf.pdf`; `_incomplete/` and `_meta/` are not sources. `library/_meta/inventory.jsonl` has page and character counts.)
- Read first, in this order: `CLAUDE.md`, `CHARTER.md` (skim), `DIGEST_SPEC.md`, `pipeline/DESIGN.md` (**the spec you implement**), `pipeline/prompts/*.md`, `canon/catalog.json` (work metadata, tier, field).

## 1. Safety rules (GCP, browser, money)
- GCP project: `playground-491901` only. Do not touch other projects.
- Prefer the `gcloud` / `bq` / `gsutil` CLIs. Use Chrome only to *look* at console pages, or for a step the CLI cannot do; tell Kunhao what you will click before you do it.
- **Ask Kunhao before every command that creates, changes or deletes a cloud resource or IAM binding, or that can cost money** (enabling APIs, creating buckets, submitting batch jobs). Read-only commands need no approval.
- Authentication: Kunhao runs `gcloud auth login` and `gcloud auth application-default login` himself. Never type, read, store or print passwords, tokens or keys. **Do not create service-account keys.**
- Never delete files in the library or in the repo's `wiki/` without asking.
- Budget: **$300 total, hard stop at $280** (see DESIGN.md "Budget control"). If a forecast would exceed it, stop and report.

## 2. Division of labour
- You own: `pipeline/*.py` (or a `pipeline/` package), `pipeline/config.yaml`, `pipeline/state/`, `pipeline/STATUS.md`, tests, GCP setup.
- The quality lead owns: `DIGEST_SPEC.md`, `pipeline/prompts/*.md`, `pipeline/reviews/*.md`. Don't edit these; put suggestions in `pipeline/reviews/prompt-proposals.md`.
- Talk through the repo: commit and push often. Check `pipeline/reviews/` and `pipeline/control.json` after every `git pull`.

## 3. Tasks

### Gate 0 — setup and smoke test
1. Check tools: Homebrew, Python ≥ 3.11 (`uv` preferred), `gcloud`, `poppler` (`pdftotext`, `pdftoppm`, `pdfinfo`), Node (for a KaTeX check). Install what is missing (ask first).
2. Have Kunhao log in (ADC). Confirm `gcloud config get project` = `playground-491901`.
3. Research the current docs and record findings in `pipeline/NOTES.md` with links:
   - the exact Vertex model id for Claude Sonnet 5.5 and whether it supports the **global** endpoint;
   - how **batch prediction** works for Claude on Vertex (BigQuery or GCS JSONL input, request format, supported regions/global, limits on request size and on images per request, turnaround);
   - whether image blocks (base64) are allowed in batch requests;
   - the **actual** Vertex price for Sonnet 5.5 (standard and batch), from the pricing page or Cloud Billing SKUs.
4. With approval: enable needed APIs; create a bucket `gs://ai4read-batch-<suffix>` (or a BigQuery dataset, whichever batch needs) in the right location; set a budget with alerts at $150/$250/$300 (CLI if permitted; otherwise ask Kunhao to create it in the console).
5. Smoke test: one online request (text only, a few tokens) and one batch job with 2 tiny requests (one with an image). Record tokens and cost.
6. Write `pipeline/config.yaml` (model id, endpoint, prices, bucket, paths, `max_spend_usd: 280`) and push. Update `pipeline/STATUS.md`.

### Gate 1 — unit plan (then STOP)
Implement the unit planner: list works from the library, match them to `canon/catalog.json` ids (prefix match on the file stem; note duplicates such as two Osborne files and two Shiller files: keep both as separate works only if their catalog ids differ, otherwise report), split books into chapters using the PDF outline or the table of contents, split chapters longer than ~35 pages at section boundaries, detect image pages (see DESIGN.md), estimate tokens and cost. Write `pipeline/units.csv` and a short summary in `pipeline/STATUS.md`, push, and **stop**. Wait for `pipeline/reviews/gate1.md` from the quality lead.

### Gate 2 — pilot wave (then STOP)
Build the passes (P1 digest, P2 verify, P3 re-digest, deterministic checks, P4 work map) and the state machine exactly as in DESIGN.md. Template the prompts: `{{DIGEST_SPEC}}` = contents of `DIGEST_SPEC.md`; `{{CONCEPT_SPINE}}` = the "Concept spine" section of `canon/<field>.md` for the work's first field. Run the pilot wave from DESIGN.md (save the two reference units as `*.pipeline.md`). Record measured cost per page and a forecast for the full run. Push and **stop**. Wait for `pipeline/reviews/gate2.md` and Kunhao's go.

### Waves
Run waves in tier order (core → deep → reference). After each wave: commit accepted digests, `pipeline/STATUS.md`, and the state log; then wait for the quality lead's `pipeline/reviews/wave-N.md` **only if** `control.json` says `"review_each_wave": true`; otherwise continue.

## 4. Resumability requirements (must have)
- Append-only state log `pipeline/state/units.jsonl`; idempotent re-runs keyed by `unit_id + content_hash + spec_version`.
- The runner `git pull`s and reads `pipeline/control.json` before every submission; `pause` = submit nothing new but keep collecting finished jobs; `stop` = exit cleanly.
- Safe to kill at any moment (Ctrl-C, sleep, reboot). Re-running `python -m pipeline run` continues where it stopped.
- `python -m pipeline status` shows counts by state, spend vs budget, and ETA.
- Run active waves under `caffeinate -i`.

## 5. Definition of done (per gate)
- Gate 0: smoke test passed, prices recorded, budget alert exists, NOTES.md has doc links.
- Gate 1: `units.csv` covers every library source file (or lists why it is skipped).
- Gate 2: ~12 pilot units through P1–P2 (+P3 where needed), deterministic checks pass, cost forecast written.
- Final: every unit `accepted` or `needs_human`, a work map for every book, total spend ≤ $280, everything pushed.

Keep `pipeline/STATUS.md` short and readable on a phone: current gate/wave, counts, spend, next action, blockers.

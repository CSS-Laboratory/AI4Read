---
name: wave1-decision-brief
description: Everything the project manager needs to decide whether to start digest wave 1. Entry point; links to all detailed results.
date: 2026-10-13
author: engineer (local Claude Code agent)
---

# Decision brief — start wave 1?

## The decisions requested
1. **Go / no-go for wave 1** — 107 core units (12 whole works), ≈ **$27** incl. retries, ≈ 1–2 h on GCP.
   Engineer's recommendation: **go** (pipeline proven on the pilot; wave 1 is affordable under any scope option below).
2. **Budget or scope for the full run — needed before the later waves, not before wave 1.**
   The library grew today (new field **control theory**, + Lycan's real PDF): full-run forecast is now **≈ $313–328 vs the $280 hard stop**.

| Option | Forecast (incl. 10–15% retries) | Fits $280? |
|---|---|---|
| A. Everything (1,339 units) | $313–328 | no — runner stops at $280; the reference tier's tail is cut |
| B. Defer the reference tier (163 units, 9 works) | $262–274 | yes |
| C. Raise the cap to ≈ $340 (≈ ¥54,000 budget) | $313–328 | yes |
| D. Shorter digests via prompt change (quality lead), then re-forecast | unknown (each −20% P1 output ≈ −$20) | maybe |

Order of work is core → deep → reference, so with option A nothing important is lost first.
Spent so far: **$5.88** (pilot $3.90, A/B test $1.98, smoke tests < $0.01).

## Where we are
| Gate | Status | Detail |
|---|---|---|
| 0 — setup | ✅ | Vertex Claude Sonnet 5.5; ADC auth; bucket `gs://ai4read-batch-628671`; budget ¥48,000 with alerts. **Batch runs in `us-east5`** (the `us` multi-region fails Claude batch jobs with `INTERNAL`, 5/5 tests). `pipeline/NOTES.md` |
| 1 — unit plan | ✅ approved (`reviews/gate1.md`) | `pipeline/units.csv`: 1,339 digest units, 24,977 pages, 184 works; 29 reviewed tables of contents in `pipeline/toc/`. `pipeline/GATE1.md` |
| 2 — pilot | ✅ done; **quality-lead review `reviews/gate2.md` not yet written** | 11/11 units accepted. `pipeline/GATE2.md` |
| A/B cost test | ✅ done (Kunhao: quality first) | `pipeline/GATE2.md` § A/B, `pipeline/results/ab_results.csv` |

## Pilot results (11 units, 213 pages, $3.90)
- All 11 accepted. First verifier (P2) verdicts: 6 pass (with minor edits), 5 repair; none failed outright.
- Typical serious issues the verifier caught and fixed: claims stronger than the source, a reversed claim (Dennett), a mis-stated probability (MacKay), page-reference drift on scanned spreads.
- Two extra loops were caused by the engineer's checker (false positives) — fixed.
- Batch turnaround: P1 22 min, P2 12 min for 11 units.
- Per unit: `pipeline/results/pilot_units.csv`; digests in `wiki/works/` (the two reference units as `*.pipeline.md` beside the hand-made references, for comparison).

## Decisions already taken (from the A/B test)
| Lever | Result | Decision |
|---|---|---|
| Verify (P2) at effort `medium`/`low` | Much cheaper (almost no thinking) but **missed real errors** `high` caught (Dennett critical, Kahneman major, MacKay major) | **Keep P2 at `high`** |
| Digest (P1) images 1200 px instead of 1500 | No math-reading errors; equation coverage equal; P1 input −20–33% | **P1 at 1200 px; P2 stays 1500 px** |
| Engineering fixes | Printed labels for scanned spreads; whitespace-tolerant verifier edits; failed edits → batch fix pass instead of online | Done |

## Cost model (measured, used for all forecasts)
- First pass (P1 + P2): **$0.0086 / text page, $0.0149 / image page** (minus ≈ $0.0008 per image page from the 1200-px change).
- Thinking ≈ 17% of P1 output and ≈ 71% of P2 output (kept: needed for quality).
- Retries/fixes estimated at +10–15% (pilot: +40%, inflated by the now-fixed checker false positives).

| Tier | Units | Pages | Image pages | First pass |
|---|---|---|---|---|
| core | 1,031 | 19,123 | 8,320 | $210 |
| deep | 145 | 2,314 | 1,548 | $28 |
| reference | 163 | 3,540 | 2,989 | $47 |
| **total** | **1,339** | **24,977** | **12,857** | **$285** |

Control theory (new today): 128 units, 2,852 pages, ≈ $36 of the total.

## Wave 1 (proposed, `pipeline/waves/wave1.txt`)
107 core units, 12 whole works, one or two per field: Gettier 1963, Blei 2017, Carey 1989, Anderson 1972, Ashby 1956, Axelrod 1984, Cover & Thomas (rest of the book), Axler 2024, Argyle 2023, Achen & Bartels 2016, Apperly 2009, Godfrey-Smith 2003. 2,103 pages, ≈ $24 first pass.
How it runs: `control.json` → `"mode": "run", "next_wave": "wave1"`; the runner (`python -m pipeline run wave1`) submits P1 → P2 → fix/P3 as batch jobs, writes accepted digests to `wiki/works/`, commits `STATUS.md` at least every 15 min, and refuses any job that would pass the $280 cap. Pause any time by setting `"mode": "pause"` (GitHub app is fine). `review_each_wave: true` → it stops after the wave for `reviews/wave-1.md`.

## Risks and open items
- **Quality-lead review of Gate 2** (`reviews/gate2.md`) is not written yet; DESIGN.md requires it plus Kunhao's go. Prompt suggestions waiting for the quality lead: `pipeline/reviews/prompt-proposals.md` (hard limits, HTML citations, keep hedges, no outside knowledge).
- **Main remaining error type:** the digest adding claims beyond the source. The verifier catches them at a cost; a prompt fix would cut both errors and spend.
- **Budget:** the cap is in USD in our code, but GCP bills in JPY (budget ¥48,000 ≈ $300 at 160). Watch the budget alerts.
- **Library changes** after planning need a re-plan (`python -m pipeline plan`) — done today for control theory and Lycan.
- Work maps (P4, one per book) are not built yet (≈ $3 total); planned after each work's units are accepted.
- HTML stubs still without full text: Nash 1950, Aumann 1976, Kullback 1951, Jara-Ettinger 2016 (skipped until PDFs arrive).

## File index
| File | What |
|---|---|
| `pipeline/STATUS.md` | phone-readable status |
| `pipeline/GATE2.md` | pilot + A/B report (full) |
| `pipeline/GATE1.md`, `pipeline/units.csv` | unit plan |
| `pipeline/NOTES.md` | GCP research, prices, batch debugging history |
| `pipeline/results/pilot_units.csv` | per-unit tokens, cost, verdicts (pilot) |
| `pipeline/results/ab_results.csv` | A/B arms per unit (verdict, issue counts, tokens, cost) |
| `pipeline/results/pilot/`, `pipeline/results/ab/` | raw model outputs (P1 digests, P2 verdicts) |
| `pipeline/state/units.jsonl`, `spend.jsonl`, `jobs.jsonl`, `ab.jsonl` | append-only logs |
| `pipeline/waves/pilot.txt`, `pipeline/waves/wave1.txt` | wave unit lists |
| `pipeline/reviews/prompt-proposals.md` | engineer → quality lead suggestions |

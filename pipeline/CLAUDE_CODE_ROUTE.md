---
name: claude-code-route
description: Spec for digesting the deep and reference tiers with Claude Code's own Sonnet subagents on Kunhao's Mac, every Thursday afternoon, using leftover weekly subscription usage. Read before building or running it.
status: approved in principle 2026-10-14 (Kunhao); parity test required before scaling
---

# Claude Code route (deep + reference tiers)

## Why
Vertex budget covers the core tier only (≈ $315–325). The deep (145 units) and reference (162 units) tiers — ≈ 5,850 pages — run on Kunhao's Claude subscription instead, every **Thursday afternoon** before his weekly usage resets at **21:00 JST**, so they use usage that would otherwise expire.

## Principle: same pipeline, different model call
Reuse everything except the Vertex call:
- the unit plan (`pipeline/units.csv`), page rendering (1200 px for P1, 1500 px for P2) and printed labels;
- the prompts `pipeline/prompts/digest.md` and `verify.md` (templated exactly as in the batch path, incl. `{{MANDATORY_ITEMS}}`, `{{TARGET_WORDS}}`);
- deterministic checks (`checks.py`), edit application, fix pass, residue stripping;
- the state log (`pipeline/state/units.jsonl`) with `route: claude-code`.

Only P1 / P2 / P3 calls change: each becomes a **fresh Sonnet subagent** (Claude Code Task/Agent with model `sonnet`), given the rendered prompt and the page images/text as files to read. **P1 and P2 must be different subagents with no shared context** (independence of the checker is the point).

## Run shape
- Trigger: macOS `launchd` job (or Claude Code's own scheduler if available) that starts headless Claude Code on Thursdays at **13:00 JST** in `~/code/AI4Read` with a fixed prompt: "run `python -m pipeline cc-run --until 20:30`".
- `cc-run`: pull; read `control.json` (respect `pause`/`stop`); pick the next units in tier order (deep → reference; within a tier, prefer works linked to upcoming posts if `pipeline/waves/priority.txt` exists); process unit by unit (P1 → checks → P2 → edits → fix/P3 as in the batch path); commit + push after each accepted unit; stop cleanly at 20:30 or when Claude Code reports a usage limit.
- Resumable: a unit is "in progress" only in memory; an interrupted unit is redone from P1 next week. Never partially write a digest file.
- Needs the Mac awake (`caffeinate -i` for the run) and Google Drive synced.
- Permissions: run with an allow-list limited to reading the library folder, writing inside the repo, `git`, and the pipeline's Python; no network except git push.

## Parity test (before scaling) — Gate CC
Run the Claude Code route on 3 units already done and audited in the batch path (e.g. `kuhn-1962-structure/ch09-nature`, `gelman-2013-bda3/ch05-hierarchical`, `dennett-1987-intentional-stance/ch02-true`), saving outputs as `*.cc.md` (do not overwrite). Report: verifier issue counts by kind, `<h_checks>` not-ok rate, length vs target, wall time, and the share of weekly usage consumed (Kunhao reads the usage meter before/after). The quality lead compares them with the batch versions and the audits before the first real Thursday run.

## Reporting
`pipeline/STATUS.md` gets a "Claude Code route" block: units done this week / total, last run time, stop reason, issues.

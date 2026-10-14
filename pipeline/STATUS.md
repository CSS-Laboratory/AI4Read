# Digest pipeline — status

- **Wave:** `wave3` — 375 units · accepted 370 · p1_submitted 1 · p2_submitted 4
- **Mode:** run
- **Spent:** $223.23 of $325 cap
- **Jobs running:** 2 (p3, p2)
- **All units:** accepted 691 · p1_submitted 1 · p2_submitted 4 · planned 1
- **Updated:** 2026-10-14 15:26

- **Wave 3:** 375 core units (363 + 12 Ashby re-runs with spread splitting), 26 works, 5,433 pages · est ≈ $89 (v2.2 rates).
- **Wave 4 (planned):** 336 core units, 41 works, 6,684 pages · est ≈ $105. Waves 3+4 + spent ≈ $317 vs $325 cap.
- GCP budget alert raised to ¥53,000 (Kunhao, 2026-10-14).
- Claude Code route (deep + reference): being built; no model calls until the parity test (Gate CC).
- **Claude Code route built (not run):** `python -m pipeline cc-run [--until 20:30] [--units …] [--suffix .cc.md] [--dry-run]`; each pass = fresh `claude -p --model sonnet` (Read-only tools, restricted, no MCP, subscription auth — never `--bare`); state log with `route: claude-code`; commit+push per accepted unit; stops at time / pause / usage limit. Queue: 307 units (deep 145 → reference 162). launchd job written to `pipeline/launchd/` (Thursdays 13:00) — **not installed**. Dry run OK (no model call). **Next: Gate CC parity test — waiting for Kunhao.**

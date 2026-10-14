# Gate CC — Claude Code route parity test

Route: every pass = a fresh `claude -p --model sonnet` session (Read-only tools, restricted, no MCP), subscription auth; same prompts v2.2, length target, checks, edit handling and state machine as the batch path. Parity outputs: `*.cc.md` next to the batch files (nothing overwritten).

## Parity units (also done in batch and hand-audited)

| Unit | Result | Sessions | Wall time | Words vs target | Verifier, first pass | h_checks not ok (first) | Batch: words · verifier | Batch audited |
|---|---|---|---|---|---|---|---|---|
| `kuhn-1962-structure/ch09-nature` | accepted (repaired) | 2 (p1×1, p2×1) | 12.5 min | 3739 / 2015 = 1.86× | repair · 2c/1M/6m (faithfulness 3, coverage 1, format 1, strength/voice 3) | 5/78 (6%) | 4533 words · repair · 7c/4M/4m (faithfulness 1, math 1, pages 1, coverage 1, format 1, strength/voice 10) | yes |
| `gelman-2013-bda3/ch05-hierarchical` | accepted (repaired) | 6 (p1×1, p2×3, p3×2) | 40.7 min | 5891 / 6000 = 0.98× | pass · 0c/0M/5m (labels 1, format 1, strength/voice 2) | 5/73 (7%) | 7381 words · repair · 9c/2M/7m (faithfulness 3, labels 1, format 2, strength/voice 12) | yes |
| `dennett-1987-intentional-stance/ch02-true` | accepted (repaired) | 2 (p1×1, p2×1) | 14.8 min | 6520 / 5670 = 1.15× | repair · 4c/0M/5m (math 2, pages 1, format 1, strength/voice 4) | 8/119 (7%) | 6557 words · repair · 9c/2M/6m (faithfulness 5, format 2, strength/voice 10) | yes |

## needs-review re-checks (normal route; written in place only if all checks pass)

| Unit | Result | Sessions | Wall time | Words vs target | Verifier, first pass | h_checks not ok |
|---|---|---|---|---|---|---|
| `meadows-2008-thinking/ch02-note` | accepted (repaired) | 3 (p1×1, p2×1, p2fix×1) | 19.7 min | 1923 / 1000 = 1.92× | repair · 2c/0M/7m (faithfulness 3, format 1, strength/voice 5) | 11/46 (24%) |
| `popper-1959-logic/front-preface-2` | accepted (repaired) | 4 (p1×1, p2×2, p3×1) | 29.5 min | 3211 / 1344 = 2.39× | repair · 9c/4M/4m (faithfulness 5, pages 1, coverage 1, format 1, strength/voice 9) | 26/77 (34%) |

## Totals
- Sessions: 17 · model wall time 117 min (≈ 23 min per unit, sequential)
- Tokens reported by Claude Code: input 270 · cache read 7,655,744 · cache write 1,211,897 · output 703,838
- **Weekly usage meter (Kunhao): 43% → 45%**

## Reading the results (engineer)
- **All 5 units accepted.** Parity outputs: `wiki/works/kuhn-1962-structure/ch09-nature.cc.md`, `gelman-2013-bda3/ch05-hierarchical.cc.md`, `dennett-1987-intentional-stance/ch02-true.cc.md` (batch + audited files untouched). The 2 needs-review units passed all checks and were written in place (`verified: repaired`); `cc_recheck.txt` is done.
- **Usage:** 43% → 45% of the weekly meter for 17 sessions (this also includes the coordinating session). ≈ 0.3–0.4% per unit → deep + reference (307 units) ≈ 90–125% of one week's allowance in total.
- **Wall time is the bottleneck, not usage:** a clean unit takes 12–15 min (one P1 + one P2 session, sequential); ≈ 25–35 units per Thursday window (13:00–20:30) → ≈ 9–12 Thursdays for 307 units. Running 2–3 units in parallel would cut this proportionally (usage per Thursday ≈ 10–15% at that pace).
- **Verifier strength — needs the quality lead's comparison:** on first pass the Claude Code verifier reports far fewer criticals than the batch verifier on the same units (Kuhn 2c vs 7c; Gelman `pass` with 0c vs 9c; Dennett 4c vs 9c). Either the CC digests are cleaner or the CC verifier checks less deeply (Claude Code does not report thinking tokens, so this cannot be told from usage). The hand-audited batch files are the yardstick.
- **Length:** CC digests overshoot the target like the batch ones (Kuhn 1.86×, Meadows 1.92×, Popper 2.39×; Gelman 0.98×, Dennett 1.15×).

## Engineering issues found during the test (fixed or noted)
- **Narration before the frontmatter** ("All confirmed. I now have complete grounding to write the digest.") broke the frontmatter check and caused Gelman's 2 extra re-digests (≈ 25 min). Fixed: text before the `---` that opens the frontmatter is dropped (`8bae57d`). Dennett and the re-checks ran with the fix.
- **Popper:** one verifier output could not be parsed → re-digest (old rule). A Claude Code result has no `stop_reason`, so truncation cannot be told apart from a format slip; next step would be to rerun P2 (not P3) for any unparseable verifier output on this route.
- `CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000` is set for every session (verifier with ≤ 120 h_checks).
- launchd job (Thursdays 13:00) is still **not installed**.

# Wave 4 review — quality lead (2026-10-14) · core tier complete

**Verdict: accepted. The core tier (1,031 units, $322.95) is done.** Proceed to the Claude Code parity test (Gate CC).

## Audit (10 units ≈ 3%; reports `pipeline/reviews/audit/wave4-*.md`)
| Unit | Crit | Major | Minor | Coverage |
|---|---|---|---|---|
| Sutton & Barto ch. 9 p2 | 1 | 3 | 7 | complete |
| McElreath ch. 7 p2 | 2 | 2 | 6 | complete |
| Strogatz ch. 7 p2 | 0 | 1 | 5 | complete (0.69× target) |
| Shannon 1951 | 1 | 2 | 4 | complete |
| Xie et al. 2022 | 0 | 2 | 4 | complete |
| Schelling ch. 8 | 0 | 4 | 10 | one key argument missing (p. 232) → fixed |
| Zaller ch. 8 | 0 | 1 | 9 | complete |
| Quine 1951 | 0 | 3 | 10 | complete |
| Pearl & Mackenzie ch. 6 | 0 | 1 | 7 | complete |
| Rogers ch. 6 p1 | 0 | 3 | 10 | complete |

- **Shorter target did not cost coverage**: 9/10 complete; the one gap fixed by hand.
- ≈ 0.4 critical per unit, all in summary lines (L3 correct). Equations, toy examples, added steps all correct.
- All critical/major errors fixed by hand (90 fixes; `audit/wave4-fixes.md`).
- **Edition note**: `mcelreath-2020-rethinking` PDF is the **1st edition** (2016), not the 2nd; digests now say so. Catalog id kept.

## Core tier — summary across all audits
| Wave | Units audited | Crit / unit | Major / unit |
|---|---|---|---|
| Pilot (v1) | 8 | 0.50 | 1.5 |
| 1 (v2.1) | 12 | 0.50 | 1.3 |
| 2 (v2.2) | 13 | 0.54 | 1.8 |
| 3 (v2.2) | 10 | 0.30 | 2.3 |
| 4 (v2.2, shorter) | 10 | 0.40 | 2.2 |
45 audited digests carry `audited: 2026-10-14` (hand-fixed). The rest carry the model-verified status; CHARTER §9 applies (claims re-checked against the page when used in a post).

## Gate CC — parity test (next)
Per `pipeline/CLAUDE_CODE_ROUTE.md`, with these specifics:
- Units (already audited in the batch path, so we can compare): `kuhn-1962-structure/ch09-nature`, `gelman-2013-bda3/ch05-hierarchical`, `dennett-1987-intentional-stance/ch02-true`. Write outputs as `*.cc.md` next to the batch versions; never overwrite.
- Plus the 2 `needs-review` units (`pipeline/waves/cc_recheck.txt`), written in place only if they pass all checks.
- Use the current prompts (v2.2) and the current length target; P1 and P2 in separate fresh Sonnet subagents.
- Kunhao notes his weekly usage meter before and after; record wall time per unit.
- Report in `pipeline/GATE-CC.md`: per unit — verifier issues by kind, `<h_checks>` not-ok rate, length vs target, wall time; total usage share. Then stop for the quality lead.

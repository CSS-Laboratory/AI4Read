# Gate CC review — quality lead (2026-10-14)

**Verdict: not yet at parity.** Do not install the Thursday job yet. Decision on the route is pending with Kunhao.

## Evidence (audit: `pipeline/reviews/audit/gate-cc.md`)
| Unit | Batch residual (pre-fix) C/M | Claude Code route C/M |
|---|---|---|
| Kuhn ch. IX | 0 / 5 | 1 / 9 |
| Gelman ch. 5 | 0 / 2 | 2 / 5 |
| Dennett ch. 2 | 0 / 1 | 1 / 3 |
| Meadows note | — | 1 / 2 |
| Popper 1959 preface | — | 1 / 2 |

- At 17 of the 21 new critical/major spots, the batch digest was correct → the CC route is genuinely weaker, not just audited more harshly.
- Pattern: hedges dropped inside L3, voice errors (3 of 5 units), invented "because" links, and a **shallower verifier** (Gelman passed first time with a wrong ANOVA cell; first-pass critical counts were ~½ of the batch verifier's on the same units).
- Usage is cheap: 43% → 45% of the weekly meter for 5 units (≈ 0.3–0.4% per unit).

## Likely causes (to test, if the route is kept)
1. **Thinking depth**: batch P2 runs at effort `high` with 15–50k thinking tokens; `claude -p` sessions may run with less. Set the highest effort / thinking budget the CLI allows for every session and confirm it in the transcript.
2. **Selective page reading**: in the batch path the verifier receives every page image; a Claude Code agent chooses what to Read. Require P2 to Read every page image in order and check the transcript's Read calls (count = pages) before accepting.
3. **Verifier model**: use **Opus** for P2 (stronger, independent from the Sonnet digester); usage cost stays modest at current rates.

## Options for Kunhao
- **A. Fix the CC route, then re-test** (items 1–3) on the same 3 parity units; scale only if residuals ≤ batch. Cost: one more test round + audit; usage per unit rises (Opus verifier).
- **B. Finish deep (145 units, ≈ $33) on Vertex** with the proven route; reference tier (162 units) stays just-in-time: digested via A when a post needs it.
- **C. Finish deep + reference on Vertex (≈ $85)**, then use Thursday leftover usage for work that needs Claude anyway: summary-line re-checks across core digests, the knowledge graph, and posts.

## Decision (Kunhao, 2026-10-14): option C
- Finish **deep (145 units) and reference (162 units) on Vertex** with the proven route (prompts v2.2, current length target).
- Estimate: deep $33–44, reference $52–71 (reference is image-heavy: Murphy PML2, Polyanskiy–Wu, Bertsekas, Prince, Särkkä) → total ≈ **$410–440**. Hard stop **$445**.
- Order: wave 5 = all deep; wave 6 = all reference. `review_each_wave: true` (≈ 3% audit each).
- Claude Code route: parked. Thursday spare usage goes to (1) a summary-line re-check of core digests, (2) the knowledge graph, (3) posts — specs to follow from the quality lead.

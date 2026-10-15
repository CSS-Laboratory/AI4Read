---
name: digestion-report
description: Final report of the one-off digestion of the AI4Read library (Oct 2026): what exists, how good it is, what it cost, and how to use it safely.
date: 2026-10-15
---

# Digestion report

## What exists
- **1,339 digests** in `wiki/works/<work>/<unit>.md` covering **177 works** in 12 fields (core 1,031 · deep 145 · reference 163), ≈ 5.0 M words, spec v1.2 / prompts v2.2 (earliest wave-1 units v2.1).
- Every digest: L0–L3 progressive disclosure, Prerequisites, printed-page citations (or § / headings; `(pdf N)` only where the source shows no page numbers), toy example, concepts, instances, candidate bridges, questions, reading notes, and exercises for textbooks.
- **56 digests hand-audited and corrected** against page images (`audited:` in frontmatter).

## Quality (independent audits, 64 units, ≈ 5%)
| Wave | Critical / unit | Major / unit |
|---|---|---|
| Pilot (v1) | 0.50 | 1.5 |
| 1 | 0.50 | 1.3 |
| 2 | 0.54 | 1.8 |
| 3 | 0.30 | 2.3 |
| 4 | 0.40 | 2.2 |
| 5 (deep) | 0.33 | 1.8 |
| 6 (reference) | 0.80 | 2.0 |

- **Math, equations, tables, numbers, toy examples: near-perfect** across all audits.
- **Residual risk ≈ 0.4 critical per unit**, concentrated in **summary lines** (L0–L2, Concepts/Instances): dropped conditions or hedges, occasional voice slips. L3 walkthroughs are usually right where summaries are wrong.
- Usage rule (CHARTER §9): any claim used in a post is re-checked against the cited page.

## Cost
Vertex AI (Claude Sonnet 5.5, batch, `us-east5`): **$433.74** of a $445 cap — pilot/tests ≈ $16, core $322 (waves 1–4), deep $44, reference $66. Plus quality-lead audits on the subscription.

## Known gaps
- Not digested: Nash 1950, Aumann 1976, Kullback & Leibler 1951 full text, Jara-Ettinger 2016 (HTML stubs; PDFs missing), Bayes Rules! (online book), Shannon & Weaver book (duplicate of Shannon 1948), Shiller 2017 paper (book covers it).
- Editions differing from the catalog: Cover & Thomas 1st ed. (1991), Pierce 1961, McElreath 1st ed., Osborne draft, Clark 2nd ed., Hernán online 2026, Wittgenstein PI 4th ed.
- Work maps (P4, one `index.md` per book) not yet built.
- Claude Code route parked (below parity, `pipeline/reviews/gate-cc.md`).

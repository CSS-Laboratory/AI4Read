# Notes: Lens 3 (sonnet)

**Checked in code** (scratchpad lens3.py): posterior 4^n/(4^n+1) with exact fractions for n=0..8; P(right) 0.5/0.74/0.853/0.888/0.897 (matches W4); n=2 hand arithmetic (0.02, 0.00125, 0.941, odds 16); r = ln(0.05/0.2) = -1.386 so e^{nr} = 4^-n; Monte Carlo conditioning check (0.80, 0.94, 0.98); prior sensitivity (0.1, 0.01, 0). Word count about 986 incl. table and cites, excl. display math and the dev comment.

**Relied on:** xie-2022-icl/main.md (pp. 1-4 setting, eq. 1 p. 2, eqs. 5-6 p. 5-6, Cond. 1 and Thm 1 p. 7, GINC p. 10, "first step" p. 12); brown-2020-gpt3 main-p1 (pp. 4, 24) and main-p2 (p. 34); source-brief item 12 and cross-source tension 4; bayes-theorem hub (Gelman 2013, p. 7).

**Unsure:** (1) p. 6 vs pp. 5-6 for the e^{n r_n} weight (brief says p. 6, digest puts eqs. 5-6 on pp. 5-6). (2) "glued-together examples look odd" is my plain-words paraphrase of the mismatch and delimiter error terms (pp. 4, 7). (3) "4-layer Transformer" for the ablations is from the digest. (4) Gelman p. 7 is via the hub quote, not read at source. (5) Link type split (same-math inside the model, structural analogy for real LLMs) is my judgement. (6) The toy "concept B = occupation" is ours and not Xie's. (7) Dropped the "longer examples help" bullet for length. All claims need the usual source-page recheck.

**Interactive spec:** in the HTML comment after the figure.

**Effort:** about 8 tool calls and 3 writes; roughly 5 minutes wall clock.

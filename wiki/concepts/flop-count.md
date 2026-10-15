---
id: flop-count
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch03-norm]
generated_by: build_kg.py
---

# flop-count

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 441): approximate number of arithmetic operations, lower-order terms dropped [new]
- [[boyd-2018-vmls/ch03-norm]] (p. 63): number of arithmetic operations; norm 2n, correlation 10n [new]

## Candidate bridges

- [same-math] Compute accounting (2 flops × 3 for backward = 6 per parameter per token) ↔ llm: compute-optimal training — the same per-token flop count is used to budget compute versus data. — from [[brown-2020-gpt3/main-p2]] (llm → llm)

---
id: flop-count
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 4
n_works: 1
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch05-linear]
aliases: [flop-count-complexity]
generated_by: build_kg.py
---

# flop-count

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `flop-count-complexity` — 2 digest(s)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/app-appendices]] (p. 441): approximate number of arithmetic operations, lower-order terms dropped [new]
- [[boyd-2018-vmls/ch01-vectors]] (pp. 23–24): number of floating point operations of a specific method, simplified to leading order [alias `flop-count-complexity`; new]
- [[boyd-2018-vmls/ch03-norm]] (p. 63): number of arithmetic operations; norm 2n, correlation 10n [new]
- [[boyd-2018-vmls/ch05-linear]] (p. 102): operation count; Gram–Schmidt is about $2nk^2$ [alias `flop-count-complexity`; new]

## Candidate bridges

- [same-math] Compute accounting (2 flops × 3 for backward = 6 per parameter per token) ↔ llm: compute-optimal training — the same per-token flop count is used to budget compute versus data. — from [[brown-2020-gpt3/main-p2]] (llm → llm)

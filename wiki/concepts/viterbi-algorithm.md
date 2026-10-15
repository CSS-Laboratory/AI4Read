---
id: viterbi-algorithm
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 2
n_works: 2
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch09-message, sarkka-2023-bayesianfiltering/ch12-bayesian]
generated_by: build_kg.py
---

# viterbi-algorithm

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch09-message]] (pp. 409–410): max-product version of the forwards pass plus traceback; finds the MAP path (pp. 409–410) (new)

### control-theory

- [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (p. 263): recursion for the MAP path: forward pass for $V_k$, backward argmax pass [new; work fields: control-theory, bayesian]

## Instances that use it

- [[viterbi-algorithm]] — entries 12.9, 12.10 — from [[sarkka-2023-bayesianfiltering/ch21-list]]

## Candidate bridges

- [same-math] Viterbi algorithm ↔ HMM MAP smoothing — the text states this identification (p. 6). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
- [structural-analogy] Viterbi algorithm (12.9) ↔ control theory: principle of optimality — both build a best path recursively. — from [[sarkka-2023-bayesianfiltering/ch21-list]] (control-theory → control-theory)

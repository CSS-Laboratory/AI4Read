---
id: cross-entropy-method
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p4, murphy-2023-pml2/ch06-optimization-p2]
generated_by: build_kg.py
---

# cross-entropy-method

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 312): EDA with a Gaussian fitted to the top $K$ samples [new]

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p4]] (pp. 427–428): random search that re-centres on accepted low-cost samples [new]

## Instances that use it

- [[tetris-cross-entropy]] — cross-entropy method used with impressive success — from [[bertsekas-2026-rlcourse/ch03-learning-p4]]

## Candidate bridges

- [structural-analogy] cross-entropy method ↔ evolutionary search: a population is resampled around the best members. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other)
- [structural-analogy] Rare-event thresholding in SMC ↔ cross-entropy method — same stepwise-threshold idea, different move mechanism (p. 569). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → unspecified)

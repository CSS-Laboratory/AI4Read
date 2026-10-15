---
id: bits-back-coding
type: concept
fields: [bayesian, information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch28-model, murphy-2023-pml2/ch05-information-p2]
generated_by: build_kg.py
---

# bits-back-coding

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (p. 250): argument that randomness used to sample the code can be recovered, so the cost is a KL rate [new]

### information-theory

- [[mackay-2003-information/ch28-model]] (p. 353): send a posterior sample, then recover its random bits; net cost $-\log P(D\mid H)$ plus a constant [new]

## Candidate bridges

- [structural-analogy] Mixture code with $\log K$-bit header and incompleteness ↔ Bayesian: model averaging over $K$ models with a uniform prior. The source only points to bits-back coding (p. 108), so the link is ours. — from [[mackay-2003-information/ch05-symbol]] (information-theory → bayesian)

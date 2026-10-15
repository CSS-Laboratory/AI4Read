---
id: wasserstein-distance
type: concept
fields: [bayesian, llm]
fields_strong: [bayesian, llm]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p3, prince-2023-udl/ch15-generative]
generated_by: build_kg.py
---

# wasserstein-distance

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p3]] (p. 317): $W_p$: optimal Kantorovich value for cost $d^p$, then the $1/p$ power [new]

### llm

- [[prince-2023-udl/ch15-generative]] (pp. 284, 286): cost of moving mass to turn one distribution into another; WGAN needs discriminator Lipschitz constant < 1 [new]

## Candidate bridges

- [same-math] TV coupling form (7.20) ↔ optimal transport: Wasserstein distance with Hamming cost. — from [[polyanskiy-2025-information/ch08-f-p1]] (information-theory → other:optimal-transport)

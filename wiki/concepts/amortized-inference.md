---
id: amortized-inference
type: concept
fields: [bayesian, llm]
fields_strong: [bayesian, llm]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch21-variational]
generated_by: build_kg.py
---

# amortized-inference

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch10-variational-p1]] (p. 444): an inference network predicts local variational parameters from x [new]
- [[murphy-2023-pml2/ch21-variational]] (p. 791): one network $q_\phi(z|x)$ gives the approximate posterior for any $x$ [new; work fields: bayesian, llm]

## Candidate bridges

- [metaphor] Amortized inference network ↔ learning to learn: one shared model replaces per-example optimization. — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → bayesian)
- [structural-analogy] Amortized inference network ↔ rational analysis: a learned procedure approximately inverts the generative model of the environment. — from [[murphy-2023-pml2/ch21-variational]] (bayesian → bayesian)

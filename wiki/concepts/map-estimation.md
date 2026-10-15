---
id: map-estimation
type: concept
fields: [linear-algebra, llm]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch09-linear, prince-2023-udl/ch09-regularization]
generated_by: build_kg.py
---

# map-estimation

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch09-linear]] (pp. 300–301): maximize the posterior $p(\theta\mid\mathcal X,\mathcal Y)$; a compromise between prior and likelihood [new]

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 140): maximizing prior × likelihood; the penalty is $-\log Pr(\phi)$ [new]

## Candidate bridges

- [same-math] Optimal block decoder argmax P(s|y) ↔ bayesian: MAP estimation with the codeword as the hypothesis and the channel as the likelihood. — from [[mackay-2003-information/ch09-communication]] (information-theory → bayesian)
- [metaphor] ensemble learning: a point estimate is a delta-function Q ↔ MAP estimation: the spike is the crudest member of the family. — from [[mackay-2003-information/ch33-variational]] (information-theory → other)

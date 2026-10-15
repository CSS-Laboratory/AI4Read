---
id: chernoff-bound
type: concept
fields: [information-theory, linear-algebra]
fields_strong: [information-theory, linear-algebra]
n_sources: 2
n_works: 2
tiers: [deep, reference]
grounding: digests
sources: [polyanskiy-2025-information/ch17-information, spielman-2025-sagt/ch07-cayley]
generated_by: build_kg.py
---

# chernoff-bound

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch17-information]] (pp. 292–293): Markov on e^{λΣXᵢ}, optimised over λ≥0; non-asymptotic [new]

### linear-algebra

- [[spielman-2025-sagt/ch07-cayley]] (p. 66): tail bound 2e^{−t²/2k} for sums of ±1 variables [new]

## Candidate bridges

- [structural-analogy] Marginal-bound proof of Thm 8.2 ↔ large deviations: the same inequality follows from a Chernoff bound with KL divergence (p. 159). — from [[polyanskiy-2025-information/ch09-entropy]] (information-theory → information-theory)
- [structural-analogy] Matrix Chernoff for $\sum X_i$ ↔ probability: Chernoff bounds for real variables; the text calls the matrix bounds analogs of these (p. 259). — from [[spielman-2025-sagt/ch32-sparsification]] (linear-algebra → other:probability)

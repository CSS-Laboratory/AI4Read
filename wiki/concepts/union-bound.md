---
id: union-bound
type: concept
fields: [bayesian, information-theory, linear-algebra]
fields_strong: [bayesian, information-theory, linear-algebra]
n_sources: 4
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [mackay-2003-information/ch10-noisy, mackay-2003-information/ch13-binary, mackay-2003-information/ch14-very, spielman-2025-sagt/ch14-approximating]
generated_by: build_kg.py
---

# union-bound

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch10-noisy]] (p. 166): total error probability $\le$ the sum of the probabilities of events that each suffice for error [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 216): $P(\text{block error})\le\sum_{w>0}A(w)\beta(f)^w$ [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 230): error count ≤ sum of clash indicators (14.9) [new; work fields: information-theory, bayesian]

### linear-algebra

- [[spielman-2025-sagt/ch14-approximating]] (p. 133): failure over all $\binom n2$ pairs is at most the sum of the single-pair failures [new]

## Candidate bridges

- [structural-analogy] random coding with a union bound here ↔ channel coding (Part IV): the text says data transmission is based on the same method (p. 215). — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → information-theory)
- [structural-analogy] Chernoff + union bound ↔ concentration arguments in random-matrix and randomized-algorithm proofs. — from [[spielman-2025-sagt/ch07-cayley]] (linear-algebra → unspecified)
- [structural-analogy] union bound over all $2^m-1$ messages ↔ the Chernoff-plus-union-bound argument of Section 7.5 (p. 232) — from [[spielman-2025-sagt/ch28-brief]] (linear-algebra → unspecified)
- [structural-analogy] Random set separates all pairs with a union bound ↔ probabilistic method in combinatorics: show existence by random choice. — from [[spielman-2025-sagt/ch40-testing]] (linear-algebra → other:mathematics)

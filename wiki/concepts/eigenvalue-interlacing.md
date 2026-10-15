---
id: eigenvalue-interlacing
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 1
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch08-eigenvalues, spielman-2025-sagt/ch24-nodal]
generated_by: build_kg.py
---

# eigenvalue-interlacing

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch08-eigenvalues]] (p. 71, 81): adding a rank-one matrix interlaces the eigenvalues: the top one moves up a lot, the others at most to the next one; Exercise 1 states $\beta_i\ge\alpha_i\ge\beta_{i+1}$ for $B=A+xx^T$ [new]
- [[spielman-2025-sagt/ch24-nodal]] (p. 203): used in Thm 24.5.1 to pass from 'the block-diagonal matrix of the $B_i$ has at least $c$ eigenvalues below $\lambda_k$' to the same for $L$ [new]

## Candidate bridges

- [structural-analogy] Lemma 19.6.1 ↔ Courant–Fischer / eigenvalue interlacing: both bound eigenvalues of $A$ by those of its sub-blocks (the unit uses Theorem 4.3.1 for this). — from [[spielman-2025-sagt/ch19-independent]] (linear-algebra → linear-algebra)

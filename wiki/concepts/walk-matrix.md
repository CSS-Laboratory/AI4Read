---
id: walk-matrix
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 1
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch10-random]
generated_by: build_kg.py
---

# walk-matrix

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch01-introduction]] (p. 4): $W_G=M_GD_G^{-1}$, one diffusion step; lazy version $I/2+W_G/2$ [new]
- [[spielman-2025-sagt/ch10-random]] (p. 93): W = MD⁻¹; maps distribution p_t to p_{t+1}; not symmetric [new]

## Instances that use it

- [[path-on-3-vertices-norm]] — an asymmetric walk matrix with norm $\sqrt2>1$ — from [[spielman-2025-sagt/ch31-psrgs]]

## Candidate bridges

- [same-math] Walk matrix $W_G=M_GD_G^{-1}$ ↔ probability/Markov chains: the author names "probability that a random walk is at that vertex"; each non-isolated vertex's column sums to 1. — from [[spielman-2025-sagt/ch01-introduction]] (linear-algebra → other:probability)

---
id: preconditioner
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [deisenroth-2020-mml/ch07-continuous, spielman-2025-sagt/ch36-preconditioning]
generated_by: build_kg.py
---

# preconditioner

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch07-continuous]] (p. 230): a matrix $P$ chosen so that $P^{-1}A$ is better conditioned [new]
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 287): easy-to-solve PSD $B$ with small $\kappa(A,B)$ [new]

## Instances that use it

- [[tree-preconditioner-vaidya]] — a subgraph/tree Laplacian as preconditioner — from [[spielman-2025-sagt/ch36-preconditioning]]

## Candidate bridges

- [structural-analogy] NGD with Fisher preconditioner ↔ Bayesian inference: the text says it is equivalent to EKF sequential inference in the online exponential-family case (p. 281) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → bayesian)

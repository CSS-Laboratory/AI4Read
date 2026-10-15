---
id: krylov-subspace-methods
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 4
n_works: 3
tiers: [deep, core]
grounding: digests
sources: [deisenroth-2020-mml/ch02-linear-p1, spielman-2025-sagt/ch35-conjugate, spielman-2025-sagt/ch36-preconditioning, vonluxburg-2007-spectralclustering/main]
raw_ids: [Krylov subspace methods]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# krylov-subspace-methods

## Canon spine entry

- **Krylov subspace methods** (linear-algebra): Arnoldi, Lanczos, and conjugate gradients; solving huge sparse problems using only matrix–vector products (grad)

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch02-linear-p1]] (p. 35): iterative solvers for large systems, named (conjugate gradients, etc.) [as `Krylov subspace methods`]
- [[spielman-2025-sagt/ch35-conjugate]] (p. 282): iterates lie in span$\{b,Ab,\dots,A^tb\}$; CG picks the A-norm-best vector there
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 289–290): Chebyshev iteration and PCG as polynomial methods
- [[vonluxburg-2007-spectralclustering/main]] (p. 22): Lanczos method, speed depends on eigengap

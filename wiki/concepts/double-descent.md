---
id: double-descent
type: concept
fields: [llm, linear-algebra]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [prince-2023-udl/ch08-measuring, prince-2023-udl/ch20-does, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# double-descent

## Definitions in the sources

### llm

- [[prince-2023-udl/ch08-measuring]] (p. 129): test error falls, rises near the exact-fit point, then falls again with capacity [new]
- [[prince-2023-udl/ch20-does]] (p. 413): generalization improving with overparameterization on top of the bias/variance curve [new]

### linear-algebra

- [[strang-2023-introduction/ch10-learning]] (p. 382): test error rises near n = m weights then falls again for n > m [new]

## Instances that use it

- [[double-descent-curves]] — MNIST-1D with 15% label noise, MNIST, CIFAR-100 — from [[prince-2023-udl/ch08-measuring]]

## Candidate bridges

- [structural-analogy] Double descent via weight norm ↔ classical bias/variance trade-off — from [[prince-2023-udl/ch20-does]] (llm → unspecified)
- [structural-analogy] Double descent's minimum-norm solution ↔ linear algebra: pseudoinverse solution of underdetermined Ax = b — the unit's setting is nonlinear and it does not mention the pseudoinverse — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)

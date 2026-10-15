---
id: dual-basis
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p3, boyd-2018-vmls/ch11-matrix]
generated_by: build_kg.py
---

# dual-basis

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p3]] (p. 106): φ_j(v_k)=1 if j=k and 0 otherwise; reads off coordinates [new]
- [[boyd-2018-vmls/ch11-matrix]] (p. 205): rows of $B=A^{-1}$, as vectors $b_i$, paired with the columns $a_i$ of $A$ [new]

## Candidate bridges

- [structural-analogy] Dual basis as coordinate functionals ↔ statistics/data: a regression coefficient or weight vector as a linear readout of a feature vector. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → other:statistics)
- [same-math] dual basis coefficients $\beta=A^{-1}x$ ↔ change of basis: $A^{-1}$ converts standard coordinates into coordinates in the basis of columns of $A$ — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)

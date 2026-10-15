---
id: kernel-trick
type: concept
fields: [linear-algebra, bayesian, control-theory]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch15-multi, deisenroth-2020-mml/ch12-classification, murphy-2023-pml2/ch18-gaussian-p1, sutton-2018-rl/ch09-policy-p2]
generated_by: build_kg.py
---

# kernel-trick

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch15-multi]] (p. 333): use $(A^TA+\lambda I)^{-1}A^T=A^T(AA^T+\lambda I)^{-1}$ to invert a small $m\times m$ matrix [new]
- [[deisenroth-2020-mml/ch12-classification]] (p. 388–389): replace $\langle\phi(\boldsymbol x_i),\phi(\boldsymbol x_j)\rangle$ by $k(\boldsymbol x_i,\boldsymbol x_j)$ [new]

### bayesian

- [[murphy-2023-pml2/ch18-gaussian-p1]] (p. 692): replace feature inner products by kernel evaluations [new]

### control-theory

- [[sutton-2018-rl/ch09-policy-p2]] (p. 233): evaluate $\mathbf x(s)^\top\mathbf x(s')$ compactly without computing in feature space [new]

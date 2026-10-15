---
id: gram-matrix
type: concept
fields: [linear-algebra]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch10-matrix, boyd-2018-vmls/ch11-matrix, boyd-2018-vmls/ch12-least, deisenroth-2020-mml/ch12-classification, spielman-2025-sagt/ch09-strongly]
generated_by: build_kg.py
---

# gram-matrix

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch10-matrix]] (p. 181): $G=A^TA$, entries $a_i^Ta_j$, symmetric [new]
- [[boyd-2018-vmls/ch11-matrix]] (p. 214): $A^TA$; invertible iff the columns of $A$ are independent [new]
- [[boyd-2018-vmls/ch12-least]] (p. 229): $A^TA$, with inner products of columns as entries [new]
- [[deisenroth-2020-mml/ch12-classification]] (p. 389): $\boldsymbol K$ with $K_{ij}=k(\boldsymbol x_i,\boldsymbol x_j)$; symmetric positive semidefinite [new]
- [[spielman-2025-sagt/ch09-strongly]] (p. 87): matrix of inner products $\boldsymbol x_i\boldsymbol x_j^T$; equals $UU^T$ [new]

## Instances that use it

- [[group-membership-gram-matrix]] — $G_{ij}$ = number of items in both groups i and j — from [[boyd-2018-vmls/ch10-matrix]]
- [[gram-matrix-gradient]] — $d(\mathbf R^\top\mathbf R)/d\mathbf R$ — from [[deisenroth-2020-mml/ch05-vector]]

## Candidate bridges

- [same-math] Cholesky $B=R^*R$ ↔ positive (semi)definite matrices (canon): "Gram matrix" form $A^*A$ (7.38 (f)), refined to a triangular factor. — from [[axler-2024-ladr/ch07-operators-p2]] (linear-algebra → linear-algebra)
- [same-math] $C^{\mathrm t}BC$ rule for the matrix of a bilinear form ↔ inner products: the Gram matrix $\langle e_j,e_k\rangle$ changes this way under a basis change — the inner product is a symmetric bilinear form here (9.10). — from [[axler-2024-ladr/ch09-multilinear-p1]] (linear-algebra → other)
- [same-math] Gram matrix of a 0/1 membership matrix ↔ social network analysis: co-membership counts in two-mode (affiliation) networks — the same product $A^TA$ on an incidence-style matrix. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → complex-systems)
- [same-math] Covariance-like Gram matrix $\tilde A^T\tilde A/n$ (exercise 10.16) ↔ statistics: covariance matrix of de-meaned data. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other)
- [same-math] SVM Gram matrix $\boldsymbol K$ (symmetric PSD, 12.53) ↔ linear-algebra: positive semidefinite matrices — the Gram matrix of inner products is a PSD matrix. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → linear-algebra)
- [same-math] "Any $M$ with $M^TM=L^+$" ↔ factorizations of a PSD matrix: only the Gram matrix matters, not which factor is used. — from [[spielman-2025-sagt/ch14-approximating]] (linear-algebra → linear-algebra)

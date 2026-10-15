---
id: change-of-basis
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 10
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch08-operators, axler-2024-ladr/ch09-multilinear-p1, axler-2024-ladr/ch09-multilinear-p2, boyd-2018-vmls/ch07-matrix, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch05-vector, strang-2023-introduction/ch08-linear]
raw_ids: [change of basis]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# change-of-basis

## Canon spine entry

- **change of basis** (linear-algebra): the same vector or map described in different coordinates; A ↦ P⁻¹AP (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p2]] (p. 93): A=C⁻¹BC with C=M(I,(u),(v)) [as `change of basis`]
- [[axler-2024-ladr/ch08-operators]] (p. 327): $A=C^{-1}BC$ used for trace invariance
- [[axler-2024-ladr/ch09-multilinear-p1]] (p. 336): for bilinear forms $A=C^{\mathrm t}BC$, unlike the operator rule $C^{-1}BC$
- [[axler-2024-ladr/ch09-multilinear-p2]] (pp. 358–359): $\det(S^{-1}TS)=\det T$, so $\det\mathcal M(T)$ is basis-independent [as `change of basis`]
- [[boyd-2018-vmls/ch07-matrix]] (p. 130): here a change of coordinates $x^{\rm earth}=p+Qx^{\rm body}$, which includes a shift $p$ [as `change of basis`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 54): $\tilde A_\Phi=T^{-1}A_\Phi S$ (Theorem 2.20)
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 103, 106, 116): diagonalization is a basis change to the eigenbasis; similar matrices share det, trace, eigenvalues [as `change of basis`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 121): $V^\top$ and $U$ are basis changes in domain and codomain [as `change of basis`]
- [[deisenroth-2020-mml/ch05-vector]] (p. 151): the matrix with $\mathbf J\mathbf b_i=\mathbf c_i$ implements the basis change and is the Jacobian of a linear map [as `change of basis`]
- [[strang-2023-introduction/ch08-linear]] (p. 319, 327): B = W⁻¹V for T = identity; A becomes B_out⁻¹AB_in

## Instances that use it

- [[example-3-83-identity-two-bases]] — change-of-basis matrix for (4,2),(5,3) — from [[axler-2024-ladr/ch03-linear-p2]]

## Candidate bridges

- [structural-analogy] basis and unique coordinates (2.28) ↔ linear-algebra canon: change of basis — a basis gives the coordinates that the canon's change-of-basis acts on. — from [[axler-2024-ladr/ch02-finite]] (linear-algebra → linear-algebra)
- [same-math] 3.84 A=C⁻¹BC ↔ linear-algebra spine: change of basis A ↦ P⁻¹AP — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [same-math] dual basis coefficients $\beta=A^{-1}x$ ↔ change of basis: $A^{-1}$ converts standard coordinates into coordinates in the basis of columns of $A$ — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → linear-algebra)
- [structural-analogy] Eigendecomposition as $P^{-1}$, then $D$, then $P$ ↔ change of basis: do the easy operation in the right coordinates, then return. — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] Choosing a representation basis ↔ feature engineering: structure sometimes becomes visible only after a change of basis. — from [[polyanskiy-2025-information/ch11-lossless]] (information-theory → other:statistics)
- [structural-analogy] translate–act–translate back, T₋PT₊ ↔ change of basis: A ↦ P⁻¹AP — conjugating by an invertible map. — from [[strang-2023-introduction/app10-computer]] (linear-algebra → linear-algebra)
- [structural-analogy] $V=WB$ with B invertible ↔ change of basis: the same space described by different basis vectors (p. 123). — from [[strang-2023-introduction/ch03-four-p2]] (linear-algebra → linear-algebra)

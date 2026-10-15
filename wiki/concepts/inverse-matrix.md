---
id: inverse-matrix
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 10
n_works: 4
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch09-multilinear-p2, boyd-2018-vmls/ch11-matrix, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch04-matrix-p1, strang-2023-introduction/app10-computer, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch02-solving-p2, strang-2023-introduction/ch05-determinants]
raw_ids: [inverse matrix]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# inverse-matrix

## Canon spine entry

- **inverse matrix** (linear-algebra): the map that undoes A; exists iff det ≠ 0 (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p2]] (p. 91): square A with AB=BA=I for some square B; unique (p. 91). Author does not mention determinants in this unit. [as `inverse matrix`]
- [[axler-2024-ladr/ch09-multilinear-p2]] (p. 357): an operator or matrix is invertible iff its determinant is nonzero [as `inverse matrix`]
- [[boyd-2018-vmls/ch11-matrix]] (pp. 202–203): a matrix $A^{-1}$ with $AA^{-1}=A^{-1}A=I$; exists only for square matrices, and then left, right and two-sided invertibility coincide [as `inverse matrix`]
- [[deisenroth-2020-mml/ch02-linear-p1]] (pp. 24, 33): B with AB = I = BA; unique if it exists; 2×2 formula valid iff $a_{11}a_{22}-a_{12}a_{21}\ne0$; found by $[A|I]\rightsquigarrow[I|A^{-1}]$ [as `inverse matrix`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 47, 49): appears as regular matrix ($\mathrm{rk}=n$) and as $\Phi^{-1}$ of a bijection
- [[deisenroth-2020-mml/ch04-matrix-p1]] (pp. 100, 103): exists iff $\det\neq0$ iff full rank (Thms 4.1, 4.3) [as `inverse matrix`]
- [[strang-2023-introduction/app10-computer]] (p. 416): T₋ and T₊ undo each other [as `inverse matrix`]
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 50–52): A⁻¹ with A⁻¹A = I = AA⁻¹; exists iff n pivots (row exchanges allowed); (AB)⁻¹ = B⁻¹A⁻¹
- [[strang-2023-introduction/ch02-solving-p2]] (pp. 67–68, 83): (AB)⁻¹ = B⁻¹A⁻¹; (A⁻¹)ᵀ = (Aᵀ)⁻¹ [as `inverse matrix`]
- [[strang-2023-introduction/ch05-determinants]] (p. 202): exists when det ≠ 0; $A^{-1}=C^{\mathsf T}/\det A$ [as `inverse matrix`]

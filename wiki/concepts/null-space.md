---
id: null-space
type: concept
fields: [linear-algebra]
n_sources: 9
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch06-inner-p2, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch12-classification, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch29-expander, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch04-orthogonality-p1]
generated_by: build_kg.py
---

# null-space

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p1]] (p. 135): the kernel; here eigenvectors for $\lambda$ are the nonzero elements of $\operatorname{null}(T-\lambda I)$
- [[axler-2024-ladr/ch06-inner-p2]] (p. 220): appear as $\operatorname{null}T$ and $\operatorname{range}T$ and their complements
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 58–59): kernel $\{v:\Phi(v)=0\}$; solutions of $Ax=0$
- [[deisenroth-2020-mml/ch12-classification]] (p. 390): mentioned only to distinguish it from the "kernel" of this chapter
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 26): $\{z:Mz=0\}$; orthogonal to the span (column space) of a symmetric $M$
- [[spielman-2025-sagt/ch29-expander]] (p. 238): codewords are $\{y: My=0\}$
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 40, 50): nonzero X with AX = 0 exist exactly when columns are dependent; solutions of Ax = b then come in lines x + αX
- [[strang-2023-introduction/ch03-four-p2]] (p. 120): $N(A)$ has basis the $n-r$ special solutions
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 156–157, 168): N(AᵀA) = N(A); the error lies in N(Aᵀ)

## Instances that use it

- [[differentiation-map]] — linear; null space = constants; surjective on $\mathcal P(\mathbf R)$; not surjective on $\mathcal P_5$ to itself — from [[axler-2024-ladr/ch03-linear-p1]]
- [[multiplication-by-x-squared]] — injective, null space $\{0\}$; does not commute with differentiation — from [[axler-2024-ladr/ch03-linear-p1]]
- [[backward-shift]] — null space $\{(a,0,0,\dots)\}$ — from [[axler-2024-ladr/ch03-linear-p1]]

## Candidate bridges

- [structural-analogy] Null space of $T$ ↔ lost information: inputs that look identical after the map. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → other)
- [structural-analogy] V/U (collapsing a subspace to zero) ↔ linear-algebra: null space of a map. T̃ identifies V/(null T) with range T, a "first isomorphism" pattern. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product). — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → other)
- [structural-analogy] Null-space coordinate vectors giving a 3D drawing ↔ spectral graph drawing: low-eigenspace vectors as vertex coordinates. — from [[spielman-2025-sagt/ch26-planar]] (linear-algebra → linear-algebra)
- [same-math] linear code as column space or null space ↔ linear algebra: range and kernel, here over $\mathbb F_2$ (p. 232) — from [[spielman-2025-sagt/ch28-brief]] (linear-algebra → linear-algebra)

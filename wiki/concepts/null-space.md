---
id: null-space
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 24
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch03-linear-p3, axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch06-inner-p2, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch12-classification, spielman-2025-sagt/ch02-eigenvalues, spielman-2025-sagt/ch26-planar, spielman-2025-sagt/ch28-brief, spielman-2025-sagt/ch29-expander, spielman-2025-sagt/ch39-testing, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch02-solving-p2, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch06-eigenvalues-p1, strang-2023-introduction/ch08-linear, strang-2023-introduction/ch10-learning]
aliases: [null-space-kernel]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# null-space

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `null-space-kernel` — 15 digest(s)

## Canon spine entry

- **null space (kernel)** (linear-algebra): all inputs sent to zero; what the map destroys (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p1]] (p. 59): $\{v: Tv=0\}$, a subspace of the domain [as `null space (kernel)`; alias `null-space-kernel`]
- [[axler-2024-ladr/ch03-linear-p3]] (pp. 111–113): null T′ = (range T)⁰ and range T′ = (null T)⁰ [as `null space (kernel)`; alias `null-space-kernel`]
- [[axler-2024-ladr/ch05-eigenvalues-p1]] (p. 135): the kernel; here eigenvectors for $\lambda$ are the nonzero elements of $\operatorname{null}(T-\lambda I)$
- [[axler-2024-ladr/ch06-inner-p2]] (p. 220): appear as $\operatorname{null}T$ and $\operatorname{range}T$ and their complements
- [[deisenroth-2020-mml/ch02-linear-p1]] (p. 33): solution space of Ax = 0; named only as a forward reference, basis read by the minus-1 trick [as `null space (kernel)`; alias `null-space-kernel`]
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 58–59): kernel $\{v:\Phi(v)=0\}$; solutions of $Ax=0$
- [[deisenroth-2020-mml/ch04-matrix-p1]] (p. 106): eigenspace $E_\lambda=\ker(A-\lambda I)$ [as `null space (kernel)`; alias `null-space-kernel`]
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 125): $v_i$ with $i>m$ (case $m<n$) span a null-space basis [as `null space (kernel)`; alias `null-space-kernel`]
- [[deisenroth-2020-mml/ch12-classification]] (p. 390): mentioned only to distinguish it from the "kernel" of this chapter
- [[spielman-2025-sagt/ch02-eigenvalues]] (p. 26): $\{z:Mz=0\}$; orthogonal to the span (column space) of a symmetric $M$
- [[spielman-2025-sagt/ch26-planar]] (p. 213): contains the three coordinate vectors [as `null space (kernel)`; alias `null-space-kernel`]
- [[spielman-2025-sagt/ch28-brief]] (p. 232): a linear code defined by $Mc=0$ is the null space of $M$ over $\mathbb F_2$ [alias `null-space-kernel`]
- [[spielman-2025-sagt/ch29-expander]] (p. 238): codewords are $\{y: My=0\}$
- [[spielman-2025-sagt/ch39-testing]] (p. 311): nullspaces mod 2 are used to intersect the subgroups $\mathcal A_j$ [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/app1-ranks]] (pp. 400, 411): AᵀA and A have the same nullspace; special solutions X from F [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 40, 50): nonzero X with AX = 0 exist exactly when columns are dependent; solutions of Ax = b then come in lines x + αX
- [[strang-2023-introduction/ch02-solving-p2]] (p. 80): Bx = 0 for a nonzero x shows B is singular [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/ch03-four-p1]] (pp. 88, 93): all solutions x of Ax = 0; a subspace; unchanged by row operations [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/ch03-four-p2]] (p. 120): $N(A)$ has basis the $n-r$ special solutions
- [[strang-2023-introduction/ch03-four-p3]] (pp. 131–133): solutions of Ax = 0; preserved by elimination; basis = special solutions [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 156–157, 168): N(AᵀA) = N(A); the error lies in N(Aᵀ)
- [[strang-2023-introduction/ch06-eigenvalues-p1]] (p. 220): eigenvectors for λ are the nullspace of A − λI [as `null space (kernel)`; alias `null-space-kernel`]
- [[strang-2023-introduction/ch08-linear]] (p. 313): Strang's "kernel of T" is the set of inputs with T(v) = 0 [alias `null-space-kernel`]
- [[strang-2023-introduction/ch10-learning]] (p. 382): appears in the double-descent explanation [as `null space (kernel)`; alias `null-space-kernel`]

## Instances that use it

- [[differentiation-map]] — linear; null space = constants; surjective on $\mathcal P(\mathbf R)$; not surjective on $\mathcal P_5$ to itself — from [[axler-2024-ladr/ch03-linear-p1]]
- [[multiplication-by-x-squared]] — injective, null space $\{0\}$; does not commute with differentiation — from [[axler-2024-ladr/ch03-linear-p1]]
- [[backward-shift]] — null space $\{(a,0,0,\dots)\}$ — from [[axler-2024-ladr/ch03-linear-p1]]

## Candidate bridges

- [structural-analogy] Null space of $T$ ↔ lost information: inputs that look identical after the map. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → other:lost-information)
- [structural-analogy] V/U (collapsing a subspace to zero) ↔ linear-algebra: null space of a map. T̃ identifies V/(null T) with range T, a "first isomorphism" pattern. — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product). — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [structural-analogy] Null-space coordinate vectors giving a 3D drawing ↔ spectral graph drawing: low-eigenspace vectors as vertex coordinates. — from [[spielman-2025-sagt/ch26-planar]] (linear-algebra → linear-algebra)
- [same-math] linear code as column space or null space ↔ linear algebra: range and kernel, here over $\mathbb F_2$ (p. 232) — from [[spielman-2025-sagt/ch28-brief]] (linear-algebra → linear-algebra)

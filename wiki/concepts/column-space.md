---
id: column-space
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 15
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch03-linear-p3, axler-2024-ladr/ch06-inner-p2, deisenroth-2020-mml/ch02-linear-p2, spielman-2025-sagt/ch28-brief, spielman-2025-sagt/ch29-expander, strang-2023-introduction/app1-ranks, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch02-solving-p1, strang-2023-introduction/ch03-four-p1, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch08-linear]
aliases: [column-space-range]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# column-space

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `column-space-range` — 8 digest(s)

## Canon spine entry

- **column space (range)** (linear-algebra): all outputs Ax; where the map can reach (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p1]] (p. 61): here the range of any linear map $T$: all outputs $Tv$, a subspace of the target (p. 61); no matrices yet [as `column space (range)`; alias `column-space-range`]
- [[axler-2024-ladr/ch03-linear-p2]] (p. 90): here only the span of columns; dim range T equals its dimension, i.e. the column rank of M(T) [as `column space (range)`; alias `column-space-range`]
- [[axler-2024-ladr/ch03-linear-p3]] (pp. 111–113): null T′ = (range T)⁰ and range T′ = (null T)⁰ [as `column space (range)`; alias `column-space-range`]
- [[axler-2024-ladr/ch06-inner-p2]] (p. 220): appear as $\operatorname{null}T$ and $\operatorname{range}T$ and their complements
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 59): image of $x\mapsto Ax$; span of the columns
- [[spielman-2025-sagt/ch28-brief]] (p. 232): $C_G=\{Gb\}$ is the column space of $G$ over $\mathbb F_2$ [alias `column-space-range`]
- [[spielman-2025-sagt/ch29-expander]] (p. 239): codewords are $\{Gx\}$, with $G$ a generator matrix
- [[strang-2023-introduction/app1-ranks]] (p. 400): C(AB) lies inside C(A) [as `column space (range)`; alias `column-space-range`]
- [[strang-2023-introduction/ch01-vectors]] (p. 20): C(A): all Ax, all combinations of the columns
- [[strang-2023-introduction/ch02-solving-p1]] (pp. 40, 44): b has a solution iff b lies in the combinations of the columns of A
- [[strang-2023-introduction/ch03-four-p1]] (p. 87): all combinations of the columns of A, i.e. all Ax; Ax = b solvable iff b is in it [as `column space (range)`; alias `column-space-range`]
- [[strang-2023-introduction/ch03-four-p2]] (pp. 119, 122): basis: the pivot columns; dimension $r$
- [[strang-2023-introduction/ch03-four-p3]] (p. 132): spanned by the pivot columns of A; not preserved by elimination [as `column space (range)`; alias `column-space-range`]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 156–157, 168): N(AᵀA) = N(A); the error lies in N(Aᵀ)
- [[strang-2023-introduction/ch08-linear]] (p. 313): Strang's "range of T" is the set of all outputs T(v) [alias `column-space-range`]

## Instances that use it

- [[triangular-matrix-a4]] — upper-triangular ones; its column space is all of R⁴ — from [[strang-2023-introduction/ch01-vectors]]

## Candidate bridges

- [same-math] 3.50 "Ab is a combination of columns of A" ↔ linear-algebra spine: matrix–vector product as column space reachability — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [same-math] 3.78 dim range T = column rank ↔ linear-algebra spine: rank as dimension of column space — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product). — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → linear-algebra)
- [structural-analogy] Normal equations, $\hat r\perp$ columns ↔ projection: $A\hat x$ is the closest point in the column space (the text uses the word "closest", not "projection", in the chapter; exercise 12.8 names it). — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → linear-algebra)
- [same-math] ŷᵈ = Aθ̂ as a projection ↔ linear-algebra: projection of yᵈ onto the column space of A (P = A(AᵀA)⁻¹Aᵀ) — the same normal-equation solution. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → linear-algebra)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other:statistics)
- [same-math] Least-squares ERM (8.9) ↔ linear-algebra: least squares by projecting y onto the column space of X (the book defers the closed form to Sec. 9.2 (p. 261); the projection reading is from the field list, not this unit). — from [[deisenroth-2020-mml/ch08-when]] (linear-algebra → linear-algebra)
- [same-math] ML fit $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top y$ ↔ projection onto the column space; $\Phi\Phi^\top y$ for orthonormal columns. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → unspecified)
- [structural-analogy] $\boldsymbol w=\sum\alpha_ny_n\boldsymbol x_n$ ↔ column space/span: the solution lives in the row space (span) of the data matrix $\boldsymbol X$. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → linear-algebra)
- [same-math] linear code as column space or null space ↔ linear algebra: range and kernel, here over $\mathbb F_2$ (p. 232) — from [[spielman-2025-sagt/ch28-brief]] (linear-algebra → linear-algebra)

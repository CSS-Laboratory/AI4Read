---
id: rank-nullity
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 9
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch03-linear-p3, axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch08-operators, deisenroth-2020-mml/ch02-linear-p2, spielman-2025-sagt/ch29-expander, strang-2023-introduction/ch03-four-p3, strang-2023-introduction/ch04-orthogonality-p1]
aliases: [rank-nullity-fundamental-theorem-of-linear-maps]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# rank-nullity

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `rank-nullity-fundamental-theorem-of-linear-maps` — 4 digest(s)

## Canon spine entry

- **rank–nullity (Fundamental Theorem of Linear Maps)** (linear-algebra): dim V = dim null T + dim range T (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch03-linear-p1]] (p. 62): $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ for finite-dimensional $V$ [as `rank–nullity (Fundamental Theorem of Linear Maps)`; alias `rank-nullity-fundamental-theorem-of-linear-maps`]
- [[axler-2024-ladr/ch03-linear-p2]] (pp. 84, 86): used as 3.21/3.66 to prove 3.65 and 3.70 [as `rank–nullity (Fundamental Theorem of Linear Maps)`; alias `rank-nullity-fundamental-theorem-of-linear-maps`]
- [[axler-2024-ladr/ch03-linear-p3]] (p. 102, used throughout): the repeated tool: dim V = dim null T + dim range T [as `rank–nullity (Fundamental Theorem of Linear Maps)`; alias `rank-nullity-fundamental-theorem-of-linear-maps`]
- [[axler-2024-ladr/ch05-eigenvalues-p1]] (p. 150): used as the fundamental theorem of linear maps (3.21) in 5.34
- [[axler-2024-ladr/ch08-operators]] (pp. 299, 323): used in 8.4 and 8.45
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 60): $\dim\ker\Phi+\dim\mathrm{Im}\,\Phi=\dim V$
- [[spielman-2025-sagt/ch29-expander]] (p. 238): constraint counting gives dimension $\ge dn-\#\text{constraints}$
- [[strang-2023-introduction/ch03-four-p3]] (p. 133): here the Counting Theorem r + (n − r) = n [as `rank–nullity (Fundamental Theorem of Linear Maps)`; alias `rank-nullity-fundamental-theorem-of-linear-maps`]
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 145): used for the counts r + (n−r) = n and r + (m−r) = m

## Candidate bridges

- [same-math] Fundamental theorem of linear maps ↔ linear-algebra spine: rank–nullity $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ — same statement, stated without matrices. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] Rank–nullity ↔ the earlier solution-set count: $Ax=0$ has an $(n-\mathrm{rk}A)$-dimensional solution space — the same statement for $\Phi:x\mapsto Ax$. — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → other:the-earlier-solution-set)
- [same-math] Counting dimension of $\{y:My=0\}$ ≥ unknowns − constraints ↔ rank–nullity (over $\mathbb F_2$ here). — from [[spielman-2025-sagt/ch29-expander]] (linear-algebra → unspecified)

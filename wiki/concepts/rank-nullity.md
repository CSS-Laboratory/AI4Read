---
id: rank-nullity
type: concept
fields: [linear-algebra]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch05-eigenvalues-p1, axler-2024-ladr/ch08-operators, deisenroth-2020-mml/ch02-linear-p2, spielman-2025-sagt/ch29-expander, strang-2023-introduction/ch04-orthogonality-p1]
generated_by: build_kg.py
---

# rank-nullity

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch05-eigenvalues-p1]] (p. 150): used as the fundamental theorem of linear maps (3.21) in 5.34
- [[axler-2024-ladr/ch08-operators]] (pp. 299, 323): used in 8.4 and 8.45
- [[deisenroth-2020-mml/ch02-linear-p2]] (p. 60): $\dim\ker\Phi+\dim\mathrm{Im}\,\Phi=\dim V$
- [[spielman-2025-sagt/ch29-expander]] (p. 238): constraint counting gives dimension $\ge dn-\#\text{constraints}$
- [[strang-2023-introduction/ch04-orthogonality-p1]] (p. 145): used for the counts r + (n−r) = n and r + (m−r) = m

## Candidate bridges

- [same-math] Fundamental theorem of linear maps ↔ linear-algebra spine: rank–nullity $\dim V=\dim\operatorname{null}T+\dim\operatorname{range}T$ — same statement, stated without matrices. — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → linear-algebra)
- [same-math] Rank–nullity ↔ the earlier solution-set count: $Ax=0$ has an $(n-\mathrm{rk}A)$-dimensional solution space — the same statement for $\Phi:x\mapsto Ax$. — from [[deisenroth-2020-mml/ch02-linear-p2]] (linear-algebra → other)
- [same-math] Counting dimension of $\{y:My=0\}$ ≥ unknowns − constraints ↔ rank–nullity (over $\mathbb F_2$ here). — from [[spielman-2025-sagt/ch29-expander]] (linear-algebra → unspecified)

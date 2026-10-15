---
id: effective-resistance
type: concept
fields: [linear-algebra]
n_sources: 6
tiers: [deep]
grounding: digests
sources: [spielman-2025-sagt/ch12-effective, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch14-approximating, spielman-2025-sagt/ch17-monotonicity, spielman-2025-sagt/ch32-sparsification, spielman-2025-sagt/ch37-augmented]
generated_by: build_kg.py
---

# effective-resistance

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch12-effective]] (p. 112): $(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)$; the voltage drop for a unit current; a squared Euclidean distance [new]
- [[spielman-2025-sagt/ch13-random]] (p. 126): $(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)$ [new]
- [[spielman-2025-sagt/ch14-approximating]] (p. 129): $\mathrm{R}_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL^+(\delta_a-\delta_b)$, a squared Euclidean distance [new]
- [[spielman-2025-sagt/ch17-monotonicity]] (p. 149): potential difference for one unit of current from $s$ to $t$; $i_{ext}^TL^+i_{ext}$ [new]
- [[spielman-2025-sagt/ch32-sparsification]] (p. 261): $R_{\rm eff}(a,b)=(\delta_a-\delta_b)^TL_G^+(\delta_a-\delta_b)$ [new]
- [[spielman-2025-sagt/ch37-augmented]] (p. 297): resistance between $a$ and $b$ in $G$; controls sampling probabilities [new]

## Instances that use it

- [[path-effective-resistance]] — path resistances add — from [[spielman-2025-sagt/ch17-monotonicity]]

## Candidate bridges

- [structural-analogy] Effective resistance as squared distance between $L^{+/2}\delta_a$ points ↔ spectral embedding: vertices as vectors — both use the spectral decomposition of $L$. — from [[spielman-2025-sagt/ch12-effective]] (linear-algebra → linear-algebra)
- [same-math] effective resistance $i^TL^+i$ ↔ linear algebra: pseudoinverse solving $Lv=b$ — the same quadratic form. — from [[spielman-2025-sagt/ch17-monotonicity]] (linear-algebra → linear-algebra)
- [same-math] Stretch of an edge ↔ electrical networks: effective resistance in a series path of resistors (p. 291). — from [[spielman-2025-sagt/ch36-preconditioning]] (linear-algebra → other)

---
id: shannon-lower-bound
type: concept
fields: [information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch33-mutual]
generated_by: build_kg.py
---

# shannon-lower-bound

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch29-evaluating]] (p. 511): $R(D)\ge\frac12\log\frac{\sigma^2}{D}-D(P_S\|\mathcal N(0,\sigma^2))$; tight as $D\to0$ under conditions [new]
- [[polyanskiy-2025-information/ch33-mutual]] (p. 588): $h(\theta)+\frac d2\log\frac{2\pi ed}D$ bound on rate-distortion for isotropic $\theta$ [new]

## Candidate bridges

- [structural-analogy] Shannon lower bound for estimation (§30.1 preview) ↔ statistics: lower bounds on estimation error via rate-distortion. — from [[polyanskiy-2025-information/ch29-evaluating]] (information-theory → other)
- [same-math] SLB for $\phi$ ↔ rate-distortion theory: Shannon lower bound (Section 26.1) — from [[polyanskiy-2025-information/ch33-mutual]] (information-theory → other)

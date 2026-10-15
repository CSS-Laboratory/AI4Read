---
id: f-divergence
type: concept
fields: [information-theory, bayesian]
n_sources: 12
tiers: [reference, deep]
grounding: digests
sources: [murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch26-generative, nielsen-2020-elementary/main-p1, nielsen-2020-elementary/main-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch08-f-p1, polyanskiy-2025-information/ch08-f-p2, polyanskiy-2025-information/ch16-neyman, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch35-entropic, polyanskiy-2025-information/ch36-strong-p1]
canon_spine: information-theory
generated_by: build_kg.py
---

# f-divergence

## Canon spine entry

- **f-divergence** (information-theory): a family of divergences including KL, total variation, χ² and Hellinger (grad)

## Definitions in the sources

### information-theory

- [[nielsen-2020-elementary/main-p1]] (pp. 23–24): $I_f=\sum\theta_if(\theta'_i/\theta_i)$; invariant and separable
- [[nielsen-2020-elementary/main-p2]] (pp. 44–45): $I_f(p:q)=\int pf(q/p)$; extended version $I_f^e$ subtracts a linear term to keep sample estimates non-negative
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): family that includes Hellinger and χ² (named alongside total variation); used where KL is not the right measure
- [[polyanskiy-2025-information/ch03-divergence]] (pp. 20, 37): KL and $\chi^2$ are members; $\chi^2(P\|Q)=\int dQ(\frac{dP}{dQ}-1)^2$
- [[polyanskiy-2025-information/ch08-f-p1]] (p. 115): $D_f(P\|Q)=\mathbb E_Q f(dP/dQ)$, $f$ convex, $f(1)=0$; independent of dominating measure
- [[polyanskiy-2025-information/ch08-f-p2]] (p. 138–139, 147): $D_f(P\|Q)=\int dQ\,f(dP/dQ)$ for convex $f$ with $f(1)=0$; this part studies its local and dual behaviour
- [[polyanskiy-2025-information/ch16-neyman]] (p. 278): all of them can be computed from $\mathcal R(P,Q)$; TV example
- [[polyanskiy-2025-information/ch32-classical]] (p. 576): here mainly $\chi^2$, used with data processing and its variational form to bound variance
- [[polyanskiy-2025-information/ch35-entropic]] (p. 614): squared Hellinger is an f-divergence, hence convex, so Hellinger balls are convex
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 629): the family $D_f$ in which η is defined

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (p. 55): $\int qf(p/q)$ with convex $f$, $f(1)=0$ [new]
- [[murphy-2023-pml2/ch26-generative]] (p. 898–899): $\int q f(p/q)$, convex $f$, $f(1)=0$; lower-bounded through convex conjugates [new]

## Instances that use it

- [[f-gan]] — f-divergence lower bound game (26.27) — from [[murphy-2023-pml2/ch26-generative]]
- [[gaussian-location-model]] — $P_t=\mathcal N(t,1)$: all listed f-divergences except TV are quadratic in $t$ — from [[polyanskiy-2025-information/ch08-f-p2]]

---
id: mutual-information-ixy
type: concept
fields: [information-theory]
n_sources: 13
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch16-inequalities, mackay-2003-information/ch44-supervised, pierce-1980-introduction/ch08-noisy, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch27-rate, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch34-lower, stone-2022-information/appf-rules, stone-2022-information/ch06-mutual, stone-2022-information/ch07-channel, stone-2022-information/ch08-rate]
raw_ids: [mutual information I(X;Y), mutual-information-I(X;Y)]
canon_spine: information-theory
generated_by: build_kg.py
---

# mutual-information-ixy

## Canon spine entry

- **mutual information I(X;Y)** (information-theory): how much knowing Y reduces uncertainty about X; symmetric, and zero iff X and Y are independent (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 6): reduction in uncertainty, $H(X)-H(X|Y)$; symmetric, non-negative [as `mutual information I(X;Y)`]
- [[cover-2006-elements/ch16-inequalities]] (p. 484): $D(p(x,y)\|p(x)p(y))\ge0$, zero iff independent [as `mutual-information-I(X;Y)`]
- [[mackay-2003-information/ch44-supervised]] (p. 533): proposed classifier score $I(T;Y)$ [as `mutual information I(X;Y)`]
- [[pierce-1980-introduction/ch08-noisy]] (p. 155; canon link, not stated in this unit): Pierce does not use this name. His rate $R$ in 8.8–8.10 is the same quantity [as `mutual information I(X;Y)`]
- [[polyanskiy-2025-information/ch04-mutual]] (p. 42, 44): here defined as D(P_{X,Y}‖P_X P_Y), the general definition; equals H(X)−H(X|Y) for discrete X when H(X|Y)<∞ [as `mutual information I(X;Y)`]
- [[polyanskiy-2025-information/ch21-channel]] (p. 376): the quantity maximized to get capacity; its information density is a sum of iid terms in the proof [as `mutual information I(X;Y)`]
- [[polyanskiy-2025-information/ch27-rate]] (p. 486, 488): the quantity minimized in $\phi_X(D)$; convex in $P_{Y|X}$, super-additive for independent inputs [as `mutual information I(X;Y)`]
- [[polyanskiy-2025-information/ch33-mutual]] (p. 585): information the data give about $\theta$; capped by channel capacity [as `mutual information I(X;Y)`]
- [[polyanskiy-2025-information/ch34-lower]] (p. 599): bounded via the chain rule and the Jensen–Shannon form [as `mutual information I(X;Y)`]
- [[stone-2022-information/appf-rules]] (p. 266): H.13–H.18 [as `mutual information I(X;Y)`]
- [[stone-2022-information/ch06-mutual]] (pp. 135, 148): here I(X,Y) = H(X)+H(Y)−H(X,Y) = H(X)−H(X|Y) = H(Y)−H(Y|X); symmetric, zero if X, Y are independent [as `mutual information I(X;Y)`]
- [[stone-2022-information/ch07-channel]] (pp. 153, 165): $H(Y)-H(Y|X)$; for Gaussians, $\tfrac12\log\frac1{1-\rho^2}$ [as `mutual information I(X;Y)`]
- [[stone-2022-information/ch08-rate]] (p. 180): the quantity minimised in $R^I(D)$ [as `mutual information I(X;Y)`]

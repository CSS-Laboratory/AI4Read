---
id: information-density
type: concept
fields: [information-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch20-random, polyanskiy-2025-information/ch28-rate]
generated_by: build_kg.py
---

# information-density

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch20-random]] (p. 351): $i(x;y)=\log\frac{dP_{X,Y}}{dP_XP_Y}$; its mean is $I(X;Y)$; also called pointwise mutual information [new]
- [[polyanskiy-2025-information/ch28-rate]] (p. 494): information density of the joint law $P_{X,Y}$ (Definition 18.1, not restated on these pages); its upper tail ($i>\log\gamma$) enters the random-coding bounds [new]

## Candidate bridges

- [structural-analogy] Pierce's "language that the listener knows" ↔ uniform information density / efficient communication: an audience can take in only a small variety rate, so signals are paced and predictable. — from [[pierce-1980-introduction/ch13-information]] (information-theory → communication-theory)
- [structural-analogy] Random-coding exponent $\min_{Q}\min_P D(P_{\hat S|S}\|Q|P_S)=\phi_S(D)$ ↔ information-theory (channel coding): random-coding argument with information density and unsent codeword — same change-of-measure bound (pp. 494, 498; text cites Chapter 18). — from [[polyanskiy-2025-information/ch28-rate]] (information-theory → information-theory)

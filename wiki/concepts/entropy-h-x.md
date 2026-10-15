---
id: entropy-h-x
type: concept
fields: [information-theory]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [gibson-2019-efficiency/main, mackay-2003-information/ch05-symbol, mackay-2003-information/ch31-ising, pierce-1980-introduction/ch13-information, polyanskiy-2025-information/ch01-introduction]
raw_ids: [entropy-H-X]
generated_by: build_kg.py
---

# entropy-h-x

## Definitions in the sources

### information-theory

- [[gibson-2019-efficiency/main]] (p. 4): average surprisal of a random variable, as uncertainty about its value [as `entropy-H-X`]
- [[mackay-2003-information/ch05-symbol]] (p. 97): lower bound on expected length of any uniquely decodeable code
- [[mackay-2003-information/ch31-ising]] (p. 402): here called $S=\sum p\ln(1/p)$ and tied to $\ln Z$ and free energy (Ex. 31.1)
- [[pierce-1980-introduction/ch13-information]] (p. 252): here "variety/information rate" of a work, which must stay within human limits to be distinctive [as `entropy-H-X`]
- [[polyanskiy-2025-information/ch01-introduction]] (p. xviii): average, over outcomes, of the KL dissimilarity between prior and the posterior that puts all mass on the observed outcome [as `entropy-H-X`]

## Instances that use it

- [[noisy-channel-conditional-entropy]] — $H(X|Y)=h(\delta)$ for XOR noise — from [[polyanskiy-2025-information/ch02-entropy]]

## Candidate bridges

- [same-math] $-\sum\mu_iP_{ij}\log P_{ij}$ ↔ conditional entropy $H(X_2|X_1)$ under the stationary law — literally the same quantity. — from [[cover-2006-elements/ch04-entropy]] (information-theory → unspecified)

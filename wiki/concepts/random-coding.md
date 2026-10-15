---
id: random-coding
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p1, mackay-2003-information/ch10-noisy, polyanskiy-2025-information/ch13-fixed]
generated_by: build_kg.py
---

# random-coding

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p1]] (pp. 198, 202): proof technique: draw the codebook i.i.d. and average the error, to show a good code exists [new]
- [[mackay-2003-information/ch10-noisy]] (pp. 164–165): Shannon's method: average error over randomly drawn codes, so a good code must exist [new; work fields: information-theory, bayesian]
- [[polyanskiy-2025-information/ch13-fixed]] (pp. 215, 217): pick the codebook at random and show the average error is small, so a good code exists; non-constructive [new]

## Instances that use it

- [[birthday-problem]] — expected number of collisions S(S−1)/(2A) as insight for random coding — from [[mackay-2003-information/ch09-communication]]
- [[bernoulli-half-hamming-rd]] — $P_S=Q_{\hat S}=\mathrm{Ber}(1/2)$: random coding with $M=2^{n(1-h(D)+\delta)}$ achieves $\phi_S(D)=1-h(D)$ — from [[polyanskiy-2025-information/ch28-rate]]

## Candidate bridges

- [structural-analogy] Random-coding existence argument ↔ probabilistic method in combinatorics: average over random objects to prove one good object exists. — from [[cover-2006-elements/ch08-channel-p1]] (information-theory → other:mathematics)
- [structural-analogy] rate distortion $\min I(X;\hat X)$ s.t. distortion ↔ information-theory: channel capacity $\max I(X;Y)$ s.t. cost — dual optimizations with a random-coding proof and a shared alternating algorithm. — from [[cover-2006-elements/ch13-rate]] (information-theory → information-theory)
- [structural-analogy] Random-coding existence proof ↔ probabilistic method: if the average has a property, some member does (pp. 164, 166). — from [[mackay-2003-information/ch10-noisy]] (information-theory → other:mathematics)
- [structural-analogy] random-coding existence proof ↔ probabilistic method in combinatorics: an average over objects shows one object has the property. — from [[pierce-1980-introduction/ch08-noisy]] (information-theory → other:mathematics)
- [structural-analogy] random coding with a union bound here ↔ channel coding (Part IV): the text says data transmission is based on the same method (p. 215). — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → information-theory)
- [structural-analogy] Random-coding exponent $\min_{Q}\min_P D(P_{\hat S|S}\|Q|P_S)=\phi_S(D)$ ↔ information-theory (channel coding): random-coding argument with information density and unsent codeword — same change-of-measure bound (pp. 494, 498; text cites Chapter 18). — from [[polyanskiy-2025-information/ch28-rate]] (information-theory → information-theory)
- [structural-analogy] Random-coding proof (average over codes, so one good code exists) ↔ probabilistic existence arguments — from [[shannon-1948-mathematical/main-p1]] (information-theory → unspecified)

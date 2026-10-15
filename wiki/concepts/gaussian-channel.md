---
id: gaussian-channel
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch10-gaussian, mackay-2003-information/ch11-error]
generated_by: build_kg.py
---

# gaussian-channel

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch10-gaussian]] (p. 239): $Y=X+Z$ with i.i.d. $\mathcal N(0,N)$ noise independent of $X$, with average power constraint on the input [new]
- [[mackay-2003-information/ch11-error]] (p. 177): real input and output, $y=x+$ Normal$(0,\sigma^2)$ noise, discrete in time; also called AWGN [new; work fields: information-theory, bayesian]

## Instances that use it

- [[gaussian-channel-likelihood-ratio]] — $\exp(2xy_n/\sigma^2)$ — from [[mackay-2003-information/ch25-exact]]
- [[pulse-detection-gaussian-channel]] — the posterior of a binary source given a Gaussian-noise signal is a linear logistic function — from [[mackay-2003-information/ch39-single]]

## Candidate bridges

- [structural-analogy] Reverse water-filling for parallel Gaussians ↔ information-theory: water-filling power allocation for parallel Gaussian channels — only structurally similar here; the text does not state the channel version, so confirm before using. — from [[cover-2006-elements/ch13-rate]] (information-theory → information-theory)
- [structural-analogy] Gaussian compression noise var(X−X̂) = D ↔ information-theory: Gaussian channel noise N in $\tfrac12\log\frac{P+N}{N}$ — the chapter equates the two expressions (Eq. 8.28). — from [[stone-2022-information/ch08-rate]] (information-theory → information-theory)

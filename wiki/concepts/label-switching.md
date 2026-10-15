---
id: label-switching
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [blei-2017-variational/main-p1, gelman-2013-bda3/ch22-finite, murphy-2023-pml2/ch28-latent-p1, murphy-2023-pml2/ch29-state-p1]
generated_by: build_kg.py
---

# label-switching

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (p. 11): symmetric posterior modes from permuting cluster labels; one mode suffices for clusters or prediction [new]
- [[gelman-2013-bda3/ch22-finite]] (p. 533): likelihood is invariant to permuting component labels, so under an exchangeable prior the marginal posterior is identical for every component [new]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 939): permuting cluster labels leaves the likelihood unchanged, so cluster parameters are unidentifiable [new]
- [[murphy-2023-pml2/ch29-state-p1]] (p. 993): learned states permuted relative to the truth because of unidentifiability [new]

## Instances that use it

- [[svi-gmm-3-components]] — reparameterized SVI on a 3-component 2D mixture, with label switching — from [[murphy-2023-pml2/ch10-variational-p1]]
- [[two-component-gmm-label-switching]] — swapped means give equal likelihood — from [[murphy-2023-pml2/ch28-latent-p1]]

## Candidate bridges

- [structural-analogy] Label switching ↔ rotation unidentifiability in FA: both are symmetries of the likelihood that make some parameters meaningless — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → other)

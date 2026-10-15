---
id: total-correlation
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch28-latent-p2]
generated_by: build_kg.py
---

# total-correlation

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch05-information-p2]] (p. 241): $D_{KL}(p(\boldsymbol x)\|\prod_dp(x_d))$; non-negative [new; work fields: bayesian, information-theory]
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 976): $\sum_j\mathbb H(z_j)-\mathbb H(z)$; KL from joint to product of marginals [new]

## Instances that use it

- [[total-correlation-vae-chairs]] — latent dimensions for rotation, size, legs — from [[prince-2023-udl/ch17-variational]]

## Candidate bridges

- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → information-theory)

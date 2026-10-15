---
id: gaussian-mixture-model
type: concept
fields: [bayesian, linear-algebra]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [blei-2017-variational/main-p2, deisenroth-2020-mml/ch11-density, murphy-2023-pml2/ch28-latent-p1]
generated_by: build_kg.py
---

# gaussian-mixture-model

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p2]] (p. 29): diagonal-covariance mixture with Dirichlet, normal-gamma priors [new]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 930): mixture whose components are Gaussians; used for clustering and as a density model/prior [new]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (p. 349): density $\sum_k\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$, a convex combination of Gaussians; $K=1$ is a single Gaussian [new]

## Instances that use it

- [[gaussian-mixture-model]] — $k$-component mixture, the example for EM — from [[polyanskiy-2025-information/ch06-extremization]]

## Candidate bridges

- [structural-analogy] Gaussian HMM ↔ Gaussian mixture model: clusters of observations, but with Markov temporal dependence between cluster labels (p. 982). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → other)

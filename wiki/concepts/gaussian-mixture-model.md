---
id: gaussian-mixture-model
type: concept
fields: [bayesian, information-theory, linear-algebra]
fields_strong: [bayesian, information-theory, linear-algebra]
n_sources: 6
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [blei-2017-variational/main-p2, deisenroth-2020-mml/ch06-probability-p2, deisenroth-2020-mml/ch11-density, mackay-2003-information/ch21-exact, mackay-2003-information/ch22-maximum, murphy-2023-pml2/ch28-latent-p1]
aliases: [mixture-of-gaussians]
generated_by: build_kg.py
---

# gaussian-mixture-model

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `mixture-of-gaussians` — 3 digest(s)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p2]] (p. 29): diagonal-covariance mixture with Dirichlet, normal-gamma priors [new]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 930): mixture whose components are Gaussians; used for clustering and as a density model/prior [new]

### information-theory

- [[mackay-2003-information/ch21-exact]] (p. 298): density that is a weighted sum of Gaussians with weights summing to 1 [alias `mixture-of-gaussians`; new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch22-maximum]] (p. 302): density as weighted sum of Gaussians with unknown class labels [alias `mixture-of-gaussians`; new; work fields: information-theory, bayesian]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 202): weighted sum of densities (not of variables); moments in Theorem 6.12 [alias `mixture-of-gaussians`; new]
- [[deisenroth-2020-mml/ch11-density]] (p. 349): density $\sum_k\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$, a convex combination of Gaussians; $K=1$ is a single Gaussian [new]

## Instances that use it

- [[gaussian-mixture-model]] — $k$-component mixture, the example for EM — from [[polyanskiy-2025-information/ch06-extremization]]

## Candidate bridges

- [structural-analogy] Mixture-of-Gaussians resolution as an ill-posed inverse problem ↔ Bayesian: hierarchical models and regularizing priors — prior information selects among many consistent decompositions. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → bayesian)
- [same-math] Student-$t$ as a scale mixture of Gaussians ↔ heavy-tailed robust priors: marginal over unknown variance gives the $t$ (pp. 89, 100). — from [[murphy-2023-pml2/ch03-statistics-p2]] (bayesian → other:heavy-tailed-robust-priors)
- [structural-analogy] Gaussian HMM ↔ Gaussian mixture model: clusters of observations, but with Markov temporal dependence between cluster labels (p. 982). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → other:gaussian-mixture-model)

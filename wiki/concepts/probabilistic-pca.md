---
id: probabilistic-pca
type: concept
fields: [bayesian, linear-algebra]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch10-dimensionality, murphy-2023-pml2/ch28-latent-p1]
raw_ids: [probabilistic PCA]
generated_by: build_kg.py
---

# probabilistic-pca

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch28-latent-p1]] (p. 944): FA with orthogonal $W$ columns and $\Psi=\sigma^2I$; closed-form MLE; PCA as $\sigma^2\to0$ [new]

### linear-algebra

- [[deisenroth-2020-mml/ch10-dimensionality]] (pp. 340, 345): latent-variable model $x=Bz+\mu+\epsilon$ with $z\sim\mathcal N(0,I)$; PCA is its noise-free ML limit [as `probabilistic PCA`; new]

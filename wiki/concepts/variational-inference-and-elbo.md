---
id: variational-inference-and-elbo
type: concept
fields: [bayesian]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch23-normalizing]
generated_by: build_kg.py
---

# variational-inference-and-elbo

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p2]] (p. 182): mean-field VI mentioned for image denoising
- [[murphy-2023-pml2/ch23-normalizing]] (p. 831): here, ELBO (23.5) maximized with a flow as $q_\theta(z|x)$ via reparameterization

## Candidate bridges

- [same-math] VB lower bound $\mathrm E_g\log(p(\theta,y)/g)$ ↔ bayesian canon, variational inference and ELBO — same objective, up to the constant $\log p(y)$. — from [[gelman-2013-bda3/ch13-modal]] (bayesian → unspecified)

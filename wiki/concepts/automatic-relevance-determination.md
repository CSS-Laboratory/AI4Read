---
id: automatic-relevance-determination
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [blei-2017-variational/main-p2, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch28-latent-p1]
generated_by: build_kg.py
---

# automatic-relevance-determination

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p2]] (p. 27): a separate latent precision per regression coefficient shrinks irrelevant coefficients [new]
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 419): a separate relevance parameter for each distance dimension in the kernel [new]
- [[murphy-2023-pml2/ch15-generalized]] (p. 606): empirical-Bayes per-weight precisions; sparse via marginal likelihood [new]
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 949): prior that prunes irrelevant weights, used to estimate effective latent dimension [new]

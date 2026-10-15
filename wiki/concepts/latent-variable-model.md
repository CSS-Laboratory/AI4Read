---
id: latent-variable-model
type: concept
fields: [linear-algebra, bayesian, information-theory, llm]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch11-density, mackay-2003-information/ch34-independent, murphy-2023-pml2/ch28-latent-p1, prince-2023-udl/ch17-variational]
generated_by: build_kg.py
---

# latent-variable-model

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (pp. 275–276): extra unobserved z; the likelihood marginalizes it out (8.25) [new]
- [[deisenroth-2020-mml/ch11-density]] (pp. 363–365): model with unobserved variable $\boldsymbol z$; here discrete and one-hot, marginalized to give the likelihood [new]

### bayesian

- [[murphy-2023-pml2/ch28-latent-p1]] (p. 929): probabilistic model with variables that are always hidden; here a single layer $z$ with decoder $f(z)$ [new]

### information-theory

- [[mackay-2003-information/ch34-independent]] (p. 437): generative model where hidden variables, with simple distribution, give rise to observables [new]

### llm

- [[prince-2023-udl/ch17-variational]] (p. 327): model Pr(x,z) with hidden z, get Pr(x) by marginalizing z [new]

## Instances that use it

- [[error-correcting-code-as-latent-variable-model]] — source bits are latent; $\mathbf G$ normally known in advance — from [[mackay-2003-information/ch34-independent]]

## Candidate bridges

- [metaphor] "Latent concepts" as hidden causes of word choice ↔ latent-variable models in social science. — from [[deerwester-1990-lsa/main]] (linear-algebra → unspecified)
- [metaphor] Canonic components as latent "factors" ↔ latent-variable models in social science. — from [[eckart-1936-lowrank/main]] (linear-algebra → unspecified)
- [structural-analogy] Mismeasured confounder as surrogate for unmeasured confounder ↔ Bayesian latent-variable models: observed indicator of a latent true variable — both treat the data as noisy proxies of a hidden quantity. — from [[hernan-2020-whatif/ch09-measurement]] (bayesian → bayesian)
- [structural-analogy] Probit latent-variable model ↔ economic choice theory: threshold on a latent utility plus noise (p. 621). — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → economics-finance)

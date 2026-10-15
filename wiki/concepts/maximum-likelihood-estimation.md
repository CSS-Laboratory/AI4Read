---
id: maximum-likelihood-estimation
type: concept
fields: [linear-algebra, complex-systems, information-theory]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [clauset-2009-powerlaw/main-p1, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch11-density, mackay-2003-information/ch43-boltzmann]
generated_by: build_kg.py
---

# maximum-likelihood-estimation

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch08-when]] (pp. 265–267): minimize the negative log-likelihood (8.17) over θ [new]
- [[deisenroth-2020-mml/ch09-linear]] (p. 293): choose $\theta$ maximizing $p(\mathcal Y\mid\mathcal X,\theta)$; here it equals least squares [new]
- [[deisenroth-2020-mml/ch11-density]] (p. 351): choose $\boldsymbol\theta$ to maximize $\log p(\mathcal X\mid\boldsymbol\theta)$. For GMMs there is no closed form [new]

### complex-systems

- [[clauset-2009-powerlaw/main-p1]] (p. 5): choose parameters maximising the data's likelihood; here MLEs (3.1)–(3.7) for $\alpha$ [new]

### information-theory

- [[mackay-2003-information/ch43-boltzmann]] (p. 523): choosing $\mathbf W$ to maximize the likelihood, dropping the prior $P(\mathbf W)$ [new]

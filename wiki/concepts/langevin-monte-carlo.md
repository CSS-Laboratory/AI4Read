---
id: langevin-monte-carlo
type: concept
fields: [bayesian, information-theory, llm]
fields_strong: [bayesian, information-theory, llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch41-learning, murphy-2023-pml2/ch12-markov-p1]
generated_by: build_kg.py
---

# langevin-monte-carlo

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch12-markov-p1]] (pp. 521–522): HMC with $L=1$ (MALA); dropping the MH step gives an unadjusted update, and with $\Sigma=\mathbf I$, $\eta=\sqrt2$ the continuous-time limit is Langevin diffusion (ULA) [new]

### information-theory

- [[mackay-2003-information/ch41-learning]] (pp. 496, 498): gradient descent with noise plus accept/reject, with detailed balance [new; work fields: information-theory, bayesian, llm]

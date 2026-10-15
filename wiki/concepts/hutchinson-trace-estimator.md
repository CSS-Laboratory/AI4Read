---
id: hutchinson-trace-estimator
type: concept
fields: [llm, bayesian]
fields_strong: [llm, bayesian]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch23-normalizing, prince-2023-udl/ch16-normalizing]
generated_by: build_kg.py
---

# hutchinson-trace-estimator

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch23-normalizing]] (p. 843): $\mathrm{tr}(\mathbf M)\approx v^\top\mathbf Mv$, $v$ zero-mean unit-covariance [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch16-normalizing]] (p. 317): estimates trace by $\mathbb E[\epsilon^T A\epsilon]$ with random $\epsilon$ [new]

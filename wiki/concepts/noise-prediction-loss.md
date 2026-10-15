---
id: noise-prediction-loss
type: concept
fields: [llm, bayesian]
fields_strong: [llm, bayesian]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch25-diffusion, prince-2023-udl/ch18-diffusion]
generated_by: build_kg.py
---

# noise-prediction-loss

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch25-diffusion]] (p. 871): weighted least squares on $\epsilon$; $\lambda_t=1$ gives $L_{\text{simple}}$ [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch18-diffusion]] (p. eq. 18.40, p. 363): least-squares loss for predicting the noise added to data [new]

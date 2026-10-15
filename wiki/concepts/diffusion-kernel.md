---
id: diffusion-kernel
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

# diffusion-kernel

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch25-diffusion]] (p. 869): $q(x_t|x_0)=\mathcal N(\sqrt{\bar\alpha_t}x_0,(1-\bar\alpha_t)I)$ [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch18-diffusion]] (p. 353): closed-form $q(\mathbf z_t|\mathbf x)=\mathrm{Norm}[\sqrt{\alpha_t}\mathbf x,(1-\alpha_t)\mathbf I]$ [new]

---
id: diffusion-model
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

# diffusion-model

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch25-diffusion]] (p. 867): generative model: fixed noising chain plus learned denoising chain [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch18-diffusion]] (p. 349): generative model with a fixed noising encoder and a learned denoising decoder; latents have the data's size [new]

## Instances that use it

- [[hagerstrand-simulation]] — spatial diffusion model — from [[rogers-2003-diffusion/ch02-history-p3]]
- [[saucio-colombia-study]] — diffusion model applied in a peasant village. Composite score gives five categories — from [[rogers-2003-diffusion/ch07-innovativeness]]

## Candidate bridges

- [structural-analogy] DSM target $(x-\tilde x)/\sigma^2$ ↔ diffusion models' denoising (the text points to Section 25.3) (p. 857). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → unspecified)
- [structural-analogy] Diffusion models as hierarchical VAEs (p. 342) ↔ generative modeling: the next chapter's model class. — from [[prince-2023-udl/ch17-variational]] (llm → llm)

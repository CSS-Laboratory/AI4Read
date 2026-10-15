---
id: beta-vae
type: concept
fields: [bayesian, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch21-variational, prince-2023-udl/ch17-variational]
generated_by: build_kg.py
---

# beta-vae

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch21-variational]] (p. 797–798): ELBO with the KL scaled by $\beta$; $\beta<1$ less blur, $\beta>1$ more compression [new]

### llm

- [[prince-2023-udl/ch17-variational]] (p. 343): VAE whose KL term is multiplied by β > 1 [new]

## Instances that use it

- [[beta-vae-celeba-sunglasses]] — latent arithmetic with $s\in\{-2,\dots,2\}$ — from [[murphy-2023-pml2/ch20-generative]]

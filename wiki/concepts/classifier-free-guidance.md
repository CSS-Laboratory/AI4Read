---
id: classifier-free-guidance
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

# classifier-free-guidance

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch25-diffusion]] (p. 886): mix conditional and unconditional scores with weight $w$ [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch18-diffusion]] (p. 366): conditional model trained with randomly dropped labels; the conditional and unconditional outputs can be weighted [new]

## Candidate bridges

- [structural-analogy] Classifier-free guidance ↔ GAN truncation: both trade variety for typicality (the text says "somewhat analogous", p. 367). — from [[prince-2023-udl/ch18-diffusion]] (llm → other:gan-truncation)

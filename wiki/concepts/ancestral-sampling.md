---
id: ancestral-sampling
type: concept
fields: [llm, bayesian, linear-algebra]
fields_strong: [llm, bayesian, linear-algebra]
n_sources: 4
n_works: 3
tiers: [reference, core]
grounding: digests
sources: [deisenroth-2020-mml/ch11-density, murphy-2023-pml2/ch04-graphical-p1, prince-2023-udl/ch18-diffusion, prince-2023-udl/ch23-probability]
generated_by: build_kg.py
---

# ancestral-sampling

## Definitions in the sources

### llm

- [[prince-2023-udl/ch18-diffusion]] (p. 357): sampling $\mathbf z_T$, then each earlier latent in turn, up to $\mathbf x$ [new]
- [[prince-2023-udl/ch23-probability]] (p. 460): sample root variable, then each conditional in turn [new]

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p1]] (p. 154): sample nodes in topological order, each given its parents [new]

### linear-algebra

- [[deisenroth-2020-mml/ch11-density]] (p. 364): sample $\boldsymbol z\sim p(\boldsymbol z)$ first, then $\boldsymbol x\mid\boldsymbol z$ [new]

## Instances that use it

- [[ancestral-sampling-chain]] — $Pr(x)Pr(y|x)Pr(z|y)$ sampled in order — from [[prince-2023-udl/ch23-probability]]

## Candidate bridges

- [structural-analogy] g-formula simulation of $(Y^{\bar a},\bar L^{\bar a})$ and Monte Carlo of Technical Point 21.9 ↔ Bayesian computation: ancestral sampling from a sequential generative model, drawing each $L_k$ given the history set by the strategy. — from [[hernan-2020-whatif/ch21-g]] (bayesian → bayesian)
- [structural-analogy] Ancestral sampling over $T$ denoising steps ↔ LLM: autoregressive next-token sampling, both sequential draws that build a sample (our proposal). — from [[prince-2023-udl/ch18-diffusion]] (llm → llm)
- [structural-analogy] Ancestral sampling ↔ language models: autoregressive generation draws each token given earlier ones, like the chain in C.32. — from [[prince-2023-udl/ch23-probability]] (llm → llm)

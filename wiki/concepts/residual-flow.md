---
id: residual-flow
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

# residual-flow

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch23-normalizing]] (pp. 842–844): $f(u)=u+\mathbf F(u)$ invertible under conditions on $\mathbf F$, e.g. $\mathbf F$ contractive (guaranteed invertible), or with a low-rank Jacobian for a cheap determinant [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch16-normalizing]] (pp. 314–316): invertible residual layers, by reversal (iRevNet) or fixed-point iteration (iResNet) [new]

## Instances that use it

- [[planar-flow]] — $M=1$ low-rank residual flow; $\det=1+w^\top v\sigma'(\cdot)$ — from [[murphy-2023-pml2/ch23-normalizing]]
- [[iresnet]] — contractive residual flow with spectrally normalized convolutions — from [[murphy-2023-pml2/ch23-normalizing]]
- [[irevnet-iresnet]] — two residual-flow designs — from [[prince-2023-udl/ch16-normalizing]]

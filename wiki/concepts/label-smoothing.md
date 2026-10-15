---
id: label-smoothing
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch09-regularization, vaswani-2017-transformer/main]
generated_by: build_kg.py
---

# label-smoothing

## Definitions in the sources

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 150): train on targets with $1-\rho$ on the true class and the rest spread equally [new]
- [[vaswani-2017-transformer/main]] (p. 8): $\epsilon_{ls}=0.1$; hurts perplexity, improves accuracy and BLEU [new]

## Candidate bridges

- [metaphor] Label smoothing ↔ scoring rules that discourage extreme confidence in forecasting. — from [[prince-2023-udl/ch09-regularization]] (llm → unspecified)

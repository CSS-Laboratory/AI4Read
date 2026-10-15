---
id: dropout
type: concept
fields: [llm, bayesian]
fields_strong: [llm, bayesian]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch16-deep, prince-2023-udl/ch09-regularization]
generated_by: build_kg.py
---

# dropout

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch16-deep]] (pp. 636–637): random omission of units while training; ensemble view; weights scaled by $1-p$ at test [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch09-regularization]] (p. 147): randomly clamp hidden units to zero during training [new]

## Instances that use it

- [[mnist-batchbald]] — BALD vs BatchBALD with MC dropout, batch size 4 — from [[murphy-2023-pml2/ch34-decision]]
- [[dropout-kink-removal]] — three conspiring units cause a kink dropout removes — from [[prince-2023-udl/ch09-regularization]]

## Candidate bridges

- [structural-analogy] dropout ensemble ↔ Bayesian model averaging (Monte Carlo dropout, Ch. 17): both average over many networks; the chapter only points forward — from [[murphy-2023-pml2/ch16-deep]] (bayesian → bayesian)
- [structural-analogy] Dropout / Monte Carlo dropout ↔ ensembling: many sub-networks as an implicit ensemble. — from [[prince-2023-udl/ch09-regularization]] (llm → llm)
- [structural-analogy] Neighbourhood sampling ↔ dropout: the author calls it "reminiscent of dropout" (p. 254). — from [[prince-2023-udl/ch13-graph]] (llm → llm)

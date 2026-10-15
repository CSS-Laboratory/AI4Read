---
id: learning-to-learn
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch19-beyond, tenenbaum-2011-grow/main]
aliases: [learning-to-learn-overhypotheses]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# learning-to-learn

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `learning-to-learn-overhypotheses` — 0 digest(s)

## Canon spine entry

- **Learning to learn (overhypotheses)** (bayesian): hierarchical models that learn abstract priors which then speed up learning of specific cases (grad)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch19-beyond]] (p. 755): meta-learning as hierarchical Bayesian prediction from train to test split per task
- [[tenenbaum-2011-grow/main]] (p. 1282): here: transfer learning, acquiring inductive constraints from earlier related tasks

## Candidate bridges

- [metaphor] gene-pattern building R1 which builds R2 ↔ learning to learn: a design that builds the learner. — from [[ashby-1956-cybernetics/ch14-amplifying]] (control-theory → bayesian)
- [structural-analogy] Inner loop (in-context learning) / outer loop (SGD) ↔ ML: meta-learning, learning to learn across a distribution of tasks — the authors say the structure is the same, while staying agnostic on mechanism (p. 4, fn. 1) — from [[brown-2020-gpt3/main-p1]] (llm → llm)
- [metaphor] Amortized inference network ↔ learning to learn: one shared model replaces per-example optimization. — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → bayesian)

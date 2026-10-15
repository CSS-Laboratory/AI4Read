---
id: alignment-tax
type: concept
fields: [llm]
n_sources: 3
tiers: [core]
grounding: digests
sources: [ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3]
raw_ids: [alignment tax]
canon_spine: llm
generated_by: build_kg.py
---

# alignment-tax

## Canon spine entry

- **alignment tax** (llm): capability lost on standard benchmarks as a side effect of alignment training (grad)

## Definitions in the sources

### llm

- [[ouyang-2022-instructgpt/main-p1]] (pp. 3–4): lower performance on some tasks caused by alignment training (here SQuAD, DROP, HellaSwag, translation) [as `alignment tax`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 42): canon link; the unit reports "regressions on public NLP datasets" such as SQuADv2 and DROP, mitigated by pretraining gradients, without using this term
- [[ouyang-2022-instructgpt/main-p3]] (p. 51): here, regressions of PPO models on public NLP datasets, mitigated by pretraining mix

## Candidate bridges

- [metaphor] Alignment tax ↔ economic "tax" on adoption: a cost that discourages use of aligned models (the paper uses this reasoning, p. 14). — from [[ouyang-2022-instructgpt/main-p1]] (llm → economics-finance)

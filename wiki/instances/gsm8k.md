---
id: gsm8k
type: instance
fields: [llm]
n_sources: 2
tiers: [core]
grounding: digests
sources: [wei-2022-cot/main-p1, wei-2022-cot/main-p2]
canon_instance: [chain-of-thought-on-gsm8k]
canon_match_rule: same-work-tokens
generated_by: build_kg.py
---

# gsm8k

## Canon entry

- **Chain-of-thought on GSM8K** (llm): written-out reasoning lifts PaLM 540B to state of the art on grade-school math — wei-2022-cot

## Descriptions in the sources

### llm

- [[wei-2022-cot/main-p1]] (pp. 2, 20): the arithmetic benchmark with the lowest baseline here. PaLM 540B reaches 56.9% with chain of thought, against 17.9% standard [new]
- [[wei-2022-cot/main-p2]] (p. 25–28): math word problems used for the correct and incorrect chain analysis [new]

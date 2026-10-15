---
id: chain-of-thought
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 5
n_works: 4
tiers: [deep, core]
grounding: digests
sources: [bai-2022-constitutional/main, mahowald-2024-dissociating/main, wei-2022-cot/main-p1, wei-2022-cot/main-p2, wei-2022-emergent/main]
canon_spine: [llm]
generated_by: build_kg.py
---

# chain-of-thought

## Canon spine entry

- **chain-of-thought** (llm): prompting or training the model to generate intermediate reasoning steps before answering (UG)

## Definitions in the sources

### llm

- [[bai-2022-constitutional/main]] (p. 7, p. 11): "Let's think step-by-step" reasoning used for AI labelling; improves accuracy and transparency
- [[mahowald-2024-dissociating/main]] (p. 12): prompting to output intermediate steps before answering; partly bridges generalisation gaps
- [[wei-2022-cot/main-p1]] (p. 2): a series of natural-language intermediate reasoning steps leading to the final answer, shown in exemplars and produced by the model
- [[wei-2022-cot/main-p2]] (p. 24): reasoning steps the model writes before its answer; here contrasted with instructions (input) and NLEs (with or after the answer)
- [[wei-2022-emergent/main]] (p. 5): prompting the model to produce intermediate steps before the final answer

## Instances that use it

- [[gsm8k]] — the arithmetic benchmark with the lowest baseline here. PaLM 540B reaches 56.9% with chain of thought, against 17.9% standard — from [[wei-2022-cot/main-p1]]
- [[roger-tennis-balls]] — the Figure 1 exemplar contrasting standard and chain-of-thought answers — from [[wei-2022-cot/main-p1]]
- [[last-letter-concatenation]] — symbolic task; PaLM 540B reaches 99.4% in-domain with chain of thought — from [[wei-2022-cot/main-p1]]

## Candidate bridges

- [structural-analogy] critique-then-revise loop ↔ chain-of-thought as inference-time reasoning: both write intermediate text before the final output, and here the text is also training data. — from [[bai-2022-constitutional/main]] (llm → other:chain-of-thought-as)
- [structural-analogy] chain-of-thought prompting ↔ llm: scratchpads (Nye et al. 2021, cited here) — both have the model write intermediate steps before the answer (p. 9) — from [[wei-2022-cot/main-p1]] (llm → llm)
- [metaphor] chain of thought as extra computation per problem ↔ computation: time spent per instance — the paper says this holds "in principle" (p. 3), and its dots-only test does not support it as a sufficient cause (p. 6) — from [[wei-2022-cot/main-p1]] (llm → other:computer-science)

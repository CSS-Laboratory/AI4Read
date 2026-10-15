---
id: dpo
type: concept
fields: [llm]
n_sources: 1
tiers: [deep]
grounding: digests
sources: [rafailov-2023-dpo/main]
canon_spine: llm
generated_by: build_kg.py
---

# dpo

## Canon spine entry

- **DPO** (llm): RLHF rewritten as a closed-form classification loss on preference pairs, with no explicit reward model (grad)

## Definitions in the sources

### llm

- [[rafailov-2023-dpo/main]] (p. 2, Eq. 7 p. 4): Direct Preference Optimization: a classification loss on preference pairs that trains the policy, whose log-ratio to a reference is the implicit reward [new]

## Instances that use it

- [[tldr-summarization]] — Reddit TL;DR summarization with human preferences; DPO about 61% vs PPO 57% GPT-4 win rate — from [[rafailov-2023-dpo/main]]
- [[anthropic-hh-dialogue]] — single-turn helpful/harmless dialogue; DPO as the only efficient method improving over preferred completions — from [[rafailov-2023-dpo/main]]

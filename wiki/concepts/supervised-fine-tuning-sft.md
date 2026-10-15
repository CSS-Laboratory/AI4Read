---
id: supervised-fine-tuning-sft
type: concept
fields: [llm]
n_sources: 3
tiers: [core]
grounding: digests
sources: [ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3]
raw_ids: [supervised fine-tuning (SFT)]
canon_spine: llm
generated_by: build_kg.py
---

# supervised-fine-tuning-sft

## Canon spine entry

- **supervised fine-tuning (SFT)** (llm): fine-tuning on demonstrations of desired responses (UG)

## Definitions in the sources

### llm

- [[ouyang-2022-instructgpt/main-p1]] (p. 8): fine-tuning GPT-3 on labeler demonstrations; here run 16 epochs despite validation-loss overfitting after 1 [as `supervised fine-tuning (SFT)`]
- [[ouyang-2022-instructgpt/main-p2]] (pp. 40–41): fine-tuning GPT-3 on demonstrations; here 16 epochs, selected by RM score
- [[ouyang-2022-instructgpt/main-p3]] (p. 56): baseline fine-tuning on demonstrations. Also used as PPO's init model

---
id: supervised-fine-tuning
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 7
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [bai-2022-constitutional/main, ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3, rafailov-2023-dpo/main, wei-2022-cot/main-p2, ziems-2024-css/main-p1]
aliases: [supervised-fine-tuning-sft]
canon_spine: [llm]
generated_by: build_kg.py
---

# supervised-fine-tuning

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `supervised-fine-tuning-sft` — 3 digest(s)

## Canon spine entry

- **supervised fine-tuning (SFT)** (llm): fine-tuning on demonstrations of desired responses (UG)

## Definitions in the sources

### llm

- [[bai-2022-constitutional/main]] (p. 8): SL-CAI: fine-tuning a pretrained model on revised responses plus helpful RLHF samples
- [[ouyang-2022-instructgpt/main-p1]] (p. 8): fine-tuning GPT-3 on labeler demonstrations; here run 16 epochs despite validation-loss overfitting after 1 [as `supervised fine-tuning (SFT)`; alias `supervised-fine-tuning-sft`]
- [[ouyang-2022-instructgpt/main-p2]] (pp. 40–41): fine-tuning GPT-3 on demonstrations; here 16 epochs, selected by RM score [alias `supervised-fine-tuning-sft`]
- [[ouyang-2022-instructgpt/main-p3]] (p. 56): baseline fine-tuning on demonstrations. Also used as PPO's init model [alias `supervised-fine-tuning-sft`]
- [[rafailov-2023-dpo/main]] (pp. 3, 8): the first RLHF phase, giving $\pi^{\text{SFT}}$ (and Preferred-FT as a baseline)
- [[wei-2022-cot/main-p2]] (p. 25): prior intermediate-step work trains on annotated or synthetic steps; CoT needs no gradient updates
- [[ziems-2024-css/main-p1]] (p. 254): used for the RoBERTa-large and T5-base baselines

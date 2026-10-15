---
id: supervised-fine-tuning
type: concept
fields: [llm]
n_sources: 4
tiers: [deep, core]
grounding: digests
sources: [bai-2022-constitutional/main, rafailov-2023-dpo/main, wei-2022-cot/main-p2, ziems-2024-css/main-p1]
generated_by: build_kg.py
---

# supervised-fine-tuning

## Definitions in the sources

### llm

- [[bai-2022-constitutional/main]] (p. 8): SL-CAI: fine-tuning a pretrained model on revised responses plus helpful RLHF samples
- [[rafailov-2023-dpo/main]] (pp. 3, 8): the first RLHF phase, giving $\pi^{\text{SFT}}$ (and Preferred-FT as a baseline)
- [[wei-2022-cot/main-p2]] (p. 25): prior intermediate-step work trains on annotated or synthetic steps; CoT needs no gradient updates
- [[ziems-2024-css/main-p1]] (p. 254): used for the RoBERTa-large and T5-base baselines

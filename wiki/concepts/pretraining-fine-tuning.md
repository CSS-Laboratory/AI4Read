---
id: pretraining-fine-tuning
type: concept
fields: [llm]
n_sources: 14
tiers: [core, deep, reference]
grounding: digests
sources: [brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, devlin-2019-bert/main, hoffmann-2022-chinchilla/main, mahowald-2024-dissociating/main, ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, prince-2023-udl/ch09-regularization, prince-2023-udl/ch10-convolutional, prince-2023-udl/ch12-transformers, radford-2019-gpt2/main, wei-2022-cot/main-p1, xie-2022-icl/main, ziems-2024-css/main-p1]
raw_ids: [pretraining / fine-tuning]
canon_spine: llm
generated_by: build_kg.py
---

# pretraining-fine-tuning

## Canon spine entry

- **pretraining / fine-tuning** (llm): generic self-supervised training on huge text, followed by task-specific adaptation (UG)

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p1]] (pp. 3, 6): the paradigm the paper contrasts with: weights updated on thousands to hundreds of thousands of task examples
- [[brown-2020-gpt3/main-p2]] (pp. 33–34, 40): pretraining objective limits; multi-task fine-tuning contrasted with in-context use [as `pretraining / fine-tuning`]
- [[devlin-2019-bert/main]] (p. 4173): unsupervised pre-training, then all parameters are fine-tuned per task with a small output layer [as `pretraining / fine-tuning`]
- [[hoffmann-2022-chinchilla/main]] (p. 9): pre-training compute is traded against fine-tuning and inference costs
- [[mahowald-2024-dissociating/main]] (p. 6, 11): generic text-prediction training, then extra task-specific training; key for judging functional claims
- [[ouyang-2022-instructgpt/main-p1]] (p. 8): GPT-3 pretrained on web text, then fine-tuned in three steps [as `pretraining / fine-tuning`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 42): pretraining data is mixed into SFT (10%) and PPO (8× the episodes, weight $\gamma=27.8$)
- [[prince-2023-udl/ch09-regularization]] (p. 152): here: pre-train on a related task, then train new final layers or the whole model
- [[prince-2023-udl/ch10-convolutional]] (p. 177): YOLO is trained on ImageNet, then fine-tuned for detection [as `pretraining / fine-tuning`]
- [[prince-2023-udl/ch12-transformers]] (p. 219): self-supervised pre-training, then task-specific adaptation with labelled data [as `pretraining / fine-tuning`]
- [[radford-2019-gpt2/main]] (pdf 2): prior paradigm: transfer then supervised adaptation; the paper aims to skip the supervised step [as `pretraining / fine-tuning`]
- [[wei-2022-cot/main-p1]] (pp. 2, 9): used as a contrast: the paper's method needs no finetuning, only prompting
- [[xie-2022-icl/main]] (p. 2): here only the pretraining distribution is analysed, assumed fit exactly by the LM
- [[ziems-2024-css/main-p1]] (p. 263): here, instruction fine-tuning plus pretraining on text and code changes CSS accuracy more than size does in the OpenAI family

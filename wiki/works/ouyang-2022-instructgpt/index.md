---
id: ouyang-2022-instructgpt/index
work: ouyang-2022-instructgpt
type: work-map
units: [ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3]
---

# Ouyang, L., Wu, J., Jiang, X., et al. (2022). *Training language models to follow instructions with human feedback*. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). arXiv:2203.02155.

## In one paragraph
Language models trained only to predict the next token often fail to do what users want. They invent facts, produce toxic text, or ignore instructions. This paper fine-tunes GPT-3 in three steps. First, supervised learning on human demonstrations. Second, a reward model trained on human rankings of outputs. Third, reinforcement learning with PPO against that reward model, with a KL penalty that keeps the model close to the supervised one. The resulting InstructGPT models are preferred by labelers over much larger GPT-3 models: a 1.3B InstructGPT beats 175B GPT-3. Truthfulness improves, but bias does not, and simple mistakes remain. Mixing pretraining updates into PPO reduces the "alignment tax" on public benchmarks. The model is aligned to the preferences of a specific group of labelers, not to human values in general. The recipe underlies many chat assistants.

## The path through the work
- [[ouyang-2022-instructgpt/main-p1]] — Fine-tuning GPT-3 with human demonstrations, a reward model learned from human rankings, and PPO makes labelers prefer its outputs over those of a model 100x larger, while truthfulness improves and some harms and mistakes remain.
- [[ouyang-2022-instructgpt/main-p2]] — The appendices document where InstructGPT's prompts came from, how labelers were chosen and instructed, and the exact hyperparameters and design choices for supervised fine-tuning (SFT), the reward model (RM), PPO (the reinforcement-learning step) and the FLAN/T0 baselines (GPT-3 fine-tuned on the FLAN and T0 datasets).
- [[ouyang-2022-instructgpt/main-p3]] — The appendices show that RLHF with PPO alone lowers scores on several public NLP benchmarks, that mixing in pretraining updates mitigates this, and that a larger KL coefficient did not in a 1.3B test.

## Big ideas across units
- **The three-step recipe (SFT, reward model, PPO).** Introduced in main-p1 and given concrete data and hyperparameters in main-p2. main-p3 shows how the pieces behave in ablations. Units: main-p1, main-p2, main-p3.
- **Human preference data as the training signal.** Rankings are turned into pairwise comparisons for the reward model (main-p1, main-p2). Prompt sourcing, labeler screening and splits by organization are documented in main-p2. The reward model appears to generalize to held-out labelers (main-p3). Units: main-p1, main-p2, main-p3.
- **The alignment tax and the pretraining mix.** PPO alone regresses on public NLP datasets. Pretraining gradients (PPO-ptx) reduce this (main-p1). The coefficient is given in main-p2 and tested in main-p3. Units: main-p1, main-p2, main-p3.
- **The KL penalty keeps the policy near the SFT model.** It is described in main-p1, set to β = 0.02 in main-p2, and found in main-p3 not to fix regressions even at 100× the default. Units: main-p1, main-p2, main-p3.
- **Mixed safety results.** Truthfulness and closed-domain hallucination improve. Toxicity improves only when the model is prompted to be respectful. Bias does not improve (main-p1). The metrics behind these claims are defined in main-p3. Units: main-p1, main-p3.
- **Whose preferences, and helpfulness versus harmlessness.** The model is aligned to about 40 contractors and the researchers' instructions (main-p1). Labelers prioritized helpfulness in training and truthfulness and harmlessness in evaluation (main-p2). Samples show a helpfulness-first model answering a harmful request (main-p3). Units: main-p1, main-p2, main-p3.
- **Human-preference data versus public instruction datasets.** FLAN and T0 do less well than preference data on the API distribution (main-p1). How the baselines were trained is in main-p2. Units: main-p1, main-p2.

## How to read it
- **Essential:** main-p1. It holds the argument, the method, the headline result and the alignment-tax discussion. It is enough on its own for the core idea.
- **Appendix units, depend on main-p1:** main-p2 and main-p3 both assume the SFT → reward model → PPO pipeline from main-p1.
- **Read next if you want to reproduce or evaluate:** main-p2 covers data, labelers and hyperparameters. main-p3 covers the ablations of the pretraining mix and KL coefficient, the evaluation setups, and sample outputs.
- **Can be skipped on a first pass:** the details of labeler screening and the survey (main-p2), and the sample outputs and tuning choices (main-p3).
- main-p3 builds on the PPO-ptx idea from main-p1 and the γ and β settings from main-p2.

## Concepts introduced
- [[supervised-fine-tuning-sft]] — main-p1
- [[reward-model]] — main-p1
- [[bradley-terry-model]] — main-p1
- [[rlhf]] — main-p1
- [[kl-penalty]] — main-p1
- [[alignment-tax]] — main-p1
- [[pretraining-fine-tuning]] — main-p1
- [[zero-shot-few-shot-prompting]] — main-p1
- [[ppo-ptx]] — main-p1
- [[helpful-honest-harmless]] — main-p1
- [[preference-win-rate]] — main-p1
- [[misaligned-objective]] — main-p1
- [[bandit-environment]] — main-p1
- [[cross-entropy-log-loss]] — main-p1
- [[labeler-screening]] — main-p2
- [[helpful-truthful-harmless]] — main-p2
- [[org-level-split]] — main-p2
- [[pretraining-mix-ptx]] — main-p3
- [[entropy-bias-metric]] — main-p3

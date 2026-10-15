---
id: rlhf
type: concept
fields: [llm, bayesian]
n_sources: 10
tiers: [deep, core, reference]
grounding: digests
sources: [bai-2022-constitutional/main, mahowald-2024-dissociating/main, murphy-2023-pml2/ch22-autoregressive, ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3, prince-2023-udl/ch19-reinforcement, rafailov-2023-dpo/main, ziems-2024-css/main-p1, ziems-2024-css/main-p2]
raw_ids: [RLHF]
canon_spine: llm
generated_by: build_kg.py
---

# rlhf

## Canon spine entry

- **RLHF** (llm): optimizing a policy against a learned reward model with RL (e.g., PPO), usually with a KL penalty (grad)

## Definitions in the sources

### llm

- [[bai-2022-constitutional/main]] (p. 3): RL against a PM trained on human preference labels; here it is the baseline and the source of the helpful model
- [[mahowald-2024-dissociating/main]] (p. 2, 17): reinforcement learning used to impart human preferences; said to improve functional tasks
- [[ouyang-2022-instructgpt/main-p1]] (p. 2): use human preferences as a reward signal to fine-tune; here PPO against the RM [as `RLHF`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 42): PPO against the 6B RM, with a KL term and pretraining mix
- [[ouyang-2022-instructgpt/main-p3]] (pp. 56–58): PPO fine-tuning against a reward model. Here, its ablations: learning rate, batch size, init model
- [[prince-2023-udl/ch19-reinforcement]] (p. 399): reward model plus PPO training of chatbots, as described in the Notes [as `RLHF`]
- [[rafailov-2023-dpo/main]] (p. 3): three phases: SFT, reward learning, RL fine-tuning with a KL-penalized reward
- [[ziems-2024-css/main-p1]] (pp. 253, 263): training with human preference feedback (text-003, gpt-3.5-turbo); +3.5 mean F1 over davinci-002
- [[ziems-2024-css/main-p2]] (p. 266): human-feedback-tuned models (gpt-3.5-turbo, text-davinci-003); here they benefit generation tasks significantly

### bayesian

- [[murphy-2023-pml2/ch22-autoregressive]] (p. 825): RL fine-tuning against a ranking model so responses fit human intent [new]

## Instances that use it

- [[pareto-helpful-harmless-plot]] — Fig. 2: RL-CAI vs RLHF trade-off — from [[bai-2022-constitutional/main]]
- [[palms-hh-vs-rl-cai-samples]] — evasive HH RLHF refusals vs RL-CAI CoT explanations — from [[bai-2022-constitutional/main]]
- [[instructgpt-rlhf-pipeline]] — fine-tune, reward model, PPO — from [[prince-2023-udl/ch19-reinforcement]]

## Candidate bridges

- [metaphor] RLHF ranking model and CLIP critic ↔ likelihood × weighting in Bayes' theorem: both use an external score to steer or rank model output. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → bayesian)
- [structural-analogy] Policy network (p. 12–13) ↔ llm: RLHF policy optimized for reward — both map a state/context to actions under a reward signal (canon link; not stated in this unit). — from [[prince-2023-udl/ch01-introduction]] (llm → llm)
- [structural-analogy] RLHF's reward model + PPO (p. 399) ↔ llm: Bradley–Terry reward model and KL-penalised policy optimization (canon link; not stated in this unit). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)

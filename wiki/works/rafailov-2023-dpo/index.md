---
id: rafailov-2023-dpo/index
work: rafailov-2023-dpo
type: work-map
units: [rafailov-2023-dpo/main]
generated: deterministic
---

# Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., & Finn, C. (2023). *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). arXiv:2305.18290.

## One digest
This work has a single digest, which is also its work-level summary: [[rafailov-2023-dpo/main]].

## In one line
Under the Bradley–Terry preference model, the KL-constrained RLHF problem can be solved exactly by training the language model with a simple binary classification loss on preference pairs, with no separate reward model and no reinforcement learning.

## The gist
RLHF (reinforcement learning from human feedback) aligns a language model with human preferences by fitting a reward model and then running reinforcement learning (RL). This is complex and often unstable. The paper asks whether the same KL-constrained reward-maximization problem can be solved without either step. Answer: the reward can be rewritten as β times a log-ratio between the policy and a reference policy. The preference loss then becomes a classification loss on the policy itself. This is Direct Preference Optimization (DPO). In the authors' experiments on sentiment, summarization and dialogue (models up to 6B parameters), DPO performs as well as or better than PPO-based RLHF. It is also much simpler to implement and train.

**Prerequisites:** logistic/sigmoid function; maximum likelihood; KL divergence; the idea that a language model defines a policy π(y|x); basic RLHF vocabulary (reward model, PPO); sums over discrete outcomes; gradients of log-probabilities.

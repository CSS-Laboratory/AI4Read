---
id: reward-model
type: concept
fields: [llm]
n_sources: 6
tiers: [core, deep, reference]
grounding: digests
sources: [bai-2022-constitutional/main, ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3, prince-2023-udl/ch19-reinforcement, rafailov-2023-dpo/main]
raw_ids: [reward model]
canon_spine: llm
generated_by: build_kg.py
---

# reward-model

## Canon spine entry

- **reward model** (llm): a model trained on human pairwise preferences to score outputs (grad)

## Definitions in the sources

### llm

- [[bai-2022-constitutional/main]] (p. 5): the preference model (PM) scoring responses, trained on human helpfulness plus AI harmlessness comparisons
- [[ouyang-2022-instructgpt/main-p1]] (p. 8): SFT model minus unembedding layer, outputting a scalar for (prompt, response); only 6B used [as `reward model`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 41): 6B model with scalar head, trained on ranked comparisons for one epoch
- [[ouyang-2022-instructgpt/main-p3]] (p. 52): preference predictor. Here, its cross-labeler generalization is tested
- [[prince-2023-udl/ch19-reinforcement]] (p. 399): transformer scoring a prompt-response pair from human preferences [as `reward model`]
- [[rafailov-2023-dpo/main]] (p. 3): a network $r_\phi(x,y)$ fit by maximum likelihood on pairwise preferences (Eq. 2); DPO replaces it with an implicit one

## Instances that use it

- [[instructgpt-rlhf-pipeline]] — fine-tune, reward model, PPO — from [[prince-2023-udl/ch19-reinforcement]]

## Candidate bridges

- [structural-analogy] Pairwise preference modeling with sigmoid ↔ llm: Bradley–Terry reward models also use σ(·) to turn a score difference into a probability; the chapter shows only sigmoid-to-Bernoulli (canon link; not stated in this unit). — from [[prince-2023-udl/ch05-loss]] (llm → llm)
- [structural-analogy] Discriminator as learned critic for the generator ↔ llm: reward model scoring outputs — both are learned judges whose scores steer a generator — from [[prince-2023-udl/ch15-generative]] (llm → llm)
- [structural-analogy] RLHF's reward model + PPO (p. 399) ↔ llm: Bradley–Terry reward model and KL-penalised policy optimization (canon link; not stated in this unit). — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)

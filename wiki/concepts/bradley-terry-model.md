---
id: bradley-terry-model
type: concept
fields: [llm]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [ouyang-2022-instructgpt/main-p1, rafailov-2023-dpo/main]
raw_ids: [Bradley–Terry model]
canon_spine: llm
generated_by: build_kg.py
---

# bradley-terry-model

## Canon spine entry

- **Bradley–Terry model** (llm): P(A preferred to B) = σ(r(A) − r(B)); the preference model under RLHF and DPO (grad)

## Definitions in the sources

### llm

- [[ouyang-2022-instructgpt/main-p1]] (p. 8): eq. (1) uses $\sigma(r_w-r_l)$ as P(winner preferred); the paper describes it as "log odds" via Stiennon et al., without naming Bradley–Terry (canon link; not stated in this unit) [as `Bradley–Terry model`]
- [[rafailov-2023-dpo/main]] (p. 3): preference probability is the logistic function of the reward difference (Eq. 1)

---
id: kl-penalty
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 4
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [ouyang-2022-instructgpt/main-p1, ouyang-2022-instructgpt/main-p2, ouyang-2022-instructgpt/main-p3, rafailov-2023-dpo/main]
raw_ids: [KL penalty]
canon_spine: [llm]
generated_by: build_kg.py
---

# kl-penalty

## Canon spine entry

- **KL penalty** (llm): a term keeping the fine-tuned policy close to the reference model, measured by KL divergence (grad)

## Definitions in the sources

### llm

- [[ouyang-2022-instructgpt/main-p1]] (p. 9): per-token penalty from the SFT model to curb RM over-optimisation, coefficient $\beta$ [as `KL penalty`]
- [[ouyang-2022-instructgpt/main-p2]] (p. 42): KL reward against the SFT model with $\beta=0.02$
- [[ouyang-2022-instructgpt/main-p3]] (p. 53): reward-side KL term with coefficient β against a reference model. Here, raising it to 100× the default did not fix regressions on the 1.3B model
- [[rafailov-2023-dpo/main]] (p. 4): the β-weighted KL term in Eq. 3 that keeps $\pi_\theta$ near $\pi_{\text{ref}}$ and preserves diversity

## Candidate bridges

- [same-math] KL divergence inside $D_{JS}$ (eq. 15.9) ↔ llm: KL penalty — same divergence $D_{KL}$, here used between a distribution and a mixture — from [[prince-2023-udl/ch15-generative]] (llm → llm)
- [same-math] KL term in ELBO ↔ llm (KL penalty): the same KL divergence between two distributions, though used for a different purpose. — from [[prince-2023-udl/ch17-variational]] (llm → llm)

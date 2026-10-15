---
id: mixture-of-experts
type: concept
fields: [llm, control-theory]
n_sources: 3
tiers: [deep, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p5, elhage-2022-superposition/main-p2, wei-2022-emergent/main]
generated_by: build_kg.py
---

# mixture-of-experts

## Definitions in the sources

### llm

- [[elhage-2022-superposition/main-p2]] (§ "Approach 1"): neurons grouped in blocks that rarely activate, so more neurons per flop [new]
- [[wei-2022-emergent/main]] (pp. 2, 10): sparse models with more parameters per unit of compute than dense models [new]

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p5]] (p. 429): several policies plus on-line change detection and gating to select among them [new]

## Candidate bridges

- [structural-analogy] Mixture of experts with gating ↔ control-theory: multiple-model adaptive control — switch among controllers when the plant changes — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → control-theory)
- [structural-analogy] Mixture of Experts ↔ neuron sparsity exploited as free flops, competing with superposition. — from [[elhage-2022-superposition/main-p2]] (llm → unspecified)

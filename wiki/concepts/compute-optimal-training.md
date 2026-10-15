---
id: compute-optimal-training
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 3
n_works: 3
tiers: [deep, core]
grounding: digests
sources: [hoffmann-2022-chinchilla/main, kaplan-2020-scaling/main, wei-2022-emergent/main]
canon_spine: [llm]
generated_by: build_kg.py
---

# compute-optimal-training

## Canon spine entry

- **compute-optimal training** (llm): splitting a fixed compute budget between model size and data (Chinchilla) (grad)

## Definitions in the sources

### llm

- [[hoffmann-2022-chinchilla/main]] (p. 2): choosing parameters $N$ and tokens $D$ to minimize final loss for a fixed FLOP budget (Eq. 1)
- [[kaplan-2020-scaling/main]] (p. 5, p. 16): allocating a fixed compute budget among model size, batch size and steps; here the answer is mostly model size, $N\propto C_{\min}^{0.73}$
- [[wei-2022-emergent/main]] (pp. 10–11): Hoffmann et al.'s argument that more training data is needed than earlier work implied; the paper cites it for data scaling

## Candidate bridges

- [same-math] Compute accounting (2 flops × 3 for backward = 6 per parameter per token) ↔ llm: compute-optimal training — the same per-token flop count is used to budget compute versus data. — from [[brown-2020-gpt3/main-p2]] (llm → llm)

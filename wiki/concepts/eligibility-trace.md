---
id: eligibility-trace
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch12-eligibility, sutton-2018-rl/ch14-psychology, sutton-2018-rl/ch15-neuroscience-p2]
generated_by: build_kg.py
---

# eligibility-trace

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch12-eligibility]] (p. 287, 292): a fading short-term memory vector $\mathbf z_t$ (same size as $\mathbf w$) marking which weights recently contributed to value estimates [new]
- [[sutton-2018-rl/ch14-psychology]] (pp. 350, 362): decaying trace of past states; like Hull's stimulus traces; introduced by Klopf as synaptic traces, which are more complex than the exponential traces used here [new]
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 399): synapse-local decaying record of past activity that lets a later reinforcement signal change it [new]

## Candidate bridges

- [structural-analogy] eligibility trace ↔ control-theory: fading-memory (exponentially weighted) filter of past inputs — both keep a decaying sum of past signals, with decay set by one parameter. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
- [same-math] eligibility trace $z_t=\gamma\lambda z_{t-1}+g_t$ ↔ signal processing: a first-order exponentially decaying (low-pass) sum of past inputs. — from [[sutton-2018-rl/ch15-neuroscience-p2]] (control-theory → other:signal-processing)

---
id: pomdp
type: concept
fields: [control-theory, theory-of-mind]
fields_strong: [control-theory, theory-of-mind]
n_sources: 3
n_works: 2
tiers: [reference, deep]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch02-approximation-p6, rabinowitz-2018-machine-tom/main]
raw_ids: [POMDP]
canon_spine: [theory-of-mind]
generated_by: build_kg.py
---

# pomdp

## Canon spine entry

- **POMDP** (theory-of-mind): partially observable Markov decision process: planning under uncertainty about the world state, used to model agents with beliefs (grad)

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 98): partially observed Markovian decision problem; solving exactly is typically intractable [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 309): partially observed MDP; here the special case of a perfectly observed $x_k$ plus a constant hidden $\theta$ [new]

### theory-of-mind

- [[rabinowitz-2018-machine-tom/main]] (pdf 2): environment family with rewards and observation functions attached to agents [as `POMDP`]

## Instances that use it

- [[pipeline-repair-pomdp]] — case study of approximate rollout and PI [BBW20] — from [[bertsekas-2026-rlcourse/ch03-learning-p2]]
- [[pomdp-belief-discretization]] — representative beliefs and convex-combination weights give a finite aggregate problem — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]
- [[pomdp-belief-state]] — the belief vector as a Markov state — from [[sutton-2018-rl/ch17-frontiers]]

## Candidate bridges

- [structural-analogy] relevance problem (what to feed into mindreading) ↔ inverse planning / POMDP: the modeller must specify the state space, priors and goals before inference — the chapter says theories treat this as given. — from [[apperly-2011-mindreaders/ch07-elaborating]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Finite-history state for POMDP ↔ sequence models: the author states that this is how LLMs such as ChatGPT work. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → other:sequence-models)
- [structural-analogy] notional world as the world an agent takes itself to be in ↔ theory-of-mind/POMDP: an agent's belief state about the world — both describe an agent by what it takes the world to be like. — from [[dennett-1987-intentional-stance/ch05-beyond-p2]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Child's two models (own knowledge vs protagonist's belief) ↔ POMDP / BToM: agent's belief state kept distinct from the world state — both separate what is true from what the agent represents. — from [[wimmer-1983-beliefs-about-beliefs/main]] (theory-of-mind → theory-of-mind)

---
id: random-surfer
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [brin-1998-anatomy/main, bryan-2006-eigenvector/main]
generated_by: build_kg.py
---

# random-surfer

## Definitions in the sources

### linear-algebra

- [[brin-1998-anatomy/main]] (pdf 4): a model user who follows links and restarts randomly; visit probability is PageRank [new]
- [[bryan-2006-eigenvector/main]] (p. 10): probabilistic reading of $q$ as long-run visiting frequency [new]

## Instances that use it

- [[random-surfer-model]] — behavioural justification of PageRank — from [[brin-1998-anatomy/main]]
- [[map-of-science-s3]] — 88-field partition, ranked by random-surfer visits — from [[rosvall-2008-maps/main-p2]]

## Candidate bridges

- [structural-analogy] random surfer with restarts ↔ linear-algebra: Markov chain, steady-state eigenvector — the paper ties PageRank to a principal eigenvector but gives no derivation. — from [[brin-1998-anatomy/main]] (linear-algebra → linear-algebra)
- [same-math] Random surfer with teleportation ↔ web search: PageRank steady-state distribution. — from [[rosvall-2008-maps/main-p1]] (information-theory → other:computer-science)
- [metaphor] Random surfer visiting fractions ↔ information-theory: how often a source emits each symbol, which sets ideal code lengths. — from [[rosvall-2008-maps/main-p2]] (information-theory → information-theory)

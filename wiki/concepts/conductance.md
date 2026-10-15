---
id: conductance
type: concept
fields: [linear-algebra, bayesian]
n_sources: 5
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch12-markov-p2, spielman-2025-sagt/ch16-lov, spielman-2025-sagt/ch20-graph, spielman-2025-sagt/ch21-cheeger, spielman-2025-sagt/ch22-local]
generated_by: build_kg.py
---

# conductance

## Definitions in the sources

### linear-algebra

- [[spielman-2025-sagt/ch16-lov]] (p. 144): φ(S) = |∂(S)| / (d·min(|S|, n−|S|)) on a d-regular graph [new]
- [[spielman-2025-sagt/ch20-graph]] (p. 173): $\phi(S)=w(\partial S)/\min(d(S),d(V-S))$ [new]
- [[spielman-2025-sagt/ch21-cheeger]] (p. 177): $\phi(S)=w(\partial S)/\min(d(S),d(V-S))$ [new]
- [[spielman-2025-sagt/ch22-local]] (p. 183): $\phi(S)=w(\partial S)/d(S)$ [new]

### bayesian

- [[murphy-2023-pml2/ch12-markov-p2]] (p. 526): bottleneck measure (12.96); low conductance implies high mixing time [new]

## Instances that use it

- [[hodgkin-huxley-neuron]] — conductance-based neuron model — from [[astrom-2021-feedbacksystems/ch03-system-p2]]
- [[parallel-resistors]] — conductances add — from [[spielman-2025-sagt/ch17-monotonicity]]

## Candidate bridges

- [metaphor] Rayleigh monotonicity ↔ stiffer springs give a stiffer whole — an intuition for "more edge weight, more conductance". — from [[spielman-2025-sagt/ch12-effective]] (linear-algebra → unspecified)
- [metaphor] Conductance ↔ random walks: a low-conductance set traps a walker for a long time. The text only says conductance is useful for random walks (p. 173). — from [[spielman-2025-sagt/ch20-graph]] (linear-algebra → other)

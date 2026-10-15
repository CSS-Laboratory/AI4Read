---
id: kinematic-graph
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch02-change, ashby-1956-cybernetics/ch03-determinate]
generated_by: build_kg.py
---

# kinematic-graph

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch02-change]] (p. 22): arrows from each state to its one-step transform; shows long-run fates [new]
- [[ashby-1956-cybernetics/ch03-determinate]] (p. 29): graph of arrows operand → transform. Equilibrium = no outgoing arrow, cycle = circuit [new]

## Instances that use it

- [[kinematic-graph-u-and-t]] — worked graphs with a stopping state, cycles and several basins — from [[ashby-1956-cybernetics/ch02-change]]

## Candidate bridges

- [structural-analogy] Repeated transformation and trajectory on the kinematic graph ↔ control-theory: state evolution of a discrete-time system, with the initial state set and then left to run without input (the text calls the correspondence "analogous"). — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → control-theory)
- [same-math] Kinematic graph of a single-valued transformation ↔ graph theory: the directed graph of a function on a finite set, where each point has one outgoing arrow. — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → other:graph-theory)

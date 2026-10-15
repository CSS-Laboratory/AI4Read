---
id: functional-equation
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch03-iii]
generated_by: build_kg.py
---

# functional-equation

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 11): an equation in which the unknown function appears on both sides, such as (8.1) [new]
- [[bellman-1957-dp/ch01-i-p3]] (p. 40): equation for $f_N(x)$ in terms of $f_{N-1}$ (or $f$ itself) that solves a multi-stage problem [new]
- [[bellman-1957-dp/ch03-iii]] (pp. 84–86): equation for the return function in terms of itself, e.g. (4.3), (4.5), (5.2) [new]

## Candidate bridges

- [same-math] Discrete functional equation (4.2) ↔ RL: Bellman optimality equation for a deterministic MDP with action-dependent immediate payoff. — from [[bellman-1957-dp/ch06-vi]] (control-theory → control-theory)
- [structural-analogy] Max-Min functional equation ↔ control-theory: Bellman equation of a one-person problem — replacing $\max$ by $\max\min$ keeps the "payoff plus value of next state" form. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)

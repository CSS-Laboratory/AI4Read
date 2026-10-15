---
id: katz-bonacich-centrality
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 1
n_works: 1
tiers: [core]
grounding: digests
sources: [bonacich-1987-power/main]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# katz-bonacich-centrality

## Canon spine entry

- **Katz–Bonacich centrality** (linear-algebra): (I − βA)⁻¹ counts all walks with decay β (grad)

## Definitions in the sources

### linear-algebra

- [[bonacich-1987-power/main]] (pp. 1173, 1174, fn. 7): c(α,β)=α(I−βR)⁻¹R1, a walk count weighted by βᵏ; here β may also be negative

## Candidate bridges

- [same-math] $(I-T)^{-1}=I+T+\dots+T^{m-1}$ for nilpotent $T$ (Exercise 8A.17) ↔ linear-algebra: Katz–Bonacich centrality $(I-\beta A)^{-1}$ for an acyclic-graph adjacency matrix (finite walk count) — same Neumann series. — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [structural-analogy] $(I-B)^{-1}=I+\sum B^i$ ↔ Katz–Bonacich centrality: both are walk-counting series. — from [[spielman-2025-sagt/ch11-walks]] (linear-algebra → linear-algebra)

---
id: zero-error-capacity
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 3
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p2, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch25-channel]
raw_ids: [zero-error capacity]
generated_by: build_kg.py
---

# zero-error-capacity

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p2]] (pp. 209, 222): bits per use transmittable with zero error probability; zero for the BSC [new]
- [[polyanskiy-2025-information/ch21-channel]] (p. 374): $C_0=\liminf\frac1n\log M^*(n,0)$ [as `zero-error capacity`; new]
- [[polyanskiy-2025-information/ch25-channel]] (pp. 450–451): rate with $\epsilon=0$; with feedback $C_{fb,0}=\max_{P_X}\min_y\log\frac1{P_X(S_y)}$ [new]

## Instances that use it

- [[binary-symmetric-channel]] — zero-error capacity 0; repetition code has rate $\to0$ — from [[cover-2006-elements/ch08-channel-p2]]
- [[polygon-channel]] — zero-error capacities with and without feedback; pentagon — from [[polyanskiy-2025-information/ch25-channel]]

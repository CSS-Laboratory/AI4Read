---
id: finite-state-machine
type: concept
fields: [control-theory, information-theory]
n_sources: 5
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, pierce-1980-introduction/ch03-mathematical, pierce-1980-introduction/ch06-language]
raw_ids: [finite state machine]
generated_by: build_kg.py
---

# finite-state-machine

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch01-introduction]] (p. 1-21): logic that switches the controller between modes [as `finite state machine`; new]
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (pp. 3-8, 3-18): discrete modes with guarded transitions; with continuous dynamics too
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-5): discrete-mode logic, e.g. Off/Standby/Cruise/Hold [new]

### information-theory

- [[pierce-1980-introduction/ch03-mathematical]] (p. 62): machine with finitely many states, moving between them by random transitions (p. 54) or input-driven transitions [new]
- [[pierce-1980-introduction/ch06-language]] (pp. 111–112, 115): a machine that is in a particular state at each point and moves to another state. Chomsky rejects it as a possible or proper model of English grammar, but Pierce notes that his grammar with a bounded sentence length corresponds to one [new]

## Instances that use it

- [[traffic-light-controller]] — four-state finite state machine — from [[astrom-2021-feedbacksystems/ch03-system-p1]]
- [[finite-state-machine-fig-iii-1]] — coin-driven machine producing "COMMUNIST PARTY" sentences — from [[pierce-1980-introduction/ch03-mathematical]]
- [[reverse-after-z-process]] — a sequence rule with unbounded long-range order that no finite-state machine can follow — from [[pierce-1980-introduction/ch06-language]]
- [[fsm-investor-competitiveness]] — LZ-based investing vs finite-state-machine investors — from [[polyanskiy-2025-information/ch15-universal]]

## Candidate bridges

- [structural-analogy] syndrome-as-state ↔ information-theory: a parity-check constraint turned into a finite-state machine. — from [[mackay-2003-information/ch25-exact]] (information-theory → information-theory)
- [same-math] finite-state machine with coin-flip transitions ↔ probability: Markov chain with given transition probabilities (here, 1/2 per arrow) — from [[pierce-1980-introduction/ch03-mathematical]] (information-theory → other)
- [metaphor] man as a possible finite-state machine with a fantastic number of states, beside a gas whose many molecular configurations are summarised by pressure and temperature ↔ statistical physics: summarising many micro-states by a few variables (p. 62) — from [[pierce-1980-introduction/ch03-mathematical]] (information-theory → complex-systems)

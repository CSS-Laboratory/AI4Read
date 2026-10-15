---
id: black-box
type: concept
fields: [control-theory, information-theory]
fields_strong: [control-theory]
n_sources: 5
n_works: 2
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch02-change, ashby-1956-cybernetics/ch06-black, ashby-1956-cybernetics/ch08-transmission, ashby-1956-cybernetics/ch13-regulating, meadows-2008-thinking/ch04-systems]
raw_ids: [black box]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# black-box

## Canon spine entry

- **black box** (control-theory): a system known only through its input–output behavior (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch02-change]] (p. 11): the idea that one can know a transformation without knowing the cause of change; this id is the nearest canon link, and the text does not use the term [as `black box`; weak: not really used in this unit]
- [[ashby-1956-cybernetics/ch06-black]] (p. 87): a system known only through chosen inputs and observed outputs, with a casing temporarily accepted
- [[ashby-1956-cybernetics/ch08-transmission]]: not named in this unit [as `black box`; weak: not really used in this unit; work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch13-regulating]] (p. 255): a system whose contents are unknown but whose output is known to respond to an input such as a switch. Setting the switch to get the desired behaviour is design in a Black Box [as `black box`]
- [[meadows-2008-thinking/ch04-systems]] (p. 88): a system known only by its inputs and outputs; events are its outputs [as `black box`]

## Instances that use it

- [[black-box-roulette-wheel]] — a device that fires with a daily known probability and cannot be stopped — from [[schelling-1960-conflict/ch08-threat]]
- [[black-box-amplification]] — majority vote over $t+1$ correlated runs has error $\le(2/\sqrt5)^{t+1}$ — from [[spielman-2025-sagt/ch31-psrgs]]

## Candidate bridges

- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [structural-analogy] Black box / input–output pairs (Boulding) ↔ control-theory: black-box identification — behavior-level models fail when structure changes, like fitted input–output models. — from [[meadows-2008-thinking/ch04-systems]] (control-theory → control-theory)

---
id: rao-blackwellization
type: concept
fields: [bayesian, control-theory]
fields_strong: [bayesian, control-theory]
n_sources: 4
n_works: 3
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch11-monte, robert-2011-mcmc/main, sarkka-2023-bayesianfiltering/ch11-particle, sarkka-2023-bayesianfiltering/ch17-epilogue]
generated_by: build_kg.py
---

# rao-blackwellization

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch11-monte]] (p. 494–495): replace a sample by its conditional expectation to lower variance [new]
- [[robert-2011-mcmc/main]] (p. 6): technique used by Gelfand and Smith (1990); its validity for Gibbs sampling was established by Liu, Wong and Kong [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch11-particle]] (p. 247): compute part of the filter analytically, sample the rest, lower variance [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 350): marginalizing out states or parameters exactly or approximately, preferred to sampling [new; work fields: control-theory, bayesian]

## Candidate bridges

- [same-math] Rao-Blackwellization (law of iterated variance) ↔ statistics: conditioning never increases variance — the same identity (11.55). — from [[murphy-2023-pml2/ch11-monte]] (bayesian → other:statistics)
- [structural-analogy] Rao-Blackwellization ↔ variance reduction by analytic integration — replace sampling with a conditional expectation where possible (p. 557). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → unspecified)

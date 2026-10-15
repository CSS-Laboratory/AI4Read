---
id: ancillary-statistic
type: concept
fields: [information-theory, bayesian]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [hernan-2020-whatif/ch10-random, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch17-principles-p2]
generated_by: build_kg.py
---

# ancillary-statistic

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch08-sufficiency]] (pp. 253–255): $z$ with $p(z|\theta I)=p(z|I)$; equivalent to $p(\theta|ZI)=p(\theta|I)$; conditioning on it leaves the likelihood unchanged if $z$ is a function of the data [new]
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 551): conditioning on it is Fisher's remedy; Jaynes says it is equivalent to Bayes when possible [new]

### bayesian

- [[hernan-2020-whatif/ch10-random]] (pp. 145–146): S-ancillary: the data's distribution given the statistic depends on the parameter of interest, while the statistic's own density shares no parameters with it; exact (known marginal distribution) vs approximate [new]

## Candidate bridges

- [structural-analogy] Marginalization (B₁ vs B₂) ↔ Bayesian: sufficiency and ancillary statistics — a statistic whose sampling distribution is free of the nuisance parameter is the structure DSZ exploit. — from [[jaynes-2003-probability/ch15-paradoxes]] (information-theory → bayesian)

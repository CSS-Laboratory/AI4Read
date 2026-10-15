---
id: frequentist-vs-bayesian
type: concept
fields: [bayesian, information-theory]
n_sources: 25
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/appb-mathematical, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch10-physics, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch24-exact, mackay-2003-information/ch37-bayesian, mcelreath-2020-rethinking/ch01-golem, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/front-preface, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch07-tool, mcgrayne-2011-theory/ch08-jerome, mcgrayne-2011-theory/ch09-there, mcgrayne-2011-theory/ch11-business, mcgrayne-2011-theory/ch12-who, mcgrayne-2011-theory/ch13-cold, mcgrayne-2011-theory/ch14-three, mcgrayne-2011-theory/ch15-navy, mcgrayne-2011-theory/ch16-eureka, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch02-buccaneers]
generated_by: build_kg.py
---

# frequentist-vs-bayesian

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch01-golem]] (p. 11): frequentist: probability as frequency, uncertainty via imagined resampling; Bayesian: probability as plausibility, for any uncertainty
- [[mcelreath-2020-rethinking/ch02-small]] (pp. 26, 34–35, 44): the author stresses similarities (likelihood central; MLE ≈ quadratic approximation; penalised likelihood ≈ regularising prior) alongside differences
- [[mcelreath-2020-rethinking/front-preface]] (p. xii): here only a note: avoiding significance testing is not uniquely Bayesian
- [[mcgrayne-2011-theory/app-appendixes]] (pp. 253–254): presented satirically as two "religions"
- [[mcgrayne-2011-theory/ch02-man]] (p. 31): Laplace's switch, after 1810, to a frequency-based approach
- [[mcgrayne-2011-theory/ch03-many]] (p. 36): frequency of events vs degree of belief; here treated as opposites, though Laplace saw them as equivalent
- [[mcgrayne-2011-theory/ch07-tool]] (pp. 99, 105): frequentism as ad hoc tests about frequencies and groups; Bayes as a unified rule that also handles one-off events
- [[mcgrayne-2011-theory/ch08-jerome]] (p. 116): Cornfield saw frequentist trial rules as rigid
- [[mcgrayne-2011-theory/ch09-there]] (pp. 121, 123): on McGrayne's account, Fisher's relative-frequency view gave zero risk after zero accidents; Bayes allowed doubt
- [[mcgrayne-2011-theory/ch11-business]] (pp. 142, 145): McGrayne's contrast: error rates and accept/reject vs probabilities for unknowns
- [[mcgrayne-2011-theory/ch12-who]] (pp. 156–157): Mosteller accepted both kinds of probability, and compared both methods empirically
- [[mcgrayne-2011-theory/ch13-cold]] (pp. 169–170): Tukey criticised Fisher's frequency methods even more sharply than Bayesian methods, and warned against using Bayes everywhere
- [[mcgrayne-2011-theory/ch14-three]] (p. 180): frequentists did not assign probability distributions to unknowns
- [[mcgrayne-2011-theory/ch15-navy]] (p. 209): Hilborn's contrast: Bayesians can ask how much each alternative is believed
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 232): here the author sees practice, not new philosophy, as the driver of change: Bayes "finally worked"
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 23–24): not treated here; Bayesian networks are previewed only
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 89–90): Bayesians admit subjective probabilities. Frequentists resisted, and Bayesian analysis was later accepted

### information-theory

- [[jaynes-2003-probability/appb-mathematical]] (p. 674): Jaynes says confidence intervals are satisfactory only where they match Bayesian intervals
- [[jaynes-2003-probability/ch06-elementary-p2]] (pp. 192, 195–196): here "orthodox" statistics is criticised for lacking priors and nuisance integration
- [[jaynes-2003-probability/ch09-repetitive-p1]] (pp. 280, 284): Jaynes: frequentist theory is functionally $I_0$ reasoning and ignores prior information
- [[jaynes-2003-probability/ch10-physics]] (p. 336): here a contrast between probability as frequency/physical property and as state of knowledge
- [[mackay-2003-information/ch02-probability]] (p. 26): probabilities only for random variables vs. also for beliefs about unknowns
- [[mackay-2003-information/ch03-more]] (pp. 50–51, 64): author contrasts estimators, tests and p-values with the single Bayesian posterior
- [[mackay-2003-information/ch24-exact]] (p. 320): sampling theory chooses estimators by sampling criteria; Bayesian answers are posterior distributions
- [[mackay-2003-information/ch37-bayesian]] (p. 457): here "sampling theory" judges methods by long-run behaviour over repeated experiments, and "Bayesian" computes probabilities of hypotheses given the data

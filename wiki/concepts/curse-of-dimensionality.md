---
id: curse-of-dimensionality
type: concept
fields: [bayesian, control-theory, llm, information-theory, political-science]
n_sources: 13
tiers: [core, deep, reference]
grounding: digests
sources: [bellman-1957-dp/ch06-vi, bengio-2003-nplm/main, gelman-2013-bda3/ch20-basis, grimmer-2022-textasdata/ch27-text, hernan-2020-whatif/ch10-random, liberzon-2012-calculus/ch05-hamilton, mackay-2003-information/ch21-exact, mcgrayne-2011-theory/ch16-eureka, pearl-2016-primer/ch01-preliminaries, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch10-big, prince-2023-udl/ch08-measuring, sutton-2018-rl/ch04-dynamic]
generated_by: build_kg.py
---

# curse-of-dimensionality

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch20-basis]] (p. 495): basis count and data needs grow rapidly with the number of predictors [new]
- [[hernan-2020-whatif/ch10-random]] (p. 149): with many strata, conditional estimators become uninformative while marginal ones stay conditionally biased [new]
- [[mcgrayne-2011-theory/ch16-eureka]] (pp. 213–214): the plague of unknowns that appears as variables are refined; it hurt both Bayesians and frequentists [new]
- [[pearl-2016-primer/ch01-preliminaries]] (p. 30): estimating a high-dimensional joint distribution without structural knowledge is impossible with moderate data [new]
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 204–205): Strata multiply exponentially with covariates, leaving many empty [new]
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 317): estimation is hard with many variables; Big Data and machine learning help [new]

### control-theory

- [[bellman-1957-dp/ch06-vi]] (pp. 183, 189, 203): Bellman calls it "the usual difficulty of dimensionality": many stages plus many activities make tabulation costly [new]
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 127): backward cost $O(NMT)$ is still large if $N,M$ are large [new]
- [[sutton-2018-rl/ch04-dynamic]] (p. 87): the number of states often grows exponentially with state variables [new]

### llm

- [[bengio-2003-nplm/main]] (p. 1137): sequences in testing differ from training ones; parameters are potentially exponential in sequence length [new]
- [[prince-2023-udl/ch08-measuring]] (p. 129): volume of high-dimensional space overwhelms the number of training points [new]

### information-theory

- [[mackay-2003-information/ch21-exact]] (p. 298): grid of at least 10^K points for K parameters if the uncertainty about each has been reduced by, say, a factor of ten [new]

### political-science

- [[grimmer-2022-textasdata/ch27-text]] (p. 448): too many text features to condition on directly, since words outnumber observations [new]

## Candidate bridges

- [metaphor] Curse of dimensionality for surfaces ↔ sparse data in cells of a high-dimensional contingency table. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → unspecified)
- [structural-analogy] curse of dimensionality (sparse data in 40-D) ↔ nearest-neighbour and density estimation: distances lose contrast in high dimensions (note 5, p. 135). — from [[prince-2023-udl/ch08-measuring]] (llm → other)

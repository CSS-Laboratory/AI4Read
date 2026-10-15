---
id: curse-of-dimensionality
type: concept
curated: 2026-10-15
fields: [bayesian, control-theory, llm, information-theory, political-science]
level: UG
grounding: digests
aliases: []
sources: [gelman-2013-bda3/ch20-basis, hernan-2020-whatif/ch10-random, mcgrayne-2011-theory/ch16-eureka, pearl-2016-primer/ch01-preliminaries, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch10-big, bellman-1957-dp/ch06-vi, liberzon-2012-calculus/ch05-hamilton, sutton-2018-rl/ch04-dynamic, mackay-2003-information/ch21-exact, bengio-2003-nplm/main, prince-2023-udl/ch08-measuring, grimmer-2022-textasdata/ch27-text]
links: [overfitting, dynamic-programming, monte-carlo-integration, typical-set, word-embedding]
generated_version: wiki/kg/hub-sources/curse-of-dimensionality.md
---

# Curse of dimensionality

**Gist.** When a problem has many variables, the number of cases to tabulate, cells to fill or points to cover grows exponentially, so data and computation that are enough in low dimensions become hopelessly thin.

13 digests in five fields use this id; each field meets the same growth in its own setting.

## How each field uses it

### Control theory (dynamic programming, RL)
- “Bellman calls it "the usual difficulty of dimensionality": many stages plus many activities make tabulation costly” — [[bellman-1957-dp/ch06-vi]] (pp. 183, 189, 203)
- “the number of states often grows exponentially with state variables” — [[sutton-2018-rl/ch04-dynamic]] (p. 87)
- “backward cost $O(NMT)$ is still large if $N,M$ are large” — [[liberzon-2012-calculus/ch05-hamilton]] (p. 127)

### Bayesian theory & modeling (including causal inference)
- “basis count and data needs grow rapidly with the number of predictors” — [[gelman-2013-bda3/ch20-basis]] (p. 495)
- “estimating a high-dimensional joint distribution without structural knowledge is impossible with moderate data” — [[pearl-2016-primer/ch01-preliminaries]] (p. 30)
- “Strata multiply exponentially with covariates, leaving many empty” — [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 204–205)
- “with many strata, conditional estimators become uninformative while marginal ones stay conditionally biased” — [[hernan-2020-whatif/ch10-random]] (p. 149)
- “the plague of unknowns that appears as variables are refined; it hurt both Bayesians and frequentists” — [[mcgrayne-2011-theory/ch16-eureka]] (pp. 213–214)

### Information theory (MacKay, exact inference)
- “grid of at least 10^K points for K parameters if the uncertainty about each has been reduced by, say, a factor of ten” — [[mackay-2003-information/ch21-exact]] (p. 298)

### Large language models / ML
- “sequences in testing differ from training ones; parameters are potentially exponential in sequence length” — [[bengio-2003-nplm/main]] (p. 1137)
- “volume of high-dimensional space overwhelms the number of training points” — [[prince-2023-udl/ch08-measuring]] (p. 129)

### Political science (text as data)
- “too many text features to condition on directly, since words outnumber observations” — [[grimmer-2022-textasdata/ch27-text]] (p. 448)

## Bridges between fields

The digests propose few explicit bridges for this concept. The ones they give:

- **structural-analogy** (LLMs/ML → statistics): “curse of dimensionality (sparse data in 40-D) ↔ nearest-neighbour and density estimation: distances lose contrast in high dimensions (note 5, p. 135).” — [[prince-2023-udl/ch08-measuring]]. Justification: the same sparsity defeats methods that rely on nearby points.
- **metaphor** (Bayesian): “Curse of dimensionality for surfaces ↔ sparse data in cells of a high-dimensional contingency table.” — [[gelman-2013-bda3/ch20-basis]]. Justification: a picture of the same thinness of data.

Knowledge-manager reading (not a digest claim; for review): the definitions above share one structure — a count that is exponential in the number of variables (DP states in Sutton, grid points in MacKay, strata in Pearl, word features in Grimmer). Link type: **structural-analogy**, because the objects counted differ while the growth is the same.

## Where definitions disagree

- **Computation vs. data.** In control theory the problem is computing and storing tables (Bellman, Liberzon quotes). In Bayesian and causal inference it is having too little data per cell or stratum (Pearl, Hernán quotes). MacKay's grid is a computation problem inside inference.
- **Can it be beaten?** Pearl's popular book says “estimation is hard with many variables; Big Data and machine learning help” — [[pearl-2018-bookofwhy/ch10-big]] (pdf 317), while the primer says such estimation “without structural knowledge is impossible with moderate data” — [[pearl-2016-primer/ch01-preliminaries]]: structure (a causal model) is the remedy there. Bengio's neural language model answers with learned word vectors (see [[word-embedding]]).
- **Who suffers?** McGrayne reports that it “hurt both Bayesians and frequentists” — [[mcgrayne-2011-theory/ch16-eureka]]; it is not a problem of one school.

## Digests

Control theory: [[bellman-1957-dp/ch06-vi]], [[sutton-2018-rl/ch04-dynamic]], [[liberzon-2012-calculus/ch05-hamilton]] ·
Bayesian: [[gelman-2013-bda3/ch20-basis]], [[hernan-2020-whatif/ch10-random]], [[mcgrayne-2011-theory/ch16-eureka]], [[pearl-2016-primer/ch01-preliminaries]], [[pearl-2018-bookofwhy/ch07-beyond]], [[pearl-2018-bookofwhy/ch10-big]] ·
Information theory: [[mackay-2003-information/ch21-exact]] ·
LLMs / ML: [[bengio-2003-nplm/main]], [[prince-2023-udl/ch08-measuring]] ·
Political science: [[grimmer-2022-textasdata/ch27-text]]

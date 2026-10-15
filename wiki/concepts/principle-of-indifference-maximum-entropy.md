---
id: principle-of-indifference-maximum-entropy
type: concept
fields: [bayesian, information-theory, control-theory]
fields_strong: [bayesian, information-theory, control-theory]
n_sources: 23
n_works: 6
tiers: [core, reference]
grounding: digests
sources: [bayes-1763-essay/main, gelman-2013-bda3/ch02-single, jaynes-2003-probability/appa-other, jaynes-2003-probability/ch03-elementary, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch18-p, mackay-2003-information/ch35-random, mcelreath-2020-rethinking/ch01-golem, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch09-big, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch11-monsters, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, mcelreath-2020-rethinking/ch14-missing, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch35-reinforcement]
aliases: [principle-of-indifference-max-entropy, principle-of-indifference-maxent]
raw_ids: [Principle of indifference / maximum entropy]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# principle-of-indifference-maximum-entropy

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `principle-of-indifference-max-entropy` — 2 digest(s)
- `principle-of-indifference-maxent` — 1 digest(s)

## Canon spine entry

- **Principle of indifference / maximum entropy** (bayesian): with no information, spread probability evenly; more generally, choose the least-committal distribution consistent with constraints (grad)

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 22–23): the scholium argues from having no reason to expect one count rather than another; these pages do not call it a principle
- [[gelman-2013-bda3/ch02-single]] (pp. 34, 54): Laplace's "insufficient reason"; its weakness is parameterization dependence [alias `principle-of-indifference-max-entropy`]
- [[jaynes-2003-probability/appa-other]] (p. 655): cited as an example of principles for converting information into priors, with transformation groups [alias `principle-of-indifference-max-entropy`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch03-elementary]] (p. 51): equal probability 1/N for mutually exclusive, exhaustive hypotheses that $B$ does not distinguish, which gives the Bernoulli urn rule [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch04-elementary]] (pp. 88, 94, 112): indifference gives $P(A|X)=1/11$; a no-basis-for-preference argument (Laplace) motivates the uniform prior (4.66), with better justification promised later; maximum entropy listed as a principle for priors [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p1]] (p. 274): equal probability to $N$ outcomes when nothing else is known; used for the robot on $I_0$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch11-discrete]] (p. 365): uniform assignment is a special case of maximum entropy; a Gaussian sampling distribution is maximum entropy for given first and second moments, and a binomial one is equivalent to a uniform maximum-entropy assignment on a deeper hypothesis space [alias `principle-of-indifference-maxent`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch12-ignorance]] (p. 395): Jaynes defends indifference between *problems*, not events [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch13-decision]] (p. 418): the entropy principle generalises indifference in step (2) [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch18-p]] (p. 563, p. 571): contained in (18.44) when N = 0. P(N_n|X) is uniform (maximum entropy) [work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch01-golem]] (p. 7): exponential-family distributions are maximum-entropy; only mentioned here
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (pp. 75–76): Gaussian as the least-committal choice given only mean and variance; the author postpones the formal argument
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 179): maxent: least surprising distribution given constraints; only previewed here
- [[mcelreath-2020-rethinking/ch09-big]] (p. 269): choose the distribution that can arise the most ways, equivalently with biggest entropy, that fits the stated constraints; it is the most conservative one
- [[mcelreath-2020-rethinking/ch10-counting]] (pp. 292, 323, 328): binomial, multinomial and geometric are described as maximum entropy under stated constraints [as `Principle of indifference / maximum entropy`]
- [[mcelreath-2020-rethinking/ch11-monsters]] (p. 350): the beta-binomial and gamma-Poisson are maximum entropy under the same constraints as binomial and Poisson [as `Principle of indifference / maximum entropy`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (pp. 359, 364): Gaussian cluster distribution and exponential σ prior justified by maximum entropy
- [[mcelreath-2020-rethinking/ch13-adventures]] (p. 389): cited as the epistemological reason for a Gaussian: it is the maximum entropy form given only means, variances and covariances
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 426): with only a mean and sd known, Gaussian error is the most conservative choice
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 44): max-entropy distribution with feature constraints is exponential family; moments $x,x^2$ give the Gaussian
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 103): maxent prior as formalization of Laplace's insufficient reason
- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1182): the max-ent IRL model [work fields: bayesian, control-theory]

### information-theory

- [[mackay-2003-information/ch35-random]] (p. 445): here ignorance is expressed as invariance under rescaling, not as a uniform distribution [work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Desideratum (IIIc), equivalent knowledge gives equal plausibilities ↔ bayesian: principle of indifference/maximum entropy — from [[jaynes-2003-probability/ch01-plausible]] (bayesian → bayesian)
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors. — from [[jaynes-2003-probability/ch10-physics]] (bayesian → bayesian)
- [same-math] Maxent model with $\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ ↔ principle of indifference / maximum entropy: least-committal distribution matching feature expectations (p. 174–175). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → bayesian)

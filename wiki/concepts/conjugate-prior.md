---
id: conjugate-prior
type: concept
fields: [bayesian, information-theory, control-theory, decision-game-theory, linear-algebra, political-science]
fields_strong: [bayesian, information-theory, control-theory, decision-game-theory, linear-algebra, political-science]
n_sources: 37
n_works: 9
tiers: [core, reference]
grounding: digests
sources: [blei-2017-variational/main-p1, blei-2017-variational/main-p2, deisenroth-2020-mml/ch06-probability-p2, gelman-2013-bda3/appa-standard, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch03-introduction, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch18-models, gelman-2013-bda3/ch20-basis, gelman-2013-bda3/ch21-gaussian, gelman-2013-bda3/ch22-finite, gelman-2013-bda3/ch23-dirichlet, grimmer-2022-textasdata/ch06-multinomial, jaynes-2003-probability/ch15-paradoxes, mackay-2003-information/ch06-stream, mackay-2003-information/ch24-exact, mackay-2003-information/ch35-random, mackay-2003-information/ch36-decision, mcelreath-2020-rethinking/ch08-markov, mcgrayne-2011-theory/ch09-there, mcgrayne-2011-theory/ch11-business, mcgrayne-2011-theory/ch15-navy, murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch04-graphical-p1, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch29-state-p1, murphy-2023-pml2/ch29-state-p2, murphy-2023-pml2/ch34-decision, murphy-2023-pml2/ch35-reinforcement]
raw_ids: [Conjugate prior]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# conjugate-prior

## Canon spine entry

- **Conjugate prior** (bayesian): a prior family that yields a posterior in the same family (e.g., Beta–Binomial), giving closed-form updating (UG)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 6, 18): prior in the family matching the likelihood, giving a posterior in the same family; used in §4.2
- [[blei-2017-variational/main-p2]] (p. 27): e.g., normal-gamma conjugate to a normal likelihood with unknown mean and precision
- [[gelman-2013-bda3/appa-standard]] (pp. 583–585): gamma for the inverse normal variance and Poisson mean; inverse-gamma for the normal variance; Wishart for the inverse covariance matrix; inverse-Wishart for the covariance matrix; beta for the binomial; Dirichlet for the multinomial
- [[gelman-2013-bda3/ch02-single]] (pp. 35–36): a prior family whose posterior stays in the same family; "natural" ones copy the likelihood's functional form
- [[gelman-2013-bda3/ch03-introduction]] (pp. 67, 69, 72): a family closed under updating; for the normal it is N-Inv-$\chi^2$, for the multinomial Dirichlet, for the multivariate normal normal-inverse-Wishart
- [[gelman-2013-bda3/ch05-hierarchical]] (pp. 108–109, 115): here, conditional/partial conjugacy makes $p(\theta|\phi,y)$ a product of known densities
- [[gelman-2013-bda3/ch11-basics]] (pp. 277, 289): used here for conjugate conditionals that make Gibbs easy
- [[gelman-2013-bda3/ch14-introduction]] (pp. 376–377): normal prior on β and scaled inverse-χ² on σ² give the same families; coded as extra data
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 389): conjugacy of normal prior and regression likelihood allows the augmented-regression form
- [[gelman-2013-bda3/ch16-generalized]] (pp. 409, 429): hypothetical data $(y_0,X_0)$ for GLM; Dirichlet-like prior for loglinear counts
- [[gelman-2013-bda3/ch18-models]] (p. 462): Dirichlet prior for multinomial cell probabilities
- [[gelman-2013-bda3/ch20-basis]] (p. 488): normal-inverse-χ² (or normal-gamma) prior for (β, σ²) keeps the posterior in the same family, given the basis
- [[gelman-2013-bda3/ch21-gaussian]] (p. 503): GP is conditionally conjugate given $\tau,l,\sigma$ under a Gaussian observation model
- [[gelman-2013-bda3/ch22-finite]] (pp. 521, 534): Dirichlet for $\lambda$ (multinomial indicators); normal-inverse-gamma for component parameters in the Gaussian mixture
- [[gelman-2013-bda3/ch23-dirichlet]] (p. 547): Dirichlet/DP conjugacy gives posterior $\mathrm{DP}(\alpha P_0+\sum\delta_{y_i})$
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 481): the prior (15.84) used in Example #5 [as `Conjugate prior`; work fields: bayesian, information-theory]
- [[mcelreath-2020-rethinking/ch08-markov]] (p. 245): prior–likelihood pairs with an analytical single-parameter posterior; here, what Gibbs sampling needs
- [[mcgrayne-2011-theory/ch09-there]] (p. 125): priors and posteriors sharing the same curves, which Madansky hoped would allow pencil-and-paper calculation
- [[mcgrayne-2011-theory/ch11-business]] (p. 149): prior whose posterior has the same curve shape
- [[mcgrayne-2011-theory/ch15-navy]] (p. 203): a prior whose posterior stays in the same distribution class, used at Suez
- [[murphy-2023-pml2/ch02-probability-p2]] (p. 29): Gaussian prior with Gaussian likelihood gives a Gaussian posterior
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 65): prior whose posterior has the same functional form
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 83): prior family whose posterior stays in the family; closed-form update for exponential families
- [[murphy-2023-pml2/ch04-graphical-p1]] (p. 159): Dirichlet prior on each CPT row; posterior $\text{Dir}(N_{ij}+\alpha_{ij})$
- [[murphy-2023-pml2/ch07-inference]] (p. 348): a prior conjugate to the likelihood gives a tractable posterior; in general this is the case when both are in the same exponential family, so natural parameters add
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 470): conjugacy is what makes VB factors and VMP updates closed-form
- [[murphy-2023-pml2/ch15-generalized]] (pp. 597–598): Gaussian (known $\sigma^2$) and NIG (unknown $\sigma^2$) priors give closed-form linear-regression posteriors
- [[murphy-2023-pml2/ch29-state-p1]] (p. 996): Dirichlet and matrix-normal inverse-Wishart priors make the $\theta$ step easy [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch29-state-p2]] (pp. 997, 1004): Dirichlet/MNIW posteriors; conjugate UPM gives closed-form BOCPD likelihood [work fields: bayesian, control-theory]
- [[murphy-2023-pml2/ch34-decision]] (pp. 1116, 1123): Beta–Bernoulli and Gaussian updates give closed-form belief states [work fields: bayesian, decision-game-theory]
- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1149): Dirichlet for Thompson sampling [work fields: bayesian, control-theory]

### information-theory

- [[mackay-2003-information/ch06-stream]] (p. 118): the Dirichlet model (6.12) with parameter $\alpha$ generalises Laplace's rule; $\alpha=1$ recovers it [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch24-exact]] (p. 319): a prior whose form combines naturally with the likelihood, giving convenient inferences [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch35-random]] (p. 450): the Beta/Dirichlet priors give the closed-form Dirichlet-multinomial evidence (35.13) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch36-decision]] (p. 452): Gaussian prior with Gaussian likelihood gives a Gaussian posterior. The author does not use the term [weak: not really used in this unit; work fields: information-theory, bayesian, decision-game-theory]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 208): prior whose posterior has the same form (Def. 6.13) [new]

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 122): prior whose posterior has the same form; the Dirichlet for the multinomial [new]

## Instances that use it

- [[suez-canal-clearance]] — conjugate priors for the unknown number of bombs — from [[mcgrayne-2011-theory/ch15-navy]]

## Candidate bridges

- [same-math] Dirichlet-multinomial evidence (35.13) ↔ bayesian: marginal likelihood with conjugate priors — the same integral over the prior. — from [[mackay-2003-information/ch35-random]] (information-theory → bayesian)
- [structural-analogy] Prior strength as $n=1/\sigma^2_{\text{post}}$ ↔ Bayesian inference: conjugate priors act like pseudo-observations (Beta–Binomial). — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → bayesian)
- [same-math] Raiffa's conjugate priors ↔ Beta–Binomial conjugacy: both are closed-form updating within one family — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → other:beta-binomial-conjugacy)
- [same-math] Dirichlet prior over die probabilities ↔ Bayesian inference: Dirichlet-multinomial conjugate prior — the text treats Dir as the multivariate beta; conjugacy itself is not stated here — from [[murphy-2023-pml2/ch02-probability-p1]] (bayesian → bayesian)
- [same-math] uniform Dirichlet prior on transition rows (add-$\alpha$) ↔ Conjugate prior — counts plus pseudo-counts $\alpha$ (Dirichlet–categorical updating). — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)

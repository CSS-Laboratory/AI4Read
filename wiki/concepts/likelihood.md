---
id: likelihood
type: concept
curated: 2026-10-15
fields: [bayesian, information-theory, llm, linear-algebra, decision-game-theory, analytic-philosophy]
level: UG
grounding: digests
aliases: []
sources: [bayes-1763-essay/main, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch04-asymptotics, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch17-principles-p1, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch06-overfitting-p1, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch06-arthur, pearl-2018-bookofwhy/ch03-evidence, tenenbaum-2011-grow/main, efron-1986-bayesian/main, mackay-2003-information/ch02-probability, mackay-2003-information/ch22-maximum, mackay-2003-information/ch25-exact, mackay-2003-information/ch41-learning, mackay-2003-information/ch44-supervised, deisenroth-2020-mml/ch09-linear, prince-2023-udl/ch23-probability, kahneman-2011-thinking/ch14-tom, tversky-1974-heuristics/main, xie-2022-icl/main, gelman-2013-philosophy/main]
links: [bayes-theorem, maximum-likelihood-estimation, marginal-likelihood, likelihood-principle, likelihood-ratio, prior-distribution, posterior-distribution, cross-entropy]
generated_version: wiki/kg/hub-sources/likelihood.md
---

# Likelihood

**Gist.** The likelihood is the probability of the data you actually saw, read as a function of the unknown parameter or hypothesis; it scores how well each value explains the data, but it is not a probability distribution over those values.

54 digests use this id (full list in the generated version). Related but separate ids: [[maximum-likelihood-estimation]], [[marginal-likelihood]], [[likelihood-principle]].

## How each field uses it

### Bayesian theory & modeling (home field)
- “$p(y|\theta)$ as a function of $\theta$ for fixed $y$; the authors stress it is not a probability distribution” — [[gelman-2013-bda3/ch01-probability]] (pp. 7, 10)
- “$P(D|HX)$ as a function of $H$ for fixed $D$; not a probability for $H$; constant factors irrelevant” — [[jaynes-2003-probability/ch04-elementary]] (p. 89)
- “the only place data enter the posterior” — [[jaynes-2003-probability/ch08-sufficiency]] (p. 250)
- “formula giving the relative number of ways the data arise for each parameter value; here the binomial” — [[mcelreath-2020-rethinking/ch02-small]] (p. 33)
- “dominates the prior for large n; flat for nonidentified parameters” — [[gelman-2013-bda3/ch04-asymptotics]] (p. 88–89)
- “the binomial $Ex^pr^q$ as a function of the single-trial chance $x$” — [[bayes-1763-essay/main]] (pp. 17, 20)
- “$P(d\mid h)$, how expected the data are under $h$ relative to other hypotheses” (Bayesian cognition) — [[tenenbaum-2011-grow/main]] (p. 1280)

### Information theory
- “$P(\text{data}\mid\text{parameters})$ as a function of the parameters; not a probability distribution over them” — [[mackay-2003-information/ch02-probability]] (p. 29)
- “for a memoryless channel, a product of per-bit terms; only the ratio matters for decoding” — [[mackay-2003-information/ch25-exact]] (pp. 324–325)

### Machine learning (llm field)
- “$\beta E_D$ or $G$ is the negative log likelihood” — [[mackay-2003-information/ch44-supervised]] (p. 529, p. 530)
- “$P(D\mid\mathbf w)=\exp(-G)$; the error is minus its log” — [[mackay-2003-information/ch41-learning]] (p. 492)
- “$Pr(x|y)$ viewed as a function of $y$; need not sum to one” — [[prince-2023-udl/ch23-probability]] (p. 451)

### Linear algebra (ML mathematics)
- “density of the targets given inputs and parameters. It is normalized in $y$, not in $\theta$” — [[deisenroth-2020-mml/ch09-linear]] (pp. 291, 293)

## Bridges between fields

- **same-math** (decision theory → Bayesian): “Bayes's rule with prior and likelihood ratio ↔ Bayesian statistics generally: posterior odds = prior odds × likelihood ratio (our added step reproduces the author's 3% → 11% example).” — [[kahneman-2011-thinking/ch14-tom]]. Justification: the psychology example is computed with the likelihood ratio.
- **structural-analogy** (decision theory → Bayesian): “Insensitivity to prior probability ↔ Bayesian updating: the judge acts as if the likelihood ratio alone fixed the posterior odds.” — [[tversky-1974-heuristics/main]]. Justification: the bias is described as using the likelihood ratio and dropping the prior.
- **structural-analogy** (LLMs → Bayesian): “Concept selection by exponentially shrinking likelihood ratios $\exp(n\,r_n)$ ↔ Bayesian model comparison: the posterior concentrates on the best-fitting hypothesis as data accumulate.” — [[xie-2022-icl/main]]. Justification: in-context learning is analysed as likelihood-driven model selection.
- **same-math** (information theory / ML): the training error of a network is a negative log likelihood (MacKay ch41 and ch44 quotes above), so minimising the error is maximising the likelihood. Justification: stated in the digests' definitions.

## Where definitions disagree

- **Probability of what?** The technical digests insist it is not a distribution over the parameter (Gelman, Jaynes, Prince, Deisenroth quotes above). McGrayne's popular history describes it, “as McGrayne puts it, the probability of competing hypotheses for the fixed observed data” — [[mcgrayne-2011-theory/ch01-causes]] (p. 8), which reads more loosely.
- **Likelihood vs. "forward probability".** Pearl's digest uses a diagnostic-test example: “here $P(T\mid D)$, the forward probability, e.g., test sensitivity” — [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 103–104).
- **Is the likelihood the whole story?** Jaynes: “after the data are in, what remains significant for inference is the likelihood function” — [[jaynes-2003-probability/ch07-central-p1]] (p. 216), and Efron: “Efron says tree-building has no effect on the likelihood function, so it makes no difference to the Bayesian” — [[efron-1986-bayesian/main]] (p. 3). Jaynes also notes it is “not used by the orthodox tail-area test (p. 523) or by Feller's sampling distributions” — [[jaynes-2003-probability/ch17-principles-p1]] (p. 526). See [[likelihood-principle]].
- **Model checking.** Gelman & Shalizi treat it as one part of a full model: “the model's p(y|θ); the full joint distribution makes it a conditional density” — [[gelman-2013-philosophy/main]] (p. 4).
- **Maximum likelihood is not always welcome.** “Bailey rejects Fisher's maximum likelihood for insurance because it assigns zero probability to nonevents” — [[mcgrayne-2011-theory/ch06-arthur]] (p. 92).

## Digests

Bayesian: [[bayes-1763-essay/main]], [[gelman-2013-bda3/ch01-probability]], [[gelman-2013-bda3/ch04-asymptotics]], [[jaynes-2003-probability/ch04-elementary]], [[jaynes-2003-probability/ch07-central-p1]], [[jaynes-2003-probability/ch08-sufficiency]], [[jaynes-2003-probability/ch17-principles-p1]], [[mcelreath-2020-rethinking/ch02-small]], [[mcelreath-2020-rethinking/ch06-overfitting-p1]], [[mcgrayne-2011-theory/ch01-causes]], [[mcgrayne-2011-theory/ch06-arthur]], [[pearl-2018-bookofwhy/ch03-evidence]], [[tenenbaum-2011-grow/main]], [[efron-1986-bayesian/main]], [[gelman-2013-philosophy/main]] ·
Information theory: [[mackay-2003-information/ch02-probability]], [[mackay-2003-information/ch22-maximum]], [[mackay-2003-information/ch25-exact]] ·
ML / LLMs: [[mackay-2003-information/ch41-learning]], [[mackay-2003-information/ch44-supervised]], [[prince-2023-udl/ch23-probability]], [[xie-2022-icl/main]] ·
Linear algebra: [[deisenroth-2020-mml/ch09-linear]] ·
Decision theory: [[kahneman-2011-thinking/ch14-tom]], [[tversky-1974-heuristics/main]]

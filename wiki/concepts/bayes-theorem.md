---
id: bayes-theorem
type: concept
fields: [bayesian, information-theory, analytic-philosophy, linear-algebra]
n_sources: 54
tiers: [core, reference, deep]
grounding: digests
sources: [bayes-1763-essay/main, deisenroth-2020-mml/ch06-probability-p1, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch09-decision, godfreysmith-2003-theory/ch14-bayesianism, griffiths-2006-optimal/main, jaynes-2003-probability/appa-other, jaynes-2003-probability/ch02-quantitative, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch09-communication, mackay-2003-information/ch12-hash, mackay-2003-information/ch21-exact, mackay-2003-information/ch25-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch43-boltzmann, mackay-2003-information/ch46-deconvolution, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch06-arthur, mcgrayne-2011-theory/ch08-jerome, mcgrayne-2011-theory/ch11-business, mcgrayne-2011-theory/ch12-who, mcgrayne-2011-theory/ch14-three, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch20-generative, pearl-2016-primer/ch01-preliminaries, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch06-paradoxes, tenenbaum-2011-grow/main]
raw_ids: ["Bayes' theorem"]
canon_spine: bayesian
generated_by: build_kg.py
---

# bayes-theorem

## Canon spine entry

- **Bayes' theorem** (bayesian): posterior ∝ likelihood × prior; how to turn P(data | hypothesis) into P(hypothesis | data) (HS)

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 15–16, 22): here shown as Prop. 5/Prop. 9: probability of the first event given the second equals probability of both divided by probability of the second
- [[gelman-2013-bda3/ch01-probability]] (p. 7): $p(\theta|y)=p(\theta)p(y|\theta)/p(y)$; the unnormalised form is $\propto p(\theta)p(y|\theta)$
- [[gelman-2013-bda3/ch09-decision]] (p. 245): used to update Pr(cancer) after a test result
- [[griffiths-2006-optimal/main]] (p. 767): Eq. 1 combines likelihood and prior to give a posterior over $t_{total}$
- [[mcelreath-2020-rethinking/ch02-small]] (p. 37): posterior = likelihood × prior / average likelihood, derived by equating two factorisations of the joint probability
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 49): used to invert $\Pr(\text{positive}\mid\text{vampire})$ into $\Pr(\text{vampire}\mid\text{positive})$
- [[mcgrayne-2011-theory/app-appendixes]] (p. 257): $P(A|B)=P(A)P(B|A)/P(B)$, with A a hypothesis and B data
- [[mcgrayne-2011-theory/ch01-causes]] (p. 8): prior times likelihood is proportional to the posterior
- [[mcgrayne-2011-theory/ch02-man]] (pp. 20, 31): Laplace's 1774 and 1810–14 formulas for moving from effect to probable cause
- [[mcgrayne-2011-theory/ch03-many]] (p. 38): rule combining prior information with new data; here used as practical tool by artillery, Bell, insurers
- [[mcgrayne-2011-theory/ch04-bayes]] (pp. 67–69): rule for turning evidence into updated odds, used here as hunch-weighing; Turing talked about bans, not Bayes
- [[mcgrayne-2011-theory/ch06-arthur]] (pp. 93–94): the rule for combining prior knowledge with observed data. Bailey announced that the Credibility formula was derived from it
- [[mcgrayne-2011-theory/ch08-jerome]] (p. 111): used by Cornfield as a calculation linking population risk and subgroup risk
- [[mcgrayne-2011-theory/ch11-business]] (pp. 142, 149): rule combining prior and sample data; here used by trees without being named
- [[mcgrayne-2011-theory/ch12-who]] (p. 157): adjusts the probability of "Hamilton wrote No. 52" as evidence arrives
- [[mcgrayne-2011-theory/ch14-three]] (p. 180): normally the way to combine expert opinion with equipment failure rates; the panel avoided naming it and called its approach "subjectivistic"
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 242, 246): combines prior knowledge with new evidence, from spam scoring to translation
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): rule (2.15) obtained from the definition of conditional probability, for events with positive probability
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 61): used to turn class-conditionals into the density ratio
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 63): posterior = prior × likelihood / evidence, eq. (3.1)
- [[murphy-2023-pml2/ch07-inference]] (p. 345): posterior = prior × likelihood / $p(\mathcal D)$; $p(\mathcal D)$ is the bottleneck
- [[murphy-2023-pml2/ch20-generative]] (p. 779): used as $p(\boldsymbol z|\boldsymbol x)\propto p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)$ for structure discovery
- [[pearl-2016-primer/ch01-preliminaries]] (p. 12): $P(A|B)=P(B|A)P(A)/P(B)$, from (1.7) and symmetry of $P(A,B)$
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 100): Bayes's rule (3.1): reverse a conditional probability using the two marginals
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 182): belief rises for a hypothesis that survived a test that threatened it
- [[tenenbaum-2011-grow/main]] (p. 1280): Eq. (1): posterior proportional to prior × likelihood, normalized over hypothesis space $H$

### information-theory

- [[jaynes-2003-probability/appa-other]] (p. 654): for Jaynes, a consequence of Boolean associativity and commutativity, used without restriction
- [[jaynes-2003-probability/ch02-quantitative]] (p. 36): appears as product rule form (2.73); not named in this unit
- [[jaynes-2003-probability/ch04-elementary]] (pp. 87–89): (4.3) as the product rule rearranged; "prior" and "posterior" are logical, not temporal
- [[jaynes-2003-probability/ch05-queer]] (pp. 127, 134, 140): update by likelihood ratio; used on reports, theories and testimony, always conditional on the information actually received
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 150, 171): used to invert urn sampling distributions and counter likelihoods
- [[jaynes-2003-probability/ch06-elementary-p2]] (p. 178): posterior ∝ prior × likelihood, applied here to $n_1$, $s$ and $\alpha$
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 246): used here to prove sufficiency and ancillarity results [as `Bayes' theorem`]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 294): written as decibel evidence update (9.79), always relative to a named alternative
- [[jaynes-2003-probability/ch13-decision]] (p. 413): turns prior and sampling distribution into posterior; here it appears from minimising averaged risk
- [[jaynes-2003-probability/ch14-simple]] (p. 438): posterior odds = prior odds × likelihood ratio, (14.53) [as `Bayes' theorem`]
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 461): used for $p(H|DI)$ in the tetrahedra problem [as `Bayes' theorem`]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 510): has available all the information in the data and, jointly, in all possible estimators
- [[jaynes-2003-probability/ch17-principles-p2]] (pp. 533, 551): the single method Jaynes says resolves orthodox difficulties
- [[jaynes-2003-probability/ch18-p]] (p. 555): used to move A_p to the left of the bar and to update (A_p|E)
- [[jaynes-2003-probability/ch19-physical]] (p. 592): applied directly to $y=Ax+\delta$ to get the posterior and the best estimate, instead of conjecturing a linear form
- [[jaynes-2003-probability/ch20-model]] (p. 602): as used throughout
- [[mackay-2003-information/ch01-introduction]] (p. 6): used for optimal decoding, with posterior ∝ likelihood × prior
- [[mackay-2003-information/ch02-probability]] (p. 24): posterior from likelihood and prior, derived from the product rule, equations (2.9), (2.10)
- [[mackay-2003-information/ch03-more]] (p. 49, p. 53): posterior ∝ likelihood × prior, used for parameters ($\lambda$, $p_a$) and for models alike
- [[mackay-2003-information/ch09-communication]] (p. 148): used to infer inputs from outputs and in the optimal decoder
- [[mackay-2003-information/ch12-hash]] (p. 203): posterior odds = prior odds × likelihood ratio, used for the retrieval check and casting out nines
- [[mackay-2003-information/ch21-exact]] (p. 294): posterior = likelihood × prior / normalizer, used in (21.4)
- [[mackay-2003-information/ch25-exact]] (p. 324): gives the codeword posterior $P(\mathbf t\mid\mathbf y)\propto P(\mathbf y\mid\mathbf t)P(\mathbf t)$
- [[mackay-2003-information/ch28-model]] (pp. 347–348): used for posterior over parameters (28.4) and over models (28.6)
- [[mackay-2003-information/ch43-boltzmann]] (pp. 522–523): posterior (43.5), of which only the likelihood is used
- [[mackay-2003-information/ch46-deconvolution]] (p. 550): posterior = likelihood × prior / evidence

### analytic-philosophy

- [[godfreysmith-2003-theory/ch14-bayesianism]] (pp. 203, 207): $P(h|e)=P(e|h)P(h)/P(e)$, a consequence of axiom 4 [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 185): posterior = likelihood × prior / evidence, a consequence of the product rule [new]

## Candidate bridges

- [same-math] posterior odds = prior odds × likelihood ratio ↔ Bayes' theorem in HS form (e.g. medical-test base rates): the same rule on a different scale. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [structural-analogy] Discrete Bayes update after a test (p. 245) ↔ base-rate neglect: the prior (0.9) and the test's error rates combine by Bayes' theorem. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [same-math] Gibbs step for $z_{i}$ (22.5, p. 527; p. 534 step 1) ↔ Bayes' theorem: posterior component probability ∝ prior weight × component likelihood. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [structural-analogy] Weak syllogism (1.3) ↔ bayesian: Bayes' theorem — evidence consistent with a hypothesis raises its posterior (canon link; not stated in this unit) — from [[jaynes-2003-probability/ch01-plausible]] (information-theory → bayesian)
- [structural-analogy] (12.44) as multiplication of odds by $a$ ↔ Bayes' theorem in odds form — consistent with the log-odds check above. — from [[jaynes-2003-probability/ch12-ignorance]] (information-theory → unspecified)
- [same-math] Mammogram calculation ↔ Bayes' theorem (HS level): natural-frequency counts equal the formula — from [[mcgrayne-2011-theory/app-appendixes]] (bayesian → bayesian)
- [same-math] 1774 formula with equal priors ↔ Bayes' theorem with a uniform prior over a discrete set of hypotheses — it is the general formula with equal $P_{\text{prior}}$ cancelling. — from [[mcgrayne-2011-theory/ch02-man]] (bayesian → unspecified)
- [same-math] Tree-flipping ↔ Bayes' theorem: reversing P(result | state) into P(state | result) — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → bayesian)
- [same-math] screening results (HIV, PSA) ↔ Bayes' theorem and base-rate neglect: a positive result is weighed against disease prevalence. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → bayesian)
- [same-math] DRE trick via Bayes' rule ↔ Bayes' theorem — posterior odds times prior odds correction gives the likelihood ratio. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
- [structural-analogy] Bayesian posterior as the KL-minimizing constrained update ↔ Bayes' theorem: the text says Bayes' rule alone is a trivial chain-rule identity, while the KL view gives a principle for updating (§5.1.7). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] Gibbs posterior $\propto e^{-\lambda r}\pi_0$ ↔ Bayes' theorem: with log loss and $\lambda=N$ the two coincide — a special case, not general (p. 577) — from [[murphy-2023-pml2/ch14-predictive]] (bayesian → bayesian)
- [metaphor] RLHF ranking model and CLIP critic ↔ likelihood × weighting in Bayes' theorem: both use an external score to steer or rank model output. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → bayesian)
- [same-math] Optimal discriminator $D^*=p^*/(p^*+q_\theta)$ ↔ Bayes' theorem: posterior class probability with equal class priors $\tfrac12$. — from [[murphy-2023-pml2/ch26-generative]] (bayesian → bayesian)
- [same-math] $P(U\mid E=e)$ in step (i) ↔ Bayes' theorem: conditioning the distribution of the latent exogenous variables on evidence (p. 97). — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Collider bias ↔ Bayes' theorem/explaining away: learning one cause lowers belief in another cause of the same effect. — from [[pearl-2018-bookofwhy/ch05-smoke]] (bayesian → bayesian)
- [same-math] Monty Hall posterior via likelihood × prior ↔ Bayes' theorem: the host's rule supplies the likelihood term (pdf 182). — from [[pearl-2018-bookofwhy/ch06-paradoxes]] (bayesian → bayesian)
- [structural-analogy] Do-calculus proof as symbol manipulation ↔ Bayesian inference: both turn one kind of probability into another by licensed rewrites (conditioning, Bayes' theorem) — different rules, same "format change" spirit. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → bayesian)

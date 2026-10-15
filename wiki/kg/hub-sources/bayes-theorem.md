---
id: bayes-theorem
type: concept
fields: [bayesian, information-theory, decision-game-theory, llm, analytic-philosophy, linear-algebra]
fields_strong: [bayesian, information-theory, decision-game-theory, llm, analytic-philosophy, linear-algebra]
n_sources: 59
n_works: 18
tiers: [core, reference, deep]
grounding: digests
sources: [bayes-1763-essay/main, deisenroth-2020-mml/ch06-probability-p1, dixit-2008-art-strategy/ch08-interpreting, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch09-decision, godfreysmith-2003-theory/ch14-bayesianism, griffiths-2006-optimal/main, jaynes-2003-probability/appa-other, jaynes-2003-probability/ch02-quantitative, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, kahneman-2011-thinking/ch14-tom, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch09-communication, mackay-2003-information/ch12-hash, mackay-2003-information/ch21-exact, mackay-2003-information/ch25-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch43-boltzmann, mackay-2003-information/ch46-deconvolution, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch06-arthur, mcgrayne-2011-theory/ch08-jerome, mcgrayne-2011-theory/ch11-business, mcgrayne-2011-theory/ch12-who, mcgrayne-2011-theory/ch14-three, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch20-generative, osborne-2004-introduction/ch17-mathematics, pearl-2016-primer/ch01-preliminaries, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch06-paradoxes, prince-2023-udl/ch23-probability, stone-2022-information/appf-rules, tenenbaum-2011-grow/main]
aliases: [bayes-rule]
raw_ids: ["Bayes' theorem"]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# bayes-theorem

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `bayes-rule` — 5 digest(s)

## Canon spine entry

- **Bayes' theorem** (bayesian): posterior ∝ likelihood × prior; how to turn P(data | hypothesis) into P(hypothesis | data) (HS)

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 15–16, 22): here shown as Prop. 5/Prop. 9: probability of the first event given the second equals probability of both divided by probability of the second
- [[gelman-2013-bda3/ch01-probability]] (p. 7): $p(\theta|y)=p(\theta)p(y|\theta)/p(y)$; the unnormalised form is $\propto p(\theta)p(y|\theta)$
- [[gelman-2013-bda3/ch09-decision]] (p. 245): used to update Pr(cancer) after a test result
- [[griffiths-2006-optimal/main]] (p. 767): Eq. 1 combines likelihood and prior to give a posterior over $t_{total}$
- [[jaynes-2003-probability/appa-other]] (p. 654): for Jaynes, a consequence of Boolean associativity and commutativity, used without restriction [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch02-quantitative]] (p. 36): appears as product rule form (2.73); not named in this unit [weak: not really used in this unit; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch04-elementary]] (pp. 87–89): (4.3) as the product rule rearranged; "prior" and "posterior" are logical, not temporal [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch05-queer]] (pp. 127, 134, 140): update by likelihood ratio; used on reports, theories and testimony, always conditional on the information actually received [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 150, 171): used to invert urn sampling distributions and counter likelihoods [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch06-elementary-p2]] (p. 178): posterior ∝ prior × likelihood, applied here to $n_1$, $s$ and $\alpha$ [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch08-sufficiency]] (p. 246): used here to prove sufficiency and ancillarity results [as `Bayes' theorem`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch09-repetitive-p2]] (p. 294): written as decibel evidence update (9.79), always relative to a named alternative [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch13-decision]] (p. 413): turns prior and sampling distribution into posterior; here it appears from minimising averaged risk [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch14-simple]] (p. 438): posterior odds = prior odds × likelihood ratio, (14.53) [as `Bayes' theorem`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 461): used for $p(H|DI)$ in the tetrahedra problem [as `Bayes' theorem`; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 510): has available all the information in the data and, jointly, in all possible estimators [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch17-principles-p2]] (pp. 533, 551): the single method Jaynes says resolves orthodox difficulties [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch18-p]] (p. 555): used to move A_p to the left of the bar and to update (A_p|E) [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch19-physical]] (p. 592): applied directly to $y=Ax+\delta$ to get the posterior and the best estimate, instead of conjecturing a linear form [work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch20-model]] (p. 602): as used throughout [work fields: bayesian, information-theory]
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
- [[murphy-2023-pml2/ch20-generative]] (p. 779): used as $p(\boldsymbol z|\boldsymbol x)\propto p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)$ for structure discovery [work fields: bayesian, llm]
- [[pearl-2016-primer/ch01-preliminaries]] (p. 12): $P(A|B)=P(B|A)P(A)/P(B)$, from (1.7) and symmetry of $P(A,B)$
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 100): Bayes's rule (3.1): reverse a conditional probability using the two marginals
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 182): belief rises for a hypothesis that survived a test that threatened it
- [[tenenbaum-2011-grow/main]] (p. 1280): Eq. (1): posterior proportional to prior × likelihood, normalized over hypothesis space $H$

### information-theory

- [[mackay-2003-information/ch01-introduction]] (p. 6): used for optimal decoding, with posterior ∝ likelihood × prior [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch02-probability]] (p. 24): posterior from likelihood and prior, derived from the product rule, equations (2.9), (2.10) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch03-more]] (p. 49, p. 53): posterior ∝ likelihood × prior, used for parameters ($\lambda$, $p_a$) and for models alike [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (p. 148): used to infer inputs from outputs and in the optimal decoder [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch12-hash]] (p. 203): posterior odds = prior odds × likelihood ratio, used for the retrieval check and casting out nines [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch21-exact]] (p. 294): posterior = likelihood × prior / normalizer, used in (21.4) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch25-exact]] (p. 324): gives the codeword posterior $P(\mathbf t\mid\mathbf y)\propto P(\mathbf y\mid\mathbf t)P(\mathbf t)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch28-model]] (pp. 347–348): used for posterior over parameters (28.4) and over models (28.6) [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch43-boltzmann]] (pp. 522–523): posterior (43.5), of which only the likelihood is used [work fields: information-theory, bayesian, llm]
- [[mackay-2003-information/ch46-deconvolution]] (p. 550): posterior = likelihood × prior / evidence [work fields: information-theory, bayesian]
- [[stone-2022-information/appf-rules]] (p. 262): posterior = likelihood × prior / marginal likelihood [alias `bayes-rule`; new]

### decision-game-theory

- [[dixit-2008-art-strategy/ch08-interpreting]] (p. 246): updating the probability of a type after seeing an action: joint chance divided by the chance of the action [alias `bayes-rule`; new]
- [[kahneman-2011-thinking/ch14-tom]] (pdf 151): combines prior belief with diagnosticity of evidence; here, base rate plus evidence strength [alias `bayes-rule`; new]
- [[osborne-2004-introduction/ch17-mathematics]] (pp. 453–454): formulas (453.2) and (454.2) for updating a prior given evidence [alias `bayes-rule`; new]

### analytic-philosophy

- [[godfreysmith-2003-theory/ch14-bayesianism]] (pp. 203, 207): $P(h|e)=P(e|h)P(h)/P(e)$, a consequence of axiom 4 [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 185): posterior = likelihood × prior / evidence, a consequence of the product rule [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 452): posterior = likelihood × prior / evidence [alias `bayes-rule`; new]

## Candidate bridges

- [same-math] Bayes' Rule in the poker example ↔ probability/statistics: posterior = joint probability ÷ marginal — the same formula applied to a bid. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → other:statistics)
- [same-math] posterior odds = prior odds × likelihood ratio ↔ Bayes' theorem in HS form (e.g. medical-test base rates): the same rule on a different scale. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [structural-analogy] Discrete Bayes update after a test (p. 245) ↔ base-rate neglect: the prior (0.9) and the test's error rates combine by Bayes' theorem. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → decision-game-theory)
- [same-math] Gibbs step for $z_{i}$ (22.5, p. 527; p. 534 step 1) ↔ Bayes' theorem: posterior component probability ∝ prior weight × component likelihood. — from [[gelman-2013-bda3/ch22-finite]] (bayesian → bayesian)
- [same-math] Naïve Bayes classification ↔ statistics/ML: Bayes' rule with conditional independence of features given the class — the equation is the standard one. — from [[grimmer-2013-textasdata/main]] (political-science → llm)
- [structural-analogy] Weak syllogism (1.3) ↔ bayesian: Bayes' theorem — evidence consistent with a hypothesis raises its posterior (canon link; not stated in this unit) — from [[jaynes-2003-probability/ch01-plausible]] (bayesian → bayesian)
- [structural-analogy] (12.44) as multiplication of odds by $a$ ↔ Bayes' theorem in odds form — consistent with the log-odds check above. — from [[jaynes-2003-probability/ch12-ignorance]] (bayesian → unspecified)
- [same-math] Base-rate neglect ↔ Bayes' rule: posterior odds = prior odds × likelihood ratio; the 5.44 factor is the ratio of the prior odds in the two conditions, $(7/3)\div(3/7)=(.7/.3)^2$. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → bayesian)
- [same-math] Base rate plus witness reliability ↔ probability: Bayes' rule with prior 0.15 and likelihood ratio 4:1 gives 0.12/0.29. — from [[kahneman-2011-thinking/ch16-causes]] (decision-game-theory → other:probability)
- [same-math] Posterior belief after hearing "better" ↔ statistics: Bayes' rule over speaker types (fn. 19–20). — from [[lupia-1998-dilemma/ch03-people]] (political-science → other:statistics)
- [same-math] Mammogram calculation ↔ Bayes' theorem (HS level): natural-frequency counts equal the formula — from [[mcgrayne-2011-theory/app-appendixes]] (bayesian → bayesian)
- [same-math] 1774 formula with equal priors ↔ Bayes' theorem with a uniform prior over a discrete set of hypotheses — it is the general formula with equal $P_{\text{prior}}$ cancelling. — from [[mcgrayne-2011-theory/ch02-man]] (bayesian → unspecified)
- [same-math] Tree-flipping ↔ Bayes' theorem: reversing P(result | state) into P(state | result) — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → bayesian)
- [same-math] Kalman filter as derived from Bayes' rule (Aoki 1967) ↔ bayesian: sequential updating — the author says it can be derived directly from Bayes' rule (p. 205). — from [[mcgrayne-2011-theory/ch15-navy]] (bayesian → bayesian)
- [same-math] screening results (HIV, PSA) ↔ Bayes' theorem and base-rate neglect: a positive result is weighed against disease prevalence. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → bayesian)
- [same-math] DRE trick via Bayes' rule ↔ Bayes' theorem — posterior odds times prior odds correction gives the likelihood ratio. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
- [structural-analogy] Bayesian posterior as the KL-minimizing constrained update ↔ Bayes' theorem: the text says Bayes' rule alone is a trivial chain-rule identity, while the KL view gives a principle for updating (§5.1.7). — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [structural-analogy] Gibbs posterior $\propto e^{-\lambda r}\pi_0$ ↔ Bayes' theorem: with log loss and $\lambda=N$ the two coincide — a special case, not general (p. 577) — from [[murphy-2023-pml2/ch14-predictive]] (bayesian → bayesian)
- [metaphor] Logit adjustment ↔ Bayes' rule with changed priors: dividing by $\pi_y$ removes the label prior. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
- [metaphor] RLHF ranking model and CLIP critic ↔ likelihood × weighting in Bayes' theorem: both use an external score to steer or rank model output. — from [[murphy-2023-pml2/ch22-autoregressive]] (bayesian → bayesian)
- [structural-analogy] NCE ↔ logistic regression / classifier-based density-ratio estimation: the classifier is linked to the density ratio via Bayes' rule (p. 861). — from [[murphy-2023-pml2/ch24-energy]] (bayesian → other:statistics)
- [same-math] Optimal discriminator $D^*=p^*/(p^*+q_\theta)$ ↔ Bayes' theorem: posterior class probability with equal class priors $\tfrac12$. — from [[murphy-2023-pml2/ch26-generative]] (bayesian → bayesian)
- [structural-analogy] Scaled likelihood trick ↔ Bayes' rule: $p(y\mid z)\propto p(z\mid y)/p(z)$ (29.17). — from [[murphy-2023-pml2/ch29-state-p1]] (bayesian → bayesian)
- [same-math] Bayes' rule with states and signals ↔ Bayesian game / Bayesian Nash equilibrium: beliefs about types updated on a signal. — from [[osborne-2004-introduction/ch17-mathematics]] (decision-game-theory → decision-game-theory)
- [same-math] Bayes' rule with prior ↔ Bayesian inference: posterior ∝ likelihood × prior — same formula (1.8), with the hypothesis as $A$ and the evidence as $B$. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [same-math] $P(U\mid E=e)$ in step (i) ↔ Bayes' theorem: conditioning the distribution of the latent exogenous variables on evidence (p. 97). — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → bayesian)
- [structural-analogy] Collider bias ↔ Bayes' theorem/explaining away: learning one cause lowers belief in another cause of the same effect. — from [[pearl-2018-bookofwhy/ch05-smoke]] (bayesian → bayesian)
- [same-math] Monty Hall posterior via likelihood × prior ↔ Bayes' theorem: the host's rule supplies the likelihood term (pdf 182). — from [[pearl-2018-bookofwhy/ch06-paradoxes]] (bayesian → bayesian)
- [structural-analogy] Do-calculus proof as symbol manipulation ↔ Bayesian inference: both turn one kind of probability into another by licensed rewrites (conditioning, Bayes' theorem) — different rules, same "format change" spirit. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → bayesian)
- [metaphor] Bayes' rule posterior ↔ language models: Bayesian reading of conditioning on a prompt (canon link; not stated here). — from [[prince-2023-udl/ch23-probability]] (llm → llm)
- [same-math] Exercise 1.3 (package choice) ↔ Bayes' rule on a discrete hypothesis — a posterior update after evidence. — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
- [structural-analogy] Bayes' rule (prior → posterior) ↔ statistics: updating beliefs after data. — from [[stone-2022-information/appf-rules]] (information-theory → other:statistics)
- [structural-analogy] Predict–correct cycle ↔ Bayesian updating: the paper links the filter's justification to conditioning on past measurements (Bayes' rule) (p. 4). — from [[welch-2004-kalmanintro/main]] (control-theory → bayesian)

---
id: expectation
type: concept
fields: [bayesian, economics-finance, information-theory, llm]
fields_strong: [bayesian, economics-finance, information-theory, llm]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [jaynes-2003-probability/ch03-elementary, keynes-1936-general/ch04-choice, prince-2023-udl/ch23-probability]
generated_by: build_kg.py
---

# expectation

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch03-elementary]] (pp. 66–67): probability-weighted average of a quantity's possible values; $P(R_1|B)=\langle F\rangle$ when $F$ is unknown [new; work fields: bayesian, information-theory]

### economics-finance

- [[keynes-1936-general/ch04-choice]] (§ III, para 1; § IV): not developed in this chapter. It appears only in the expected proceeds that induce employment and in the expectation of increased demand

### llm

- [[prince-2023-udl/ch23-probability]] (p. 453): average of $f[x]$ weighted by $Pr(x)$; four rules [new]

## Instances that use it

- [[ames-room]] — a perceptual illusion that outrages naive expectations — from [[dennett-1987-intentional-stance/ch01-setting]]
- [[cara-normal-noisy-rational-expectations-model]] — the paper's worked example in which conjectures 1–7 can be checked — from [[grossman-1980-impossibility/main]]
- [[burning-cars-road]] — a repeat in the same place makes an expectation active — from [[kahneman-2011-thinking/ch06-norms]]
- [[allais-paradox]] — A/B choices inconsistent with the expectation principle; shows the certainty effect — from [[kahneman-2011-thinking/ch29-fourfold]]
- [[wife-one-dollar-week]] — without reinvestment the gambler should bet all on the highest-expectation event — from [[kelly-1956-information/main]]
- [[expectation-driven-cycle]] — a single change in expectation can generate a rise to a peak and a decline, shaped like a cycle — from [[keynes-1936-general/ch05-expectation]]
- [[discovery-of-x-rays]] — discovery by accident. It shows that instruments carry expectations — from [[kuhn-1962-structure/ch06-anomaly]]
- [[uranium-fission-identification]] — late recognition, partly because chemical tests were chosen by expectation — from [[kuhn-1962-structure/ch06-anomaly]]
- [[eight-queens]] — hill climbing 14% vs tabu 94% success; restart expectation of 22 steps; GA crossover example — from [[murphy-2023-pml2/ch06-optimization-p2]]
- [[eighty-twenty-split]] — consistent asymmetric expectations that cannot be shown irrational — from [[schelling-1960-conflict/appb-abandonment]]
- [[atomic-weapons-convention]] — a difference that exists purely in shared expectations — from [[schelling-1960-conflict/appc-re-p2]]
- [[union-wage-commitment]] — union leaders raising member expectations so they cannot concede — from [[schelling-1960-conflict/ch02-essay]]
- [[us-housing-bubble-liar-loans]] — optimistic expectations and lax lending — from [[thaler-2015-misbehaving/ch26-fruit]]
- [[bang-expectation]] — expecting a bang while someone aims a gun — from [[wittgenstein-1953-investigations/ch06-intentionality]]
- [[burning-fuse-expectation]] — watching a burning fuse, perhaps with no thoughts or only disjointed ones, is certainly a case of expecting — from [[wittgenstein-1953-investigations/ch07-negation]]

## Candidate bridges

- [same-math] Average quality of sellers at price $p$, $E[x \mid x \le p] = p/2$ ↔ information-theory / Bayesian updating: conditioning on a selection event — the act of selling is a signal about quality, and the price changes who selects in; the same truncated-expectation calculation appears in the winner's curse in auctions. — from [[akerlof-1970-lemons/main]] (economics-finance → information-theory)
- [metaphor] Labels sustaining self-confirming stereotypes ↔ convention/focal point: a shared expectation that stays stable because everyone acts on it. — from [[axelrod-1984-cooperation/ch08-social]] (decision-game-theory → analytic-philosophy)
- [same-math] $c_i=\sum_j\alpha_{ij}h_j$ with softmax weights ↔ probability: an expectation of $h_j$ under a distribution over positions (the paper's own "expected annotation" reading) — from [[bahdanau-2015-attention/main]] (llm → other:probability)
- [same-math] Prop. 3 and Cor. ↔ probability: product rule $P(A\cap B)=P(A)P(B\mid A)$ — Bayes derives the same rule from expectations. — from [[bayes-1763-essay/main]] (bayesian → other:probability)
- [same-math] Prop. 3.4.1 ↔ statistics: the conditional expectation of an indicator is the conditional probability, and it minimizes mean squared error. — from [[bertsekas-2026-rlcourse/ch03-learning-p3]] (control-theory → other:statistics)
- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26). — from [[blei-2017-variational/main-p2]] (bayesian → bayesian)
- [same-math] Sanov's $P^*\propto Q\,e^{\sum\lambda_ig_i}$ ↔ maximum entropy / exponential families: the same tilted form as MaxEnt solutions under expectation constraints. — from [[cover-2006-elements/ch12-information-p1]] (information-theory → information-theory)
- [structural-analogy] Folk physics and folk psychology as expectation-generating systems ↔ predictive models in cognitive science: both are efficient systems that generate expectations. — from [[dennett-1987-intentional-stance/ch01-setting]] (theory-of-mind → other:psychology-cognitive-science)
- [structural-analogy] Maxims as expectations about a partner ↔ conventions that solve coordination problems: Grice offers analogies from cooperative non-talk tasks (p. 47). — from [[grice-1975-conversation/main]] (analytic-philosophy → other:conventions-that-solve-coordination)
- [metaphor] Contextual integrity ↔ research ethics: expectations of the context in which information was shared — from [[grimmer-2022-textasdata/ch03-principles]] (political-science → other:research-ethics)
- [structural-analogy] Blind coders and held-out test data ↔ blinding in experiments: both keep expectations from shaping the measurement. — from [[grimmer-2022-textasdata/ch15-principles]] (political-science → other:blinding-in-experiments)
- [structural-analogy] Averaging predictions over the observed $L_i$ ↔ Monte Carlo integration: replacing an expectation over $L$ by a sample average. — from [[hernan-2020-whatif/ch13-standardization]] (bayesian → bayesian)
- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$. — from [[jaynes-1957-information/main]] (information-theory → information-theory)
- [same-math] §9.9 Gibbs distribution with $\overline G=-\partial\log Z/\partial\lambda$ ↔ information-theory: exponential family from MaxEnt under an expectation constraint. — from [[jaynes-2003-probability/ch09-repetitive-p2]] (bayesian → information-theory)
- [same-math] weatherman log-pay expectation ↔ information-theory: cross-entropy / log scoring rule — expected pay B[log n + Σp_i log q_i] is maximised at q = p, a Gibbs-type inequality. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → information-theory)
- [metaphor] Surprise as a measure of a violated expectation ↔ Bayesian decision theory: an unlikely observation under a model — the text states no probabilities. — from [[kahneman-2011-thinking/ch06-norms]] (decision-game-theory → bayesian)
- [structural-analogy] Reference points set in negotiation ↔ decision-game-theory: anchors and focal points that coordinate expectations — both fix a shared starting point. — from [[kahneman-2011-thinking/ch28-bad]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Short-term expectations modified gradually by recent results ↔ economics-finance: adaptive expectations — both revise forecasts partly in the light of recent outcomes. Keynes gives no formula. — from [[keynes-1936-general/ch05-expectation]] (economics-finance → economics-finance)
- [metaphor] marginal user cost depending on expected length of the slump ↔ expectations-driven pricing: current price reflects beliefs about future recovery. — from [[keynes-1936-general/ch06-definition]] (economics-finance → other:expectations-driven-pricing)
- [structural-analogy] Conventional long rate that is durable if believed durable ↔ coordination game / multiple equilibria: self-fulfilling expectations select the outcome. — from [[keynes-1936-general/ch15-psychological]] (economics-finance → decision-game-theory)
- [metaphor] Money as link between present and future ↔ rational expectations (canon link; not stated in this unit): expectations feed back on current decisions. — from [[keynes-1936-general/ch21-theory]] (economics-finance → economics-finance)
- [structural-analogy] Sentence-by-sentence probing ↔ violation-of-expectation paradigm: both infer belief tracking from how responses shift when evidence changes. — from [[kosinski-2024-llm-tom/main]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Anomaly detected only against a precise expectation ↔ statistics: a deviation is flagged only relative to an expected tolerance. The same reading is "anomalous" under a tight tolerance and not under a loose one. — from [[kuhn-1962-structure/ch06-anomaly]] (analytic-philosophy → other:statistics)
- [structural-analogy] Scorekeeping of commitments (Brandom, citing Lewis 1979) ↔ convention: both are shared public record-keeping that sustains coordinated expectations. — from [[lycan-2019-language/ch06-use]] (analytic-philosophy → decision-game-theory)
- [structural-analogy] Wittgenstein's rule-governed language-games ↔ convention (Lewis): regularities kept up by mutual expectation, though the unit does not make this link. — from [[lycan-2019-language/ch06-use]] (analytic-philosophy → analytic-philosophy)
- [same-math] Soft K-means update (22.21) ↔ Expectation–Maximization for Gaussian mixtures — the same weighted-mean update; these pages never mention EM, and say only that a proof that the algorithm maximizes the likelihood is deferred to section 33.7 (p. 305). — from [[mackay-2003-information/ch22-maximum]] (information-theory → unspecified)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → information-theory)
- [same-math] Posterior samples as Monte Carlo draws ↔ simulation: expectations and probabilities are sample averages and fractions — from [[mcelreath-2020-rethinking/ch03-sampling]] (bayesian → other:simulation)
- [structural-analogy] Higher-order expectations anchored on public signal ↔ Keynesian beauty contest / conventional expectations — the focal public signal fixes what others are expected to do. — from [[morris-2002-public/main]] (economics-finance → unspecified)
- [same-math] Maxent model with $\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ ↔ principle of indifference / maximum entropy: least-committal distribution matching feature expectations (p. 174–175). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → bayesian)
- [structural-analogy] Control variate/baseline ↔ Monte Carlo variance reduction in estimating expectations (p. 275) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → unspecified)
- [structural-analogy] ADF moment projection ↔ expectation propagation: EP iterates ADF-style projections with past and future factors. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → bayesian)
- [same-math] Reparameterized gradient $\mathbb E_{p(\epsilon)}[\nabla_\phi f(g(\phi,\epsilon))]$ ↔ Monte Carlo integration: a single-sample Monte Carlo estimate of an expectation of a gradient. — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → bayesian)
- [structural-analogy] Rao-Blackwellization ↔ variance reduction by analytic integration — replace sampling with a conditional expectation where possible (p. 557). — from [[murphy-2023-pml2/ch13-sequential]] (bayesian → unspecified)
- [same-math] Importance weighting $w=q(x)/p(x)$ for target risk (19.12–19.16) ↔ Monte Carlo integration: importance sampling re-expresses an expectation under $q$ as one under $p$ times a density ratio. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [same-math] M step of PPCA-EM ↔ multi-output linear regression (author notes this, p. 946), with latent expectations in place of inputs — from [[murphy-2023-pml2/ch28-latent-p1]] (bayesian → unspecified)
- [same-math] Fubini swap giving $R_B(\delta)$ two ways ↔ probability: law of iterated expectation — the author states they are equivalent (p. 1107). — from [[murphy-2023-pml2/ch34-decision]] (bayesian → other:probability)
- [structural-analogy] Austen model's $\tilde g\sim\mathrm{Beta}$ with Bernoulli treatment ↔ Bayesian conjugacy: beta-Bernoulli updating gives the conditional logit expectations used in the bias formula. — from [[murphy-2023-pml2/ch36-causality-p2]] (bayesian → bayesian)
- [metaphor] Looking longer at surprising events ↔ machine learning: prediction error — larger mismatch with expectation draws more attention. — from [[onishi-2005-infant-false-belief/main]] (theory-of-mind → llm)
- [structural-analogy] Stackelberg first mover choosing the best point on the follower's reaction curve ↔ credible commitment: limiting one's own options changes the other's expectations — firm 1 gains by being unable to change its output. — from [[osborne-2004-introduction/ch06-extensive]] (decision-game-theory → political-science)
- [same-math] Gaussian conditional expectation is linear in the regressors ↔ Bayesian linear regression: both use the multivariate normal conditional $E[Y|X_1..X_n]=r_0+\sum r_ix_i$. — from [[pearl-2016-primer/ch03-effects]] (bayesian → bayesian)
- [structural-analogy] precedent-setting at first use ↔ repeated game: today's act changes expectations about future play. — from [[schelling-1960-conflict/appa-nuclear]] (decision-game-theory → decision-game-theory)
- [structural-analogy] regress "I expect you to expect…" ↔ mutual vs common knowledge: shared expectation replaces an infinite hierarchy — from [[schelling-1960-conflict/appb-abandonment]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Commitment as a selective reduction of one's own payoffs ↔ decision-game-theory: credible commitment — limiting options to change the other's expectations. — from [[schelling-1960-conflict/appc-re-p2]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Tipping and explosive convergence of expectations ↔ decision-game-theory: convention — a self-sustaining regularity that solves a coordination problem. — from [[schelling-1960-conflict/appc-re-p2]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Convergent expectations in coordination ↔ Nash equilibrium / convention: an outcome that each expects of the other and that sustains itself. — from [[schelling-1960-conflict/ch04-toward]] (decision-game-theory → decision-game-theory)
- [metaphor] Mob formation and neighbourhood tipping ↔ threshold or tipping models of collective behaviour: expectations of others' action drive the outcome. — from [[schelling-1960-conflict/ch04-toward]] (decision-game-theory → other:threshold-or-tipping-models)
- [structural-analogy] Hypothetical meter experiment ↔ experimental economics: an operational test of whether expectations converge. — from [[schelling-1960-conflict/ch04-toward]] (decision-game-theory → economics-finance)
- [same-math] Gaussian maximises entropy at fixed variance (Lagrange: $-1-\log p+\lambda x^2+\mu=0$) ↔ information-theory canon "exponential family / Gibbs distribution": same exponential form arises from expectation constraints. — from [[shannon-1948-mathematical/main-p2]] (information-theory → information-theory)
- [structural-analogy] Narrative recovery by forgetting ↔ adaptive expectations: the state fades without an outside shock. — from [[shiller-2019-narrative/app-applying]] (economics-finance → economics-finance)
- … 18 more bridge lines mention this id (see wiki/kg/bridges.jsonl)

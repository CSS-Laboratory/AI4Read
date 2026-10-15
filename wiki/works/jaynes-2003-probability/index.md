---
id: jaynes-2003-probability/index
work: jaynes-2003-probability
type: work-map
units: [jaynes-2003-probability/front-preface, jaynes-2003-probability/ch01-plausible, jaynes-2003-probability/ch02-quantitative, jaynes-2003-probability/ch03-elementary, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch09-repetitive-p1, jaynes-2003-probability/ch09-repetitive-p2, jaynes-2003-probability/ch10-physics, jaynes-2003-probability/ch11-discrete, jaynes-2003-probability/ch12-ignorance, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch16-orthodox, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch19-physical, jaynes-2003-probability/ch20-model, jaynes-2003-probability/ch21-outliers, jaynes-2003-probability/ch22-introduction, jaynes-2003-probability/appa-other, jaynes-2003-probability/appb-mathematical, jaynes-2003-probability/appc-convolutions]
---

# Jaynes, E. T. (2003). *Probability Theory: The Logic of Science* (G. L. Bretthorst, Ed.). Cambridge University Press. DOI 10.1017/CBO9780511790423.

## In one paragraph
Jaynes argues that probability is the logic of plausible reasoning when information is incomplete. He starts from a few common-sense desiderata for an idealized reasoning robot, and from them derives the sum and product rules. Probabilities then describe a state of knowledge, not physical frequencies or "randomness" in nature. From this base he builds a method of inference. Prior information is stated explicitly. Priors come from symmetry (transformation groups) or from maximum entropy. Nuisance parameters are integrated out. Decisions are made by adding a loss function. He applies the method to estimation, model comparison, outliers, physics and communication theory. He criticizes orthodox (frequentist) statistics as ad hoc and information-wasting. He also traces many paradoxes to careless use of infinite sets. The result is a unified, polemical alternative to both orthodox statistics and rival foundations.

## The path through the work
- [[jaynes-2003-probability/front-preface]] — Jaynes argues that the rules of probability are the unique consistent rules for plausible reasoning under incomplete information, not just rules for frequencies of "random variables".
- [[jaynes-2003-probability/ch01-plausible]] — Where deduction cannot settle a question, we need an extension of logic that assigns degrees of plausibility, and Jaynes proposes to derive its rules from a few desiderata imposed on an idealized reasoning robot.
- [[jaynes-2003-probability/ch02-quantitative]] — If degrees of plausibility are real numbers that match common sense and are consistent, then a monotonic function of them must obey the product rule and the sum rule; rescaled to an ordinary probability, it is fixed by the data (for indifferent cases, to $1/n$).
- [[jaynes-2003-probability/ch03-elementary]] — The product rule, sum rule and indifference already give the hypergeometric and binomial distributions, and show that probability expresses logical connection between propositions (a state of knowledge), which need not be physical causation.
- [[jaynes-2003-probability/ch04-elementary]] — Hypothesis testing needs no new principle beyond the product rule: compute the probability of the hypothesis given all the evidence, and (for two hypotheses) work in log-odds ("evidence" in decibels) so that independent data add up.
- [[jaynes-2003-probability/ch05-queer]] — Probability theory gives consistent answers only for the information you actually put in: reports of marvels, disagreements, scientific tests and uncertain evidence all go wrong when the relevant alternatives or the real form of the information are left out.
- [[jaynes-2003-probability/ch06-elementary-p1]] — Probability theory as logic gives point and interval estimates from one posterior, and the conclusions (Laplace's rule, futile sampling under a binomial prior, Bayes vs maximum likelihood) can depend, often surprisingly, on the prior information (though different priors need not give different conclusions).
- [[jaynes-2003-probability/ch06-elementary-p2]] — Vague but smooth priors barely change an estimate, whereas even one qualitative fact (a common hidden source) can change it a lot and tighten it; so data never "speak for themselves."
- [[jaynes-2003-probability/ch07-central-p1]] — Jaynes argues that Gaussian error laws are used because they describe a state of knowledge (roughly: only the first two moments of the noise are known), not because real error frequencies are Gaussian, and that they succeed because with them the actual error frequencies become irrelevant to the inference.
- [[jaynes-2003-probability/ch07-central-p2]] — Gaussians stay Gaussian under convolution (the density of a sum of independent variables; means and variances add), and this stability, with its maximum-entropy character, motivates calling it the "central" distribution; Jaynes also asks what a Gaussian form in data can and cannot show.
- [[jaynes-2003-probability/ch08-sufficiency]] — Jaynes argues that sufficiency, the likelihood principle, ancillarity and the rules for combining data are all handled automatically by the Chapter 2 rules (product rule, Bayes' theorem), with the principle that redundant information is not counted twice ($AA=A$) behind several of them.
- [[jaynes-2003-probability/ch09-repetitive-p1]] — A robot told only the number $N=m^n$ of possible outcomes (and so, by indifference, giving each probability $1/N$) reproduces the classical frequentist results (independent trials, binomial law, probability = frequency), so Jaynes concludes that frequentist theory is functionally the reasoning of a poorly informed robot, which helps explain why it has trouble with induction.
- [[jaynes-2003-probability/ch09-repetitive-p2]] — A goodness-of-fit test is only meaningful relative to a stated class of alternatives; Bayes' theorem gives an exact version (ψ) for the Bernoulli class of alternatives; Pearson's χ² approximates it when frequencies are close to the expected ones, and it grossly over-penalises very unlikely events.
- [[jaynes-2003-probability/ch10-physics]] — Jaynes argues that "physical probabilities" of coins, dice, cards or atoms do not exist as properties of the object alone, so probability should be read as logic that uses information such as symmetry, not as frequency.
- [[jaynes-2003-probability/ch11-discrete]] — Jaynes argues that when the prior information is a set of average values, the "most honest" probability assignment is the one that maximizes the entropy $H=-\sum p_i\log p_i$ subject to those averages, and this has the exponential form $p_i \propto \exp(-\sum_j\lambda_j f_j(x_i))$, where the $f_j$ are the quantities whose averages are given and the $\lambda_j$ are constants fitted to them.
- [[jaynes-2003-probability/ch12-ignorance]] — A prior for "complete ignorance" is restricted, and in many cases fully determined, by naming the transformations (shift, rescaling, and so on) that turn the problem into an equivalent one, and demanding that the prior keep the same form under them.
- [[jaynes-2003-probability/ch13-decision]] — Inference only gives a posterior; to act, add a loss (utility) function and minimise expected loss over that posterior. A sampling theorist who thinks his estimation problem through to the end ends up obliged to use this same Bayesian calculation, even if he rejects its rationale.
- [[jaynes-2003-probability/ch14-simple]] — Signal-detection decision theory is ordinary Bayesian inference plus a loss function, so the classical criteria discussed here all reduce to a likelihood-ratio test whose threshold is the only thing they disagree about; the "widget problem" shows maximum-entropy priors, with no new data, can drive a decision.
- [[jaynes-2003-probability/ch15-paradoxes]] — Jaynes argues that the famous paradoxes of probability (nonconglomerability, Borel–Kolmogorov, marginalization) come mainly from using infinite sets, zero-measure conditions or improper priors as if the limit were already reached, and, in the tetrahedra and marginalization cases, from leaving prior information out of the notation.
- [[jaynes-2003-probability/ch16-orthodox]] — Jaynes argues that the "orthodox" statistics of about 1900–1970 answered pre-data (sampling-distribution) questions while claiming to answer post-data ones, and he links its course partly to the problems it faced and partly to personalities and ideology.
- [[jaynes-2003-probability/ch17-principles-p1]] — In simple problems, orthodox sampling-theory tools (unbiased estimators, tail-area significance tests, pre-filtering) waste, ignore or distort information, whereas Bayes' theorem has all the relevant information available; the Cramér–Rao bound turns out to be tied to maximum-entropy distributions.
- [[jaynes-2003-probability/ch17-principles-p2]] — Jaynes argues that, in the examples he gives, orthodox methods either lose information or reach Bayesian results only by a much longer route, and that integrating out nuisance parameters (parameters we must model but do not want to estimate) is the clean way to handle trend and seasonality.
- [[jaynes-2003-probability/ch18-p]] — Introducing the proposition "A_p: the probability of A is p" and keeping its density lets a reasoner store, in one function, what it needs from past experience about A, including how stable that state is, and yields Laplace's rule of succession as a defensible, well-defined inference.
- [[jaynes-2003-probability/ch19-physical]] — Applying Bayes' theorem to the "equations of condition" with Gaussian errors and a uniform prior gives the weighted least-squares estimate $\hat x=(\tilde AWA)^{-1}\tilde AWy$ and its accuracy $(\tilde AWA)^{-1}$, without any guess about linear combinations.
- [[jaynes-2003-probability/ch20-model]] — Comparing models is compound hypothesis testing: each model is scored by its prior-averaged likelihood, which equals its maximum likelihood times an Ockham factor, and that factor reflects prior plausibility rather than "simplicity" as such.
- [[jaynes-2003-probability/ch21-outliers]] — Whether to discard or keep an outlier depends on prior information about the apparatus, and Jaynes argues that a Bayesian mixture model of "good" and "bad" data, if flexible enough, delivers robustness automatically when it is desirable, with no ad hoc rule.
- [[jaynes-2003-probability/ch22-introduction]] — Jaynes treats Shannon's communication theory as maximum-entropy inference: the "source" distribution describes the *engineer's* state of knowledge, not a physical frequency, and many of the standard results follow from it.
- [[jaynes-2003-probability/appa-other]] — Jaynes argues that Kolmogorov's axioms, de Finetti's coherence and comparative (ordinal) probability are either special cases of, or weaker foundations than, his consistency-based extension of logic.
- [[jaynes-2003-probability/appb-mathematical]] — Jaynes fixes his notation and defends a "cautious approach": derive results on finite sets of propositions, then pass to infinite limits only at the end and only if the limit is well-behaved. He also defines "function" as the practical analyst does (good functions plus their well-behaved limits).
- [[jaynes-2003-probability/appc-convolutions]] — Cumulants are combinations of moments that add when functions are convolved; the (scaled) Taylor coefficients of the logarithm of the Fourier transform are additive and so are cumulants, and Jaynes argues they give all the independent ones.

## Big ideas across units
- **Probability as extended logic, derived from desiderata.** Plausibility as real numbers plus common sense and consistency forces the sum and product rules, so no appeal to "chance" is needed. Units: front-preface, ch01-plausible, ch02-quantitative, ch03-elementary, ch16-orthodox, appa-other (rival foundations are special cases or weaker).
- **Probabilities describe knowledge, not the world (the mind projection fallacy).** Logical dependence is not causal dependence, "physical probabilities" do not exist as properties of an object alone, and Gaussian or source distributions are states of knowledge. Units: ch01-plausible, ch03-elementary, ch04-elementary, ch05-queer, ch07-central-p1, ch09-repetitive-p2, ch10-physics, ch16-orthodox, ch19-physical, ch22-introduction.
- **Maximum entropy as the rule for assigning probabilities from partial information.** It appears as the Gaussian justification, as a result of counting multiplicities, as the exponential-family solution with its Gibbs/thermodynamic structure, and as the basis of Cramér–Rao equality, widget priors and communication design. Units: front-preface, ch07-central-p1, ch07-central-p2, ch09-repetitive-p1, ch11-discrete, ch14-simple, ch17-principles-p1, ch19-physical, ch22-introduction.
- **Prior information matters, and ignorance priors come from invariance.** The same data can lead to different conclusions under different priors or qualitative knowledge. Symmetry or transformation groups (Jeffreys priors, Bertrand's problem) fix "ignorance" priors, and improper ones are only limits. Units: front-preface, ch05-queer, ch06-elementary-p1, ch06-elementary-p2, ch12-ignorance, ch15-paradoxes, ch18-p.
- **Finite sets first, limit last.** Infinite-set paradoxes, such as nonconglomerability, Borel–Kolmogorov and marginalization, come from jumping to a limit without specifying how it is approached. Units: front-preface, ch02-quantitative, ch04-elementary, ch15-paradoxes, appb-mathematical.
- **Bayes versus orthodox methods, and integrating out nuisance parameters.** Sufficiency, ancillarity and the likelihood principle follow from the product rule. Orthodox tools such as unbiased estimators, tail-area tests, randomization and detrending lose information that Bayesian marginalization keeps. Units: ch04-elementary, ch06-elementary-p2, ch08-sufficiency, ch09-repetitive-p1, ch16-orthodox, ch17-principles-p1, ch17-principles-p2, ch21-outliers.
- **Hypotheses are judged only against stated alternatives.** This applies to marvels and ESP, goodness-of-fit (ψ versus χ²), model comparison with the Ockham factor, and good/bad data mixtures for outliers. Units: ch04-elementary, ch05-queer, ch09-repetitive-p2, ch20-model, ch21-outliers.
- **Decision theory is inference plus a loss function.** Mean, median and mode follow from the choice of loss, and the classical detection criteria reduce to a likelihood-ratio test with different thresholds. Units: ch06-elementary-p1, ch13-decision, ch14-simple.

## How to read it
- **Essential for the catalog's focus (entropy principle and communication theory):**
  - ch01-plausible and ch02-quantitative give the framing, with front-preface as orientation.
  - ch11-discrete is the entropy-principle chapter.
  - ch22-introduction is the communication-theory chapter.
- **Dependencies stated in the digests:**
  - ch02 builds on ch01's desiderata.
  - ch04 uses ch03's binomial sampling, and ch05 uses ch04's decibel evidence.
  - ch06-p2 continues ch06-p1, and ch07-p2 continues ch07-p1.
  - ch09-p1 introduces multiplicities and entropy, and ch09-p2 relies on ch04 and §9.9.
  - ch10 uses exchangeability from ch09.
  - ch11 draws on ch2 and ch9 ideas.
  - ch12 uses Shannon entropy and Jacobians.
  - ch14 uses the maximum entropy of ch11.
  - ch17-p1 uses ch11, and ch16 previews ch17.
  - ch21 uses de Finetti's theorem from ch18.
  - ch22 uses maximum entropy and partition functions from ch11.
- **Useful but not needed for the entropy and communication thread:** ch03, ch05, ch06, ch08, ch10, ch12–ch14 and ch18–ch21. Of these, ch09-p1 and ch12 are the closest to the entropy thread.
- **Opinion and history:** ch16 describes itself as history and opinion, and ch17 gives the technical comparison. Ch13 judges decision theory not fundamental.
- **Reference material:** appa-other and appb-mathematical expand on Ch. 2 and Ch. 15's themes, and appc-convolutions supports the convolution material in ch07-p2.

## Concepts introduced
Ids are listed once, in the unit where they first appear. A few ids appear under different spellings elsewhere (for example `evidence-decibel`, `sufficient-statistics`, `coxs-theorem`). These are noted at the end.

**Preface**
- [[probability-as-extended-logic]], [[cox-theorem]], [[maximum-entropy-principle]], [[frequentist-vs-bayesian-inference]], [[prior-distribution]], [[nuisance-parameter-elimination]], [[finite-sets-policy]], [[exploratory-phase]]

**Ch. 1**
- [[weak-syllogism]], [[strong-syllogism]], [[boolean-algebra]], [[material-implication]], [[adequate-set-of-operations]], [[plausibility-notation]], [[desiderata-of-plausible-reasoning]], [[reasoning-robot]], [[mind-projection-fallacy]]

**Ch. 2**
- [[product-rule]], [[sum-rule]], [[extended-sum-rule]], [[associativity-equation]], [[principle-of-indifference]], [[subjective-probability]], [[bayes-theorem]]

**Ch. 3**
- [[principle-of-indifference-maximum-entropy]], [[exchangeability]], [[hypergeometric-distribution]], [[binomial-distribution]], [[multiplicity]], [[expectation]], [[logical-vs-causal-dependence]], [[randomization-as-information-discarding]], [[markov-chain-transition-matrix]], [[sampling-distribution]], [[Bayes-inverse-problem]]

**Ch. 4**
- [[likelihood]], [[posterior-distribution]], [[evidence-decibels]], [[odds-likelihood-ratio-form]], [[logical-vs-causal-independence]], [[sequential-inference]], [[nonextensibility-multiple-hypotheses]], [[dead-hypothesis-resurrection]], [[nuisance-parameter-marginalization]], [[composite-hypothesis]], [[de-moivre-laplace-gaussian-approximation]], [[weber-fechner-law]]

**Ch. 5**
- [[relative-entropy-kl-divergence]], [[evidence-decibel]], [[device-of-imaginary-results]], [[resurrection-of-hypotheses]], [[deception-hypothesis-testimony]], [[alternatives-needed]], [[jeffrey-rule-critique]]

**Ch. 6 (part 1)**
- [[posterior-predictive-distribution]], [[laplace-rule-of-succession]], [[uninformative-about-N-condition]], [[stopping-rule-irrelevance]], [[posterior-mean-median-mode]], [[improper-prior]], [[maximum-likelihood-estimate]]

**Ch. 6 (part 2)**
- [[jeffreys-prior]], [[qualitative-prior-information]], [[chebyshev-inequality]], [[asymptotic-normality-of-posterior]], [[sure-thing-hypothesis]], [[frequentist-vs-bayesian]], [[bayesian-occams-razor]]

**Ch. 7 (part 1)**
- [[gaussian-distribution]], [[central-limit-theorem]], [[sufficient-statistics]], [[error-cancellation]], [[incremental-invariance-landon]], [[fisher-sufficiency-note]]

**Ch. 7 (part 2)**
- [[convolution]], [[characteristic-function]], [[cauchy-distribution]], [[nuisance-parameter]], [[regression-to-the-mean]], [[gaussian-mixture-inverse-problem]], [[hermite-polynomials]]

**Ch. 8**
- [[sufficient-statistic]], [[generalized-sufficiency]], [[likelihood-principle]], [[conditionality-principle]], [[ancillary-statistic]], [[blackwell-rao-theorem]], [[chain-consistency]], [[logical-independence]], [[sample-reuse-fallacy]], [[Fisher information]], [[Sequential updating]]

**Ch. 9 (part 1)**
- [[multiplicity-factor]], [[poorly-informed-robot]], [[induction]], [[extension-space]], [[partition-function]], [[entropy]], [[exponential-family]], [[relative-entropy-kl]]

**Ch. 9 (part 2)**
- [[probability-vs-frequency]], [[implied-alternatives]], [[bernoulli-class]], [[psi-test]], [[chi-squared-test]], [[p-value]], [[exponential-family-gibbs]], [[magnification-technique]], [[induction-as-plausible-reasoning]]

**Ch. 10**
- [[physical-probability]], [[strong-connection-probability-frequency]], [[symmetry-invariance-prior]], [[coarse-graining-phase-space]], [[arrogance-of-the-uninformed]]

**Ch. 11**
- [[principle-of-indifference-maxent]], [[shannon-composition-law]], [[wallis-derivation]], [[legendre-duality-logZ-S]], [[maxent-reciprocity-fluctuation-laws]], [[entropy-concentration]], [[information-vs-thermodynamic-entropy]]

**Ch. 12**
- [[differential-entropy]], [[invariant-measure]], [[ignorance-prior]], [[transformation-group-prior]], [[pre-prior]]

**Ch. 13**
- [[loss-function]], [[utility-function]], [[bayes-decision-rule]], [[risk-function]], [[admissibility]], [[complete-class-theorem]], [[minimax-criterion]], [[maximum-likelihood-as-01-loss]], [[kl-divergence]], [[entropy-hx]], [[kelly-criterion-doubling-rate]]

**Ch. 14**
- [[likelihood-ratio-test]], [[decision-rule]], [[bayes-decision-criterion]], [[neyman-pearson-criterion]], [[matched-filter]], [[false-alarm-false-rest]], [[entropy H(X)]], [[exponential family / Gibbs distribution]]

**Ch. 15**
- [[nonconglomerability]], [[conglomerability]], [[limit-last-policy]], [[finite-vs-countable-additivity]], [[borel-kolmogorov-paradox]], [[marginalization-paradox]], [[complete-ignorance]], [[zeta-overdetermination]], [[prior-information-notation]]

**Ch. 16**
- [[orthodox-statistics]], [[estimator]], [[pre-data-vs-post-data]]

**Ch. 17 (part 1)**
- [[unbiased-estimator]], [[bias-variance-decomposition]], [[cramer-rao-bound]], [[efficiency-umv-estimator]], [[tail-area-significance-test]], [[periodogram-and-prefiltering]], [[exponential-family-gibbs-distribution]]

**Ch. 17 (part 2)**
- [[marginalization]], [[monte-carlo-integration]], [[magnification]]

**Ch. 18**
- [[a-p-distribution]], [[sequential-updating]], [[weight-of-evidence]], [[hypothesis-space]], [[carnap-lambda-method]], [[inner-outer-robot]]

**Ch. 19**
- [[equations-of-condition]], [[generalized-inverse-problem]], [[gaussian-as-state-of-knowledge]]

**Ch. 20**
- [[marginal-likelihood]], [[ockham-factor]], [[high-likelihood-region]], [[fair-judge-vs-cruel-realist]], [[posterior-odds-for-models]]

**Ch. 21**
- [[outlier-two-model-mixture]], [[quasi-likelihood]], [[robust-resistant-estimation]]

**Ch. 22**
- [[channel-capacity]], [[bit]], [[partition-function-channel]], [[markov-chain-maxent]], [[noisy-channel]], [[checksum-block-coding]], [[source-coding-theorem]]

**Appendix A**
- [[kolmogorov-axioms]], [[sigma-field]], [[continuity-at-zero]], [[dutch-book-argument]], [[principle-of-indifference-max-entropy]], [[comparative-probability]], [[universal-comparability]], [[lattice-theory-of-plausibility]]

**Appendix B**
- [[cautious-approach-policy]], [[probability-symbol-notation]], [[good-function-and-limits]], [[delta-function]], [[fourier-operational-properties]], [[cramer-lower-bound]]

**Appendix C**
- [[moment]], [[cumulant]], [[fourier-transform-characteristic-function]], [[central-moment]]

*Spelling variants of ids above that appear in later units:*
- `evidence-decibel` is a variant of `evidence-decibels` (ch. 4 → ch. 5).
- `coxs-theorem` is a variant of `cox-theorem`.
- `sufficient-statistics` and `sufficient-statistic` are one concept.
- `frequentist-vs-bayesian` and `frequentist-vs-bayesian-inference` are one concept.
- `principle-of-indifference-maxent`, `principle-of-indifference-maximum-entropy` and `principle-of-indifference-max-entropy` are one concept.
- `exponential-family-gibbs` and `exponential-family-gibbs-distribution` are one concept.
- `relative-entropy-kl`, `relative-entropy-kl-divergence` and `kl-divergence` are one concept.
- `nuisance-parameter-marginalization` and `nuisance-parameter` are closely related to `marginalization`.
- A few others appear only in capitalized form, for example "Likelihood", "Bayes' theorem" and "Principle of indifference".

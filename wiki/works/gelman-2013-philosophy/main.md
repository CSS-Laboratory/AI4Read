---
id: gelman-2013-philosophy/main
work: gelman-2013-philosophy
unit: paper
pages: 1–26 (body); 26–36 (references, not digested)
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Philosophy and the practice of Bayesian statistics (Gelman & Shalizi)

## L0 — One line
The authors argue that good Bayesian data analysis is better understood as hypothetico-deductive (deduce implications of a model and test them against data) model building and model checking than as inductive updating of the probabilities that hypotheses are true.

## L1 — The gist (≤ 120 words)
Is Bayesian statistics best seen as inductive inference that ends in posterior probabilities of hypotheses? The authors argue it is not. In the practice they describe, the prior and the likelihood together form a set of assumptions. The analyst fits the model, checks it against data (for example by posterior predictive checks), and expands it when the checks show misfit. By general agreement, all models in use in social science are false, and updating probabilities among candidate models does not solve the problem of learning about flaws in existing models. They propose a hypothetico-deductive reading, much closer to Popper than to Kuhn. They say the inductive story has, at best, encouraged fitting models without checking them.

**Prerequisites:** Bayes' rule, prior/likelihood/posterior, p-values and test statistics, logistic regression, the idea of Kullback–Leibler divergence; no philosophy needed (Popper, Kuhn, Quine–Duhem are explained in the text).

## L2 — Key ideas
- **The target.** The "usual story" links Bayes to induction and treats the posterior p(θ|y) as the whole of inference. The authors think most of this received philosophy is wrong, not the Bayesian method itself (pp. 2, 3, fn. 2).
- **Analysis does not end at the posterior.** The fitted model can be checked by simulating data and comparing with the observed data. Discrepancies can be used to motivate model expansion. Two applied examples (voting patterns, redistricting) show the cycle (pp. 5, 8, 18–19).
- **Bayesian principal–agent problem.** The idealised Bayesian agent believes only what lies in the support of its prior (the parameter values the prior allows). Under regularity conditions, with a misspecified model, the posterior tends to concentrate on the prior-support values with the lowest divergence rate d(θ) (a measure of mismatch between the model at θ and the true data distribution). These values need not be good for the scientific parameters. Non-Bayesian checking is how the authors address this (pp. 9–11).
- **Posterior predictive checks.** They are the main tool: p-values of the form Pr(T(y^rep) > T(y) | y) generalise classical p-values. A very low value says the data would be very improbable if the model were true. Whether a high value is evidence for the model depends on how unlikely such a value would be if the model were false (pp. 11–12).
- **The prior is a testable part of the model.** It need not be a personal belief. It is "more like" a regularization device (something that stabilises estimates, as penalties do in ridge regression). So the authors see no need for unique objective priors (pp. 12–13).
- **Purpose of testing, and model expansion.** The aim is to learn how a model fails, not to show it is false. The authors prefer pure significance testing (checking a model's implications against data with no named alternative) and continuous model expansion (enlarging a model to contain the competitors) over model selection or averaging. They do not take posterior model probabilities as a general vehicle for scientific learning (pp. 14–17).
- **Induction.** The authors see no interesting and correct sense in which Bayesian statistics is a logic of induction that does not equally imply that frequentist statistics is also a theory of inductive inference. Both are deductively guaranteed by probabilistic assumptions (pp. 20–21).
- **Popper and Kuhn.** The authors' views are much closer to Popper's than to Kuhn's. They note an analogy between Kuhn's normal/revolutionary science and within-model updating versus model checking, and say they do not want to push it too far (pp. 24–25).
- **Why it matters.** The inductive view has, they say, encouraged fitting and comparing models without checking, and at worst actively discouraged checking. They recommend large models, graphical checks and continuous expansion (pp. 25–26).

## L3 — Walkthrough

### Abstract (p. 1)
- The authors say a school in philosophy of science identifies Bayesian inference with inductive inference and even with rationality. They argue that the most successful forms of Bayesian statistics fit sophisticated hypothetico-deductivism much better (p. 1).
- They examine the role of priors, and model checking and revision, which lie outside Bayesian confirmation theory. They draw on literature on consistency of Bayesian updating and on applied social-science work (p. 1).

### 1. The usual story (pp. 1–4)
- **Classical statistics** (Fisher p-values, Neyman–Pearson tests, confidence intervals) is linked to the hypothetico-deductive, falsificationist view. On this view, hypotheses can be rejected (falsified) but never really established or accepted in the same way. Mayo (1996) is the leading statement (p. 1).
- **Bayesian statistics** is linked to induction, learning the general from particulars. In this view, evidence accretes into a posterior, and science shows as rising and falling posterior probabilities of models (Figure 1). On this view p(θ|y) "says it all", and anything not in the posterior is irrelevant. This view is attributed to Savage's influence and to Bayesian confirmation theory (p. 2).
- **Authors' thesis.** They think most of the received view is wrong. Bayesian methods are no more inductive than other modes of inference. Best Bayesian practice has much in common with Mayo's error-statistical approach, and model checking can be seen as *error probes* (p. 2).
- **Fn. 2:** they claim the philosophy is wrong, not the inference. A method can be useful with a wrong justification (p. 2).
- **Fn. 3:** they do not mean Hempel-style confirmation theory, but an older hypothetico-deductive account (p. 2).
- **Social-science premise.** There is general agreement that all models in use are wrong, not merely falsifiable. With enough data, often a moderate amount, any analyst could reject any model now in use. Model fitting is still the crux of data analysis (p. 3).
- **Lineage.** They follow Box, Good, Morris, Hill, Jaynes and others, who stress model checking and frequency evaluation. This remains a minority view (p. 3).
- **Three possible readings** of the clash between that practice and the usual story:
  1. inductive Bayes is right and Box et al. can be reinterpreted;
  2. model checking could be improved by moving to posterior probabilities of competing models;
  3. Box et al. are right and the inductive story is faulty. The authors advocate (3) (pp. 3–4).
- **Fn. 4:** the authors report having met Bayesians who saw no reason to assess fit because Bayesian models are subjective (p. 4).
- They focus on Popper, Kuhn and Mayo, and admit their philosophical coverage is incomplete (p. 4).

*Intuition note.* The paper is about how Bayesian practice should be described, not about abandoning Bayesian inference (fn. 2, p. 2). The claim is that the checking step is what the inductive picture leaves out.

### 2. The data-analysis cycle (pp. 4–5)
- **Setup.** The model stochastically generates data y, with joint distribution given by a likelihood function of parameters θ in a space Θ (possibly infinite-dimensional). Latent or missing data ỹ and covariates may also appear. Bayesians insist on a full joint distribution over observables, latent variables and parameters, so the likelihood becomes a conditional density p(y|θ) (p. 4).
- **Meaning of parameters.** Some have concrete referents (the Baltimore rat survey). Others reflect the mathematical form (the degrees of freedom of a t-distribution for heavy-tailed noise). Few statisticians take the latter as realistically as the number of rats (p. 4).
- **Factorisation** (without loss of generality), with the prior part of the model:
$$p(y,\tilde y,\theta)=p(\theta)\,p(y,\tilde y\mid\theta),\qquad p(y\mid\theta)=\int p(y,\tilde y\mid\theta)\,d\tilde y .$$
  Functional forms are chosen by a mix of substantive knowledge, conjecture, convenience, tradition and tractability (p. 5).
- **Fitting.** The analyst computes the posterior p(θ|y). Bayesian methods rose in applications through new ways to compute it, notably MCMC (p. 5).
- **The view the authors reject.** Analysis ends with p(θ|y). It may be elaborated by splitting Θ into models Θ_1,…,Θ_K with priors p(Θ_k) and parameters θ_k, giving model posteriors (formula copied as printed, p. 5):
$$p(\Theta_k\mid y)=\frac{p(\Theta_k)\,p(y\mid\Theta_k)}{\sum_{k'}p(\Theta_{k'})\,p(y\mid\Theta_{k'})}
=\frac{p(\Theta_k)\int p(y,\theta_k\mid\Theta_k)\,d\theta_k}{\sum_{k'}\Big(p(\Theta_{k'})\int p(y,\theta_k\mid\Theta_{k'})\,d\theta_{k'}\Big)} .$$
  These feed Bayesian model selection or averaging. Progress then means gathering data and plotting p(Θ_k|y) over time (Figure 1) (p. 5).
- **Authors' reply.** This account is crucially mistaken. The process does not end with the posterior. The model can be checked: do simulations from the fitted model resemble the data? Is it consistent with data not used in fitting? Do supposed noise terms show detectable patterns? Discrepancies can be used to learn how the model is inadequate and to motivate expansion (p. 5).

*Intuition note.* In the rejected picture, learning is movement of probability among fixed candidate models. In the authors' picture, a further step compares the fitted model's implications with data, and that step can change which models are considered.

### 2.1 Example: voting patterns of income groups by state (pp. 6–9)
- **Model 1.** Votes are coded y = 1 for the Republican presidential candidate and y = 0 for the Democrat. Income is coded x = −2,…,2. A varying-intercept logistic regression: $\Pr(y=1)=\mathrm{logit}^{-1}(a_s+bx)$, with s the state. Intercepts a_s capture more or less Republican-leaning states, and b is the income slope (p. 8).
- **Check.** Graphs of average response and fitted curves by income within each state showed that this model did not fit (p. 8).
- **Model 2.** Varying intercept and slope: $\Pr(y=1)=\mathrm{logit}^{-1}(a_s+b_sx)$. This led to a substantive finding: the rich–poor voting gap is much greater in poor states such as Mississippi than in rich states such as Connecticut (p. 8).
- **Authors' reading.** This was found through model checking, not Bayesian induction. They never computed the posterior probability that a model was true. Bayesian inference mattered by letting them fit rich enough hierarchical models (partial pooling), including small states (p. 8).
- **After the 2008 election.** Even the varying-slope model did not fit, especially when estimating voting by ethnic group. Comparison with data led to the current specification: a varying-intercept, varying-slope logistic regression as baseline, plus nonlinear and non-monotonic patterns (p. 8).
- **Figures 2–3 captions.** The estimates in the Figure 2 maps are the culmination of months of effort, fitting increasingly complex models, checking fit at each stage and modifying prior and likelihood (p. 6). In Figure 3 (dots = weighted Pew survey averages, ±1 SE bars; curves from multilevel models with SE about 3%), only the last of a series of models fit well enough for them to be satisfied. With larger datasets and more complex questions there are more chances to check fit and falsify in a helpful way (p. 7).
- **Deductive power.** Given data and assumptions, many inferences follow, and many can be checked. In New York (Figure 3) voters in the second income category apparently supported McCain much more than neighbouring groups. This is theoretically possible but suspicious. It is a pattern in the raw data that was moderated, not smoothed away, by the model. The natural next step is other surveys (pp. 8–9).

*Intuition note.* In this example the discovery (varying slopes, then nonlinear patterns) came from graphs of misfit. The posterior was not compared across candidate models.

### 3. The Bayesian principal–agent problem (pp. 9–11)
- **Key idea.** Bayesian model selection (posterior probabilities of candidate models) does not solve the problem of learning from data about problems with existing models (p. 9).
- **Analogy.** In economics, a principal cannot cheaply monitor an agent, so incentives must align. The *Bayesian agent* is a methodological fiction: a prior over a well-defined Θ, a likelihood p(y|θ), and conditioning as its sole way of learning. The principal is the actual scientist (p. 9).
- **Precision of the agent.** In this formulation (which the authors reject), the agent is certain some θ is the exact and complete truth. The authors have never seen a social-science model close to that. Their own experience suggests there are always specifications not yet thought of that cannot be dismissed a priori. Yet the agent's prior must cover all alternatives that could be considered (p. 9).
- **Fn. 5:** they do not say actual Bayesians hold this view. They say it is implied by the philosophy they attack (p. 9).
- **Fn. 6:** it is not clear that Savage and other founders meant the principle to apply outside small, stylised worlds (p. 9).
- **A catch-all value.** Adding a value θ^∞ for none of the above is not a small technical fix. Even if p(y|θ^∞) could be computed, in general the effect on the posterior would not be a small correction (p. 9, citing Fitelson and Thomason).
- **Limits of beliefs.** The agent's beliefs always remain within the support of its prior. The truth must already be partially believed before it can become known (p. 10).
- **Doob-type consistency.** Classical results say the posterior concentrates on the truth with *prior* probability 1 if regularity conditions hold. In short: (i) the truth is in the support of the prior; (ii) the information is rich enough that some consistent estimator exists. If the truth is not in the support, the agent still thinks Doob's theorem applies, and assigns zero prior probability to the data sets on which it fails to converge (p. 10).
- **Misspecified case.** If data actually come from q, define the divergence rate (as printed on p. 10; expectation under q):
$$d(\theta)=\lim_{n\to\infty}\frac1n\,\mathbf E\!\left[\log\frac{p(y_1,\dots,y_n\mid\theta)}{q(y_1,\dots,y_n)}\right].$$
  Under not-too-onerous regularity conditions (Shalizi, 2009), with d* the essential infimum of the divergence rate:
$$p(\theta\mid y_1,\dots,y_n)\approx p(\theta)\exp\{-n(d(\theta)-d^*)\},\qquad -\frac1n\log p(\theta\mid y_1,\dots,y_n)\to d(\theta)-d^* \ \ q\text{-almost surely}.$$
  So the posterior comes to concentrate on parts of the prior support with the lowest d(θ) and highest expected likelihood. Regions with d(θ) > d* tend to have exponentially small posterior probability (fn. 7) (p. 10).
- **Caveats the authors give.** These regions are in a geometric sense the closest approaches to the truth within the prior's support. They may or may not give accurate values of scientifically interesting parameters, and may not even give the best predictions. If d(θ) has multiple global minima, the posterior can alternate between them forever (p. 10).
- **Summary.** With a false model (in reality, always), updating tries to concentrate the posterior on the best attainable approximations, "best" measured by likelihood. Depending on how the model is misspecified, the effect on the scientific parameters can range from non-existent to profound (pp. 10–11; fn. 8 on White's examples, p. 11).
- **Resolution.** Because the authors are quite sure their models are wrong, they say one must check whether misspecification threatens inferences about scientific parameters. This non-Bayesian checking of Bayesian models is how they solve their principal–agent problem (p. 11).

*Intuition note.* Conditioning reweights the candidates the prior allows. If all are wrong, the posterior may still sharpen, but around the candidate that is best by likelihood. That candidate need not be adequate for the question of scientific interest, which is why a separate check is needed.

### 4. Model checking (pp. 11–14)
- **Posterior predictive checks.** The authors emphasise simulating data and comparing, often visually (following Box, Rubin and Tukey) (p. 11).
- **Distributions** (copied from pp. 11, 13). The model implies a marginal distribution of the data; after observing y, a posterior predictive distribution of replicated data y^rep, "of the same size and shape" as y, generated assuming the fitted model (prior and likelihood) is true:
$$p(y)=\int p(y\mid\theta)p(\theta)\,d\theta,\qquad p(y^{\rm rep}\mid y)=\int p(y^{\rm rep}\mid\theta)\,p(\theta\mid y)\,d\theta .$$
  Simulating y^rep shows what typical realisations of the fitted model look like and whether the observed data are the kind of thing it produces with reasonably high probability (p. 11).
- **Test statistic and p-value.** For a summary T(y), they use
$$\Pr\big(T(y^{\rm rep})>T(y)\mid y\big),$$
  approximated by simulating y^rep. It is a valid posterior probability within the model. In practice they find graphical comparisons more illuminating (p. 11).
- **Fn. 9:** hidden variables ỹ and the choice of which parameters to hold fixed are left out for simplicity (p. 11).
- **Logic.** With T chosen so large values mean poor fit, these p-values generalise classical ones by averaging over the posterior instead of plugging in point estimates. A very low p-value says the data would be very improbable if the model were true. A high p-value merely says T(y) is unsurprising if the model is true. Whether that is evidence for usefulness depends on how likely a high p-value would be if the model were false: the *severity* of the test (Mayo) (p. 12).
- **Hypothetico-deductive reading.** The model's probabilistic assumptions deductively imply other probabilistic regularities. Simulation works them out, and tests check whether data conform. If violations were of deterministic implications, modus tollens would apply. As it is, we get evidence and probabilities. The authors place this in the hypothetico-deductive tradition from Popper back to Bernard, with a direct influence from Jaynes: one may learn most when the model is falsified, because a problem with its assumptions has been found (p. 12).
- **Fn. 10:** there is controversy about the power of posterior predictive checks and how to modify them. The authors say all participants in the debate agree on why tail-area probabilities are relevant: they allow rejecting a Bayesian model without a specific alternative. So all disagree with the standard inductive view (p. 12).
- **The prior is checkable.** The prior is one of the model's assumptions and need not represent the statistician's personal degree of belief. It is testable through the posterior predictive distribution (expanded form from p. 13):
$$p(y^{\rm rep}\mid y)=\int p(y^{\rm rep}\mid\theta)\,\frac{p(y\mid\theta)\,p(\theta)}{\int p(y\mid\theta')p(\theta')\,d\theta'}\,d\theta .$$
  So the prior has implications for replicated data. If further data may come from the same source (sampling, time series, longitudinal), it is testable in a second way. Fn. 12: the prior has observable implications only together with the likelihood, but for a Bayesian the reverse is also true. The authors note a connection to prequentialism without pursuing it (p. 13).
- **Where priors come from.** Most statisticians do not believe their models are true, so their prior degree of belief in all of Θ is not 1 but 0. The prior is more like a regularization device, akin to penalties in ridge regression, the lasso and spline smoothing. Such devices exploit a sensitivity–stability tradeoff. An informative prior (even weakly informative) makes estimates less sensitive to the data than maximum likelihood, which can be a net gain (p. 13).
- **Consequence.** The authors do not need Jaynes's search for a unique objectively correct prior, which they say has an uninspiring track record. "The model," for a Bayesian, is prior plus likelihood, each a compromise among scientific knowledge, convenience and tractability. One states assumptions, sees their implications, and checks them (p. 13).

*Intuition note.* A check compares what the model says would happen with what happened. A very small p-value would be improbable if the model were true. A large one says less, unless the test would probably have caught the problem had it existed.

### 4.1 Testing to reveal problems (pp. 14–15)
- The authors are not interested in falsifying for its own sake. Having built the model, they are morally certain it is false. With enough data departures can be detected (folklore: chi-squared is ultimately a measure of sample size). Following Giere, the hypothesis linking model to data is that the source resembles the model closely enough, in respects that matter, that model-based reasoning is reliable (p. 14).
- **Goal.** Learn how this model fails. Particular failures tell how to improve it, and when severe tests find none, inferences about those aspects become more credible. A good test is sensitive to specific errors that would damage specific inferences. This resembles Kitcher's *eliminative induction*, which Kitcher notes is actually deductive (fn. 14) (p. 14).
- **Noise should be patternless.** Statistical models typically assert that approximation errors are unsystematic. In the voting example, varying slopes mattered not just because of the size of departures from equal slopes but because of a pattern: richer states tended to have shallower slopes (p. 14).
- **Pure significance testing** (Cox and Hinkley): compare model implications directly to data, without a contest against an alternative model. The authors think this is more in line with science. Newtonian physics around 1900 faced many difficulties before relativity and quantum mechanics. They say current best theories are universally agreed to be ultimately wrong, and recognising this does not require a replacement theory (pp. 14–15).
- **Fn. 13:** no model is safe from criticism even if it passes all checks. Latent variables bring nonidentifiability. The authors find it dubious that a prior on non-identified quantities resolves this, and say the bounds (partial identification) approach seems to be in better accord with scientific norms (p. 14).

### 4.2 Connection to non-Bayesian model checking (p. 15)
- The reasoning is shared with other communities: a model is a story of how data could arise, so the fitted model should generate data that look like the real data (p. 15).
- **Social networks.** Simulation-based checking is now widely accepted for assessing goodness of fit of social-network models. That community was pushed toward predictive checking by the observation that many specifications were *degenerate*. Under certain exponential-family models, the maximum likelihood estimate gave a bimodal distribution over networks, both modes very different from observed networks, yet with expected sufficient statistics matching the observations (p. 15).
- **Mayo's severity.** A model is severely tested if it passes a probe that had a high probability of detecting an error if present. The definition is related to, but not quite, that of power. Posterior predictive checks can be framed non-Bayesianly as graphical hypothesis tests based on the parametric bootstrap (p. 15).
- **Contribution.** Connecting this philosophy to Bayesian data analysis, going beyond evaluating Bayesian methods by their frequency properties (p. 15).

### 4.3 Why not just compare posterior probabilities of models? (pp. 15–17)
- **Standard view.** Compare posterior odds (fn. 15: Bayes factors work the same way for their purposes). On it, quoting Schervish, pure significance tests "have no role to play in the Bayesian framework" (pp. 15–16).
- **Authors' reply.** There is no hope of making Θ include all distributions that might be correct. They do not see Bayesian methods as generally useful for the posterior probability that a model is true or for preferring A over B. A technical problem: in continuous-parameter models, aspects with essentially no effect on inference *within* a model can hugely affect posterior probabilities *among* models (Jeffreys–Lindley; fn. 18: they think it has no solution) (p. 16).
- **Fn. 17:** they accept that these tools can be useful for prediction and understanding structure if posterior model probabilities are not taken too seriously (p. 16).
- **Not a defence of p-values.** Citing the Jeffreys–Lindley literature, p-values can drastically overstate evidence against a null. In their view the point of p-values is to explore misfit, not to reject a null (p. 16).
- **Continuous model expansion.** If A or B might be true, they prefer a larger model containing both as special cases, instead of selection or averaging (such as 40%/60%). Example (Merrill 1994): a *proximity* model (prefer the nearest party) versus a *directional* model (prefer parties in your direction, more strongly the further from the centre). Rather than picking one, they would build a model where voters consider both (pp. 16–17).
- **Nonparametrics.** Taken to its limit, expansion counsels social scientists to use infinite-dimensional models, and the authors are sympathetic. Cautions: (a) Bernstein–von Mises (large-sample credible regions are confidence regions) fails in infinite dimensions, so naive posterior uncertainty is unwise (not troubling for them, since they treat prior and posterior as regularization devices); (b) the prior is a stochastic process chosen for tractability, with any pretence of representing beliefs abandoned; (c) nonparametric models still embody assumptions such as conditional independence. Embracing all models compatible with prior knowledge would be an unworkable mess, so they see no contradiction with using checked parametric models (p. 17).
- **Fn. 21:** other perspectives (robust procedures, prediction with external validation) reduce reliance on models of the data source. The authors recognise their appeal but say working with all possible models is not possible for fully probabilistic methods (p. 17).

*Intuition note.* The inductive view assumes the true model (or the models being chosen among) is among those listed. Also, in continuous-parameter models, aspects with essentially no effect on inference within a model can have huge effects on the comparison among models. The authors prefer to enlarge the model until it contains the competitors, then check it.

### 4.4 Example: effects of legislative redistricting (pp. 18–19)
- **Setup** (Gelman and King, 1994). Treated units are state legislatures just after redistricting, controls are those not redistricted. The outcome is partisan bias (positive = Democrats overrepresented relative to estimated Republican performance at comparable vote shares). The default before-after model assumes a constant treatment effect, i.e. parallel regression lines (Figure 4) (p. 18).
- **Check.** Graphs showed the model did not fit: the control line had a much steeper slope than the treated one (p. 18).
- **Interaction model** (Figure 5). The largest effect of redistricting was to change the slope, bringing expected partisan bias toward zero, not to shift the intercept in either party's favour (p. 18). This higher before–after correlation in controls is quite general (Gelman 2004), but they found it only through the graph (p. 18).
- **Philosophical point.** They falsified a model "in a useful way without the specification of any alternative", then added an interaction. The falsification came from a graph, which also showed the direction of misfit (p. 19).

### 5. The question of induction (pp. 19–21)
- **If induction just means inference from particulars to the general** (from y to θ), then frequentist statistics is inductive (Mayo and Cox), as are guess-and-test behaviours. So are silly procedures, such as picking models at random and switching when error accumulates, or picking a new θ at random on an arbitrary digit rule. So something more is meant by those who call Bayes inductive (p. 20).
- **Candidate: truth-preservation in the limit** (suggestion credited to Kevin Kelly, fn. 22). This is just consistency. Bayes' rule is neither sufficient nor necessary for consistency. Every Bayesian consistency proof the authors know either posits a consistent non-Bayesian procedure or makes assumptions entailing one. Consistency theorems are deductively valid but rest on probabilistic assumptions linking future events to past data (p. 20).
- **Candidate: axiomatised rationality.** With the Kolmogorov and Savage axioms (or something like them), a prior p(θ) plus data y deductively entail the posterior p(θ|y). But many learning procedures can be axiomatised (all algorithmic ones). To choose this system we must know it gives good results, which returns to consistency (p. 20). Fn. 23: Jaynes advocated Bayes as the logic of induction but followed Cox rather than Savage, and Halpern shows the formal invalidity of Cox's proofs (p. 20).
- **Anti-inductivism.** Popper denied induction was possible. Greenland's paraphrase: no argument from repeated instances avoids a hypothesis predicting both seen and unseen instances. The tradition runs back through Hume to al Ghazali and the ancient Skeptics. Stove argued that apparent replies are statements of premises linking observed and unobserved cases (uniformity of nature, Russell's postulates). He built a parallel argument for angels (p. 20). Fn. 24: Stove further argues that induction by simple enumeration is at least sometimes reliable without such assumptions, but the authors say his calculations make no sense unless his data are i.i.d. (p. 21).
- **Norton's material theory.** Such abstract premises are dubious and often superfluous. Inductions are supported by material facts. Generalising the melting point of bismuth needs few samples, provided we accept certain facts about the homogeneity of elemental substances. Whether nature in general is uniform is not at issue (p. 21).
- **Authors' position.** The anti-inductivist view is pretty much right, but statistical models are tools for drawing inductive inferences on a deductive background. Random sampling lets us learn about unsampled units, but this rests on deductions from the statistical properties of random samples and on actually sampling, not on an axiom of induction (p. 21).
- **Learning theory.** PAC-style "distribution-free" results hold uniformly over a large class (e.g. i.i.d. or stationary mixing data) and sometimes cover Bayesian updating. Assumption-free results (Cesa-Bianchi and Lugosi) say that in retrospect the posterior predictive did almost as well as the best individual model. They speak about past training data, not extrapolation to unseen cases (p. 21).
- **Summary.** One may call statistical inference inductive logic, but these are inductions deductively guaranteed by the probabilistic assumptions of stochastic models. The authors see no interesting and correct sense in which Bayesian statistics is a logic of induction which does not equally imply that frequentist statistics is also a theory of inductive inference (p. 21).

*Intuition note.* The authors argue that each way of making "induction" precise leads back to deductive guarantees from probabilistic assumptions (consistency), or to axioms that raise the consistency question again, or to learning-theory results that need distributional assumptions or speak only about past data. They see no sense of "inductive" that fits Bayesian but not frequentist statistics.

### 6. What about Popper and Kuhn? (pp. 22–25)
- **Popper** (as the authors sketch him, not claiming a full portrait). Science advances by bold, refutable theories tested so that a match is not assured. Theories with no conceivable refuting evidence are not scientific for Popper (this demarcation criterion has been criticised, fn. 26). No finite data establish a generalisation, and there is no non-circular principle of induction (fn. 27: his corroboration and verisimilitude notions are generally regarded as failures). Objectivity lies in community organisation and institutions, not in individual detachment (p. 22).
- **Authors agree** with the hypothetico-deductive view and the anti-inductivism. But Popper's idea of a test is the rule "if p implies q and q is false, then p is false", which they call plainly inadequate for statistical hypotheses. As critics have noted since Braithwaite, he oddly ignored statistical testing (fn. 28: they find his ideas on probability of little use). They add that one can do better with standard tests and predictive checks, and, following Mayo, that the severity of tests is vital (p. 22).
- **Kuhn.** Descriptive rather than prescriptive. A *paradigm* is a problem-and-solution exemplar, with presuppositions about what counts as a problem or solution (fn. 29 gives examples). *Normal science* is puzzle-solving within a paradigm. Anomalies are generally ignored or at most put aside for later investigation. Kuhn invokes the Quine–Duhem thesis: Quine and Duhem claimed that, if predictions fail, one is always free to blame the auxiliary hypotheses (the authors note the thesis can be attacked, fn. 30). Lakatos used it to separate progressive from degenerate research programmes. Anomalies may accumulate into crisis and *revolutionary science*, with a new, *incommensurable* paradigm. Kuhn held that holdouts and converts are both rational, and the switch is more like a bistable illusion (duck/rabbit) than rule-governed reasoning (p. 23).
- **Analogy.** Updating within a Bayesian model takes prior and likelihood as unchallengeable, like normal science. Model checking corresponds to identifying anomalies, with a switch to a new model when they become intolerable. Intercepts in varying-intercept and varying-slope models mean somewhat different things, a counterpart to translation problems. The authors do not want to push the analogy too far, since Kuhn would count most model revision as puzzle-solving within one paradigm (p. 24).
- **Critique of the sharp break** (Donovan et al., Toulmin). Paradigms tend to be expanded (vague, enduring; this corresponds, they say, to relentlessly enlarging the prior's support) or shrunk (any conceptual change counts as revolution). The authors suggest some validity to both moves: a *(weak) self-similarity*, with normal science punctuated by revolutions at every scale, from consulting sessions to scientific consensus over decades. The big changes rest on extending theories far enough that they can be decisively refuted (pp. 24–25). Fn. 31: Salmon's proposal to choose paradigms by Bayes' rule has three problems, including needing strictly positive prior probability for a paradigm before it is stated (p. 24).
- **Conclusion.** The authors' views are much closer to Popper's than Kuhn's. Deductive model checking is central, and the threat of such checks motivates inference within models known to be false (p. 25).

### 7. Why does this matter? (pp. 25–26)
- The authors say the idea of Bayesian inference as inductive, culminating in posterior probabilities of hypotheses, has had malign effects: at best researchers fit and compare models without checking, at worst theorists discouraged checking (p. 25).
- **Their approach.** Build a model from available parts and drive it as far as it goes. When it breaks down, dissect it, mainly via posterior predictive checks and often visual comparison. Then tinker or try a new design. Deduction is a tool for getting the most out of the model, which is falsifiable and is altered or abandoned when consequentially falsified. They say this is no more subjective than other scientific inquiry (p. 25).
- **A problem with the inductive view:** it assumes the true model, or the models to choose or average over, is among those considered. This does not match their experience of expanding beyond the existing class (p. 26).
- **Recommendations.** Construct large models that can incorporate diverse data, use Bayesian inference to summarise parameter uncertainty, use graphical checks to understand limitations, and move by continuous expansion instead of selection or discrete averaging. They claim no novelty and say the paper aims to show this practice is compatible with a hypothetico-deductive philosophy (p. 26).
- They fear a view of Bayes as subjective, inductive inference can encourage complacency about picking or averaging among existing models. Fn. 32 cites Ghosh and Ramamoorthi, who see a similar attitude as discouraging inquiry into consistency (p. 26).

## Toy example (ours, not from the text)
**Idea:** the model with the higher posterior probability can still fail a check. Data: 10 coin flips, y = HHHHHTTTTT. Candidate models, each with a fixed θ = P(heads), prior probability ½ each: A: θ = 0.5; B: θ = 0.9. All flips independent.

**Step 1: model posteriors.**
- Likelihood under A: $0.5^{10}=1/1024\approx 0.000976563$.
- Likelihood under B: $0.9^5\times0.1^5 = 0.59049\times0.00001 = 0.0000059049$.
- $p(A\mid y)=\dfrac{0.000976563}{0.000976563+0.0000059049}=\dfrac{0.000976563}{0.000982468}\approx 0.994$, so $p(B\mid y)\approx 0.006$.
- An agent who only updates would conclude "A, almost certainly."

**Step 2: check A.** Let T(y) = number of adjacent pairs with equal outcomes (9 pairs). The data have HHHHH (4 equal pairs), one switch, TTTTT (4 equal pairs), so T(y) = 8. Under A, the 9 equality indicators are independent fair Bernoulli variables. This holds because, for independent fair flips, whether each flip matches its predecessor is itself a fair coin and is independent of the other matches. So T(y^rep) ~ Binomial(9, ½).
- $\Pr(T(y^{\rm rep})\ge 8)=\dfrac{\binom98+\binom99}{2^9}=\dfrac{9+1}{512}\approx 0.0195$.
- A is unlikely to produce such long runs. The check flags a specific failure of A: it assumes flips are independent, but the data show strong dependence between neighbours.

**Step 3: lesson.** The 0.994 says only that A beats B. The 0.0195 says that A, the winner, fails a check. In the paper's spirit, the next move is to expand the model (for instance, let each flip depend on the previous one), not to keep updating between A and B. 

## Concepts
- [[inductive-bayesianism]] (new) — the "usual story": Bayes as inductive inference ending in posterior probabilities of hypotheses (pp. 1–2)
- [[hypothetico-deductivism]] (new) — deduce implications of a model, test them against data, reject or revise; used by the authors for Bayesian analysis (pp. 1–2, 12)
- [[posterior-distribution]] — p(θ|y); on the usual story it is all of inference, for the authors it is only the output of the fitting step (pp. 2, 5)
- [[prior-distribution]] — here an assumption of the model, testable, not necessarily a belief; "more like" a regularization device (pp. 12–13)
- [[prior-as-regularization]] (new) — prior viewed like ridge/lasso/spline penalties that trade sensitivity for stability (p. 13)
- [[likelihood]] — the model's p(y|θ); the full joint distribution makes it a conditional density (p. 4)
- [[posterior-predictive-check]] — compare y with replicates y^rep from p(y^rep|y); p-value Pr(T(y^rep) > T(y) | y) (p. 11)
- [[severe-testing]] (new) — Mayo's idea: a model passes severely if the probe would probably detect an error that is present; related to but not the same as power (pp. 12, 15)
- [[pure-significance-testing]] (new) — test a model's implications against data without a specific alternative (p. 14)
- [[model-misspecification]] (new) — all models in use in social science are false by general agreement; posterior behaviour then follows d(θ) (pp. 3, 10)
- [[bayesian-principal-agent-problem]] (new) — idealised Bayesian agent is confined to the prior's support, unlike the scientist (pp. 9–10)
- [[kl-divergence]] — the divergence rate d(θ) governs where the misspecified posterior concentrates (p. 10)
- [[marginal-likelihood-evidence]] — p(y|Θ_k) enters model posteriors; the authors doubt such probabilities are a general vehicle for learning (pp. 5, 16)
- [[continuous-model-expansion]] (new) — build a larger model containing competitors as special cases instead of selecting or averaging (p. 16)
- [[hierarchical-multilevel-model]] — varying-intercept/slope logistic regressions with partial pooling (p. 8)
- [[partial-pooling-shrinkage]] — mentioned as what the hierarchical models allow, including for small states (p. 8)
- [[frequentist-vs-bayesian-inference]] — the authors say Bayesian methods are no more inductive than other modes of inference, and see much in common between best Bayesian practice and Mayo's frequentist error-statistical approach (pp. 2, 21)
- [[quine-duhem-thesis]] (new) — the claim (invoked by Kuhn) that one is always free to blame auxiliary hypotheses for failed predictions (p. 23)
- [[normal-vs-revolutionary-science]] (new) — Kuhn's puzzle-solving vs paradigm change; compared in part with within-model updating vs model checking (pp. 23–24)

## Canonical instances
- [[red-state-blue-state-voting-model]] (new) — varying-intercept then varying-slope then nonlinear logistic regression, driven by checks (pp. 8–9, Figs. 2–3)
- [[redistricting-partisan-bias]] (new) — parallel-lines model rejected by a graph, interaction model found (pp. 18–19)
- [[network-model-degeneracy]] (new) — MLE bimodal over networks, far from observed networks; this degeneracy pushed the field toward predictive checking (p. 15)
- [[proximity-vs-directional-voting]] (new) — Merrill's two models; the authors would prefer to combine them rather than select one (pp. 16–17)
- [[newtonian-physics-anomalies]] (new) — theory known to be in trouble without a replacement (p. 14)
- [[bismuth-melting-point]] (new) — Norton's example of induction supported by material facts (p. 21)

## Bridges (candidates)
- [structural-analogy] posterior predictive p-value ↔ frequentist parametric-bootstrap goodness-of-fit: both simulate replicates from the fitted model, but the Bayesian one averages over the posterior and the bootstrap plugs in a point estimate (pp. 12, 15)
- [structural-analogy] prior as regularization ↔ penalties in ridge, lasso, splines: all trade sensitivity for stability, as the authors say (p. 13)
- [structural-analogy] posterior under misspecification concentrating where d(θ) is smallest ↔ maximum-likelihood/quasi-likelihood under a wrong model (White, p. 11, fn. 8): both target the best-fitting member of a wrong family
- [structural-analogy] data-analysis cycle (fit, check, expand) ↔ Bayesian workflow in the canon (p. 5; canon link, not stated in this unit)
- [metaphor] Kuhn's normal vs revolutionary science ↔ within-model updating vs model checking: the authors warn against pushing it too far (p. 24)

## Questions this raises
- Since it is debated whether posterior predictive checks have too little power (fn. 10, p. 12), how should T be chosen so that tests are severe for the inference one cares about?
- When is a continuous model expansion large enough to be useful but small enough to be checkable? (pp. 16–17)
- Can model-misspecification theory be combined with checking to say when a within-model posterior is still trustworthy for the scientific parameter? (pp. 10–11)
- If Bayes is "inductive" only through its assumptions, what does that imply for choosing between Bayesian and frequentist methods in practice? (p. 21)

## Reading notes
- **Edition.** The pages are the arXiv version (arXiv:1006.3868v4 [math.ST], dated 27 June 2011 on the title page, with an arXiv stamp of 28 Jun 2011). Metadata cites the journal version (BJMSP 66(1), 8–38), whose pagination differs. All page numbers here are the printed numbers on these pages. Printed = pdf. References occupy pp. 26–36 and are not digested.
- **Possible sign misprint, p. 10.** The page image shows $\log\big(p(y_1..y_n|\theta)/q(y_1..y_n)\big)$ inside d(θ). With this order, d(θ) is minus a Kullback–Leibler divergence, so "lowest d(θ)" would not match "highest expected likelihood". The text's statements fit the reverse ratio q/p. I copied the equation as printed.
- **Notation oddity, p. 5.** The second line of the model-posterior formula has θ_k with dθ_{k'} in the denominator, as printed. I kept it.
- **Typos in the source.** "peroperties" (p. 3), "ways of to actually" (p. 5), "Michaelson-Morley" (p. 14), "we we" (fn. 18, p. 16), "which which" (p. 17), "just much" (p. 13), "ac-count, in contrast" (p. 23). The sentence ending "Bayesian inference is good for deductive inference within a model we prefer to evaluate a model by comparing it to data" (p. 16) has a missing connective. On p. 20 the clause "…formalized in the hypothetico-deductive method are also inductive" is garbled. The Figure 5 caption lacks its closing parenthesis (p. 19).
- **Text layer.** It was clean. I checked the equations against the page images. Figures 1–5 were read from the images and captions, not described in detail.
- **Footnote 11 (Tilly quote, p. 12)** is not summarised in L3.

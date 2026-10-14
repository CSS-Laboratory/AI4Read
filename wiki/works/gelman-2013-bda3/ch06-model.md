---
id: gelman-2013-bda3/ch06-model
work: gelman-2013-bda3
unit: "6 Model checking"
pages: 141-164
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Model checking (BDA3, Chapter 6)

## L0 — One line
A fitted Bayesian model should be checked by simulating replicated data from its posterior predictive distribution and comparing them with the observed data, to see where and how much the model fails for its purpose.

## L1 — The gist (≤ 120 words)
How can we tell whether a fitted Bayesian model is adequate? The chapter's answer: simulate replicated datasets from the posterior predictive distribution and compare them with the observed data, using numerical test quantities, tail-area (p-)values, and graphs. Systematic differences indicate potential failings. The aim is to learn how and where the model is inadequate for its purpose, not to accept or reject it. Sensitivity analysis asks how much inferences change under other reasonable models. Examples include Newcomb's speed-of-light data, adolescent smoking, and the eight schools.

**Prerequisites:** posterior and posterior predictive distributions; simulation from a posterior; hierarchical models (Ch. 5, eight-schools example); classical test statistics and p-values; Beta–Binomial updating.

## L2 — Key ideas (5–10 bullets)
- Bayesian inference assumes the whole model structure (likelihood, prior, hierarchy, predictors), so checking fit to the data and substantive plausibility is crucial. A super-model covering all possibilities is conceptually impossible and computationally infeasible except in the simplest problems (pp. 141–142).
- The authors prefer not to ask whether the model is true, since models are rarely perfectly true; the more relevant question is whether its deficiencies noticeably affect the inferences of interest. Sensitivity analysis asks how much inferences change under other reasonable models (pp. 141–142).
- Posterior predictive checking: draw $y^{\rm rep}$ from $p(y^{\rm rep}\mid y)$ and compare a test quantity $T(y,\theta)$ for observed and replicated data. $T$ may depend on $\theta$ as well as the data; because simulation draws all parameters from the posterior, nuisance parameters need no special handling (pp. 145–146).
- The posterior predictive p-value is a posterior probability about future replications; in general it is not a $u$-value, and it is not $\Pr(\text{model true}\mid\text{data})$. A model is suspect when the discrepancy is practically important and the p-value is near 0 or 1 (pp. 150–152).
- The test quantity must fit the purpose: the sample variance is a poor test statistic here because it is a sufficient statistic of the model, whereas the minimum and the switch count detect real misfit. The authors make no multiple-comparisons adjustment, because they use checks to understand the limits of applicability, not to accept or reject (pp. 146–150).
- The sampling rule matters for checking even when likelihoods are identical, because replications depend on the data-collection protocol (p. 152).
- Marginal, cross-validation and mixed predictive checks give per-observation p-values that in general behave differently from joint checks (pp. 152–153).
- Graphical checks (full data display, parameter batches against their prior, binned residuals) compare displays to replications. Good ordering and binning make misfit visible (pp. 153–158).
- In the eight-schools case, the checks seem to support the posterior inferences, and a sensitivity analysis covers prior on τ, normal population and normal likelihood (pp. 159–161).

## L3 — Walkthrough

### 6.1 The place of model checking in applied Bayesian statistics (pp. 141–142)
- After building a model and computing the posterior, one should assess fit to the data and to substantive knowledge. It is difficult to include all of one's knowledge in a probability distribution (p. 141).
- Bayesian prior-to-posterior inference assumes the whole probability model and can mislead if the model is poor. "Model" here includes sampling distribution, prior, hierarchical structure, and choice of explanatory variables. The likelihood is typically just as suspect as the prior (p. 141).
- **Sensitivity analysis:** how much do posterior inferences change when other reasonable models replace the present one? A model may fit adequately while inferences still differ under plausible alternatives (p. 141).
- In theory, checking and sensitivity can be built into one comprehensive joint distribution (a mixture of all possible "true" models). Its posterior would automatically include sensitivity analysis but would still presume that some member of the class is true. In practice this is conceptually impossible and computationally infeasible except in the simplest problems, so models must be examined in other ways (pp. 141–142).
- **Judging flaws by practical implications.** The authors do not like asking "true or false?", since even coin tosses and die rolls are not truly exchangeable. The relevant question is whether deficiencies noticeably affect substantive inferences. In the Chapter 5 examples (beta population for tumor rates, normal for eight school effects), convenient assumptions turn out not to matter for the main inferences (p. 142).

*Intuition note:* Models in most analyses are not perfectly true. What matters is whether the flaws noticeably change the answers you care about.

### 6.2 Do the inferences from the model make sense? (p. 142–143)
- Knowledge that is not formally in the prior or likelihood can show that posterior inferences are false, suggesting a better model (p. 142).
- **Example (1992 election).** A hierarchical linear regression gave posterior probabilities that Clinton wins each state (Figure 6.1, p. 143). Even before the election, some forecasts looked wrong. For instance, state polls showed Clinton much weaker in Texas and Florida than the map. This does not mean the forecast is useless, but it is good to know where its weak points are (p. 142).
- **External validation:** predict future data, then collect them and compare. Posterior means should be correct on average, 50% intervals should contain the truth half the time. It was used in Section 1.7 and 19.2 (toxicology: a generally reasonable fit with some notable discrepancies). Often the model must be checked before new data arrive, so this chapter and the next discuss methods that can approximate external validation with existing data (p. 142).
- **Choices of predictive quantities.** One model supports different predictions: the same 8 schools $p(\tilde y\mid y)$, 8 new schools $p(\tilde y_i\mid y),\ i=9,\dots,16$, or other combinations. In surveys and designed experiments one may replicate with a new randomization of selection or treatment (p. 143).
- Sections 6.3–6.4 use global summaries to check the joint posterior predictive $p(\tilde y\mid y)$. The end of 6.3 covers checks of marginal $p(\tilde y_i\mid y)$, related to cross-validation (Chapter 7) (p. 143).

### 6.3 Posterior predictive checking (pp. 143–153)
**Idea.** If the model fits, replicated data should look like the observed data. This is a self-consistency check, since an observed discrepancy can be due to misfit or chance. Draw replicated data from the joint posterior predictive and compare; systematic differences indicate potential failings (p. 143).

**Example: Newcomb's speed of light (pp. 143–144).**
- Newcomb's 66 measurements were modeled as $N(\mu,\sigma^2)$ with a noninformative uniform prior on $(\mu,\log\sigma)$ (Section 3.2). The lowest measurements look like outliers (p. 143–144).
- Procedure: draw $(\mu,\sigma^2)$ from the posterior, then 66 values from $N(\mu,\sigma^2)$. Figure 6.2 shows 20 such histograms; all look different from the real data (p. 144).
- Test statistic: the smallest value. Newcomb's smallest is $-44$. In all 20 replications the smallest value is much larger (Figure 6.3). The normal model does not capture Newcomb's variation. A revised model might use an asymmetric contaminated normal or a symmetric long-tailed distribution (p. 144).
- Graphical comparison is often useful. For less blatant discrepancies, the "statistical significance" of lack of fit is formalized next (p. 145).

**Notation (p. 145).** $y$ is observed data; $\theta$ is all parameters (including hyperparameters). $y^{\rm rep}$ is the replicated data that could have been observed: the data we would see tomorrow if the experiment were replicated with the same model and same $\theta$. It differs from $\tilde y$ (any future observable): explanatory variables $x$ are identical for $y$ and $y^{\rm rep}$, but $\tilde y$ may have its own $\tilde x$. The reference distribution is the posterior predictive distribution
$$p(y^{\rm rep}\mid y)=\int p(y^{\rm rep}\mid\theta)\,p(\theta\mid y)\,d\theta. \tag{6.1}$$

**Test quantities (p. 145).** A test quantity (discrepancy measure) $T(y,\theta)$ is a scalar summary of data and parameters used as the standard in comparing data with predictive simulations. It plays the role that test statistics play in classical testing. $T(y)$ denotes a test *statistic*: a test quantity depending on data only. In the Bayesian setting $T$ may also depend on parameters, evaluated over their posterior draws. Calibration-type quantities depending on both $y_i$ and $y_i^{\rm rep}$ (or $\tilde y_i$) come later in the section; Chapter 7 covers predictive-accuracy measures (p. 145).

**Tail-area probabilities (pp. 145–146).**
- *Classical p-value*, for a test statistic $T(y)$, with $\theta$ fixed:
$$p_C=\Pr\big(T(y^{\rm rep})\ge T(y)\mid\theta\big), \tag{6.2}$$
  probability over $y^{\rm rep}$ with $\theta$ fixed. The fixed value may be a 'null' value or a point estimate such as the MLE. A point estimate must be substituted in classical statistics (p. 146).
- *Bayesian (posterior predictive) p-value*:
$$p_B=\Pr\big(T(y^{\rm rep},\theta)\ge T(y,\theta)\mid y\big)=\iint I_{T(y^{\rm rep},\theta)\ge T(y,\theta)}\,p(y^{\rm rep}\mid\theta)\,p(\theta\mid y)\,dy^{\rm rep}\,d\theta,$$
  where the probability is over the joint $p(\theta,y^{\rm rep}\mid y)$, $I$ is the indicator function, and $p(y^{\rm rep}\mid\theta,y)=p(y^{\rm rep}\mid\theta)$ was used (p. 146).
- *Computation:* given $S$ posterior draws $\theta^s$, draw one $y^{\mathrm{rep}\,s}$ from $p(y^{\rm rep}\mid\theta^s)$ for each, giving $S$ draws from $p(y^{\rm rep},\theta\mid y)$. Compare realized $T(y,\theta^s)$ with predictive $T(y^{\mathrm{rep}\,s},\theta^s)$. The estimated p-value is the proportion of $s=1,\dots,S$ with $T(y^{\mathrm{rep}\,s},\theta^s)\ge T(y,\theta^s)$ (p. 146).
- No special handling of nuisance parameters is needed: simulation implicitly averages over all parameters (p. 146).

*Intuition note:* A p-value near 0 (or 1) says that replications rarely (or very often) look more extreme than the real data on the feature you chose. It is a probability conditional on the model and the data.

**Speed of light, continued (pp. 146–147).**
- Sample variance (observed 115.5) against 200 posterior predictive variances (Figure 6.4a, p-value 0.48 in the figure): a poor test statistic, because it is a sufficient statistic of the model. Without an informative prior, the posterior is automatically centered near the observed value, so a p-value near ½ is expected (pp. 146–147).
- To show a model can be inadequate for some purposes and adequate for others, test asymmetry in the centre: $T(y,\theta)=|y_{(61)}-\theta|-|y_{(6)}-\theta|$. The 61st and 6th order statistics approximate the 90% and 10% points; $T$ should scatter about zero for a symmetric distribution. With 200 simulations (Figure 6.4b) the estimated p-value is 0.26, so asymmetry in the middle can easily be explained by sampling variation (pp. 146–147).

**Choosing test quantities (pp. 147–150).**
- One must specify $T(y)$ or $T(y,\theta)$ and the predictive distribution for $y^{\rm rep}$. If $T(y)$ does not appear consistent with $T(y^{\mathrm{rep}\,1}),\dots,T(y^{\mathrm{rep}\,S})$, the model is making predictions that do not fit the data. The authors prefer to look at the magnitude of the discrepancy as well as its p-value (p. 147).
- **Example: independence in binomial trials (pp. 147–148).** Binary $y_1,\dots,y_n$ are modeled as independent trials with common success probability $\theta$ under a uniform prior. Posterior: $p(\theta\mid y)\propto\theta^{\sum y}(1-\theta)^{n-\sum y}$, depending on the data only through $\sum_i y_i$. Observed data ($n=20$): 1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0. The autocorrelation is evidence of flaw. Test quantity: $T$ = number of switches between 0 and 1. Observed $T(y)=3$. Simulation: draw $\theta\sim$ Beta(8,14), then 20 independent Bernoulli($\theta$) values. Figure 6.5 shows $T(y^{\mathrm{rep}\,s})$ for 10,000 draws. The observed switch count is about one-third of what the model expects; the p-value $\Pr(T(y^{\rm rep})\ge T(y)\mid y)$ is $9838/10000$. Changing the sign of the statistic gives $\Pr(T(y^{\rm rep},\theta)\le T(y,\theta)\mid y)=0.028$. The two tail p-values sum to more than 1 because $T(y^{\rm rep})$ is discrete (p. 148).
- If $T$ depends on $\theta$, both $T(y,\theta)$ and $T(y^{\rm rep},\theta)$ are unknowns represented by $S$ simulations. Display a scatterplot of $T(y,\theta^s)$ vs $T(y^{\mathrm{rep}\,s},\theta^s)$ (symmetric about the 45° line under the model) or a histogram of differences $T(y,\theta^s)-T(y^{\mathrm{rep}\,s},\theta^s)$ (should include 0) (p. 148).
- Since a model can fail in many ways, compute p-values for several quantities. Ideally $T$ reflects aspects relevant to the scientific purpose. Common choices measure features the model does not directly address, such as ranks or correlation of residuals with a candidate explanatory variable (p. 148).
- **Example: adolescent smoking (pp. 148–150).** Data: about 2000 Australian adolescents, smoking recorded every six months over three years. Average age at start 14.9 (Figure 6.6). Model 1 is a hierarchical logistic regression, for person $j$ at wave $t$:
$$\Pr(y_{jt}=1)=\mathrm{logit}^{-1}\big(\beta_0+\beta_1X_{j1}+\beta_2X_{j2}+\beta_3(1-X_{j2})t+\beta_4X_{j2}t+\alpha_j\big), \tag{6.3}$$
  with $X_{j1}$ parental smoking, $X_{j2}$ female indicator ($\beta_3,\beta_4$ are the male and female time trends), $\alpha_j\sim N(0,\tau^2)$, and a noninformative uniform prior on $\beta,\tau$ (p. 148). Model 2 adds an unobserved susceptibility $S_j\in\{0,1\}$: $y_{jt}=0$ always if $S_j=0$; for $S_j=1$ model (6.3) applies conditionally on susceptibility; $\Pr(S_j=1)=\mathrm{logit}^{-1}(\gamma_0+\gamma_1X_{j1}+\gamma_2X_{j2})$ with a uniform prior on $\gamma$ (p. 149).

  | Test variable | $T(y)$ | M1 95% int. for $T(y^{\rm rep})$ | M1 p | M2 95% int. | M2 p |
  |---|---|---|---|---|---|
  | % never-smokers | 77.3 | [75.5, 78.2] | 0.27 | [74.8, 79.9] | 0.53 |
  | % always-smokers | 5.1 | [5.0, 6.5] | 0.95 | [3.8, 6.3] | 0.44 |
  | % incident smokers | 8.4 | [5.3, 7.9] | 0.005 | [4.9, 7.8] | 0.004 |

  (Table 6.1, p. 149.) "Incident smokers" began as non-smokers, switched to smoking, and did not switch back. Both models capture never-smokers; Model 2 fits always-smokers better, which makes sense since its mixture separates smokers from non-smokers. Both underpredict incident smokers, suggesting they do not fully fit within-individual variation (pp. 149–150). The goal here is to explore how models might be lacking, not to choose between them (Section 7.3) (p. 150).
- Numerical test quantities can be built from patterns noticed visually, to quantify a pattern or to repeat a check across datasets (p. 150).

**Multiple comparisons (p. 150).** With three test variables, a "multiple comparisons" adjustment would perhaps raise 0.005 to somewhere near 0.015. The authors do not adjust: predictive checks show how aspects of the data would appear in replications. If several quantities are examined, it is no surprise that some are not fitted, but if the model will be applied, those atypical aspects are of interest. They are not concerned with Type I error, since checks are used not to accept or reject but to understand limits of applicability. For several comparisons at once, they prefer to infer them directly with a multilevel model (p. 150).

**Interpreting p-values (pp. 150–151).**
- A model is suspect if a discrepancy is of practical importance and its tail-area probability is near 0 or 1. A p-value is a posterior probability and interpretable directly, but not as $\Pr(\text{model true}\mid\text{data})$ (p. 150).
- Major failures (typically p < 0.01 or > 0.99) can be addressed by expanding the model. Lesser failures may suggest improvements or be ignored short-term if the main inferences are unaffected. In some cases even extreme p-values may be ignored if the misfit is substantively small relative to variation within the model (p. 150).
- Near 0 or 1, exact extremeness matters little: 0.00001 is virtually no stronger than 0.001 in practice. A slight model improvement (or correcting a coding error) could bring either into, say, 0.05–0.95. The p-value measures statistical, not practical, significance (pp. 150–151).
- The goal is not to answer "do the data come from the assumed model?" (almost always no) but to quantify discrepancies and assess whether they could have arisen by chance under the model's own assumptions (p. 151).

**Limitations of posterior tests (p. 151).** Finding an extreme p-value is never the end: the departure often suggests model improvements or data checks. Even when no deviation is found, a more rigorous experiment is often the next step. In the eight-schools data the model "all $\theta_j$ equal" cannot be rejected, but it is clearly unrealistic, so $\tau$ is not restricted to zero. A demonstrably wrong model can still work for some purposes (Section 14.3) (p. 151).

**P-values and u-values (pp. 151–152).**
- Posterior predictive checking generalizes classical testing by averaging over $p(\theta\mid y)$ rather than fixing $\theta$ at $\hat\theta$. It needs neither pivotal quantities nor asymptotics, but the choice of test quantity and predictive distribution still needs care (p. 151).
- If $\theta$ is known (or estimated very precisely), or $T(y)$ is ancillary (depends only on observed data, with distribution independent of parameters) with a continuous distribution, then $\Pr(T(y^{\rm rep})>T(y)\mid y)$ is uniform if the model is true (p-values < 0.1 occur 10% of the time, etc.) (p. 151).
- More generally, when posterior uncertainty in $\theta$ propagates to the distribution of $T(y\mid\theta)$, the p-value under a true model is more concentrated near the middle: more likely near 0.5 than near 0 or 1 ("stochastically less variable" than uniform) (p. 151).
- A **u-value** is any function of $y$ with a U(0,1) sampling distribution. It can be averaged over $\theta$ but is fundamentally not Bayesian, since it need not be a posterior probability. The posterior predictive p-value is a probability statement, conditional on model and data, about future replications (p. 151).
- The authors say the p-value is to the u-value as the posterior interval is to the confidence interval (p. 152). Some have called posterior predictive checks conservative or uncalibrated; **the authors** do not find this labeling helpful and interpret p-values directly as probabilities. A p-value of 0.4 means: if we believe the model, there is a 40% chance that tomorrow's $T(y^{\rm rep})$ exceeds today's $T(y)$. They are as calibrated as other model-based probabilities (loaded dice, Obama/Michigan 2008 examples) (p. 152).

*Intuition note:* "Calibrated" can mean uniform under repeated sampling from the true model (u-value) or a correct probability given the model. The authors interpret p-values in the second way.

**Model checking and the likelihood principle (p. 152).**
- Bayesian posteriors depend on data only through the likelihood. Example: test whether the mean score of 55 students exceeds 80, normal scores, prior on $(\mu,\sigma)$. Four data-collection protocols: (a) fixed sample of 55; (b) sample sequentially, stopping after each student with probability 0.02; (c) sample for a fixed time; (d) sample until the classical t-test shows the mean differs from 80 (p. 152).
- These give different probability models but identical likelihood functions for the data at hand, so $p(\mu,\sigma\mid y)$ is the same, *if the model is assumed true*. For checking, the distribution of $y^{\rm rep}$ changes with the sampling rule. So aspects of the data may fit under one protocol but not another with the same likelihood (p. 152).

**Marginal predictive checks (pp. 152–153).**
- Instead of the joint $y^{\rm rep}$, use each marginal $p(\tilde y_i\mid y)$: $p_i=\Pr(T(y_i^{\rm rep})\le T(y_i)\mid y)$. For scalar continuous $y_i$ with $T(y_i)=y_i$: $p_i=\Pr(y_i^{\rm rep}\le y_i\mid y)$. For ordered discrete data, a 'mid' p-value:
$$p_i=\Pr(y_i^{\rm rep}<y_i\mid y)+\tfrac12\Pr(y_i^{\rm rep}=y_i\mid y).$$
- *Eight schools:* (i) For the 8 existing schools with noninformative or weakly informative population prior, the predictive centre is close to $y_i$ and the $p_i$ tend to concentrate near 0.5; with no pooling they are exactly 0.5. (ii) For new schools $i=9,\dots,16$ compared with the observed $y_i$, the effect of a single $y_i$ is smaller, working through the population distribution, so the $p_i$ have distributions closer to U(0,1) (p. 153).
- *Cross-validation predictive p-values:* $p_i=\Pr(y_i^{\rm rep}\le y_i\mid y_{-i})$. For continuous data they are uniform if the model is calibrated, but need extra computation. In some settings, *mixed predictive checking* (marginal predictions for new individuals with exactly the same predictors $x_i$) can bridge cross-validation and full Bayesian predictive checking. Cross-validation returns in Chapter 7 (p. 153).
- If marginal p-values concentrate near 0 and 1, the data are overdispersed relative to the model; if near 0.5, underdispersed. The *conditional predictive ordinate* $\mathrm{CPO}_i=p(y_i\mid y_{-i})$ is low for unlikely observations, which can give insight for improvement. Chapter 17 covers robustness to outliers (p. 153).

### 6.4 Graphical posterior predictive checks (pp. 153–159)
Basic idea: display the data next to simulated data from the fitted model and look for systematic discrepancies. Three kinds of display: all the data; summaries or parameter inferences; residuals or other discrepancy measures (p. 153).

**Direct data display (pp. 154–155).**
- Figure 6.7: binary data from a psychology experiment, a $15\times23$ array (15 reactions × 23 situations) for each of 6 persons, with reactions, situations and persons ordered by increasing average response. $T(y)$ is the display itself, including the ordering. Seven replications $y^{\rm rep}$ from a fitted logistic regression, ordered the same way, look fuzzy and "random", while the data have strong rectilinear row and column structure the model misses (p. 154).
- One replication would suffice here, but comparing several is safer to see whether patterns could occur by chance. The ordering is crucial: without it (Figure 6.8) the discrepancies are not clear (pp. 154–155).

**Displaying summary statistics or inferences (pp. 155–157).**
- Exploratory-analysis analogy: hierarchical modeling uses batches of parameters for different levels. In checking, replications correspond to new draws of a batch of parameters (p. 155).
- Psychology model (details not given): parameters $\phi_1,\dots,\phi_{90}$ (patients) and $\psi_1,\dots,\psi_{69}$ (symptoms), each independent Beta(2,2) prior, each a probability of association with a syndrome (p. 155).
- Why a single posterior draw should look like prior draws if the model is true (pp. 155–156): (1) If the model were true, $y$ and true $\theta$ are a draw from $p(y,\theta)$, so $y$ comes from the prior predictive $p(y)$. (2) A draw $\theta^s\sim p(\theta\mid y)$ with $y\sim p(y)$ means $(y,\theta^s)$ follow the model's joint distribution, so $\theta^s$ has the same marginal as $\theta$. (3) So $\theta$ and $\theta^s$ have the same marginals (and same joint with $y$). Hence a histogram of one simulated vector $\phi$ or $\psi$ should resemble the prior, equivalent to a posterior predictive check for a new set of patients and symptoms (p. 156).
- Result (Figure 6.9): too many values near zero, contradicting Beta(2,2). The prior was replaced by mixtures with fixed parameters:
$$p(\phi_j)=0.5\,\mathrm{Beta}(\phi_j\mid1,6)+0.5\,\mathrm{Beta}(\phi_j\mid1,1),\qquad p(\psi_j)=0.5\,\mathrm{Beta}(\psi_j\mid1,16)+0.5\,\mathrm{Beta}(\psi_j\mid1,1).$$
  The spiked component handles values near zero; labeling of symptoms is subjective. Beta(2,2) had originally been used so MLEs would lie in the interior of [0,1], a concern that vanished with Bayesian inference (Exercise 4.9) (p. 156).
- **Objection** (some might object to revising the prior after seeing fit): the authors reply it is consistent with common practice of iteratively altering a model. A hierarchical structure with hyperparameters would be the natural next step but brings more computation and possible instability. Refit (Figure 6.10): not perfect but much better (p. 157).

**Residual plots and binned residual plots (pp. 157–158).**
- *Bayesian residuals:* for a regression with $g(x,\theta)=E(y\mid x,\theta)$, the realized residual is $y_i-g(x_i,\theta)$, as opposed to the classical $y_i-g(x_i,\hat\theta)$. A Bayesian residual graph plots one realization based on a single draw of $\theta$. Classical plots approximate it, ignoring posterior uncertainty (p. 157).
- *Discrete data:* residuals take only certain values, so even under a correct model they are not independent of fitted values. Figure 6.11a (pain relief scores) shows stripes (p. 157).
- *Binned residuals:* choose $w=(w_1,\dots,w_n)$ (a function of $x$, $\theta$, perhaps $y$). Order the $w_i$, sort into $K$ bins with about equal counts $n_k$. In each bin compute averages $\bar w_k,\bar r_k$. The plot is $\bar r_k$ vs $\bar w_k$ (several overlaid plots for posterior uncertainty in $\theta$). The reference is plots of $\bar r_k^{\rm rep}$ vs $\bar w_k^{\rm rep}$ with $r_i^{\rm rep}=y_i^{\rm rep}-E(y_i\mid x,\theta)$; bins and $\bar w_k^{\rm rep}$ can vary if $w$ depends on $y$ (pp. 157–158).
- Why bin: averages of residuals (each with expectation zero) are approximately symmetric by the central limit theorem when bins are large. A reference distribution with simple features (independent, approximately normal $\bar r_k$) gives a clear interpretation of misfit. This is why residuals rather than data are plotted vs predicted values: a horizontal line is easier to compare than a 45° line. Replicated data need never be displayed: the replication distribution is implicit, given that binned residuals are independent and approximately normal, and is shown as 95% error bounds (p. 158).
- Figure 6.11b (20 bins): average errors are small but with a consistent pattern, low predictions too low and high predictions too high (p. 158).

**General interpretation (pp. 158–159).** Any data display can be compared with replications to see what it "should" look like under the model. Strong patterns in the cancer-rate maps (Figs 2.6–2.8) are uninformative if replications under the model would show the same. The erroneous reading of Figure 2.6 was an erroneous model check, comparing the display with a random pattern instead of one expected under a reasonable variation model (p. 159).

### 6.5 Model checking for the educational testing example (pp. 159–161)
**Assumptions (p. 159).** (1) Normality of $y_j\mid\theta_j,\sigma_j$ with known $\sigma_j$; (2) exchangeability of the $\theta_j$; (3) normality of $\theta_j\mid\mu,\tau$; (4) uniform hyperprior on $(\mu,\tau)$.
- Assumption 1 is routine when a study is summarized by an effect and standard error; design and analysis make it seem justifiable (p. 159).
- Exchangeability means no prior wish to say school A's effect is probably larger than B's, or that A and B are more similar than A and C. The data are left to inform ordering and similarity. Known information (e.g. B and C having similar students) could suggest a nonexchangeable prior. In the absence of such information the $\theta_j$ are independent samples from a population indexed by hyperparameters $(\mu,\tau)$ (p. 159).
- Assumptions 3 and 4 are harder to justify a priori (why normal rather than Cauchy or asymmetric; why uniform on location and scale). Tractability is one reason, but if the family is inappropriate, Bayesian answers can mislead (p. 159).

**Posterior inferences vs substantive knowledge (p. 160).** Posterior mean effects range from 5 to 10 points (test scores range 200–800), plausible. School A's 95% posterior interval is −2 to 31 points. Both extremes seem plausible, so estimates do not violate common sense or the limited substantive knowledge (p. 160).

**Predicted values (p. 160).** From each of 200 posterior draws of $(\theta,\mu,\tau)$, draw $y_j^{\rm rep}\sim N(\theta_j,\sigma_j^2)$, $j=1,\dots,8$. The $\theta_j$ values are plausible, and simulated $y_j^{\rm rep}$ range from −48 to 63, also judged plausible (p. 160).

**Posterior predictive checking (pp. 160–161).** If all 200 simulated maxima $\max_j y_j^{\rm rep}$ were below the observed 28, the model would not fit that aspect and the normal-based inference might shrink school A too far. The four test statistics are $\max_j y_j$, $\min_j y_j$, mean$(y_j)$, sd$(y_j)$. Figure 6.12 gives p-values 0.54 (max), 0.19 (min), 0.50 (mean), 0.78 (sd). Observed outcomes are typical of the model's predictions. Other quantities (e.g. skewness against a particular skewed prior) could be used; useful displays often come from intuitive quantities without a specific alternative model (p. 160, Fig. p. 161).

**Sensitivity analysis (p. 161).** Good fit alone does not give complete confidence, since other reasonable models may fit as well but lead to different conclusions.
- *Uniform prior on $\tau$:* the posterior under another prior is obtained by multiplying the density of Figure 5.5 by that prior. There will be little change as long as the prior is not sharply peaked and does not put a great deal of mass on $\tau>10$.
- *Normal population distribution:* made for convenience. A natural check is a longer-tailed alternative such as $t$ (deferred to Section 17.4). Alternatives must keep predictive distributions to realistic SAT improvements.
- *Normal likelihood:* justified by the central limit theorem and study designs; the authors say it need not and cannot be seriously challenged here. Assessing it would need the original data, not just the estimates and standard errors of Table 5.2 (p. 161).

### 6.6 Bibliographic note (pp. 161–162)
The posterior predictive approach was presented in Rubin (1981a, 1984); test quantities that depend on parameters are discussed by Gelman, Meng and Stern (1996). The smoking example appears in Carlin et al. (2001). Bush and Mosteller (1955) is cited as an early simulation check with parameters fixed at point estimates. Box (1980, 1983) proposed comparing data to the *prior* predictive distribution $p(y^{\rm rep})=\int p(y^{\rm rep}\mid\theta)p(\theta)d\theta$. With an improper prior on $\theta$ this is itself improper and the check is not generally defined, even if the posterior is proper (Exercise 6.7). The note says many common checks (outlier tests, residual plots, normal plots) can be read as posterior predictive checks (p. 162).

### 6.7 Exercises (pp. 163–164)
Listed below under "Exercises worth doing".

## Toy example (ours, not from the text)
Observed binary sequence, $n=6$: $y=1,1,1,0,0,0$. Model: independent Bernoulli($\theta$), uniform prior. Test quantity: $T$ = number of switches, observed $T(y)=1$. Is such a clean "runs" pattern surprising?

1. Posterior: 3 ones, 3 zeros, so Beta(4,4); $B(4,4)=\frac{3!\,3!}{7!}=\frac1{140}$.
2. Posterior predictive probability of one specific sequence with $k$ ones: $140\cdot B(4+k,10-k)=140\cdot\frac{(3+k)!(9-k)!}{13!}$. Since $13!/140=44{,}478{,}720$, the probability is $N_k/44{,}478{,}720$ with $N_k=(3+k)!(9-k)!$:
   $N_0=N_6=2{,}177{,}280$; $N_1=N_5=967{,}680$; $N_2=N_4=604{,}800$; $N_3=518{,}400$.
3. Check: $\sum_k\binom6kN_k=44{,}478{,}720$, so the probabilities sum to 1.
4. Low switch counts are the discrepancy of interest, so the p-value is $\Pr(T(y^{\rm rep})\le1\mid y)$. Sequences with $T\le1$: all-0, all-1 ($k=0,6$), plus one-switch sequences $0^{6-k}1^k$ and $1^k0^{6-k}$ for $k=1,\dots,5$ (two each).
5. Sum: $2N_0=4{,}354{,}560$; $2(N_1+N_2+N_3+N_4+N_5)=2(3{,}663{,}360)=7{,}326{,}720$. Total $11{,}681{,}280$.
6. $p=11{,}681{,}280/44{,}478{,}720\approx0.263$.

Reading: not extreme, so with only 6 points the check does not flag the clustering; the text's 20-point sequence had $T=3$ and a one-tail p-value of 0.028. The example also shows the check is exactly a probability computed in the model. In practice the sum is done by simulation, as in the text.

## Concepts
- [[posterior-predictive-check]] — compare observed data/test quantity with replications drawn from $p(y^{\rm rep}\mid y)$ (p. 143)
- [[posterior-predictive-distribution]] — $p(y^{\rm rep}\mid y)=\int p(y^{\rm rep}\mid\theta)p(\theta\mid y)d\theta$, eq. (6.1) (p. 145)
- [[test-quantity]] (new) — scalar discrepancy $T(y,\theta)$; a "test statistic" $T(y)$ if it depends on data only (p. 145)
- [[posterior-predictive-p-value]] (new) — $\Pr(T(y^{\rm rep},\theta)\ge T(y,\theta)\mid y)$, a posterior probability, not $\Pr$(model true) (p. 146, 150)
- [[u-value]] (new) — any function of data with U(0,1) sampling distribution; not necessarily a posterior probability (p. 151)
- [[sensitivity-analysis]] (new) — how much posterior inferences change under other reasonable models (p. 141)
- [[external-validation]] (new) — predict future data, then compare with them (p. 142)
- [[likelihood-principle]] (new) — inference depends on data only via likelihood; checking nevertheless depends on the sampling rule (p. 152)
- [[marginal-predictive-check]] (new) — p-values per observation from $p(\tilde y_i\mid y)$; includes mid p-value, cross-validation and mixed variants, CPO (pp. 152–153)
- [[binned-residual-plot]] (new) — averaged residuals in bins plotted against predictors, with 95% bounds as the reference (p. 158)
- [[exchangeability]] — here, a prior stance that the $\theta_j$ are symmetric and the data decide ordering and similarity (p. 159)
- [[prior-predictive-check]] — Box's alternative with $p(y^{\rm rep})=\int p(y^{\rm rep}\mid\theta)p(\theta)d\theta$, mentioned in the bibliographic note (p. 162)
- [[cross-validation-loo-waic]] — only touched here via cross-validation predictive p-values (p. 153)
- [[hierarchical-model]] — batches of parameters compared with their prior as a check (p. 155)

## Canonical instances
- [[newcomb-speed-of-light]] — normal model fails on the min (−44), variance check a poor test statistic, asymmetry check consistent with the model (pp. 143–147)
- [[binomial-switches-check]] — switch count detects dependence in 20 binary trials; Beta(8,14) posterior (pp. 147–148)
- [[adolescent-smoking-models]] — Table 6.1 compares two hierarchical models on three statistics (pp. 148–150)
- [[psychology-binary-array-display]] — ordered direct display reveals misfit of logistic regression (pp. 154–155)
- [[psychometric-beta-prior-check]] — Beta(2,2) prior contradicted by posterior draws; mixtures adopted (pp. 155–157)
- [[eight-schools]] — model checks and sensitivity analysis of the SAT coaching model (pp. 159–161)
- [[election-forecast-1992]] — a forecast judged against state-level knowledge (p. 142)

## Bridges (candidates)
- [structural-analogy] Posterior predictive p-value ↔ frequentist p-value: both compare a statistic with replications; the Bayesian one averages over $p(\theta\mid y)$ rather than fixing $\theta$.
- [structural-analogy] Posterior predictive check ↔ simulation-based fake-data checking (Bayesian workflow): simulate from the fitted model and look for discrepancies.
- [metaphor] Binned residuals with 95% bounds ↔ calibration plots in forecasting: averaged errors judged against expected variation.
- [structural-analogy] Marginal/cross-validation predictive p-values ↔ leave-one-out predictive checks (Chapter 7): same conditional predictive idea.

## Questions this raises
- How should one choose test quantities so that they have power against the failures that matter, without relying on the data to pick them?
- When the posterior predictive p-value is not uniform under a true model, how can one reason about its false-alarm rate for repeated checks?
- How do prior predictive checks (Box) and posterior predictive checks differ when the prior is diffuse or improper (Exercise 6.7)?
- How should one pick the replication reference set (fixed $\theta$, fixed hyperparameters, new groups)?

## Exercises worth doing
- Ex. 1 (p. 163) — formal posterior predictive check of the identical-schools model with order statistics; why it fits yet is unacceptable for some purposes — difficulty: medium
- Ex. 2 (p. 163) — posterior predictive checks of independence and trend for four Poisson models of airline fatalities — difficulty: medium
- Ex. 6 (p. 163) — change the sampling protocol (stop after 13 zeros): posterior unchanged but replications differ — difficulty: medium
- Ex. 7 (p. 164) — prior vs posterior predictive check of $\max_i|y_i|$ under a diffuse prior — difficulty: hard
- Ex. 8 (p. 164) — alternative reference set (fix $(\mu,\tau)$, vary $\theta$) for the eight-schools checks — difficulty: hard
- Ex. 10 (p. 164) — graphical and numerical check of equal variance in football point-spread data — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 151 = printed 141).
- The text layer renders $\theta$ as "ω", minus as "→" (e.g. "logit→1", "y→i") and some integrals as "!"/"#". The page images show $\theta$, $-$ and $\int$; the digest follows the images.
- p. 153: the second bullet reads "$y_i, y_i=1,\dots,8$" in the image, apparently a misprint for $i=1,\dots,8$.
- Figure 6.11 caption (p. 158) says scores run from 0 (no pain relief) to 5 (complete pain relief), but the text (p. 157) says scores were reported as 0, 1, 2, 3, or 4.
- Figure 6.4b caption (p. 147) says the simulations are of both prior and posterior, but the text describes simulations from the posterior.
- The p-value 0.48 for the variance check appears only in the figure image (Figure 6.4a), the text says only "close to ½".
- Section references to other chapters (e.g. Sections 14.3, 15.2, 17.4) point to material outside these pages and are not digested here.
- Header on every page: "This electronic edition is for non-commercial purposes only."
- No exercise solutions appear on these pages.

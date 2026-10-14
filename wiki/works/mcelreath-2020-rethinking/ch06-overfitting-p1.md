---
id: mcelreath-2020-rethinking/ch06-overfitting-p1
work: mcelreath-2020-rethinking
unit: "Chapter 6. Overfitting, Regularization, and Information Criteria (part 1/2: introduction, 6.1 and 6.2)"
pages: 165-185
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Overfitting and the problem with parameters: from entropy to out-of-sample deviance

## L0 — One line
The chapter's target for a model is predictive accuracy on new data, measured as out-of-sample deviance (an approximation of relative K-L divergence), because fit to the sample improves as parameters are added (always, in the models seen so far).

## L1 — The gist (≤ 120 words)
Adding parameters always improves fit to the sample (in the models seen so far), but often worsens prediction of new data. Too few parameters also tend to predict badly. The chapter asks how to choose a target for "good prediction". The answer built here: use joint probability (likelihood), measure the distance between a model and the truth with K-L divergence (from information entropy), approximate it by deviance, and care only about deviance on new data. A simulation shows training deviance always falls with more parameters, while test deviance does not keep falling (on average it is smallest at the true model's 3 parameters). This sets up regularizing priors and information criteria.

**Prerequisites:** logarithms; expectation as an average; likelihood as a product of per-case probabilities; linear and polynomial regression; R².

## L2 — Key ideas
- Ockham's razor gives no guidance when models differ in both accuracy and simplicity. Regularizing priors and information criteria trade the two off explicitly, aiming at predictive accuracy (p. 165–166).
- Overfitting means learning too much from the sample; underfitting means learning too little. Both predict badly (p. 166, 168).
- In the models so far, more parameters always improve in-sample fit. A 7-parameter polynomial fits 7 hominin species perfectly, with R² = 1, yet makes absurd predictions (p. 168–172).
- Overfit models are over-sensitive to the sample; underfit models are insensitive to it (p. 173).
- A target must be defined. Joint probability (likelihood), not hit rate, is the right accuracy measure (p. 174–176).
- Information entropy $H(p)=-\sum p_i\log p_i$ measures uncertainty. K-L divergence measures the extra uncertainty from using $q$ for $p$. It is asymmetric (p. 177–181).
- Comparing models needs only average log-probability, because the unknown truth cancels. Deviance $D(q)=-2\sum\log q_i$ approximates this (p. 181–182).
- Simulation: training deviance always improves with parameters, but test deviance is best near the true model. The true model is not guaranteed to predict best (p. 183–185).

## L3 — Walkthrough

### Opening: Copernicus and the razor (p. 165–167)
- Copernicus preferred the heliocentric model as more "harmonious" and as needing fewer causes. The author says it was not more accurate. It still needed epicycles (circles on circles), since orbits were perfect circles. It made the same predictions as the geocentric model (p. 165).
- Ockham's razor ("fewer assumptions are preferred") gives a clear answer here, because the predictions are equal. Usually models differ in both accuracy and simplicity, and the razor offers no guidance on trading these off (p. 165).
- The chapter's tools each trade off accuracy and simplicity explicitly, so they are "not like the razor" (p. 165).
- **Ulysses' compass.** Two monsters are two errors. **Overfitting** is poor prediction from learning too much from the data. **Underfitting** is poor prediction from learning too little (p. 166).
- Two families of approaches, which can be (maybe should be) combined (p. 166):
  1. A **regularizing prior**, which tells the model not to get too excited by the data. Non-Bayesian methods call this "penalized likelihood".
  2. A scoring device such as **information criteria** (AIC, DIC, WAIC), which estimates predictive accuracy. These need information theory first.
- *Rethinking: Stargazing.* Choosing the model whose coefficients are all significant is, the author says, a mistake for choosing among structurally different models. P-values are not designed to navigate between under- and overfitting. Variables that improve prediction are not always significant, and significant variables can do nothing useful for prediction (p. 167).
- *Rethinking: Is AIC Bayesian?* AIC uses MAP estimates and requires flat priors. DIC and WAIC give almost exactly the same results as AIC when AIC's assumptions are met. So the author says AIC can fairly be regarded as a special limit of a Bayesian criterion such as WAIC (p. 167).

### 6.1 The problem with parameters (p. 167–174)
Two concerns with simply adding variables (p. 167–168):
1. More parameters nearly always improve **fit**, meaning retrodiction of the data used to fit the model.
2. More complex models often predict new data worse. Too-simple models underfit, over- or under-predicting systematically.

$$R^2=\frac{\mathrm{var(outcome)}-\mathrm{var(residuals)}}{\mathrm{var(outcome)}}=1-\frac{\mathrm{var(residuals)}}{\mathrm{var(outcome)}}$$

$R^2$ increases as predictors are added, even random-number predictors. So fit to the sample alone is no good for choosing models (p. 168).

**6.1.1 More parameters always improve fit (p. 168–172).**
- Samples have regular features (which generalize) and irregular ones (which mislead). Overfitting is learning the irregular ones. In the models seen so far, an added parameter always improves in-sample fit. Models in Chapter 12 onward are different (p. 168).
- Data: mean brain volume (cc) and body mass (kg) for 7 hominin species (p. 168–169):

| species | afarensis | africanus | habilis | boisei | rudolfensis | ergaster | sapiens |
|---|---|---|---|---|---|---|---|
| brain (cc) | 438 | 452 | 612 | 521 | 752 | 871 | 1350 |
| mass (kg) | 37.0 | 35.5 | 34.5 | 41.5 | 55.5 | 61.0 | 53.5 |

- The author stresses that polynomials are common but usually a bad idea, and this example shows it. The lesson holds even after log transforms (p. 169).
- Models are fitted with `lm`, so priors are flat. $m6.1$ is linear:

$$v_i\sim\mathrm{Normal}(\mu_i,\sigma),\qquad \mu_i=\alpha+\beta_1 m_i$$

  Its $R^2$ is 0.490158 (p. 169–170).
- Models $m6.2$ to $m6.6$ are polynomials of degree 2 to 6. Degree 2 is $\mu_i=\alpha+\beta_1m_i+\beta_2m_i^2$ (p. 170).
- Figure 6.3: $R^2$ = 0.49, 0.54, 0.68, 0.81, 0.99 and 1.00 for degrees 1–6. The degree-6 model passes through every point, with no residual variance (p. 170–171).
- Higher-degree curves look increasingly absurd. There are no fossils with body mass between 55 kg and about 60 kg. In that gap the models "pay no price" for wild swings, and $m6.6$ predicts negative brain size at about 58 kg (p. 170, 172).
- Why perfect? The model has 7 parameters ($\alpha,\beta_1,\dots,\beta_6$) for 7 species. If you adopt a model family with enough parameters, you can fit the data exactly, but such a model will make rather absurd predictions for yet-to-be-observed cases (p. 172).
- *Rethinking: compression.* Model fitting is lossy data compression. A model with one parameter per datum achieves no compression, so we learn nothing. This view is called Minimum Description Length (MDL) (p. 172).

> **Intuition note:** In-sample fit rewards memorizing. A model with as many parameters as data points can fit the data exactly (as the degree-6 polynomial does for 7 species), yet predict absurdly. Fit to the sample alone is therefore no good for choosing models.

**6.1.2 Too few parameters hurts, too (p. 172–174).**
- Underfit models are inaccurate both within and out of sample. They fail to recover regular features (p. 172).
- $m6.7$ has only an intercept: $v_i\sim\mathrm{Normal}(\mu,\sigma)$, $\mu=\alpha$. It gives a horizontal line with $R^2=0$ and a broad interval, and "presumably" predicts badly (Figure 6.4, p. 172–173).
- Sensitivity: drop each row in turn and refit (seven datasets). Straight lines hardly vary (Fig. 6.5a). The curves in Fig. 6.5b are fifth-order polynomials and "fly about wildly". The author's general contrast: underfit models are insensitive to the sample, overfit ones over-sensitive (p. 173).
- The Overthinking box shows `d[ -i , ]` for dropping row $i$ (p. 174).
- *Rethinking: bias and variance.* The author describes bias–variance as "not exactly the same" distinction, with bias related to underfitting and variance to overfitting. The book prefers the under/overfitting terms (p. 174).

### 6.2 Information theory and model performance (p. 174–185)
Roadmap (p. 174): (a) joint probability is the right accuracy measure; (b) information theory gives a distance scale between distributions; (c) deviance approximates relative distance from the target; (d) only out-of-sample deviance matters. The first step is to choose the **target**, the criterion of performance.

**6.2.1 Firing the weatherperson (p. 174–177).** A target has two dimensions: cost–benefit, and accuracy in context (some tasks are inherently easier) (p. 175).
- Setup (10 days). The current weatherperson forecasts rain probability 1, 1, 1 on days 1–3, when it rains, and 0.6 on days 4–10, when it is sunny. The newcomer always forecasts 0 (always sun) (p. 175).
- **Hit rate** is the average chance of a correct prediction. Current: $3\times1+7\times0.4=5.8$, so 0.58 per day. Newcomer: $3\times0+7\times1=7$, so 0.7. The newcomer wins on hit rate (p. 175).
- *6.2.1.1 Costs and benefits.* Getting wet costs −5, carrying an umbrella −1, and the chance of carrying an umbrella equals the forecast probability. Current: $3\times(-1)+7\times(-0.6)=-7.2$. Newcomer: $-15$. The newcomer now looks foolish (p. 175–176).
- *6.2.1.2 Measuring accuracy.* Even ignoring costs, hit rate is not special. The **joint probability** of the observed sequence is the product of per-day probabilities of the observed outcome. This is the joint likelihood used in Bayes' theorem (p. 176).
  - Current: $1^3\times0.4^7\approx0.005$ as printed. Newcomer: $0^3\times1^7=0$ (p. 176). (Check: $0.4^7=0.0016384$; see Reading notes.)
- The author says joint probability is the measure we want. It is the likelihood in Bayes' theorem and counts the relative number of ways each sequence could happen. Maximizing average probability would not identify the right model; maximizing joint probability would (p. 176).
- A measure of distance from the target must reflect that some targets are harder. Adding snow gives three ways to be wrong instead of two. The archery analogy adds a third dimension (time) to hit (p. 176).
- *Rethinking: true model.* "True" probabilities are the right probabilities given our state of ignorance. The probability is in the model, not the world. With all relevant information outcomes would be 0/1. In the globe toss, 70% water is the right answer to the question the model poses (p. 176–177).

**6.2.2 Information and uncertainty (p. 177–179).**
- **Information:** the reduction in uncertainty derived from learning an outcome (p. 177).
- Three desiderata for an uncertainty measure (p. 177–178):
  1. Continuous.
  2. Increases with the number of possible events (rain/shine vs rain/shine/hail, each 1/3).
  3. Additive. Uncertainty over combinations (rain/hot etc.) equals the sum of the separate uncertainties.
- The author states that only one function satisfies these, **information entropy**. With $n$ events of probabilities $p_i$:

$$H(p)=-\mathrm{E}\log(p_i)=-\sum_{i=1}^{n}p_i\log(p_i)\tag{6.1}$$

  In words, uncertainty is the average log-probability of an event (with sign flipped). The derivation is not given. We accept $H$ because it has proved useful, not because of the premises (p. 178).
- Examples (p. 178):
  - $p=(0.3,0.7)$: $H\approx0.61$ (R gives 0.6108643).
  - Abu Dhabi, $p=(0.01,0.99)$: $H\approx0.06$. Rain is rare, so less uncertainty.
  - Sun, rain, snow $=(0.7,0.15,0.15)$: $H\approx0.82$. Adding an event type tends to raise entropy.
- *Overthinking:* the $-1$ only makes $H$ increase from zero ("conventional, but not functional"). Logs are natural, and the base does not matter if used consistently. For $p_i=0$, $\lim_{p_i\to0}p_i\log p_i=0$ (L'Hôpital), so $0\log0=0$ (p. 178–179).
- *Rethinking: maximum entropy (maxent)* finds the least surprising distribution consistent with what we know, by maximizing entropy under constraints. It returns in Chapter 9 for GLMs (p. 179).

> **Intuition note:** Entropy is the average "surprise" built into a distribution. A rarely-rainy place is predictable, so its entropy is low. Adding possible outcomes tends to raise entropy.

**6.2.3 From entropy to accuracy (p. 179–181).**
- **Divergence:** the additional uncertainty induced by using probabilities from one distribution to describe another. This is the Kullback–Leibler (K-L) divergence (p. 179).

$$D_{KL}(p,q)=\sum_i p_i\big(\log(p_i)-\log(q_i)\big)=\sum_i p_i\log\!\Big(\frac{p_i}{q_i}\Big)$$

  It is the average difference in log-probability between target $p$ and model $q$ (p. 179).
- If $p=q$, then $D_{KL}(p,p)=\sum_i p_i(\log p_i-\log p_i)=0$ (p. 179).
- Figure 6.6: with $p=(0.3,0.7)$ and $q_1$ ranging from 0.01 to 0.99, divergence is zero only at $q_1=0.3$ and grows elsewhere. Of candidate approximations, the one with the smallest divergence is the closest to the target (p. 179–180).
- *Overthinking: cross entropy.* $H(p,q)=-\sum_i p_i\log(q_i)$. Then (p. 180):

$$D_{KL}(p,q)=H(p,q)-H(p)=-\sum_i p_i\log q_i-\Big(-\sum_i p_i\log p_i\Big)=-\sum_i p_i\big(\log q_i-\log p_i\big)$$

  In general $H(p,q)\neq H(q,p)$ (p. 180).
- *Rethinking: direction.* Mars has 1% surface water ($p=(0.01,0.99)$) and Earth has $q=(0.7,0.3)$ (water, land). Using Earth to predict Mars: $D_{E\to M}=D_{KL}(p,q)=1.14$. Swapping roles: $D_{M\to E}=D_{KL}(q,p)=2.62$. The author calls this a feature, not a bug. Predicting from Mars, we would be very surprised to land in water on Earth. Predicting from Earth, we expect both water and land. Practical consequence: using a high-entropy distribution to approximate an unknown truth reduces distance to the truth (p. 180–181).

> **Intuition note:** K-L divergence is "how surprised you are, on average, when reality follows $p$ but you expected $q$". Surprise is not symmetric. A distribution that gave an event very little probability is punished heavily when it happens (as in the Mars-to-Earth example).

**6.2.4 From divergence to deviance (p. 181–183).**
- Two aims: (1) measure distance from the target (K-L divergence, done); (2) estimate it (p. 181).
- $p$ is usually unknown. But when comparing candidates $q$ and $r$, the $\mathrm{E}\log(p_i)$ term appears in both divergences and subtracts out. So we can tell which is closer, and by how much, without knowing $p$. Only $\mathrm{E}\log(q_i)$ and $\mathrm{E}\log(r_i)$ are needed (p. 181).
- Summing the log-probabilities of the observed cases approximates $\mathrm{E}\log(q_i)$, because "nature takes care of presenting the events" (p. 181–182).
- Absolute values of $\mathrm{E}\log(q_i)$ are not interpretable. Only the difference $\mathrm{E}\log(q_i)-\mathrm{E}\log(r_i)$ tells us about relative divergence (p. 182).
- **Deviance**, where $q_i$ is the likelihood of case $i$:

$$D(q)=-2\sum_i\log(q_i)$$

  The $-2$ is for historical reasons. It is a sum, not an average, so it scales with sample size (p. 182).
- Computation: plug MAP estimates into the likelihood for each row, add the log-probabilities, multiply by $-2$. `logLik` gives the sum of log-probabilities. For `m6.1`, $(-2)\times\mathrm{logLik}$ is 94.92499 (df = 3) (p. 182).
- Because parameters are uncertain, deviance has a posterior distribution. For specific parameter values it is exactly defined (p. 182).
- The Overthinking box refits with `map` on standardized mass (`m6.8`) and computes the deviance by hand as 94.92704, which the author says matches $-2\,\mathrm{logLik}(m6.8)$ (p. 182–183).

**6.2.5 From deviance to out-of-sample (p. 183–185).**
- In-sample deviance has the same flaw as $R^2$: it always improves with complexity, for the models considered so far. It measures retrodiction, not prediction. What matters is deviance on new data (p. 183).
- Thought experiment (p. 183):
  1. Training sample of size $N$.
  2. Fit the model and compute $D_{\mathrm{train}}$.
  3. Draw a test sample of size $N$ from the same process.
  4. Compute $D_{\mathrm{test}}$ using the MAP estimates from step 2.
- Simulation: 10,000 repetitions for each of five linear regressions with 1 to 5 free parameters. The data-generating model is (p. 183–184):

$$y_i\sim\mathrm{Normal}(\mu_i,1),\qquad \mu_i=(0.15)x_{1,i}-(0.4)x_{2,i}$$

  This has $\alpha=0$, $\beta_1=0.15$, $\beta_2=-0.4$. The first model has 1 free parameter (unknown mean, $\sigma=1$ fixed), and each further parameter adds a predictor with its coefficient. The "true" model has 3 parameters (p. 184).
- Figure 6.7 ($N=20$ and $N=100$; `sim.train.test` in the rethinking package): training deviance falls on average with each added parameter. Test deviance is smallest on average at 3 parameters, the data-generating model, and gets worse with each parameter after the third. The extra parameters "fit the noise" (p. 184–185).
- Caveats from the author (p. 185):
  - Individual train/test pairs can reverse the average pattern (SD bars are large), because a training sample may mislead and a test sample may be unrepresentative.
  - The true model need not have the smallest average out-of-sample deviance. At $N=20$ the 2-parameter model does worse than the 1-parameter model, because the first predictor's estimate is too imprecise. At $N=100$ the 2-parameter model is better.
  - Deviance assesses predictive accuracy, not truth. A false model is not guaranteed to predict poorly.
- Conclusion: training deviance always improves with added predictors. Future-data deviance may or may not, depending on the true process and on how much data there is. This is the basis for regularizing priors and information criteria (p. 185).
- Overthinking code: `sapply` over `kseq <- 1:5`, with `replicate(1e4, sim.train.test(N=N, k=k))`, returning means and SDs. `dev` is a 4-by-5 matrix. The plotting code (R code 6.14) begins at the end of this part (p. 185).

> **Intuition note:** Training and test deviance tell different stories because the extra parameters fit the noise in the additional predictors. Training deviance keeps improving, but test deviance gets worse on average after the third parameter. On future data, deviance may or may not improve, depending on the true data-generating process and on how much data there is.

## Toy example (ours, not from the text)
Gaussian model with fixed $\sigma=1$. For one case, $-2\log\mathrm{Normal}(y\mid\mu,1)=\log(2\pi)+(y-\mu)^2$, with $\log(2\pi)\approx1.838$. So for $N=2$, $D=2(1.838)+\mathrm{SSR}=3.676+\mathrm{SSR}$, where SSR is the sum of squared errors.

Both models use the same data. Model A has one shared mean (1 parameter). Model B has a separate mean for each case (2 parameters, so it "memorizes"). Training data: $y=(1,3)$.
- A: $\hat\mu=2$, SSR $=(1-2)^2+(3-2)^2=2$, so $D_{\mathrm{train}}=5.676$.
- B: $\hat\mu=(1,3)$, SSR $=0$, so $D_{\mathrm{train}}=3.676$. B looks better in sample.

Suppose the true mean is 2 and the test sample is $y'=(3,1)$, paired with the same cases.
- A: SSR $=(3-2)^2+(1-2)^2=2$, so $D_{\mathrm{test}}=5.676$.
- B: SSR $=(3-1)^2+(1-3)^2=8$, so $D_{\mathrm{test}}=11.676$.

The more complex model wins in sample and loses out of sample. This is one contrived draw. As the text warns, single train/test pairs can reverse the average pattern (p. 185).

## Concepts
- [[overfitting]] (new) — learning too much from the sample, including irregular features; poor prediction (p. 166, 168)
- [[underfitting]] (new) — learning too little; inaccurate within and out of sample (p. 166, 172)
- [[regularizing-prior]] (new) — prior telling the model not to get too excited by data; "penalized likelihood" elsewhere (p. 166)
- [[information-criteria]] (new) — scoring devices (AIC, DIC, WAIC) estimating predictive accuracy; described later in the chapter (p. 166)
- [[r-squared]] (new) — fit measure $1-\mathrm{var(resid)}/\mathrm{var(outcome)}$; always rises with predictors (p. 168)
- [[likelihood]] — here, the joint probability of the observed data; the right accuracy measure (p. 176)
- [[information-entropy]] (new) — $H(p)=-\sum p_i\log p_i$; uncertainty in a distribution (p. 178)
- [[kl-divergence]] — extra uncertainty from using $q$ to describe $p$; $\sum p_i\log(p_i/q_i)$; asymmetric (p. 179)
- [[cross-entropy]] (new) — $H(p,q)=-\sum p_i\log q_i$; $D_{KL}=H(p,q)-H(p)$ (p. 180)
- [[deviance]] (new) — $-2\sum\log q_i$; approximates relative K-L distance; a sum, not an average (p. 182)
- [[out-of-sample-deviance]] (new) — deviance on a test sample using training estimates; the chapter's target (p. 183)
- [[principle-of-indifference-maximum-entropy]] — maxent: least surprising distribution given constraints; only previewed here (p. 179)
- [[bias-variance-tradeoff]] (new) — alternative name for the under/overfitting tension; "not exactly the same" (p. 174)

## Canonical instances
- [[hominin-brain-polynomials]] — 7 species, polynomials of degree 1–6; $R^2$ rises to 1 and predictions become absurd (p. 168–172)
- [[drop-one-row-sensitivity]] — refitting without each row shows over-sensitivity of complex models (p. 173)
- [[weatherperson-example]] — hit rate vs cost vs joint probability as accuracy targets (p. 175–176)
- [[earth-mars-divergence]] — $D_{KL}$ is asymmetric: 1.14 vs 2.62 (p. 180–181)
- [[train-test-deviance-simulation]] — in- vs out-of-sample deviance for 1–5 parameters at $N=20$ and $N=100$ (p. 183–185)
- [[copernicus-ptolemy-epicycles]] — razor example where predictions are equal (p. 165)

## Bridges (candidates)
- [same-math] deviance $-2\sum\log q_i$ ↔ classical likelihood-based statistics: $-2\times$ the log-likelihood.
- [same-math] entropy $-\sum p_i\log p_i$ and $D_{KL}$ ↔ information theory/machine learning: entropy and cross-entropy loss.
- [structural-analogy] train/test deviance simulation ↔ cross-validation: estimating out-of-sample error from held-out data.
- [structural-analogy] drop-one-row refits ↔ leave-one-out/jackknife: sensitivity to the sample.
- [structural-analogy] overfitting/underfitting ↔ machine learning: variance vs bias.
- [metaphor] Ulysses' compass ↔ Occam's razor: steering between two errors vs cutting away assumptions.

## Questions this raises
- Regularizing priors are said to reduce overfitting. How strong should the prior be, and how does that relate to the number of parameters?
- Deviance on new data cannot be computed for a real sample. How will information criteria estimate it from training data alone?
- If the true model need not predict best, when should we prefer prediction over truth, for example in causal questions?
- Is the asymmetry of K-L divergence a problem when we pick which distribution plays "truth"?

## Reading notes
- Part 1 starts at the chapter opening (printed p. 165) and ends at printed p. 185, mid-way through the Overthinking box on simulated training and testing (code 6.14 continues on the next page). Section 6.2.5 is the last section here. The source notes say the split is at a section boundary; on these pages the part ends inside the Overthinking box of 6.2.5.
- Page offset: printed = pdf − 14.
- Calculation check: the text gives $1^3\times0.4^7\approx0.005$ (p. 176). Direct computation gives $0.4^7=0.0016384$, so "0.005" appears to be a misprint. The comparison with 0 is unaffected.
- The Figure 6.2 caption says "six hominin species". The text (p. 168), the data code (p. 169) and the labels in the figure show seven.
- Fig. 6.5b is described as fifth-order polynomials (p. 173). The surrounding text speaks of $m6.6$ (degree 6). I report this as printed.
- Deviance for `m6.1` (lm) is 94.92499 and for `m6.8` (map, Nelder–Mead) is 94.92704. The text says the hand computation (94.92704) equals $-2\,\mathrm{logLik}(m6.8)$ (p. 183); it does not compare it with `m6.1`. The two values are close but not identical (different fitting routines).
- Code on these pages uses `map` and `lm`. No exercises appear on these pages.
- Figure 6.7 means are only readable approximately from the image, so I did not quote them.

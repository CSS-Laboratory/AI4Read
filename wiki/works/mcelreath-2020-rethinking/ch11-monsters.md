---
id: mcelreath-2020-rethinking/ch11-monsters
work: mcelreath-2020-rethinking
unit: Chapter 11. Monsters and Mixtures
pages: 331-354
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Monsters and Mixtures

## L0 — One line
Likelihoods and link functions can be assembled from simpler parts (cumulative logits, mixtures of a binary event with a count, per-observation random rates) to fit ordered, zero-heavy or over-dispersed outcomes, at the price of models that are harder to fit and interpret.

## L1 — The gist (≤ 120 words)
How do we model outcomes that no single standard GLM fits well? The chapter builds hybrid "monsters" from earlier pieces. Ordered categories get a cumulative logit link, so predictors move probability up or down the ordered scale. Zero-inflated models mix a binary process with a Poisson, because a zero can have two causes. Beta-binomial and gamma-Poisson models give each observation its own probability or rate, which helps mitigate over-dispersion. These models are powerful but harder to fit, plot and compare; WAIC is risky for the last two. The author advises validating any custom model by simulating data and recovering its parameters.

**Prerequisites:** logit and log-odds; binomial and Poisson GLMs with logit and log links; the beta distribution as a distribution over probabilities; posterior samples; WAIC; map and map2stan syntax.

## L2 — Key ideas
- An ordered outcome is a multinomial problem with an order constraint. The fix is to model cumulative probabilities on the log-cumulative-odds scale, with one intercept per category except the last, so K categories need K − 1 intercepts (pp. 332, 335).
- A single-value likelihood comes from subtracting adjacent cumulative probabilities, $p_k=\Pr(y\le k)-\Pr(y\le k-1)$. This yields the likelihood needed for Bayes' theorem (p. 335).
- The linear model $\phi_i$ is subtracted from each intercept. That way a positive slope pushes probability mass toward higher categories, and the order is preserved automatically (p. 338).
- Ordered-logit coefficients are hard to read on their own, so predictions are plotted as cumulative probability curves across predictor values. In the trolley data, intention, action and contact all lower the average moral permissibility rating (pp. 340-342).
- A mixture model uses more than one likelihood for one outcome. The zero-inflated Poisson combines a coin flip (drink or work) with a Poisson count, and it can recover the share of drinking days without knowing which zeros came from drinking (pp. 342-346).
- Over-dispersion means the observed variance exceeds what the count likelihood allows after conditioning on predictors. It signals an omitted source of heterogeneity (p. 346).
- Beta-binomial and gamma-Poisson models give each row its own probability or rate. Those are drawn from a beta or gamma distribution whose mean carries the linear model (pp. 347, 350).
- WAIC should not be used on beta-binomial or gamma-Poisson models unless you are sure what you are doing, because the row structure of the data affects the log-likelihood. The author suggests DIC and, later, multilevel models (p. 351).

## L3 — Walkthrough

### Introduction (p. 331)
The author says many statistical models are hybrids, like mythical monsters. The chapter builds likelihoods and links by piecing together earlier components. Two families are previewed: ordered categorical models (a categorical likelihood plus a cumulative link) and zero-inflated or zero-augmented models (a binary event mixed with a Poisson or binomial GLM). Such models help us adapt the model to the measurement, not the measurement to the model. A custom monster should be validated by simulating dummy data and recovering the data-generating process (p. 331).

### 11.1 Ordered categorical outcomes (pp. 331-342)
**Setting.** An ordered categorical outcome is discrete like a count, but its values only mark ordered levels. Gaps between levels need not be equal (pp. 331-332). It is formally a multinomial problem, but we want a rising predictor to move predictions progressively through the categories in sequence (p. 332).

**Cumulative link.** The cumulative probability of $k$ is the probability of $k$ or any smaller value. A link to cumulative probability can guarantee the ordering. The author explains this in two steps: parameterize the outcome distribution on the log-cumulative-odds scale, then add predictors (p. 332).

**11.1.1 Moral intuition data.** The data are "trolley problem" experiments by philosophers. Three principles may explain differences in judgment (p. 333):
- *action*: harm caused by action is morally worse than equivalent harm by omission.
- *intention*: harm intended as a means is worse than equivalent harm foreseen as a side effect.
- *contact*: harm by physical contact is worse than equivalent harm without it.

The Dennis boxcar story has action only. The Evan story has action and intention (pp. 333). The author says most people judge Evan pulling the lever as less permissible than Dennis pulling it (p. 333). The `Trolley` data have 12 columns and 9930 rows from 331 individuals. The outcome `response` is an integer 1 to 7 giving moral permissibility (p. 333).

**11.1.2 Describing an ordered distribution with intercepts.** Start from the histogram of `response` (Figure 11.1, left), convert it to cumulative proportions (middle), then to log-cumulative-odds (right) (pp. 333-334). The logit is log-odds; the cumulative logit is log-cumulative-odds. Both constrain probabilities to the 0/1 interval, so predictors can safely be added on this scale (p. 334). For each possible value $k$ there is an intercept $\alpha_k$:

$$\log\frac{\Pr(y_i\le k)}{1-\Pr(y_i\le k)}=\alpha_k \tag{11.1}$$

Computed directly from the sample, the values for $k=1,\dots,7$ are −1.916, −1.267, −0.719, 0.248, 0.890, 1.769 and Inf (p. 335). For $k=7$ the cumulative probability is always 1, so $\log(1/(1-1))=\infty$. That intercept comes free from the law of total probability, so $K=7$ values need only $K-1=6$ intercepts (p. 335).

To use Bayes' theorem we need $\Pr(y_i=k)$. Each $\alpha_k$ implies a cumulative probability through the inverse link. The likelihood is then obtained by subtraction (Figure 11.2):

$$p_k=\Pr(y_i=k)=\Pr(y_i\le k)-\Pr(y_i\le k-1) \tag{11.2}$$

The model, with no predictors (p. 335):

$$\begin{aligned}R_i&\sim\text{Ordered}(\mathbf p)\\ \text{logit}(p_k)&=\alpha_k\\ \alpha_k&\sim\text{Normal}(0,10)\end{aligned}$$

Ordered is a categorical distribution over a vector $\mathbf p=\{p_1,\dots,p_6\}$ for response values below the maximum. The priors are weakly regularizing. With this much data almost any prior is overwhelmed. In small samples priors need more thought, for example because $\alpha_1<\alpha_2$ is known before seeing data (p. 335).

In `map`, `dordlogit(phi, c(a1,...,a6))` has the link built in. Here `phi <- 0` is a placeholder for the later linear model. The start values must be in increasing order, but their exact values do not matter (p. 336). The posterior (code 11.6) is: a1 −1.92 (sd 0.03), a2 −1.27 (0.02), a3 −0.72 (0.02), a4 0.25 (0.02), a5 0.89 (0.02), a6 1.77 (0.03) (p. 336). Applying `logistic` gives 0.128, 0.220, 0.328, 0.562, 0.709, 0.854, the same as `cum_pr_k` (p. 337). The Stan version (`map2stan`) uses an explicit `cutpoints` vector and gives the same means, with Rhat 1 (p. 337).

*Intuition note.* The ordered logit re-describes the histogram as a staircase of cumulative probabilities. Each step height is an intercept on the log-odds scale. A category's probability is the gap between two neighboring steps.

**11.1.3 Adding predictor variables.** With $\phi_i=\beta x_i$, each cumulative logit is (p. 337):

$$\log\frac{\Pr(y_i\le k)}{1-\Pr(y_i\le k)}=\alpha_k-\phi_i,\qquad \phi_i=\beta x_i$$

This keeps the order of the outcome values while changing each value's likelihood as $x_i$ changes (p. 337). Why subtract $\phi$? Lowering the log-cumulative-odds of every value below the maximum shifts probability mass upward (p. 338). Demonstration using `dordlogit(1:7, 0, coef(m11.1))`:
- Probabilities: 0.128, 0.092, 0.108, 0.234, 0.147, 0.146, 0.146. Mean response is 4.199.
- Subtracting 0.5 from each intercept gives 0.082, 0.064, 0.082, 0.209, 0.159, 0.184, 0.219. Mean response is 4.730 (p. 338).

So a positive $\beta$ means that increasing $x$ raises the average response (p. 338).

For the trolley data, with dummy variables $A_i$ (action), $I_i$ (intention) and $C_i$ (contact) (p. 338):

$$\phi_i=\beta_AA_i+\beta_II_i+\beta_CC_i$$

`m11.2` fits this with `phi <- bA*action + bI*intention + bC*contact`, priors Normal(0,10), and start values taken from `m11.1`. No link is written around `phi`, since it is inside `dordlogit` (pp. 338-339). `m11.3` adds `bAI*action*intention + bCI*contact*intention`. Action and contact cannot interact, because contact is a type of action in these data (p. 339).

Estimates from `coeftab` (p. 339-340):

| | m11.1 | m11.2 | m11.3 |
|---|---|---|---|
| a1…a6 | −1.92 … 1.77 | −2.84, −2.16, −1.57, −0.55, 0.12, 1.02 | −2.63, −1.94, −1.34, −0.31, 0.36, 1.27 |
| bA | – | −0.71 | −0.47 |
| bI | – | −0.72 | −0.28 |
| bC | – | −0.96 | −0.33 |
| bAI | – | – | −0.45 |
| bCI | – | – | −1.27 |

The $\alpha$ values are intercepts that define outcome frequencies when all predictors are zero (p. 340). The author says the `precis` intervals show all slopes are reliably negative, so action, intention and contact each reduce the average response. Slopes are changes in cumulative log-odds for every value except the maximum, so their size is hard to read directly (p. 340).

WAIC comparison (p. 340):

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m11.3 | 36929.4 | 11.2 | 0.0 | 1 | 81.29 | NA |
| m11.2 | 37090.3 | 9.2 | 160.8 | 0 | 76.22 | 25.80 |
| m11.1 | 37854.7 | 6.1 | 925.2 | 0 | 57.71 | 62.69 |

The author says `m11.3` dominates (dWAIC 161 ± 26), so model uncertainty can be ignored here (p. 340). If it had not, one would pass a list of models to `ensemble` (p. 340).

**Plotting predictions.** There is no perfect way, because each prediction is a vector of probabilities. The author plots intention (0 or 1) on the horizontal axis and cumulative probability on the vertical axis. Code 11.19 loops over 100 posterior samples. For each it computes $\phi$ and applies `pordlogit(1:6, a=ak, phi=phi)`, then draws one line per response boundary (pp. 340-341). Figure 11.3 shows three panels (p. 342):
- action = 0, contact = 0.
- action = 1, contact = 0. The author says this panel shows the action-by-intention interaction (pp. 341-342).
- action = 0, contact = 1. The author says this shows the large contact-by-intention interaction, the largest estimated effect in the model (p. 342).

Posterior uncertainty in the boundaries is small because there is so much data (p. 341).

*Intuition note.* Each blue line is a boundary between neighboring response values. Moving intention from 0 to 1 pushes the boundaries up, so probability mass moves to lower ratings. The steeper the lines, the bigger the shift.

**Rethinking: Staring into the abyss (p. 342).** The author's view: prediction code grows more complex with more monstrous models. It is better to see the machinery than to live in awe or fear of it. Someone unwilling to learn the structure should collaborate with a statistician.

### 11.2 Zero-inflated outcomes (pp. 342-346)
**Mixtures.** Observations are often mixtures of several processes. A mixture model uses more than one simple distribution, in effect more than one likelihood, for the same outcome (p. 342). Counts are prone to this, because a zero can arise when the event rate is low or when the generating process never started. Example: no scrub jays were counted either because there were none or because they were scared off (pp. 342-343).

**Rethinking: Breaking the law (p. 343).** The author says computing is now capable enough that you can imagine a generative process, simulate data, write the model and verify recovery of the true parameters. You need not wait for a mathematician to "legalize" the model.

**11.2.1 Zero-inflated Poisson.** Monks complete a Poisson number of manuscripts per day, but on drinking days they complete none. Let $p$ be the probability of a drinking day, and $\lambda$ the mean manuscripts per working day (p. 343). The probability of a zero is (p. 343):

$$\Pr(0\mid p,\lambda)=\Pr(\text{drink}\mid p)+\Pr(\text{work}\mid p)\times\Pr(0\mid\lambda)=p+(1-p)\exp(-\lambda)$$

This uses the Poisson $\Pr(y\mid\lambda)=\lambda^y\exp(-\lambda)/y!$, so $\Pr(0\mid\lambda)=\exp(-\lambda)$ (p. 343). For $y>0$ (p. 344):

$$\Pr(y\mid p,\lambda)=\Pr(\text{drink}\mid p)(0)+\Pr(\text{work}\mid p)\Pr(y\mid\lambda)=(1-p)\frac{\lambda^y\exp(-\lambda)}{y!}$$

Drinking monks never produce $y>0$ (p. 344). The regression (p. 344):

$$\begin{aligned}y_i&\sim\text{ZIPoisson}(p_i,\lambda_i)\\ \text{logit}(p_i)&=\alpha_p+\beta_px_i\\ \log(\lambda_i)&=\alpha_\lambda+\beta_\lambda x_i\end{aligned}$$

There are two linear models and two links, one per process. They may use different predictors (p. 344).

*Intuition note.* A zero is either a "drinking" zero or a "worked but got nothing" zero. The likelihood adds the two probabilities. Non-zero counts can only come from a working day.

**Simulation (code 11.20).** `prob_drink = 0.2`, `rate_work = 1`, $N=365$ days. `drink <- rbinom(N,1,prob_drink)` and `y <- (1-drink)*rpois(N,rate_work)` (p. 345). The histogram (Figure 11.4, right) has more zeros than a plain Poisson. Zeros from drinking are marked in blue, but in real data we cannot see which zeros come from which process (pp. 344-345).

**Fitting.** `m11.4` uses `dzipois(p, lambda)`, `logit(p) <- ap`, `log(lambda) <- al`, `ap ~ dnorm(0,1)`, `al ~ dnorm(0,10)`. Estimates: `ap` −1.23 (sd 0.29, 89% interval −1.69 to −0.77), `al` 0.06 (sd 0.08, −0.08 to 0.19) (p. 345). On the natural scale the printed outputs are 0.199 for the drink probability and 1.051 for the work rate (pp. 345-346). The author concludes that we get an accurate estimate of the proportion of drinking days without knowing which days were drinking days (p. 346). With predictors, add them to either or both linear models (p. 346).

**Overthinking (p. 346).** `dzipois` guards against numerical error. A transparent version `dzip` returns `p + (1-p)*exp(-lambda)` for $x=0$ and `(1-p)*dpois(x,lambda)` otherwise, optionally logged. The author says it is nearly always better to compute probabilities on the log scale.

### 11.3 Over-dispersed outcomes (pp. 346-351)
**Over-dispersion** means the observed variance exceeds what the count likelihood implies (p. 346). For a binomial the mean is $np$ and the variance is $np(1-p)$. When the observed variance exceeds this after conditioning on all predictors, the author says some omitted variable is adding dispersion (p. 346). Ignoring it can hide effects or produce spurious inferences, like ignoring any predictor (p. 346). The best fix is to find the omitted variable. Otherwise there are two strategies (pp. 346-347):
1. A continuous mixture: attach the linear model to a distribution of observations (beta-binomial, gamma-Poisson).
2. Multilevel models (GLMMs, Chapter 12), which the author says are often easier to fit and much more flexible (p. 347).

**11.3.1 Beta-binomial.** Each binomial count has its own probability of success. The model estimates a distribution of probabilities across cases, and predictors change the shape of that distribution (p. 347). The `UCBadmit` data are over-dispersed if department is ignored, because departments differ a lot in baseline admission rates (p. 347). The beta distribution is a distribution for probabilities, chosen because it permits a closed-form likelihood (p. 347). It has an average probability $\bar p$ and a shape parameter $\theta$. At $\theta=2$ every probability is equally likely. Above 2 the distribution concentrates. Below 2 extreme probabilities near 0 and 1 are more likely than the mean (p. 347). The model (p. 348):

$$\begin{aligned}A_i&\sim\text{BetaBinomial}(n_i,\bar p_i,\theta)\\ \text{logit}(\bar p_i)&=\alpha\\ \alpha&\sim\text{Normal}(0,10)\\ \theta&\sim\text{HalfCauchy}(0,1)\end{aligned}$$

Here $A$ is `admit` and $n$ is `applications`. Predictors would go in the linear model for $\bar p_i$ (p. 348). The code `m11.5` uses `dbetabinom`, `a ~ dnorm(0,2)`, `theta ~ dexp(1)`, `constraints=list(theta="lower=0")` and `start=list(theta=3)`. The author notes $\theta$ can be fickle, so an exponential prior and a start value are better (p. 348). Posterior: `theta` 2.77 (sd 0.96, 89% interval 1.26 to 4.15), `a` −0.38 (sd 0.30, −0.86 to 0.10) (p. 348). The implied average admission probability, `logistic(a)`, has 2.5%, 50% and 97.5% quantiles 0.273, 0.399, 0.543 (p. 348). Figure 11.5 (left) draws 100 beta distributions from the posterior. The author reads it as: central tendency is below 0.5, but plausible distributions allow departments that admit most applicants (p. 349). The posterior check (right) shows that the raw data fall inside the wide prediction intervals. The model cannot see departments but does see heterogeneity across rows (p. 350). The scale $\theta$ is often poorly identified, because many values give similar predictions. An exponential prior samples better "without changing inference" (p. 350).

*Intuition note.* Instead of one admission probability for all rows, the model lets each row draw its own from a beta curve. The mean and spread of that curve are what we estimate. A wide curve lets the model anticipate the department-to-department variation that was left out.

**11.3.2 Negative-binomial (gamma-Poisson).** Each Poisson count has its own rate. These rates follow a gamma distribution with mean $\mu$ and scale $\theta$. Predictors adjust the distribution's shape, not each observation's expected value, and the model parallels the beta-binomial (p. 350). Per the author, as $\theta$ increases, the distribution becomes more dispersed around its mean. As $\theta$ approaches zero, it approaches a Gaussian with the same mean (p. 350). A linear model attaches to $\mu$ through a log link. No worked example is given here (p. 350). Fitting uses `dgampois`.

**11.3.3 Over-dispersion, entropy and information criteria.** Both models are maximum entropy for the same constraints as the ordinary binomial and Poisson, while accounting for unobserved heterogeneity (pp. 350-351). The author says a beta-binomial can be treated as a binomial model, and a gamma-Poisson as a Poisson model, for comparison (p. 351). But do not use WAIC with them unless very sure. Ordinary binomial and Poisson models can be aggregated or disaggregated across rows without changing causal assumptions; these cannot, because an unobserved parameter applies to each row. How the data are structured determines how the beta or gamma variation enters the log-likelihood (p. 351). In most cases the author suggests falling back on DIC. Multilevel models reduce the obstacle, because they can assign heterogeneity at any level of aggregation (p. 351).

**Overthinking: Continuous mixtures (p. 351).** A beta-binomial is a continuous mixture. The probability of $y$ successes averages the binomial over beta-distributed $p$:

$$f(y\mid n,\alpha,\beta)=\int_0^1 g(y\mid n,p)\,h(p\mid\bar p,\theta)\,dp$$

Here $f$ is the beta-binomial density, $g$ the binomial and $h$ the beta density. The gamma-Poisson has a similar form, averaging a Poisson over a gamma distribution of rates. Both integrals can be closed analytically, and `dbetabinom` and `dgampois` implement the closed forms.

### 11.4 Summary (pp. 351-352)
Ordered logistic models attach a cumulative link to a categorical outcome. Zero-inflated models mix two outcome distributions to handle excess zeros. Beta-binomial and gamma-Poisson models draw each observation's expected value from a distribution whose shape depends on a linear model. The next chapter introduces multilevel models (p. 352).

### 11.5 Practice (pp. 352-353)
The set contains easy, medium and hard problems (see Exercises below).

## Toy example (ours, not from the text)
**Ordered logit, 3 categories, no real data.** Intercepts $\alpha_1=-1$, $\alpha_2=1$. Cumulative probabilities are $\text{logistic}(\alpha_k-\phi)$.

*Case $\phi=0$:*
- $\text{logistic}(-1)=1/(1+e^{1})=1/3.71828=0.2689$; $\text{logistic}(1)=0.7311$.
- $p_1=0.2689$, $p_2=0.7311-0.2689=0.4622$, $p_3=1-0.7311=0.2689$. (The tiny difference from 0.4621 is rounding.)
- Mean $=0.2689\cdot1+0.4622\cdot2+0.2689\cdot3=0.2689+0.9244+0.8067=2.000$.

*Case $\phi=1$ ($\beta=1$, $x=1$):*
- $\alpha_1-1=-2$: $\text{logistic}(-2)=1/(1+e^{2})=1/8.389=0.1192$.
- $\alpha_2-1=0$: $\text{logistic}(0)=0.5$.
- $p_1=0.1192$, $p_2=0.5-0.1192=0.3808$, $p_3=1-0.5=0.5$.
- Mean $=0.1192+0.7616+1.5=2.3808$.

A positive $\phi$ raised the mean from 2.000 to 2.381 and moved mass to category 3, as the chapter says.

**Zero-inflated check.** With $p=0.2$, $\lambda=1$: $\Pr(0)=0.2+0.8e^{-1}=0.2+0.8(0.3679)=0.4943$ and $\Pr(1)=0.8(0.3679)=0.2943$. A plain Poisson with $\lambda=1$ gives $\Pr(0)=0.3679$, so zeros are inflated.

## Concepts
- [[ordered-categorical-outcome]] (new) — discrete outcome whose values are ordered levels, with differences between levels not necessarily equal (p. 332)
- [[cumulative-link]] (new) — links a linear model to $\Pr(y\le k)$ through a cumulative logit, which guarantees ordering (p. 332)
- [[log-cumulative-odds]] (new) — $\log[\Pr(y\le k)/(1-\Pr(y\le k))]=\alpha_k$; needs $K-1$ intercepts for $K$ values (p. 335)
- [[ordered-logit-model]] (new) — likelihood by subtraction of adjacent cumulative probabilities; slopes enter as $\alpha_k-\phi_i$ (pp. 335, 337)
- [[mixture-model]] (new) — uses more than one likelihood for one outcome variable, because several causes can produce the same observation (p. 342)
- [[zero-inflated-poisson]] (new) — ZIPoisson with parameters $p$ (probability of a drinking day, which gives only zeros) and $\lambda$ (Poisson mean), each with its own linear model (p. 344)
- [[over-dispersion]] (new) — observed variance larger than the count likelihood implies after conditioning on predictors (p. 346)
- [[beta-binomial]] (new) — binomial with each row's success probability drawn from a beta with mean $\bar p$ and shape $\theta$ (p. 347)
- [[gamma-poisson]] (new) — Poisson with each row's rate drawn from a gamma with mean $\mu$ and scale $\theta$ (also called negative-binomial) (p. 350)
- [[continuous-mixture]] (new) — averaging a likelihood over a continuous distribution of its parameter (p. 351)
- WAIC — used to compare the ordered models m11.1–m11.3; caution against WAIC for beta-binomial and gamma-Poisson models (pp. 340, 351)
- Posterior predictive check — `postcheck(m11.5)` compares the model's predicted intervals with the data (p. 350)
- Principle of indifference / maximum entropy — the beta-binomial and gamma-Poisson are maximum entropy under the same constraints as binomial and Poisson (p. 350)
- Hierarchical (multilevel) model — named as the second strategy for over-dispersion; developed in Chapter 12 (p. 347)

## Canonical instances
- [[trolley-problems]] — the `Trolley` data (action, intention, contact) as an ordered outcome with interactions (pp. 332-342)
- [[monastery-zero-inflation]] — simulated drinking monks and manuscripts for the ZIPoisson (pp. 343-346)
- [[ucbadmit-beta-binomial]] — over-dispersed admissions counts once department is ignored (pp. 347-350)

## Bridges (candidates)
- [structural-analogy] Cumulative link $\alpha_k-\phi_i$ ↔ latent threshold models: cut points on a continuous scale (not stated in this unit; proposal only) — shifting $\phi$ moves all cut points together.
- [structural-analogy] Beta-binomial / gamma-Poisson integrals ↔ [[hierarchical-model]] (Bayesian): both let each row have its own parameter drawn from a distribution; the next chapter develops multilevel models.
- [structural-analogy] Zero-inflation mixture ↔ finite mixture / latent-class models: a hidden binary state selects which likelihood generated the observation.
- [metaphor] "Monsters" as hybrids ↔ model building as composition: new likelihoods assembled from parts with known behavior.

## Questions this raises
- If WAIC is risky for beta-binomial and gamma-Poisson models, how does the multilevel alternative in Chapter 12 let us compare models at the right level of aggregation?
- How would the ordered-logit slopes look as differences in expected response or category probabilities, rather than changes in cumulative log-odds?
- When a zero-inflated model has predictors in both the $p$ and $\lambda$ parts, can the data identify which part each predictor affects?
- Why does the author say $\theta$ is poorly identified, and how much does the prior choice (half-Cauchy vs exponential) matter in small samples?

## Exercises worth doing
- Ex. 11E3 (p. 352) — what ignoring zero-inflation does to inference — difficulty: easy
- Ex. 11M1 (p. 352) — compute log cumulative odds from rating counts 12, 36, 7, 41 — difficulty: easy
- Ex. 11M3 (p. 352) — adapt the ZIPoisson derivation to a zero-inflated binomial — difficulty: medium
- Ex. 11H2 (p. 353) — gamma-Poisson hurricane model; why the association weakens — difficulty: hard
- Ex. 11H5 (p. 353) — use the Trolley data to compare women and men on contact — difficulty: hard
- Ex. 11H6 (p. 353) — zero-inflated Poisson with an exposure offset for the Fish data — difficulty: hard

## Reading notes
- Printed page = pdf − 14. The last pdf page (printed 354) is blank.
- Mismatch in code 11.23: the code shows `logistic(-1.39)` and `exp(0.05)`, which match the printed outputs 0.1994 and 1.0513. The `precis` table above shows −1.23 and 0.06 (mean −1.23, 0.06). The outputs do not follow from the table values shown.
- In the Overthinking box on p. 346 the text refers to "m12.12". The model in this chapter is `m11.4`.
- Notation in the ordered model block (p. 335): `logit(p_k)=α_k` treats $p_k$ as cumulative, while eq. 11.2 uses $p_k$ for a single-value probability. The Overthinking box (p. 351) writes $f(y\mid n,\alpha,\beta)$ on the left but the parameters $\bar p,\theta$ inside the integral.
- The beta-binomial math block (p. 348) gives priors Normal(0,10) and HalfCauchy(0,1), but the code (`m11.5`) uses `dnorm(0,2)` and `dexp(1)`. The text itself explains the switch to the exponential.
- The text describes "upper-left, upper-right, lower-left" panels (pp. 341-342), but Figure 11.3 in the page image shows three panels in one row.
- Typo: "Even pulls the lever" on p. 333 should read Evan.
- Code uses `map`/`map2stan` from the rethinking package. Only `precis` outputs printed in the text are reported here.
- Footnote numbers (147-152, 153) appear in the text, but footnote content is not in these pages.

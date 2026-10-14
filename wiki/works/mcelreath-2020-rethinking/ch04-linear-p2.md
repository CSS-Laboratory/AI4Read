---
id: mcelreath-2020-rethinking/ch04-linear-p2
work: mcelreath-2020-rethinking
unit: "Chapter 4. Linear Models (part 2/2): 4.4 Adding a predictor – 4.7 Practice"
pages: 92-117
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Linear regression, posterior-sample intervals, and polynomials (Ch. 4, second half)

## L0 — One line
Make the Gaussian mean a deterministic linear function of a predictor, fit it, and then understand it by sampling from the posterior and computing any quantity (line, interval, prediction) for each sample.

## L1 — The gist (≤ 120 words)
How can a Gaussian model of height depend on a predictor such as weight? The answer is to replace the mean with $\mu_i=\alpha+\beta x_i$, where α and β are invented parameters. The model is then fitted by quadratic approximation. Tables of estimates alone are hard to read for most models. So the author interprets the posterior by sampling: lines, intervals for the mean, and prediction intervals for new heights. In this example, centering makes α easier to read and removes the parameter correlation. Squared and cubed terms give curves. The practical lesson is that anything that depends on the parameters inherits their posterior uncertainty.

**Prerequisites:** Gaussian likelihood; priors and posteriors; sampling from a posterior; quadratic (MAP) approximation from the first half of the chapter; matrices as rows × columns; basic R reading.

## L2 — Key ideas (5–10 bullets)
- Regression here means using predictors to model an outcome's distribution. The linear-model strategy sets $\mu_i=\alpha+\beta x_i$ with a deterministic "=" line. α and β are invented "targets of learning" (pp. 92–94).
- α is the expected outcome when $x_i=0$. β is the expected change in the outcome per one unit of x. Nothing makes a linear form special; theory-based forms can do better (p. 94).
- There is no uniquely correct prior. Priors encode prior information, and you should vary them to see their influence. Weak priors give results that echo non-Bayesian fits (pp. 94–95).
- Tables of estimates are often insufficient. Parameters can be strongly correlated (α and β: −0.99). In this example, centering the predictor removes this and makes α the expected outcome at the average predictor value (pp. 97–100).
- Everything that depends on parameters has a posterior. Compute it for each posterior sample, then summarize: lines, intervals for μ, and the recipe with `link` (pp. 96, 104–107).
- A prediction interval for actual heights adds the Gaussian sampling variation (σ) to the uncertainty in μ. These are two distinct kinds of uncertainty (pp. 107–109).
- Polynomial regression adds powers of one predictor. It fits curves, but the parameters are hard to interpret, so it is "in general" a bad thing to do. A better fit may not be a better model (pp. 110–114).

## L3 — Walkthrough

### 4.4 Adding a predictor (p. 92)
Section 4.4 turns the earlier Gaussian model of adult !Kung height into regression. The data are the Kalahari foragers' height and weight (R code 4.37 plots them). The plot shows an obvious relationship: knowing weight helps predict height (p. 92).

**Rethinking: What is "regression"?** Today it means using predictors to model the distribution of outcomes. The term originally came from Galton's observation that sons of tall and short men were closer to the population mean (p. 92). The author says this arises whenever measurements are assigned a common distribution, producing shrinkage because each measurement informs the others. He also says this regression/shrinkage idea forms one basis of multilevel modeling (Chapter 12) (p. 92).

#### 4.4.1 The linear model strategy (pp. 92–95)
The strategy makes the Gaussian mean μ a linear function of the predictor and new parameters. It assumes a perfectly constant, additive relationship between the predictor and the mean (p. 92). The posterior then ranks every combination of parameter values by relative plausibility, given model and data (p. 92).

Recall the earlier model (p. 93):
$$h_i\sim \text{Normal}(\mu,\sigma),\quad \mu\sim\text{Normal}(178,20),\quad \sigma\sim\text{Uniform}(0,50)$$
With $x$ the column `d2$weight`, the new model is (p. 93):
$$
\begin{aligned}
h_i&\sim \text{Normal}(\mu_i,\sigma) &&\text{[likelihood]}\\
\mu_i&=\alpha+\beta x_i &&\text{[linear model]}\\
\alpha&\sim\text{Normal}(178,100)\\
\beta&\sim\text{Normal}(0,10)\\
\sigma&\sim\text{Uniform}(0,50)
\end{aligned}
$$

- **Likelihood (4.4.1.1).** The index $i$ on μ means the mean depends on the row (p. 93).
- **Linear model (4.4.1.2).** μ is no longer a parameter. The line has "=" not "∼" because it is deterministic: once α, β and $x_i$ are known, $\mu_i$ is known. α and β are "made up". They are devices for letting μ vary systematically across cases, and the author calls them targets of learning (p. 93).
- The two questions asked by $\mu_i=\alpha+\beta x_i$ (p. 94):
  1. What is the expected height when $x_i=0$? α answers it, so α is the intercept.
  2. How much does expected height change when $x_i$ changes by 1 unit? β answers it.

  Together they ask for a line through α at $x_i=0$ with slope β (p. 94).
- **Rethinking: nothing special about linear models.** For example, $\mu_i=\alpha\exp(-\beta x_i)$ is a legitimate regression model but not a linear one. Fields such as ecology and demography often use theory-based forms. Models built from substantive theory "can dramatically outperform" linear ones (p. 94).
- **Overthinking: units.** With units written out, $h_i$ (cm) $\sim$ Normal($\mu_i$ cm, σ cm) and $\mu_i = \alpha\,\text{cm}+\beta\,\frac{\text{cm}}{\text{kg}}\,x_i\,\text{kg}$. So β must be in cm/kg and is a kind of rate (p. 94).
- **Priors (4.4.1.3).** All are weak, so inferences echo non-Bayesian methods such as maximum likelihood. The author advises playing with the priors (p. 94). The α prior is widened because the intercept can swing far from the outcome's mean (p. 94).
- The β prior is centered at zero. It puts equal probability on negative and positive slopes, which many people see as conservative. It pulls mass toward zero, giving more conservative estimates than a flat prior. With SD 10 the effect is very small. A smaller SD gives more shrinkage toward zero (pp. 94–95).
- The author admits this prior is silly for height and weight (a negative relation is not as plausible as a positive one). It is harmless here because there is a lot of data (p. 95).
- **Rethinking: what's the correct prior?** There is no more a uniquely correct prior than a uniquely correct likelihood. Priors can be wrong, but only in the same sense that a kind of hammer can be wrong for building a table. Priors encode states of information before data. Vary them to see how initial information changes inference. Frequently several reasonable priors give the same inference. Conventional Bayesian priors are conservative relative to conventional non-Bayesian approaches. The author calls it an illusion that default procedures are more objective; if they were, "objective" would only mean that everyone does the same thing, with no guarantee of realism or accuracy (p. 95).

> *Intuition note.* α and β are not found in nature. We invent them so that the mean can change with x. The posterior then tells us which (α, β) pairs are plausible.

#### 4.4.2 Fitting the model (pp. 95–97)
The model is fitted with `map` (quadratic approximation). In the code the linear model uses `<-` while the math uses "=" (pp. 95–96):
```
m4.3 <- map(alist(height ~ dnorm(mu,sigma), mu <- a + b*weight,
  a ~ dnorm(156,100), b ~ dnorm(0,10), sigma ~ dunif(0,50)), data=d2)
```
(R code 4.38, p. 96; d2 = adults, age ≥ 18).
- `mu` has no prior because the linear model defines it (p. 96).
- In the start list, `a` starts at the overall mean and `b` at 0. A start value of 0 is not the same as a prior mean of 0. Start values do not alter the posterior, while priors do. If the search starts far outside the high-density region, R may give up before finding the MAP values (p. 96).
- **Rethinking: everything that depends on parameters has a posterior.** Since α and β have a joint posterior, so does μ. To account for uncertainty in any quantity, compute it for each posterior sample. The resulting values approximate its posterior distribution (p. 96).
- **Overthinking: embedding.** The linear model can be merged into the likelihood: `height ~ dnorm(a + b*weight, sigma)` (R code 4.39). This is exactly the same model. The explicit form is easier to read, and some helper functions depend on it (p. 97).

#### 4.4.3 Interpreting the model fit (pp. 97–109)
The model only reports posteriors, and it is the analyst's job to make sense of them. Two kinds of processing exist: reading tables and plotting. Tables are hard to read for models with many parameters. With interactions (Chapter 7) or polynomials it may not even be possible to guess the direction of a predictor's influence (p. 97). The author emphasizes plotting. Plots help check (1) whether fitting worked, (2) absolute magnitude of the relationship, (3) uncertainty around the average relationship, and (4) uncertainty in implied predictions, which differs from parameter uncertainty (p. 97).

**Rethinking: what do parameters mean?** There is no consensus. The author's view is that posterior probabilities of parameter values describe the relative compatibility of different states of the world with the data, according to the model. These are small-world numbers (p. 98).

**4.4.3.1 Tables of estimates (pp. 98–100).** For `m4.3` (R code 4.40, p. 98):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 113.90 | 1.91 | 110.85 | 116.94 |
| b | 0.90 | 0.04 | 0.84 | 0.97 |
| sigma | 5.07 | 0.19 | 4.77 | 5.38 |

- β = 0.90 means a person 1 kg heavier is expected to be 0.90 cm taller. 89% of the posterior lies between 0.84 and 0.97. Values near zero or well above one are highly incompatible with these data and this model. This is conditional on the model (p. 98).
- α = 113.9 says a person of weight 0 should be about 114 cm tall. This is nonsense as biology, yet it is true of the fitted line. The intercept is frequently uninterpretable without the β parameters. This is why intercepts often need very weak priors (pp. 98–99).
- σ: about 95% of a Gaussian lies within two SDs, so about 95% of plausible heights lie within about 10 cm (2σ) of the mean height. σ itself is also uncertain (p. 99).
- The default table does not fully describe the quadratic posterior. The variance-covariance matrix is also needed. `precis(m4.3, corr=TRUE)` shows correlations, equal to `cov2cor(vcov(m4.3))`: a–b is −0.99, and both are 0 with sigma (R code 4.41, p. 99). Here this is harmless: the two carry the same information, because as the slope changes the best intercept changes to match. In more complex models such correlations can make fitting difficult (p. 99).
- **Centering** means subtracting the variable's mean from each value: `weight.c <- weight - mean(weight)` (R code 4.42). Refitting as `m4.4` with `mu <- a + b*weight.c` gives (R code 4.44, p. 100):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 154.60 | 0.27 | 154.17 | 155.03 |
| b | 0.91 | 0.04 | 0.84 | 0.97 |
| sigma | 5.07 | 0.19 | 4.77 | 5.38 |

  β and σ are unchanged within rounding. α now equals the raw mean height. All parameter correlations are 0 (p. 100). α still means the expected outcome when the predictor is zero. Now zero is the average weight, so α is the expected height at average weight (p. 100).

> *Intuition note.* Before centering, tilting the line forces the intercept to move the other way, so the two numbers are tied together. After centering, the intercept is the expected height at average weight, and in this example the correlations are zero, so changing the slope no longer drags the intercept along (our plain-words reading).

**4.4.3.2 Plotting posterior inference against the data (p. 100).** Plots interpret the posterior and give an informal check on assumptions. If predictions do not come close to key patterns in the data, the model may not have fit correctly or may be badly specified (p. 100). The MAP line is drawn with `abline(a=coef(m4.3)["a"], b=coef(m4.3)["b"])` (R code 4.45; Figure 4.4, p. 101).

**4.4.3.3 Uncertainty around the mean (pp. 100–102).** The MAP line shows magnitude but poorly communicates uncertainty (p. 100). Each (α, β) pair is a line, so we can sample lines from the posterior. `extract.samples(m4.3)` returns rows of correlated draws of `a`, `b`, `sigma`, using the covariances in `vcov` (R codes 4.46–4.47, p. 101). The scatter around the average line is meaningful (p. 101).

To show how data change the scatter, the author refits on the first N = 10 cases (`mN`, R code 4.48) and plots 20 sampled lines (R code 4.49; Figure 4.5, p. 102). The cloud is wider at extreme weights ("very common"). With N = 10, 50, 150, 352 the cloud becomes more compact as the model grows more confident about the mean's location (pp. 102–103).

**4.4.3.4 Regression intervals and contours (pp. 102–107).**
- At a single weight, 50 kg, compute $\mu=\alpha+\beta\cdot 50$ for each sample: `mu_at_50 <- post$a + post$b*50` (R code 4.50, p. 103). This is a vector of 10,000 means. It carries the uncertainty in, and correlation between, both parameters (p. 103).
- The distribution of μ is Gaussian, since adding Gaussian distributions gives a Gaussian (Figure 4.6, p. 104). The 89% HPDI (highest posterior density interval) is 158.5642 to 159.6616 (R code 4.52, p. 104). The author says the model places the average height at 50 kg between about 159 and 160 cm, conditional on model and data (p. 104).
- `link(m4.3)` returns a 1000 × 352 matrix: a row per posterior sample and a column per case in the data (R code 4.53, pp. 104–105). Passing new data, `weight.seq <- seq(25, 70, by=1)`, gives a 1000 × 46 matrix (R code 4.54, p. 105).
- Plotting these μ values at each weight shows piles of Gaussian values whose spread depends on weight (R code 4.55; Figure 4.7 left, pp. 105–106).
- Summaries: `mu.mean <- apply(mu, 2, mean)` and `mu.HPDI <- apply(mu, 2, HPDI, prob=0.89)`, where "2" means by column (R code 4.56, p. 105). The line and shaded interval come from `lines` and `shade` (R code 4.57; Figure 4.7 right, p. 106).
- The author says his attempts to teach the analytic approach went badly, partly because many scientists get nervous around integrals. The sample-based approach is flexible, and he says that under MCMC (Chapter 8) it is the only approach available (p. 106).
- **Recipe (p. 107):**
  1. Use `link` to get posterior values of μ, passing new predictor values.
  2. Summarize with `mean`, `HPDI` or `PI` for each predictor value.
  3. Plot with `lines` and `shade`, or do other calculations.

  The author says this recipe works for every model fitted in the book, as long as you know how parameters relate to the data (p. 107).
- **Rethinking: overconfident confidence intervals.** The interval hugs the MAP line, but inferences are always conditional on the model. Even a very bad model can have very tight intervals. Read Figure 4.7 as: *conditional on a straight-line relation, this is the most plausible line and these are its plausible bounds* (p. 107).
- **Overthinking: how `link` works.** It just evaluates the linear model for each posterior sample and case. The manual equivalent is (R code 4.58, p. 107):
```
post <- extract.samples(m4.3)
mu.link <- function(weight) post$a + post$b*weight
mu <- sapply(weight.seq, mu.link)
```
  The author says the manual method is more flexible than automated tools (p. 107).

**4.4.3.5 Prediction intervals (pp. 107–110).** The intervals above concern μ only. Actual heights follow $h_i\sim\text{Normal}(\mu_i,\sigma)$, so they scatter around μ with spread σ, and σ must enter the predictions (pp. 107–108). The method is to simulate: for each posterior sample and each weight, draw a height from a Gaussian with that sample's μ and σ. `sim(m4.3, data=list(weight=weight.seq))` returns a 1000 × 46 matrix of simulated heights (R code 4.59, p. 108). `height.PI <- apply(sim.height, 2, PI, prob=0.89)` summarizes it (R code 4.60). The MAP line, the narrow shaded region for μ, and the wide region for simulated heights are plotted together (R code 4.61; Figure 4.8, pp. 108–109).
- The wide region is where the model expects 89% of actual heights at each weight. Nothing is special about 89%; other levels such as 67% or 97% can be added with `prob=` (pp. 108–109).
- The outline is jagged because of simulation variance in the tails. Increasing `n` (R code 4.62, `n=1e4`) smooths it. The author notes that computing a value to ten decimals does not make the inference that precise (p. 109).
- **Rethinking: two kinds of uncertainty.** Uncertainty in parameter values (the posterior) differs from sampling variation in a Gaussian process (the simulated outcomes). They are processed the same way and blended in the simulation, but they rest on different model assumptions. The Gaussian likelihood can also be viewed as a purely epistemological device for estimating mean and variance, in which case it may not make complete sense to simulate outcomes (p. 109).
- **Overthinking: rolling your own `sim`.** Use `rnorm(n=nrow(post), mean=post$a+post$b*weight, sd=post$sigma)` for each weight (R code 4.63, p. 110).

> *Intuition note.* The narrow band answers "where is the average height at this weight?" The wide band answers "where might a new person's height fall?" The second band is wider because it adds person-to-person scatter (σ) on top of uncertainty about the average.

### 4.5 Polynomial regression (pp. 110–114)
The full !Kung data (544 rows: height, weight, age, male; R code 4.64) show a visibly curved relation when non-adults are included (p. 110). "Polynomial" here means adding squares, cubes and higher powers of a single predictor, so it is still a bivariate regression with more parameters (p. 110). The author warns that polynomials are "in general" a bad thing to do because they are hard to interpret. A more mechanistic model would be better (see the practice problems). He teaches them anyway because they are common and expose issues taken up in Chapter 6 (pp. 110–111).

The parabolic (second-order) model (p. 111):
$$\mu_i=\alpha+\beta_1 x_i+\beta_2 x_i^2$$
β₂ measures the curvature (p. 111).

**Rethinking: linear, additive, funky.** The parabola is still called a "linear model" because $\mu_i$ is a linear function of any single parameter. Such models are easier to fit and often easier to interpret, because they assume that parameters act independently on the mean. They are also strongly conventional and often used thoughtlessly. The author calls them "geocentric engines" that describe partial correlations (p. 111).

**Standardizing** means centering the variable and then dividing by its standard deviation: `weight.s <- (weight - mean(weight))/sd(weight)` (R code 4.65, p. 112). The new variable has mean 0 and SD 1, and no information is lost (p. 112). Two reasons (p. 111):
1. A one-unit change is one SD, which is often more interesting. It also helps compare predictors, but may be harder if you want the natural scale.
2. More important, large predictor values can cause numerical glitches, common in polynomials because squares and cubes of large numbers are massive. Standardizing largely resolves this.

The model, with priors (p. 112):
$$
\begin{aligned}
h_i&\sim\text{Normal}(\mu_i,\sigma),\quad \mu_i=\alpha+\beta_1x_i+\beta_2x_i^2,\\
\alpha&\sim\text{Normal}(178,100),\ \beta_1\sim\text{Normal}(0,10),\ \beta_2\sim\text{Normal}(0,10),\ \sigma\sim\text{Uniform}(0,50)
\end{aligned}
$$
The square is pre-computed, `weight.s2 <- weight.s^2`, and used in `mu <- a + b1*weight.s + b2*weight.s2` (R code 4.66, `m4.5`). The author says it is better to pre-process variable transformations (p. 112). Estimates (R code 4.67, p. 112):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 146.66 | 0.37 | 146.07 | 147.26 |
| b1 | 21.40 | 0.29 | 20.94 | 21.86 |
| b2 | −8.42 | 0.28 | −8.87 | −7.97 |
| sigma | 5.75 | 0.17 | 5.47 | 6.03 |

α is still the expected height when `weight.s` = 0, but it is no longer equal to the sample mean height, since there is no such guarantee in polynomial regression. β₁ and β₂ are the linear and square components, but that does not make them easy to read (p. 112). One must plot (p. 113).

Plot code (R codes 4.68–4.69): `weight.seq <- seq(-2.2, 2, length.out=30)`, `pred_dat` containing `weight.s` and `weight.s2`, then `link`, `sim`, `PI`. Figure 4.9 compares (a) linear, (b) parabolic and (c) cubic fits on the full data (p. 113). The linear model makes very poor predictions at both very low and middle weights. The parabola finds a better central path (p. 113).

The cubic model adds $\beta_3 x_i^3$ with $\beta_3\sim\text{Normal}(0,10)$; `m4.6` uses `weight.s3` (R code 4.70, p. 114). It is more flexible and fits better. But the author says it is unclear that any of these models make much sense. They are good geocentric descriptions of the sample, and Chapter 6 will show that a better fit might not be a better model (p. 114).

**Overthinking: converting back to natural scale.** Plot with `xaxt="n"` (R code 4.71), then use `at <- c(-2,-1,0,1,2)`, `labels <- at*sd(d$weight)+mean(d$weight)`, `axis(side=1, at=at, labels=round(labels,1))` (R code 4.72, p. 114). Standard units are sometimes called z-scores (p. 114).

> *Intuition note.* Adding a squared term lets the fitted mean bend. The price is that the coefficients are not transparent (p. 112), so the author plots the fit to understand it (p. 113).

### 4.6 Summary (p. 115)
The chapter introduced simple linear regression. The Gaussian likelihood counts the relative number of ways different mean/SD combinations can produce an observation. It introduced MAP estimation and procedures to visualize posterior distributions and predictions. The next chapter adds more than one predictor (p. 115).

### 4.7 Practice (pp. 115–117)
Easy (4E1–4E5): identify the likelihood and the linear model; count posterior parameters; write Bayes' theorem for a given model. Medium (4M1–4M6): simulate heights from the prior; translate between math and `map` formulas; choose priors for a yearly height regression and revise them given extra information. Hard (4H1–4H3): predict heights and 89% intervals for five new weights (46.95, 43.72, 64.78, 32.59, 54.63 kg); fit a regression to the 192 rows under age 18; regress height on $\log(w_i)$ for all 544 rows. See Exercises below.

## Toy example (ours, not from the text)
Pretend the posterior is summarized by three samples. Weights have mean $\bar x=50$ kg. The sample parameters in the centered form $\mu = a_c + b(x-50)$ are:

| sample | $a_c$ | $b$ |
|---|---|---|
| S1 | 145 | 0.9 |
| S2 | 146 | 0.7 |
| S3 | 144 | 1.1 |

**Uncentered intercepts.** $a = a_c - 50b$: S1: $145-45=100$; S2: $146-35=111$; S3: $144-55=89$. So $(a,b)$ = (100, 0.9), (111, 0.7), (89, 1.1). Steeper slopes go with lower intercepts, a strong negative correlation, as in the text (p. 99). Centered, the intercept barely moves (144–146).

**Mean at three weights**, $\mu=a_c+b(x-50)$:
- x = 50: 145, 146, 144 (range 2).
- x = 70: S1 $145+0.9\cdot20=163$; S2 $146+0.7\cdot20=160$; S3 $144+1.1\cdot20=166$ (range 6).
- x = 30: S1 $145-18=127$; S2 $146-14=132$; S3 $144-22=122$ (range 10).

Uncertainty about μ is smallest at the data's mean and larger at the extremes, as in Figure 4.5 (p. 102).

**Prediction.** Take σ = 5 for every sample and made-up standard normal draws z = 0.5, −1, 1.2. At x = 70, simulated heights are $163+5(0.5)=165.5$; $160+5(-1)=155$; $166+5(1.2)=172$. They spread (155–172, range 17) more than the three μ values (160–166, range 6), because σ adds sampling variation.

## Concepts
- [[linear-regression-model]] (new) — a Gaussian outcome whose mean is a deterministic linear function of a predictor, $\mu_i=\alpha+\beta x_i$ (p. 93)
- [[likelihood]] — the Gaussian line $h_i\sim\text{Normal}(\mu_i,\sigma)$; μ now varies by row (p. 93)
- [[prior-distribution]] — encodes information before data; here deliberately weak; no uniquely correct prior (pp. 94–95)
- [[posterior-distribution]] — ranks all (α, β, σ) combinations by relative plausibility; the author reads it as relative compatibility of states of the world with data, given the model (pp. 92, 98)
- [[map-quadratic-approximation]] (new) — fitting by a Gaussian approximation at the posterior peak; `map` in `rethinking` (p. 95)
- [[centering]] (new) — subtracting the mean of a predictor; makes α the expected outcome at the average predictor and decorrelates α and β here (pp. 99–100)
- [[standardization]] (new) — centering then dividing by SD; one unit = one SD; avoids numerical glitches with powers (p. 111)
- [[polynomial-regression]] (new) — adding powers of one predictor to μ; still "linear" in each parameter; hard to interpret (pp. 110–111)
- [[credible-interval]] — here HPDI and PI of posterior samples; the author sometimes uses "confidence interval" for the same shaded bands (pp. 104, 107)
- [[posterior-predictive-distribution]] — simulated heights that combine posterior uncertainty with Gaussian sampling variation (pp. 108–109)
- [[prediction-interval]] (new) — the interval where the model expects a given percent of actual outcomes at a predictor value (p. 108)
- [[posterior-sampling-recipe]] (new) — compute any quantity for each posterior sample, then summarize it (pp. 96, 107)

## Canonical instances
- [[howell1-kung-height-weight]] (new) — the !Kung height/weight data used for the linear fit (adults, 352 rows) and polynomial fits (all, 544 rows) (pp. 92, 105, 110)
- [[galton-regression-to-the-mean]] — sons of tall/short fathers closer to the mean; shrinkage as a basis of multilevel models (p. 92)
- [[height-weight-parabola-cubic]] (new) — Figure 4.9: linear vs parabolic vs cubic fits (pp. 113–114)

## Bridges (candidates)
- [structural-analogy] Galton's regression to the mean / shrinkage ↔ bayesian: partial pooling, where noisy estimates are pulled toward a common mean (p. 92 links it to multilevel models)
- [same-math] Simulating heights from each posterior sample's (μ, σ) ↔ bayesian: posterior predictive distribution; the procedure is the same Monte Carlo averaging over parameters
- [metaphor] Author's "geocentric" linear models ↔ philosophy of science: descriptive devices that fit well without explaining mechanism

## Questions this raises
- How does the choice of weakly informative priors change the intervals in small samples such as N = 10?
- Why does a better in-sample fit (cubic vs parabola) not make a better model (promised for Chapter 6)?
- What would a mechanistic, theory-based form for height as a function of weight look like (cf. the log-weight exercise)?
- When correlations among parameters are strong in a model with several predictors, how does centering or standardizing help?

## Exercises worth doing
- Ex. 4E2 and 4E5 (p. 115) — counting parameters in the posterior with and without a linear model — difficulty: easy
- Ex. 4M1 (p. 115) — simulate observed heights from the prior only; shows what the priors imply — difficulty: medium
- Ex. 4M4–4M6 (p. 116) — choose and revise priors using stated background knowledge — difficulty: medium
- Ex. 4H1 (p. 116) — use posterior samples to predict heights and 89% intervals for new weights — difficulty: medium
- Ex. 4H2 (p. 116) — fit and criticize a linear model for children (192 rows); what fits poorly? — difficulty: hard
- Ex. 4H3 (pp. 116–117) — regress height on log(weight) and plot mean and 97% intervals — difficulty: hard

## Reading notes
- This part starts at section 4.4 "Adding a predictor" (printed p. 92) and ends at the end of the chapter (last printed problem, 4H3(b), p. 117). The pdf page at printed 118 is blank. Printed = pdf − 14.
- Prior mismatch: the math for α is Normal(178, 100), but the printed code on p. 95 and in R code 4.38 (p. 96) shows `a ~ dnorm(156,100)`, and the polynomial table on p. 112 shows `a ~ dnorm(140,100)`. R codes 4.39, 4.43 and 4.66 use 178.
- p. 96 discusses a `start` list, but the displayed code 4.38 has no start list.
- p. 115 summary reads "maximum a prior" for MAP. The image shows this wording; the Figure 4.4 caption on p. 101 reads "maximum a posteriori".
- p. 105 says the plot shows μ values "at each height", but the code and figure show them at each weight value. p. 113 has the typo "spectularly".
- The author calls HPDI/PI bands "confidence interval" on p. 107, though they are intervals computed from posterior samples.
- Footnote markers 68, 69, 70 appear (pp. 92, 94, 112), but footnote text is not in these pages. Figure 4.5 sample sizes (10, 50, 150, 352) were read from the image.

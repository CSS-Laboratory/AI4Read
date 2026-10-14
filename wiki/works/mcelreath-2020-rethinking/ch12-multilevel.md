---
id: mcelreath-2020-rethinking/ch12-multilevel
work: mcelreath-2020-rethinking
unit: Chapter 12. Multilevel Models
pages: 355-386
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Chapter 12. Multilevel Models

## L0 — One line
A multilevel model gives each cluster its own parameter and learns the prior shared by those parameters from the data, so clusters share information (partial pooling), which tends to improve estimates.

## L1 — The gist (≤ 120 words)
Models with one dummy variable per cluster treat clusters as unrelated and "forget" what earlier clusters taught. This chapter asks how to learn about each cluster and about the population of clusters at once. The answer is varying intercepts: each cluster's intercept comes from a Gaussian whose mean and standard deviation are themselves estimated. Small or extreme clusters are shrunk toward the population mean. Simulated ponds show that these partially pooled estimates have lower average error than no-pooling estimates. The chapter then adds a second cluster type and shows how to predict for the same clusters or for new ones.

**Prerequisites:** Binomial and Poisson regression with logit and log links; priors and posterior sampling; overfitting versus underfitting and WAIC (Ch. 6); maximum entropy; basic MCMC diagnostics.

## L2 — Key ideas (5–10 bullets)
- Dummy-variable (fixed-intercept) models assume clusters share no information, which the author calls "anterograde amnesia". Multilevel models instead learn the population of clusters and use it as an adaptive prior (pp. 355–356).
- A varying-intercepts model puts a Normal(α, σ) prior on cluster intercepts and hyperpriors on α and σ (hyperpriors are priors for these population parameters, which are themselves "parameters for parameters"). It cannot be fitted by MAP (finding the single highest point of the posterior), so MCMC (sampling the posterior) is used (pp. 358–360).
- Fitting gives shrinkage: estimates move toward the population mean, more for small clusters and for extreme ones (p. 362).
- The multilevel tadpole model has fewer effective parameters (38; pWAIC, a measure of how flexible the fit is) than the ordinary fixed-intercept (no-pooling) model (49.4), though it has more actual parameters (50 vs 48) (pp. 359–360).
- In simulated ponds, partial pooling beats no pooling on average, most for the smallest ponds. Complete pooling (one shared estimate for all clusters) underfits, and no pooling (separate, unrelated estimates for each cluster) overfits (pp. 364–370).
- Several cluster types can be used together. Each gets its own σ, and one shared mean α sits in the linear model. The σ of a cluster type can be read as a crude measure of its relevance for explaining the outcome; a σ near zero suggests little relevance (pp. 372–376).
- Predictions depend on focus. For observed clusters use their intercepts. For new clusters, or over-dispersion (more variation than a binomial or Poisson model expects), simulate intercepts from the hyperparameters (the population parameters, such as α and σ) (pp. 381–384).

## L3 — Walkthrough

### Introduction (pp. 355–357)
- **Amnesia analogy.** Clive Wearing cannot form new long-term memories. Many models behave the same way: when they move from one cluster (individual, group, location) to the next, they forget the previous clusters. Models that use dummy variables for categories are "programmed for amnesia": their parameters are independent and learn from separate portions of the data (p. 355).
- **Aim.** We want to learn about each cluster while learning about the population of clusters. This transfers information across clusters and improves accuracy (p. 355).
- **Coffee robot.** A robot has a prior for waiting times of mean 5 min and sd 1. It sees 4 min at café 1 and updates. Using café 1's posterior as the prior for café 2 would assume the cafés are identical. Ignoring café 1 would be amnesia. Instead, the robot represents the population of cafés (at least an average and a standard deviation). That population distribution is the prior for each café, and it is learned from the data (pp. 355–356).
- If the population seems highly variable, the prior is flat and one café says little about another. If it varies little, the prior is narrow and one café strongly affects estimates for another (p. 356).
- **Four benefits** (p. 356):
  1. Better estimates for repeat sampling; single-level models either maximally underfit or overfit.
  2. Better estimates under imbalanced sampling; over-sampled clusters do not dominate.
  3. Explicit estimates of variation among groups.
  4. No pre-averaging, which removes variation, creates false confidence and adds arbitrary transformations.
- The author says multilevel regression "deserves to be the default approach". Single-level models are better in some contexts, but the contexts favouring multilevel models are more numerous (p. 356).
- **Costs** (pp. 356–357):
  - New assumptions: we must define the distributions the cluster characteristics come from. Conservative maximum entropy distributions do well here.
  - New estimation challenges, which lead into MCMC.
  - Predictions are made at several levels, so model comparison with DIC or WAIC is more subtle. The basic logic is unchanged, but we must decide which parameters to focus on.
- Terminology varies ("hierarchical", "mixed effects", "random effects"). Only a mathematical or algorithmic definition removes ambiguity (p. 357).

### 12.1 Example: multilevel tadpoles (pp. 357–364)
**Data.** `reedfrogs` has 48 rows, each a "tank" holding tadpoles. We use only `surv` (number surviving) out of `density` (initial count) (p. 357). A tank is a *cluster variable*: several observations (tadpoles) are made within it. Unmeasured tank-specific factors cause variation in survival (pp. 357–358).

**Why not ignore or separate tanks.** One common intercept ignores baseline variation, which could mask other associations. A dummy variable per tank is amnesia, since tanks differ but still help estimate each other (p. 358).

**Fixed-intercept model (m12.1).** Each intercept is a separate parameter with a fixed regularizing prior (p. 358):
$$s_i \sim \text{Binomial}(n_i, p_i), \quad \text{logit}(p_i) = \alpha_{\text{tank}[i]}, \quad \alpha_{\text{tank}} \sim \text{Normal}(0, 5)$$

**Multilevel model (m12.2).** Make the prior a function of its own parameters (p. 359):
$$
\begin{aligned}
s_i &\sim \text{Binomial}(n_i, p_i)\\
\text{logit}(p_i) &= \alpha_{\text{tank}[i]}\\
\alpha_{\text{tank}} &\sim \text{Normal}(\alpha, \sigma)\\
\alpha &\sim \text{Normal}(0, 1)\\
\sigma &\sim \text{HalfCauchy}(0, 1)
\end{aligned}
$$
- Two levels: in the top level the outcome is $s$, the parameters are $\alpha_{\text{tank}}$ and the prior is Normal(α, σ). In the second level the "outcome" is the vector $\alpha_{\text{tank}}$, the parameters are α and σ, and their priors are the last two lines (p. 359).
- α and σ are **hyperparameters** (parameters for parameters); their priors are **hyperpriors**. In principle there is no limit on the number of "hyper" levels; in practice computation and understanding limit it (p. 359).
- **Why Gaussian?** Three answers: convention; pragmatism (easy, and it generalizes to more dimensions); and the author's preferred one, entropy: if we only state a mean and variance, the Gaussian is the most conservative assumption. Other distributions may be used for good reason (p. 359).
- **Why MAP fails** (p. 360). When the prior is a function of parameters, the probability of the data must average over each level. In general there is no analytical solution, so there is no single log-posterior function to optimize. Also, the posterior of these models is routinely non-Gaussian. As models grow more complex, concentration of measure "guarantees" that the posterior mode is far from the posterior median, so optimization is abandoned in favour of MCMC. The model is fitted with `map2stan` (iter=4000, chains=4) (pp. 359–360).

**WAIC comparison (p. 360).** The model has 50 parameters (α, σ and 48 intercepts).

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m12.2 | 1010.2 | 38.0 | 0.0 | 1 | 37.94 | NA |
| m12.1 | 1023.3 | 49.4 | 13.1 | 0 | 43.01 | 6.54 |

- The multilevel model has about 12 fewer effective parameters than actual ones, because the prior shrinks intercepts toward α. The mean of σ is around 1.6, so the prior is fairly strong. The regularization strength was learned from the data (p. 360).
- m12.2 has fewer effective parameters than m12.1 although it has more actual ones (50 vs 48). The extra two parameters let it learn a more aggressive regularizing prior ("adaptive regularization") (p. 360).

*Intuition note.* A parameter counts less than one "free" parameter when its prior holds it near the others. A prior learned from the data can hold the 48 intercepts together more tightly than a fixed prior would.

**Figure 12.1 (pp. 361–362).** It plots raw proportions surviving against the multilevel posterior medians (converted from log-odds with the logistic function). The dashed line near 0.8 is the estimated median survival proportion in the population of tanks (α), and it is not the same as the empirical mean survival. Three observations (p. 362):
1. In every tank the multilevel estimate is closer to the dashed line than the raw proportion. This is **shrinkage**, which results from regularization.
2. Estimates for smaller tanks (10 tadpoles) shrink more than those for larger tanks (25, 35).
3. The farther a raw proportion is from the global average α, the greater the shrinkage.

All three arise from **pooling**: each tank's data inform the estimates of all other tanks. This works because we assumed a distribution (normal) for the tank log-odds, so Bayes' theorem can share information "optimally (in the small world only)" (p. 362).

*Intuition note.* A small tank gives a noisy raw proportion, so the model trusts the population more. For an unusually high or low proportion, few tanks behave that way, so it is pulled back more (though sometimes outliers really are outliers, p. 370).

**Population distribution (Figure 12.2, pp. 362–363).** Plot 100 Gaussians, one for each of the first 100 posterior samples of (α, σ). Then draw 8000 new log-odds from `rnorm(8000, post$a, post$sigma)` and transform with the logistic. Uncertainty in α and σ is propagated into the simulated survival probabilities. "Sampling" from a posterior is a convenient way to work with uncertainty, not a simulation of empirical sampling (p. 362).

**Rethinking: varying intercepts as over-dispersion (p. 363).** Giving each observed count its own intercept, pooled through a common distribution, makes predictions expect over-dispersion like beta-binomial or gamma-Poisson models. This is often easier to estimate and extend.

**Overthinking: priors for variance components (pp. 363–364).** Half-Cauchy priors work well in routine cases but can be problematic in two contexts:
- there is little information on the variance (e.g. only 5 clusters);
- non-linear models with logit or log links, where floor and ceiling effects make extreme variance values as plausible as realistic ones.

The Cauchy tail is thick and long, so chains may wander over very large values, sampling inefficiently (small n_eff, possibly many divergent iterations). An alternative is $\sigma \sim \text{Exponential}(1)$ (`dexp(1)`), with a much thinner tail. The exponential is the maximum entropy prior for the standard deviation if all we want to say a priori is its expected value. It is not usually necessary, but it can be when variance components are only weakly identified. It is useful to try different priors and see how inference changes (p. 364).

### 12.2 Varying effects and the underfitting/overfitting trade-off (pp. 364–370)
Varying intercepts are regularized estimates, with the amount of regularization estimated from how diverse the clusters are. On average they estimate individual cluster means better than raw estimates, because they trade off underfitting and overfitting better (p. 364).

**Three perspectives** (imagine natural ponds, with future prediction for the same ponds) (pp. 364–365):
1. **Complete pooling.** Use one common intercept (the overall mean). It is precise but unlikely to match any pond, so it underfits. It is equivalent to assuming zero variation among ponds.
2. **No pooling.** Use each pond's raw proportion (the blue points in Fig. 12.1). Little data go into each estimate, so error is high, especially in small ponds; the estimates overfit, and standard errors can be very large or even infinite. It is like assuming infinite variation among ponds.
3. **Partial pooling.** Varying intercepts give estimates less underfit than the grand mean and less overfit than no pooling. This matters most for small ponds. When each pond has a lot of data, the partial-pooling and no-pooling estimates differ less (p. 365).

The chapter simulates data so the true pond probabilities are known. The author also recommends simulating data from a model to check that the estimation method recovers the parameters (p. 365).

**12.2.1 The model (p. 365).** The same model as before, with "pond" for "tank":
$$s_i \sim \text{Binomial}(n_i, p_i),\ \text{logit}(p_i) = \alpha_{\text{pond}[i]},\ \alpha_{\text{pond}} \sim \text{Normal}(\alpha, \sigma),\ \alpha \sim \text{Normal}(0,1),\ \sigma \sim \text{HalfCauchy}(0,1)$$
To simulate we must assign α, σ, a vector $\alpha_{\text{pond}}$ and the sample sizes $n_i$. The priors are used when estimating but not when simulating: "priors are epistemology, not ontology". They describe the robot's initial information, not how nature picks parameters (p. 366).

**12.2.2–12.2.3 Simulate (pp. 366–367).** Values: α = 1.4, σ = 1.5, 60 ponds, with $n_i$ = 5, 10, 25, 35 (15 ponds each), stored as integers because Stan requires integer trial counts. Draw `a_pond <- rnorm(60, 1.4, 1.5)`. Survivors come from `rbinom` with
$$p_i = \frac{\exp(\alpha_i)}{1 + \exp(\alpha_i)}$$
(the logistic function; p. 367).

**12.2.4 No-pooling estimates (p. 367).** `p_nopool = si / ni`. These equal the estimates of a dummy-variable model with flat priors.

**12.2.5 Partial-pooling estimates (pp. 367–368).** Fit m12.3 (the same multilevel model, iter=1e4, warmup=1000, one chain). Key estimates: α (a) = 1.13 (sd 0.23); σ (sigma) = 1.59 (sd 0.22). Convert the pond intercepts with the logistic to get `p_partpool`, compute the true $p$ from `true_a`, and take absolute errors `abs(p_nopool - p_true)` and `abs(p_partpool - p_true)` (p. 368).

**Figure 12.3 (pp. 368–369).** Findings:
1. Both kinds of estimates are more accurate for larger ponds (more data).
2. The average no-pooling error (blue line) is above the partial-pooling average (dashed) in each size group.
3. The gap grows as ponds get smaller, so partial pooling suffers less from small sample size.

A reader's own plot will look different because of simulation variance; the pattern shown is the central tendency (p. 368).

**Why (pp. 369–370).** Shrinkage balances the overfitting risk of individual means against the underfitting risk of the grand mean. Small ponds hold less information, so they are pulled more toward the (underfit) grand mean. Large ponds shrink little. Where ponds are very large, pooling does little to improve their estimates but does no harm, and the information they contribute can help small ponds. This is regularization like Chapter 6, but with the amount learned from the data (p. 370).

*Intuition note.* Raw proportions from small samples jump around by chance. Pulling them toward the average removes some of that noise, at the price of fitting the sample less closely. On average the partly pooled estimates are better.

**Exceptions (p. 370).** Sometimes no-pooling is better. This often happens in ponds with extreme survival probabilities, which partial pooling shrinks because few ponds behave that way. "But sometimes outliers really are outliers."

**Overthinking: repeating the simulation (p. 370).** The compiled Stan model can be reused with new data (`map2stan(m12.3, data=newdat, ...)`), which is useful for simulation studies.

### 12.3 More than one type of cluster (pp. 370–376)
Observations in `chimpanzees` (lever pulls) belong to an `actor` (1 to 7) and to a `block` (1 to 6, a day of experiment). Each can have unique intercepts, and both can be partially pooled at once (pp. 370–371).

**Rethinking: cross-classification and hierarchy (p. 371).** Actors are not nested in blocks, so this is a *cross-classified* model. If each chimpanzee did all pulls in one block, the data would be hierarchical. The specification would typically be the same. Other software sometimes forces the two cases to be treated differently, because its conditioning engine is less capable than MCMC.

**12.3.1 Varying intercepts on actor (pp. 371–372).** Start from the full chimpanzee model of Chapter 10, with $L_i$ = pulled left, $P_i$ = prosocial option on left, $C_i$ = partner condition:
$$
\begin{aligned}
L_i &\sim \text{Binomial}(1, p_i)\\
\text{logit}(p_i) &= \alpha + \alpha_{\text{actor}[i]} + (\beta_P + \beta_{PC} C_i) P_i\\
\alpha_{\text{actor}} &\sim \text{Normal}(0, \sigma_{\text{actor}})\\
\alpha, \beta_P, \beta_{PC} &\sim \text{Normal}(0, 10)\\
\sigma_{\text{actor}} &\sim \text{HalfCauchy}(0, 1)
\end{aligned}
$$
- The mean α now sits in the linear model, not in the Gaussian prior. This is mathematically equivalent to the tadpole form, because a Gaussian equals a constant plus a zero-centred Gaussian. The author demonstrates this with `y1 <- rnorm(1e4, 10, 1)` and `y2 <- 10 + rnorm(1e4, 0, 1)`, which give the same distribution. This arises from the independence of the Gaussian's mean and standard deviation, which most distributions lack (pp. 371–372).
- Fit as m12.4 (warmup=1000, iter=5000, chains=4). `a_actor` values are deviations from `a`, so the total intercept for an actor is $\alpha + \alpha_{\text{actor}[i]}$. Added over samples, the posterior mean total intercepts for actors 1–7 are −0.71, 4.59, −1.02, −1.02, −0.71, 0.23, 1.76 (p. 372).

**12.3.2 Two cluster types (pp. 372–374).** Add a block intercept, with its own σ:
$$
\begin{aligned}
\text{logit}(p_i) &= \alpha + \alpha_{\text{actor}[i]} + \alpha_{\text{block}[i]} + (\beta_P + \beta_{PC} C_i) P_i\\
\alpha_{\text{actor}} &\sim \text{Normal}(0, \sigma_{\text{actor}}), \quad \alpha_{\text{block}} \sim \text{Normal}(0, \sigma_{\text{block}})\\
\sigma_{\text{actor}}, \sigma_{\text{block}} &\sim \text{HalfCauchy}(0, 1)
\end{aligned}
$$
(other priors as above; p. 373). Each cluster type needs its own σ. There is only one global mean α, and both varying intercepts are centred at zero, because a separate mean per cluster type cannot be identified when both are added to the same linear prediction. A practice problem explores including two grand means (p. 373). The block column is renamed `block_id` because `block` is reserved by Stan. The fit (m12.5, 20,000 samples from 4 chains) may produce a warning about divergent iterations (3 here), which the author says is safe to ignore for now; inspect n_eff and Rhat (pp. 373–374).

**Estimates (p. 374).** Selected rows (mean, sd): `a_actor[2]` 4.14 (1.59); `a_actor[1]` −1.17 (0.93); `a_actor[7]` 1.32 (0.96); `a_block[1..6]` between −0.18 and 0.11, sd 0.18–0.22; α 0.46 (0.92); bp 0.82 (0.26); bpc −0.13 (0.30); sigma_actor 2.25 (0.90); sigma_block 0.22 (0.18). All Rhat = 1.
- n_eff varies a lot (e.g. 2079 for sigma_block, 9532 for a_block[4]). A common cause is a parameter spending much time near a boundary; here `sigma_block` is near its minimum of zero (p. 374).
- Estimated variation among actors is much larger than among blocks (Figure 12.4). The model is confident that actors vary more than blocks, though there is uncertainty about actor variation (pp. 374–375).

**WAIC (p. 375).**

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m12.4 | 531.5 | 8.1 | 0.0 | 0.65 | 19.50 | NA |
| m12.5 | 532.7 | 10.5 | 1.2 | 0.35 | 19.74 | 1.94 |

m12.5 has 7 more parameters but only about 2.5 more effective parameters, because `sigma_block` is near zero and strongly shrinks the 6 block intercepts. The actor intercepts shrink much less, so each contributes more to pWAIC. The WAIC difference (1.2) is small relative to its standard error (1.94), so the two models predict nearly identically (p. 375). The author advises against "selecting" m12.4. Whether block is included hardly matters, and retaining and reporting both is more informative (p. 376).

*Intuition note.* A cluster type with almost no real variation gets a σ near zero. Its intercepts are then squeezed to about zero, so including it costs little overfitting.

**12.3.3 Even more clusters (p. 376).** More cluster types are added the same way. Hamiltonian Monte Carlo can handle tens of thousands of varying effects, though sampling is slow. If there is a theoretical reason to include a cluster variable, there is reason to partially pool it. The σ of each cluster can be thought of as a crude measure of that cluster's relevance for explaining variation in the outcome.

### 12.4 Multilevel posterior predictions (pp. 376–384)
Posterior predictions help check software, understand models ("every model is a merger of sense and nonsense", p. 376), and compute information criteria. Two nuances for multilevel models (p. 376):
- We should not expect even a good fit to retrodict the raw sample exactly, because shrinkage deliberately trades some in-sample fit for better inference.
- "Prediction" requires a choice: predict for the clusters in the sample, or for new clusters.

**12.4.1 Same clusters (pp. 377–378).** Varying intercepts are just parameters, and the only care needed is to use the right intercept for each case; `link` and `sim` do this automatically. `post$a_actor` is a matrix with shape (8000 samples × 7 actors); `post$a_actor[,5]` means all samples for actor 5. A manual link function computes
$$\text{logistic}\big(a + a_{\text{actor}}[,\text{actor}] + (bp + bpC \cdot \text{condition}) \cdot \text{prosoc\_left}\big)$$
for the 4 treatment combinations (prosoc_left = 0,1,0,1; condition = 0,0,1,1) (pp. 377–378). Bayesian models are generative, so predictions are made by pushing posterior samples up through the model and summarizing the resulting distributions (p. 378).

**12.4.2 New clusters (pp. 378–381).** For new chimpanzees, individual intercepts are not of interest, but their distribution is. Think of leaving actor 7 out of the fit: `a_actor` estimates are useless, but `a` and `sigma_actor` describe the population (p. 378). Three ways to show predictions (Figure 12.5, p. 380):
1. **Average actor** (left panel): replace `a_actor` samples by zeros, a matrix of shape 1000×7, via `link(..., replace=list(a_actor=a_actor_zeros))`. This gives the effect of treatment and uncertainty in the mean, but the uncertainty is much smaller than honest uncertainty about a new individual, and it ignores variation among actors (pp. 378–380).
2. **Marginal of actor** (middle): simulate `a_actor_sims <- matrix(rnorm(7000, 0, post$sigma_actor), 1000, 7)` from the model's prior $\alpha_{\text{actor}} \sim \text{Normal}(0, \sigma_{\text{actor}})$ and pass it with `replace`. This averages over variation among actors (pp. 379–380).
3. **Simulated actors** (right): `sim.actor(i)` draws one new intercept using `sigma_actor[i]` and computes $p$ for the four treatments with the i-th posterior sample. Plot 50 lines. This shows both the zig-zag effect of `prosoc_left` and variation among actors (p. 381).

Which of 1–2 to use "depends" on the question: average-actor predictions show treatment impact, and marginal predictions show how variable chimpanzees are. Compute both to understand a model (p. 380). Because the model is binomial, parameters interact through ceiling and floor effects: actors with very large intercepts (strong handedness preference) show little treatment effect, while actors with intercepts near the mean are influenced by treatment (p. 381).

**12.4.3 Focus and multilevel prediction (pp. 381–384).** *Focus* is the level of the model whose parameters make direct predictions. Three cases (p. 382):
1. *Retrodicting the sample:* the hyperparameters (α, σ_actor) do not influence prediction directly and had their effects during estimation, by shrinking; focus is on the top level.
2. *Forecasting for a cluster in the sample* (e.g. chimpanzee 2, whose intercept was very large, so she will probably pull left): again the top level.
3. *Forecasting for a new cluster* (new individual, school, year, location): we need the hyperparameters to generate new intercepts. This is also the right approach when varying effects model over-dispersion.

**Over-dispersed Poisson example** (Oceanic societies, `Kline` data; p. 382). A varying intercept is given to every observation (society):
$$
\begin{aligned}
T_i &\sim \text{Poisson}(\mu_i)\\
\log(\mu_i) &= \alpha + \alpha_{\text{society}[i]} + \beta_P \log P_i\\
\alpha &\sim \text{Normal}(0, 10),\quad \beta_P \sim \text{Normal}(0, 1)\\
\alpha_{\text{society}} &\sim \text{Normal}(0, \sigma_{\text{society}}),\quad \sigma_{\text{society}} \sim \text{HalfCauchy}(0, 1)
\end{aligned}
$$
- $T$ is `total_tools` and $P$ is `population`. σ_society estimates over-dispersion; the intercepts are residuals, and their distribution estimates the excess variation relative to the Poisson expectation (p. 382).
- Fitted as m12.6 (iter=4000, chains=3). It has 13 parameters for 10 observations, but WAIC "should" show about 5 effective parameters. With hundreds of observations you get hundreds of intercepts; you care about the hyperparameters, not the individual estimates (p. 383).
- `postcheck(m12.6)` uses `a_society` directly, not the hyperparameters. To see the general trend, simulate counterfactual societies: `a_society_sims` is a matrix of shape 2000×10 drawn from Normal(0, `sigma_society`), passed to `link` with `replace`. The envelope (67%, 89%, 97% intervals, Figure 12.6) is much wider than in Chapter 10, as a result of the varying intercepts combined with more variation in the data than a pure Poisson model expects (pp. 383–384).

### 12.5 Summary (p. 384)
Varying intercepts give better estimates of baseline differences among clusters, because they model the population of clusters and use it to pool information. They are adaptively regularized parameters with a prior learned from the data.

### 12.6 Practice (pp. 384–386)
Problems only (see Exercises). 12H1 begins with a data-prep step: make cluster indices contiguous integers (`as.integer(as.factor(d$district))`), because district 54 is absent from the data (p. 386).

## Toy example
*Ours, not from the text.* It is a Gaussian analogue of the robot's café problem. Unlike the chapter's models, it treats the population mean and sd as known so the arithmetic can be done by hand. In the chapter they are learned from the data.

Setup: the population of cafés has mean $\mu = 6$ min and sd $\tau = 1$. Each visit's waiting time has noise sd $s = 2$ around the café's true mean. For a café with $n$ visits and sample mean $\bar y$, the precision-weighted estimate is
$$\hat\theta = w\,\bar y + (1-w)\,\mu,\qquad w = \frac{n/s^2}{n/s^2 + 1/\tau^2}.$$
(This is the standard normal–normal combination of two sources; the chapter does not give this formula.)

| café | n | ȳ | n/s² | w | estimate | shift from raw |
|---|---|---|---|---|---|---|
| A | 1 | 4 | 1/4 = 0.25 | 0.25/(0.25+1) = 0.2 | 0.2·4 + 0.8·6 = 0.8 + 4.8 = 5.6 | 1.6 |
| B | 16 | 8 | 16/4 = 4 | 4/(4+1) = 0.8 | 0.8·8 + 0.2·6 = 6.4 + 1.2 = 7.6 | 0.4 |
| C | 1 | 5.5 | 0.25 | 0.2 | 0.2·5.5 + 0.8·6 = 1.1 + 4.8 = 5.9 | 0.4 |

Reading: A and C each have one visit, and both shrink strongly toward 6 (weight 0.2 on their own data). B has many visits, so it keeps weight 0.8 and is shifted little. A is farther from 6 than C, so A moves more (1.6 vs 0.4). These match the three observations of Figure 12.1: more shrinkage for small clusters and for clusters far from the mean.

## Concepts
- [[hierarchical-multilevel-model]] — parameters for clusters are drawn from a population distribution whose parameters are also learned (pp. 356, 359)
- [[partial-pooling-shrinkage]] — cluster estimates are pulled toward the population mean; more for small or extreme clusters (p. 362)
- [[varying-intercepts]] (new) — one intercept per cluster, with an adaptive prior shared by all (p. 358)
- [[hyperparameter]] (new) — a parameter of a prior on parameters, such as α and σ for tank intercepts; its prior is a hyperprior (p. 359)
- [[complete-pooling-no-pooling]] (new) — complete pooling uses one shared estimate and underfits; no pooling treats clusters as independent and overfits (pp. 364–365)
- [[cluster-variable]] (new) — a variable identifying groups of repeated observations, e.g. tank, pond, actor, block (pp. 357–358)
- [[cross-classified-model]] (new) — observations belong to two or more cluster types that are not nested (p. 371)
- [[effective-number-of-parameters]] (new) — pWAIC; how flexible the fit is, fewer than actual parameters under shrinkage (pp. 360, 375)
- [[over-dispersion]] (new) — more variation than a binomial or Poisson model expects; a varying intercept per observation can model it (pp. 363, 382)
- [[prediction-focus]] (new) — which model level makes direct predictions: top-level parameters for observed clusters, hyperparameters for new clusters (pp. 381–382)
- [[markov-chain-monte-carlo]] — used here because MAP cannot average over the second level (p. 360)
- [[convergence-diagnostics]] — n_eff, Rhat and divergent iterations are checked for the more complex models (pp. 373–374)
- [[cross-validation-loo-waic]] — WAIC and pWAIC compare the multilevel and fixed models (pp. 360, 375)
- [[principle-of-indifference-maximum-entropy]] — Gaussian cluster distribution and exponential σ prior justified by maximum entropy (pp. 359, 364)
- [[hamiltonian-monte-carlo-nuts]] — said to handle tens of thousands of varying effects (p. 376)
- [[posterior-predictive-distribution]] — retrodiction versus predictions for new clusters by simulating intercepts (pp. 376–381)

## Canonical instances
- [[coffee-robot-cafes]] — a robot learns waiting times for each café and for the population of cafés (pp. 355–356)
- [[reed-frog-tadpoles]] — 48 tanks, multilevel binomial model, shrinkage and WAIC (pp. 357–362)
- [[simulated-ponds]] — simulated data with known truth showing partial pooling beats no pooling (pp. 365–370)
- [[chimpanzees-actor-block]] — cross-classified varying intercepts on actor and block, and posterior predictions for new actors (pp. 370–381)
- [[oceanic-societies-overdispersion]] — Poisson model with an intercept per society to model over-dispersion (pp. 382–384)
- [[clive-wearing-amnesia]] — metaphor for models that forget earlier clusters (p. 355)

## Bridges (candidates)
- [structural-analogy] Shrinkage toward the population mean with learned strength ↔ ridge/L2 penalized regression: a Gaussian prior acts like a penalty. Here the penalty strength σ is estimated, not tuned.
- [structural-analogy] Partial pooling ↔ bias–variance trade-off in estimation: the pooled estimate adds bias but cuts variance, most for noisy small clusters.
- [structural-analogy] Varying intercept on every observation ↔ over-dispersed count models (beta-binomial, gamma-Poisson): the text says both allow over-dispersion; whether the math is identical is not claimed.
- [metaphor] Anterograde amnesia versus remembering ↔ cognitive science: independent per-category learning versus learning an abstract population prior.

## Questions this raises
- How does the amount of shrinkage depend on cluster size and on σ in a formula, rather than only in pictures?
- When many clusters have σ near zero or few clusters exist, how reliable is the learned prior, and how sensitive is inference to the half-Cauchy versus exponential choice?
- What changes when slopes, not only intercepts, vary by cluster (the next chapter)?
- How should a report choose between average-actor and marginal predictions?

## Exercises worth doing
- Ex. 12E1 (p. 384) — shrinkage depends on how narrow the prior is — easy
- Ex. 12E5 (p. 385) — write a cross-classified Poisson model — easy
- Ex. 12M1 (p. 385) — how inferred tank variation changes when predictors enter the model — medium
- Ex. 12M3 (p. 385) — replace the Gaussian with a Cauchy for varying intercepts and compare estimates — medium
- Ex. 12M4 (p. 385) — separate means α and γ for two cluster types and compare with the chapter model and n_eff — medium
- Ex. 12H1 (p. 386) — fixed versus varying intercepts for Bangladesh districts, and explaining the disagreements — hard

## Reading notes
- Printed page = pdf − 14 (pdf 369 = printed 355).
- The text of 12H1 prints "By the year 200"; presumably 2000 is meant (my inference).
- The text on p. 368 names the column `p.partpool`, but the code uses `p_partpool`. Chimp code uses `bpC` in m12.4 and `bpc` in m12.5.
- On p. 376 the standard error of the WAIC difference (1.94) is said to be "twice as large as the difference itself", but 1.94/1.2 is about 1.6.
- The Figure 12.1 caption and text call the dividing lines "vertical gray lines"/"vertical lines"; in the image they are black. This does not affect the content.
- Code is from the `rethinking` package (map2stan era); no code was run here. Equations were read from the page images and checked.

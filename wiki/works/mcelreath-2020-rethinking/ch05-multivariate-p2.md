---
id: mcelreath-2020-rethinking/ch05-multivariate-p2
work: mcelreath-2020-rethinking
unit: "Chapter 5. Multivariate Linear Models (part 2/2): Overthinking box on masking relationships, 5.3 When adding variables hurts, 5.4 Categorical variables, 5.5 OLS and lm, 5.6 Summary, 5.7 Practice"
pages: 141-164
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
# Multicollinearity, post-treatment bias, categorical predictors and lm

## L0 — One line
Adding predictors can hurt: nearly redundant predictors give a wide, uninformative posterior for each slope, and controlling for a consequence of the treatment can hide a real effect.

## L1 — The gist (≤ 120 words)
When should you not add a predictor to a regression, and how do categories enter a model? Two nearly redundant predictors (multicollinearity) produce wide posteriors for each slope, although the model is correctly saying the data cannot separate them. Controlling for a consequence of a treatment (post-treatment bias) can hide a real treatment effect. Categories enter through dummy variables (0/1 indicator columns) (k − 1 for k categories) or through one intercept per category. A difference between groups needs its own posterior, computed from posterior samples (a contrast). The unit ends by relating `lm` (ordinary least squares, OLS: minimise squared residuals; flat priors) and design formulas (compact notation such as `y ~ 1 + x`) to `map`-style models.

**Prerequisites:** Gaussian linear regression; posterior samples and percentile intervals; the chapter's earlier idea that a multiple regression coefficient measures the value of a predictor given the other predictors.

## L2 — Key ideas (5–10 bullets)
- A multiple regression asks: what is the value of knowing each predictor after knowing the others? Two almost identical predictors therefore each add little once the other is known, and the model reports this honestly (pp. 143, 148).
- With near-duplicate predictors the likelihood behaves approximately as if it depended only on the sum of the slopes. The posterior is a narrow ridge of (β₁, β₂) pairs, and the sum is well estimated (pp. 143–144).
- Real data show the same effect. Percent fat and percent lactose (r ≈ −0.94) are each strong bivariate predictors of milk energy, but both weaken in one model (pp. 146–148).
- Posterior sd inflates slowly at first and then very rapidly as predictor correlation approaches 1. Checking pairs plots and sd inflation helps, but correlation alone cannot tell you (pp. 148–149).
- Controlling for a post-treatment variable (fungus) removes the treatment's effect from view. Model comparison cannot detect this, because that model predicts better (pp. 150–152).
- Dummy variables switch parameters on or off by category; k categories need k − 1 dummies. Group means and contrasts are obtained by adding or subtracting posterior samples (pp. 153–157).
- "Significant vs not significant" does not imply a significant difference. Compute the contrast itself (p. 158).
- `lm` with a design formula gives OLS estimates, equal to `map` under flat priors, but it gives no σ estimate and has quirks with factors and transforms (pp. 159–161).

## L3 — Walkthrough

### Start of this part: Overthinking box on masking relationships (p. 141)
Overthinking box: simulating a masking relationship. Code: `N <- 100`, `rho <- 0.7`, `x_pos <- rnorm(N)`, `x_neg <- rnorm(N, rho*x_pos, sqrt(1-rho^2))`, `y <- rnorm(N, x_pos - x_neg)` (p. 141). Here y rises with x_pos and falls with x_neg, and the predictors are positively correlated.
- Two bivariate regressions underestimate the true associations (about 1 and −1). The model with both predictors recovers them better (p. 141).
- Masking weakens as `rho` → 0 and grows as `rho` → ±1. If `rho` gets very close to ±1, the predictors hold the same information and no model can separate them (p. 141).
- The author lists possible reasons for such correlation: a shared unmeasured cause, one predictor partly caused by the other, or reciprocal causation (p. 141). The lifespan/learning story for body size and neocortex in primates is explicitly speculative (p. 141).

**Intuition note.** If two predictors push the outcome in opposite directions and move together, each hides the other. Including both lets the model separate them, provided they are not too tightly correlated.

### 5.3 When adding variables hurts (pp. 141–142)
The author names three purely statistical reasons not to add every available predictor (p. 141):
1. **Multicollinearity**: very strong correlation between two or more predictors.
2. **Post-treatment bias**: statistically controlling for consequences of a causal factor.
3. **Overfitting**: deferred to the next chapter.

Consequence of multicollinearity: the posterior says a very large range of parameter values is plausible, from tiny to massive associations, even if all variables are really strongly associated with the outcome (pp. 141–142).

### 5.3.1 Multicollinear legs (pp. 142–145)
**Simulation** (p. 142), for N = 100 individuals:
- height ~ Normal(10, 2);
- leg proportion ~ Uniform(0.4, 0.5);
- each leg = proportion × height + Normal(0, 0.02) error.

**Expectation.** Legs are on average 45% of height, so a leg slope should be about 10/4.5 ≈ 2.2 (p. 142).

**Model m5.8** (p. 142):
$$h_i \sim \text{Normal}(\mu_i,\sigma),\quad \mu_i = a + b_l\,\text{leg\_left}_i + b_r\,\text{leg\_right}_i$$
Priors: a ~ Normal(10, 100); b_l, b_r ~ Normal(2, 10); σ ~ Uniform(0, 10).

| param | mean | sd | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 0.70 | 0.31 | 0.20 | 1.20 |
| bl | −0.43 | 2.18 | −3.92 | 3.06 |
| br | 2.48 | 2.19 | −1.01 | 5.98 |
| sigma | 0.62 | 0.04 | 0.55 | 0.69 |

- The fit is correct. The posterior answers the question asked: what is the value of knowing each leg's length after already knowing the other leg's length? (p. 143)
- The joint posterior of (bl, br) is a narrow negatively sloping ridge: when bl is large, br must be small (p. 143, Fig. 5.8 left). Practically infinitely many combinations give the same predictions (p. 143).

**Why.** With one x used twice, the likelihood is rewritten (p. 144):
$$\mu_i=\alpha+\beta_1x_i+\beta_2x_i=\alpha+(\beta_1+\beta_2)x_i$$
Only the sum β₁ + β₂ influences μ, so β₁ and β₂ cannot be pulled apart (p. 144). The legs are almost the same variable, so this is approximately the situation here.

**Check:** `sum_blbr <- post$bl + post$br` has posterior mean a little over 2 and a much smaller sd than bl or br (p. 144, Fig. 5.8 right). A model with one leg only (m5.9) gives bl = 2.05, sd 0.07, interval [1.94, 2.16] (p. 145).

**Intuition note.** The posterior is not wrong. It says the data cannot tell the legs apart, which is a valid answer. For pure prediction the two-leg model is fine, but it makes no claim about which leg matters (p. 145).

### 5.3.2 Multicollinear milk (pp. 145–150)
Data: primate `milk`; outcome `kcal.per.g`; predictors `perc.fat` and `perc.lactose` (no missing values) (p. 145).

**Bivariate fits** (priors a ~ Normal(0.6, 10), slope ~ Normal(0, 1), σ ~ Uniform(0, 10)) (pp. 145–146):
- m5.10: bf = 0.010, sd 0.001, 89% interval [0.008, 0.012].
- m5.11: bl = −0.011, sd 0.001, [−0.012, −0.009].

These are essentially mirror images, each narrow and lying almost entirely on one side of zero (p. 146). The slopes look small but the predictors are percents. The influence on prediction is the product of parameter and data, so plot predictions rather than trust slope size (p. 146).

**Both predictors, m5.12** (p. 147): a = 1.007 (sd 0.200); bf = 0.002 (sd 0.002, [−0.002, 0.006]); bl = −0.009 (sd 0.002, [−0.013, −0.005]); σ = 0.061.
- Both means move toward zero and the sds are about twice those of the bivariate fits. The bf mean is essentially zero (p. 147).
- Reason: the variables are substitutes and form essentially one axis of variation (Fig. 5.9, p. 147). The posterior is a long ridge of equally plausible (bf, bl) combinations (p. 147).
- `cor(perc.fat, perc.lactose)` = −0.9416373 (p. 148).

**How strong is too strong?** No easy answer. What matters is the correlation that remains after accounting for the other predictors, not only the pairwise one (p. 148).

**Simulation experiment** (pp. 148–149, Fig. 5.10): make a fake predictor x correlated with perc.fat at a chosen level, regress kcal.per.g on both, and record the sd of the perc.fat slope. Average over 100 regressions per correlation level.
- The sd grows with correlation, but not linearly. Above a correlation of 0.9 it rises very rapidly, approaching ∞ as the correlation approaches 1 (p. 148).
- The code is in an Overthinking box (p. 150). It uses `lm`, so implicit flat priors, which exaggerate the effect. With informative priors the inflation can be much slower (p. 150).

**What to do** (p. 148–149):
- Be aware. Check predictors against each other in a pairs plot. Pairs or clusters correlated over about 0.9 may be problematic as main effects in one model (p. 148).
- Highly correlated variables are not always fully redundant. Other predictors correlated with only one of them can help extract each one's unique information. So a correlation table cannot tell you in advance, but a big sd inflation when both are included usually diagnoses the problem (pp. 148–149).
- Conventions differ. Some fields use data reduction (principal components, factor analysis) and use the components as predictors. Others consider this "voodoo", because components are hard to interpret, involve hidden decisions, and do not translate directly into a real measurement's association (p. 149).
- A defensive approach: show that models using any one member of a correlated cluster give the same inferences and predictions (rainfall vs soil moisture example) (p. 149).

**Non-identifiability** (p. 149). Multicollinearity belongs to a family of problems where data and model structure make it impossible to estimate a parameter. It sometimes comes from coding mistakes, but many important models have non-identifiable or weakly identifiable parameters even when coded correctly. If data hold little information, the posterior will be very wide. This is the right answer to the question asked, though it may prompt a better question. Check parameter covariation, especially when intervals are very wide (p. 149).

Rethinking box (p. 150): technically, identifiability is not a concern for Bayesian models. If the posterior is proper (integrates to 1), all parameters are identified. That does not make the posterior easy to understand, so "weakly identified" is the better term.

**Intuition note.** Two predictors that carry the same information leave the model unable to split the credit between them. Wide intervals here are an honest "I can't tell", not a sign of a bug.

### 5.3.3 Post-treatment bias (pp. 150–152)
- **Omitted variable bias**: mistaken inference from leaving out predictors; the earlier chapter's examples illustrate it. **Post-treatment bias**: mistaken inference from including variables that are consequences of other variables. The second is less routinely worried about (p. 150). It also applies to observational studies (p. 150).
- **Example** (p. 150): greenhouse plants, initial height, then antifungal soil treatments, then final height and fungus presence. Fungus reduces growth. For a causal inference about the treatment, fungus should not be included, because it is a post-treatment effect.

**Simulation** (p. 151), N = 100:
- h0 ~ Normal(10, 2);
- treatment = 0 for the first 50 plants and 1 for the last 50;
- fungus ~ Binomial(1, prob = 0.5 − 0.4·treatment);
- h1 = h0 + Normal(5 − 3·fungus, 1).

**m5.13** (h1 on h0, treatment, fungus; priors a ~ Normal(0, 100), slopes ~ Normal(0, 10), σ ~ Uniform(0, 10)) (p. 151): a = 5.05; bh = 1.00 (0.05); bt = −0.27 (sd 0.22, [−0.61, 0.08]); bf = −3.29 (0.25); σ = 0.95.
- The treatment effect looks negative or near zero. The author says it mainly had very little effect (p. 151).
- Why: fungus is mostly a consequence of treatment. Controlling for fungus asks: once we know whether a plant developed fungus, does soil treatment matter? The answer is "no", because treatment acts on growth through reducing fungus (pp. 151–152).

**m5.14** (omit fungus) (p. 152): a = 4.19; bh = 0.94 (0.08); bt = 1.07 (sd 0.31, [0.57, 1.57]); σ = 1.56. The treatment effect is now strong and positive.
- Controlling for pre-treatment differences like h0 is sensible. Including post-treatment variables can mask the treatment (p. 152).
- That fungus shrinks bt suggests the treatment works for the expected reason, but a correct inference about the treatment still needs fungus omitted (p. 152).
- In experiments pre- and post-treatment variables are easy to tell apart. In observational studies it is harder (p. 152).

Rethinking box (p. 152): model comparison does not help here. The model with fungus fits the sample better and would predict better out of sample. It misleads because it asks the wrong question, and no statistical procedure substitutes for scientific knowledge.

**Intuition note.** If the treatment works only by way of fungus, then "holding fungus fixed" leaves nothing for the treatment to do. The question changes, even though the model fits well.

### 5.4 Categorical variables (pp. 152–153)
A categorical variable has unordered categories (ape vs monkey; sex; developmental status; region). Such variables, often called factors, are routinely put in linear models. The author exposes the machinery because interpreting their estimates can be harder than for continuous variables (p. 153).

### 5.4.1 Binary categories (pp. 153–154)
Data `Howell1`, 544 observations; `male` is a **dummy variable** (1 if male, 0 if female). It does not matter which category gets the 1, but you must remember it (p. 153). The dummy turns a parameter on for one category and off for the other (p. 153).

Model (p. 153):
$$h_i\sim\text{Normal}(\mu_i,\sigma),\quad \mu_i=\alpha+\beta_m m_i$$
$$\alpha\sim\text{Normal}(178,100),\quad \beta_m\sim\text{Normal}(0,10),\quad \sigma\sim\text{Uniform}(0,50)$$
When $m_i=0$, $\beta_m$ is multiplied by zero and has no effect (p. 153).

**m5.15** (p. 154): a = 134.84 (sd 1.59), bm = 7.27 (sd 2.28, [3.62, 10.92]), σ = 27.31 (0.83).
- Since $m_i=0$ gives $\mu_i=\alpha+\beta_m(0)=\alpha$, α is the average female height (about 135 cm). βm is the average male–female difference (7.3 cm). Average male height is 135 + 7.3 = 142.3 (p. 154).
- α and βm are correlated, so you cannot just add interval boundaries. Instead sum the samples: `mu.male <- post$a + post$bm; PI(mu.male)` gives 5% = 139.3947, 94% = 144.7834 (p. 154). Working with samples handles the correlation whatever it is (p. 154).

**Overthinking: re-parameterizing** (pp. 154–155). Use one parameter per sex:
$$\mu_i=\alpha_f(1-m_i)+\alpha_m m_i$$
Plugging in $m_i=0$ and $m_i=1$ shows only one of αf, αm is on for any case. Rearranged (p. 155):
$$\mu_i=\alpha_f+(\alpha_m-\alpha_f)m_i$$
So the earlier βm is $\alpha_m-\alpha_f$. The two fits are inferentially equivalent; the author leaves confirming this fit (m5.15b) to the reader (p. 155).

### 5.4.2 Many categories (pp. 155–158)
**Rule:** k categories need k − 1 dummy variables. Each dummy marks one category with 1. The category without a dummy is the "intercept" category (p. 155).

Example: `clade` has four levels (Ape, New World Monkey, Old World Monkey, Strepsirrhine). Dummies are made with `ifelse`, e.g. `clade.NWM` (pp. 155–156). Ape is the default. Adding an ape dummy would make the model non-identifiable (p. 156); the text asks the reader to find out why.

Model (p. 156):
$$k_i\sim\text{Normal}(\mu_i,\sigma),\quad \mu_i=\alpha+\beta_{NWM}NWM_i+\beta_{OWM}OWM_i+\beta_S S_i$$
Priors: α ~ Normal(0.6, 10); each β ~ Normal(0, 1); σ ~ Uniform(0, 10).

This defines four linear models (p. 156):

| Category | NWM | OWM | S | μ |
|---|---|---|---|---|
| Ape | 0 | 0 | 0 | α |
| New World monkey | 1 | 0 | 0 | α + β_NWM |
| Old World monkey | 0 | 1 | 0 | α + β_OWM |
| Strepsirrhine | 0 | 0 | 1 | α + β_S |

**m5.16** (p. 156): a = 0.55 (0.04); b.NWM = 0.17 (0.05); b.OWM = 0.24 (0.06); b.S = −0.04 (0.06); σ = 0.11 (0.02).

Category means by summing samples (p. 157): mu.ape = post$a, mu.NWM = a + b.NWM, and so on. Results (89% intervals): ape 0.55 [0.49, 0.61]; NWM 0.71 [0.65, 0.77]; OWM 0.79 [0.71, 0.86]; S 0.51 [0.43, 0.59].

**Contrast.** Re-parameterizing after fitting is possible. For NWM − OWM, `quantile(mu.NWM - mu.OWM, c(0.025, 0.5, 0.975))` gives −0.190, −0.0737, 0.0474 (p. 157). No posterior uncertainty is discarded.

**Rethinking: differences and significance** (pp. 157–158). It is an error to think that, because one parameter is "significant" and another is not, their difference is significant. To learn about a difference you must compute it.
- Example: βf = 0.15 ± 0.02, βm = 0.02 ± 0.10. If uncorrelated, the difference is $(0.15-0.02)\pm\sqrt{0.02^2+0.1^2}\approx0.13\pm0.10$, which overlaps a lot with zero (p. 158).
- You can be confident βf is far from zero but not that βf − βm is (p. 158).
- Underneath lies the mistake of accepting the null: treating "not significantly different from zero" as "no effect". The author calls this illogical and extremely common (p. 158).

**Intuition note.** A group's mean is "intercept + its offset", and uncertainty travels with the samples. A difference between two groups needs its own posterior, not a comparison of two separate intervals.

### 5.4.3 Adding regular predictors (p. 158)
Add them to the mean, e.g. $\mu_i=\alpha+\beta_{NWM}NWM_i+\beta_{OWM}OWM_i+\beta_S S_i+\beta_F F_i$, with $F_i$ the percent fat. Dummies can also make slopes differ by category; this is deferred to the interactions chapter (p. 158).

### 5.4.4 Unique intercepts (pp. 158–159)
Alternative: one intercept per category with an **index variable** (`coerce_index(d$clade)` gives values 1–4; the order is arbitrary because categories are unordered) (p. 158). Model m5.16_alt (p. 159):
$$\mu_i=a_{\text{clade\_id}[i]},\quad a_{[j]}\sim\text{Normal}(0.6,10),\quad \sigma\sim\text{Uniform}(0,10)$$
`precis(..., depth=2)` is needed to show vector parameters. Estimates a[1]–a[4] are 0.55, 0.71, 0.79, 0.51 (sds 0.04, 0.04, 0.05, 0.05), the same averages as before (p. 159). The author says this approach is common in multilevel models (Chapter 12) (p. 158).

### 5.5 Ordinary least squares and lm (pp. 159–162)
**OLS** estimates a linear regression by minimising the sum of squared residuals instead of maximising the posterior. It is often functionally equivalent to maximising the posterior or likelihood. The text states that Gauss invented OLS as a method for computing Bayesian MAP estimates (p. 159). With flat priors, `lm` gives the same estimates as `map` (p. 159). `lm` is a convenience only when flat priors are acceptable; the next chapter gives reasons to doubt flat priors (p. 159).

**5.5.1 Design formulas** (pp. 159–160). They keep the predictor names of μᵢ, separated by `+`, and drop the parameters. They are sufficient to describe a model's design provided all priors are flat. Examples: `y ~ 1 + x` for $\mu_i=\alpha+\beta x_i$; `y ~ 1 + x + z + w` for $\mu_i=\alpha+\beta_xx_i+\beta_zz_i+\beta_ww_i$ (p. 160). The leading `1` is the intercept.

**5.5.2 Using lm** (pp. 160–161): `lm(y ~ 1 + x, data=d)`. Quirks:
- *Intercepts are optional*: `y ~ x` equals `y ~ 1 + x`. Without an intercept (α = 0) use `y ~ 0 + x` or `y ~ x - 1` (p. 160).
- *Categorical variables*: `lm` expands factors into dummies, but a numeric code like season 1–4 could be categories or continuous. Use `as.factor(season)`, or make dummies yourself to control which category is the intercept (pp. 160–161).
- *Transform first*: make new variables (`d$x2 <- d$x^2`) and use them. `I(x^2)` also works in `lm`, but `I()` cannot be used inside `map` (p. 161).
- *No estimate for σ*: `lm` reports a "residual standard error", a slightly different estimate with no uncertainty information. For full prediction intervals, or informative priors, fall back on `map` (p. 161).

**5.5.3 glimmer** (p. 162): `glimmer(dist ~ speed, data=cars)` returns a `map`-style `alist` with default priors: Intercept ~ dnorm(0, 10), b_speed ~ dnorm(0, 10), sigma ~ dcauchy(0, 2). These can be changed or removed.

### 5.6 Summary (p. 162)
Multiple regression builds descriptive models of how the mean relates to more than one predictor. Its defining question is: what is the value of knowing each predictor once we already know the others? This implies (1) a focus on describing the sample, not forecasting a future sample, and (2) an assumption that each predictor's value does not depend on the others' values. The next two chapters address these.

### 5.7 Practice (pp. 162–164)
Easy 5E1–5E4, Medium 5M1–5M5, Hard 5H1–5H3 (foxes data: group, avgfood, groupsize, area, weight). No solutions are printed.

## Toy example (ours, not from the text)
**A. Collinearity.** Let $x=1,2,3$ and $y=2,4,6$, and fit $\mu=\beta_1x+\beta_2x$ with α = 0 (the same x entered twice).
- $(\beta_1,\beta_2)=(2,0)$: $\mu=(2+0)\cdot(1,2,3)=2,4,6$.
- $(1,1)$: $(1+1)\cdot(1,2,3)=2,4,6$.
- $(3,-1)$: $(3-1)\cdot(1,2,3)=2,4,6$.
- $(0,2)$: $\mu=2,4,6$.

All pairs with sum 2 fit equally well. The data fix only $\beta_1+\beta_2=2$, which is why the posterior is a ridge.

**B. Post-treatment.** Use the text's simulation rules (p. 151) and their expected values. Growth is $5-3F$ (F = fungus), and $P(F=1)=0.5$ for treatment 0 and $0.1$ for treatment 1.
- Expected growth, treatment 0: $5-3(0.5)=3.5$.
- Expected growth, treatment 1: $5-3(0.1)=4.7$.
- Total treatment effect: $4.7-3.5=1.2$. (The fitted bt in m5.14 is 1.07, close given sampling noise.)
- Holding fungus fixed: growth is $5-3F$ whatever the treatment, so the difference is $0$. That is why m5.13 shows bt near zero.

## Concepts
- [[multicollinearity]] (new) — very strong correlation between predictors, which makes the posterior for each slope very wide (p. 141).
- [[non-identifiability]] (new) — data and model structure do not permit estimating a parameter; in Bayesian terms, "weakly identified" parameters (pp. 149–150).
- [[post-treatment-bias]] (new) — error from controlling for a consequence of the treatment (p. 150).
- [[omitted-variable-bias]] (new) — error from leaving out a predictor (p. 150).
- [[masked-relationship]] (new) — two predictors with opposite effects on the outcome and positive correlation hide each other in bivariate fits (p. 141).
- [[dummy-variable]] (new) — a 0/1 variable that switches a parameter on for one category (p. 153).
- [[index-variable]] (new) — an integer category code selecting one intercept per category (p. 158).
- [[contrast]] (new) — the posterior of a difference between parameters, computed from samples (pp. 157–158).
- [[design-formula]] (new) — compact notation for a linear model's predictors, e.g. `y ~ 1 + x` (p. 159).
- [[ordinary-least-squares]] (new) — fitting by minimising squared residuals; here equal to flat-prior estimates (p. 159).
- [[posterior-distribution]] — here read as an honest answer to the question the model asks, even when wide (p. 143).
- [[prior-distribution]] — flat implicit priors in `lm` exaggerate collinearity's effect (pp. 150, 159).
- [[credible-interval]] — percentile intervals (PI) from sampled posteriors, e.g. for the male mean (p. 154).

## Canonical instances
- [[leg-length-multicollinearity]] (new) — simulated left/right legs predicting height; ridge posterior but well-estimated sum (pp. 142–145).
- [[milk-fat-lactose-collinearity]] (new) — fat and lactose, r = −0.94; each strong alone, both weaken together (bf near zero, bl still away from zero) (pp. 145–148).
- [[collinearity-sd-inflation-simulation]] (new) — sd of a slope inflates sharply above r ≈ 0.9 (pp. 148–149).
- [[greenhouse-fungus-post-treatment]] (new) — controlling for fungus hides the treatment effect (pp. 150–152).
- [[howell-height-by-sex]] (new) — a dummy for male; α is the female mean (pp. 153–154).
- [[milk-clade-dummies]] (new) — k − 1 dummies for four clades and posterior group means (pp. 155–157).

## Bridges (candidates)
- [structural-analogy] Post-treatment variable (fungus) ↔ causal inference: conditioning on a mediator on the path treatment → outcome blocks that path (canon "fork, chain, collider"; not stated in this unit).
- [same-math] `lm` with flat priors ↔ Bayesian inference: under flat priors and a Gaussian likelihood the OLS estimates equal the MAP estimates (p. 159).
- [structural-analogy] One intercept per category via an index ↔ hierarchical models: the unique-intercept form is the one the text says is common in multilevel models (p. 158).
- [structural-analogy] Wide posterior under collinearity ↔ non-identifiable parameters in other models: only a combination of parameters is constrained (p. 149).

## Questions this raises
- If a post-treatment variable should be left out, how do we decide in an observational study which variables are pre- or post-treatment (p. 152)?
- Why would an ape dummy added to the clade model make it non-identifiable (p. 156)? What replaces it in the index-variable form?
- How do informative priors change how fast the sd inflates with correlation (p. 150)?
- When both variables are collinear, how can we check that using either one gives the same predictions (p. 149)?

## Exercises worth doing
- Ex. 5E4 (p. 162) — which codings of four categories are inferentially equivalent (tests k − 1 dummies and the index form) — difficulty: medium
- Ex. 5M2 (p. 163) — invent a masked relationship — difficulty: medium
- Ex. 5M3 (p. 163) — reversed causal direction between divorce and marriage; design a regression to evaluate it — difficulty: hard
- Ex. 5M5 (p. 163) — outline regressions for two mechanisms linking gas price to obesity (links to post-treatment reasoning) — difficulty: hard
- Ex. 5H2 (p. 163) — fox weight on area and groupsize; why results differ from bivariate fits — difficulty: medium
- Ex. 5H3 (p. 164) — avgfood and area together shrink each other's effects; explain (collinearity) — difficulty: hard

## Reading notes
- Part starts at printed p. 141 (the last lines of the preceding text, then the full Overthinking box on masking relationships) and ends at p. 164 (end of Practice). Printed = pdf − 14.
- Footnotes 77–81 are cited in the text but their text is not on these pages; so the Gauss/MAP claim (p. 159) and the source for post-treatment bias are only as the main text states them.
- Cross-references to p. 124 (matrix box), p. 134 and Chapter 12 point outside this unit.
- Misprints visible in the source: p. 155 says the re-parameterized model is equivalent to "the original m5.13", but the original is m5.15. p. 157 says "model m5.14 such that each b parameter is a difference from apes", but that is m5.16. p. 156 reads "you'll up with"; p. 149 spells "principle components" (principal).
- p. 148 says "standard error" and then "standard deviation" for the same quantity; Fig. 5.10's caption says posterior sd.
- Simulated outputs vary from run to run (the author attributes this to simulation variance, pp. 143, 145, 151). The Overthinking code for Fig. 5.10 uses `lm`, not `map`.
- Code uses the older `map`/`precis` interface; `precis` shows 89% intervals (5.5%–94.5%).
- Page images were checked for tables and equations; the text layer was clean.

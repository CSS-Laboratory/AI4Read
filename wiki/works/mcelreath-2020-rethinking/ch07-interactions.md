---
id: mcelreath-2020-rethinking/ch07-interactions
work: mcelreath-2020-rethinking
unit: "Chapter 7. Interactions"
pages: 209–240
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Interactions: letting one slope depend on another predictor

## L0 — One line
When the effect of one predictor depends on another, make that slope itself a linear function of the other predictor; the resulting coefficients are hard to read from tables, so centre the predictors and plot predictions.

## L1 — The gist (≤ 120 words)
Earlier models gave each predictor an independent slope. Can an effect be conditional on another variable? McElreath builds a linear interaction by making a slope a linear model of a second predictor. His examples are terrain ruggedness and GDP inside and outside Africa, and tulip blooms under water and shade. A dummy variable alone cannot change a slope. Interaction coefficients change meaning, and uncertainty is hard to see in tables. Centring (subtracting the mean) helps both fitting and interpretation. Plots of posterior predictions, such as triptychs (three side-by-side panels), are the safe route. A linear interaction is symmetric: saying A's effect depends on B, or that B's effect depends on A, describes the same model.

**Prerequisites:** linear regression with a Gaussian likelihood; dummy (0/1) variables; priors and MAP fitting; sampling from a posterior; WAIC model comparison.

## L2 — Key ideas
- Data are conditional on how they entered the sample (survivor scars on manatees and bombers); the author says every inference is conditional on something (pp. 209–210).
- Interaction is conditioning on a further predictor: a slope is defined by its own linear model, with the interaction parameter measuring the dependency (pp. 210, 216–217).
- A dummy variable only shifts the mean. Recovering the reversed ruggedness slope in Africa needs an interaction term (pp. 215–216, 219).
- Once an interaction is in the model, the slope for one predictor needs several parameters plus the other predictor, so tables of estimates are hard to read (pp. 220–221).
- Anything computed from parameters has a posterior. Compute the distribution of a difference directly; the overlap of two marginal plots (each parameter's own posterior) is not a test (pp. 221–222).
- Linear interactions are symmetric. Plotting the reverse view can reveal different patterns (pp. 223–225).
- With continuous predictors, centring eases fitting and gives the intercept and main effects clear meanings. Triptych plots show how a slope changes (pp. 226, 230–234).
- Design formulas expand `x*z` into main effects plus interaction; higher-order interactions include all lower-order terms (pp. 235–236).

## L3 — Walkthrough

### Opening: conditioning (pp. 209–211)
- Manatees carry propeller scars, and returning A.W.38 bombers carry bullet holes. Intuition says to guard the damaged parts. But the evidence is conditional on survival: a manatee hit by a keel is less likely to live, and bombers hit in cockpit or engine did not return. Armouring the *undamaged* sections was the right answer for bombers (p. 209).
- Data are conditional on how they got into the sample, posteriors on the data, and inference on the model. "Every inference is conditional on something, whether we notice it or not." (p. 209)
- Linear models make each outcome $y_i$ conditional on predictors. They frequently fail to give enough conditioning when the importance of one predictor depends on another. Example: the effect of brain size on milk energy might differ by taxonomic group. Interaction lets parameters (really their posteriors) be conditional on further aspects of the data (p. 210).
- The simplest case, the linear interaction, extends the linear-modeling strategy to parameters inside the linear model. The author compares this to epicycles on epicycles: descriptive but powerful (p. 210).
- In GLMs (generalized linear models, from Chapter 9) predictors interact to some degree even if not defined that way, and each variable interacts with itself. Multilevel models are described as essentially massive interaction models, with estimates conditional on clusters (pp. 210–211).
- Chapter plan: a categorical-by-continuous interaction, then continuous-by-continuous, then higher-order interactions. In every section of the chapter, predictions are plotted averaging over parameter uncertainty (p. 211).
- *Rethinking (Wald):* Wald proved that for many types of statistical decision rules, there is a Bayesian rule at least as good as any non-Bayesian one. He started from non-Bayesian premises (p. 211).

### 7.1 Building an interaction (pp. 211–222)
**Data.** `rugged`: each row is a country. `rugged` is a Terrain Ruggedness Index. The outcome is $\log$ of real GDP per capita in 2000. The log is used because wealth is roughly exponentially related to what increases it; the log gives an evenly spaced scale of magnitudes (p. 212).

**Puzzle.** Separate regressions give a *positive* slope of log-GDP on ruggedness inside Africa and a *negative* slope outside (Fig. 7.2, p. 212). Models `m7.1` (Africa) and `m7.2` (non-Africa) use priors $\alpha\sim\text{Normal}(8,100)$, $\beta_R\sim\text{Normal}(0,1)$, $\sigma\sim\text{Uniform}(0,10)$ (pp. 212–213).

**Tentative causal story.** Outside Africa, ruggedness plausibly hampers transport and markets. Within Africa, *if the relationship is at all causal*, rugged regions may have been protected from the large-scale slave trades, because slavers preferred to raid easily accessed settlements. The author says GDP has many influences and it is hard to be sure (p. 213).

**Why not split the data.** Four reasons (pp. 213–214):
1. Parameters like $\sigma$ would be estimated twice with less data. This accidentally assumes different variances.
2. To get probability statements about the splitting variable, it must be in the model.
3. Information-criterion comparison needs all models fit to the same data.
4. Multilevel models can borrow information across categories, which is impossible after splitting.

#### 7.1.1 Adding a dummy variable doesn't work (pp. 214–216)
- `m7.3`: log-GDP on ruggedness, all data. `m7.4` adds a dummy for Africa: $\mu_i=\alpha+\beta_R R_i+\beta_A A_i$ (pp. 214–216).
- WAIC (p. 215):

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m7.4 | 476.5 | 4.5 | 0.0 | 1 | 15.29 | NA |
| m7.3 | 539.6 | 2.7 | 63.1 | 0 | 13.27 | 15.05 |

- The author reads the difference of 63 (about ±30 for a 95% interval) as suggesting that the continent predictor seems to be picking up something important to the sample, even accounting for expected overfitting (p. 215).
- But the fitted lines for Africa and non-Africa are parallel (Fig. 7.3): the dummy only lets the model predict a lower mean for Africa and cannot change the slope. The good WAIC only shows African nations have lower GDP on average (p. 215).
- *Rethinking (97%):* 97% intervals are used to remind the reader that 95% is arbitrary (p. 215).

> *Intuition note.* A dummy variable moves a whole line up or down. To tilt the line differently in each group, the slope itself must depend on the group.

#### 7.1.2 Adding a linear interaction does work (pp. 216–218)
The additive model is $Y_i\sim\text{Normal}(\mu_i,\sigma)$, $\mu_i=\alpha+\beta_R R_i+\beta_A A_i$ (p. 216). Make the slope a linear model of $A$ (p. 216):

$$Y_i\sim\text{Normal}(\mu_i,\sigma)\quad[\text{likelihood}]$$
$$\mu_i=\alpha+\gamma_i R_i+\beta_A A_i\quad[\text{linear model of }\mu]$$
$$\gamma_i=\beta_R+\beta_{AR}A_i\quad[\text{linear model of slope}]$$

- $\gamma_i$ is a placeholder for the slope of GDP on ruggedness; the structure is the same as any Gaussian model fitted so far (p. 216).
- $\beta_{AR}$ is the strength of the dependency. If $\beta_{AR}=0$ the previous model returns. If $\beta_{AR}>0$ African nations have the more positive slope; if $<0$, the more negative. For non-African nations $A_i=0$, so $\beta_{AR}$ has no effect on their predictions (p. 217).
- `m7.5` fits this with `map` (maximum a posteriori: the posterior peak). Priors: $\alpha\sim\text{Normal}(8,100)$; $\beta_A,\beta_R,\beta_{AR}\sim\text{Normal}(0,1)$; $\sigma\sim\text{Uniform}(0,10)$ (p. 217).
- WAIC (p. 217):

| model | WAIC | pWAIC | dWAIC | weight | SE | dSE |
|---|---|---|---|---|---|---|
| m7.5 | 469.6 | 5.3 | 0.0 | 0.97 | 15.13 | NA |
| m7.4 | 476.4 | 4.4 | 6.8 | 0.03 | 15.35 | 6.22 |
| m7.3 | 539.7 | 2.8 | 70.1 | 0.00 | 13.31 | 15.22 |

- `m7.5` has about 97% of the weight. The weight left for `m7.4` suggests the `m7.5` slopes are a little overfit. The dSE (6.22) is almost the same as the difference (6.8), and the data on African countries are sparse (p. 217).
- *Do information criteria make sense here?* The author thinks so, but says reasonable people can disagree (p. 218):
  - Estimates must be overfit, since not every feature of a sample is caused by the process of interest, even when the aim is explanation.
  - WAIC's penalty comes from the posterior's shape (sum of variances of the log-likelihood of each point). It measures flexibility and so is useful heuristically, and it nudges toward conservative inference.
- *Overthinking (conventional form):* Substituting $\gamma_i$ and multiplying out gives one linear model, equivalent to the above and used by tools like `lm` (p. 218):
$$\mu_i=\alpha+\beta_R R_i+\beta_{AR}A_iR_i+\beta_A A_i$$

#### 7.1.3 Plotting the interaction (pp. 218–219)
Compute `link` means and 97% intervals of $\mu$ over a grid of ruggedness, separately for `cont_africa` = 1 and 0, and overlay them on the corresponding countries (Fig. 7.4). The slope now reverses between Africa and non-Africa (p. 219).

#### 7.1.4 Interpreting an interaction estimate (pp. 219–222)
The author usually advises against understanding interactions from tables alone. Two reasons (pp. 219–220):
1. Adding an interaction changes the meaning of parameters. A "main effect" coefficient in an interaction model does not mean what the same-named coefficient means without the interaction.
2. Tables rarely show covariance among parameters, so uncertainty is hard to incorporate.

**7.1.4.1 Parameters change meaning.** The change in $\mu_i$ per unit of $R_i$ is $\gamma_i$, which depends on $\beta_R$, $\beta_{AR}$ and $A_i$. $\beta_R$ has its old meaning only when $A_i=0$ (p. 220). `precis(m7.5)` (pp. 220–221):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 9.18 | 0.14 | 8.97 | 9.40 |
| bA | −1.85 | 0.22 | −2.20 | −1.50 |
| bR | −0.18 | 0.08 | −0.31 | −0.06 |
| bAR | 0.35 | 0.13 | 0.14 | 0.55 |
| sigma | 0.93 | 0.05 | 0.85 | 1.01 |

$\gamma$ is not in the table, so compute it at the MAP values (p. 221):
$$\gamma=\beta_R+\beta_{AR}(1)=-0.18+0.35=0.17\ \text{(Africa)};\qquad \gamma=\beta_R+\beta_{AR}(0)=-0.18\ \text{(not Africa)}$$

**7.1.4.2 Incorporating uncertainty.** Since $\gamma$ depends on parameters that have a posterior, it has one too: "Anything calculated using parameters has a distribution." (p. 221).
- Method: draw posterior samples (`extract.samples`); compute `gamma.Africa = bR + bAR*1` and `gamma.notAfrica = bR + bAR*0` per sample (p. 221).
- Means: 0.163 and −0.182, nearly the MAP values (p. 221). Fig. 7.5 shows the two marginal posteriors of $\gamma$, overlapping somewhat (p. 222).
- Difference: for each sample compute `gamma.Africa − gamma.notAfrica` and take the proportion below zero. The result is 0.0036. Conditional on model and data, it is highly implausible that the slope is lower inside Africa (p. 222).
- This tiny number looks small compared with the visual overlap of Fig. 7.5. That is not a mistake: the plotted densities are marginal, "like silhouettes", and the difference's distribution is a different object. So overlap of intervals is no informal test of a difference; compute the difference's distribution directly (p. 222).
- *Rethinking:* 0.0036 is not the probability of any observable event. It is the relative plausibility the model ("golem") assigns to the claim, for these data only (pp. 222–223).

> *Intuition note.* In an interaction model the effect of ruggedness is a quantity you compute from several parameters, not one you read off. Do the computation sample by sample, so that uncertainty carries through; tables rarely show how parameters covary.

### 7.2 Symmetry of the linear interaction (pp. 223–225)
In the toy problem of Buridan's ass, an ass who always moves to the closest pile would starve if equidistant between two identical piles (the author notes it would not really starve). A linear interaction has two symmetric phrasings (p. 223):
1. How much does the influence of ruggedness depend on being in Africa?
2. How much does the influence of being in Africa depend on ruggedness?

**7.2.1 Buridan's interaction.** Expand $\gamma_i$ in $\mu_i$, then factor the $A_i$ terms (p. 223):
$$\mu_i=\alpha+(\beta_R+\beta_{AR}A_i)R_i+\beta_A A_i=\alpha+\beta_R R_i+\beta_{AR}A_iR_i+\beta_A A_i$$
$$\mu_i=\alpha+\beta_R R_i+\underbrace{(\beta_A+\beta_{AR}R_i)}_{G}A_i$$
$G$ plays the role of $\gamma_i$: the same model, re-expressed so the interaction applies to $A_i$. This proves the symmetry. The model has no basis to prefer one reading. Our minds tend to prefer the one that is easier to imagine manipulating, here flattening hills rather than moving a country between continents (pp. 223–224).

**7.2.2 Africa depends upon ruggedness.** Plot continent on the horizontal axis, with one line for minimum ruggedness (0.003) and one for maximum (6.2). Points are split at the median ruggedness (p. 224).
- At minimum ruggedness, changing continent to Africa reduces expected log-GDP by about 2 points.
- At maximum ruggedness there is almost no expected effect. The line slopes up slightly, but the interval is wide (p. 224).
- Both perspectives hold at once. The second view makes clearer that African nations are on average nearly always worse off, and only at very high ruggedness do the two groups have the same expected log-GDP (p. 225).

> *Intuition note.* One equation, two stories. Both statements are true of the same model; the second view made clear something that was not obvious in the first.

### 7.3 Continuous interactions (pp. 225–235)
Interactions between continuous variables are especially opaque, even though the mathematics is essentially the same as in the categorical case. The author introduces the triptych (a panel of three complementary plots) and centring (rescaling a predictor so its mean is zero). Centring has two benefits: it makes coefficients easier to read, especially when comparing models with and without an interaction, and it can make model fitting faster and more reliable (pp. 225–226). Even so, the author's message is to always plot posterior predictions (p. 226).

#### 7.3.1 The data (p. 226)
`tulips`: 27 rows. `bed` (a, b, c) is a cluster. `water` (1 low to 3 high) is soil moisture. `shade` (1 = high light to 3 = low light). `blooms` is the outcome, ranging from 0 to 362 (pp. 226–227). Light and water are both needed for photosynthesis, which motivates an interaction. A simple linear interaction is a good start but "not close to the best that we could do" (p. 226).

#### 7.3.2 The un-centered models (pp. 226–229)
Two models, with $B$ blooms, $W$ water, $S$ shade (pp. 226–227):
$$\mu_i=\alpha+\beta_W W_i+\beta_S S_i\ \ (\texttt{m7.6});\qquad \mu_i=\alpha+\beta_W W_i+\beta_S S_i+\beta_{WS}W_iS_i\ \ (\texttt{m7.7})$$
- Priors are very flat: $\alpha,\beta\sim\text{Normal}(0,100)$, $\sigma\sim\text{Uniform}(0,100)$. The author says this is not the best practice, and that "flat" is relative to the likelihood. `bed` is left out here; the author thinks a sincere analysis needs it (p. 227).
- Fitting is likely to produce errors ("non-finite finite-difference value" and "maximum iterations reached"). Fixes (p. 228):
  1. Use another optimizer (BFGS is the default; try `Nelder-Mead`, then `SANN`).
  2. Allow more iterations (`control=list(maxit=1e4)`).
  3. Rescale or centre the data (preferred typically).
  
  The text uses fixes 1 and 2 first.
- `coeftab` (p. 229):

| | m7.6 | m7.7 |
|---|---|---|
| a | 53.49 | −84.26 |
| bW | 76.36 | 150.96 |
| bS | −38.95 | 35.00 |
| sigma | 57.38 | 46.27 |
| bWS | NA | −39.5 |

- The intercept jumps from 53 to −84. It is the expected outcome when all predictors are zero, and neither predictor is ever zero in the data (p. 229).
- In `m7.6`, water's effect is positive and shade's negative. In `m7.7` both main effects are positive and the interaction negative, so shade's main effect changes sign; the author asks whether we should now conclude that shade helps the tulips.
- WAIC: `m7.7` 296.4 (pWAIC 6.3, weight 0.99, SE 10.00); `m7.6` 305.8 (5.2, dWAIC 9.3, weight 0.01, SE 8.94, dSE 6.03) (p. 229).
- *Rethinking:* troubleshooting is realistic; "how you fit the model is part of the model" (pp. 229–230).

#### 7.3.3 Center and re-estimate (pp. 230–232)
Centre by subtracting the mean: `shade.c`, `water.c` (variance unchanged; both now range from −1 to 1) (p. 230). Re-fit as `m7.8`, `m7.9` with priors $\alpha\sim\text{Normal}(130,100)$, other priors as before, and explicit `start` values ($\alpha$ at mean blooms, slopes at 0, $\sigma$ at sd of blooms) (p. 230).

| | m7.8 | m7.9 |
|---|---|---|
| a | 129.00 | 129.01 |
| bW | 74.22 | 74.96 |
| bS | −40.74 | −41.14 |
| sigma | 57.35 | 45.22 |
| bWS | NA | −51.87 |

The main effects now match across models, and the direction for shade has not changed (p. 231).

**7.3.3.1 Estimation worked better.** With centred predictors the MAP value of $\alpha$ is the empirical mean of the outcome, which is also the start value; with uncentred predictors the MAP is far away, hence the long failed search (p. 231).

**7.3.3.2 Estimates changed less across models.** In uncentred models the interaction enters every prediction, since neither predictor is ever zero. For a tulip at the mean levels $S=W=2$ (p. 231):
$$\mu_i|_{S_i=2,W_i=2}=\alpha+\beta_W(2)+\beta_S(2)+\beta_{WS}(2\times2)$$
Using `m7.7`'s coefficients in R gives 129.6895. The centred `m7.9`, at mean values, gives 129.008 (p. 231). In the centred model, at the means:
$$\mu_i|_{S_i=0,W_i=0}=\alpha+\beta_W(0)+\beta_S(0)+\beta_{WS}(0\times0)=\alpha$$
The intercept is then the grand mean of blooms (p. 232).

`precis(m7.9)` (p. 232):

| | Mean | StdDev | 5.5% | 94.5% |
|---|---|---|---|---|
| a | 129.01 | 8.67 | 115.15 | 142.87 |
| bW | 74.96 | 10.60 | 58.02 | 91.90 |
| bS | −41.14 | 10.60 | −58.08 | −24.20 |
| bWS | −51.87 | 12.95 | −72.57 | −31.18 |
| sigma | 45.22 | 6.15 | 35.39 | 55.06 |

Readings (p. 232):
- $\alpha$: expected blooms at average water and shade.
- $\beta_W$: change in blooms per unit water *when shade is at its average*; it says nothing about other shade values.
- $\beta_S$: the same, for shade, at average water.
- $\beta_{WS}$: the expected change in water's influence when shade rises one unit, or equally in shade's influence when water rises one unit.

Why is it negative? Water and shade have opposite effects on blooms, but each makes the other more important to the outcome. The author says if you can't read this from −52, you are not alone, and that is why you should plot (p. 232).

> *Intuition note.* Centring puts "zero" at a typical case. Then the main effect is the effect for a typical case, and the intercept is the typical outcome.

#### 7.3.4 Plotting implied predictions (pp. 232–235)
- Without interactions one can hold other predictors at any value. With interactions the effect of changing one predictor depends on the others, so make several bivariate plots at different values of the unviewed variable (pp. 232–233).
- Triptych: three panels of blooms against shade at `water.c` = −1, 0, 1, showing only the matching raw data. Each shows the posterior mean and a 97% interval of the mean (via `link`, in a loop over `water.c`) (p. 233).
- Fig. 7.7, top row (no interaction, `m7.8`): the same slope in all three panels, with only the line height changing (p. 234).
- Fig. 7.7, bottom row (`m7.9`): the shade slope differs by water level (p. 234).
  - Lowest water: nearly flat; a very weak positive trend with substantial uncertainty.
  - Mean water: blooms approximately halve from least to most shade.
  - Highest water: steeper; blooms fall about two-thirds (pp. 234–235).
- Likely explanation: tulips need both water and light. At low water, shade cannot matter much because blooms are limited anyway. At high water, shade can matter much more. The same story works symmetrically for water given shade (p. 235). The plot could be redone with water on the horizontal axis (p. 235).

### 7.4 Interactions in design formulas (pp. 235–236)
`lm` forces flat priors, "hardly ever the best priors" (p. 235).
- $\mu_i=\alpha+\beta_x x_i+\beta_z z_i+\beta_{xz}x_iz_i$ is `y ~ x + z + x*z` (7.29), which is also `y ~ x*z` (7.30) (p. 235).
- To drop a main effect, subtract it: `y ~ x + x*z - z` (7.31). This is for when $\beta_z=0$ is known a priori (p. 235).
- Higher-order: `y ~ x*z*w` (7.32) gives all three main effects, three two-way interactions and the three-way term $\beta_{xzw}x_iz_iw_i$; lower-order terms are implied. `model.matrix(~x*z*w)` shows the columns: "(Intercept)", "x", "z", "w", "x:z", "x:w", "z:w", "x:z:w"; the colon means multiplication (pp. 235–236).

### 7.5 Summary (p. 236)
Interactions let the association between a predictor and the outcome depend on another predictor's value. They are difficult to interpret; triptych plots help. Fitting these models will need a more capable "conditioning engine" (next chapter) (p. 236).

### 7.6 Practice (pp. 236–239)
Easy: 7E1–7E3 (name a third variable; spot interactions in verbal explanations; write linear models). Medium: 7M1–7M3 (hot-temperature tulips; raven–wolf "species interaction"). Hard: 7H1–7H2 (add `bed`; WAIC), 7H3 (rugged without Seychelles), 7H4 (`nettle` language diversity with `mean.growing.season`, `sd.growing.season` and their interaction) (pp. 236–239).

## Toy example (ours, not from the text)
Take $\mu=\alpha+\beta_R R+\beta_A A+\beta_{AR}AR$ with $\alpha=9$, $\beta_R=-0.2$, $\beta_A=-2$, $\beta_{AR}=0.4$, $A\in\{0,1\}$.

- Slope in $R$ is $\gamma=\beta_R+\beta_{AR}A$. For $A=0$: $-0.2$. For $A=1$: $-0.2+0.4=0.2$. So the sign flips.
- Means at $R=0$ and $R=5$:
  - $A=0,R=0$: $9$.
  - $A=0,R=5$: $9-0.2\cdot5=8$.
  - $A=1,R=0$: $9-2=7$.
  - $A=1,R=5$: $9-1-2+0.4\cdot5=8$.
- Slope check for $A=1$: $(8-7)/5=0.2$ ✓. For $A=0$: $(8-9)/5=-0.2$ ✓.
- Symmetry: the effect of switching $A$ from 0 to 1 is $G=\beta_A+\beta_{AR}R$. At $R=0$: $-2$ (from $7-9$). At $R=5$: $-2+0.4\cdot5=0$ (from $8-8$). Same table, read the other way.
- A dummy-only model ($\beta_{AR}=0$) would give both groups slope $-0.2$ and could not reproduce $A=1$'s rising line.

## Concepts
- [[interaction]] (new) — the dependence of one predictor's association with the outcome on another predictor; a form of conditioning (p. 210)
- [[linear-interaction]] (new) — a slope defined as a linear model of another predictor, e.g. $\gamma_i=\beta_R+\beta_{AR}A_i$ (p. 216)
- [[interaction-symmetry]] (new) — expanding the model shows that ruggedness's effect depending on Africa and Africa's effect depending on ruggedness are the same model (p. 223)
- [[dummy-variable]] (new) — a 0/1 indicator for category membership; in an additive model it only shifts the mean (pp. 214, 215)
- [[centering]] (new) — subtracting the mean so zero marks a typical case; gives the intercept and main effects clearer meanings and eases fitting (pp. 225–226, 230)
- [[triptych-plot]] (new) — three panels of one predictor's predicted effect at three values of another (p. 233)
- [[survivorship-conditioning]] (new) — evidence from survivors is conditional on survival, so damage patterns mislead (p. 209)
- [[posterior-distribution]] — anything computed from parameters, such as a slope or a difference, has its own posterior, obtained by transforming samples (p. 221)
- [[cross-validation-loo-waic]] — WAIC is used for comparing models and read as a flexibility/overfitting measure, even if the train/test story isn't literal (pp. 215, 218)
- [[partial-pooling]] — the author mentions borrowing information across categories in multilevel models as a reason not to split data (p. 214)
- [[hierarchical-model]] — described as essentially massive interaction models (p. 211)

## Canonical instances
- [[manatee-bomber-survivorship]] — manatee propeller scars and A.W.38 bomber damage (Wald's story) show that conditioning on survival misleads (p. 209)
- [[rugged-africa-gdp]] — terrain ruggedness vs log-GDP: slope positive in Africa, negative elsewhere; dummy fails, interaction works (pp. 212–222)
- [[tulips-water-shade]] — blooms by water and shade; centred interaction model and triptych (pp. 226–235)
- [[buridans-ass]] — the symmetry analogy for linear interactions (p. 223)

## Bridges (candidates)
- [structural-analogy] conditioning on survival (p. 209) ↔ causal inference: selection bias from conditioning on a common effect — both distort what the observed sample shows.
- [structural-analogy] ruggedness slope reversing between groups (p. 212) ↔ Simpson's paradox: association changes sign when split by a third variable.
- [same-math] the posterior of $\gamma=\beta_R+\beta_{AR}$ from per-sample arithmetic (p. 221) ↔ Monte Carlo integration: transform draws, then summarise.
- [structural-analogy] interaction as slope conditional on cluster (p. 211) ↔ hierarchical models: group-specific slopes drawn from a population.
- [structural-analogy] interaction in a linear predictor (p. 210) ↔ GLMs: nonlinear link makes predictors interact implicitly.

## Questions this raises
- If the interaction posterior is estimated from few African countries (p. 217), how much does partial pooling in a multilevel model change the slopes?
- When there is a good mechanistic theory (e.g. plant physiology, p. 226), what non-linear function should replace $\beta_{WS}WS$?
- Since linear interactions are symmetric, what outside information (such as manipulability, p. 223) lets us prefer a causal reading?
- How do you pick the values at which to hold the other variable for a triptych when it is continuous rather than three-valued?

## Exercises worth doing
- Ex. 7E2–7E3 (p. 237) — recognise which verbal explanations imply an interaction and write linear models for them — difficulty: easy
- Ex. 7M1–7M2 (p. 237) — express a "no blooms when hot" three-way dependency in a regression equation — difficulty: medium
- Ex. 7H1–7H2 (p. 237) — add `bed` as a main effect and compare by WAIC; reconcile with the coefficients — difficulty: medium
- Ex. 7H3 (pp. 237–238) — drop Seychelles, refit, plot, and WAIC-compare/model-average the three ruggedness models — difficulty: hard
- Ex. 7H4 (pp. 238–239) — open-ended analysis of language diversity with main effects and an interaction of growing-season mean and sd — difficulty: hard

## Reading notes
- Printed page = pdf − 14 (pdf 223 = p. 209). Pdf 254 (printed 240) has no text in the text layer. Page 239 ends the exercises (7H4 a–c).
- The code uses `map`, as printed.
- **Inconsistencies seen in the pages:**
  - `coeftab` for `m7.7` (p. 229) gives a = −84.26, bW = 150.96, bS = 35.00, bWS = −39.5. The worked formula on p. 231 uses −150.8, 181.5, 64.1, −52.9, which sum to about 128.8, not the 129.6895 printed. The `coeftab` values give about 129.66, close to but not equal to the printed 129.6895.
  - p. 229 says shade's main effect in `m7.6` lowers blooms "by 42"; the table shows −38.95.
  - p. 231 says the interaction posterior mean stayed the same after centring; the tables show −39.5 (uncentred) and −51.87 (centred).
  - The 7.3.3.2 mean-level calculation and the `m7.7` coefficient values on p. 231 do not agree with the p. 229 table; I cannot explain this from these pages.
- Section 7.3.2 says "three basic solutions"; I give them as listed on p. 228.
- The text layer was readable. Tables and figures were checked against the page images.

---
id: mcelreath-2020-rethinking/ch14-missing
work: mcelreath-2020-rethinking
unit: Chapter 14. Missing Data and Other Opportunities
pages: 423-440
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
# Missing Data and Other Opportunities

## L0 — One line
State your assumptions about measurement error or missingness as part of the model, and Bayesian conditioning will estimate the true or missing values and the regression coefficients together.

## L1 — The gist (≤ 120 words)
How should we handle data that are measured with error, or not measured at all? McElreath's answer is not to be clever. Replace each uncertain datum by a parameter with a distribution, and let conditional probability do the rest. For known standard errors, the observed value becomes a Gaussian centered on an unknown true value. For missing values, the incomplete variable is modelled jointly with the outcome, so present data give a prior for each missing value. Both approaches shrink uncertain values toward the regression, and the coefficients can change. They also stop us from throwing away cases or averaging away uncertainty. Information flows in both directions.

**Prerequisites:** conditional probability; Gaussian distribution and standard error; linear regression with priors; shrinkage (partial pooling); reading `precis` output.

## L2 — Key ideas
- Bayesian work is "ruthless" application of conditional probability. Once the assumptions are stated, the rules of probability reveal their implications (p. 424).
- Ordinary data are a special case of a distribution with all its mass on one value. An uncertain datum can therefore be replaced by a distribution (p. 425).
- With measurement error on the outcome, each $D_{\text{OBS},i}$ is Gaussian around a parameter $D_{\text{EST},i}$, and the $D_{\text{EST}}$ values serve as the regression outcome. Uncertain states shrink toward the regression line and the slope changes (pp. 427–429).
- Ignoring measurement error tends to exaggerate associations, though it might also mask one (p. 428). Adding predictor error left the main coefficients essentially unchanged (p. 430).
- Do not average a distribution of values down to one number. Model it instead (p. 431).
- Missing values become parameters. The observed values supply a learned prior for them. Under MCAR (missing completely at random), imputation (estimating the missing values) uses the incomplete cases, and the neocortex slope fell from 2.8 to 1.9 (pp. 432–434).
- A better imputation model, one that includes the other predictor, narrows the imputed intervals. It also preserves the predictor–predictor association (pp. 435–437).
- If missingness depends on the values, one can try to model how it arises and see what the data say about that model. The chapter only sketches this (p. 437).

## L3 — Walkthrough

### Opening: Bertrand's box (pancakes) (pp. 423–424)
- Three pancakes: BB (burnt both sides), BU (one side), UU (none). One is served at random and its up side is burnt. What is Pr(down side burnt)? Most people say 1/2; the author says this is wrong (p. 423).
- Condition on what we know:
$$\Pr(\text{burnt down}\mid\text{burnt up})=\frac{\Pr(\text{burnt up, burnt down})}{\Pr(\text{burnt up})}$$
- Numerator: $\Pr(BB)=1/3$. Denominator, averaging over pancakes: $\Pr(\text{burnt up}) = \Pr(BB)(1)+\Pr(BU)(0.5)+\Pr(UU)(0) = 1/3+(1/3)(1/2)=0.5$. So the answer is $\frac{1/3}{1/2}=\frac23$ (p. 423).
- A simulation of 10,000 pancakes gave 0.6777889 (p. 424). The intuition is to count sides, not pancakes. Given a burnt up side, three sides could be down, and two of them are burnt (p. 424).
- The author's lesson: probability is just counting, and no cleverness is needed if conditional probability is applied to data and parameters alike. Model fitting works the same way (p. 424). The chapter has two applications: measurement error and imputation of missing data (p. 424).

*Intuition note:* You state what you know; the rules of probability work out the consequences. Intuition about those consequences can fail, as it does with the pancakes.

### 14.1 Measurement error (pp. 424–431)
- Data: US divorce and marriage rates (Chapter 5). Both are measured with error, reported as standard errors, and the error varies a lot across states. Large states give better samples and so smaller error (p. 425, Fig. 14.1).
- Ad hoc weighting procedures leave information unused. They also prevent information from flowing among measurements to improve the estimates of the data themselves (p. 425).

**14.1.1 Error on the outcome.**
- Generative view: if the true value is 10 m and measurement is Gaussian with sd 2, then $y\sim\text{Normal}(10,2)$. If the true value is unknown, put a parameter there (p. 426).
- Why Gaussian: if all we know about the error is its standard deviation, the maximum entropy distribution is Gaussian. Choosing another distribution would imply extra information. This does not claim the error really is Gaussian; it is the most conservative assumption given a mean and variance (p. 426).
- Model (p. 427), with $D_{\text{SE},i}$ the known standard error:
$$\begin{aligned}
D_{\text{EST},i}&\sim\text{Normal}(\mu_i,\sigma)\\
\mu_i&=\alpha+\beta_A A_i+\beta_R R_i\\
D_{\text{OBS},i}&\sim\text{Normal}(D_{\text{EST},i},D_{\text{SE},i})\\
\alpha,\beta_A,\beta_R&\sim\text{Normal}(0,10),\qquad \sigma\sim\text{Cauchy}(0,2.5)
\end{aligned}$$
- The only change from ordinary regression is that the outcome is now a vector of parameters. Each also acts as the mean of the distribution that "predicts" the observation. Information flows both ways: measurement uncertainty affects the coefficients, and the coefficients affect the estimated true values (p. 427).
- Fitting notes (`m14.1`, `map2stan`; p. 428):
  - WAIC is turned off, because the default code does not integrate over each `div_est`.
  - A `start` list gives the number of parameters.
  - `adapt_delta` is raised from 0.8 to 0.95. Without this there are a few divergent iterations, harmless here.
- Results (p. 428): $\beta_A=-0.55$ (sd 0.21, 89% interval −0.88 to −0.20), $\beta_R=0.13$ (sd 0.08), $\sigma=1.12$. Chapter 5 gave about −1 for $\beta_A$. It is now almost half that but still reliably negative.
- The author says ignoring measurement error tends to exaggerate associations, but it might also mask one, depending on which cases carry how much error (p. 428).
- Why: states with extreme ages at marriage tend to have more uncertain divorce rates. Those rates are shrunk toward the regression line. More uncertain states move more, which is shrinkage as in earlier chapters (p. 428, Fig. 14.2 left).
- Estimates and trend move each other. For an uncertain state, the trend strongly influences its new estimate. For a state with small standard error, the state strongly influences the trend (p. 429).

*Intuition note:* Precise data points pull the line, and the line pulls imprecise points. The slope settles where both pulls balance, and here it ends up flatter.

**14.1.2 Error on both outcome and predictor (pp. 429–431).**
- Same approach: each observed predictor is a draw around an unknown true value with known sd. The model adds $R_{\text{OBS},i}\sim\text{Normal}(R_{\text{EST},i},R_{\text{SE},i})$ and uses $\mu_i=\alpha+\beta_A A_i+\beta_R R_{\text{EST},i}$ (p. 430).
- Fit as `m14.2` with `mar_est[i]` in the linear model and 3 chains (p. 430).
- Result: coefficients for age at marriage and marriage rate are essentially unchanged. The marriage-rate estimates are updated, though (Fig. 14.3). Highly uncertain rates tend to belong to small states with high marriage rates, so pooling lowers those estimates (p. 430).
- Marriage-rate estimates move less than divorce estimates. Divorce rate is only weakly associated with marriage rate and so carries little information about it. Age at marriage strongly predicts divorce and carries a lot (pp. 430–431).
- Caveat: that information in age may be illusory, since age's own uncertainty is not modelled. It could be added the same way if standard errors or distributions were available (p. 431).
- Take-home: when you have a distribution of values, use the whole distribution. Using an average and discarding its uncertainty risks overconfidence and spurious inference, including when data were averaged before analysis. "Do not average. Instead, model." (p. 431).

### 14.2 Missing data (pp. 431–438)
- Information can flow from present data to missing data, if we are willing to model the whole variable (p. 431).

**14.2.1 Imputing neocortex (pp. 432–435).**
- Primate milk data: 12 missing `neocortex.perc` values. The Chapter 5 complete-case analysis dropped those 12 cases, including their good body mass and milk energy values, leaving 17 cases (p. 432).
- Imputation estimates will be wide but honest given the assumptions (p. 432).
- MCAR (Missing Completely At Random): the location of missing values is completely random with respect to those values and all other values. Dropping cases only makes sense under this assumption, since otherwise it biases the results. So imputing adds no new assumption (p. 432).
- Trick: model the incomplete predictor jointly with the outcome. The present values give a prior for each missing value, updated by the predictor–outcome relationship. The predictor becomes a mixed vector of data and parameters, e.g. $N=[0.55,N_2,N_3,N_4,0.65,\dots]$ (p. 432).
- Model (p. 432; $k$ is milk energy, $M$ is body mass):
$$\begin{aligned}
k_i&\sim\text{Normal}(\mu_i,\sigma)\\
\mu_i&=\alpha+\beta_N N_i+\beta_M\log M_i\\
N_i&\sim\text{Normal}(\nu,\sigma_N)\\
\alpha,\beta_N,\beta_M&\sim\text{Normal}(0,10),\quad\sigma\sim\text{Cauchy}(0,1),\\
\nu&\sim\text{Normal}(0.5,1),\quad\sigma_N\sim\text{Cauchy}(0,1)
\end{aligned}$$
- For observed $N_i$, the third line is a likelihood. For missing $N_i$, the same line is a prior, learned from the data via $\nu$ and $\sigma_N$ (p. 432).
- Weakness: the Gaussian ignores that proportions lie between 0 and 1. The author says practice problems show how to do better (p. 433).
- `map2stan` merges data and parameters automatically (pp. 433–434). Results for `m14.3` (p. 434):

| | complete cases (`m14.3cc`) | imputed (`m14.3`) |
|---|---|---|
| $\beta_N$ | 2.77 (sd 0.87) | 1.93 (sd 0.73) |
| $\beta_M$ | −0.10 | −0.07 |

  The imputed neocortex values are about 0.62–0.71 with sd 0.05. The author asks whether you would want colleagues to use all the data even if that means inferring a weaker relationship, and says to apply the same standard to yourself (p. 434).
- Figure 14.4: imputed values tilt gently toward the regression line, with wide uncertainty. They show no upward slope against log mass, because the imputation model assumed no relationship between the predictors (p. 435).

**14.2.2 Improving the imputation model (pp. 435–437).**
- Replace $N_i\sim\text{Normal}(\nu,\sigma_N)$ with
$$N_i\sim\text{Normal}(\nu_i,\sigma_N),\qquad \nu_i=\alpha_N+\gamma_M\log M_i$$
 (p. 435).
- Results (`m14.4`, p. 436): $\gamma_M=0.02$ (89% interval 0.01 to 0.03), $\beta_N=2.44$ (sd 0.75), $\beta_M=-0.09$. Imputed sds fall to about 0.03–0.04.
- Figure 14.5: the slope increases slightly (mean 1.5 vs 1.2). The imputed values preserve the positive neocortex–log-mass association (p. 436).
- General goal: model the joint distribution of all variables. Assumptions are not oaths: try alternatives to check sensitivity. Often the most conservative assumptions are hard to object to and use more of the data (p. 437).

*Intuition note:* A missing value is a parameter whose prior comes from the rest of the data. A prior that knows about the other predictor is sharper than one that does not.

**14.2.3 Not at random (p. 437).**
- Missingness may depend on values. For example, species with small brains may be harder to measure, so missingness correlates with neocortex percent. If we can model how missingness arises, Bayesian inference can estimate that model. The same holds for sampling bias. No example is worked.

**Overthinking: imputation algorithm (pp. 437–439).**
- To write this in Stan, build an index vector `nc_missing`: 0 where observed, otherwise the index of the matching imputation parameter. It has 12 non-zero entries (1 to 12) (p. 437).
- `NA` values are replaced by −1 so Stan accepts the data. The model block merges: if `nc_missing[i] > 0`, `nc_merged[i]` is `nc_impute[nc_missing[i]]`, else the observed value. Then `nc_merged ~ normal(mu_nc, sigma_nc)` and `kcal ~ normal(mu, sigma)` with $\mu=\alpha+\beta_N\,\text{nc\_merged}+\beta_M\,\text{logmass}$ (p. 438).
- It is "just two regressions" fitted together and sharing parameters. Per the text it reproduces the earlier results (p. 439).

### 14.3 Summary (p. 439)
- Both models require assumptions about variable distributions. These cascade through the model and change inferences about the data as well as from it. Model design remains up to you.

### 14.4 Practice (pp. 439–440)
- Exercises: measurement error and imputation for the Oceanic tools model; MCAR assumptions; WAIC with imputed cases; doubled standard errors; elephant matings with age error; an imputation example where one imputed datum reverses a relationship.

## Toy example (ours, not from the text)
Shrinkage of one uncertain observation, holding $\mu$ and $\sigma$ fixed (a simplification; in the chapter's model they are also estimated).

Suppose the regression predicts $\mu=9$ with $\sigma=1$. A state reports $D_{\text{OBS}}=12$.
- Case A: $D_{\text{SE}}=2$. Precisions (1/variance) are $1/4=0.25$ for the observation and $1/1=1$ for the regression. *(added step)* A Gaussian likelihood combined with a Gaussian prior gives a precision-weighted mean: $(12\cdot0.25+9\cdot1)/(0.25+1)=12/1.25=9.6$. Posterior sd $=\sqrt{1/1.25}=0.894$.
- Case B: $D_{\text{SE}}=0.5$. Precisions are 4 and 1. Mean $=(12\cdot4+9\cdot1)/5=57/5=11.4$.

The noisy observation moves from 12 to 9.6, a shift of 2.4. The precise one moves only 0.6. This is the pattern in Fig. 14.2 (left).

## Concepts
- [[measurement-error-model]] (new) — replace an observed value by a distribution around an unknown true-value parameter, with the standard error as its sd (p. 426)
- [[bayesian-imputation]] (new) — treat each missing value as a parameter whose prior is learned from the observed data (p. 432)
- [[mcar]] (new) — missing completely at random: missingness unrelated to the missing values or to any other values (p. 432)
- [[complete-case-analysis]] (new) — dropping all cases with any missing value; sensible only under MCAR (p. 432)
- [[missing-not-at-random]] (new) — missingness depends on values; if a model of how missingness arises can be made, Bayesian inference can assess it (p. 437)
- [[partial-pooling-shrinkage]] — less certain estimates move more toward the regression via pooling (p. 428)
- [[principle-of-indifference-maximum-entropy]] — with only a mean and sd known, Gaussian error is the most conservative choice (p. 426)
- [[prior-distribution]] — for a missing $N_i$, the "likelihood" line acts as a prior learned from the data (p. 432)
- [[hamiltonian-monte-carlo]] — `adapt_delta` is raised from 0.8 to 0.95; without that, a few (harmless here) divergent iterations appear (p. 428)

## Canonical instances
- [[bertrand-box-paradox]] — the pancake problem; answer 2/3 by conditional probability (p. 423)
- [[waffle-divorce-data]] — US state divorce and marriage rates with standard errors (p. 425)
- [[primate-milk-data]] — 12 missing neocortex values; complete-case vs imputed estimates (p. 432)

## Bridges (candidates)
- [structural-analogy] Missing neocortex values as parameters ↔ causal inference: unobserved potential outcomes — both treat unobserved quantities as unknowns inferred from a model.
- [structural-analogy] MCAR ↔ ignorability: both say the mechanism deciding what is seen is unrelated to the unseen values.
- [structural-analogy] Shrinkage of noisy $D_{\text{EST}}$ toward the regression line ↔ hierarchical models: more uncertain units are pooled more.
- [metaphor] "Do not average, model" ↔ propagating uncertainty in any pipeline.

## Questions this raises
- How would a model of missingness itself look when small-brained species are harder to measure?
- What bounded distribution would suit proportions such as neocortex, instead of the Gaussian?
- How sensitive are the coefficients to the assumed size of the standard errors (see 14M3, 14H2)?
- Can an imputed datum reverse an inferred relationship (14H3)?

## Exercises worth doing
- Ex. 14E1 (p. 439) — write a measurement-error model for log population in a Poisson regression — difficulty: easy
- Ex. 14M1 (p. 439) — state what the imputation model assumes about how values went missing — difficulty: medium
- Ex. 14M3 (p. 440) — double the standard errors and explain the effect on inference — difficulty: medium
- Ex. 14H1 (p. 440) — elephant matings with age measured with ±5 years error — difficulty: hard
- Ex. 14H3 (p. 440) — imputing one datum reverses the direction of β — difficulty: hard

## Reading notes
- Printed = pdf − 14. Pages 423–440.
- The chapter text on p. 435 says "90% confidence intervals" for imputed values, but the Fig. 14.4 caption says 89% posterior intervals. I follow the caption.
- The math on p. 432 gives $\alpha\sim\text{Normal}(0,10)$, but the code (14.7) uses `a ~ dnorm(0,100)`. I report both as printed.
- The model on p. 430 writes $R_{\text{EST},i}$; the code uses `mar_est[i]`.
- The text gives "mean 1.5 now instead of 1.2" for the slope on p. 436 without saying which quantity it means; the precis tables show $\beta_N$ as 1.93 and 2.44. The text does not report both values elsewhere.
- The text promises practice problems on bounded proportions (p. 433). None of the listed problems is visibly about this.
- The Stan code uses `<-` for assignment, as printed.
- The text layer was readable, and I checked equations against the images.

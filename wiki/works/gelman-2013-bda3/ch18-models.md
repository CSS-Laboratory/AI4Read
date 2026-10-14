---
id: gelman-2013-bda3/ch18-models
work: gelman-2013-bda3
unit: "18 Models for missing data"
pages: 449–468
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Models for missing data (BDA3, Chapter 18)

## L0 — One line
Missing values are treated as extra unknowns with a joint posterior alongside the parameters, so inference alternates between imputing the missing data and drawing the parameters, and under an ignorable mechanism the missingness process need not be modelled for inference (it is still needed when simulating replicated data for model checking).

## L1 — The gist (≤ 120 words)
How should we do Bayesian inference when some data are missing? The chapter treats missing values as extra unknowns with a joint posterior alongside the parameters. If missingness is at random and its parameters are distinct from the data parameters, the mechanism is ignorable and need not be modelled for inference. Inference then splits into imputing missing values and drawing parameters, done by EM and data augmentation (a Gibbs sampler), with shortcuts for monotone patterns. Simple rules combine several imputed datasets. Applications: a hierarchical normal model for 51 US polls in 1988; a multinomial model for "don't know" answers in a Slovenian poll (posterior median 0.883 vs actual 88.5%).

**Prerequisites:** Bayes' theorem and posterior simulation; multivariate normal and conditional distributions; Dirichlet–multinomial conjugacy; basics of EM and the Gibbs sampler (BDA Ch. 11, 13); BDA Ch. 8 notation (inclusion indicator, ignorability).

## L2 — Key ideas (5–10 bullets)
- Missing data and parameters are both uncertain; Bayes puts a joint posterior on them. The model has three parts: prior, joint data model, and an inclusion model for the missingness process (p. 449).
- The mechanism is *ignorable* if the data are missing at random (MAR) and the mechanism's parameters φ are distinct from the data parameters θ. Then only $p(y_{\rm obs}|\theta)$ is needed. MCAR (missing completely at random: missingness independent of the data altogether) is stronger and, the authors say, relatively rare in practice (p. 450).
- Multiple imputation: draw several completed datasets, analyse each as if complete, and combine. The combining uses the average complete-data variance (within), the spread of the estimates across imputations (between), and a total variance $T_K$ built from both (pp. 451–453).
- EM (which finds posterior modes) and data augmentation (a Gibbs sampler that draws from the posterior) alternate between filling in missing data and updating parameters. For the normal model the E-step (expectation step) computes expected sufficient statistics, and monotone patterns (variables can be ordered so that each block is observed whenever the next one is) allow direct draws (pp. 452–455).
- The $t$ model adds an imputed scale variable $V_i$ per unit, and nonignorable models just add φ and condition on $I$ (p. 456).
- Polls example: a hierarchical normal model across 51 surveys imputes both "not answered" and "not asked" items. Plots of imputations exposed a model flaw (missing time trend) (pp. 457–462).
- For counted data, partially classified cases are allocated to cells in proportion to the current cell probabilities (p. 462).
- Slovenia: crude estimates 0.93 and 0.69 were far off. EM, SEM (a numerical way to get the posterior variance from EM) and data augmentation gave about 0.88, close to the 88.5% outcome (pp. 463–466).

## L3 — Walkthrough

### Introduction (p. 449)
- Earlier chapters mostly assume complete data. Here the work separates into (1) **multiple imputation**: simulate $y_{\rm mis}$ from its posterior predictive distribution given $y_{\rm obs}$; and (2) draw the parameters θ (p. 449).
- Bayes draws no distinction between missing data and parameters; both have a joint posterior given the observed data. The practical difference shows up in model setup: (i) a prior (and hyperprior if hierarchical), (ii) a joint model for all data, (iii) an *inclusion model* for missingness (p. 449).
- If the mechanism is ignorable (Section 8.2), inference needs no inclusion model. The inclusion model *is* needed when simulating replicated datasets for model checking (p. 449).

### 18.1 Notation (pp. 449–451)
- $y=(y_{\rm obs},y_{\rm mis})$ is the complete data. The **inclusion indicator** $I$ has the same size as $y$: 1 if observed, 0 if missing. $I$ is assumed fully observed. Item nonresponse is $I_{ij}=0$ for one item. Unit nonresponse is $I_{ij}=0$ for all items of unit $i$ (p. 449).
- The joint model is $p(y,I|\theta,\phi)=p(y|\theta)\,p(I|y,\phi)$. The second factor, indexed by φ, is the missing-data mechanism (pp. 449–450).
- The observed-data distribution integrates out $y_{\rm mis}$:
$$p(y_{\rm obs},I|\theta,\phi)=\int p(y_{\rm obs},y_{\rm mis}|\theta)\,p(I|y_{\rm obs},y_{\rm mis},\phi)\,dy_{\rm mis}.\tag{18.1}$$
- **MAR:** $p(I|y_{\rm obs},y_{\rm mis},\phi)=p(I|y_{\rm obs},\phi)$. The mechanism may depend on observed values, including fully observed covariates, and on φ. Formally this needs $p(I|y,\phi)$ only at the observed $y_{\rm obs}$ (p. 450).
- Under MAR:
$$p(y_{\rm obs},I|\theta,\phi)=p(I|y_{\rm obs},\phi)\int p(y_{\rm obs},y_{\rm mis}|\theta)dy_{\rm mis}=p(I|y_{\rm obs},\phi)\,p(y_{\rm obs}|\theta).\tag{18.2}$$
- If also φ and θ are *distinct* (independent in the prior), Bayesian inference for θ can use only the observed-data likelihood $p(y_{\rm obs}|\theta)$. The mechanism is then called **ignorable** (p. 450).
- **Observed at random / MCAR:** $p(I|y_{\rm obs},y_{\rm mis},\phi)=p(I|\phi)$ (18.3). MAR plus observed at random is MCAR. MAR plus distinct parameters is the weaker pair that is *sufficient* for inference without modelling the mechanism. MCAR is rarely plausible, so the chapter focuses on MAR (p. 450).
- MAR (not MCAR) becomes more plausible when more relevant observed variables are included in $y$ (p. 450).
- **Age–income example** (bivariate normal, age always recorded, income sometimes missing) (pp. 450–451):
  - Same recording probability for everyone: MCAR.
  - Missingness depends on age but not on income given age: MAR but not observed at random. It is ignorable if the mechanism's parameters are distinct from the normal's, as is typical.
  - Missingness depends on income within age groups: neither MAR nor observed at random; nonignorable.
- Relevance depends on the goal. For only the mean and variance of age, one can discard income and the mechanism is ignorable. For the marginal distribution of income, the mechanism is of paramount importance (p. 451).
- If information on the mechanism exists, a nonignorable analysis may still be possible (Section 8.2) (p. 451).

*Intuition note.* The chance that a value is missing may depend on things you can see; if the mechanism's parameters are also distinct from the data parameters, the mechanism need not be modelled for inference. It cannot be ignored when missingness depends on the hidden value itself. Including more relevant observed variables makes the 'depends only on what we see' assumption (MAR) more plausible.

### 18.2 Multiple imputation (pp. 451–454)
- A single imputation gives a complete dataset many researchers can use. With a reasonable imputation model, results are likely more accurate than discarding incomplete cases. **Multiple imputation** makes more than one replacement set, so nonresponse uncertainty under a given model can be reflected. Data augmentation can be viewed as iterative multiple imputation (p. 451).
- Paradigm: regression $p(y|X,\theta)$ with missing entries in $X$. The full Bayesian approach needs a model for $X$ (parameters ψ) and inference on $(X_{\rm mis},\psi,\theta|X_{\rm obs},y)$. There is no way around this, but it takes modelling effort away from the primary goal (p. 451).
- Computation yields simulations $(y_{\rm mis}^s,\theta^s)$, $s=1,\dots,S$. Two options: use them for inferences directly, or release $y_{\rm obs}$ with the draws $y^s_{\rm mis}$ (the multiple imputations). Other users then analyse the completed datasets without modelling the missingness (p. 451).
- Three-step procedure (pp. 451–452):
  1. Model $X,y$ jointly; keep only completed datasets $X^s=(X_{\rm obs},X^s_{\rm mis})$ for a few draws and discard the parameter inferences.
  2. For each $X^s$, infer θ from $p(y|X^s,\theta)$, treating imputed data as known.
  3. Combine. With Bayesian simulation, just mix the simulations. Analytic methods are given later in the section.
- The chapter covers step 1 and missing-data analysis (p. 452).

**Computation using EM and data augmentation (p. 452).**
- Imputation usually starts from crude methods (e.g. under MCAR) as starting points for mode-finding and simulation. Gibbs and EM formalize the old idea: fill in estimates, estimate parameters, repeat (p. 452).
- Notation conversion from Section 13.4 (p. 452): data $y$ becomes $(y_{\rm obs},I)$; marginal mode of φ becomes posterior mode of θ (or $(\theta,\phi)$ if the mechanism is estimated); averaging over γ becomes averaging over $y_{\rm mis}$. Augmented quantities such as mixture indicators count as part of $y_{\rm mis}$.
- For exponential families, the expected complete-data log posterior is linear in the expected sufficient statistics, so only those need to be imputed (p. 452).
- **EM for nonignorable models:** it works if a mechanism model is specified (e.g. censoring point or rounding rule known). All calculations condition on $I$. The expected complete-data log posterior is a function of $(\theta,\phi)$, averaged over $y_{\rm mis}$ at $(\theta^{\rm old},\phi^{\rm old})$ (p. 452).

**Monotone patterns (p. 453).**
- A pattern is *monotone* if variables can be ordered in blocks with block 1 more observed than block 2, and so on. "More observed" means values in block 1 are present whenever those in block 2 are present, but not conversely. For normal data, there are only as many missingness patterns as there are blocks, so all observations with the same pattern can be handled in one E-step. Near-monotone data: do the E-step for entries outside the pattern, then the efficient step for the rest (p. 453).

**Inference with multiple imputations (p. 453).**
For $K$ imputed sets under one model, with complete-data estimates $\hat\theta_k$ and variance estimates $\widehat W_k$ for a scalar θ:
$$\bar\theta_K=\frac1K\sum_{k=1}^K\hat\theta_k,\qquad \overline W_K=\frac1K\sum_{k=1}^K\widehat W_k\ \text{(within)},\qquad B_K=\frac1{K-1}\sum_{k=1}^K(\hat\theta_k-\bar\theta_K)^2\ \text{(between)},$$
$$T_K=\overline W_K+\frac{K+1}{K}B_K,\qquad \text{d.f.}=(K-1)\left(1+\frac{K}{K+1}\frac{\overline W_K}{B_K}\right)^2 .$$
Interval estimates use a $t$ distribution with this d.f., an approximation obtained by matching moments (p. 453). The bibliographic note relates it to the Satterthwaite approximation (p. 466).

*Intuition note.* The total uncertainty has two sources: ordinary sampling noise (within) and disagreement between plausible fills (between). If the imputed datasets give very different estimates, $B_K$ is large and the interval widens.

- A relatively small number of imputations can typically be used in areas like sample surveys (p. 453).
- If the fraction of missing information is low, inference will likely not be sensitive to assumptions about the mechanism. Suggested approach: build a "reasonable" model and check sensitivity to others; it often seems helpful to start ignorable and explore plausible nonignorable models (p. 454).

### 18.3 Missing data in the multivariate normal and $t$ models (pp. 454–456)
Setting: $y$ is a sample of size $n$ from $\mathrm N_d(\mu,\Sigma)$, uniform prior (p. 454).

**EM (pp. 454–455).**
- Sufficient statistics: $\sum_i y_{ij}$ ($j=1..d$) and $\sum_i y_{ij}y_{ik}$ ($j,k=1..d$). With $\theta^{\rm old}=(\mu^{\rm old},\Sigma^{\rm old})$, the E-step is
$$\mathrm E\Big(\sum_i y_{ij}\,\Big|\,y_{\rm obs},\theta^{\rm old}\Big)=\sum_i y_{ij}^{\rm old},\qquad \mathrm E\Big(\sum_i y_{ij}y_{ik}\,\Big|\,y_{\rm obs},\theta^{\rm old}\Big)=\sum_i\big(y_{ij}^{\rm old}y_{ik}^{\rm old}+c^{\rm old}_{ijk}\big),$$
where $y^{\rm old}_{ij}=y_{ij}$ if observed and $\mathrm E(y_{ij}|y_{\rm obs},\theta^{\rm old})$ if missing. Also $c^{\rm old}_{ijk}=0$ if $y_{ij}$ or $y_{ik}$ is observed, and $\mathrm{cov}(y_{ij},y_{ik}|y_{\rm obs},\theta^{\rm old})$ if both are missing (p. 454).
- The conditional law of $y_{\rm mis\,i}$ given $y_{\rm obs}$ and θ is multivariate normal. Its mean and variance come from $\theta^{\rm old}$ as in Appendix A (p. 454).
- M-step (pp. 454–455):
$$\mu_j^{\rm new}=\frac1n\sum_{i=1}^n y^{\rm old}_{ij},\qquad \sigma^{\rm new}_{jk}=\frac1n\sum_{i=1}^n\big(y^{\rm old}_{ij}y^{\rm old}_{ik}+c^{\rm old}_{ijk}\big)-\mu^{\rm new}_j\mu^{\rm new}_k .$$
- Start with crude methods and several starting values (multiple modes possible). The initial variance matrix must be positive definite; complete-case estimates can help (p. 455).

**Sampling (p. 455).**
- Starting from the modal estimates, data augmentation (Gibbs) alternately draws $y_{\rm mis}$, μ, Σ from their conditional posteriors. More complicated models may need Metropolis steps (p. 455).
- *Monotone case:* with $y_1$ more observed than $y_2$, and so on (k ≤ d blocks), let $\psi=(\psi_1,\dots,\psi_k)$. Here $\psi_1$ parameterizes the marginal of block 1 and $\psi_j$ the regression of $y_j$ on $y_1,\dots,y_{j-1}$ (coefficients and residual variance matrix). ψ is a one-to-one function of θ, and its parameter space is the product of those of the $\psi_j$. The log likelihood factors (p. 455):
$$\log p(y_{\rm obs}|\psi)=\log p(y_{\rm obs\,1}|\psi_1)+\log p(y_{\rm obs\,2}|y_{\rm obs\,1},\psi_2)+\cdots+\log p(y_{\rm obs\,k}|y_{\rm obs\,1},\dots,y_{\rm obs\,k-1},\psi_k),$$
with piece $j$ depending only on $\psi_j$. If the prior factors in closed form, $p(\psi)=p(\psi_1)p(\psi_2|\psi_1)\cdots p(\psi_k|\psi_1,\dots,\psi_{k-1})$, one can draw directly from $p(\theta|y_{\rm obs})$ in sequence: $\psi_1$, then $\psi_2$ given $\psi_1$, and so on (p. 455).
- *Not exactly monotone:* **monotone data augmentation** imputes only enough values to make the pattern monotone, then draws the posterior directly. Typically more efficient than ordinary data augmentation if the departure from monotonicity is not substantial. The best variable ordering is complicated. A simple choice puts the variable with fewest missing values first (p. 455).

*Intuition note.* If each variable is observed whenever the next one is, the likelihood splits into separate regression pieces. Each can be fitted on its own, and if the prior factors the same way, the parameters can be drawn directly in sequence, with no iteration.

**$t$ extension (p. 456).**
- Model: $y_i|\theta,V_i\sim\mathrm N_d(\mu,V_i\Sigma)$ with independent $V_i\sim\text{Inv-}\chi^2(\nu,1)$; ν specified (if unknown, another parameter). Useful for outliers or as sensitivity analysis (p. 456).
- Data augmentation adds an imputation step for $V_i$, treated as extra missing data:
$$p(V_i|y_{\rm obs},\theta,\nu)\propto \mathrm N(y_{\rm obs\,i}|\mu_{\rm obs\,i},\Sigma_{\rm obs\,i}V_i)\,\text{Inv-}\chi^2(V_i|\nu,1).\tag{18.4}$$
This is scaled inverse-$\chi^2$, so easy to draw. Then $y_{\rm mis\,i}$ is drawn from the conditional normal given $V_i$ (as in the ordinary normal model). The posterior step is a complete-data weighted multivariate normal problem (p. 456).
- EM: replace draws by conditional expectations of $V_i$ and conditional means and variances of $y_{\rm mis\,i}$. The M-step finds the conditional posterior mode. If ν varies, use ECM or ECME (Section 13.4) (p. 456).
- **Nonignorable models:** same principles. Supplement θ with φ and condition on $y_{\rm obs}$ and $I$ (p. 456).

### 18.4 Example: multiple imputation for a series of polls (pp. 456–462)
**Background (pp. 456–457).** The 1988 US presidential election: Dukakis was far ahead four months before the election but lost by a large margin. The data are 51 national polls from nine organizations over six months. The aim was time trends in vote intention by subgroup. Ideology was missing in 10 of the 51 surveys. Economy and perceived-ideology questions were asked in fewer than half. Two naive options: impute each survey separately (difficult when a question was not asked in that survey), or pool all surveys (does not account for differences between surveys). The chosen compromise is a separate model per survey with parameters linked hierarchically. Imputations for item nonresponse are then driven mostly by that survey. Imputations for unasked questions use other surveys and other answers in that survey (p. 457).

**Framework (p. 457).** There are $Q=15$ questions (outcome, variables believed most related to it, several demographics; the survey date is also included in the analysis) and $S=51$ surveys. Augment so that every survey has all $Q$ questions. The complete data are $((y_{si1},\dots,y_{siQ}):i=1..N_s,\ s=1..S)$ (18.5). Ignorable missingness is assumed, plausible since almost all missingness is "not asked". If ignorability is clearly violated (e.g. a defense question asked more during war), add survey-level variables (e.g. international tension) to restore MAR (p. 457).

**Model (p. 458).**
$$y_{si}|\mu_s,\Psi,\theta,\Sigma\overset{\rm ind}\sim \mathrm N_Q(\mu_s,\Psi),\quad i=1..N_s,\ s=1..S\tag{18.6}$$
- Common Ψ across surveys could be tested by splitting surveys (e.g. early vs late) and estimating separate matrices.
- With $P$ fully observed survey-level covariates $x_s$ (organization, time trend), and $\mathbf X$ the $S\times P$ matrix:
$$\mu_s|\mathbf X,\beta,\Sigma\overset{\rm ind}\sim \mathrm N_Q(\beta x_s,\Sigma),\quad s=1..S\tag{18.7}$$
 with β a $Q\times P$ coefficient matrix and $\Sigma=\mathrm{Diag}(\sigma_1^2,\dots,\sigma_Q^2)$. Hence $Q$ separate regressions:
$$\mu_{sj}|\mathbf X,\beta,\Sigma\sim \mathrm N(\beta_jx_s,\sigma_j^2),\quad s=1..S,\ j=1..Q\tag{18.8}$$
where $\beta_j$ is row $j$ of β.
- Noninformative prior:
$$p(\Psi,\beta,\Sigma)=p(\Psi)p(\beta)\prod_{q=1}^Q p(\sigma^2_Q)\propto|\Psi|^{-(Q+1)/2}.\tag{18.9}$$
If fewer than $Q$ individuals answered all questions, a proper prior for Ψ is needed.

**Continuous model for discrete answers (pp. 458–459).** The variables are sex and ethnicity (unordered), vote intention and education (ordered discrete), and age, income and 1–5/1–7 opinion scales (potentially continuous but coded discrete). Responses are recoded to a common scale across organizations. The options are (1) latent-variable models, (2) continuous model then rounding, (3) continuous model with continuous imputations. The authors use (3) and round when discrete values are needed. Little is lost because the most discrete variables are fully or nearly fully observed, and the opinion questions with the most nonresponse are essentially continuous (p. 459).

**Computation (pp. 459–460).** A special program was needed, because a simple Gibbs or Metropolis algorithm would be too slow. The method uses monotone data augmentation plus Gibbs under the monotone pattern. Figure 18.1 shows the approximately monotone pattern, with variables sorted from sex (most observed) to the candidates' perceived ideologies (least observed). Its labels read 183,229 missing, 61,457 missing and 610,794 observed (the text does not explain the labels). The data matrix in the monotone ordering is
$$y_{\rm mp}=\big((\mathbf y^{(k)}_{s_ii1},\dots,\mathbf y^{(k)}_{s_iik}),\ i=1..n_k,\ k=1..Q\big),\tag{18.10}$$
where $k$ indexes the observed data patterns, $n_k$ is the number of respondents with pattern $k$, and $s_i$ is respondent $i$'s survey. It still has missing entries $y_{\rm mp,mis}$ (asked but not answered), so $y_{\rm mp}=(y_{\rm obs},y_{\rm mp,mis})$ (p. 459). Each Gibbs iteration (p. 460):
1. Impute $y_{\rm mp,mis}$ given $\Psi,\mu_1..\mu_S,\beta,\Sigma,y_{\rm obs}$ (joint normal draws).
2. Draw $(\Psi,\beta,\Sigma)$ given $\mu_1..\mu_S,y_{\rm obs},y_{\rm mp,mis}$ (hierarchical linear model with complete data).
3. Draw $(\mu_1..\mu_S)$ given the rest; they are mutually independent normals in this conditional posterior.

**Weights (p. 460).** Sampling and poststratification weights were not used in imputation, because the variables they were based on were largely already in the model. They *are* used when computing averages from the imputed data, to get unbiased population averages unconditional on demographics (p. 460).

**Results (pp. 460–462).**
- Figure 18.2 plots survey-level mean versus date for income (expected stable) and perceived ideology of Dukakis (expected to change). Error bars are ±1 posterior standard error, combining within- and between-imputation variance. Inner brackets show within-imputation standard deviation alone (p. 460).
- Income: where the question was asked, within-imputation variance almost equals total variance. Where it was not asked, standard errors are large, sensibly so, since income is not highly correlated with the other questions (p. 460).
- Survey means of income vary from $31,000 to $37,000, more than sampling variability explains. The authors attribute this to different pollsters' income codings. Since the aim is to impute what each survey would have looked like, this variability is judged reasonable. Income is wanted as a predictor, and this uncertainty is accepted (pp. 460–461).
- Dukakis's perceived ideology: observed and imputed responses both show a time trend (more liberal late in the campaign). An earlier model without time as a predictor showed the trend in observed data but not in the imputations. The plot revealed this flaw, since imputed responses looked systematically different from the data (pp. 461–462).

*Intuition note.* A hierarchical imputation model lets each survey borrow strength from the others, so a question never asked in one survey still gets a sensible, appropriately uncertain fill-in. Plotting imputations against observed data is a practical way to catch a misspecified imputation model.

### 18.5 Missing values with counted data (p. 462)
- The complete data are multinomial: size $n$, cells $c_1..c_J$, probabilities $\theta=(\pi_1,\dots,\pi_J)$, counts $n_1..n_J$. A conjugate Dirichlet prior is used. The observed data are $m$ completely classified cases ($m_j$ in cell $j$) and $n-m$ partially classified cases known only to lie in a subset of cells. Example: in a $2\times2\times2$ table ($J=8$), a case with the third dimension missing lies in one of two cells (p. 462).
- Group the partially classified cases into $K$ types, with subset $S_k$ containing $r_k$ cases (p. 462).
- *Data augmentation:* the imputation step assigns each of the $r_k$ cases at random to cells in $S_k$ with probability
$$\frac{\pi_jI_{j\in S_k}}{\sum_{l=1}^J\pi_lI_{l\in S_k}}.$$
The parameter step draws from the Dirichlet posterior, treating imputed and observed data as complete. Nonconjugate priors are possible but make computation harder (p. 462).
- *EM* is the nonstochastic version. The E-step computes the expected number of the $r_k$ cases in each cell (the multinomial mean). The M-step combines observed counts with these expectations (p. 462).
- Monotone or nearly monotone patterns: the likelihood is the product of the marginal for the most observed variables and conditionals for later sets. With a factored (e.g. Dirichlet) prior, the posterior can be drawn directly. For near-monotone data, iterate between imputing the cases needed to complete monotonicity and a direct posterior draw. Loglinear models bring further complications (p. 462).

### 18.6 Example: an opinion poll in Slovenia (pp. 463–466)
**Setting (p. 463).**
- In 1990 a plebiscite was held on independence. Non-attendance counted as "no". Only attending-and-voting-"yes" counted as in favour.
- A survey of 2074 Slovenians asked: (1) independence? (2) secession? (3) attend the plebiscite? Table 18.1 gives the $3\times3\times3$ counts, with "don't know" (DK) as a third answer. The estimand is α, the proportion planning to attend and vote in favour of independence.
- DK is treated as missing data. This view holds at least if "yes"/"no" answers are accurate for the plebiscite, because every participant will effectively vote yes or no. Question 2 is not of direct interest but may help impute missing answers, since a "yes" to question 2 may indicate support for independence in someone who did not answer question 1.

**Crude estimates (pp. 463–464).**
- Available cases (answering independence and attendance): $\hat\alpha=1439/1549=0.93$.
- But only $1439/2074=69\%$ definitely plan to attend and vote yes. Treating DK as "no" would give a much different estimate.
- Using information not in the table, only 1251/2074 of the *original* intended sample (excluding substitutes) plan to attend and vote yes, which is the most pessimistic estimate. Substitutes are treated as originals and clustering is ignored in the later analysis (pp. 463–464).

**Likelihood and prior (p. 464).**
- The complete data are 2074 observations on the 8 cells of a $2\times2\times2$ table with probabilities θ. $\theta_{ijk}$ is the probability that the respondent answered $i$, $j$, $k$ to questions 1, 2, 3 (0 = no, 1 = yes). The estimand is $\alpha=\theta_{101}+\theta_{111}$ (p. 464).
- A Dirichlet prior with all parameters 0 is noninformative in the sense that the posterior mean is the MLE. One observed cell count is 0 (secession yes, attendance no, independence no), so this improper prior gives an improper posterior, unless the cell is treated as a structural zero. That is judged implausible. The authors use a Dirichlet with all parameters 0.1 (convenient, arbitrary, diffuse) and note that a thorough analysis should check sensitivity to this choice (p. 464).

**Missing-data model (pp. 464–465).**
- There are 18 types of partially classified observations. For example, type 1 ($r_1$ cases) has yes, yes, DK, so $S_1$ contains cells 111 and 110. DK is assumed MAR: the probability of DK may depend on other answers but not on the unobserved answer to that question (p. 464).
- Complete-data likelihood: $p(n|\theta)\propto\prod_{i=0}^1\prod_{j=0}^1\prod_{k=0}^1\theta_{ijk}^{n_{ijk}}$. Under MAR, the $r_p$ cases of pattern $p$ are multinomial with probabilities
$$\pi_{ijk\,p}=\frac{\theta_{ijk}I_{ijk\in S_p}}{\sum_{i'j'k'}\theta_{i'j'k'}I_{i'j'k'\in S_p}}.$$

**EM (p. 465).**
- E-step: $n^{\rm old}_{ijk}=\mathrm E(n_{ijk}|m,r,\theta^{\rm old})=m_{ijk}+\sum_p r_p\pi_{ijk\,p}$. DK cases are allocated to cells in proportion to the current parameters.
- M-step for the saturated multinomial: $\theta^{\rm new}=(n^{\rm old}_{ijk}+0.1)/(n+0.8)$.
- Convergence tolerance was set to the "unnecessarily low" $10^{-16}$. The posterior mode of α is 0.882, which turned out close to the eventual outcome (p. 465).

**SEM and normal approximation (p. 465).** The SEM algorithm uses the EM program and the complete-data variance matrix to estimate the posterior variance numerically. It is applied on the logit scale, where the normal approximation is generally more accurate. The 95% interval for α is [0.857, 0.903]. The standard error was inflated for the clustered design using approximate normal methods (p. 465).

**Data augmentation (pp. 465–466).** To avoid relying on asymptotic normality, data augmentation under the noninformative Dirichlet prior alternates a multinomial allocation of the $r_p$ cases with a Dirichlet draw. A total of 1000 draws came from the second half of 20 series of 100 iterations, at which point $\hat R<1.1$ for all parameters (pp. 465–466).

**Result (p. 466).** The posterior median of α is 0.883. The 95% interval, with variance inflated for clustering, is [0.859, 0.904]. It matches the asymptotic interval, as expected from the large sample. Neither crude estimate was close to the actual outcome (88.5% attended and voted yes) (p. 466).

*Intuition note.* Ignoring the DK answers (0.93) and counting them as "no" (0.69) are both far from the actual outcome. The model-based answer allocates each DK to the cells consistent with it, in proportion to what the rest of the data suggest, and lands near the true result.

### 18.7 Bibliographic note (p. 466)
Credits "missing at random", "observed at random" and "ignorability" to Rubin (1976), and multiple imputation to Rubin (1978b). It points to Little and Rubin (2002) and Van Buuren (2012) as texts, and to Tanner and Wong (1987) for data augmentation. The monotone method is attributed to Anderson (1957), extended by Rubin. The polls example is from Gelman, King and Liu (1998) and the Slovenia survey from Rubin, Stern and Vehovar (1995) (p. 466).

### 18.8 Exercises (p. 467)
Three exercises: reproduce Section 18.6 for a $2\times2$ table, create a monotone pattern in the Slovenia data, and impute General Social Survey data with several R packages (p. 467).

## Toy example (our own, not from the text)
**Goal:** estimate $\theta_{11}$ = share with A=1 and B=1, when B is sometimes missing. Missingness depends only on A (so it is MAR).

Data (140 cases): fully classified counts $m_{11}=40$, $m_{10}=10$, $m_{01}=20$, $m_{00}=30$ (total 100). In addition, $r=40$ cases have A=1 and B missing (subset $S=\{11,10\}$). No A=0 case is missing B.

Estimates (no prior, so plain EM for simplicity):
- *Complete cases only:* $40/100=0.40$.
- *Treat missing B as "0":* $40/140=0.286$.
- *EM, start θ uniform (0.25 each).*
  - Iteration 1: $\pi_{11}=0.25/(0.25+0.25)=0.5$. $n_{11}=40+40(0.5)=60$ and $n_{10}=10+20=30$. Counts (60, 30, 20, 30), total 140. $\theta_{11}=60/140=0.4286$, $\theta_{10}=0.2143$.
  - Iteration 2: $\pi_{11}=0.4286/(0.4286+0.2143)=0.667$. $n_{11}=40+40(0.667)=66.67$. $\theta_{11}=66.67/140=0.476$.
  - Iteration 3: $\pi_{11}=66.67/90=0.741$. $n_{11}=40+29.6=69.6$. $\theta_{11}=0.497$.
  - Fixed point: $\pi_{11}=40/50=0.8$ (the complete-case share of B=1 among A=1). $n_{11}=40+40(0.8)=72$, $n_{10}=10+8=18$. $\theta_{11}=72/140=0.514$.
- *Check of the fixed point:* with $\theta_{11}=72/140$ and $\theta_{10}=18/140$, $\pi_{11}=72/90=0.8$ again, so the E-step reproduces the same counts (added step).

**Lesson:** under MAR the 40 partially classified cases are filled in using what the A=1 cases with B observed look like. The result, 0.514, differs from both naive answers (0.40 and 0.286), just as in Slovenia. In each iteration the E-step allocates the 40 partial cases by the current probabilities and the M-step renormalizes the counts by 140.

## Concepts
- [[missing-data-mechanism]] (new) — the conditional law $p(I|y,\phi)$ of the inclusion indicator given the complete data (p. 450)
- [[inclusion-indicator]] (new) — array $I$ of 1s (observed) and 0s (missing), same size as $y$, assumed fully observed (p. 449)
- [[missing-at-random]] (new) — $p(I|y_{\rm obs},y_{\rm mis},\phi)=p(I|y_{\rm obs},\phi)$; mechanism may depend on observed values only (p. 450)
- [[mcar]] (new) — missingness independent of $y$ altogether, $p(I|\phi)$; rarely plausible (p. 450)
- [[ignorable-missingness]] (new) — MAR plus distinct φ, θ (independent a priori); only $p(y_{\rm obs}|\theta)$ is needed. This differs from the causal-inference use of "ignorability" listed under *Assignment mechanism / ignorability* (p. 450)
- [[nonignorable-missingness]] (new) — the mechanism is not ignorable, e.g. missingness depends on the unobserved values themselves; a valid analysis then needs a model or information about the mechanism (pp. 451–452)
- [[multiple-imputation]] (new) — several simulated completions of $y_{\rm mis}$, each analysed as complete, then combined (p. 451)
- [[rubin-combining-rules]] (new) — $\bar\theta_K$, $\overline W_K$, $B_K$, $T_K$ and a $t$ reference d.f. (p. 453)
- [[data-augmentation]] (new) — alternate imputing $y_{\rm mis}$ and drawing parameters; a special case of Gibbs sampling here (pp. 451, 465)
- [[em-algorithm]] (new) — E-step imputes expected sufficient statistics or counts, M-step updates the parameters; finds posterior modes (p. 452)
- [[monotone-missing-pattern]] (new) — variables orderable so that each block is more observed than the next; enables direct draws (p. 453)
- [[gibbs-sampling]] — used as data augmentation on $(y_{\rm mis},\theta)$ (p. 455)
- [[hierarchical-model]] — per-survey means $\mu_s$ regressed on survey covariates, with common Ψ (p. 458)
- [[conjugate-prior]] — Dirichlet prior for multinomial cell probabilities (p. 462)
- [[convergence-diagnostics]] — $\hat R<1.1$ used for data augmentation chains (p. 466)
- [[posterior-predictive-distribution]] — $y_{\rm mis}$ is drawn from its posterior predictive given $y_{\rm obs}$ (p. 449)

## Canonical instances
- [[age-income-missingness]] — three missingness cases (MCAR; MAR but not observed at random, ignorable if parameters are distinct; nonignorable) in a bivariate normal (pp. 450–451)
- [[1988-presidential-polls-imputation]] — hierarchical normal model for 51 polls with monotone data augmentation (pp. 456–462)
- [[slovenia-plebiscite-survey]] — "don't know" as missing data, estimand α, EM/SEM/data augmentation, actual 88.5% (pp. 463–466)

## Bridges (candidates)
- [structural-analogy] inclusion mechanism and ignorability here ↔ causal inference: assignment mechanism and ignorability given covariates — both ask whether the process deciding what is seen depends on the hidden values.
- [same-math] data augmentation ↔ Gibbs sampling: alternately draw $y_{\rm mis}$ and parameters from full conditionals (the text calls it a special case of Gibbs) (p. 465).
- [structural-analogy] within- plus between-imputation variance ($T_K$) ↔ hierarchical modelling: total uncertainty splits into noise inside units and variation across plausible fills.
- [structural-analogy] borrowing strength across surveys ↔ partial pooling/shrinkage: unasked questions in one survey are imputed using other surveys.
- [structural-analogy] checking imputations against observed data (Fig. 18.2b) ↔ posterior predictive checks: systematic difference signals model misfit.

## Questions this raises
- How can one assess sensitivity to a plausible nonignorable mechanism when the data cannot reveal it?
- How many imputations $K$ are enough, and when do the $t$-based combining rules fail?
- How much does the diffuse Dirichlet(0.1) prior matter when a cell count is 0 and many answers are DK?
- Can inconsistent-but-convenient imputation models (separate univariate models) be justified (the bibliographic note mentions "inconsistent Gibbs", p. 466)?

## Exercises worth doing
- Ex. 1 (p. 467) — reproduce the Slovenia analysis on the $2\times2$ table with EM, SEM and a Markov chain simulation including diagnostics; consolidates all of 18.5–18.6 — difficulty: medium
- Ex. 2 (p. 467) — make the Slovenia data monotone by discarding observations and compare with the full results; shows what monotone structure buys — difficulty: medium
- Ex. 3 (p. 467) — impute General Social Survey data with three R packages and compare logistic regressions with the complete-case fit; practical comparison of imputation methods — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 10 (pdf 459 = printed 449). The last page (pdf 478) is blank apart from the running header.
- The text layer shows ω where the page images show θ; I followed the images and used θ throughout.
- p. 458: the text says "separate matrices Φ for the two groups". The image shows Φ, though the matrix is called Ψ elsewhere; probably a typo.
- (18.9) as printed has $\prod_{q=1}^Q p(\sigma^2_Q)$; the index is probably meant to be $q$. I copied it as printed.
- p. 465: the M-step formula $(n^{\rm old}_{ijk}+0.1)/(n+0.8)$ is copied as printed ($0.8=8\times0.1$). The text calls the resulting estimate a posterior mode; I did not check this against the Dirichlet(0.1) posterior.
- The running header on every page reads "This electronic edition is for non-commercial purposes only."
- Fig. 18.1 and Fig. 18.2 were read from the images. The text does not explain the three counts shown in Fig. 18.1.

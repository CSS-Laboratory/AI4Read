---
id: gelman-2013-bda3/ch08-modeling
work: gelman-2013-bda3
unit: "8 Modeling accounting for data collection"
pages: 197–236
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Modeling accounting for data collection (BDA3, Chapter 8)

## L0 — One line
Bayesian inference must model how the data were collected (through an inclusion indicator $I$); designs that are "ignorable" let you ignore that model (while still conditioning on the design variables), and all others require it.

## L1 — The gist (≤ 120 words)
How do surveys, experiments, observational studies, and censored or missing data affect a Bayesian analysis? The chapter treats all of them as missing-data problems. It adds an inclusion indicator $I$ to the model for the complete data $y$. If the design is "ignorable" (missing at random with distinct parameters is a sufficient condition), the posterior for $\theta$ can be computed from $y_{\rm obs}$ and the model alone. Ignorable designs still require conditioning on every covariate used in the design, and they do not make model checking independent of the design. Randomization helps ignorability and reduces sensitivity to model choice. Surveys, experiments, noncompliance and censoring examples show the principle at work. Nonignorable mechanisms change the likelihood.

**Prerequisites:** Bayes' rule; hierarchical normal and multinomial–Dirichlet models (Ch. 3, 5); posterior predictive checks (Ch. 6); the central limit theorem; the normal cdf $\Phi$; the idea of potential outcomes.

## L2 — Key ideas (5–10 bullets)
- Data collection is modeled by an inclusion indicator $I$, with complete-data likelihood $p(y|\theta)\,p(I|y,\phi)$. The usable likelihood is the observed-data likelihood, which integrates out $y_{\rm mis}$ (pp. 199–201).
- A design is ignorable when $p(\theta|x,y_{\rm obs})=p(\theta|x,y_{\rm obs},I)$. Missing at random plus distinct parameters is sufficient for this (pp. 202–203).
- Ignorability supports only a weak version of "the design doesn't matter": it holds for the posterior under one fixed model. It does not cover sensitivity analysis or posterior predictive checks, and nonignorable designs change the posterior (p. 203).
- Include in the model all variables used in the design (strata, clusters, blocks, plot locations, sizes). Hierarchical models are a natural way to handle strata and clusters, and survey and experimental inference then rests on modeling $p(y|x,\theta)$ (pp. 207–217).
- Randomization gives ignorability without covariates. Given covariates, it adds a model-consistency check, flexibility in replications, protection against "cheating", and less dependence on one model (pp. 218–220).
- Observational studies are typically analyzed as if they came from an experiment; once ignorability given covariates is accepted, the usual methods apply. Poor covariate overlap can still make inference highly sensitive to the model, even if ignorability is accepted (pp. 220–222).
- Noncompliance is handled by principal stratification. The instrumental-variables estimate needs the exclusion restriction, which the Bayesian missing-data approach can relax (pp. 223–224).
- Censoring and truncation change the likelihood: censored points contribute $\Phi(\theta-\phi)$ terms. Ignoring the indicator gives a wrong likelihood (pp. 225–228).

## L3 — Walkthrough

### Intro and 8.1 Bayesian inference requires a model for data collection
Two messages (p. 197): (1) information on how the data were collected should be included, typically through a model (e.g. a regression) conditional on the design variables; (2) partial information (thresholds, missing values) should be related to the other variables by a probability model. The goal is generalization beyond the observed data to a larger population (p. 197).

**Naive view (voice: a naive student).** Because inference conditions on the data, collection is irrelevant. This is a misplaced appeal to the likelihood principle. The author's reply is that "the observed data" should include how the values arose (p. 198).

**Die example (p. 198).** Ten rolls, all 6's. Your attitude to the die differs if (i) these were the only rolls, (ii) 60 rolls were made and only the 6's reported, or (iii) the authors decided in advance to report ten 6's and concealed that it took 500 rolls.

Four principles (p. 198):
1. Use all relevant information; the pattern of what is observed can be informative.
2. Ignorable designs (Section 8.2), often randomized, are likely to give inferences less sensitive to model choice than nonignorable designs.
3. More explanatory variables make conclusions more valid conditionally but possibly more sensitive to the model.
4. Thinking about the design and the data one could have observed helps structure inference about finite-population estimands. Posterior predictive checks depend on the design through $y^{\rm rep}$.

Terminology: observed data come from a larger complete (potential) data set. "Missing" covers unintentional cases (nonresponse, censoring, noncompliance) and intentional ones (unsampled units, unobserved potential outcomes). Table 8.1 gives the pairs: sample vs population, outcomes under the applied treatment vs under all treatments, rounded vs precise values (pp. 198–199).

### 8.2 Data-collection models and ignorability
**Notation (p. 199).** $y=(y_1,\dots,y_N)$ is the matrix of potential data, with $y_{ij}$ for component $j$ of unit $i$. $I$ has the same shape. $I_{ij}=1$ means $y_{ij}$ is observed and $I_{ij}=0$ means it is missing. "obs" and "mis" index the two sets. $I$ is assumed always observed. The sample space is the product of the spaces for $y$ and $I$. This chapter writes $y_{\rm obs}$ where other chapters write $y$ (p. 199).

**Stability (p. 200).** The complete data $y$ are not affected by the inclusion pattern $I$. In experiments this is the stable unit treatment value assumption, which includes no interference between units. Example of failure: fertilizers leaching between close plots. The notation of this chapter implicitly assumes stability.

**Fully observed covariates $x$ (p. 200).** Reasons to include $x$: (1) interest in the joint distribution of $(x,y)$; (2) $x$ gives information about $y$, so $p(y|x)$ can be more precise; (3) $x$ must be included even if only $y$ matters whenever $I$ depends on $x$ (strata, blocks).

**Data and inclusion models (p. 200).**
$$p(y,I|\theta,\phi)=p(y|\theta)\,p(I|y,\phi).\tag{8.1}$$
$\theta$ parametrizes the complete data and $\phi$ the inclusion mechanism. The estimands are usually functions of $y$ (finite-population) or of $\theta$ (superpopulation); $\phi$ is usually not of scientific interest. $\theta$ and $\phi$ may be dependent in the prior, or even deterministically related (pp. 200–201).

**Observed-data likelihood (p. 201).** (8.1) is not the actual likelihood unless $y$ is fully observed. The available information is $(y_{\rm obs},I)$, so
$$p(y_{\rm obs},I|\theta,\phi)=\int p(y,I|\theta,\phi)\,dy_{\rm mis}.$$
With covariates, everything is conditional on $x$.

**Joint posterior (p. 201).** With $p(y,I|x,\theta,\phi)=p(y|x,\theta)\,p(I|x,y,\phi)$:
$$p(\theta,\phi|x,y_{\rm obs},I)\propto p(\theta,\phi|x)\int p(y|x,\theta)\,p(I|x,y,\phi)\,dy_{\rm mis}.$$
Averaging over $\phi$:
$$p(\theta|x,y_{\rm obs},I)=p(\theta|x)\iint p(\phi|x,\theta)\,p(y|x,\theta)\,p(I|x,y,\phi)\,dy_{\rm mis}\,d\phi.\tag{8.2}$$
In practice one often draws simulations of $(y_{\rm mis},\theta,\phi)$ instead of evaluating the integrals.

**Finite-population vs superpopulation (pp. 201–202).** Analysis has two steps: superpopulation inference on $p(\theta,\phi|x,y_{\rm obs},I)$, then finite-population inference using $p(y_{\rm mis}|x,y_{\rm obs},I,\theta,\phi)$. Posterior draws of $y_{\rm mis}$ are multiple imputations. They are obtained by drawing $(\theta,\phi)$ first, then $y_{\rm mis}$. If a large fraction of potential observations is observed, finite-population inferences are more robust to assumptions such as linearity than superpopulation inferences (p. 202). Predicting future complete data $\tilde y$ needs only $p(y|x,\theta)$ and the posterior of $\theta$. Predicting future observed data $\tilde y_{\rm obs}$ also needs $p(I|x,y,\phi)$ (p. 202).

**Ignorability (p. 202).** Ignoring the collection process gives
$$p(\theta|x,y_{\rm obs})\propto p(\theta|x)\int p(y|x,\theta)\,dy_{\rm mis}.\tag{8.3}$$
The design is *ignorable* (for the proposed model) when (8.3) equals (8.2). Then $\theta$ and the predictive distribution of $y_{\rm mis}$ are determined by $p(y|x,\theta)p(\theta|x)$ and $y_{\rm obs}$.

**Two sufficient conditions (p. 202).**
- *Missing at random:* $p(I|x,y,\phi)=p(I|x,y_{\rm obs},\phi)$. Given $\phi$, missingness depends only on $x$ and $y_{\rm obs}$. A deterministic rule depending only on $x$ qualifies (example: auditing tax returns with declared income above \$1 million).
- *Distinct parameters:* $p(\phi|x,\theta)=p(\phi|x)$.

By (8.2), MAR plus distinct parameters gives $p(\theta|x,y_{\rm obs})=p(\theta|x,y_{\rm obs},I)$ (p. 203).

*Intuition note.* If nothing about *which* values are missing depends on the missing values, and the mechanism's parameters are unrelated to the model's parameters, the pattern of missingness carries no information about $\theta$. You can then ignore $I$ (while conditioning on the observed covariates $x$).

**What ignorability does and does not justify (p. 203).** A relatively weak version of the claim "design doesn't matter" is true for all ignorable designs when "Bayesian inference" is interpreted strictly as the posterior under one fixed model (prior and likelihood), conditional on the data, excluding sensitivity analyses and posterior predictive checks. With fixed $p(y|\theta)$, $p(\theta)$ and $y$, the posterior varies across different nonignorable mechanisms. Mechanisms are also *known* (including known parametric families with unknown $\phi$) or *unknown*.

**Taxonomy of designs (pp. 203–204).**
- *Ignorable and known, no covariates* (simple random sampling, complete randomization): $p(I|x,y,\phi)=p(I)$ (8.4). Only $p(y|x,\theta)$ and $p(\theta)$ are needed.
- *Ignorable and known given covariates* (stratified sampling, randomized blocks): the key idea is to include in $p(y|x,\theta)$ enough $x$ to make the design ignorable. Not all such designs are equally good for all purposes.
- *Strongly ignorable* (unconfounded): $p(I|x,y,\phi)=p(I|x)$. A design ignorable but not strongly ignorable: a sequential experiment where assignment probabilities depend on earlier observed outcomes.
- *Ignorable and unknown* (nonrandom assignment on fully observed covariates): ignorable if $p(I|x,y,\phi)$ depends only on fully observed covariates and $\theta$ is distinct from $\phi$. The analysis must condition on these covariates.
- *Nonignorable and known* (censoring, rounding).
- *Nonignorable and unknown* (hardest). Example: censoring at an unknown point typically implies great sensitivity to the model for $y$. Another: in a study of therapies $j=1,\dots,J$, treatments expected to have smaller effects get larger $n_j$. Then $n_j$ would be expected to correlate with efficacy $\theta_j$, so parameters are not distinct, and a joint model for $(n_j,y_j)$ is needed. Observational studies are typically nonignorable and unknown; initial analyses treat them as ignorable but unknown.

**Propensity scores (p. 204).** For strongly ignorable designs, $\Pr(I_i=1|X)=\pi_i$ are the propensity scores. In some designs $\pi=(\pi_1,\dots,\pi_N)$ is an adequate summary of the covariates. Conditioning on $\pi$ may lose some precision but can simplify modeling and make inference more robust. Propensity scores alone never supply enough information for posterior predictive replications, because different designs can share them. Example: a completely randomized experiment with $\pi_i=\tfrac12$ and independent coin-flip assignments have the same $\pi_i$. Simple random sampling shares its propensity scores with some stratified or cluster equal-probability designs.

**Unintentional missing data (pp. 204–205).** With little missingness, assuming ignorability given observed covariates is often fine. As the fraction missing grows, ignorability becomes more critical. In observational studies of causal effects, at most half of the potential data are observed, so one must assume ignorability given covariates or model the selection process explicitly (p. 205).

### 8.3 Sample surveys

**Simple random sampling (pp. 205–206).** A population of $N$ persons; $y_i$ is weekly food spending. Units are exchangeable: $p(y)=\int\prod_i p(y_i|\theta)\,p(\theta)\,d\theta$. $I_i=1$ if person $i$ is sampled. Simple random sampling means $p(I|y,\phi)=p(I)=\binom{N}{n}^{-1}$ if $\sum I_i=n$, and $0$ otherwise. It is strongly ignorable and known, with $\pi_i=n/N$. The posterior is $p(\theta|y_{\rm obs})\propto p(\theta)\,p(y_{\rm obs}|\theta)$. The estimand is the finite-population mean
$$\bar y=\frac nN\bar y_{\rm obs}+\frac{N-n}{N}\bar y_{\rm mis}.\tag{8.5}$$
To get its posterior: draw $\theta^s$, $s=1,\dots,S$. For each, draw $y_{\rm mis}$ from $\prod_{i:I_i=0}p(y_i|\theta^s)$ and average it. Then apply (8.5). Any function of $y$ (median, mean of $\log y_i$) could be the estimand (p. 206).

**Large-sample equivalence (p. 206).** If $N-n$ is large, the CLT gives $p(\bar y_{\rm mis}|\theta)\approx{\rm N}\!\big(\mu,\tfrac1{N-n}\sigma^2\big)$ with $\mu=E(y_i|\theta)$ and $\sigma^2={\rm var}(y_i|\theta)$. If $n$ is also large, the posteriors of $\theta,\mu,\sigma$ are approximately normal. With $N,n\to\infty$ and $N/n$ fixed:
$E(\bar y_{\rm mis}|y_{\rm obs})\approx E(\mu|y_{\rm obs})\approx\bar y_{\rm obs}$, and
$${\rm var}(\bar y_{\rm mis}|y_{\rm obs})\approx{\rm var}(\mu|y_{\rm obs})+E\!\Big(\tfrac1{N-n}\sigma^2\Big|y_{\rm obs}\Big)\approx\tfrac1n s^2_{\rm obs}+\tfrac1{N-n}s^2_{\rm obs}=\tfrac{N}{n(N-n)}s^2_{\rm obs}.$$
Combined with (8.5):
$$\bar y|y_{\rm obs}\approx{\rm N}\!\Big(\bar y_{\rm obs},\Big(\tfrac1n-\tfrac1N\Big)s^2_{\rm obs}\Big).\tag{8.6}$$
(Added step: $\big(\tfrac{N-n}{N}\big)^2\cdot\tfrac{N}{n(N-n)}=\tfrac{N-n}{nN}=\tfrac1n-\tfrac1N$.) This is the formal Bayesian justification of normal-theory inference for finite-sample surveys. For normal $p(y_i|\theta)$ with the standard noninformative prior, the exact result is $\bar y|y_{\rm obs}\sim t_{n-1}\big(\bar y_{\rm obs},(\tfrac1n-\tfrac1N)s^2_{\rm obs}\big)$ (p. 206; Ex. 8.7).

*Intuition note.* When the unsampled population is huge, the mean of the unseen part is close to $\mu$, so the finite-population answer is close to the superpopulation answer (pp. 206, 208). With $N/n$ fixed, (8.6) shows the finite-population variance still differs from that of $\mu$ by a $1/N$ term.

**Stratified sampling (pp. 206–207).** $N$ units are divided into $J$ strata, with simple random samples of size $n_j$ in stratum $j$. The design is ignorable given the stratum indicators $x_{ij}$, provided we know $N_j$ and the strata of sampled units. Model each stratum with parameters $\theta_j$, usually with a hierarchical model across $\theta_j$. Finite-population inference weights strata: $\bar y=\sum_j\frac{N_j}{N}\bar y_j$. There is no requirement that $n_j/n=N_j/N$; the inference corrects automatically for over- or undersampling (p. 207).

**Example: pre-election polling (pp. 207–210).** CBS survey, 1447 adults, 16 strata crossing region (Northeast, Midwest, South, West) with density of residential area (Table 8.2, p. 207). Assumed: random sampling within strata, $N_j/N=n_j/n$, ignorable nonresponse, and the population of respondents on residential phone numbers. Complications in the real design are ignored (p. 208).
- *Data model:* $y_{\mathrm{obs}\,j}\sim{\rm Multin}(n_j;\theta_{1j},\theta_{2j},\theta_{3j})$, counts for Bush, Dukakis, other/no opinion (p. 208).
- *Nonhierarchical model:* independent Dirichlet(1,1,1) priors per stratum, so posteriors are separate. The estimand is
$$\sum_{j=1}^{16}\frac{N_j}{N}(\theta_{1j}-\theta_{2j}).\tag{8.7}$$
Superpopulation means $\theta_{kj}$ stand in for population averages $\bar y_{kj}$; with huge finite populations the two are essentially identical (p. 208).
- *Result (Fig. 8.1a):* 1000 draws are centered at 0.097 vs 0.098 in Fig. 3.2, and slightly more concentrated. The difference in centers is probably due to the prior. The stratified Dirichlet adds one voter per category per stratum (16 per category in total); a Dirichlet with parameters $\frac1{16}$ would reproduce the nonstratified median. The smaller spread is expected (pp. 208–209).
- *Hierarchical model:* transform
$$\alpha_{1j}=\frac{\theta_{1j}}{\theta_{1j}+\theta_{2j}},\qquad\alpha_{2j}=1-\theta_{3j},\tag{8.8}$$
interpreted as the probability of preferring Bush given a preference, and the probability of expressing a preference. Put $\beta_{kj}={\rm logit}(\alpha_{kj})$. Model $(\beta_{1j},\beta_{2j})$ as exchangeable across strata, bivariate normal with mean $(\mu_1,\mu_2)$ and covariance matrix with entries $\tau_1^2,\rho\tau_1\tau_2,\tau_2^2$. This ignores the $4\times4$ structure of the strata. The nonhierarchical model equals this model with $\tau_1,\tau_2$ fixed at $\infty$. Priors are uniform on the hyperparameter means and standard deviations and on the correlation. The 37-dimensional posterior is sampled with the Metropolis algorithm (p. 209).
- *Results (Table 8.3, p. 210):* posterior medians of $\alpha_{1j}$ range from 0.48 to 0.59, showing considerable shrinkage from the raw proportions 0.33 to 0.67 (p. 209). The median of $\rho$ is negative ($-0.44$) with large variability. The estimand (8.7) now has a higher median, 0.11 (Fig. 8.1b), and slightly more variability. Strata 1 and 5 had the lowest Bush support and small samples, so they are pulled toward the grand mean (p. 210).
- *Model check:* test statistic $T(y)=\min_j y_{\mathrm{obs}\,1j}/n_j$, observed value 0.298 (stratum 1). Over 1000 posterior predictive draws $T(y^{\rm rep})$ ranges from 0.14 to 0.48, with 163 of 1000 below 0.298. The extreme value is plausible under the model (p. 210).

**Cluster sampling (pp. 210–212).** $N$ units in $K$ clusters. First sample $J$ clusters, then $n_j$ of the $N_j$ units in each sampled cluster. The design is ignorable given cluster indicators and the cluster sizes. Analysis proceeds as for stratified sampling, but unsampled clusters act as additional exchangeable batches in a hierarchical model (p. 211).

*Example: Melbourne schoolchildren (pp. 211–212).* 72 schools were sampled with probability proportional to the number of classes, then two classes per school. Students, classes and schools are indexed $i,j,k$; $N_{jk}$, $M_k$, $K$ as in the text. $y_{ijk}=1$ if the student walks to school; $\bar y_{.jk}$, $\bar y_{..k}=\frac1{N_k}\sum_j N_{jk}\bar y_{.jk}$; estimand $\bar Y=\frac1N\sum_kN_k\bar y_{..k}$.
- Principle: include a parameter for each level of clustering. Class averages: $\bar y_{.jk}\sim{\rm N}(\theta_{jk},\sigma^2_{jk})$ with $\sigma^2_{jk}=\bar y_{.jk}(1-\bar y_{.jk})/N_{jk}$ (8.9), a normal approximation to the binomial. Then
$$\theta_{jk}\sim{\rm N}(\theta_k,\tau^2_{\rm class}),\qquad\theta_k\sim{\rm N}(\alpha+\beta M_k,\tau^2_{\rm school}).\tag{8.10}$$
$M_k$ is included because the sampling probabilities depend on school size, so the design is ignorable only for a model that includes the $M_k$ (p. 211).
- Four steps: (1) fit (8.9)–(8.10) with noninformative priors on $\alpha,\beta,\tau_{\rm class},\tau_{\rm school}$; (2) simulate $\theta_{jk},\theta_k$ for unsampled classes and schools via (8.10); (3) use (8.9) to infer students in unsampled classes and schools, and combine to $\bar y_{..k}$. For an unsampled school, $\bar y_{..k}\sim{\rm N}\big(\alpha+\beta M_k,\ \tau^2_{\rm school}+\tau^2_{\rm class}/M_k+\sigma^2/N_k\big)$. For a sampled school it averages over sampled and unsampled classes. (4) Combine school averages into $\bar Y$; this requires the $N_k$, which otherwise must be modeled jointly with $\theta_k$ (pp. 211–212).
- If only a small fraction of schools is sampled:
$$\bar Y\approx\frac1N\sum_kN_k\,E(\theta_k)=\frac1N\sum_kN_k(\alpha+\beta M_k).\tag{8.11}$$
This depends on $\alpha,\beta$ and the population distribution of $(M_k,N_k)$, not on the school-level $\theta_k$ (p. 212).

**Unequal probabilities of selection (p. 212).** Independent sampling with unequal probabilities is ignorable given the covariates $x$ determining the probabilities, provided the covariates are known in the sample and their distribution is known in the population. The critical step is modeling $y|x$.

*Example: Alcoholics Anonymous groups (pp. 213–214).* About 400 groups, sampled with equal probability, responded in 1997, averaging 20 surveys each; about 6000 were unsampled. For a binary response, $y_j\sim{\rm Bin}(n_j,\theta_j)$ (finite-population correction ignored; the main uncertainty is in unsampled clusters). The estimand is
$$\bar Y=\frac{\sum_{j=1}^Kx_j\theta_j}{\sum_{n=1}^Kx_j},\tag{8.12}$$
where $x_j$ is the average number of people attending group $j$. Model $p(x_j,\theta_j)=p(x_j)p(\theta_j|x_j)$:
$$x_j\sim{\rm N}(\mu_x,\tau_x^2),\qquad\theta_j\sim{\rm N}(\alpha+\beta x_j,\tau_\theta^2).\tag{8.13}$$
This ignores the constraints $0<\theta_j<1$ and $x_j>0$ but is convenient. Simplified likelihoods: $y_j/n_j\approx{\rm N}(\theta_j,\sigma_j^2)$ with $\sigma_j^2=y_j(n_j-y_j)/n_j^3$ (8.14); $n_j\approx{\rm N}(\pi x_j,\pi x_j)$ (8.15), a normal approximation to a Poisson with mean $\pi x_j$, where $\pi$ is the response probability. With uniform priors on $\alpha,\beta,\tau_x,\tau_\theta,\pi$ this is a bivariate hierarchical normal model (p. 213). With many unobserved clusters, $\bar Y\approx E(x_j\theta_j)/E(x_j)$, so
$$\bar Y=\frac{\alpha\mu_x+\beta(\mu_x^2+\tau_x^2)}{\mu_x}.\tag{8.16}$$
(Added step: $E(x\theta)=E[x(\alpha+\beta x)]=\alpha\mu_x+\beta E(x^2)$.) If $\theta_j$ and $x_j$ are independent, $\beta=0$ and (8.16) reduces to $\alpha$; otherwise each group is counted in proportion to its size (p. 214). With many categories, hierarchical models may be needed (p. 214).

### 8.4 Designed experiments (pp. 214–218)
An experiment assigns treatments under the experimenter's control. Inference must generalize to hypothetical outcomes under other assignments and, typically, to other units (p. 214).

**Completely randomized experiments (pp. 214–216).** With $n$ even, half get A and half B. Complete data are $(y_i^A,y_i^B)$, an $n\times2$ matrix, which requires stability. The unit causal effect is $y_i^A-y_i^B$. Superpopulation effect: $E(y_i^A-y_i^B|\theta)=E(y_i^A|\theta)-E(y_i^B|\theta)$. Finite-population effect: $\bar y^A-\bar y^B$ (p. 214).
- Inclusion: $I_i=(1,0)$ for A, $(0,1)$ for B, $(0,0)$ for neither; both cannot be 1. For complete randomization $p(I)=\binom{n}{n/2}^{-1}$ if $\sum I^A_i=\sum I^B_i=n/2$ and $I_i^A\ne I_i^B$ for all $i$; else 0. It is known and ignorable (p. 215).
- Superpopulation: $p(\theta|y_{\rm obs})\propto p(\theta)p(y_{\rm obs}|\theta)$, with $p(y_{\rm obs}|\theta)=\prod_{I_i=(1,0)}p(y_i^A|\theta)\prod_{I_i=(0,1)}p(y_i^B|\theta)$. This allows separate analysis of $\theta_A$ and $\theta_B$ (p. 215).
- Finite-population: $p(y_{\rm mis}|\theta,y_{\rm obs})=\prod_{I_i=(1,0)}p(y_i^B|\theta,y_i^A)\prod_{I_i=(0,1)}p(y_i^A|\theta,y_i^B)$ requires a model for $p(y_i^A,y_i^B|\theta)$. The parameters $\theta_{AB}$ of the joint distribution do not appear in the likelihood. Their posterior comes from the conditional prior $p(\theta_{AB}|\theta_A,\theta_B)$ averaged over the posterior of $\theta_A,\theta_B$ (p. 215).
- Large-sample correspondence: finite-population inference on $\bar y^A-\bar y^B$ is sensitive to ${\rm corr}(y^A_i,y^B_i|\theta)$, about which there are no data. The sensitivity vanishes for large populations when the estimand compares only $\theta_A$ and $\theta_B$. If the $n$ units are a random sample from $N$ units and the target is the mean difference for all $N$, then for large $n$ and $N/n$ (Ex. 8.8)
$$(\bar y^A-\bar y^B)|y_{\rm obs}\approx{\rm N}\!\Big(\bar y^A_{\rm obs}-\bar y^B_{\rm obs},\ \tfrac2n\big(s^{2A}_{\rm obs}+s^{2B}_{\rm obs}\big)\Big).\tag{8.17}$$
The author calls the similarity to repeated-sampling randomization results "striking, but not entirely unexpected" (pp. 215–216).

**Randomized blocks, Latin squares (p. 216).** Model outcomes conditional on all factors used in assigning treatments.

*Example: Latin square (Table 8.4, p. 216).* Millet yields on 25 plots, treatments A–E (spacings 2–10 inches). Complete data $y$ are $25\times5$, with one entry observed per row. $I$ is a fully observed $25\times5$ 0/1 matrix. The relevant design factor is plot location, a $25\times2$ matrix $x$. An ignorable model has the form $p(y|x,\theta)$, and one can infer $\theta$ from $p(y_{\rm obs}|x,\theta)$. A starting point is a linear additive model on log yields with row, column and treatment effects, possibly with treatment-by-location interactions. Analysis has two parts: superpopulation inference for $y$ given treatments and $x$, then finite-population inference averaging over the $x$ of the 25 plots. If told the data came from a completely randomized experiment that happened to be balanced, the analysis should not change. A simpler $p(y|\theta)$ would be valid, but conditioning on location is more relevant and would tend to be more precise if location effects are modeled appropriately (pp. 216–217; Ex. 8.6).

**Sequential designs (p. 217).** Claims that Bayesian analysis of sequential experiments is "essentially impossible" or "trivial" (analyze as if completely randomized) are both rejected by the author. The design is ignorable conditional on all variables used in allocation (time of entry, earlier outcomes). It is not strongly ignorable (Ex. 8.15).

**Adequate summary (p. 217).** The minimal set of design variables needed for ignorability, with treatment and outcome, is an *adequate summary*; the corresponding inference is a *minimal analysis*. Propensity scores can sometimes serve as one. It is generally advisable to use additional available information. Example: a simple random sample of 100 from a population known to be 51% female. Model responses given sex and average over the known proportions, as with a stratified sample (posterior predictive checks can still use the simple random sampling design). If the population proportions are unknown, sex is not fully observed and they must be estimated. The joint analysis could in principle be informative, but the adequate summary might be more appealing in practice (p. 217).

**Example: cows and re-randomization (pp. 217–218).** 50 cows, four feed-additive levels, three pre-treatment covariates (lactation number, age, initial weight), six outcomes. Random assignments were tried and the one with the best covariate balance was kept. The assignment is ignorable (depends only on recorded covariates) but unknown (re-randomization decisions unexplained). $x$ is $50\times3$; $y$ is $50\times24$, with one of four 6-vectors observed per unit. The minimal analysis models mean daily milk fat given treatment and covariates, assuming distinct parameters. The author says reasonable violations should not have large effects (Ex. 8.3). A linear additive model after transformations seems reasonable. Finite-population estimands are probably not of interest, since the 50 cows are not of particular interest. If the goal is more generally to understand treatment effects, it would be better to model the six outcomes jointly; after appropriate transformations a multivariate normal regression could make sense. If $\phi$ is not distinct from $\theta$ (e.g. assignment depends on the experimenter's belief about efficacy), modeling $y$ is not the only issue. For fixed model and data the posterior is identical for all ignorable collection models, but better designs are likely to yield less model-sensitive data; here explicit balancing over the covariates, most simply a randomized block design, would have been better (p. 218).

### 8.5 Sensitivity and the role of randomization (pp. 218–220)
Posterior inference for $\theta$ and $y_{\rm mis}$ is completely insensitive to the details of an ignorable design, given a fixed model (p. 218).

**Complete randomization (pp. 218–219).** With no fully observed covariates, the only way to get an ignorable design (assignment distribution invariant to permutation of indices, excluding degenerate designs) is to randomize. Some ignorable designs are better than others. For 10 subjects and two treatments with a noninformative prior, assigning a random half to each is generally better than independent coin flips, because expected posterior precision is higher with equal groups.

**Randomization given covariates (p. 219).** Randomized designs compete with deterministic ignorable designs (propensity scores 0 or 1). Example: 12 adjacent plots, fertilizers A and B; random assignment of six each vs the systematic ABABABBABABA. Both are ignorable given location $x$. Advantages of randomization:
- An analysis pretending $x$ unknown is still valid. Compare $p(y_{\rm mis}|y_{\rm obs})$ with the updated $p(y_{\rm mis}|y_{\rm obs},x)$. They should be consistent, with the second more precise. If not, reconsider the model. A systematic design lacks this check without averaging over a distribution of $x$.
- More flexibility for posterior predictive checks, since replications give different assignments.
- A single systematic design is sensitive to particular assumptions about $y|x$, and repeating it makes inferences systematically dependent on them.

**Designs that "cheat" (pp. 219–220).** Randomization makes it harder for an experimenter to bias assignments (e.g. A to sunny plots, B to shaded). Complications: (1) assignment depends on unrecorded covariates: nonignorable, so unknown selection effects must be modeled, which is difficult and sensitive; (2) assignment depends on recorded covariates: $p(y|x,\theta)$ must be modeled and inference may be highly sensitive. If all sunny plots get A and all shaded get B, the treatment and sunny/shaded indicators coincide and the likelihood cannot separate them; (3) even a randomized design can be nonignorable if parameters are not distinct. Example: an experimenter randomizes completely when expecting large effects and uses blocks when expecting small effects, so $\phi$ and $\theta$ are dependent in the prior. One can often ignore this if the data dominate the prior.

**Nonrandomized studies (p. 220).** Example: an interviewer questions all adults passing a street corner from 11 am to noon. (1) Nonignorable model: inclusion depends on travel pattern, unobserved for the $N-n$ non-sampled adults, so a model for $I$ given $y$ is needed. (2) Ignorable model: inclusion depends on an observed indicator $x_i$ (passed by or not), but there is no data when $x=0$. Either way, inference for $\bar y$ is highly sensitive to the prior unless $n/N$ is close to 1. With covariates and a roughly balanced nonrandomized ignorable design, inferences are typically less sensitive. Any strongly ignorable design is implicitly randomized over variables not in $x$: units with identical $x$ have equal propensity scores. The usual goal is an ignorable model so one can work with $p(\theta|x,y_{\rm obs})\propto p(\theta)p(x,y_{\rm obs}|\theta)$.

### 8.6 Observational studies (pp. 220–224)
In an observational study, treatments are observed, not controlled by the experimenter. Experiments are often but not necessarily randomized (the SAT coaching study of Section 5.5 is experimental). In randomized experiments, groups are similar on average or differ in known ways. In observational studies, groups can differ greatly and by unmeasured factors (pp. 220–221).

**Five conditions for a well-conducted observational study (p. 221):** (1) controls well for background differences; (2) enough independent units per treatment for narrow posterior intervals; (3) design made without reference to the analysis outcome; (4) attrition, dropout and other missing data minimized or properly modeled; (5) analysis accounts for design information. Systematic pre-treatment differences should be included in the analysis through covariates or a realistic nonignorable model. Minor differences can be controlled by regression; with larger differences, posterior inferences become highly sensitive to the functional form. In some cases estimated propensity scores can help by restricting to treated and control units with similar covariate distributions.

**Figure 8.2 (pp. 221–222).** Hypothetical single-covariate data: (a) balanced, like a randomized experiment, with a treatment-effect estimate relatively insensitive to the model form; (b, c) unbalanced data (e.g. a training program taken only by people with higher incomes). A linear fit in (b) gives a positive effect. In (c) the same data fit just as well by a mildly nonlinear relation with no treatment effect. Estimated propensity scores diagnose this: with (b, c) there is little or no overlap between the two treatment groups. This works with multivariate $X$ because the score is a scalar (p. 222).

**Bayesian inference (p. 222).** Gather many covariates so assignment is close to ignorable given them, then analyze as an experiment with assignment probabilities depending on those covariates (illustrated in Section 14.3). Without enough covariates, sensitivity to plausible missing-data models can be so great that the data may provide essentially no information. Inference can be sensitive even under accepted ignorability if covariate overlap is poor. Design methods (matched sampling, subclassification, blocking, stratification) limit extrapolation in $x$-space. Bayesian techniques that arise naturally include post-stratification and analysis of covariance: infer conditional on covariates and then average over their population distribution. Two difficulties: (1) unbalanced treatments; (2) assignment depending on unknown or unmeasurable factors, making $\theta$ sensitive to the nonignorable assignment model (p. 222). Covariate information generally increases expected precision and, if well done, reduces sensitivity, but too much blocking can make modeling more difficult and sensitive (p. 223; Ex. 8.6).

**Principal stratification (p. 223).** For an intermediate outcome $C$ with potential outcomes $C(1),C(0)$, the observed value is $C_{{\rm obs},i}=I_iC_i(1)+(1-I_i)C_i(0)$. Treating $C_{\rm obs}$ as a covariate is a common mistake unless $C(1)\equiv C(0)$. The correct procedure stratifies on the joint values $(C(1),C(0))$, unaffected by $I$ and so treatable as a vector covariate. This is principal stratification. The most common case is compliance. It bridges to instrumental variables and to "islands" between perfect randomized experiments and purely observational studies.

*Example: vitamin A in Indonesia (Table 8.5, p. 223).* Vitamin A was available only to those assigned to it. Strata: compliers and noncompliers. They are observed for units assigned to treatment but not for controls. $C_i(0)=0$ for everyone. Counts (assignment, exposure, survival → units): (0,0,0) 74; (0,0,1) 11514 (both complier or never-taker); (1,0,0) 34; (1,0,1) 2385 (never-takers); (1,1,0) 12; (1,1,1) 9663 (compliers).

**CACE and instrumental variables (p. 224).** The overall effect of assignment is
$$\bar Y^1-\bar Y^0=p_c\cdot{\rm CACE}+(1-p_c)\cdot{\rm NACE},\tag{8.18}$$
with $p_c$ the proportion of compliers. This is the intention-to-treat effect. It is estimated by $\bar y_1-\bar y_0$; $p_c$ is estimated by the proportion of compliers among those assigned treatment. Under the *exclusion restriction* (assignment has no effect on mortality for noncompliers, so NACE $=0$):
$$\widehat{\rm CACE}=(\bar y_1-\bar y_0)/\hat p_c,\tag{8.19}$$
the instrumental variables estimate.

**Bayesian approach (p. 224).** The author calls (8.19) a method-of-moments estimate that is "generally far from satisfactory". The Bayesian approach treats unknown compliance status in the control group as missing data. It can relax the exclusion restriction. A more complex case is influenza-shot encouragement, with two kinds of noncompliers. Computation uses iterative simulation (Part III).

*Intuition note.* Compliance is an outcome of assignment, so you cannot "adjust for" it as if it were a pre-treatment variable. You can adjust for what each person *would* do under each assignment. For controls this is unobserved, hence a missing-data problem.

### 8.7 Censoring and truncation (pp. 224–228)
Setup (p. 225): initially $N=100$ weighings $y_i\sim{\rm N}(\theta,1)$ of an object, uniform prior on $\theta$, with only $n=91$ observed in every variation; $\bar y_{\rm obs}$ is the observed mean.

1. **Missing completely at random** (p. 225): $I_i\sim{\rm Bernoulli}(0.9)$ independent of $y$. Although $n$ is binomial, $p(\theta|y_{\rm obs},I)=p(\theta|y_{\rm obs})={\rm N}(\theta|\bar y_{\rm obs},1/91)$, as if $n=91$ were fixed.
2. **MCAR, unknown selection probability $\pi$** (p. 225): the posterior for $\theta$ matches variation 1 only if $\theta$ and $\pi$ are independent a priori (distinct). Otherwise $n$ carries extra information. Example: if $\pi=\theta/(1+\theta)$, then $n/N=91/100$ estimates $\pi$ and thus $\theta=\pi/(1-\pi)$, even without the measurements. Formally $p(\theta,\pi|y_{\rm obs},I)\propto p(\theta,\pi)\,{\rm N}(\theta|\bar y_{\rm obs},1/91)\,{\rm Bin}(n|100,\pi)$; with $\pi=\theta/(1+\theta)$, $p(\theta|y,I)\propto{\rm N}(\theta|\bar y_{\rm obs},1/91)\,{\rm Bin}(n|100,\theta/(1+\theta))$. It can be computed numerically and simulated by the inverse-cdf method.
3. **Censored at 200 kg** (p. 226): 91 numerical values and 9 "too heavy". The 9 contribute $\Phi(\theta-200)$ each. Inclusion: ${\rm Pr}(I_i=1|y_i)=1$ if $y_i\le200$, else 0. $p(\theta|y_{\rm obs},I)\propto p(\theta)\prod_{i=1}^{91}{\rm N}(y_{\mathrm{obs}\,i}|\theta,1)\prod_{i=1}^{9}\Phi(\theta-200)\propto{\rm N}(\theta|\bar y_{\rm obs},1/91)[\Phi(\theta-200)]^9$. Numerical, with inverse-cdf simulation.
4. **Censoring point $\phi$ unknown** (pp. 226–227): the 9 contributions are $\Phi(\theta-\phi)$. Even if $\theta,\phi$ are independent a priori, they become dependent in the posterior, so the joint $p(\theta,\phi)$ is needed:
$$p(\theta,\phi|y_{\rm obs},I)\propto p(\phi|\theta)\,{\rm N}(\theta|\bar y_{\rm obs},1/91)[\Phi(\theta-\phi)]^9\,1_{\phi>\max(y_{\rm obs})}.$$
Computed on a grid. Formal derivation: the complete-data likelihood is $p(y|\theta)=\prod_{i=1}^{100}{\rm N}(y_i|\theta,1)$ and $p(I|y,\phi)=\prod_i p(I_i|y_i,\phi)$ with factor 1 if ($I_i=1$ and $y_i\le\phi$) or ($I_i=0$ and $y_i>\phi$), else 0 (p. 226). Then
$$p(y_{\rm obs},I|\theta,\phi)=\int p(y|\theta,\phi)p(I|y,\theta,\phi)\,dy_{\rm mis}=\prod_{i:I_i=1}{\rm N}(y_i|\theta,1)\prod_{i:I_i=0}\int_\phi^\infty{\rm N}(y_i|\theta,1)\,dy_i=\prod_{I_i=1}{\rm N}(y_i|\theta,1)\prod_{I_i=0}\Phi(\theta-\phi)\propto{\rm N}(\theta|\bar y_{\rm obs},1/91)[\Phi(\theta-\phi)]^9.\tag{8.20}$$
$\phi$ cannot be ignored, so the mechanism is nonignorable. Using $p(y_{\rm obs}|\theta)=\prod_{i=1}^{91}{\rm N}(y_{\mathrm{obs}\,i}|\theta,1)$ is wrong because it omits the censored-observation factors (p. 227).

5. **Truncation at 200, $N$ unknown** (pp. 227–228): only the 91 values are provided, with no count of weighings. Censoring loses the values beyond the point but keeps their number; truncation loses the number too (p. 227). Each observed point has likelihood equal to a normal density divided by $\Phi(200-\theta)$. Equivalently, treat $N$ as unknown:
$$p(\theta,N|y_{\rm obs},I)\propto p(\theta,N)\binom N{91}{\rm N}(\theta|\bar y_{\rm obs},1/91)[\Phi(\theta-200)]^{N-91}.$$
With $p(\theta,N)\propto1/N$, summing over $N\ge91$ gives a negative-binomial-form sum, so
$$p(\theta|y_{\rm obs},I)\propto{\rm N}(\theta|\bar y_{\rm obs},1/91)\sum_{N=91}^\infty\binom{N-1}{90}[\Phi(\theta-200)]^{N-91}={\rm N}(\theta|\bar y_{\rm obs},1/91)[1-\Phi(\theta-200)]^{-91}.$$
So there are two routes to the same posterior: the truncated likelihood, or censoring with $p(N)\propto1/N$ (p. 228).

6. **Truncation point $\phi$ unknown** (p. 228): the posterior for $\theta$ mixes the known-point posteriors over the posterior of $\phi$. Unlike censoring (variation 4), where the proportion observed is informative about $\phi$, here this information is absent. With $p(N|\theta,\phi)\propto1/N$: $p(\theta,\phi|y_{\rm obs},I)\propto p(\theta,\phi)\,{\rm N}(\theta|\bar y_{\rm obs},1/91)[1-\Phi(\theta-\phi)]^{-91}$. With a noninformative prior this implies an improper posterior for $\phi$ (the factor approaches 1 as $\phi\to\infty$). The marginal is $p(\theta|y_{\rm obs})={\rm N}(\theta|\bar y_{\rm obs},1/91)$, as in variation 1.

*Intuition note.* The same 91 numbers can give different posteriors depending on how the 9 other readings were lost. Seeing "too heavy" 9 times adds the factor $[\Phi(\theta-200)]^9$, which favors larger $\theta$. With truncation at an unknown point, the lost count carries no information about $\phi$ and the marginal posterior for $\theta$ returns to the variation 1 form (p. 228).

**More complicated patterns (p. 228).** Rounded or binned data (Ex. 3.5) and coarse categories (e.g. "Christian", Section 18.6) need a generalized notation where $I_i$ indicates which set in the sample space $y_i$ belongs to.

### 8.8 Discussion (p. 229)
The method of data collection dictates the minimal modeling needed: condition on all information used in the design (strata, clusters, blocks). A sufficiently conditional analysis can ignore the mechanism for inference, though not necessarily for model checking. Once all needed variables are recorded, one can proceed with the methods of the other chapters, notably regression models $p(y_{\rm obs}|x,\theta)$ as in Parts IV–V. The author says the practical advantages of Bayes come from accounting for uncertainty in multiparameter settings and from hierarchical modeling of the collection and underlying processes.

### 8.9 Bibliographic note (pp. 229–230)
Rubin (1976) first presented ignorability, missing at random and distinctness of parameters. Neyman (1923) is credited with potential outcomes in randomized experiments; Rubin (1974b) extended them to observational studies. Rosenbaum and Rubin (1983a) introduced "strongly ignorable" and propensity scores; Frangakis and Rubin (2002) introduced "principal stratification". The Australian school survey is described in Carlin et al. (1997). The vitamin A experiment is treated in Imbens and Rubin (1997).

### 8.10 Exercises (pp. 230–236)
Seventeen exercises: confusing randomization, exchangeability and ignorability (1); distinct parameters in the milk experiment (3); interference between plots (4); a penicillin randomized-blocks experiment (5–6); derivations for simple random sampling and randomized experiments (7–8); cluster sampling (9–10); capture–recapture (11); unequal-probability analyses of the CBS phone-line data (12–13); rounded data (14); sequential biased-coin assignment (15); vitamin A noncompliance (16); clustering in cell-culture dishes (17).

## Toy example (ours, not from the text)
Weigh an object $N=4$ times, $y_i\sim{\rm N}(\theta,1)$. The scale reports values up to 10 and prints "too heavy" above 10. We see $y=8.5,\ 9.5$ and two "too heavy". Use a uniform prior on a three-point grid $\theta\in\{9,10,11\}$ (our simplification).

Normal part, proportional to $\exp\{-\tfrac12[(8.5-\theta)^2+(9.5-\theta)^2]\}$:
- $\theta=9$: sum of squares $0.25+0.25=0.5$, giving $e^{-0.25}=0.7788$.
- $\theta=10$: $2.25+0.25=2.5$, giving $e^{-1.25}=0.2865$.
- $\theta=11$: $6.25+2.25=8.5$, giving $e^{-4.25}=0.01426$.

*Wrong (ignoring $I$):* the sum is $1.0796$, so the posterior is $(0.721,\ 0.265,\ 0.013)$.

*Correct (as in variation 3, with 200 replaced by 10):* each "too heavy" contributes ${\rm Pr}(y>10|\theta)=\Phi(\theta-10)$. Squared for two readings:
- $\theta=9$: $\Phi(-1)^2=0.1587^2=0.02519$.
- $\theta=10$: $0.5^2=0.25$.
- $\theta=11$: $\Phi(1)^2=0.8413^2=0.7078$.

Products: $0.7788\times0.02519=0.01961$; $0.2865\times0.25=0.07163$; $0.01426\times0.7078=0.01009$. Sum $=0.10133$. The posterior is $(0.194,\ 0.707,\ 0.100)$. Ignoring the censoring puts most mass on $\theta=9$; accounting for it moves the mode to $\theta=10$, because two readings above 10 are very unlikely at $\theta=9$.

## Concepts
- [[assignment-mechanism-ignorability]] — design is ignorable when $p(\theta|x,y_{\rm obs})=p(\theta|x,y_{\rm obs},I)$; sufficient: missing at random plus distinct parameters (pp. 202–203)
- [[inclusion-indicator-model]] (new) — $I$ records which elements of $y$ are observed; $p(y,I|\theta,\phi)=p(y|\theta)p(I|y,\phi)$ (pp. 199–200)
- [[observed-data-likelihood]] (new) — $p(y_{\rm obs},I|\theta,\phi)=\int p(y,I|\theta,\phi)\,dy_{\rm mis}$ (p. 201)
- [[missing-at-random]] (new) — $p(I|x,y,\phi)=p(I|x,y_{\rm obs},\phi)$; includes deterministic rules based on $x$ (p. 202)
- [[distinct-parameters]] (new) — $p(\phi|x,\theta)=p(\phi|x)$ (p. 202)
- [[strongly-ignorable-design]] (new) — $p(I|x,y,\phi)=p(I|x)$ (p. 203)
- [[finite-population-vs-superpopulation-estimand]] (new) — functions of $y$ vs functions of $\theta$ (p. 200)
- [[multiple-imputation]] (new) — posterior draws of $y_{\rm mis}$ given draws of $(\theta,\phi)$ (p. 201)
- [[propensity-score]] — $\Pr(I_i=1|X)=\pi_i$ in a strongly ignorable design; not sufficient for posterior predictive replications (p. 204)
- [[sutva]] — stability: no interference, $y$ unaffected by $I$ (p. 200)
- [[potential-outcomes]] — complete data hold outcomes under all treatments (pp. 198, 214)
- [[hierarchical-model]] — used across strata, clusters and groups (pp. 207, 209, 211)
- [[partial-pooling-shrinkage]] — stratum estimates pulled toward the grand mean (p. 209)
- [[posterior-predictive-check]] — depends on the design via $y^{\rm rep}$; used with $T=\min_j y_{\mathrm{obs}\,1j}/n_j$ (pp. 198, 210)
- [[adequate-summary-minimal-analysis]] (new) — minimal set of design variables needed for ignorability (p. 217)
- [[principal-stratification]] (new) — stratifying on the joint potential intermediate outcomes $(C(1),C(0))$ (p. 223)
- [[cace-instrumental-variables]] (new) — $\widehat{\rm CACE}=(\bar y_1-\bar y_0)/\hat p_c$ under the exclusion restriction (p. 224)
- [[censoring-vs-truncation]] (new) — censoring keeps the count of lost observations, truncation does not (p. 227)

## Canonical instances
- [[die-rolls-reporting]] — ten 6's interpreted differently under three reporting rules (p. 198)
- [[cbs-1988-poll-stratified]] — 16-stratum multinomial and hierarchical analysis (pp. 207–210)
- [[melbourne-school-walking]] — two-stage cluster sampling with probability proportional to size (pp. 211–212)
- [[aa-groups-survey]] — unequal probabilities with jointly modeled size and response (pp. 213–214)
- [[millet-latin-square]] — ignorable model given plot location (p. 216)
- [[cow-methionine-experiment]] — re-randomization: ignorable but unknown (pp. 217–218)
- [[vitamin-a-noncompliance]] — Indonesian experiment, CACE (pp. 223–224)
- [[weighing-censoring-truncation]] — six-variation example showing how collection changes the posterior (pp. 225–228)

## Bridges (candidates)
- [structural-analogy] Ignorability (MAR + distinct parameters) ↔ causal inference: ignorable assignment given covariates / unconfoundedness — the text treats assignment as a missing-data mechanism.
- [same-math] Strongly ignorable assignment, $p(I|x,y,\phi)=p(I|x)$ ↔ causal inference: propensity-score theory — the chapter defines propensity scores from this condition.
- [structural-analogy] CACE with exclusion restriction ↔ econometrics: instrumental variables (Wald-type ratio, (8.19)).
- [structural-analogy] Stratum-level shrinkage in the CBS poll ↔ Bayesian inference: partial pooling in the Ch. 5 hierarchical models.
- [structural-analogy] Censored likelihood term $\Phi(\theta-\phi)$ ↔ survival analysis: contributions from right-censored observations.

## Questions this raises
- When stratified or cluster designs have many covariates, how much blocking is too much? The text points to Ex. 8.6 but gives no rule.
- How should one choose and test a model for a nonignorable mechanism when $\phi$ and $\theta$ are not distinct and the data barely inform $\phi$ (variation 6, improper posterior)?
- How sensitive are CACE results to relaxing the exclusion restriction, and what extra information would identify it?
- Does re-randomization (the cow example) affect posterior predictive checks, given the unexplained "re-randomize" decisions?

## Exercises worth doing
- Ex. 8.1 (p. 230) — separates randomization, exchangeability and ignorability, each of which the chapter uses — difficulty: medium
- Ex. 8.7 (p. 232) — derive the exact and asymptotic (8.6) posteriors for the finite-population mean — difficulty: medium
- Ex. 8.8 (p. 232) — derive (8.17) and see why dependence on $\rho$ vanishes for large $N/n$ — difficulty: hard
- Ex. 8.11 (p. 233) — capture–recapture as a missing-data/sampling model with partially known tags — difficulty: medium
- Ex. 8.15 (p. 235) — biased-coin sequential design and what must be recorded for ignorability — difficulty: medium
- Ex. 8.16 (p. 235) — ignorability, ITT and IV estimate on the vitamin A data — difficulty: easy

## Reading notes
- Printed page = pdf − 10 (pdf 207 = printed 197).
- The text layer shows $\theta$ as "ω" and has other garbled symbols (e.g. "→" for "−" and "∼"). I used the page images and wrote $\theta$.
- (8.12) prints the denominator index as "$n=1$" ("$\sum_{n=1}^K x_j$"). The sum is clearly over groups $j$.
- p. 209 refers to posterior inference for a "37-dimensional parameter vector $(\beta,\mu_1,\mu_2,\sigma_1,\sigma_2,\tau)$". The hyperparameters defined on the same page are $(\mu_1,\mu_2,\tau_1,\tau_2,\rho)$; 32 betas plus 5 hyperparameters give 37.
- p. 210 refers to Figure 8.1b as "on page 208"; this uses printed page numbers.
- Exercise solutions are not printed in these pages. Table 8.2's last column is described as sample proportions $n_j/n$.

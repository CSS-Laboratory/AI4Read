---
id: gelman-2013-bda3/ch19-parametric
work: gelman-2013-bda3
unit: "19 Parametric nonlinear models"
pages: 471–486
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Parametric nonlinear models (BDA3, Chapter 19)

## L0 — One line
When parameters and predictors do not combine linearly, the usual Bayesian recipe (build the model, compute the posterior, check the fit) still applies, but each problem generally has to be tackled afresh: it needs its own model, its computation can be challenging, and sometimes new graphical checks are needed. Two worked examples show how.

## L1 — The gist (≤ 120 words)
How do we do Bayesian analysis when the mean function is not a linear predictor? The chapter gives no general menu. It gives two case studies. (1) A serial dilution assay: a four-parameter logistic calibration curve with non-constant variance recovers concentrations, even from readings the standard software calls "below detection limit". (2) Population toxicokinetics: a hierarchical model around a differential-equation body model, with informative priors from the literature and a Gibbs/Metropolis sampler. The point is that a good model, prior information and Bayesian inference combine to give estimates where the simpler approaches discussed (standard assay software; direct measurement or animal extrapolation) do not.

**Prerequisites:** Bayesian hierarchical models; normal and lognormal distributions; Gibbs sampling and the Metropolis algorithm; R-hat; basic ordinary differential equations (first-order).

## L2 — Key ideas (5–10 bullets)
- Nonlinear models are presented as general principles plus case studies, not a systematic menu. Fitted nonlinear relations should be displayed graphically, because parameters are hard to read off directly (p. 471).
- Serial dilution assay: the mean reading follows a four-parameter curve $g(x,\beta)$ (19.1). The variance grows with the mean through the exponent $2\alpha$ (19.2). The unknown concentrations are parameters, linked to wells by dilution factors (19.4) (pp. 474–475).
- Bayesian fit of the assay yields estimates for all ten unknowns, including Unknown 8, which the standard method labels "below detection limit". The Bayesian estimates agree more closely between the two data halves (pp. 473, 476).
- Toxicokinetic model: a four-compartment differential-equation model has 15 physiological parameters per person. Estimating mixtures of exponentials is ill-conditioned, so informative priors with physical meaning are essential (pp. 478–479).
- Constrained parameters (shares summing to 1 or to 0.873) are handled by the transform (19.5). The population model is truncated normal on the transformed scale (p. 480).
- Priors separate two sources of variation: uncertainty about the population average ($S_l$) and variation among people ($\tau_l$) (pp. 480–481).
- Computation: Gibbs sampler with Metropolis steps for $\psi_k$, one person at a time, because evaluating the ODE solution $g_m$ is the costliest step (p. 482).
- Checks: relative residuals, plus external validation on a second experiment. This showed misfit in the first 15 minutes (pp. 483–485).
- Five features must work together: physiological model, population model, prior information, data, Bayesian inference (p. 485).

## L3 — Walkthrough

### Chapter introduction (p. 471)
- Part IV's linear regression gives a "menu": response distributions, transformations, linear predictors. A generalized linear model has $\mathrm{E}(y|X,\beta)=g^{-1}(X\beta)$. Robust (Ch. 17) and mixture (Ch. 22) models add a latent parameter per data point (p. 471).
- This chapter treats parameters and predictors that do not combine linearly. Examples: a ratio $\mathrm{E}(y)=\frac{a_1+b_1x_1}{a_2+b_2x_2}$, or a sum $\mathrm{E}(y)=A_1e^{-\alpha_1x}+A_2e^{-\alpha_2x}$ (Exercise 19.3) (p. 471).
- The general principles of inference apply directly. Three steps: model building, computation, model checking.
  - The most flexible approaches typically involve complicated predictor–outcome relations, but generally without needing unusual probability distributions.
  - Computation can present challenges, because linear-regression computations (as in Ch. 16) cannot simply be adapted.
  - Checking can use residual plots and $\chi^2$ tests, but sometimes new graphs are needed.
  - Interpretation is harder; a key step is to plot the fitted nonlinear relation (p. 471).
- There is no systematic menu, so each problem is tackled afresh; two examples follow (p. 471).

### 19.1 Example: serial dilution assay (pp. 471–476)

**Design.** Concentration is read from an optical colour change. The colour change is informative only in a limited range: it is imperceptible at low values and saturates at high values. So each sample is measured at several dilutions, which gives measurements of differing accuracy to be combined (p. 471).
- Wells hold *unknowns* (samples to measure) or *standards* (dilutions of a known compound, used to calibrate). A 96-well plate: two columns of standards, ten columns of unknowns (Fig. 19.1). Dilutions for unknowns are more widely spaced, to cover a wider range (p. 472).
- Data: one plate from a study of cockroach allergens in homes of asthma sufferers (Fig. 19.2). The goal is to scale the $x$-axes of the unknowns so they line up with the curve estimated from the standards (p. 472).

**Problem with the standard method (Fig. 19.3).** The standards have concentrations 0.64 down to 0, and readings fall from above 100 to about 14 (p. 473).
- Unknown 8: all estimates are marked "below detection limit", so the software gives no estimate. Yet readings decline consistently from dilution 1 to 1/3 to 1/9 (about 19.2–19.5, then 16, then 15), so a clear signal is present in the first six measurements. Only the final dilutions apparently look lost in noise (the readings at 1/27 are no lower than at 1/9) (p. 473).
- Unknown 9: four of eight measurements are above detection limit. The four more diluted ones are below it, yet they too decline consistently with dilution (p. 473).
- These unknowns are fairly typical of the plate. In allergen measurement even low concentrations can be important, so the authors need to distinguish zero from merely low. The Bayesian analysis does this far more precisely (pp. 473–474).

**The model.** Notation: unknown concentrations $\theta_1,\dots,\theta_{10}$; the standard's known concentration $\theta_0$; $x_i$ = concentration in well $i$; $y_i$ = colour intensity; $i=1,\dots,96$ (p. 474). The model is built in stages.

*Calibration curve.* The usual four-parameter model (p. 474):
$$\mathrm{E}(y|x,\beta)=g(x,\beta)=\beta_1+\frac{\beta_2}{1+(x/\beta_3)^{-\beta_4}}\tag{19.1}$$
- $\beta_1$: intensity at zero concentration; $\beta_2$: increase to saturation; $\beta_3$: concentration at which the gradient turns; $\beta_4$: rate of saturation. All are restricted to be nonnegative.
- The model is equivalent to a scaled and shifted logistic function of $\log x$. It fits the data fairly well (p. 474).

*Measurement error.* Normal with unequal variances:
$$y_i\sim \mathrm N\!\left(g(x_i,\beta),\ \left(\frac{g(x_i,\beta)}{A}\right)^{2\alpha}\sigma_y^2\right)\tag{19.2}$$
- $\alpha\in(0,1)$ captures that variance is higher for larger measurements. $A=30$ is arbitrary (middle of the data range); it gives $\sigma_y$ the meaning of the error SD for a "typical" measurement (p. 474).
- With $\alpha=0$ this is an equal-variance normal model. With $\alpha=1$ it approximately corresponds to the equal-variance model on the log scale (p. 474).
- Getting the variance relation right matters because many data are at low concentrations; we want to use them without overstating their precision (p. 474).

*Dilution errors.* Errors arise in the initial dilution and in serial dilutions. Serial dilution errors were low for these data, so only the initial dilution error is modelled (p. 474). For the standard, with $d_0^{\rm init}$ the known called-for initial dilution and $x_0^{\rm init}$ the actual unknown concentration:
$$\log(x_0^{\rm init})\sim \mathrm N\big(\log(d_0^{\rm init}\cdot\theta_0),(\sigma^{\rm init})^2\big)\tag{19.3}$$
- For unknowns there is no initial dilution, so $x_j^{\rm init}=\theta_j$, $j=1,\dots,10$ (p. 475).
- Further dilutions: with $j(i)$ the sample (0–10) of observation $i$ and $d_i$ its dilution relative to the initial one (the numbers in Fig. 19.1),
$$x_i=d_i\cdot x^{\rm init}_{j(i)}\tag{19.4}$$
This ignores serial dilution errors, assumed low enough (p. 475).

*Priors.* Noninformative: $\log\beta_k\sim U(-\infty,\infty)$ for $k=1,\dots,4$; $\sigma_y\sim U(0,\infty)$; $\alpha\sim U(0,1)$. Plenty of standards data lets these be estimated fairly accurately. For unknowns, $p(\log\theta_j)\propto1$ (p. 475).
- A hierarchical model $\log\theta_j\sim \mathrm N(\mu_\theta,\sigma_\theta^2)$ is an option (better still, a mixture allowing some true $\theta_j=0$). For simplicity the analysis uses no pooling ($\sigma_\theta=\infty$) (p. 475).
- $\sigma^{\rm init}$ cannot be estimated from one plate. It is fixed at 0.02 (2% SD), from a previous analysis of plates with several initial dilutions (p. 475).

**Inference.**
- Fitted in Bugs (a predecessor of Stan). Two parallel Gibbs chains of 50,000 iterations, every 20th draw saved; $\widehat R<1.1$ for all parameters (p. 475).
- Computation tips: use reasonable starting points (crude estimates); parameterize with logs. To speed convergence, work with $\log\beta,\alpha,\sigma_y,\log\gamma$, where $\log\gamma_j=\log(\theta_j/\beta_3)$. This avoids strong posterior correlation between the unknown concentrations and $\beta_3$, which sets the $x$-position of the curve (p. 475).
- Posterior medians [50% intervals]: $\hat\beta_1=14.7\,[14.5,14.9]$, $\hat\beta_2=99.7\,[96.8,102.9]$, $\hat\beta_3=0.054\,[0.051,0.058]$, $\hat\beta_4=1.34\,[1.30,1.38]$. Also $\hat\sigma_y=2.2\,[2.1,2.3]$ and $\hat\alpha=0.97\,[0.94,0.99]$ (p. 475).
- Estimates exist for all ten unknowns, even Unknown 8 (Fig. 19.4). Residuals (Fig. 19.5) show no major problems (pp. 475–476).

*Intuition note.* The curve is calibrated on the standards. Each unknown is just a horizontal rescaling of that curve, so all its wells share one parameter $\theta_j$. Low readings that decline with dilution therefore add information about $\theta_j$ instead of being discarded.

**Comparison with the standard method** (p. 476).
- Standard practice: invert the fitted calibration curve for each measurement, divide each estimate by its dilution, and average. For Unknown 9: $\tfrac14(0.040+0.031+3\cdot0.005+3\cdot0.005)=0.025$ (p. 476).
- The Bayesian estimates are generally similar but with higher accuracy, and exist for all unknowns. Using only the top four or only the bottom four wells per unknown, the two estimates are similar under both methods, but their agreement is much stronger for the Bayesian one (p. 476).
- The authors do not want to claim too much from one plate. A more thorough comparison under a range of conditions was done but is not shown (p. 476).

### 19.2 Example: population toxicokinetics (pp. 477–485)

A much more complicated model: hierarchical and multivariate, a parameter vector per subject, informative hierarchical priors with separate variance components for uncertainty about the population average and variation around it (p. 477).

**Background.** Perchloroethylene (PERC) causes cancer in animals and is believed to do so in humans. The general understanding is that it is metabolized in the liver and that its metabolites are carcinogenic. So the relevant dose is the amount metabolized (p. 477).
- Goal: the fraction metabolized as a function of air concentration, and its variation across the population (Fig. 19.6; young adult white males, the group with data) (p. 477).
- Direct measurement of metabolites or extrapolation from animals cannot give such curves with reasonable confidence. Instead a mathematical model of flow through the body and metabolism in the liver is used (p. 477).
- Data (Fig. 19.7): six volunteers exposed at a high level for four hours (believed long enough for most organs to reach equilibrium). PERC in exhaled air and blood was then measured for a week (168 h). Each person repeated this at a second exposure level (p. 477).

**Toxicokinetic model** (p. 478).
- Standard physiological model: the toxin enters and leaves by breath, is carried by blood to four compartments (well-perfused tissues, poorly perfused tissues, fat, liver), and is metabolized in the liver. A simpler one- or two-compartment model might be easier to estimate, but such models fit these data poorly and, more importantly, lack the complexity to fit varying exposure conditions accurately (p. 478).
- Each compartment obeys a first-order differential equation with volume, blood flow and partition coefficient parameters; the liver equation has a couple of extra parameters. Together: $L=15$ parameters per person, $\theta_k=(\theta_{k1},\dots,\theta_{kL})$ (p. 478).
- Given parameters and exposure, specialized numerical algorithms solve the equations, giving compartment concentrations and metabolism rate over time (p. 478).

**Estimation difficulty and prior information** (pp. 478–479).
- Such models predict concentration patterns close to mixtures of declining exponentials. Estimating the decay times of such a mixture is ill-conditioned: the parameters are hard to estimate simultaneously (see Exercise 19.3) (p. 478).
- A *physiological* model has parameters with direct physical meaning (e.g., blood flow through fat, tissue/blood partition coefficients). Many of them can be identified through prior, e.g. published, physiological data. Being essentially impossible to estimate from the data alone, they must have physical meaning and informative priors (pp. 478–479).

**Measurement model** (p. 479).
- Data $y_{jkmt}$: $j=1,2$ exposure level, $k$ individual, $m=1$ blood or $m=2$ air, $t$ time. Expected values are $g_m(\theta_k,E_j,t)$, the numerical solution of the differential equations given the individual's parameters $\theta_k$, exposure $E_j$ and time (p. 479).
- Observed concentrations have independent lognormal errors: mean zero, SD $\sigma_m$ on the log scale, $m=1,2$. These also implicitly account for model error. The two $\sigma_m$ may differ (different protocols). Independent uniform priors on $\log\sigma_1,\log\sigma_2$; no evidence of high residual correlations was found (p. 479).

**Population model** (pp. 479–480).
- Biological parameters are generally skewed (lognormal-like) and mostly have physiological bounds. So after log-transform and scaling, individual parameters are normal with population mean, truncated at ±3 SD. Truncation also acts as a check: if simulations stick near truncation points, data and the pharmacokinetic model strongly contradict the prior, and part of the model should be re-examined (p. 479).
- Constraints: $\theta_{k2},\dots,\theta_{k5}$ are blood-flow fractions and sum to 1. $\theta_{k6},\theta_{k7},\theta_{k8}$ are organ-volume scaling coefficients and sum to 0.873 (standard fraction of lean body mass not including bones). $\theta_{k8}$ (liver) is much smaller than the others and well known a priori (p. 480). New parameters $\psi_{kl}$:
$$\theta_{kl}=\frac{e^{\psi_{kl}}}{e^{\psi_{k2}}+e^{\psi_{k3}}+e^{\psi_{k4}}+e^{\psi_{k5}}},\ l=2,3,4,5$$
$$\theta_{kl}=(0.873-e^{\psi_{k8}})\frac{e^{\psi_{kl}}}{e^{\psi_{k6}}+e^{\psi_{k7}}},\ l=6,7$$
$$\theta_{kl}=e^{\psi_{kl}},\ l=1\text{ and }8\text{–}15.\tag{19.5}$$
- $\psi_{k2..k5}$ and $\psi_{k6},\psi_{k7}$ are not identified (adding a constant to $\psi_{k2},\dots,\psi_{k5}$ leaves $\theta_{k2..k5}$ unchanged). They get proper priors, so their posteriors can still be manipulated (p. 480).
- Each $\psi_{kl}$ is normal with mean $\mu_l$ and SD $\tau_l$, truncated at three SDs. Modelling on the $\psi$ scale respects the constraints and keeps truncated lognormals for the unconstrained components. Computation uses $\psi$; results are transformed back to $\theta$ (p. 480).
- The 15 population distributions are assumed independent. Afterwards, the $15\cdot14/2$ correlations across the six people showed no evidence of differing from zero. Had they been large, the authors would add correlations (Section 15.4) or reparameterize. Using proportional rather than absolute flows and volumes already reduced correlations (p. 480).

*Intuition note.* The transform (19.5) maps unconstrained numbers $\psi$ to shares that automatically sum to the required total. Modelling on the $\psi$ scale therefore respects the constraints (p. 480).

**Prior information** (pp. 480–481).
- For each transformed parameter: $\mu_l\sim \mathrm N(M_l,S_l^2)$ and $\tau_l^2\sim \text{Inv-}\chi^2(\nu_l,\tau_{0l}^2)$, with $\nu_l$ typically 2 (low, to show large uncertainty). Hyperparameters come from the biological literature (human studies, allometric scaling from animals). The priors are independent because prior information is essentially independent given the parameterization. Where the literature is ambiguous, prior variances are set higher rather than lower (weakly informative) (p. 480).
- Two sources of variation are distinguished, in the form $\log\theta_{jk}\sim \mathrm N(\mu_k,\tau_k^2)$ (indices as printed). $S_k$ describes uncertainty about the typical population value; $\tau_k$ describes variation among people (p. 481).
- Liver weight as a fraction of lean body weight: population geometric mean 0.033, with uncertainty and heterogeneity both of the order of 10–20%. Priors: $M_k=\log(0.033)$, $S_k=\log(1.1)$, $\tau_{k0}=\log(1.1)$ (p. 481).
- Michaelis–Menten coefficient: poorly understood. Population geometric mean estimated at 0.7, with possible uncertainty up to a factor of 100 either way. Individuals were believed to vary by no more than a factor of 4 around the population mean. Priors: $M_k=\log(0.7)$, $S_k=\log(10)$, $\tau_{k0}=\log(2)$ (p. 481).

**Joint posterior** (p. 481). The posterior (up to a constant) is the product of the data distribution, the population model and the prior:
$$
\begin{aligned}
&p(\psi,\mu,\tau^2,\sigma^2\mid y,E,t,\phi,M,S,\tau_0^2,\nu)\\
&\propto p(y|\psi,\phi,E,t,\sigma^2)\,p(\psi|\mu,\tau^2)\,p(\mu,\tau^2|M,S,\tau_0^2)\,p(\sigma^2)\\
&\propto\Big(\prod_{j=1}^{J}\prod_{k=1}^{K}\prod_{m=1}^{2}\prod_t \mathrm N(\log y_{jkmt}\mid\log g_m(\theta_k,E_j,t),\sigma_m^2)\Big)\sigma_1^{-2}\sigma_2^{-2}\\
&\quad\times\Big(\prod_{k=1}^{K}\prod_{l=1}^{L}\mathrm N_{\rm trunc}(\psi_{kl}|\mu_l,\tau_l^2)\Big)\Big(\prod_{l=1}^{L}\mathrm N(\mu_l|M_l,S_l^2)\,\text{Inv-}\chi^2(\tau_l^2|\nu_l,\tau_{0l}^2)\Big).
\end{aligned}\tag{19.6}
$$
- $\mathrm N_{\rm trunc}$ is the normal truncated at the specified number of SDs. The indexes $j,k,l,m,t$ are replication, person, parameter, measurement type, time. Evaluating (19.6) requires numerical computation of $g_m$ over the measurement times (p. 481).
- (added step) Shapes, from $L=15$, $K=6$ and two measurement types (pp. 478–479): $\psi_k\in\mathbb R^{15}$ for each of $K=6$ people; $\mu,\tau\in\mathbb R^{15}$; $\sigma\in\mathbb R^2$.

**Computation** (p. 482).
- Gibbs sampler, updating in order $\sigma,\tau,\mu,\psi_1,\dots,\psi_K$ (each a vector). Conditionals for $\sigma^2,\tau^2,\mu$ are inverse-$\chi^2$, inverse-$\chi^2$ and normal. The $\psi$ conditionals have no closed form, so Metropolis steps are used. These need the density only up to a constant, as in (19.6) (p. 482).
- Metropolis updates one person at a time ($K$ jumps per iteration, each a 15-vector), with a normal proposal centred at the current value. Its covariance is proportional to one from initial runs, scaled to an acceptance rate of about 0.23 (p. 482).
- Why one person at a time: only that person's factors of the density must be recomputed. Evaluating $g_m$ is the costliest part. The alternative, one component $\psi_{kl}$ at a time, needs $KL$ jumps per iteration (p. 482).
- Five independent runs of 50,000 iterations, saving every tenth draw. Starting points: each $\psi_{kl}$ drawn from its prior, $\mu_l=M_l$; the first draws are $\sigma$ and $\tau$. Convergence was monitored by within/between-simulation variances (Section 11.4). The model was implemented over months, and agreement with earlier variants adds trust (p. 482).

**Inference for quantities of interest** (pp. 482–483).
- First the parameters and their population variability were checked for sense and consistency with the prior. The main quantity is the fraction of PERC metabolized under chosen exposure scenarios, computed by solving the ODE model at each simulated $\psi_k$. Within-person variance reflects posterior uncertainty (p. 482).
- Fig. 19.8: fraction metabolized at 50 ppm (occupational) and 0.001 ppm (environmental) for each of the six people. These exposures were hypothetical inputs to the fitted model. The figure shows correlation between high-dose and low-dose estimates. Between-person variation is large, e.g. a factor of two between subjects A and E (p. 482).
- For a new person exchangeable with the subjects, parameters are simulated from the population distribution. The resulting variance includes posterior uncertainty and real inter-individual variation. 95% intervals for the population: at 50 ppm $[0.5\%,4.1\%]$; at 0.001 ppm $[15\%,58\%]$ (pp. 482–483).
- Fraction metabolized in one day (after three weeks of inhalation) versus exposure (Fig. 19.6): constant at low exposures (metabolism is linear). Saturation starts above 1 ppm and is about complete at 10 ppm. At higher levels the fraction decreases linearly with exposure, since the metabolized quantity per unit time is at its maximum (p. 483).
- Caveats: one experiment, six people from a homogeneous population, two exposure conditions. Much uncertainty comes from these limits. More data on the same people would reduce posterior uncertainty; more people are needed to learn about the population. Population variability, here about as large as posterior uncertainty, might increase with a more heterogeneous group (p. 483).

**Evaluating the fit** (pp. 483–485).
- Fig. 19.9: observed/expected for all data, using one randomly chosen posterior draw (so the misfit is shown without adjusting for fitting). Observations span a factor of 10,000, but relative errors are mostly between 0.8 and 1.25. The errors are reasonably low compared with other fits of this kind of data (pp. 483–484).
- External validation (Fig. 19.10): a second experiment with six volunteers at constant PERC levels of 0.5–9 ppm, measured up to 50 minutes. Predictions for new individuals use draws from $p(\theta|\mu,\tau)$. The blood/exhaled-air concentration ratio was predicted. The fit is good overall, even though exposures were 5 to 100 times lower than in the main data. The text mentions 95% and 99% simulation bounds; the caption names 95% predictive intervals (p. 485).
- Short-term kinetics (<15 minutes) are not well described. The caption (p. 484) attributes this to the model assuming instantaneous equilibrium in all compartments, whereas this takes about 15 minutes to approximately hold. The text (p. 485) says instead that the model includes only a simple description of pulmonary exchanges.

**Complex model with an informative prior** (p. 485). Five features work in combination: (1) physiological model, (2) population model, (3) prior information on population parameters, (4) data, (5) Bayesian inference. If any is missing, the model will not work, according to the authors:
- without (1) there is no good way to get prior information;
- without (2) there is generally not enough data to estimate each individual separately;
- (3 and 4) the parameters of a multi-compartment physiological model cannot be determined accurately by data alone or by prior information alone, so both are needed;
- (5) gives parameters consistent with both prior and data, if such agreement is possible.
The hierarchical Bayesian posterior includes inferential uncertainty and population variability, so it can feed a risk-assessment uncertainty analysis directly (p. 485).

### 19.3 Bibliographic note (p. 485)
The note cites nonlinear-model texts (Carroll et al. 1995; Giltinan and Davidian 1995). It says the assay analysis appears in Gelman, Chew and Shnaidman (2004) and the toxicology example in Gelman, Bois and Jiang (1996). It also points to Bayesian treatments of neural networks, regression trees, splines and nonparametric models as the large-parameter-count continuation of nonlinear models (p. 485).

### 19.4 Exercises (p. 486)
Three exercises on assay data, golf putting data (Table 19.1) and ill-posed exponential mixtures; listed below (p. 486).

## Toy example (ours, not from the text)
Calibration curve with simple numbers: $\beta_1=10,\ \beta_2=100,\ \beta_3=1,\ \beta_4=1$. Then $(x/\beta_3)^{-\beta_4}=1/x$, so
$$g(x)=10+\frac{100}{1+1/x}=10+\frac{100x}{x+1}.$$
Take $\sigma_y=2$, $\alpha=1$, $A=30$, so $\mathrm{sd}(y)=\sigma_y\,g/A$.
- Unknown with true $\theta=0.5$, measured at dilution $1/9$: $x=0.5/9=0.0556$.
- Expected reading: $g=10+100\cdot(1/18)/(19/18)=10+100/19=15.263$.
- Variance model: $\mathrm{sd}=2\cdot15.263/30=1.018$.
- Suppose the observed $y=15.3$. This is a "low" reading, only 5.3 above the zero-concentration level of 10.
- If $\theta=0$: $x=0$, $g=10$, $\mathrm{sd}=2\cdot10/30=0.667$. The standardized residual is $(15.3-10)/0.667=7.95$, wildly implausible.
- If $\theta=0.5$: $z=(15.3-15.263)/1.018=0.036$, a very good fit.
- So a low reading still separates "zero" from "low", which is the point of Section 19.1. Standard-method inversion: $r=(15.3-10)/100=0.053$, $x=r/(1-r)=0.0560$, and dividing by the dilution $1/9$ gives $0.504$.
- Note the change of $\mathrm{sd}$ with the mean: it is why low readings can be precise ($0.667$ at $g=10$) without being overweighted.
- In the full model one would also have uncertainty in $\beta$ and several wells per unknown; this toy fixes $\beta$.

## Concepts
- [[parametric-nonlinear-model]] (new) — a model whose mean function combines parameters and predictors nonlinearly, beyond a (transformed) linear predictor (p. 471)
- [[serial-dilution-assay]] (new) — measurements at several dilutions of a sample, calibrated by standards of known concentration (p. 471)
- [[four-parameter-calibration-curve]] (new) — $\beta_1+\beta_2/(1+(x/\beta_3)^{-\beta_4})$, a scaled and shifted logistic in $\log x$ (p. 474)
- [[heteroscedastic-measurement-model]] (new) — normal errors with variance $\propto (g/A)^{2\alpha}$, interpolating between constant variance and constant log-scale variance (p. 474)
- [[hierarchical-model]] — here: individual physiological parameters drawn from a population distribution with learned mean and SD (p. 479); the assay uses no pooling instead (p. 475)
- [[prior-distribution]] — here informative and weakly informative priors from literature, separating uncertainty from population variation (p. 480)
- [[ill-conditioned-exponential-mixture]] (new) — estimating decay times of a sum of exponentials is hard; the parameters are hard to estimate simultaneously (p. 478)
- [[compartment-ode-model]] (new) — body model with compartments obeying first-order differential equations, solved numerically for $g_m$ (p. 478)
- [[constrained-parameter-reparameterization]] (new) — transform (19.5) maps free $\psi$ to shares with fixed sums; some $\psi$ are non-identified but have proper priors (p. 480)
- [[gibbs-sampling]] — here with Metropolis steps for the non-closed-form $\psi_k$ conditionals (p. 482)
- [[metropolis-hastings]] — normal proposal, acceptance rate about 0.23, one person at a time (p. 482)
- [[convergence-diagnostics]] — $\widehat R<1.1$ in the assay; within/between variance comparison for PERC (pp. 475, 482)
- [[posterior-predictive-check]] (in spirit) — comparing observed data with model-based expected data from posterior draws, plus external validation (pp. 483–485)
- [[exchangeability]] — a new person "exchangeable with the subjects" is simulated from the population distribution (p. 482)

## Canonical instances
- [[serial-dilution-assay-cockroach-allergen]] — allows estimates for samples that standard software marks "below detection limit" (pp. 472–476)
- [[perc-toxicokinetics]] — population-level fraction of PERC metabolized, with 95% intervals at 50 ppm and 0.001 ppm (pp. 477–485)
- [[golf-putting-data]] — Table 19.1, a nonlinear model for success probability versus distance (exercise only) (p. 486)

## Bridges (candidates)
- [same-math] Transform (19.5), $e^{\psi_l}/\sum e^{\psi}$ ↔ machine learning: softmax — the same function turns free reals into shares summing to 1.
- [structural-analogy] Assay unknown $\theta_j$ rescales the $x$-axis of a common curve ↔ calibration/measurement models in the social sciences: one shared response function, a unit-specific latent position.
- [structural-analogy] Separating prior uncertainty about the mean ($S$) from population variation ($\tau_0$) ↔ hierarchical-model hyperpriors: uncertainty about the population average versus spread among groups.

## Questions this raises
- How should a hierarchical or mixture prior on the unknown concentrations (including exact zeros) change the estimates for low samples, compared with the no-pooling analysis used here?
- When the same reading is inverted through the curve, how does posterior uncertainty about $\beta$ propagate to the unknowns? Which parts of the posterior are due to $\beta_3$–$\theta_j$ correlation?
- How much do the results depend on the ±3 SD truncation and on $\nu=2$ in the prior on $\tau_l^2$? Could a prior predictive check say?
- Could the misfit in the first 15 minutes be repaired by a model with non-instantaneous equilibrium, and would that make the model harder to estimate?

## Exercises worth doing
- Ex. 1(a)–(c) (p. 486) — fit the assay model in Stan, then with a hierarchical mixture prior allowing zero concentrations; compare inferences — difficulty: medium
- Ex. 1(d) (p. 486) — construct data where the two priors give very different inferences — difficulty: hard
- Ex. 2(a)–(b) (p. 486) — nonlinear binomial model for putting success versus distance (Table 19.1), checked in and beyond the data range, with posterior predictive checks — difficulty: medium
- Ex. 3 (p. 486) — simulate a sum of two exponentials and see how large $n$ must be before Bayesian inference recovers the true parameters (ill-posedness) — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 481 = printed 471). All citations use printed numbers.
- The text layer renders $\theta$ as "ω", "−" as "→", and "~" as "→".
- Index use is inconsistent in the source: $k$ indexes person in most places, but "$\theta_{jk}$ is the value of the $k$th parameter for person $j$" (p. 480) and $\log\theta_{jk}\sim \mathrm N(\mu_k,\tau_k^2)$ with $\mu_k,M_k,S_k$ (p. 481) use $k$ as the parameter index, while (19.6) uses $l$.
- The Michaelis–Menten prior is described as uncertain "up to a factor of 100 above or below", and $S_k=\log(10)$ is given (p. 481); the page does not say how the two statements relate. I report both as printed.
- p. 485 text says Fig. 19.10 shows 95% and 99% simulation bounds. The caption (p. 484) says 95% predictive intervals; the image shows two sets of bounds (solid and dashed).
- Figures 19.4–19.10 are described from their captions and images; no numeric values were read off the plots. Table 19.1 data are given as exercise material only.

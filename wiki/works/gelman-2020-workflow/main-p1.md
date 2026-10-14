---
id: gelman-2020-workflow/main-p1
work: gelman-2020-workflow
unit: "paper (part 1/3): Sections 1–5.6"
pages: 1–25
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Bayesian Workflow (part 1/3): introduction, before fitting, fitting, constructed data, computational problems

## L0 — One line
Applied Bayesian analysis is a tangled, iterative workflow of building, checking, fixing and comparing many models, in which simulation, simpler models and quick approximate fits help to find problems early.

## L1 — The gist (≤ 120 words)
The paper asks what applied Bayesian analysis involves beyond computing p(θ|y). Its answer is an iterative workflow of building, fitting, checking, modifying and comparing many models, many of which will be flawed or discarded. This part covers the motivation and the Figure 1 overview (Sec. 1). It then covers choices before fitting: priors, scaling, prior predictive checks, generative models (Sec. 2). Next come fitting with Hamiltonian Monte Carlo (HMC) and approximations (Sec. 3) and fake-data simulation and simulation-based calibration (Sec. 4). It ends with strategies for computational trouble (Sec. 5.1–5.6). It matters because computational trouble often signals a modelling problem, and shortcuts can be understood as approximations to a fuller workflow.

**Prerequisites:** prior, likelihood, posterior; basic MCMC ideas (chains, mixing, R̂); logistic and linear regression; hierarchical models.

## L2 — Key ideas
- Bayesian inference is just the formulation and computation of p(θ|y) ∝ p(θ)p(y|θ). Workflow adds model building, checking, improvement and multi-model comparison, the last not only for choice or averaging but more importantly to understand the models (p. 3).
- Workflow is more general than an example and less precisely specified than a method. In the authors' view, statistical ideas often move from example to case study to workflow to method to theory, though not all reach the last stages (pp. 4–6).
- Prior predictive checks (simulating data from the prior) help show what a prior implies for data, e.g. independent normal(0,1) coefficient priors imply extreme mean outcomes as predictors increase (p. 10).
- Bayesian inference needs only the likelihood. Bayesian data analysis needs a generative model (a joint distribution of data and parameters) for predictive simulation and checking. Models range from non-generative to fully generative (pp. 11–12).
- Computation is part of the modelling process. Early on, approximate algorithms (instead of Markov chain Monte Carlo, MCMC), short runs and failing fast on bad models can make sense; late in the workflow accurate exploration, usually by MCMC, is required (pp. 13–15).
- Fake-data simulation checks recovery of known parameters. Simulation-based calibration (SBC) is its more complete form, because Bayesian inference in general is calibrated only when averaging over the prior, not for a single parameter value (pp. 16–18).
- Simulating different scenarios shows how methods behave. In the exam-treatment example, adjustment works under linearity but is sensitive to functional form when assignment is unbalanced (pp. 20–22).
- The "folk theorem": computational problems often indicate a model problem. Debug by simplifying, building up, using small subsets and short runs, and plotting intermediate quantities (pp. 22–24).
- For multimodal or slowly mixing posteriors the options include initial values, priors, restricting the model, stacking (combining chains or models with cross-validation weights) and mixture-prior splitting, depending on the kind of multimodality (pp. 24–25).

## L3 — Walkthrough

### Abstract (p. 1)
Bayesian methods handle uncertainty in observations, parameters and model structure using probability. Probabilistic programming languages make models easier to specify and fit, but many decisions and computational challenges remain. The authors review the whole "tangled workflow": iterative model building, checking, troubleshooting, understanding and comparison. In practice many models are fit, even if only a subset matters for conclusions (p. 1).

### 1. Introduction

**1.1 From Bayesian inference to Bayesian workflow (pp. 3–4).**
- *Bayesian inference* is, in the authors' wording, only the formulation and computation of conditional probabilities or densities:
$$p(\theta\mid y)\propto p(\theta)\,p(y\mid\theta).$$
- *Bayesian workflow* includes three steps: model building, inference, and model checking/improvement. It also includes comparing models, not only for choice or averaging but, more importantly, to understand them. Examples: why some models predict some aspects of the data poorly, or why uncertainty estimates vary across models (p. 3).
- Even a favoured model should be compared with simpler and more complicated ones to see what it does (p. 3).
- An extended workflow would also include pre-data design and post-inference decisions. This paper focuses on modelling the data (p. 4).
- In a typical workflow many models are fit. Some are in retrospect poor choices (poor fit, no link to theory or goals, priors too weak/strong, programming errors). Some are useful but flawed (e.g. a regression adjusting for some confounders but not others). Some are worth reporting. The wrong and flawed models are unavoidable steps toward the useful ones (p. 4).

**1.2 Why a workflow? (p. 4).** Four reasons:
- Computation can be hard, so we need simpler or alternative models, faster approximations and exploration of the fitting process.
- We usually do not know the model in advance, and we expand it as data or questions grow.
- Understanding a fitted model is often best achieved by comparing related models.
- Different models can give different conclusions with none clearly better, so presenting several illustrates model uncertainty.

**1.3 Workflow, theory and practice (pp. 4–6).**
- For this paper, workflow is broader than a single example but less precisely specified than a method (p. 4). The authors cite computing-workflow ideas such as the tidyverse and the plug-and-play feel of machine learning (p. 4).
- Figure 2 (meta-workflow): example · case study · workflow · method · theory. New ideas appear in examples, are stylised into case studies, set up as workflows, then (when possible) formalised, coded and studied theoretically. Not all methods reach the last stages (pp. 4–6).
- Examples of ideas moving along this path (p. 6):
  - multilevel modelling formalises empirical Bayes estimation of priors;
  - exploratory data analysis can be understood as predictive model checking;
  - lasso and horseshoe replaced ad hoc variable selection;
  - Gaussian processes can be seen as Bayesian replacements for kernel smoothing.
- Much of the workflow is set up in Stan, but similar ideas apply elsewhere (p. 6).

**Figure 1 (p. 5).** Flow chart of the steps. Section numbers in brackets point to where each step is discussed.
- Pick an initial model (2.1) → prior predictive check → either the prior contradicts domain knowledge (go to *Modify the model*) or the prior is provisionally accepted → fit the model (3).
- Validate computation (4): convergence diagnostics, fake-data simulation, SBC. Outcomes: computation not valid → addressing computational issues (5), or computation provisionally accepted → evaluate and use model (6).
- Evaluate and use model (6): posterior predictive check, cross validation, influence of individual data points, influence of prior, prediction, poststratification. Outcomes: model not trustworthy → modify; model provisionally accepted → compare models (8).
- Addressing computational issues (5): simplify the model, implement components separately, run few iterations, run on a subset, stacking chains, check multimodality, reparametrize, plot intermediate quantities, add prior information, add data, or "give up" (→ modify).
- Modify the model (7): new starting model, replace a component, enrich/expand, use an approximation, add data, modify priors.
- Compare models (8): comparing inferences, multiverse analysis, model averaging/stacking.
- Any one analysis will most likely not use all steps (p. 5).

**1.4 Organizing the aspects (p. 7).**
- Textbook workflows are often linear (e.g. clinical trial: sample size → data → analysis → p-values). This workflow is more tangled, with sub-workflows for four reasons:
  1. fitting a complex model can itself need experimentation, plus checks that the algorithm did what was intended;
  2. we start with a model known to miss features (correlations, hierarchy, time variation) and add features gradually;
  3. data are often not fixed, and new data often require model extensions;
  4. models are best understood by comparison with alternatives.
- The authors list uncertainty about fitting correctly, about setting up and expanding models, and about interpretation. Any organisation of steps oversimplifies (p. 7).
- Time, compute and the penalty for being wrong may force shortcuts. "Approximate" is defined as not giving exact posterior summaries even with infinite compute time. Not fitting a model at all could be worse than an approximate fit. The aim is to understand shortcuts as approximations to the full workflow, so practitioners can choose where to invest effort (p. 7).

*Intuition note.* The paper treats a final reported model as the visible tip of a pile of earlier models, some of them wrong or flawed. Because shortcuts will be taken, it aims to help practitioners see shortcuts as approximations to the full workflow and choose where to invest effort.

**1.5 Aim and structure (p. 8).** The article aims to make tacit knowledge explicit. The audience is practitioners (especially Stan users), method/software developers, and Bayesian theorists. Sections 2–6 cover before fitting, fitting, debugging and evaluating. Section 7 covers modifying models and Section 8 comparing models. Sections 10 and 11 are two worked examples (golf putting; planetary motion), and Section 12 is discussion (p. 8).

### 2. Before fitting a model

**2.1 Choosing an initial model (pp. 8–9).**
- Almost all analyses start by adapting a model from a textbook, case study or paper. This is like a software design pattern. Templates can save time in model building and computing, and the cognitive load of the person who must understand the results should also be taken into account. They tell us in which direction elaborations or simplifications are likely to be useful (p. 8).
- The authors say templates are useful starting and comparison points despite the negative connotation of "cookbook analysis". They also note that development of scientific theories is not the same as development of statistical models (Navarro, 2020) (p. 8).
- One may start simple and add features, start big and strip down, or begin from several different approaches (pp. 8–9).

**2.2 Modular construction (p. 9).** A Bayesian model is built from modules that act as placeholders. Examples:
- normal → longer-tailed or mixture;
- linear → splines or Gaussian processes;
- exact observations → add measurement error;
- weak prior → stronger prior if the posterior contains unrealistic values.

This takes pressure off model building, since one can generalise later. It goes against the tradition of naming whole models; naming modules makes connections between models easier to see (p. 9).

**2.3 Scaling and transforming parameters (pp. 9–10).**
- The authors like parameters to be interpretable (for practical and ethical reasons). This leads to natural scales and, if possible, independence or interpretable dependence, which eases use of informative priors (p. 9).
- Example: a pharmacology parameter expected near 50. Model $\log(\theta/50)$, so 0 means 50 on the original scale and a difference of 0.1 means about 10% change (p. 9).
- Scale-free parameters also suit hierarchical modelling and partial pooling. Toxicology example: model each person's liver volume as person volume × liver proportion. The proportions are expected to vary less across people, so the model can pool more than when modelling absolute volumes (p. 9).
- Put parameters roughly on unit scale by log or logit transforms or standardising. If centre and scale come from the data, as for rstanarm default regression priors, this can be seen as an approximation to a hierarchical model with centre and scale as hyperparameters estimated from the data (pp. 9–10).
- More complicated transformations can also aid interpretation and prior use (p. 10).

**2.4 Prior predictive checking (pp. 10–11).**
- Prior predictive checks help understand a prior in the context of a generative model. They use simulations, not observed data, so they refine the model without using the data multiple times (p. 10).
- *Figure 3 setup (p. 10).* Logistic regression, 100 data points, 2, 4 or 15 binary covariates, independent normal(0,1) priors on coefficients. 1000 times: draw coefficients from the prior, simulate $y$, record the mean $\bar y$.
- *Figure 3 result.* With few covariates the distribution of $\bar y$ is spread out. With 15 covariates it piles up near 0 or 1 (visible in the image). So weak priors on individual coefficients imply a strong prior on $\bar y$. A more moderate prior on $\bar y$ would need coefficient priors strongly concentrated near zero (p. 10).
- General phenomenon: as the number of predictors grows, we need stronger coefficient priors (or enough data) to avoid extreme predictions (p. 10).
- One can set priors on outcomes and derive a joint prior on parameters. Joint priors allow control of the overall complexity of larger parameter sets, which helps give more sensible prior predictions that would be hard or impossible to get with independent priors (p. 10).
- *Figure 4 (p. 11).* Prior draws of a Gaussian process with squared exponential covariance for three settings of amplitude $\tau$ and length scale $l$: $(\tau,l)=(1/2,2)$, $(1/4,1/2)$, $(1/2,1/2)$. Drawn functions differ visibly in smoothness and spread. The authors call such checks essential for unfamiliar or complicated models (p. 11).
- Prior predictive simulation can also help elicit expert knowledge about measurable quantities, which is often easier than about unobservable parameters. Even when computational prior predictive checks are skipped, it might be useful to think about how the chosen priors would affect a hypothetical simulated dataset (p. 11).

*Intuition note.* A prior on a coefficient is also an indirect statement about data. Simulating data from the prior shows whether "weak" priors really are weak in terms of outcomes.

**2.5 Generative and partially generative models (pp. 11–12).**
- Fully Bayesian data analysis requires a generative model: a joint distribution of all data and parameters. Bayesian *inference* needs only the likelihood, and different generative models can share it. Predictive simulation and model checking (Sections 2.4, 4.1, 4.2, 6.1, 6.2) need the generative model (p. 11).
- Example: $y\sim\text{binomial}(n,\theta)$ with $n$, $y$ observed. Binomial sampling (fixed $n$) and negative binomial sampling (stop at a set number of successes) give likelihoods that differ by a factor depending on $y$ and $n$ but not $\theta$. For inference on $\theta$ they are equivalent. For simulating new data they differ: replications have fixed $n$ in one case and fixed $y$ in the other, so predictive checks look different (p. 11).
- The authors do not claim Bayes is necessarily better. Generative assumptions can raise efficiency but can go wrong, which motivates the workflow (p. 11).
- Common partially generative cases: regression modelling $y$ given $x$ without a model for $x$; survival data with unmodelled censoring. For predictive checks we then condition on observed predictors or extend the model so new $x$ can be sampled. Some parts (e.g. $x$ from a deterministic design) may have no stochastic generator (pp. 11–12).
- Generative thinking can help show the limits of what can be learned. A complicated autocorrelation structure may be indistinguishable from nearly independent errors if observations are spaced far apart in time (p. 12).
- Improper priors give models that are not fully generative: no joint distribution, no prior predictive sampling. The authors treat them as placeholders on the way to a proper joint model (p. 12).
- Example: the 2020 presidential election model uses state and national polls with partial pooling toward a "fundamentals" forecast, with a stochastic process for latent trends. It is run in Stan. Unlike poll aggregation, it could be run forward to generate polling data (p. 12).
- The ladder from least to most generative (p. 12):
  1. non-generative data summaries;
  2. classical models $p(y;\theta)$ with no distribution for $\theta$;
  3. usual Bayesian models $p(y,\theta\mid x)$, with unmodelled $x$ such as sample sizes, design settings, hyperparameters;
  4. fully generative $p(y,\theta,x)$ with no left-out data.
- Workflow can move up and down this ladder, e.g. by giving an unmodelled predictor $x$ a measurement-error model, which adds a level of latent data (p. 12).

*Intuition note.* The likelihood is enough to compute a posterior, but only a full data-generating story lets you simulate fake data and test the model against it.

### 3. Fitting a model (pp. 12–16)
- History: analytic calculation plus normal approximation, then Gibbs and Metropolis in the 1990s. Current state-of-the-art for open-ended models: variational inference, sequential Monte Carlo, Hamiltonian Monte Carlo (HMC) (pp. 12–13).
- Variational inference generalises EM and, in the Bayesian context, gives a fast but possibly inaccurate posterior approximation. Sequential Monte Carlo generalises Metropolis. HMC is another generalisation of Metropolis that uses gradients to move efficiently through continuous spaces (p. 13).
- The paper focuses on HMC and variants (Stan). Safe use of any algorithm requires strong diagnostics that flag unreliable computation (p. 13).

**3.1 Initial values, adaptation, warmup (p. 13).**
- Markov chain algorithms usually have stages. *Warmup* moves simulations from possibly unrepresentative starting values toward the region where the log posterior density is near its expected value (related to the "typical set"). Tuning parameters are set during warmup. The *sampling phase* ideally runs until chains have mixed (p. 13).
- Initial values do not matter asymptotically but can matter in practice, and a wrong choice can threaten validity (p. 13).
- For a correctly specified model warmup has two purposes: (a) reduce bias from initial values, (b) provide information for tuning. In model exploration it has a third role: quickly flag computationally problematic models (p. 13).

**3.2 How long to run (pp. 13–14).**
- Recommended standard practice: run at least until $\widehat R<1.01$ for all parameters and quantities of interest, and also monitor the multivariate statistic $R^*$ (p. 13).
- Early in modelling, earlier stopping can make sense. Running until effective sample size is in the thousands might seem safe, but if it takes long it limits how many models can be explored. Often a few iterations reveal big issues, especially coding errors. Running many iterations for a new model resembles premature optimisation. For the final model, the number of iterations depends on the desired Monte Carlo accuracy (pp. 13–14).
- Beyond the default of 4 or 8 chains, variance reduction can also come from more parallel chains instead of more iterations (p. 14).

**3.3 Approximate algorithms and approximate models (pp. 14–15).**
- MCMC is an approximation whose theoretical error goes to zero with more draws. If chains have mixed, Monte Carlo standard error can be estimated well, so results are often treated as exact. MCMC to convergence is not always scalable (p. 14).
- *Figure 5 (idealised, p. 14).* Distance from the target versus computation time. The approximate algorithm drops fast and plateaus; MCMC drops slower but ends lower. The better one depends on the time budget and where the curves cross. In a real problem the curves' positions are unknown, and an approximate algorithm can even do worse than MCMC at short times (p. 14).
- Late in the workflow, delicate features need accurate exploration, which usually means MCMC. Early on, decisions often depend on large-scale features that simpler methods estimate well: empirical Bayes, linearisation/Laplace, INLA, expectation propagation, mode-finding variational inference, penalised maximum likelihood (pp. 14–15).
- There is no one-size-fits-all approximation. For well-understood components (GLMs, multilevel regression, autoregressive models, Gaussian processes) an appropriate algorithm can often be built. Generic diagnostics (Yao et al. 2018a; Talts et al. 2020) can check that an approximation reproduces the posterior features you care about (p. 15).
- Alternative view: an approximate algorithm is an exact algorithm for an approximate model. Empirical Bayes replaces priors with a data-dependent point-mass prior. A Laplace approximation is a data-dependent linearisation. A nested Laplace approximation uses a linearised conditional posterior (p. 15).

**3.4 Fit fast, fail fast (pp. 15–16).**
- Goal: fail fast on bad models rather than spend time on near-perfect inference for a model that will be abandoned. The authors say there is a large literature on fitting desired models fast but little on wasting little time on models that will be abandoned, and that methods should be evaluated on this criterion. Poorly fitting models are often harder to fit (p. 15).
- *Ellipse example.* An astronomer fits an ellipse to a planetary orbit from 10 error-prone points. In Figure 6a almost any algorithm works (e.g. exact ellipses from sets of five points averaged, sequential perturbation, or least squares). In Figure 6b a hypothetical "Death Star" has perturbed the orbit. Convergence is then hard, and even a least-squares solution would be a terrible fit, because an ellipse is inappropriate. The fit should fail fast so one can move on (pp. 15–16).
- This shows in extreme form a common pattern of difficult statistical computations: fitting different subsets of the data yields very different parameter estimates (p. 16).

*Intuition note.* Cheap, rough computation can be acceptable early, since the aim is to find out which models are worth precise computation. A bad model should reveal itself quickly.

### 4. Using constructed data to find and understand problems (p. 16)
- First validate that the model finishes in acceptable time and diagnostics are reasonable. For HMC this means no divergent transitions, $\widehat R$ near 1, and sufficient effective sample sizes for central tendency, tail quantiles and energy. These diagnostics cannot protect against a program that is computed correctly but encodes a different model than intended (p. 16).
- With real data, modelling and computational issues can collide, so we first fit models to simulated data (p. 16).

**4.1 Fake-data simulation (pp. 16–18).**
- Choose a priori reasonable parameter values, simulate a fake dataset of the same size, shape and structure, fit the model, and check several things (p. 16).
- First (a design question, not strictly computational): do the data give information beyond the prior for each parameter? Look at point estimates and coverage of posterior intervals (pp. 16–17).
- If the check fails, or components gain no information from the data, break the model down and go simpler until it works, then locate the problem (Section 5.2) (p. 17).
- Second: can true parameters be recovered roughly within posterior uncertainty? This will not happen if the data are uninformative, but typically should otherwise. One simulation cannot show everything works (see 4.2), but it often reveals blatant errors, such as a coding error that fits the wrong model (p. 17).
- Third: see how behaviour changes across the parameter space. Examples (p. 17):
  - a sum of declining exponentials is informative when exponents are well separated and not when close (Section 5.9);
  - differential equation models have similar instability (Section 11);
  - hierarchical models look different at the neck and the mouth of the funnel;
  - Gaussian processes depend on length scale versus data resolution.
- Hence a two-step procedure: fit real data, then draw parameters from that posterior for fake-data checks. The statistical properties are unclear, but the authors found it helpful in practice (p. 17).
- One may also try to break the method with adversarial fake data (p. 17).
- Why it is crucial: it is arguably the only point where inference on latent variables can be directly checked, since with real data latent variables are not observed. In overparameterised models very different parameters can give similar predictions (p. 17).
- Success on fake data from the model itself guarantees nothing about real data. Failure on such fake data means it is "hopeless" to expect reasonable inference on real data. Fake-data simulations give an upper bound of what can be learned about a latent process (pp. 17–18).

**4.2 Simulation-based calibration (pp. 18–20).**
- *Figure 7 (p. 19).* Three scenarios compare a posterior sample to a true value. Scenario 1: posterior centred at the truth (fit reasonable). Scenario 2: truth in the tail (unclear whether inference is faulty). Scenario 3: multimodal posterior, so comparing with a single point cannot validate the algorithm (p. 19).
- A single simulation need not "work" even if the algorithm is right. There is a 5% chance of a draw outside a 95% interval. More fundamentally, Bayesian inference is in general calibrated only when averaging over the prior, not for a single parameter value. Recovery may also fail because data carry no information beyond the prior. If prior and posterior are approximately unimodal and the truth is at the centre of the prior, overcoverage of posterior intervals is expected (p. 18).
- *SBC (Cook et al. 2006; Talts et al. 2020)* procedure (p. 18):
  1. draw parameters from the prior;
  2. simulate data given them;
  3. fit the model;
  4. compare the posterior with the parameters that generated the data;
  5. repeat.
- The idea: inference across datasets simulated from prior draws should recover the prior. SBC helps assess how closely approximate algorithms match the theoretical posterior, even when the posterior is intractable (p. 18).
- Cost: many fits. The authors see SBC and truth-point benchmarking as two ends of a spectrum. A single truth point may flag gross problems, and more experiments reveal finer problems. SBC with few draws is an open research question. They expect a designed exploration of the prior may beat random draws for models with few parameters (p. 18).
- Problem: SBC clashes somewhat with most modellers' tendency to specify priors wider than they believe necessary. Simulated datasets can be extreme (for example, fake air pollution data with an absurdly high pollution density), and algorithms that work on realistic data may fail. The authors say this is less a problem with the computation than with the prior (pp. 18–20).
- Pragmatic fix: estimate reasonable parameter values from the real data (rough estimates or actual posterior), widen slightly, and use that as the prior for SBC, so simulated data are as realistic as the model allows (p. 20).

*Intuition note.* Calibration is a promise about the whole joint process (prior then data), not about one chosen true value. SBC tests that promise by playing the whole process many times.

**4.3 Experimentation using constructed data (pp. 20–22).**
- *Misspecification test.* Simulate $y_i\sim\text{normal}(a+bx_i,\sigma)$ with $a,b,\sigma$ drawn from the prior; fit; repeat 1000 times and check interval coverage (a version of SBC). Then simulate $y_i$ from $t_4$ but fit the normal model. This fails SBC, but the interesting question is how bad the inferences are, e.g. coverage of 50% and 95% intervals for the coefficients (p. 20).
- *Exam example (pp. 20–22).* 500 students; true abilities $\eta_i\sim\text{normal}(50,20)$; midterm $x_i$ and final $y_i$ independent $\text{normal}(\eta_i,10)$ draws. The text states the correlation as $\frac{20^2}{20^2+5^2}=0.94$, chosen high to make patterns visible (p. 20). A hypothetical treatment after the midterm adds 10 points to the final score; the true effect is 10 by construction.
  - *Balanced (random 50/50) assignment (Fig. 8b).* Difference of group means: 10.7, se 1.8. Regression adjusting for midterm: $9.7\pm0.6$ (p. 21).
  - *Unbalanced assignment.* The probability of treatment depends on the midterm score, with less well-performing students more likely treated. The text gives $\Pr(z=1)=\text{logit}^{-1}((x-50)/10)$ (but see Reading notes). Simple difference of means: $-13.8\pm1.5$, "a terrible inference" given true effect 10. Linear regression adjusting for $x$: $9.7\pm0.8$ (p. 21).
  - *Nonlinear truth (Fig. 10).* True effect still 10, but $E(y\mid x,z)$ is nonlinear (final score transformed). Fitting a linear regression: balanced design gives $10.5\pm0.8$ (errors from misspecification cancel on average because of the balance). Unbalanced design gives $7.3\pm0.9$ even after adjusting for $x$ (p. 21).
- Lesson: simulating a system under different conditions can give insight about data and inference generally, not only about computation. One could go on with varying treatment effects, selection on unobservables, and so on, indefinitely (p. 22).

*Intuition note.* Because the truth is known by construction, simulation shows which method fails under which assignment rule. Here the failures are the unadjusted comparison under unbalanced assignment, and the linear adjustment when the true relation is nonlinear and assignment is unbalanced.

### 5. Addressing computational problems

**5.1 The folk theorem of statistical computing (p. 22).**
- When computing is hard, often the model has a problem. Not always, as some models are legitimately hard to fit. But many cases of poor convergence correspond to uninteresting regions of parameter space or nonsensical models. An example of pathologies in irrelevant regions of parameter space is Figure 6. Examples of fundamentally problematic models are bugs in code and a Gaussian varying intercept per individual observation in a Gaussian or logistic regression, which data cannot inform (p. 22).
- First instinct should not be more compute (more iterations, smaller HMC step size) but checking for a substantive pathology (p. 22).

**5.2 Start at simple and complex models and meet in the middle (pp. 22–23).**
- *Figure 11 (from Gelman and Hill 2007).* Simple models that fit sit in the upper left; complex models that fail or give nonsense sit in the lower right, including the desired model (asterisk). A dotted line suggests the problem lies somewhere between them (p. 23).
- Strategy: strip the failing model down until something works, and, from the other side, add features to a simple, well-understood model until the problem appears (pp. 22–23).
- If a model has several components (e.g. a differential equation and a linear predictor for its parameters), first check each can be fit separately with simulated data, as a kind of unit test (p. 23).
- We may never fit the original complex model: it may be too hard, data and prior information may be too weak, or exploration may lead elsewhere (p. 23).

**5.3 Models that take a long time to fit (pp. 23–24).**
- HMC can be slow because of expensive gradients (differential equations), high dimension, or posterior geometry where step sizes suit one region and not another. Slowness often signals other problems, but it also makes debugging harder (p. 23).
- *Stan-users example:* multilevel logistic regression, 35,000 data points, 14 predictors, 9 batches of varying intercepts, not finished after several hours using rstanarm defaults. Suggestions, given in no particular order (pp. 23–24):
  - simulate fake data and fit it, because a badly specified model is often slow and there is no lack of fit to worry about;
  - start smaller: no varying intercepts, then add one batch at a time;
  - run 200 iterations instead of the default (2000 can come later); if $\widehat R$ is still large after 200 iterations, run longer;
  - put at least moderately informative priors on coefficients and group-level variances;
  - consider interactions of group-level predictors. Adding them should only increase run time, but the goal is to make predictions or learn about the process, not to make an arbitrary pre-chosen model converge;
  - fit a subset of the data.
- Common theme: treat any model choice as provisional, since many models must be fit to gain control over computation and inference (p. 24).

**5.4 Monitoring intermediate quantities (p. 24).** Save intermediate quantities and plot them alongside MCMC output (e.g. with bayesplot or ArviZ) rather than using print statements; in the authors' experience they learn more from a visualisation than from numbers in the console. If chains are stuck in low-density corners, look at the model's predictions at those parameter values. The most direct approach is to plot expected data given the stuck parameters and transform the gradient of the parameters into the gradient of the expected data (p. 24).

**5.5 Stacking to reweight poorly mixing chains (pp. 24–25).**
- Often MCMC mixes fine. Sometimes simulations quickly move to unreasonable regions, which may indicate misspecification, uninformative observations or difficult geometry (p. 24).
- In the intermediate case (chains slow to mix but in a generally reasonable range), *stacking* combines chains with cross-validation-based weights. This approximately discards chains stuck in low-probability modes (p. 25).
- The result is not necessarily equivalent to fully Bayesian inference even asymptotically. It is suited to model exploration, and non-uniform weights with traceplots can show where to focus effort (p. 25).

**5.6 Multimodality and other difficult geometry (p. 25).** Four kinds of problem:
1. *Disjoint volumes where all but one mode have near-zero mass* (example in Section 11). Avoid minor modes with good initial values, prior information or hard constraints, or prune them by approximately estimating each mode's mass.
2. *Disjoint, high-mass, trivially symmetric volumes* (e.g. label switching in mixtures). Standard practice is to restrict the model to identify the mode of interest.
3. *Disjoint, high-mass, different volumes.* Example: a gene-regulation model where data admit two regimes with opposite effect signs, while an effect near zero has much lower density. This is harder. Options: stacking (predictive model averaging), which is not fully general since it needs a predictive quantity of interest; a more fully Bayesian alternative of splitting the model with a strong mixture prior and fitting each component separately; or strong priors that rule out some modes.
4. *A single high-mass volume with an arithmetically unstable tail.* If you initialise near the mass, there should be no problem for most inferences. If extremely rare events matter, reparameterise anyway, because there is a limit to what can be learned from an effective sample size of a few hundred to a few thousand.

## Toy example (ours, not from the text)
**Idea:** Bayesian inference is calibrated on average over the prior, not at a fixed true value (Section 4.2, p. 18). Coin with $\theta\in\{0.2,0.8\}$. Prior $P(\theta=0.8)=0.1$, $P(\theta=0.2)=0.9$. One flip $y\in\{0,1\}$.

- Posterior given $y=1$: $P(0.8\mid 1)=\frac{0.8\cdot0.1}{0.8\cdot0.1+0.2\cdot0.9}=\frac{0.08}{0.26}=0.3077$.
- Posterior given $y=0$: $P(0.8\mid 0)=\frac{0.2\cdot0.1}{0.2\cdot0.1+0.8\cdot0.9}=\frac{0.02}{0.74}=0.0270$.
- *SBC-style check (draw $\theta$ from the prior, then $y$).* $P(y=1)=0.26$, $P(y=0)=0.74$. Average posterior probability of $\theta=0.8$: $0.26\times0.3077+0.74\times0.0270=0.08+0.02=0.10$. This equals the prior probability, so inference is calibrated.
- *Single-truth check, truth $\theta=0.8$:* $y=1$ with probability 0.8. Average posterior probability of $\theta=0.8$: $0.8\times0.3077+0.2\times0.0270=0.2462+0.0054=0.2516$.
- *Single-truth check, truth $\theta=0.2$:* $0.2\times0.3077+0.8\times0.0270=0.0615+0.0216=0.0832$.
- Neither fixed-truth average is 0.10. Weighting by the prior gives $0.1\times0.2516+0.9\times0.0832=0.0252+0.0749=0.100$, the calibrated value.

So the posterior is "wrong" at each single true value in this sense, yet exactly right on average over the prior. A one-truth fake-data run is therefore only a rough check, while SBC tests the calibration property.

## Concepts
- [[bayesian-workflow]] — the full cycle of model building, inference, checking/improvement and model comparison, with many models fit; broader than computing p(θ|y) (p. 3)
- [[bayesian-inference-vs-workflow]] (new) — inference = conditional probability computation p(θ|y) ∝ p(θ)p(y|θ); workflow adds building, checking, comparing (p. 3)
- [[meta-workflow-codification]] (new) — example → case study → workflow → method → theory as the path of statistical ideas (p. 6)
- [[modular-model-construction]] (new) — treat model components as replaceable placeholders and name modules, not whole models (p. 9)
- [[prior-predictive-check]] — simulate data from the prior and model to see what the prior implies, without using observed data (p. 10)
- [[generative-model]] (new) — a joint distribution of data and parameters; needed for simulation and checking though not for inference, which needs only the likelihood (p. 11)
- [[improper-prior-as-placeholder]] (new) — improper priors give no joint distribution for prior predictive sampling; treated as a step toward a proper model (p. 12)
- [[markov-chain-monte-carlo-mcmc]] — approximation whose theoretical error goes to zero with more draws; here mostly HMC (p. 14)
- [[hamiltonian-monte-carlo-hmc-nuts]] — a generalisation of Metropolis that uses gradients to move efficiently in continuous spaces (p. 13)
- [[warmup]] (new) — initial MCMC phase that moves from initial values to the typical region, sets tuning parameters and flags bad models (p. 13)
- [[convergence-diagnostics-r-hat-ess-divergences]] — $\widehat R<1.01$, $R^*$, effective sample size, absence of divergent transitions; they cannot detect a model coded differently than intended (pp. 13, 16)
- [[approximate-algorithm-as-approximate-model]] (new) — an approximate algorithm can be viewed as an exact algorithm for an approximate model (p. 15)
- [[variational-inference-elbo]] — fast, possibly inaccurate posterior approximation; also used as a mode-finding approximation (pp. 13, 15)
- [[fit-fast-fail-fast]] (new) — goal of quickly detecting bad models so little time is spent on them (p. 15)
- [[fake-data-simulation]] (new) — fit the model to data simulated from known parameters to check recovery; gives an upper bound on what can be learned about latent variables (pp. 16–18)
- [[simulation-based-calibration]] (new) — draw parameters from the prior, simulate data, fit, compare posteriors with the generating values; checks calibration on average over the prior (p. 18)
- [[folk-theorem-of-statistical-computing]] (new) — computational problems often indicate a model problem (p. 22)
- [[stacking]] (new) — combine chains or models with cross-validation weights; approximate, not necessarily equivalent to full Bayes (p. 25)
- [[typical-set]] — region of parameter space where log posterior density is near its expected value, which the paper relates to the typical set; warmup moves the chain toward it (p. 13)
- [[partial-pooling-shrinkage]] — pooling of group estimates, said to work better on scale-free parameters (p. 9)

## Canonical instances
- [[logistic-regression-prior-predictive]] — independent normal(0,1) priors imply extreme $\bar y$ as predictors go from 2 to 15 (p. 10)
- [[gp-prior-predictive-draws]] — GP prior draws depend on amplitude $\tau$ and length scale $l$ (p. 11)
- [[binomial-vs-negative-binomial-sampling]] — same likelihood for θ, different generative models and predictive checks (p. 11)
- [[election-2020-forecast-model]] — fully modelled polls plus fundamentals; can be run forward to generate polls (p. 12)
- [[ellipse-orbit-fit-fail-fast]] — an ellipse fits ordinary orbit data but a perturbed orbit should make the fit fail fast (pp. 15–16)
- [[exam-treatment-simulation]] — 500-student constructed data comparing balanced and unbalanced assignment, linear and nonlinear truth (pp. 20–22)
- [[stan-users-multilevel-logistic-slow-fit]] — 35,000 points, 14 predictors, 9 batches of intercepts, with six debugging suggestions (p. 23)

## Bridges (candidates)
- [structural-analogy] Exam-treatment simulation with assignment depending on $x$ ↔ causal inference: assignment mechanism / ignorability — adjusting for the covariate that drives assignment can fail if the outcome model's functional form is wrong (pp. 20–22).
- [structural-analogy] Stacking of chains/models with cross-validation weights ↔ model averaging in predictive ensembles — weights are chosen by predictive performance, not by posterior probability (p. 25).
- [metaphor] "Premature optimization" in software engineering ↔ running MCMC to large effective sample size for an untested model — compute is wasted if bugs appear early (p. 14).

## Questions this raises
- How should SBC be run with few draws, or with a designed rather than random exploration of the prior? The authors call this open (p. 18).
- The authors say stacking need not match full Bayesian inference even asymptotically. When is it good enough, and how do we define the predictive quantity it needs? (p. 25)
- If the two-step "fit real data, then simulate from the posterior" check has unclear statistical properties (p. 17), how can its reliability be assessed?
- How can methods be evaluated by how quickly they fail on bad models (p. 15)?

## Reading notes
- **Part boundary.** This unit starts at the title page and abstract (p. 1) and ends on p. 25 with the four-bullet list of Section 5.6. Section 5.7 (Reparameterization) starts after this part, on p. 26 according to the contents. The table of contents on pp. 1–3 lists Sections 5.7–12, which are not covered here.
- **Page numbers.** Printed = pdf; no offset.
- **Edition facts.** The title page reads "Bayesian workflow", dated 2 Nov 2020, with arXiv stamp arXiv:2011.01808v1 [stat.ME] 3 Nov 2020. The footnote says much of Sections 10 and 11 is taken from Gelman (2019) and Margossian and Gelman (2020).
- **Misprints and inconsistencies seen in the pages:**
  - p. 10, Figure 3 caption: says "posterior predictive distribution becomes concentrated", but the check is a prior predictive one.
  - p. 20: the text says scores are $\text{normal}(\eta_i,10)$ but gives the correlation as $20^2/(20^2+5^2)=0.94$. That arithmetic corresponds to noise sd 5. With noise sd 10 the same formula gives $400/500=0.8$ (our arithmetic). I report both as printed.
  - p. 21: the formula $\Pr(z=1)=\text{logit}^{-1}((x-50)/10)$ increases with $x$. The text and the Figure 9 curve (decreasing with pre-test score) say lower scorers are more likely treated, so a sign seems reversed in the formula.
  - p. 21: "the 200 students", but the example has 500; "Figure 9a displays the simulated exam scores" should be 9b; "final final exam score". The Figure 9 panel title reads "Unalanced" (sic) in the image as well as in the text layer.
  - p. 7: "with data are added". p. 9: "proportion of volume that the liver". p. 4 cites "Wickham and Groelmund, 2017" while p. 6 cites "Grolemund and Wickham, 2017".
- Figures 1, 3, 4, 5, 7, 9 and 11 were read from the images (Figure 4 parameter values, Figure 9 curve shape).

---
id: gelman-2020-workflow/main-p2
work: gelman-2020-workflow
unit: "paper (part 2/3): §§5.7–10.3, from reparameterization to the start of the golf example"
pages: 26-51
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Bayesian Workflow, part 2: fixing computation, evaluating, modifying and comparing models, software practice, golf example (begins)

## L0 — One line
After a model is fit, the workflow is a loop of fixing computation (often by adding prior information), checking the fit, expanding the model step by step, and comparing many fitted models to understand them rather than to pick one winner.

## L1 — The gist (≤ 120 words)
Part 2 covers what to do once a first model exists. Computational trouble can often be fixed by reparameterizing, marginalizing, or adding prior information or data. Fitted models are checked with posterior predictive checks, cross validation and prior-sensitivity tools, and are summarized graphically. Models are then expanded step by step. The authors compare them within a "topology" of models and, instead of selecting one, combine them by stacking or report all of them in a multiverse analysis. Because a model is also code, version control, testing, reproducibility and readability matter. A golf-putting example begins to show the full cycle: logistic regression, then a first-principles geometric model, then new data.

**Prerequisites:** posterior and posterior predictive distribution; MCMC/HMC basics (divergences, funnels); hierarchical models; log-concavity; leave-one-out cross validation and importance sampling; logistic regression; normal CDF Φ.

## L2 — Key ideas (5–10 bullets)
- Poor MCMC mixing can be explained by difficult posterior geometry, which in turn can be explained by data that are only weakly informative for some parts of the model (a four-step "ladder of abstraction"). Substantive prior information can fix it, but it must be real knowledge, not tweaking until the sampler runs (pp. 26–29).
- Sorting models into "identifiable" and "non-identifiable" can be misleading. The authors prefer to ask how much the actual data, at finite sample size, move the posterior away from the prior (p. 27).
- Posterior predictive checks (simulate replicated data from the fitted model and compare with the data) are often sufficient to reveal misfit, but can be overly optimistic. Cross validation (leave part of the data out and predict it; calibration via LOO-PIT, pointwise scores, influence) is less optimistic, and prior influence can be probed without refitting (pp. 30–36).
- "Noninformative" and "fully informative" priors generally do not exist. Priors form a ladder, and priors often need to tighten as models grow (the "information budget", concentration of measure, the joint prior) (pp. 39–40).
- Workflow means fitting many models in order to understand each one, not to select or average. Tools: the "topology of models", plots of inference versus complexity, and multiverse analysis (fitting all models that pass the checks and seeing whether conclusions change) (pp. 41–44).
- When averaging is needed, the authors think stacking (combining models with weights chosen to minimize cross validation error) makes more sense than Bayesian model averaging. When many candidate models are special cases of one expanded model, projection predictive selection (choosing a smaller submodel by projecting the expanded model's predictions) avoids overfitting the selection (pp. 44–45).
- Modeling is software development: version control, bottom-up testing, modularity, script-based reproducibility and readable code (pp. 45–49).
- Golf putting shows the cycle: a conventional logistic regression is beaten by a one-parameter geometric model, and new data then test it (pp. 49–51).

## L3 — Walkthrough

### 5.7 Reparameterization (p. 26)
- HMC works best when the mass matrix is well tuned and the joint posterior geometry has no sharp corners or cusps. For classical models with enough data, results such as Bernstein–von Mises suggest the posterior becomes simple (p. 26).
- Even slightly complex models cannot be guaranteed enough data for this, so a well-chosen parameterization can greatly improve HMC (p. 26).
- Example: hierarchical models can have funnel pathologies when group-level variance parameters approach zero (Neal, 2011). Reparameterization can resolve many such cases (p. 26).

> *Intuition note.* The same model can be written in different coordinates. In some coordinates the posterior geometry is simple, and in others it can have a funnel. The authors say HMC behaviour can be greatly improved by choosing a parameterization that simplifies the geometry.

### 5.8 Marginalization (p. 26)
- Hard geometries often come from parameter interactions, e.g. the funnel in the joint density of group-level scale $\phi$ and individual-level mean $\theta$. The marginal density of $\phi$ is well behaved (p. 26).
- So one can sample the marginal posterior
$$p(\phi\mid y)=\int_\Theta p(\phi,\theta\mid y)\,d\theta .$$
This needs only the marginal likelihood $p(y\mid\phi)$. Draws of $\theta$ are then recovered by exact sampling from $p(\theta\mid\phi,y)$ at small cost. This is notably used for Gaussian processes with normal likelihood (p. 26).
- In general $p(y\mid\phi)$ and $p(\theta\mid\phi,y)$ are not available. A Laplace approximation can be used, notably for latent Gaussian models. Coupled with HMC this can, depending on the case, beat reparameterization, sometimes at the cost of bias (p. 26).

### 5.9 Adding prior information (pp. 26–29)
- Computational problems can often be fixed by prior information that was available but not yet included, for instance because elicitation is costly and we began from a template model and prior. Running more iterations can sometimes help. The authors stress this is not to say that fixing fitting problems is the primary use of priors (p. 26).
- Careful inspection or diagnostics may show the data are not informative for all parts of the model (p. 26–27).
- **Against a binary view of identification.** Classifying models as identifiable or not can mislead, even with "partial/weak" categories, because information depends on the realized data. Identification is formally asymptotic, but Bayesian inference cares about finite data. The authors prefer to look at the posterior in front of them (p. 27).
- Lindley (1956) and Goel & DeGroot (1981) measure the information in an experiment by how different posterior is from prior. If data are uninformative on some aspect, priors can add information. The authors often prefer a model whose parameters the data can update over one closer to the truth where the data cannot (p. 27).

**Worked example: sum of declining exponentials** (Fig. 12–13, pp. 27–28)
- Model: $y_i=(a_1e^{-b_1x_i}+a_2e^{-b_2x_i})\times e^{\epsilon_i}$, $i=1,\dots,n$, with independent $\epsilon_i\sim\text{normal}(0,\sigma)$. Here $a_1,a_2,\sigma>0$; $b_1,b_2>0$; and $b_1<b_2$ (ordering makes the two components unique) (p. 27).
- Fake data: 1000 points, $x$ uniformly spaced on $[0,10]$, $a_1=1.0$, $a_2=0.8$, $\sigma=0.2$ (p. 27–28).
- Case (a): $(b_1,b_2)=(0.1,2.0)$, a factor 20 apart. Stan fit runs smoothly and recovers the five parameters (p. 28).
- Case (b): $(b_1,b_2)=(0.1,0.2)$, a factor 2 apart. The model is still true by construction, but convergence is terrible. The curve $y=1.8e^{-0.135x}$ is essentially indistinguishable from the true curve over these data (p. 28; Fig. 12 caption, p. 27).
- Example of a fix: default normal(0,1) priors on all parameters give sufficient regularization, while staying weak if the model is set up on roughly unit scale (Section 2.3, assumed done here). Sensitivity can be checked by comparing normal(0,0.5) and normal(0,2), or by differentiating inferences with respect to prior scale (Section 6.3) (p. 28).
- An informative normal prior adds to the tail-log-concavity of the posterior, which gives quicker mixing. This is not a bias-versus-speed tradeoff: model fitting improves as computation eases, an instance of the folk theorem of Section 5.1 (pp. 28–29).
- Caveats: strong priors can have thick tails, so more log-concave tails are not guaranteed. Conversely, a prior can be weak relative to the likelihood and still give a log-concave tail. Informativeness depends on what questions are asked (p. 29).
- **Ladder of abstraction** (p. 29): (1) poor MCMC mixing; (2) difficult geometry as the mathematical explanation; (3) weakly informative data for some parts of the model as the statistical explanation; (4) substantive prior information as the solution. Read from step 1 it is computational troubleshooting. Read from step 4 it is computational workflow (p. 29).
- Zero-avoiding priors (e.g. lognormal, inverse gamma) can avoid the high-curvature region of hierarchical funnels. They can make sense when such prior information is available, e.g. for a Gaussian-process length-scale. The authors want to be careful when using such a restriction merely to make the algorithm run faster, and at the very least a restrictive prior used to speed computation should be clearly stated as information added to the model (p. 29).
- Poor mixing can often be fixed by stronger regularization. To regularize without blurring what we want to estimate needs actual subject-matter knowledge. Haphazard tweaking until problems vanish is dangerous and hard to diagnose (p. 29).

> *Intuition note.* In the sum-of-exponentials example the data could hardly tell the two exponentials apart and the fit converged terribly. A default normal(0,1) prior on roughly unit-scale parameters made the computation more stable. The authors add that regularizing without blurring what we want to estimate needs real subject-matter knowledge, not haphazard tweaking.

### 5.10 Adding data (p. 29; Fig. 13, p. 28)
- One can constrain a model by adding data sources handled inside it, e.g. a calibration experiment informing a response's standard deviation (p. 29).
- Models fine for large data can have computational issues in small-data regimes. Fig. 13A: the normal likelihood in $(\mu,\sigma)$ for $N=1$ increases without bound, for $N=2$ is still funnel-like, and for $N=8$ the funnel is mostly suppressed (p. 28).
- Fig. 13B: an 8-parameter Lotka–Volterra model shows a funnel with divergent transitions at 6 data points. It is fittable at 9 and well behaved at 21 (p. 28).
- This funnel resembles the hierarchical one but is much harder to avoid. Often we can only acknowledge that the full model is not informed by the data and use a simpler model (p. 29).

### 6 Evaluating and using a fitted model (p. 30)
Many checks are possible, each leading in many directions. Which aspects need checking depends on the application (p. 30).

### 6.1 Posterior predictive checking (p. 30–31)
- Like prior predictive checking, but parameter draws come from the posterior. It can examine fit to real data (p. 30).
- If the data look unrepresentative of the posterior predictive distribution, the model fails to describe some aspect of the data. The most direct checks compare simulations with the full data distribution or summary statistics, including for groupings not in the model (p. 30).
- There is no general rule for which checks to run or when a failed check requires changing the model. This depends on goals, costs and benefits. The authors look for "severe tests" (Mayo, 2018): checks likely to fail if the model would mislead on the questions we care most about (p. 30).
- Fig. 14 (p. 31): (A) density check, normal fit to lognormal data, tails of $y_{rep}$ differ; (B) statistic check ($T=\text{sd}$), binomial fit to beta-binomial data, observed sd larger than the model can produce; (C) bars check for discrete data looks fine; (D) same data grouped by an omitted covariate: the "High" subgroup lies outside the range of $y_{rep}$.
- Fig. 15 (p. 32): a more involved check from a psychology experiment (15×23 binary responses for 6 participants, versus 7 replicated datasets) shows patterns in the observed data absent from the replications. Such checks often need a custom visualization (p. 30).

### 6.2 Cross validation and influence (pp. 30–34)
- Posterior predictive checks use the data twice (fit and evaluation) and can be overly optimistic. Cross validation leaves part of the data out, fits the rest, and checks prediction on the held-out part. It especially helps for flexible models (p. 30).
- Three diagnostics: (1) calibration of the CV predictive distribution; (2) which observations or groups are hardest to predict; (3) how influential observations are, i.e. how much information they add beyond the others. Importance-sampling approximations to LOO avoid refitting per point (p. 31).
- **LOO-PIT** (p. 31–32). Perfect calibration is not the ultimate goal, but checking it can reveal improvements. PPC compares marginal distributions of predictions to data. LOO-CV predictive checking examines conditional predictive distributions. Under good calibration the conditional CDF values of the left-out observations (probability integral transforms, PIT) are uniform. Deviations show under- or overdispersion. In Fig. 16 (Gabry et al., 2019) LOO-PIT values are concentrated near the middle, so predictive distributions are overdispersed (pp. 31–33).
- **Hard-to-predict points: Bangladesh arsenic example** (p. 32). Households with elevated well-arsenic were asked if they would switch to a neighbor's well. Several models predicted this binary response. Comparing pointwise log scores of two models (Fig. 17): the summed difference in expected log predictive density is $\text{elpd}_{\text{loo}}=16.4$ with standard error 4.4. The plot also shows which points cause the difference: 10–15 non-switchers with very high existing arsenic. The authors did not follow up here, because better-fitting models would not change the conclusions or recommended actions (p. 32).
- **Influence** (p. 34). One can look at how parameter inferences change when each point is left out. Limitation: if data are clustered, several points may need removing to have an effect. It is cheap, so useful. Influence can be summarized from the importance weights used in the LOO approximation.
- **Weighted-likelihood alternative** (p. 34). Take $\prod_{i=1}^n p(y_i\mid\theta)^{\alpha_i}$, which equals the original likelihood when $\alpha_i=1$ for all $i$. LOO corresponds to $\alpha_i=0$ for one observation. Another option (Giordano et al., 2018) is the gradient of the augmented log likelihood with respect to $\alpha$: a differential cross validation or influence function.
- **Multilevel models** (p. 34). Leave-one-out is possible but may not match inferential goals. In survey adjustment with state-level interest, improvements at state level may be undetectable under observation-level CV (Wang & Gelman, 2016). Variants include leave-one-unit-out and leave-one-group-out. The authors have used a mix and evaluated at both levels. Importance sampling is much harder for these variants, because more is left out and the posterior changes more. Costly refits may be needed.

> *Intuition note.* PPC asks "does simulated data look like my data?" but the model has seen that data. CV asks "can the model predict data it has not seen?", and pointwise scores tell you where it fails.

### 6.3 Influence of prior information (pp. 34–36)
- Complex models are hard to understand. A model can be understood generatively (how parameters map to data; prior predictive simulation) or inferentially (the path from data and priors to estimates and uncertainties) (p. 34).
- Most direct: refit with multiple priors (sensitivity analysis), but this can be prohibitively expensive. Shortcuts (p. 35):
  1. **Shrinkage** from prior to posterior (e.g. compare prior and posterior standard deviations or quantiles). If data are informative for a parameter relative to the prior, shrinkage should be stronger (Nott et al., 2020).
  2. **Importance sampling** to approximate the new model's posterior from the old one, provided the posteriors are close enough. If not, that is itself valuable information.
  3. **Static sensitivity analysis** (Gelman, Bois & Jiang, 1996): study sensitivity to prior perturbations without refitting.
- Fig. 18 (toxicology): posterior draws of percent metabolized under two exposure conditions, plotted against two model parameters, i.e. four scatterplots. Direct reading: the posterior correlation between the quantity of interest and a parameter. Indirect reading: a change of prior for the x-axis parameter corresponds to reweighting the points by the ratio of new prior to old prior, so the dependence in the scatterplot shows the impact. The plots show little sensitivity for one condition and strong sensitivity for the other (pp. 35–36).

### 6.4 Summarizing inference and propagating uncertainty (p. 36)
- The usual displays do not fully capture the multiple levels of variation and uncertainty. A table or graph of parameter estimates, uncertainties and standard errors shows only one-dimensional margins. Graphs of marginal posterior distributions are unwieldy for models with many parameters and fail to capture the interplay between uncertainty and variation in a hierarchical model (p. 36).
- Graph data and fitted models, for exploratory analysis and to see how the model relates to the data. Example: Ghitza & Gelman (2020) on vote preferences in the 2016 U.S. election. Fig. 19 shows the estimated white gender gap as a map, then a scatterplot motivated by the geographic pattern. The gap tends to be highest in counties where the white vote is close to evenly split. Fig. 20 compares county-level estimates from two models. The general workflow: inferential summaries motivate further exploration (pp. 36–37).
- Probabilistic programming could ultimately let random variables be manipulated like other data objects with uncertainty implicit in plots. Much work is still needed (p. 36).

### 7 Modifying a model (pp. 36–42)
- Model building is "language-like": assembling components (linear, logistic and exponential functions, binomial/Poisson/normal distributions, varying coefficients). Most parts are placeholders for replacement or expansion, or one may need approximations (pp. 36–38).
- Expansion responds to new data, failures on existing data, or computational struggles. Election forecast: the 2016 adaptation of Linzer's (2013) poll-aggregation model failed in certain swing states. The authors attributed this to poor modeling of correlations of vote swings between states and to nonsampling polling error. The revision added both (p. 38).

**7.1 Constructing a model for the data** (p. 38). In applications the data model should come from fit (posterior predictive checks) plus domain expertise. If chosen from a small menu, say so. Often the key aspect is how data link to parameters of interest, not the distribution form (e.g. nonsampling error terms for polls). Preprocessed data make any generative model an approximation. Bias can matter more than measurement error. It can make sense to expand the model to allow systematic error (Section 10.5).

**7.2 Incorporating additional data** (pp. 38–39).
- More data usually means more parameters. It can then be necessary to assume that not all of them can have a big effect in the model at the same time. Adding a parameter can be seen as relaxing a prior previously concentrated at zero. Example: interaction terms allowing the national-economy coefficient to be lower in recent years (p. 38).
- Two measurement forms of similar data need a generative model for both. Example (Weber et al., 2018): direct patient data for one drug, only averages for a competitor. The authors approximated the relevant integral analytically instead of modeling the averaged patients' outcomes as latent data (pp. 38–39).

**7.3 Working with prior distributions** (pp. 39–41).
- Noninformative and fully informative priors generally do not exist. A uniform prior depends on parameterization, a reference prior depends on an assumed asymptotic regime, and an informative prior rarely includes all knowledge. Instead, a **ladder**: (improper) flat; super-vague proper; very weakly informative; generic weakly informative; specific informative (p. 39).
- Election-model example: each random walk has an innovation standard deviation (daily, logit scale). Options: uniform; normal$^+$(0,1000) (normal truncated to positive); normal$^+$(0,1) on the percentage scale, which allows unrealistically large daily changes on the order of 0.25 percentage points but keeps away from extreme values; or normal$^+$(0,0.1), which softly constrains the parameter. Choosing a prior is choosing how much subject-matter information to include (p. 39).
- A prior can also be seen as a constraint. In $y=b_0+b_1x+g(x)+\text{error}$ with $g$ of bounded variation, a strong enough prior on $g$ gives a nearly linear fit (Simpson et al., 2017). A clear distinction between prior and model is largely arbitrary (p. 39).
- Required information depends on the parameter's role and depth in the hierarchy. Central quantities (mean, median) tolerate vague priors more than scale parameters, which tolerate them more than tail parameters (e.g. the GEV shape). Parameters closer to the data tolerate vague priors more than those further down the hierarchy (Goel & DeGroot, 1981) (p. 39).
- **Information budget** (p. 40). Data $y_{ij}$, $i=1,\dots,n_j$, $j=1,\dots,J$. Model 1 ignores groups: with moderate data, the mean is about $\bar y=\sum_{i=1}^n y_i/n$ however weak the prior, and the predictive distribution is about normal($\bar y$, $s$) with $s$ the sample sd. Model 2 lets the mean vary by group: $J+1$ extra parameters (one per group plus the between-group sd) split the same information. We "probably need to tighten up" the priors on the overall mean and observation sd, lest lack of information gives nonsense estimates.
- **Concentration of measure** (p. 40). With more predictors, the coefficient prior needs more density near the mode to keep most prior mass there. If the marginal prior on weights is fixed, the prior on $R^2$ is affected; to keep the prior on $R^2$ fixed, the prior on weights needs to get tighter. Fig. 21: the usual weak prior on 26 regression weights implies a prior strongly favoring high $R^2$ (it also affects the posterior). Alternatives shown: a normal prior scaled with number of predictors, and a regularized horseshoe. Weakly informative but independent priors may jointly be strongly informative if numerous (pp. 40–41).
- **Reparameterizing priors when expanding** (p. 40). Going from normal$(\mu,\sigma)$ to $t_\nu(\mu,\sigma)$, the variance is $\frac{\nu}{\nu-2}\sigma^2$, not $\sigma^2$. For small $\nu$, $\sigma$ is no longer close to the residual sd.
- Think in terms of the **joint** prior in the context of the generative model, lest cancellations or resonances give less stabilizing or more informative priors than intended. Prior predictive checking is the general tool. The "information budget" idea is informal but reflects important decisions that are not always clear in articles or textbooks presenting the final model (pp. 40–41).

> *Intuition note.* Each new parameter shares the same fixed amount of data. As a model grows, priors on old parameters may need tightening. Many individually weak priors can add up to a strong statement, e.g. about $R^2$.

**7.4 A topology of models** (pp. 41–42).
- Model classes (ARMA, classification trees, linear regression with fixed inputs) form partial orderings: AR(1) is simpler than AR(2), which is simpler than ARMA(2,1); MA(1) is also simpler than ARMA(2,1); AR(1) and MA(1) are not ordered. Inclusion/exclusion of $k$ regression variables gives $2^k$ corners of a cube (p. 41).
- It is a topology, not a probability space, because the goal is navigating among models, not assigning them probabilities or averaging. The topology covers the connections between models and between parameters in neighboring models (p. 41).
- Examples: the Automatic Statistician searches open-ended model classes using inference and model criticism. Menu-based packages such as Prophet need users to understand each model relative to simpler or more complex variants. The authors believe such algorithms can be better understood and improved via a formal topology of models (p. 41).
- Model outputs can be added, multiplied, linearly or log-linearly or pointwise mixed (a choice within the topology). Parameters in different models can share observable meaning, e.g. in forecasting and in causal inference (a treatment effect estimated by a series of regressions; causal inference as prediction with counterfactuals). Priors add a continuous dimension bridging models (p. 42).

### 8 Understanding and comparing multiple models (pp. 42–45)

**8.1 Visualizing models in relation to each other** (pp. 42–44)
- What takes workflow beyond Bayesian data analysis is fitting many models for one problem, not for selection or averaging but to understand each. In Wickham et al.'s words, we "explore the process of model fitting, not just the end result" (p. 42).
- Reasons for multiple models (pp. 42–43): big models are hard to fit, so build up from simple ones; mistakes (typos, coding, conceptual errors); more data arrive; a well-specified model fit to data suggests further expansion; placeholder priors, from weak to strong or strong to weak; checked models with problems are expanded or replaced but old ones kept for understanding; simple comparison models (e.g. unadjusted causal comparison); computational problems.
- Concern: researcher degrees of freedom (Simmons et al., 2011): overfitting if a single best model is picked, or treating the spread across fitted models as total uncertainty when other models could have been fit. This arises in election forecasting, with only a handful of past presidential elections (p. 43).
- Fig. 22 (hypothetical): inference for a quantity of interest (e.g. a causal effect) plotted from a simple comparison on the left to the final model on the right (p. 43).
- **Multiverse analysis:** when several models pass all checks, use all of them and see how conclusions change (pp. 43–44). If conclusions do not change, it matters less which model is "best". Fig. 23 (Niederlová et al., 2019): BBSome gene mutation/phenotype conclusions across Bayesian hierarchical logistic models (categorized by posterior predictive checks as "Main", "Secondary", "Problematic fits") and frequentist tests. Most conclusions hold across all models (p. 44). Other choices (preprocessing, response distribution, metric) can also be put in a multiverse.

**8.2 Cross validation and model averaging** (pp. 44–45)
- CV can compare models fit to the same data. If the comparison has non-negligible uncertainty (Sivula et al., 2020), do not just choose the best CV model, which discards that uncertainty. Use **stacking**: combine inferences with weights set to minimize cross validation error (Yao et al., 2018b) (p. 44).
- Stacking is preferred to traditional Bayesian model averaging, which can depend strongly on aspects with minimal effect on predictions. Example: for a well-informed model with $k$ unit-scale parameters, changing the prior from normal(0,10) to normal(0,100) divides the marginal likelihood by roughly $10^k$ while predictions stay essentially the same. Stacking also uses joint predictions and works with many similar weak models (pp. 44–45).
- Stacking can be viewed as pointwise model selection: if model 1 outperforms model 2 20% of the time, weights will be close to (0.2, 0.8). Stacking weights indicate heterogeneity, suggesting a hierarchical model, so stacking is a step toward improvement. Models can also be applied to different data points (p. 45).
- "Scaffold" models (deliberately oversimple, experimental, flawed or buggy) are not for averaging. The authors prefer continuous model expansion and rarely average, but some settings reasonably call for it (p. 45).

**8.3 Comparing a large number of models** (p. 45)
- With many candidate models as special cases of one expanded model, one often seeks a smaller model with the same predictive performance (predictor selection). Picking by minimizing CV error among many similar models overfits (Piironen & Vehtari, 2017). Projection predictive selection has been shown to be stable and reliable. It avoids overfitting by examining only projected submodels based on the expanded model's predictions, without fitting each independently. It also serves structure selection in generalized additive multilevel models and simpler explanations of complex nonparametric models (p. 45).

### 9 Modeling as software development (pp. 45–49)
Writing a model in a probabilistic programming language is software development: model code, data preprocessing, and the later use of inferences (p. 45). Software development practice can veer into dogma or bean counting; the authors recommend Hunt & Thomas (1999) and McConnell (2004) (p. 46).

- **9.1 Version control** (p. 46): set up first (e.g. Git). It allows reverting to working versions and merging collaborators' work. Keep clearly different models in different files. It keeps notes on decisions, applies to reports, graphs and data, and labels release candidates instead of "_final_final" file names. For policy models a public repository raises transparency (example: Imperial College COVID-19 repository).
- **9.2 Testing as you go** (pp. 46–47): design top-down from user goals (data input format, probabilistic model, prior, possibly simulators and tests like simulation-based calibration or posterior predictive checks). Develop bottom-up from well-tested functions, so errors are easier to localize. Key: modularity, with repeated code encapsulated in functions. Example: standardization $z(v)=(v-\text{mean}(v))/\text{sd}(v)$ has subtleties. sd may divide by $n$ or by $n-1$, which if unsorted gives mysterious biases. With $n-1$, the length-1 vector case needs a decision. Check illegal inputs early. Higher-level functions (cubic splines, Euler solvers) are harder to test (boundary combinatorics, general inputs, numerical instability, stable derivatives).
- **9.3 Reproducibility** (pp. 47–48): the goal is that another person on another machine can recreate the report (not "replicability" with new data). Bit-level reproducibility may not be possible, but practical equivalence is wanted. If reproduction changes a paper's outcome, the authors would argue the original results were not particularly robust. Use self-contained scripts, not typed commands. Scripts are documentation, and for complex projects can be more practical than one R Markdown or Jupyter document. Bit-level reproducibility requires specifying hardware, OS and every software version, and can become almost impossible over time even with Docker.
- **9.4 Readability and maintainability** (pp. 48–49): consistency in naming and layout; no repetition. Stan was designed to be self-documenting in variable usage, types and sizes. Prefer readable code over comments, e.g. `real<lower = 0> oxygen_level;` instead of `real x17; // oxygen level, should be positive`, and `target += normal_lpdf(y | mu, sigma);` instead of the hand-written normal log density with a comment. Document user-facing functions (argument types, return types, errors, behavior). Inline developer comments go stale. Keep functions small, and replace commented blocks with well-named functions. Longer names are not always better. Keep model code modular and load shared modules into models, so an error is fixed in one place.

### 10 Example: golf putting (pp. 49–51; part of the section only)
Data (Berry, 1995, via Gelman, 2019): proportion of successful putts by professional golfers versus rounded distance from the hole. Success declines with distance (Fig. 24, p. 49; error bars are $\sqrt{\hat p_j(1-\hat p_j)/n_j}$).

**10.1 First model: logistic regression** (p. 50).
$$y_j\sim\text{binomial}\big(n_j,\ \text{logit}^{-1}(a+bx_j)\big),\quad j=1,\dots,J.$$
Fit with a uniform prior on $(a,b)$, which causes no problems given the large sample size. Fig. 25 shows the fit (labelled $a=2.23$, $b=-0.26$) with posterior draws of the curve.

**10.2 Modeling from first principles** (pp. 50–51).
- Geometry (Fig. 26): a ball of radius $r$ must be hit within a threshold angle so that it falls into a hole of radius $R$, from distance $x$: threshold $\sin^{-1}((R-r)/x)$ (p. 50).
- Human error: the golfer aims straight but small factors interfere, so the actual angle is normal, centered at 0, with sd $\sigma$ (p. 51).
- Probability of success:
$$\Pr\big(|\text{angle}|<\sin^{-1}((R-r)/x)\big)=2\Phi\!\left(\frac{\sin^{-1}((R-r)/x)}{\sigma}\right)-1,$$
with $\Phi$ the cumulative normal. (Added step: for angle $\sim\text{normal}(0,\sigma)$, $\Pr(|\text{angle}|<t)=\Phi(t/\sigma)-\Phi(-t/\sigma)=2\Phi(t/\sigma)-1$ by symmetry.) The only unknown is $\sigma$ (p. 51).
- Fit with a flat prior on $\sigma$: $\hat\sigma=1.53^\circ$ with standard error 0.02. Fig. 27: the geometry-based model fits much better than the logistic regression with one fewer parameter. The authors say the model is not perfect (angle is not the only factor) but a useful start, showing the advantage of building a model directly (p. 51).

**10.3 Testing on new data** (p. 51). Years later, newer data (Broadie, 2018) on shots up to 75 feet became available. Comparing the 0–20 ft range with the older data, the success rate is similar for longer putts but much higher than before for short putts. The authors begin to say this could be a measurement issue; the unit ends mid-sentence ("if the distances…") (p. 51).

## Toy example (ours, not from the text)
Why case (b) in Fig. 12 is hard: take $a_1=1.0$, $a_2=0.8$, $b=(0.1,0.2)$ and compare with the text's single curve $1.8e^{-0.135x}$ (p. 28). All numbers are rounded.

- $x=0$: both curves equal $1.8$.
- $x=5$: true curve $e^{-0.5}+0.8e^{-1}=0.60653+0.8(0.36788)=0.60653+0.29430=0.90083$. Single curve: $1.8e^{-0.675}=1.8(0.50916)=0.91649$. On the log scale (the model has multiplicative error): $\ln0.90083=-0.1044$ and $\ln0.91649=-0.0872$, a gap of about $0.017$.
- $x=10$: true $e^{-1}+0.8e^{-2}=0.36788+0.8(0.13534)=0.47615$. Single: $1.8e^{-1.35}=1.8(0.25924)=0.46663$. Log gap: $-0.7420$ versus $-0.7622$, about $0.020$.

The log-scale gaps (about 0.02) are roughly ten times smaller than the noise sd $\sigma=0.2$. Even with 1000 points, the likelihood can hardly tell the two-component curve from a one-component curve, so $(a_1,a_2,b_1,b_2)$ lie along a flat ridge. A normal(0,1) prior adds the missing curvature (pp. 27–28).

## Concepts
- [[posterior-predictive-check]] — simulate replicated data from the fitted model and compare with observed data or summaries, possibly by subgroup (p. 30)
- [[prior-predictive-check]] — used here to see what weak priors imply, e.g. a strongly high-$R^2$ prior from 26 weak weights (p. 40)
- [[cross-validation-loo-waic]] — leave-out evaluation; here LOO-CV for calibration, hard-to-predict points and influence, approximated by importance sampling (p. 30–31)
- [[loo-pit]] (new) — LOO probability integral transforms; uniform if predictive distributions are well calibrated (p. 31)
- [[funnel-geometry]] (new) — funnel-shaped posteriors from hierarchical variance near zero or from too few data points (pp. 26, 28)
- [[reparameterization]] (new) — rewriting the model in other coordinates to simplify posterior geometry for HMC (p. 26)
- [[marginalization-for-sampling]] (new) — sample $p(\phi\mid y)$ then draw $\theta$ from $p(\theta\mid\phi,y)$; Laplace approximation when densities are unavailable (p. 26)
- [[weakly-informative-prior-ladder]] (new) — flat → super-vague → very weakly informative → generic weakly informative → specific informative (p. 39)
- [[information-budget]] (new) — informal idea that data information is divided among parameters, so priors tighten as models grow (p. 40)
- [[static-sensitivity-analysis]] (new) — reading prior sensitivity from posterior scatterplots by reweighting with prior ratios, with no refit (p. 35)
- [[topology-of-models]] (new) — partial ordering and network of models and shared-meaning parameters, for navigating models (p. 41)
- [[multiverse-analysis]] (new) — fit and report all models that pass checks and see whether conclusions change (p. 43)
- [[stacking]] (new) — combine models with weights minimizing cross-validation error; preferred to Bayesian model averaging here (p. 44)
- [[projection-predictive-selection]] (new) — choose smaller submodels by projecting the expanded model's predictions, avoiding selection overfitting (p. 45)
- [[bayesian-workflow]] — fitting many models to understand each, not to select or average (p. 42)
- [[convergence-diagnostics]] — divergent transitions signal difficult geometry and untrustworthy results (p. 28)

## Canonical instances
- [[sum-of-exponentials-example]] — weakly informative data; normal(0,1) priors stabilize the fit (pp. 27–28)
- [[lotka-volterra-funnel]] — funnel and divergences at N=6, fine at N=21 (p. 28)
- [[bangladesh-arsenic-loo]] — pointwise LOO identifies 10–15 poorly predicted non-switchers (p. 32)
- [[toxicology-static-sensitivity]] — prior sensitivity read from scatterplots (p. 35)
- [[election-forecast-model]] — expansion after 2016 failures; random-walk prior ladder (pp. 38–39)
- [[r2-prior-26-predictors]] — weak independent priors imply a strong prior on $R^2$ (pp. 40–41)
- [[bbsome-multiverse]] — conclusions largely stable across many models (p. 44)
- [[golf-putting]] — logistic regression versus geometric model; $\hat\sigma=1.53^\circ$ (pp. 49–51)

## Bridges (candidates)
- [structural-analogy] Static sensitivity analysis (reweight posterior draws by new-to-old prior ratio) ↔ importance sampling: the same reweighting idea, applied to prior changes (p. 35).
- [same-math] LOO-CV approximation by importance weights ↔ importance sampling in Monte Carlo integration: weights correct draws from the full posterior toward a leave-out posterior (p. 31).
- [structural-analogy] Weights $\alpha_i$ on likelihood terms ↔ influence functions in robust statistics: differentiating with respect to data weights measures influence (p. 34).
- [structural-analogy] Topology of models with shared-meaning parameters ↔ causal inference: a treatment effect estimated across a sequence of adjustment models (p. 42).
- [metaphor] Ladder of abstraction from poor mixing to substantive prior ↔ debugging in software: from symptom to root cause (p. 29).

## Questions this raises
- How can one tell "real" prior information that regularizes from a restrictive prior chosen only for speed, and how should the latter be reported (p. 29)?
- How much of the information-budget argument can be made formal, e.g. via priors on $R^2$ or the joint prior (pp. 40–41)?
- When stacking weights show heterogeneity across data points, what hierarchical model should replace stacking (p. 45)?
- How should uncertainty from "other models we could have fit" be reflected in a multiverse analysis (p. 43)?

## Reading notes
- This unit is part 2 of 3. It starts at §5.7 "Reparameterization" (p. 26) and ends mid-sentence in §10.3 "Testing the fitted model on new data" (p. 51). The rest of §10 and the later sections are not covered.
- Printed page number = pdf page number for all pages here.
- Typos seen in the source text: "would sufficiently informative" (p. 26); "and and" (Fig. 12 caption, p. 27); "draws form" (p. 50); "Figure 28 these new data" (verb missing, p. 51); "should be should be" (p. 46); "Gharamani" (p. 41).
- Fig. 18: the caption does not say which exposure condition shows strong sensitivity.
- Figure 12's panel titles show the $b_1,b_2$ values for panels (a) and (b), matching the caption.
- Cross-references to Sections 2.1–2.4, 3.3, 5.1 and 10.5 point to material outside this part; their content is not summarized here. Sections 6.2–6.3, cited from §5.9, are covered in this part (pp. 30–36).
- There are no exercises in this unit.

---
id: gelman-2020-workflow/main-p3
work: gelman-2020-workflow
unit: paper (part 3/3) — end of §10 (golf), §11 (planetary motion), §12 (discussion), references
pages: 52-77
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Bayesian Workflow (part 3/3): golf model expansion, planetary multimodality, discussion

## L0 — One line
The authors argue that Bayesian modeling is best done by building models step by step, using simple or fake-data versions and predictive checks to understand each failure, rather than fitting one fixed model and trusting the defaults.

## L1 — The gist (≤ 120 words)
Two case studies show the workflow in action. In golf putting, a binomial likelihood fits large bins too tightly, so the model is expanded with a "fudge" error term. In planetary motion, chains get stuck in minor modes; a one-parameter version shows these modes are mathematical artifacts of the periodic structure of the data, so starting points are tuned and the failing chains are not just discarded. The discussion argues that iterative model building suits human and computational limits, admits the risk of double use of the data (post-selection inference), says bigger data need bigger models, and notes that every workflow has holes.

**Prerequisites:** binomial and normal likelihoods; normal CDF Φ; MCMC, chains, R̂ and trace plots; first-order ODEs; posterior and prior predictive checks (earlier sections of the paper).

## L2 — Key ideas (5–10 bullets)
- A model fitted to old golf data can fail on new data. The extended geometric model with a distance-control term needs an extra error term, because the binomial likelihood is too strong for the huge short-distance bins (pp. 52–55).
- Poor MCMC convergence was a clue about model misfit, not only a computing nuisance (the folk theorem). It was diagnosed by plotting the fit directly (p. 53).
- "Bigger data need bigger models": the golf error term has no scientific meaning but was added because it lets the model fit the data flexibly (p. 55).
- In the planetary model a simple 1-parameter version, studied with quadrature, showed that the local modes come from periodic data and are negligible in mass (pp. 57–60).
- Starting points are a tuning choice: Stan's defaults were inconsistent with prior knowledge, and drawing starts from the prior fixed the problem. The authors warn against mindlessly discarding chains; they redirect computation only after examining every chain and working out how the modes arise (pp. 60, 62).
- Slow computation is a symptom: bad parameter regions give hard ODEs, which conflicts with "fail fast" (pp. 60–61).
- Iterative building is justified for humans and computers. Its danger is that checks use the data, which creates a post-selection problem. The authors respond by building one richer model, not by selecting the best fit (pp. 63–66).
- Big data do not remove the need for modeling. Extrapolation needs assumptions; effective modeling needs regularization and latent-variable modeling; poststratification is one example of connecting a model to a population (pp. 66–67).
- Every workflow has holes. The plan is to make it structured and, where possible, automated (pp. 67–68).

## L3 — Walkthrough

### 10.3 (end). Checking the fitted model on new putting data (p. 52)
- **Author:** Figure 28 applies the already-fitted model to new golf data. At equal distances the new success rate is higher. This may mean improvement over time, or just a difference between datasets (p. 52).
- Distances in the old data are only approximate, and golfers may be better now (p. 52).
- Beyond 20 feet the new empirical success rates are lower than the old model predicts. These are much harder attempts, even after allowing for the angular precision needed at long range. The new data also look smoother, perhaps from more comprehensive collection (p. 52). This motivates a model improvement.

### 10.4. A new model accounting for how hard the ball is hit (pp. 52–53)
- Broadie (2018): the putt goes in if (a) the angle lets the ball go over the hole and (b) the potential travel distance $u$ (distance the ball would go if there were no hole) lies in $[x, x+3]$. The ball must reach the hole but not go too far (p. 52).
- Broadie assumes the golfer aims one foot past the hole with multiplicative error: $u=(x+1)(1+\epsilon)$ with $\epsilon\sim$ normal$(0,\sigma_{\text{distance}})$. Hence $u\sim\text{normal}\big(x+1,\,(x+1)\sigma_{\text{distance}}\big)$ (pp. 52–53).
- (added step) Standardizing the endpoints of $[x,x+3]$ gives $(x-(x+1))/((x+1)\sigma_{\text{distance}})=-1/((x+1)\sigma_{\text{distance}})$ and $(x+3-(x+1))/((x+1)\sigma_{\text{distance}})=2/((x+1)\sigma_{\text{distance}})$.
- So the distance is acceptable with probability $\Phi\!\big(\tfrac{2}{(x+1)\sigma_{\text{distance}}}\big)-\Phi\!\big(\tfrac{-1}{(x+1)\sigma_{\text{distance}}}\big)$ (p. 53). Multiplying by the angle factor from the earlier model, the success probability is
$$
\left(2\Phi\!\left(\frac{\sin^{-1}((R-r)/x)}{\sigma_{\text{angle}}}\right)-1\right)\left(\Phi\!\left(\frac{2}{(x+1)\sigma_{\text{distance}}}\right)-\Phi\!\left(\frac{-1}{(x+1)\sigma_{\text{distance}}}\right)\right),
$$
where the earlier $\sigma$ is renamed $\sigma_{\text{angle}}$ (p. 53). The model now has two parameters. The authors call it a gross oversimplification that should still improve on the one-parameter model (p. 53).
- **Fitting problems.** Flat priors gave computational instability, so weakly informative half-normal(0,1) priors were used. With 4 chains of 2000 iterations, R̂ was still high, indicating poor mixing. The authors were concerned about the model, following the folk theorem (Sec. 5.1) (p. 53).
- They did not study trace plots. They plotted the fit using crude parameter estimates averaged over the poorly mixing chains (Figure 30a). The fit is "not terrible" but poor in the middle of the curve (p. 53).
- **Diagnosis:** the binomial likelihood constrains the model too strongly where counts are large, at the upper left. The first bins have very large $n$ (Figure 30b, e.g. $n=45198$ with $y=45183$ at $x=0.28$). The likelihood gives these points by far the most weight (pp. 53–54).
- If we were sure the model was correct this would be right. Given inevitable model error it distorts the whole curve. Poor convergence is understandable: no parameter values fit all the data, and chains struggle to move between values that fit the bulk and values that fit the first few points (p. 53).

> **Intuition note.** With huge counts, the binomial says the success rate in a bin is known extremely precisely. A simple geometric model cannot match all such tight targets at once. The sampler struggled because the model is misspecified, not only because of an algorithm problem.

### 10.5. Expanding the model with a fudge factor (pp. 53–55)
- Binning rounds distances to bin centers, which matters most at short distances. A rounding-error model is possible, but the authors choose a simpler error model (pp. 53–54).
- A beta-binomial would not help here. Its variance for point $j$ would still be roughly proportional to $n_j$, and the aim is to escape that assumption and allow for misspecification (p. 54).
- Instead, approximate the binomial by a normal and add independent variance, with $y_j\sim$ binomial$(n_j,p_j)$ replaced by
$$
y_j/n_j \sim \text{normal}\!\left(p_j,\ \sqrt{p_j(1-p_j)/n_j+\sigma_y^2}\right). \tag{unnumbered, p. 54}
$$
- The authors say it would fall apart if counts in any cell were small, but it is transparent and easy to code; it can be cleaned up later (p. 54).
- With half-normal(0,1) priors on all three parameters it fits without problems in Stan. Posterior means: $\sigma_{\text{angle}}=1.02^\circ$; $\sigma_{\text{distance}}=0.08$ (about 8% uncertainty in distance); $\sigma_y=0.003$ (the geometric model fits the aggregate success rate to within about 0.3 percentage points) (p. 54).
- Figure 31: the fit is good. Residuals $y_j/n_j-\hat p_j$ show no strong pattern and are small (within about half a percentage point at most distances). This suggests not a perfect model but no clear way to develop it further with the current data (p. 55).
- Possible improvements: let the two parameters vary by golfer, hole and weather. A key motivation for model expansion is to allow more data to be included (p. 55).

> **Intuition note.** The extra variance $\sigma_y^2$ puts a floor under how precise the data are allowed to be. It stops the largest bins from dictating the fit. It has no golf meaning; it absorbs what the geometry cannot explain.

### 10.6. General lessons from golf (pp. 55–56)
- A simple one-parameter model fit the first data. One more parameter handled the new data (p. 55).
- The binomial likelihood was too strong for the new model to fit all the data. This "stickiness" shows up in computation and inference, is implicit in any Bayesian model, but can become more prominent as sample size increases (p. 55).
- "Bigger data need bigger models". The error term has no golf interpretation but lets the model fit flexibly. It is like letting a treatment effect vary by area in a multi-center trial, or including a fully saturated interaction term in classical analysis of variance (p. 55).
- Compare models in a sequence by graphing predictions with data and by watching how estimates change. Adding distance uncertainty lowers the estimated angular uncertainty (p. 55).
- The final model is still a work in progress, so one wants a probabilistic programming environment to extend it by player and course condition (pp. 55–56).

### 11. Planetary motion: workflow with unexpected multimodality (p. 56)
- Unlike golf, here we start with a complicated model, hit inference problems, and must find out why (p. 56).
- The example shows that the workflow needs both statistical and field expertise and is not automated. The right visualization is often the key. The authors monitor intermediate quantities (Sec. 5.4) and use predictive checks extensively (p. 56).

### 11.1. Mechanistic model of motion (pp. 56–57)
- Instead of fitting an ellipse, use Newton's laws as a first-order system (Hamilton's form). This lets one estimate physical quantities such as stellar mass and apply domain knowledge (p. 56):
$$
\frac{dq}{dt}=\frac{p}{m},\qquad \frac{dp}{dt}=-\frac{k}{r^{3}}(q-q_*).
$$
- Here $q(t)$ is position and $p(t)$ momentum (each a length-2 vector, since the planet moves in a plane). $m$ is the planet's mass (taken as 1). $k=GmM$ with $G=10^{-3}$ and $M$ the stellar mass, so $k=10^{-3}M$. $r=\sqrt{(q-q_*)^T(q-q_*)}$ is the star–planet distance, and the star's position $q_*$ is fixed (pp. 56–57).
- Latent variables: $k$, initial position and momentum $q_0,p_0$, later positions $q(t)$, and $q_*$. Cartesian coordinates are used for simplicity (p. 57).
- Observations at times $t_1,\dots,t_n$ have independent normal errors: $q_{\text{obs},i}\sim \mathrm N_2(q(t_i),\sigma^2 I)$ (p. 57).
- Fake-data fitting in Stan (which has a numerical ODE solver) fails dramatically: chains do not converge and take long. The authors respond by simplifying the model, with simulated data so the truth is known (p. 57).

### 11.2. Fitting a simplified model (pp. 57–60)
- Simplified model: estimate only $k$, prior $k\sim\text{normal}^+(0,1)$, true $k=1$; fix $m=1$, $q_*=(0,0)$, $q_0=(1,0)$, $p_0=(0,1)$. One parameter allows quadrature, but MCMC is used to understand what frustrates the sampler (p. 57).
- 8 chains, 500 warmup and 500 sampling iterations. Run times range from about 2 s to about 2000 s. Some R̂ values are large (the authors are comfortable with R̂ < 1.01; R̂ > 2 indicates poor mixing) (p. 57).
- Trace plots (Figure 32): chains stick at different local modes, some with much lower log posterior. Posterior predictive checks for those chains disagree with the observations. The chains with the lowest log posterior and highest $k$ are the slowest (p. 57).
- Plotting warmup iterations (not Stan's default) shows that each chain's mode is determined by its initial value, suggesting the modes strongly attract the chain. The default plot need not be the right plot (pp. 57–58).
- **Are the modes a real phenomenon or an artifact?** The log likelihood (quadrature, Figure 33) shows a dominating mode near $k=1$ and local modes as $k$ grows. As printed (p. 58),
$$
\log p(q_{\text{obs}}\mid k)=C-\frac{1}{2\sigma}\,\lVert q_{\text{obs}}-q(k)\rVert_2^2 ,
$$
with $C$ not depending on $k$ (see Reading notes for the factor).
- Larger $k$ means stronger gravity, a closer and shorter orbit. For $k<1$ the trajectory can drift arbitrarily far from the observed ellipse. For $k>1$ the simulated ellipse lies inside the observed one, which bounds the distance. As $k$ changes and the ellipse rotates, some simulated and observed positions become relatively close by chance, producing wiggles in the tail of the likelihood (Figure 34). These parameter values do not fit well but do better than their neighbors, which is enough for a bump (p. 58).
- The authors conclude that the tail modes are a mathematical artifact of the periodic structure of the data, not a latent phenomenon of interest, and contribute negligible mass. Chains that do not focus on the dominating mode waste computation (p. 58).
- **Options considered** (p. 60):
  - *Stronger priors.* Here they would reduce density at the mode but the wiggles in the tail of the joint would persist. With more data the wiggles become stronger ("the model is fundamentally multi-modal"). The current prior is already inconsistent with the minor-mode values. A hard constraint on orbital time or velocity could in principle remove the modes.
  - *Reweighting draws per chain (e.g. stacking).* Likely gives reasonable estimates, but (i) 8 chains will not explore all modes, so stacking amounts to discarding chains stuck at local modes, and (ii) chains in minor modes run up to about 1000 times longer.
  - *Tuning starting points.* Stan's default draws $\log k^{(0)}\sim\text{uniform}(-2,2)$, designed for unconstrained unit-scale parameters, and allows values of $k$ widely inconsistent with prior and domain knowledge. In a non-asymptotic regime the chain does not always forget its start, and probably will not here. Starting from $k^{(0)}$ drawn from the prior makes chains converge quickly to the relevant region.
- Ignoring non-converging chains is generally poor practice. This case differs because all chains were examined with posterior predictive checks, the origin of the modes was worked out, and they were shown not to describe interesting data-generating processes nor to carry more than negligible mass. Only then is computation redirected (p. 60).

> **Intuition note.** An orbit is periodic, so a wrong $k$ can put some simulated points near the observed ones just by chance. That creates small bumps in the likelihood that trap a chain, even though those $k$ values do not describe the data well.

### 11.3. Bad Markov chain, slow Markov chain? (pp. 60–61)
- The slowest chains have the lowest log posteriors (the folk theorem, Sec. 5.1). Hamilton's equations get harder to solve as $k$ grows: the planet moves faster, so each time step $dt$ changes $q(t)$ more and the integrator's step size must be adjusted (pp. 60–61).
- Lesson: an easy deterministic problem can become hard in a Bayesian analysis, because inference solves it over a range of parameter values. In the authors' experience with ODE models in pharmacology and epidemiology, a costlier stiff solver is sometimes needed for difficult ODEs during warmup (p. 61).
- Slow computation can also signal absurd parameter values, so better priors or initial points are needed (p. 61).
- This conflicts with the "fail fast" principle (Sec. 3.4): current tools are slower when the fit is bad. Flagging problems quickly is an important research topic (p. 61).

### 11.4. Building up the model (p. 61)
- Starting from the simplified model, the authors rebuild the full model. Most inference problems trace back to the interaction between the likelihood and cyclical observations (p. 61).
- Example: when $q_*$ is estimated, chains converge to many values, some agreeing with the observations and some not. There is no obvious link between starting points and the neighborhood of convergence. The full model has 7 parameters, some with strong posterior correlations, so this is hard to examine (p. 61).
- Physics reasoning: changing $q_*$ (hence $r$) is like changing $k$, since both control the gravitational interaction in $dp/dt=-(k/r^3)(q-q_*)$ (p. 61).
- Quadrature over 7 parameters is impossible, so the authors look at the conditional likelihood, varying only $q_*$ with $k,q_0,p_0$ fixed (Figure 35). It shows the suspected modes. With some confidence they then construct starting points that guide chains to the dominating mode, and the complete model fits well (pp. 61–62).

### 11.5. General lessons (p. 62)
- Examining a simplified model can reveal what frustrates the algorithm, though a manageable simplification that keeps the pathology is hard to find. Fixing some parameters is a straightforward way to simplify (pp. 61–62).
- Multimodality prevents cohesive exploration and leads to biased Monte Carlo estimates. Posterior predictive checks show how modes arise and what mass they carry. Minor modes with negligible mass can "trap" a chain, so one should always run multiple chains, perhaps more than the current default of 4 (p. 62).
- Starting points matter in non-asymptotic regimes. There is no universal default initial point, just as there is no universal default prior. Modelers often need to depart from defaults to get a numerically stable evaluation of the density; at the same time the authors want dispersed starts for reliable diagnostics and to potentially explore all relevant modes. Choosing starts can be iterative (p. 62).
- The authors do not advocate mindlessly discarding misbehaving chains. Their adjustment rests on (a) the defaults being inconsistent with expertise and (b) the demonstrated artifactual nature of the modes (p. 62).

### 12.1. Three perspectives on modeling and prediction (p. 63)
- **Traditional statistics:** the model is chosen ahead of time and the goal is to summarize the posterior accurately. Compute until approximate convergence (p. 63).
- **Machine learning:** the goal is usually prediction, and computation can stop when cross-validated accuracy plateaus (p. 63).
- **Model exploration:** applied work spends much effort trying many models, many with terrible fit, predictive performance and convergence (p. 63).
- Goals differ. In traditional statistics the approximation may be in the choice of model rather than the computation. In exploration, cycling through many models makes approximate computation attractive, provided the approximation is faithful enough to reproduce the salient posterior features (p. 63).
- The distinction is not inference vs prediction or exploratory vs confirmatory. It is how much we trust a model and allow computation to approximate (p. 63).
- Problems often seem obvious in hindsight, but the workflow was needed to find them. Challenges arise in the context of the data at hand, which is why applied subfields advance from application to application (p. 63).

### 12.2. Justification of iterative model building (p. 64)
- The authors describe steps in data science so far: data summarization (up to about 1900), modeling (from Gauss and Laplace), and the current step, computation. They view "model navigation" as the next transformative step (pp. 63–64).
- Humans learn gradually, and it can be efficient to start simple and stop when the model is good enough. One workflow goal is to ease the process for humans even if exact computation were automatic (p. 64).
- Computationally, asymptotic guarantees can fail in finite time, and no fully automated computation gives perfect results across the range of models practitioners care about. Simpler versions make challenges easier to understand, so correct implementation tends to need iteration (p. 64).
- Complexity makes it hard to separate computation, modeling, data quality and code bugs. Iterative building lets one apply software-engineering practice: check simple components before adding complicated ones (p. 64).

### 12.3. Model selection and overfitting (pp. 64–66)
- **The concern:** improvement is conditioned on discrepancy between model and data, so aspects of the data are used more than once ("double dipping"). It can in principle threaten frequency properties and relates to the garden of forking paths (Gelman and Loken). The authors do not advocate picking the best fit from a set, but building up to a more complex model with each decision understood and justified (p. 64).
- If M1 fails a check and we move to M2, then had the data been different we would have been satisfied with M1. Checking and improvement are necessary but are an aspect of fitting not captured in likelihood or prior. This is post-selection inference, and Bayesian inferences are subject to it too (p. 65).
- **Example (Economist election model):** a first model gave Biden a 99% chance of winning the national vote, which seemed too high. Refactoring found bugs and places to improve, including higher between-state correlations, and lowered the figure to 98% (p. 65).
- Without noticing that implausible prediction, the authors might never have checked. This data dependence undermines a fully Bayesian reading of the final model's probabilities. Model averaging would not solve it, since one would not average the final model with its buggy predecessor, and a better future model does not exist yet (p. 65).
- **Their stance:** the authors think the workflow will avoid "the worst problems" of overfitting, because it does not search for optimally fitting models or make hard selections. The main message from the post-selection literature is that the final model should include as much information as possible. When many models are possible, embed them in a larger model, do predictive model averaging, or use all models simultaneously (Sec. 8). They expect this to work better than formally modeling the checking process (p. 65).
- They believe the workflow enables severe tests of assumptions (Mayo, 2018). A model whose assumptions withstood such tests is, they claim, often more trustworthy than a preregistered model that was never tested, despite its data-dependent route (pp. 65–66).
- Iterative building is also fully justified for understanding a fixed complex model, since components interact in complex ways (e.g. spatial effects and linear covariate effects, Hodges and Reich) (p. 66).

> **Intuition note.** Looking at the data to decide how to fix a model means the final model depends on the data in a way the posterior does not show. The authors do not claim to remove this. They argue that building one richer model, not choosing the best of many, limits the harm.

### 12.4. Bigger datasets demand bigger models (p. 66)
- Hierarchical Bayesian modeling, deep learning and regularization let researchers fit larger models, with information aggregation and partial pooling (p. 66).
- "Big data" here means too big for memory, or too big for usual algorithms to run in reasonable time; it is relative to computing capacity and goals (p. 66).
- **Assumption the authors reject:** that big data remove the need for careful modeling. Big data are messy: they favor availability over randomization, are mostly observational, and often use proxies. Inference needs extrapolation from sample to population, control to treatment, and measurements to latent variables, all requiring assumptions. Example: fit a multilevel model, then poststratify to the general population (p. 66).
- Adjusting for more factors should help but hits technical barriers. Effective modeling needs (a) regularization and (b) modeling of latent variables, missingness and measurement error. A model "emerges from engagement with the application and the available data" (p. 66).

### 12.5. Prediction, generalization, and poststratification (p. 67)
- Three core tasks: generalizing from sample to population, from control to treatment, and from observed data to underlying constructs. Related terms: "domain adaptation" and "transportability" (pp. 66–67).
- Tools include weighting and poststratification, matching and regression, and latent variable models. Bayesian methods contribute hierarchical modeling or partial pooling, regularization for large nonparametric models, and multilevel latent variable models (p. 67).
- Workflow does not stop at inference for the fitted model. The prior and data model sit inside a larger framework including predictions for new settings, and models may go into production, giving feedback (p. 67).
- The model should be understood in light of its use. Example: incentive-effect models for surveys have different relevant aspects for small incentives in mail surveys vs large incentives in telephone surveys. Rubin (1983): choice of transformation can matter little for the median but a lot for the mean (p. 67).

### 12.6. Going forward (pp. 67–68)
- **Holes in the workflow** (p. 67): a wrong model can pass a predictive check silently; an incorrect computation program can satisfy simulation-based calibration diagnostics if the posterior stays in the prior; cross-validation consistency relies on conditional independence and stationarity of covariates; causal inference always has untestable assumptions. Statistics relies on extrapolation, so one often needs new data and experiment design.
- Not covered: design, measurement and data collection; decision making and communication; computing environments and social aspects of collaboration (pp. 67–68).
- The list of steps is too long to be a useful guide. Plan: (1) abstract principles from best practice (this paper), (2) apply them in case studies, (3) implement as much as possible in software. Automating what can be automated should let analysts integrate data with domain knowledge (p. 68).
- The paper is a review and survey, a first step to put the activities "under a single roof". Worked examples with code are needed, and a book on Bayesian workflow with Stan is in preparation (p. 68).

### References (pp. 68–77)
Reference list only; not digested.

## Toy example (ours, not from the text)
**Goal:** show why the extra $\sigma_y^2$ loosens the grip of very large bins. We use the observed proportion as a stand-in for the model's $p_j$ (a simplification of ours). Data are from the table on p. 54; $\sigma_y=0.003$ is the reported estimate.

Bin 1: $n=45198$, $y=45183$, so $y/n=0.99967\approx 0.9997$.
- Binomial variance: $0.99967\times0.000332/45198\approx7.34\times10^{-9}$ (here $1-y/n=15/45198\approx0.000332$). SD $\approx 8.6\times10^{-5}$.
- With the fudge term: variance $=9\times10^{-6}+7.34\times10^{-9}\approx9.007\times10^{-6}$, SD $\approx 3.0\times10^{-3}$.
- The allowed SD grows by about $3.0\times10^{-3}/8.6\times10^{-5}\approx 35$.

Bin 5: $n=73855$, $y=64740$, so $y/n\approx0.8766$.
- Binomial variance: $0.8766\times0.1234/73855=0.10817/73855\approx1.46\times10^{-6}$. SD $\approx1.21\times10^{-3}$.
- With the fudge term: variance $=9\times10^{-6}+1.46\times10^{-6}=1.046\times10^{-5}$, SD $\approx3.23\times10^{-3}$. The ratio is only about $2.7$.

**Reading:** a miss of 0.003 in bin 1 is about $0.003/8.6\times10^{-5}\approx 35$ binomial SDs but only about 1 SD with the fudge term. So the first bins no longer dominate the fit.

## Concepts
- [[bayesian-workflow]] — iterative cycle of building, checking and expanding models; here argued to be "model navigation" (pp. 63–64)
- [[model-expansion]] (new) — adding parameters or terms, even without scientific meaning, so that bigger data can be fit (p. 55)
- [[fudge-factor-error-term]] (new) — independent extra variance $\sigma_y^2$ added to each binned observation to allow misspecification (p. 54)
- [[likelihood]] — here, a binomial likelihood with huge counts can be "too strong" and make the fit sticky (p. 55)
- [[folk-theorem-statistical-computing]] (new) — computational problems often signal modeling problems; slow or bad chains hint at a bad model (pp. 53, 60)
- [[convergence-diagnostics]] — R̂, trace plots including warmup; R̂ < 1.01 desired, R̂ > 2 means poor mixing (p. 57)
- [[multimodal-posterior]] (new) — several local modes; here artifacts of periodic data with negligible mass (pp. 58, 60)
- [[markov-chain-monte-carlo]] — chains may not forget starting points in finite time, so starts are a tuning choice (pp. 60, 62)
- [[stacking]] (new) — reweighting chain draws; treated as discarding chains stuck at local modes (p. 60)
- [[posterior-predictive-check]] — used chain by chain to see that minor modes do not fit the data (pp. 57, 62)
- [[post-selection-inference]] (new) — inference is affected when model choice depends on the data; also a concern for Bayesian inference (p. 65)
- [[garden-of-forking-paths]] (new) — different models would have been fit had the data been different (p. 64)
- [[partial-pooling]] — generalizing across similar but not identical settings via hierarchical modeling (p. 67)
- [[poststratification]] (new) — connecting model predictions to a population of interest, e.g. after a multilevel model (pp. 66–67)

## Canonical instances
- [[golf-putting]] — geometric model with angle and distance terms, expanded by an error term for large binned data (pp. 52–55)
- [[planetary-motion]] — ODE model with multimodal posterior, simplified to one parameter to understand local modes (pp. 56–62)
- [[economist-election-forecast]] — a 99% prediction prompted a model refactor and a drop to 98% (p. 65)

## Bridges (candidates)
- [structural-analogy] Local modes from periodic data ↔ optimization: local optima that trap gradient methods by starting point — both depend on initialization.
- [structural-analogy] Extra variance $\sigma_y^2$ on binned proportions ↔ random effects/overdispersion in multilevel models — absorbs unexplained variation. The text itself compares it to a saturated interaction term in ANOVA (p. 55).
- [structural-analogy] Post-selection inference (Sec. 12.3) ↔ frequentist selective inference: both address data-dependent model choice.
- [metaphor] "Approximate aliasing" in the likelihood (Fig. 33 caption, p. 59) ↔ signal processing: periodic sampling makes distinct frequencies look alike.

## Questions this raises
- How can one detect early that a bad chain comes from an artifact rather than a real mode, without a simplified model you can solve by quadrature?
- Which model changes are so data-dependent that they invalidate the posterior's probability statements, and can this be quantified?
- Can "fail fast" tools, which flag bad parameter regions before expensive ODE solves, be built into samplers?
- How much does the choice of dispersed vs prior-based initial points change convergence diagnostics?

## Reading notes
- This part starts at p. 52 with the Figure 28 caption and the end of a section whose heading is not on these pages (presumably §10.3, since §10.4 follows) and ends with the reference list on p. 77. §§10.4–12 are digested. References (pp. 68–77) are not summarized. Split at a section boundary.
- Printed page = pdf page (offset 0).
- p. 58: the log-likelihood is printed with $\frac{1}{2\sigma}$. For the stated error model $\sigma^2 I$ one would expect $\frac{1}{2\sigma^2}$. This is a likely misprint; I reproduced the source as printed.
- p. 52: "reach the whole" is a typo for "hole". The caption of Figure 30 is awkwardly worded ("expanded… that had showed poor convergence"); it refers to the two-parameter model.
- Figure 34: the caption refers to $k=2.2$ while the legend shows $k=2.16$.
- p. 67: the sentence about predictive checks passing "silently for overfitting all output at the observed values" is awkwardly worded. I paraphrased it only as "a wrong model can pass a predictive check silently".
- Equations in this part are unnumbered.
- Sections 2.4, 3.4, 5.1, 5.4, 6.1, 6.3, 7.4, 8 and 8.1 are cited but not in these pages.

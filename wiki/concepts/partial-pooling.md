---
id: partial-pooling
type: concept
fields: [bayesian, analytic-philosophy, llm]
fields_strong: [bayesian, analytic-philosophy, llm]
n_sources: 29
n_works: 8
tiers: [core, reference, deep]
grounding: digests
sources: [efron-1986-bayesian/main, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch15-hierarchical, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch20-basis, gelman-2013-philosophy/main, gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p3, hernan-2020-whatif/ch04-effect, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch07-interactions, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, mcelreath-2020-rethinking/ch14-missing, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch13-cold, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian]
aliases: [partial-pooling-shrinkage]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# partial-pooling

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `partial-pooling-shrinkage` — 23 digest(s)

## Canon spine entry

- **Partial pooling / shrinkage** (bayesian): group estimates are pulled toward the overall mean in proportion to how noisy they are (UG)

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 4): James–Stein estimation, cited as an idea that fails the objectivity test and, via its Bayesian explanation, as a hopeful prototype [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/appc-computation]] (p. 596): a half-Cauchy prior on τ gives a lower posterior mean and median of τ and greater shrinkage of θ_j than the near-uniform prior
- [[gelman-2013-bda3/ch02-single]] (pp. 45, 48–49): gamma prior pulls small-county raw rates toward the prior mean [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 96): hierarchical models shrink $\theta_j$ estimates together, handling multiple comparisons [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch05-hierarchical]] (pp. 115–116, 112–113): estimates are weighted combinations of group and overall means, shrunk more for noisier groups [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch07-evaluating]] (pp. 179, 186): hierarchical model sits between no pooling and complete pooling; shrinks comparisons toward 0 [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch08-modeling]] (p. 209): stratum estimates pulled toward the grand mean [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch13-modal]] (p. 328): shrinkage factors $\frac{\sigma^2/n_j}{\sigma^2/n_j+\tau^2}$ near zero imply little pooling here [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch14-introduction]] (p. 369): lasso posterior is partially pooled toward zero [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 381–382, 388): compromise between no pooling ($\sigma_\beta=\infty$) and complete pooling ($\sigma_\beta=0$)
- [[gelman-2013-bda3/ch16-generalized]] (p. 418): the weak prior shrinks the bioassay slope from 10.2 to 5.4 [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch17-models]] (p. 435–436): shrinkage of school estimates, whose amount depends on the prior's tails [alias `partial-pooling-shrinkage`]
- [[gelman-2013-bda3/ch20-basis]] (pp. 490, 493–494): here, the posterior mean curve is shrunk toward a prior-centred parametric curve, and coefficients are shrunk toward zero [alias `partial-pooling-shrinkage`]
- [[gelman-2013-philosophy/main]] (p. 8): mentioned as what the hierarchical models allow, including for small states [alias `partial-pooling-shrinkage`; work fields: bayesian, analytic-philosophy]
- [[gelman-2020-workflow/main-p1]] (p. 9): pooling of group estimates, said to work better on scale-free parameters [alias `partial-pooling-shrinkage`]
- [[gelman-2020-workflow/main-p3]] (p. 67): generalizing across similar but not identical settings via hierarchical modeling
- [[hernan-2020-whatif/ch04-effect]] (p. 57): here only pooled stratum-specific estimates (Mantel-Haenszel etc.) to reduce variance if there is no modification [alias `partial-pooling-shrinkage`]
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (p. 188, preview): multilevel models as adaptive regularization [alias `partial-pooling-shrinkage`]
- [[mcelreath-2020-rethinking/ch07-interactions]] (p. 214): the author mentions borrowing information across categories in multilevel models as a reason not to split data
- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 362): cluster estimates are pulled toward the population mean; more for small or extreme clusters [alias `partial-pooling-shrinkage`]
- [[mcelreath-2020-rethinking/ch13-adventures]] (pp. 396–397): estimates pulled toward the population center; in 2-D the pull follows the intercept–slope correlation [alias `partial-pooling-shrinkage`]
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 428): less certain estimates move more toward the regression via pooling [alias `partial-pooling-shrinkage`]
- [[mcgrayne-2011-theory/ch03-many]] (p. 44): Credibility's pull toward the class mean, later explained by Stein [alias `partial-pooling-shrinkage`]
- [[mcgrayne-2011-theory/ch10-46]] (pp. 130–131): pulling related group estimates toward a common mean; Stein's "shrinkage" [alias `partial-pooling-shrinkage`]
- [[mcgrayne-2011-theory/ch13-cold]] (pp. 170–171): Tukey's "borrowing strength": using similar units to inform sparse ones (pp. 170–171); the source does not use the statistical term [alias `partial-pooling-shrinkage`]
- [[murphy-2023-pml2/ch03-statistics-p2]] (pp. 110, 112): group estimates pulled to the population mean; weight $w_j=\sigma_j^2/(\sigma_j^2+\tau^2)$ [alias `partial-pooling-shrinkage`]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 116): posterior mean $\hat\theta_j=\lambda\mu+(1-\lambda)y_j$ with $\lambda=\sigma^2/(\sigma^2+\tau^2)$ [alias `partial-pooling-shrinkage`]
- [[murphy-2023-pml2/ch15-generalized]] (p. 625): compromise between separate and pooled fits
- [[murphy-2023-pml2/ch17-bayesian]] (p. 679): per-layer $\sigma^0_l$ controls shrinkage towards the shared weights [work fields: bayesian, llm]

## Instances that use it

- [[simulated-ponds]] — simulated data with known truth showing partial pooling beats no pooling — from [[mcelreath-2020-rethinking/ch12-multilevel]]

## Candidate bridges

- [structural-analogy] $\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))$ ↔ hierarchical models: within-group vs. between-group variation, which is the information partial pooling uses. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → bayesian)
- [structural-analogy] Precision-weighted posterior mean $\mu_n$ (3.8, 3.12) ↔ partial pooling/shrinkage: an estimate pulled from the data mean toward a prior mean in proportion to relative precision. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → bayesian)
- [structural-analogy] Posterior mean shrinks toward the population mean in the mother–daughter example ↔ partial pooling in hierarchical models: both weight own data against the population distribution. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → bayesian)
- [structural-analogy] Partial pooling toward a mean ↔ ensemble or regularized estimators: both trade group-specific fit for stability. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other:ensemble-or-regularized-estimators)
- [structural-analogy] Stratum-level shrinkage in the CBS poll ↔ Bayesian inference: partial pooling in the Ch. 5 hierarchical models. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [same-math] Normal–normal update (9.7) ↔ hierarchical models: precision-weighted average, as in partial pooling/shrinkage — the same weighted average of a group-level mean and noisy data. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → bayesian)
- [structural-analogy] Partial pooling ↔ shrinkage in group-level estimates: noisier groups are pulled more toward the mean (same logic as in Ch. 5). — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → other:shrinkage-in-group-level)
- [structural-analogy] borrowing strength across surveys ↔ partial pooling/shrinkage: unasked questions in one survey are imputed using other surveys. — from [[gelman-2013-bda3/ch18-models]] (bayesian → bayesian)
- [structural-analogy] Shrinkage of basis coefficients ↔ Bayesian partial pooling: coefficients are pulled toward a common centre by a prior scale learned from data. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → bayesian)
- [structural-analogy] Posterior mean (23.2), weight $\alpha/(\alpha+n)$ on $P_0$ ↔ partial pooling/shrinkage: estimate pulled to a prior guess with strength decreasing in $n$. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → bayesian)
- [structural-analogy] borrowing strength via covariates in the prior ↔ hierarchical/multilevel regression partial pooling — information is shared among similar units (p. 246) — from [[grimmer-2022-textasdata/ch13-topic]] (political-science → unspecified)
- [structural-analogy] Pooling stratum-specific effects with variance-reducing weights ↔ bayesian: partial pooling/shrinkage in hierarchical models — both combine group estimates to reduce noise, but the text uses fixed-weight averages, not a prior. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [metaphor] Adjusted estimator with too many strata ↔ Bayesian: partial pooling/shrinkage — the problem of sparse strata is what pooling addresses, but the chapter does not discuss it. — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Smoothing as borrowing information across values of $A$ ↔ bayesian: partial pooling/shrinkage, which also borrows information across units. The mechanisms differ. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Parametric smoothing over zero cells (random nonpositivity) ↔ partial pooling/shrinkage: sparse strata borrow strength from the model. — from [[hernan-2020-whatif/ch12-ip]] (bayesian → bayesian)
- [structural-analogy] Rule of succession as weighted average of $r/n$ and prior mean $1/2$ with prior weight 2 (6.46) ↔ bayesian: partial pooling / shrinkage toward a prior mean. — from [[jaynes-2003-probability/ch06-elementary-p1]] (bayesian → bayesian)
- [structural-analogy] B's use of other intervals to estimate $s$, which then sharpens each $n_k$ ↔ bayesian: partial pooling in hierarchical models — from [[jaynes-2003-probability/ch06-elementary-p2]] (bayesian → bayesian)
- [structural-analogy] Galton's reversion vs. spreading balance ↔ Bayesian: partial pooling/shrinkage toward the population mean — both pull individuals to the mean while the population keeps a fixed spread. — from [[jaynes-2003-probability/ch07-central-p2]] (bayesian → bayesian)
- [structural-analogy] Systematic error $S$ in (8.56) ↔ bayesian: shared hierarchical level (common effect) limiting how much partial pooling can reduce uncertainty. — from [[jaynes-2003-probability/ch08-sufficiency]] (bayesian → bayesian)
- [structural-analogy] Galton's regression to the mean / shrinkage ↔ bayesian: partial pooling, where noisy estimates are pulled toward a common mean (p. 92 links it to multilevel models) — from [[mcelreath-2020-rethinking/ch04-linear-p2]] (bayesian → bayesian)
- [structural-analogy] Partial pooling ↔ bias–variance trade-off in estimation: the pooled estimate adds bias but cuts variance, most for noisy small clusters. — from [[mcelreath-2020-rethinking/ch12-multilevel]] (bayesian → other:bias-variance-trade-off)
- [structural-analogy] Credibility's blend of class data and own data ↔ hierarchical modelling: partial pooling of group estimates — both pull noisy local estimates toward a wider mean — from [[mcgrayne-2011-theory/ch03-many]] (bayesian → bayesian)
- [structural-analogy] Credibility weighting of old rates and new claims ↔ bayesian: partial pooling/shrinkage, estimates pulled toward the prior in proportion to data noise. The text does not state this link. — from [[mcgrayne-2011-theory/ch06-arthur]] (bayesian → bayesian)
- [structural-analogy] Credibility/Stein–James formula ↔ bayesian: partial pooling in hierarchical models — both pull related estimates toward a mean. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] "Borrowing strength" across similar counties ↔ bayesian: partial pooling in hierarchical models — both pull sparse units toward information from related units. — from [[mcgrayne-2011-theory/ch13-cold]] (bayesian → bayesian)
- [structural-analogy] Expert prior plus sparse failure data ↔ hierarchical modelling and partial pooling: borrowing strength from outside information when data are thin. — from [[mcgrayne-2011-theory/ch14-three]] (bayesian → bayesian)
- [same-math] Hierarchical BNN with non-centered weights (17.57) ↔ hierarchical GLMs / partial pooling: the same parent-plus-offset structure with scale $\sigma^0_l$. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → bayesian)
- [structural-analogy] Hierarchical Bayesian DG and meta-learning models (Figs. 19.13, 19.15) ↔ Hierarchical models / partial pooling: task parameters drawn from a shared population level. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
- [structural-analogy] Local-level shrinkage of noisy observations ↔ partial pooling: estimate balances prior dynamics and data. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → bayesian)
- [structural-analogy] Slope $E[X|Y=y]=0.5y$ below 1 (§1.3.10) ↔ shrinkage/partial pooling: the prediction is pulled toward the mean because the predictor is noisy as a signal of $X$. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → bayesian)
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → bayesian)
- [structural-analogy] Top level of an HBM supplying the hypothesis space for the level below ↔ bayesian: hierarchical models and partial pooling — higher-level parameters shared across groups are informed by all groups. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)

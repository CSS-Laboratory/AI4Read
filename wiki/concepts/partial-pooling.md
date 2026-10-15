---
id: partial-pooling
type: concept
fields: [bayesian]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch15-hierarchical, gelman-2020-workflow/main-p3, mcelreath-2020-rethinking/ch07-interactions, murphy-2023-pml2/ch15-generalized, murphy-2023-pml2/ch17-bayesian]
generated_by: build_kg.py
---

# partial-pooling

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appc-computation]] (p. 596): a half-Cauchy prior on τ gives a lower posterior mean and median of τ and greater shrinkage of θ_j than the near-uniform prior
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 381–382, 388): compromise between no pooling ($\sigma_\beta=\infty$) and complete pooling ($\sigma_\beta=0$)
- [[gelman-2020-workflow/main-p3]] (p. 67): generalizing across similar but not identical settings via hierarchical modeling
- [[mcelreath-2020-rethinking/ch07-interactions]] (p. 214): the author mentions borrowing information across categories in multilevel models as a reason not to split data
- [[murphy-2023-pml2/ch15-generalized]] (p. 625): compromise between separate and pooled fits
- [[murphy-2023-pml2/ch17-bayesian]] (p. 679): per-layer $\sigma^0_l$ controls shrinkage towards the shared weights

## Instances that use it

- [[simulated-ponds]] — simulated data with known truth showing partial pooling beats no pooling — from [[mcelreath-2020-rethinking/ch12-multilevel]]

## Candidate bridges

- [structural-analogy] $\operatorname{var}(u)=E(\operatorname{var}(u|v))+\operatorname{var}(E(u|v))$ ↔ hierarchical models: within-group vs. between-group variation, which is the information partial pooling uses. — from [[gelman-2013-bda3/ch01-probability]] (bayesian → other)
- [structural-analogy] Precision-weighted posterior mean $\mu_n$ (3.8, 3.12) ↔ partial pooling/shrinkage: an estimate pulled from the data mean toward a prior mean in proportion to relative precision. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → other)
- [structural-analogy] Posterior mean shrinks toward the population mean in the mother–daughter example ↔ partial pooling in hierarchical models: both weight own data against the population distribution. — from [[gelman-2013-bda3/ch04-asymptotics]] (bayesian → other)
- [structural-analogy] Partial pooling toward a mean ↔ ensemble or regularized estimators: both trade group-specific fit for stability. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other)
- [structural-analogy] Stratum-level shrinkage in the CBS poll ↔ Bayesian inference: partial pooling in the Ch. 5 hierarchical models. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [same-math] Normal–normal update (9.7) ↔ hierarchical models: precision-weighted average, as in partial pooling/shrinkage — the same weighted average of a group-level mean and noisy data. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Partial pooling ↔ shrinkage in group-level estimates: noisier groups are pulled more toward the mean (same logic as in Ch. 5). — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → other)
- [structural-analogy] borrowing strength across surveys ↔ partial pooling/shrinkage: unasked questions in one survey are imputed using other surveys. — from [[gelman-2013-bda3/ch18-models]] (bayesian → other)
- [structural-analogy] Shrinkage of basis coefficients ↔ Bayesian partial pooling: coefficients are pulled toward a common centre by a prior scale learned from data. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → bayesian)
- [structural-analogy] Posterior mean (23.2), weight $\alpha/(\alpha+n)$ on $P_0$ ↔ partial pooling/shrinkage: estimate pulled to a prior guess with strength decreasing in $n$. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → other)
- [structural-analogy] borrowing strength via covariates in the prior ↔ hierarchical/multilevel regression partial pooling — information is shared among similar units (p. 246) — from [[grimmer-2022-textasdata/ch13-topic]] (political-science → unspecified)
- [structural-analogy] Pooling stratum-specific effects with variance-reducing weights ↔ bayesian: partial pooling/shrinkage in hierarchical models — both combine group estimates to reduce noise, but the text uses fixed-weight averages, not a prior. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [metaphor] Adjusted estimator with too many strata ↔ Bayesian: partial pooling/shrinkage — the problem of sparse strata is what pooling addresses, but the chapter does not discuss it. — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Smoothing as borrowing information across values of $A$ ↔ bayesian: partial pooling/shrinkage, which also borrows information across units. The mechanisms differ. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Parametric smoothing over zero cells (random nonpositivity) ↔ partial pooling/shrinkage: sparse strata borrow strength from the model. — from [[hernan-2020-whatif/ch12-ip]] (bayesian → other)
- [structural-analogy] Rule of succession as weighted average of $r/n$ and prior mean $1/2$ with prior weight 2 (6.46) ↔ bayesian: partial pooling / shrinkage toward a prior mean. — from [[jaynes-2003-probability/ch06-elementary-p1]] (information-theory → bayesian)
- [structural-analogy] B's use of other intervals to estimate $s$, which then sharpens each $n_k$ ↔ bayesian: partial pooling in hierarchical models — from [[jaynes-2003-probability/ch06-elementary-p2]] (information-theory → bayesian)
- [structural-analogy] Galton's reversion vs. spreading balance ↔ Bayesian: partial pooling/shrinkage toward the population mean — both pull individuals to the mean while the population keeps a fixed spread. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → bayesian)
- [structural-analogy] Systematic error $S$ in (8.56) ↔ bayesian: shared hierarchical level (common effect) limiting how much partial pooling can reduce uncertainty. — from [[jaynes-2003-probability/ch08-sufficiency]] (information-theory → bayesian)
- [structural-analogy] Galton's regression to the mean / shrinkage ↔ bayesian: partial pooling, where noisy estimates are pulled toward a common mean (p. 92 links it to multilevel models) — from [[mcelreath-2020-rethinking/ch04-linear-p2]] (bayesian → bayesian)
- [structural-analogy] Partial pooling ↔ bias–variance trade-off in estimation: the pooled estimate adds bias but cuts variance, most for noisy small clusters. — from [[mcelreath-2020-rethinking/ch12-multilevel]] (bayesian → other)
- [structural-analogy] Credibility's blend of class data and own data ↔ hierarchical modelling: partial pooling of group estimates — both pull noisy local estimates toward a wider mean — from [[mcgrayne-2011-theory/ch03-many]] (bayesian → other)
- [structural-analogy] Credibility weighting of old rates and new claims ↔ bayesian: partial pooling/shrinkage, estimates pulled toward the prior in proportion to data noise. The text does not state this link. — from [[mcgrayne-2011-theory/ch06-arthur]] (bayesian → bayesian)
- [structural-analogy] Credibility/Stein–James formula ↔ bayesian: partial pooling in hierarchical models — both pull related estimates toward a mean. — from [[mcgrayne-2011-theory/ch10-46]] (bayesian → bayesian)
- [structural-analogy] "Borrowing strength" across similar counties ↔ bayesian: partial pooling in hierarchical models — both pull sparse units toward information from related units. — from [[mcgrayne-2011-theory/ch13-cold]] (bayesian → bayesian)
- [structural-analogy] Expert prior plus sparse failure data ↔ hierarchical modelling and partial pooling: borrowing strength from outside information when data are thin. — from [[mcgrayne-2011-theory/ch14-three]] (bayesian → other)
- [same-math] Hierarchical BNN with non-centered weights (17.57) ↔ hierarchical GLMs / partial pooling: the same parent-plus-offset structure with scale $\sigma^0_l$. — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → other)
- [structural-analogy] Hierarchical Bayesian DG and meta-learning models (Figs. 19.13, 19.15) ↔ Hierarchical models / partial pooling: task parameters drawn from a shared population level. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] Local-level shrinkage of noisy observations ↔ partial pooling: estimate balances prior dynamics and data. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → other)
- [structural-analogy] Slope $E[X|Y=y]=0.5y$ below 1 (§1.3.10) ↔ shrinkage/partial pooling: the prediction is pulled toward the mean because the predictor is noisy as a signal of $X$. — from [[pearl-2016-primer/ch01-preliminaries]] (bayesian → other)
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → other)
- [structural-analogy] Top level of an HBM supplying the hypothesis space for the level below ↔ bayesian: hierarchical models and partial pooling — higher-level parameters shared across groups are informed by all groups. — from [[tenenbaum-2011-grow/main]] (bayesian → bayesian)

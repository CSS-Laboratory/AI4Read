---
id: partial-pooling-shrinkage
type: concept
fields: [bayesian]
n_sources: 23
tiers: [core, reference, deep]
grounding: digests
sources: [efron-1986-bayesian/main, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch07-evaluating, gelman-2013-bda3/ch08-modeling, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch14-introduction, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch20-basis, gelman-2013-philosophy/main, gelman-2020-workflow/main-p1, hernan-2020-whatif/ch04-effect, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch13-adventures, mcelreath-2020-rethinking/ch14-missing, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch13-cold, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch03-statistics-p3]
canon_spine: bayesian
generated_by: build_kg.py
---

# partial-pooling-shrinkage

## Canon spine entry

- **Partial pooling / shrinkage** (bayesian): group estimates are pulled toward the overall mean in proportion to how noisy they are (UG)

## Definitions in the sources

### bayesian

- [[efron-1986-bayesian/main]] (p. 4): James–Stein estimation, cited as an idea that fails the objectivity test and, via its Bayesian explanation, as a hopeful prototype
- [[gelman-2013-bda3/ch02-single]] (pp. 45, 48–49): gamma prior pulls small-county raw rates toward the prior mean
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 96): hierarchical models shrink $\theta_j$ estimates together, handling multiple comparisons
- [[gelman-2013-bda3/ch05-hierarchical]] (pp. 115–116, 112–113): estimates are weighted combinations of group and overall means, shrunk more for noisier groups
- [[gelman-2013-bda3/ch07-evaluating]] (pp. 179, 186): hierarchical model sits between no pooling and complete pooling; shrinks comparisons toward 0
- [[gelman-2013-bda3/ch08-modeling]] (p. 209): stratum estimates pulled toward the grand mean
- [[gelman-2013-bda3/ch13-modal]] (p. 328): shrinkage factors $\frac{\sigma^2/n_j}{\sigma^2/n_j+\tau^2}$ near zero imply little pooling here
- [[gelman-2013-bda3/ch14-introduction]] (p. 369): lasso posterior is partially pooled toward zero
- [[gelman-2013-bda3/ch16-generalized]] (p. 418): the weak prior shrinks the bioassay slope from 10.2 to 5.4
- [[gelman-2013-bda3/ch17-models]] (p. 435–436): shrinkage of school estimates, whose amount depends on the prior's tails
- [[gelman-2013-bda3/ch20-basis]] (pp. 490, 493–494): here, the posterior mean curve is shrunk toward a prior-centred parametric curve, and coefficients are shrunk toward zero
- [[gelman-2013-philosophy/main]] (p. 8): mentioned as what the hierarchical models allow, including for small states
- [[gelman-2020-workflow/main-p1]] (p. 9): pooling of group estimates, said to work better on scale-free parameters
- [[hernan-2020-whatif/ch04-effect]] (p. 57): here only pooled stratum-specific estimates (Mantel-Haenszel etc.) to reduce variance if there is no modification
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (p. 188, preview): multilevel models as adaptive regularization
- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 362): cluster estimates are pulled toward the population mean; more for small or extreme clusters
- [[mcelreath-2020-rethinking/ch13-adventures]] (pp. 396–397): estimates pulled toward the population center; in 2-D the pull follows the intercept–slope correlation
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 428): less certain estimates move more toward the regression via pooling
- [[mcgrayne-2011-theory/ch03-many]] (p. 44): Credibility's pull toward the class mean, later explained by Stein
- [[mcgrayne-2011-theory/ch10-46]] (pp. 130–131): pulling related group estimates toward a common mean; Stein's "shrinkage"
- [[mcgrayne-2011-theory/ch13-cold]] (pp. 170–171): Tukey's "borrowing strength": using similar units to inform sparse ones (pp. 170–171); the source does not use the statistical term
- [[murphy-2023-pml2/ch03-statistics-p2]] (pp. 110, 112): group estimates pulled to the population mean; weight $w_j=\sigma_j^2/(\sigma_j^2+\tau^2)$
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 116): posterior mean $\hat\theta_j=\lambda\mu+(1-\lambda)y_j$ with $\lambda=\sigma^2/(\sigma^2+\tau^2)$

## Candidate bridges

- [structural-analogy] Precision-weighted posterior mean $\mu_n$ (3.8, 3.12) ↔ partial pooling/shrinkage: an estimate pulled from the data mean toward a prior mean in proportion to relative precision. — from [[gelman-2013-bda3/ch03-introduction]] (bayesian → other)
- [same-math] Normal–normal update (9.7) ↔ hierarchical models: precision-weighted average, as in partial pooling/shrinkage — the same weighted average of a group-level mean and noisy data. — from [[gelman-2013-bda3/ch09-decision]] (bayesian → other)
- [structural-analogy] Partial pooling ↔ shrinkage in group-level estimates: noisier groups are pulled more toward the mean (same logic as in Ch. 5). — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → other)
- [structural-analogy] borrowing strength across surveys ↔ partial pooling/shrinkage: unasked questions in one survey are imputed using other surveys. — from [[gelman-2013-bda3/ch18-models]] (bayesian → other)
- [structural-analogy] Posterior mean (23.2), weight $\alpha/(\alpha+n)$ on $P_0$ ↔ partial pooling/shrinkage: estimate pulled to a prior guess with strength decreasing in $n$. — from [[gelman-2013-bda3/ch23-dirichlet]] (bayesian → other)
- [structural-analogy] Pooling stratum-specific effects with variance-reducing weights ↔ bayesian: partial pooling/shrinkage in hierarchical models — both combine group estimates to reduce noise, but the text uses fixed-weight averages, not a prior. — from [[hernan-2020-whatif/ch04-effect]] (bayesian → bayesian)
- [metaphor] Adjusted estimator with too many strata ↔ Bayesian: partial pooling/shrinkage — the problem of sparse strata is what pooling addresses, but the chapter does not discuss it. — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Smoothing as borrowing information across values of $A$ ↔ bayesian: partial pooling/shrinkage, which also borrows information across units. The mechanisms differ. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Parametric smoothing over zero cells (random nonpositivity) ↔ partial pooling/shrinkage: sparse strata borrow strength from the model. — from [[hernan-2020-whatif/ch12-ip]] (bayesian → other)
- [structural-analogy] Rule of succession as weighted average of $r/n$ and prior mean $1/2$ with prior weight 2 (6.46) ↔ bayesian: partial pooling / shrinkage toward a prior mean. — from [[jaynes-2003-probability/ch06-elementary-p1]] (information-theory → bayesian)
- [structural-analogy] Galton's reversion vs. spreading balance ↔ Bayesian: partial pooling/shrinkage toward the population mean — both pull individuals to the mean while the population keeps a fixed spread. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → bayesian)
- [structural-analogy] Credibility weighting of old rates and new claims ↔ bayesian: partial pooling/shrinkage, estimates pulled toward the prior in proportion to data noise. The text does not state this link. — from [[mcgrayne-2011-theory/ch06-arthur]] (bayesian → bayesian)
- [structural-analogy] Success = talent + luck, with regression toward the mean ↔ partial pooling/shrinkage in hierarchical models: noisy extreme values are pulled toward the average. — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → other)

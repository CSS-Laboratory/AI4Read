---
id: calibration
type: concept
fields: [decision-game-theory, bayesian, llm, political-science]
n_sources: 5
tiers: [core, deep, reference]
grounding: digests
sources: [grimmer-2022-textasdata/ch19-classifying, kahneman-2011-thinking/appa-judgment, murphy-2023-pml2/ch14-predictive, tversky-1974-heuristics/main, wei-2022-emergent/main]
generated_by: build_kg.py
---

# calibration

## Definitions in the sources

### decision-game-theory

- [[kahneman-2011-thinking/appa-judgment]] (pdf 424): stated percentile values match actual frequencies; in most studies the intervals judges gave were too narrow [new]
- [[tversky-1974-heuristics/main]] (p. 1129): a judge is properly (externally) calibrated in a set of problems if exactly $\Pi$ percent of the true values fall below his stated $X_\Pi$ [new]

### bayesian

- [[murphy-2023-pml2/ch14-predictive]] (pp. 578–580): predicted probabilities match empirical frequencies; measured by ECE/MCE [new]

### llm

- [[wei-2022-emergent/main]] (p. 5): whether a model can predict which questions it will answer correctly; compared via P(True) versus option probabilities [new]

### political-science

- [[grimmer-2022-textasdata/ch19-classifying]] (p. 322): whether predicted probabilities match true frequencies. Naive Bayes tends to be overconfident (p. 322) (new)

## Instances that use it

- [[record-linkage-calibration]] — mixture-model calibration of false-match rates, validated on test Census data — from [[gelman-2013-bda3/ch01-probability]]
- [[rabin-calibration]] — rejecting −100/+200 implies rejecting −200/+20,000 under utility theory — from [[kahneman-2011-thinking/ch26-prospect]]

## Candidate bridges

- [structural-analogy] "$n+1$ measurements fix an affine function" ↔ system identification / calibration of a sensor from reference inputs. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → unspecified)
- [structural-analogy] Posterior calibration ↔ frequentist bias: conditions on data instead of on the true parameter. — from [[gelman-2013-bda3/ch05-hierarchical]] (bayesian → other)
- [metaphor] Binned residuals with 95% bounds ↔ calibration plots in forecasting: averaged errors judged against expected variation. — from [[gelman-2013-bda3/ch06-model]] (bayesian → other)
- [structural-analogy] Assay unknown $\theta_j$ rescales the $x$-axis of a common curve ↔ calibration/measurement models in the social sciences: one shared response function, a unit-specific latent position. — from [[gelman-2013-bda3/ch19-parametric]] (bayesian → other)
- [structural-analogy] Overly narrow confidence intervals ↔ machine-learning model calibration: stated confidence exceeds hit rate. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → other)
- [structural-analogy] Rabin's theorem ↔ scaling or calibration arguments in other fields: a pattern fitted at small scale, extended by the model's own rules, gives absurd results at large scale. — from [[kahneman-2011-thinking/ch26-prospect]] (decision-game-theory → other)
- [structural-analogy] Congress needing calibrated local pictures ↔ measurement theory: combining unverified local reports without calibration instruments. — from [[lippmann-1922-publicopinion/ch18-role]] (communication-theory → other)
- [structural-analogy] Joy Pratt's calibration against data ↔ prior predictive checks: testing a prior against real data — from [[mcgrayne-2011-theory/ch11-business]] (bayesian → other)

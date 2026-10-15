---
id: correlation
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# correlation

## Definitions in the sources

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 191): covariance divided by the product of standard deviations, in $[-1,1]$ [new]
- [[strang-2023-introduction/ch10-learning]] (p. 397): ρ_xy = σ_xy/(σ_xσ_y), covariance of the standardized variables [new]

## Instances that use it

- [[risk-return-and-hedging]] — avg = return, std = risk; blending two assets with equal return and equal risk σ and correlation ρ gives risk σ√((1+ρ)/2) — from [[boyd-2018-vmls/ch03-norm]]
- [[straight-line-fit-correlation]] — slope = ρ·std(y)/std(x) — from [[boyd-2018-vmls/ch13-least]]
- [[wvs-democracy-and-gradual-change-items]] — two WVS items raise face-validity doubts; correlation only 0.38 — from [[clark-2017-principles/ch07-cultural-p1]]
- [[tv-news-random-assignment]] — survey correlation versus randomized newscasts — from [[clark-2017-principles/ch07-cultural-p2]]
- [[kendall-1953-serial-correlation]] — weekly changes in British share indices and in cotton and wheat prices look like a random walk — from [[fama-1970-efficient/main]]
- [[table-1-dow-serial-correlations]] — tiny, mixed-sign serial correlations for the 30 Dow stocks — from [[fama-1970-efficient/main]]
- [[sibling-heights-example]] — sibling heights stay correlated after controlling for age and sex; adding parents' heights lowers the correlation but in general leaves it positive — from [[gelman-2013-bda3/ch14-introduction]]
- [[spilerman-riot-sampling]] — repeated incidents with equal riot probability could explain the size correlation, $(.90)^{10}=.35$ — from [[granovetter-1978-threshold/main]]
- [[twin-study-theory-of-mind]] — 0.53 correlation in both twin types — from [[heyes-2014-cultural-evolution/main]]
- [[correlated-urn-markov-chain]] — forward correlations $\epsilon,\delta$, solved exactly; shows failure of the binomial for long runs — from [[jaynes-2003-probability/ch03-elementary]]
- [[church-suicide-spurious-correlation]] — both grow with population; correlation does not imply causation — from [[jaynes-2003-probability/ch17-principles-p2]]
- [[mechanical-turk-sample-critique]] — Kahan's argument that nonrepresentative samples may explain earlier CRT–conservatism correlations — from [[kahan-2013-motivatedreasoning/main]]
- [[german-students-dating-happiness]] — question order changes the dating–happiness correlation from about zero to very high — from [[kahneman-2011-thinking/ch09-answering]]
- [[intelligent-women-spouses]] — causal puzzle that is just imperfect correlation — from [[kahneman-2011-thinking/ch17-regression]]
- [[ceo-pairs-60-percent]] — correlation .30 gives about 60% of pairs — from [[kahneman-2011-thinking/ch19-illusion]]
- [[wealth-adviser-correlations]] — 28 correlations averaging .01 across 8 years — from [[kahneman-2011-thinking/ch20-illusion]]
- [[ashenfelter-bordeaux]] — weather formula, correlation above .90 with wine prices — from [[kahneman-2011-thinking/ch21-intuitions]]
- [[telephone-book-example]] — long-range correlation with random junk that defeats Lempel–Ziv — from [[mackay-2003-information/ch06-stream]]
- [[agenda-vs-selective-perception-test]] — all-news correlations beat own-party correlations in 18 of 24 comparisons — from [[mccombs-1972-agendasetting/main]]
- [[waffle-house-divorce]] — a correlation the author considers misleading, tied to Southernness — from [[mcelreath-2020-rethinking/ch05-multivariate-p1]]
- [[berkson-gaussian-example]] — $X\to Z\leftarrow Y$ Gaussian; selecting $z>2.5$ induces correlation between $X$ and $Y$ — from [[murphy-2023-pml2/ch04-graphical-p1]]
- [[texting-shallowness]] — correlation does not show that reducing texting reduces shallowness — from [[pearl-2016-primer/ch03-effects]]
- [[rooster-and-sunrise]] — correlation without causation; a counterfactual judgment shared by all — from [[pearl-2018-bookofwhy/ch00-introduction]]
- [[paris-skulls]] — correlation of 0.197 appears only after combining sexes — from [[pearl-2018-bookofwhy/ch02-buccaneers]]
- [[shoe-size-age-reading-fork]] — spurious correlation — from [[pearl-2018-bookofwhy/ch03-evidence]]
- [[dating-attractive-jerks]] — selection of dates creates a spurious negative correlation — from [[pearl-2018-bookofwhy/ch06-paradoxes]]
- [[tolstoy-vs-image]] — a novel and an image, whose uncompressed sizes could easily be equal, differ in correlation structure — from [[polyanskiy-2025-information/ch29-evaluating]]
- [[distributed-correlation-estimation]] — minimax error $\frac{1+o(1)}{2\ln2\,B}$ — from [[polyanskiy-2025-information/ch36-strong-p1]]
- [[total-correlation-vae-chairs]] — latent dimensions for rotation, size, legs — from [[prince-2023-udl/ch17-variational]]
- [[harvested-population-model]] — $dX/dt = X(1-X/K) - cX^2/(X^2+1)$ is the model of Fig. 1 (p. 54), where higher harvest rate c gives lower resilience, larger s.d. and higher correlation; Fig. 2 (p. 55) uses a harvested-population model driven slowly across a bifurcation (ref. 77) — from [[scheffer-2009-earlywarning/main]]
- [[height-weight-correlation]] — example of correlated variables — from [[stone-2022-information/ch07-channel]]
- [[lorenz-attractor]] — correlation dimension about 2.05 — from [[strogatz-2024-nonlinear/ch11-fractals]]

## Candidate bridges

- [structural-analogy] Cauchy–Schwarz on $\mathbf R^n$ and on $\int fg$ ↔ statistics: the same inequality bounds a correlation-like ratio — only the pairing differs. — from [[axler-2024-ladr/ch06-inner-p1]] (linear-algebra → other)
- [structural-analogy] Cauchy–Schwarz ⇒ cos θ ∈ [−1,1] ↔ statistics: correlation coefficient lies in [−1,1] — the same inequality bounds both. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → other)
- [same-math] Correlation coefficient ρ = cos∠(ã, b̃) ↔ cosine similarity of centred data vectors — the same formula, applied to mean-removed vectors. — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → unspecified)
- [structural-analogy] Carey's critique of "some do, some don't" with correlations below 0.5 ↔ statistics: low explained variance from antecedent variables, as in the toy example. — from [[carey-1989-cultural/ch02-mass]] (communication-theory → other)
- [structural-analogy] Voter/Glauber correlation equations ↔ statistical physics: same structure as the 1D zero-temperature Glauber Ising equations; in $d=1$ the dynamics coincide (p. 9–10). — from [[castellano-2009-socialdynamics/main-p1]] (complex-systems → complex-systems)
- [structural-analogy] Constraint as predictability ↔ statistics: correlation between item responses — both measure how much one variable predicts another. — from [[converse-1964-beliefsystems/ch01-introduction]] (political-science → other)
- [structural-analogy] Constraint matrix suitable for factor analysis ↔ psychometrics/latent-variable modelling: an organizing dimension shows up as shared correlation — the author himself links the two (p. 32) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other)
- [structural-analogy] "Instability sets an upper limit on constraint" (p. 47) ↔ measurement error: unreliability caps the correlation any measure can reach with others. — from [[converse-1964-beliefsystems/ch03-sections]] (political-science → other)
- [same-math] correlation $=\cos\theta$ (6.61) ↔ linear-algebra: cosine similarity — the inner product of normalised (centred) vectors. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [structural-analogy] PPCA covariance $BB^\top+\sigma^2I$ ↔ social-science latent factor models: a few shared factors plus noise explain the correlations among many observed variables. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → other)
- [structural-analogy] Explanatory asymmetry (cause → effect only) ↔ causal inference: correlation or deducibility is symmetric, but causal direction is not. — from [[godfreysmith-2003-theory/ch13-explanation]] (analytic-philosophy → bayesian)
- [structural-analogy] Detrending in order to estimate $A$ ↔ causal inference: regression adjustment for a confounder vs integrating over it. The spurious growth correlation (p. 535) is a common-cause pattern. — from [[jaynes-2003-probability/ch17-principles-p2]] (information-theory → bayesian)
- [metaphor] Conservative design under unknown correlations ↔ robust or minimax decision-making (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch22-introduction]] (information-theory → unspecified)
- [same-math] Move $r$ of the way from average to intuition ↔ statistics: prediction by a regression line with standardized variables — same weighting by correlation (the author calls it only an approximation of statistical analysis, pdf 188) — from [[kahneman-2011-thinking/ch18-taming]] (decision-game-theory → other)
- [structural-analogy] *Post hoc* reasoning ↔ causal inference: correlation versus cause — same warning, informal vocabulary. — from [[lippmann-1922-publicopinion/ch10-detection]] (communication-theory → bayesian)
- [structural-analogy] Hidden units inducing higher-order visible correlations ↔ bayesian: latent-variable and hierarchical models explaining dependence among observables. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → bayesian)
- [structural-analogy] Pooling across intercepts and slopes via correlation ↔ regression toward the mean in two dimensions — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → unspecified)
- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977). — from [[murphy-2023-pml2/ch28-latent-p2]] (bayesian → information-theory)
- [structural-analogy] I(X;Y) = −½ log(1−ρ²) for Gaussians ↔ statistics: correlation coefficient — both measure dependence, but I is bijection-invariant (p. 48). — from [[polyanskiy-2025-information/ch04-mutual]] (information-theory → other)
- [structural-analogy] Cause vs. blame; cross-sectional correlation vs. time order ↔ causal inference: the three conditions for causation (pdf 180). — from [[rogers-2003-diffusion/ch03-contributions]] (communication-theory → bayesian)
- [structural-analogy] shortcut reliance revealed by adversarial variants ↔ machine-learning evaluation: spurious correlations and shortcut learning — same logic of changing what should not matter. — from [[shapira-2024-clever-hans/main]] (theory-of-mind → other)
- [structural-analogy] MI's invariance under invertible transformations ↔ statistics: association measures such as correlation, which the author says lack this claim (p. 151). — from [[stone-2022-information/ch06-mutual]] (information-theory → other)
- [same-math] $\rho=\sqrt{1-2^{-2I}}$ for Gaussians ↔ statistics: correlation coefficient — the same bivariate Gaussian quantity expressed two ways. — from [[stone-2022-information/ch07-channel]] (information-theory → other)
- [same-math] Regression toward the mean ↔ statistics of correlation: the regression of $Y$ on $X$ when $r<1$ gives the shrinkage the text describes. — from [[tversky-1974-heuristics/main]] (decision-game-theory → other)
- [structural-analogy] Robustness to trivial alterations ↔ ML evaluation: out-of-distribution/adversarial testing of generalization — both probe whether a model learned the rule or surface correlations. — from [[ullman-2023-trivial-alterations/main]] (theory-of-mind → other)

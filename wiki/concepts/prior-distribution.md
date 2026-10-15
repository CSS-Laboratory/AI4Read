---
id: prior-distribution
type: concept
fields: [bayesian, information-theory, control-theory]
n_sources: 71
tiers: [core, reference, deep]
grounding: digests
sources: [bayes-1763-essay/main, efron-1986-bayesian/main, gelman-2013-bda3/appb-outline, gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch09-decision, gelman-2013-bda3/ch19-parametric, gelman-2013-bda3/ch21-gaussian, gelman-2013-philosophy/main, griffiths-2006-optimal/main, hernan-2020-whatif/ch11-model, jaynes-2003-probability/ch04-elementary, jaynes-2003-probability/ch05-queer, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch06-elementary-p2, jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch07-central-p2, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch15-paradoxes, jaynes-2003-probability/ch17-principles-p1, jaynes-2003-probability/ch17-principles-p2, jaynes-2003-probability/ch18-p, jaynes-2003-probability/ch20-model, jaynes-2003-probability/ch21-outliers, jaynes-2003-probability/front-preface, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch03-more, mackay-2003-information/ch07-codes, mackay-2003-information/ch21-exact, mackay-2003-information/ch25-exact, mackay-2003-information/ch28-model, mackay-2003-information/ch36-decision, mackay-2003-information/ch37-bayesian, mackay-2003-information/ch41-learning, mackay-2003-information/ch44-supervised, mackay-2003-information/ch45-gaussian, mackay-2003-information/ch46-deconvolution, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch05-multivariate-p2, mcelreath-2020-rethinking/ch06-overfitting-p2, mcelreath-2020-rethinking/ch08-markov, mcelreath-2020-rethinking/ch14-missing, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch04-bayes, mcgrayne-2011-theory/ch06-arthur, mcgrayne-2011-theory/ch07-tool, mcgrayne-2011-theory/ch08-jerome, mcgrayne-2011-theory/ch09-there, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch11-business, mcgrayne-2011-theory/ch12-who, mcgrayne-2011-theory/ch13-cold, mcgrayne-2011-theory/ch14-three, mcgrayne-2011-theory/ch15-navy, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch02-probability-p1, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch17-bayesian, pearl-2016-primer/ch01-preliminaries, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch03-evidence, sarkka-2023-bayesianfiltering/ch02-bayesian, tenenbaum-2011-grow/main]
raw_ids: [Prior distribution]
canon_spine: bayesian
generated_by: build_kg.py
---

# prior-distribution

## Canon spine entry

- **Prior distribution** (bayesian): what you believe about an unknown before seeing the current data, written as a probability distribution (UG)

## Definitions in the sources

### bayesian

- [[bayes-1763-essay/main]] (pp. 18–20): no explicit prior formula appears; the position of $o$ (uniform on $AB$) plays that role
- [[efron-1986-bayesian/main]] (p. 4): here improper priors: $d\theta$, $d\theta_1d\theta_2$, and Stein's $(\theta_1^2+\theta_2^2)^{1/2}d\theta_1d\theta_2$
- [[gelman-2013-bda3/appb-outline]] (pp. 587–588): the limit results need conditions on the prior; in particular $p(\theta_0)>0$ in the discrete case, and nonzero prior probability of the neighborhood $A$ in the continuous case
- [[gelman-2013-bda3/ch01-probability]] (p. 6): $p(\theta)$, one factor of the joint $p(\theta,y)=p(\theta)p(y|\theta)$
- [[gelman-2013-bda3/ch02-single]] (p. 34): read either as a population of parameter values or as a state of knowledge
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 88–89): its influence fades as n grows, except in the listed counterexamples
- [[gelman-2013-bda3/ch09-decision]] (pp. 248, 251): here the author uses "prior" for the predictive distribution from a hierarchical model before the house is measured, and says it is not subjective
- [[gelman-2013-bda3/ch19-parametric]] (p. 480): here informative and weakly informative priors from literature, separating uncertainty from population variation
- [[gelman-2013-bda3/ch21-gaussian]] (p. 501): here a GP prior on the unknown function $\mu(x)$
- [[gelman-2013-philosophy/main]] (pp. 12–13): here an assumption of the model, testable, not necessarily a belief; "more like" a regularization device
- [[griffiths-2006-optimal/main]] (p. 768): expectations about a class of events, here its empirical distribution of totals
- [[hernan-2020-whatif/ch11-model]] (p. 159): prior over all unknown parameters, required by Bayesian inference
- [[mcelreath-2020-rethinking/ch02-small]] (p. 34–35): initial plausibility for each parameter value; an engineering assumption to be checked, not a belief to be sworn to
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (pp. 77, 82): the initial information state of the model; here $\mu\sim\text{Normal}(178,20)$, $\sigma\sim\text{Uniform}(0,50)$
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (pp. 94–95): encodes information before data; here deliberately weak; no uniquely correct prior
- [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (pp. 150, 159): flat implicit priors in `lm` exaggerate collinearity's effect
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (pp. 186–187): here used as a tuning dial for how much to trust the sample; Normal(0,1)/(0,0.5)/(0,0.2) differ in strength
- [[mcelreath-2020-rethinking/ch08-markov]] (p. 258): flat priors say all values are equally plausible and can break chains
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 432): for a missing $N_i$, the "likelihood" line acts as a prior learned from the data
- [[mcgrayne-2011-theory/app-appendixes]] (p. 255): here, the background disease rate (0.4%) used as prior knowledge
- [[mcgrayne-2011-theory/ch01-causes]] (p. 8): the probability of the initial belief, Bayes' "guess" before new data
- [[mcgrayne-2011-theory/ch02-man]] (pp. 23, 31): the initial estimate $P_{\text{prior}}(C)$; first assumed equal for all causes
- [[mcgrayne-2011-theory/ch03-many]] (p. 37): starting probabilities; critics fixed on the equal-prior shortcut
- [[mcgrayne-2011-theory/ch04-bayes]] (pp. 73, 74, 79, 83): starting belief. Used as 50–50 by Kolmogorov (reluctantly) and Koopman, and as a 50% starting guess in Turingery; Simpson said that for practical purposes one need not agonise over prior odds
- [[mcgrayne-2011-theory/ch06-arthur]] (pp. 92–93): prior knowledge such as current insurance rates. Bailey was building a foundation to justify using it as the prior in Bayes' theorem
- [[mcgrayne-2011-theory/ch07-tool]] (p. 103): prior opinion, which may differ between researchers
- [[mcgrayne-2011-theory/ch08-jerome]] (pp. 111, 115): here the population incidence of disease, or cardiovascular death rates
- [[mcgrayne-2011-theory/ch09-there]] (p. 124): Madansky's prior on per-opportunity accident probability, deliberately not all concentrated at zero
- [[mcgrayne-2011-theory/ch10-46]] (p. 129): outside knowledge entering the analysis; the target of frequentist objections
- [[mcgrayne-2011-theory/ch11-business]] (pp. 142, 149–150): subjectively assessed starting belief, even from experts
- [[mcgrayne-2011-theory/ch12-who]] (p. 161): starting belief; here 50–50 odds, found to matter little
- [[mcgrayne-2011-theory/ch13-cold]] (p. 171): initial information from polls, expert opinion and voting histories
- [[mcgrayne-2011-theory/ch14-three]] (p. 177): "gentle" prior: belief-based but open to being overwhelmed by new information
- [[mcgrayne-2011-theory/ch15-navy]] (pp. 187, 199–200): here a map of probabilities over seabed cells, built from expert scenarios
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 237, 242, 246): prior knowledge, such as word order in English, price history or expert opinion
- [[murphy-2023-pml2/ch02-probability-p1]] (p. 8): $p(X=k)$ in (2.16), probability before seeing evidence $E$
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 64): beliefs about θ before data; here Beta(ᾰ,β̆) with hyper-parameters
- [[murphy-2023-pml2/ch03-statistics-p2]] (pp. 84, 97): here often expressed as virtual data (pseudo-counts $\breve\alpha$, strengths $\breve\kappa,\breve\nu$)
- [[murphy-2023-pml2/ch17-bayesian]] (pp. 648–651): here a prior over weights that induces a prior over functions; the architecture can matter even more
- [[pearl-2016-primer/ch01-preliminaries]] (p. 13): probability distribution assigned to hypotheses before the evidence
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 89–90): "prior belief" about the coin, which combines with evidence. Its influence may vanish as data grow
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 101, 104): probability before the evidence, e.g., 1/700 for cancer
- [[tenenbaum-2011-grow/main]] (p. 1280): $P(h)$, degree of belief in $h$ before the data; carries finer-grained background knowledge

### information-theory

- [[jaynes-2003-probability/ch04-elementary]] (pp. 87–88): probability conditional on $X$ alone, where $X$ is all information beyond the data $D$; no universal assignment rule
- [[jaynes-2003-probability/ch05-queer]] (pp. 126–131): prior information differs by person; this can make the same data support $S$ for one person and refute it for another
- [[jaynes-2003-probability/ch06-elementary-p1]] (pp. 152–162, 170): uniform, truncated, concave, binomial-monkey and Poisson priors; the choice drives conclusions
- [[jaynes-2003-probability/ch06-elementary-p2]] (p. 178): a description of the robot's own state of knowledge, not an "objectively true" probability
- [[jaynes-2003-probability/ch07-central-p1]] (p. 219): the prior $p(\sigma|I)$ states the range of plausible error scales
- [[jaynes-2003-probability/ch07-central-p2]] (pp. 220, 239–240): prior information is essential in the Gaussian-resolution problem and in safety estimation [as `Prior distribution`]
- [[jaynes-2003-probability/ch13-decision]] (pp. 413–414): g(α), first a weight on risk, then read as a prior density
- [[jaynes-2003-probability/ch15-paradoxes]] (p. 479): a proper $\pi(\eta)$ on an infinite domain is informative, since it bounds $\eta$ [as `Prior distribution`]
- [[jaynes-2003-probability/ch17-principles-p1]] (p. 528): can encode weak facts (e.g. "New York exists") and still be proper
- [[jaynes-2003-probability/ch17-principles-p2]] (p. 538): for Jaynes it carries real prior information that orthodoxy ignores
- [[jaynes-2003-probability/ch18-p]] (p. 555, p. 575): here the flat (A_p|X)=1, or the pre-prior ∝ 1/[p(1−p)]
- [[jaynes-2003-probability/ch20-model]] (p. 602): as used throughout
- [[jaynes-2003-probability/ch21-outliers]] (p. 620): prior information about the apparatus is, for Jaynes, the crucial factor in judging reject vs keep (p. 616); in the model it enters through the prior for u
- [[jaynes-2003-probability/front-preface]] (pdf 26–27): prior information as essential to correct inference; ignoring it can mislead
- [[mackay-2003-information/ch01-introduction]] (p. 6): here, P(s) = 0.5 for each source bit
- [[mackay-2003-information/ch02-probability]] (pp. 28, 31): probability density or distribution over the unknown, not a "guess" of its value
- [[mackay-2003-information/ch03-more]] (p. 50, p. 51): belief about the parameter before data; called a subjective assumption that must be explicit
- [[mackay-2003-information/ch07-codes]] (p. 135): here, the distribution over n implied by a code's lengths
- [[mackay-2003-information/ch21-exact]] (pp. 293, 298): P(b), P(e), and the uniform P(θ) on the grid
- [[mackay-2003-information/ch25-exact]] (p. 325): usually uniform over valid codewords
- [[mackay-2003-information/ch28-model]] (p. 347): as in (28.4)
- [[mackay-2003-information/ch36-decision]] (p. 452): $P(x_n)$, Gaussian with mean $\mu_n$ and variance $\sigma_n^2$
- [[mackay-2003-information/ch37-bayesian]] (p. 460): here a uniform prior on each probability
- [[mackay-2003-information/ch41-learning]] (p. 493): weight decay $\alpha E_W$ as a Gaussian prior, variance $1/\alpha$
- [[mackay-2003-information/ch44-supervised]] (p. 529): $\exp(-\alpha E_W)/Z_W$ [as `Prior distribution`]
- [[mackay-2003-information/ch45-gaussian]] (p. 535): here a prior over functions $P(y(x))$, not over parameters
- [[mackay-2003-information/ch46-deconvolution]] (p. 549–550): Gaussian here

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 19): $p(\theta)$, belief before data; may be non-informative [new]

## Candidate bridges

- [structural-analogy] Model as a priori restriction adding information ↔ bayesian: the prior distribution adding information. Fine Point 11.2 links priors to high-dimensional sensitivity. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Pretraining gradient mix during PPO ↔ regularization toward a prior distribution; here an extra loss term, not a Bayesian prior. — from [[ouyang-2022-instructgpt/main-p2]] (llm → unspecified)

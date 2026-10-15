---
id: clauset-2009-powerlaw/index
work: clauset-2009-powerlaw
type: work-map
units: [clauset-2009-powerlaw/main-p1, clauset-2009-powerlaw/main-p2]
---

# Clauset, A., Shalizi, C. R., & Newman, M. E. J. (2009). *Power-Law Distributions in Empirical Data*. SIAM Review, 51(4), 661–703.

## In one paragraph
Many papers claim a power law because a log-log plot looks roughly straight. This paper shows that this is not enough. It gives a three-step recipe. First, estimate the exponent and the lower cut-off $x_{\min}$ by maximum likelihood and KS-distance minimisation. Second, test whether a power law is plausible with a Monte Carlo goodness-of-fit $p$-value. Third, compare the power law with alternatives such as the log-normal, stretched exponential and power law with cut-off, using likelihood ratio tests. Applied to 24 real data sets, 17 are consistent with a power law, 7 are ruled out, and only word frequencies are clearly convincing. The method matters for anyone measuring heavy-tailed data.

## The path through the work
- [[clauset-2009-powerlaw/main-p1]] — The paper proposes a three-step recipe for recognising a power law: fit $x_{\min}$ and $\alpha$ by maximum likelihood plus Kolmogorov–Smirnov (KS) minimisation, test plausibility with a Monte Carlo $p$-value, and compare the fit with alternative distributions by a likelihood ratio test. A straight line on a log-log plot is not enough.
- [[clauset-2009-powerlaw/main-p2]] — Applied with proper maximum-likelihood fitting, goodness-of-fit and likelihood-ratio tests, only one of 24 data sets examined (word frequencies) appears to be a truly convincing power law, and the appendices give the mathematics behind those tools.

## Big ideas across units
- **A straight log-log line is necessary, not sufficient.** Part 1 builds the case and part 2 restates it after the real-data results. Units: main-p1, main-p2.
- **Regression on logs is unreliable; maximum likelihood is the right tool.** Part 1 shows biased least-squares fits in synthetic tests. Part 2 explains why (biased slopes, invalid standard errors, uninformative r²) and derives the continuous and discrete MLEs. Units: main-p1, main-p2.
- **The lower bound $x_{\min}$ must be estimated with $\alpha$.** KS minimisation is preferred over a BIC-based choice. Part 2 gives a simple discrete approximation for $x_{\min} \gtrsim 6$. Units: main-p1, main-p2.
- **Fitting always returns a power law, so plausibility needs a goodness-of-fit $p$-value.** A large $p$ does not prove a power law. Part 2 applies the test, with 17 of 24 sets consistent and 7 rejected. Units: main-p1, main-p2.
- **Compare against rival models by likelihood ratio.** Vuong's $p$-value tests the sign of the log-ratio and can report that the data cannot decide. Part 2 applies this to the real data, where most comparisons are inconclusive. Units: main-p1, main-p2.
- **Rival heavy-tailed families are often equally plausible.** These are the log-normal, the stretched exponential and the power law with cut-off. When statistics cannot separate them, mechanistic arguments are needed. Units: main-p1, main-p2.
- **Statistics can rule models out but not prove one.** Whether a heavy tail is "enough" depends on the scientific goal. Units: main-p1, main-p2.

## How to read it
- Essential: main-p1, which holds the whole recipe (fitting, testing, alternatives). Also read the real-data part of main-p2, including its ratings and conclusions, which shows the recipe at work.
- Depends on: main-p2 builds on main-p1. Its results use the $x_{\min}$ fit, the $p$-value and the likelihood-ratio test from part 1.
- Can skip on a first pass: the appendices in main-p2. These cover the MLE derivations and error properties, the likelihood-ratio details and the random-number recipes. Return to them for the maths, or if you need to simulate power-law data.

## Concepts introduced
Some ids in the units are near-duplicates (for example the two heavy-tail ids, the two maximum-likelihood ids, and the two nested-model ids). They are listed as written.
- [[heavy tail / power law]] — main-p1
- [[maximum-likelihood-estimation]] — main-p1
- [[x-min-estimation-ks]] — main-p1
- [[ks-statistic]] — main-p1
- [[complementary-cdf]] — main-p1
- [[bayesian-information-criterion]] — main-p1
- [[goodness-of-fit-p-value]] — main-p1
- [[likelihood-ratio-test]] — main-p1
- [[nested-models]] — main-p1
- [[bootstrap-uncertainty]] — main-p1
- [[heavy-tail-power-law]] — main-p2
- [[maximum-likelihood-estimator]] — main-p2
- [[fisher-information-cramer-rao]] — main-p2
- [[nested-vs-non-nested-models]] — main-p2
- [[power-law-with-cutoff]] — main-p2
- [[log-log-regression-pitfalls]] — main-p2
- [[inverse-transform-sampling]] — main-p2
- [[robustness-and-fragility]] — main-p2

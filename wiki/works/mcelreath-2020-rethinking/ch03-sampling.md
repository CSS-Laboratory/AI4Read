---
id: mcelreath-2020-rethinking/ch03-sampling
work: mcelreath-2020-rethinking
unit: "Chapter 3. Sampling the Imaginary"
pages: 49-70
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Sampling the Imaginary

## L0 — One line
Draw random samples from the posterior, and integral calculus becomes counting and summarizing, for parameters (intervals, point estimates) and for predictions (posterior predictive checks).

## L1 — The gist (≤ 120 words)
How do we summarize a posterior distribution and use it to predict, without doing integrals? McElreath draws many parameter values from the grid-approximate posterior of the globe tossing model. Intervals, quantiles and point estimates then come from counting and sorting samples. Different loss functions imply different point estimates. Simulating data from the sampled parameters gives the posterior predictive distribution. It carries both parameter uncertainty and observation uncertainty. Checking it against the data in several ways shows how a model fails. This matters because some of the most capable methods for fitting models, many of them Markov chain Monte Carlo (MCMC) variants used from Chapter 8, produce only samples.

**Prerequisites:** Bayes' theorem; the globe tossing grid approximation and binomial likelihood (Ch. 2); percentiles; basic R vectors.

## L2 — Key ideas (5–10 bullets)
- A positive test for a rare condition can give a low posterior probability. Many people find counts ("natural frequencies") easier to work with than probability formulas (pp. 49–50).
- Samples from the posterior turn integral problems into frequency counting. They also suit some of the most capable fitting methods, many of them Markov chain Monte Carlo (MCMC) variants, which produce only samples (pp. 50–51).
- Intervals of defined boundaries are the fraction of samples inside the bounds. Intervals of defined mass come from quantiles of the samples (pp. 53–56).
- The percentile interval (PI) puts equal mass in each tail and can mislead when the posterior is skewed. The highest posterior density interval (HPDI) is the narrowest interval with the given mass. If the choice of interval matters a lot, show the whole posterior (pp. 56–57).
- To pick a point estimate in a principled way, you need a loss function (a rule giving the cost of each possible error). Absolute loss gives the median, quadratic loss gives the mean (pp. 59–61).
- Bayesian models are generative. Likelihoods simulate "dummy data" from parameter values (p. 62).
- The posterior predictive distribution averages the data-simulation distributions over posterior samples. Using a single parameter value gives overconfident predictions (p. 65).
- Model checking asks how the model fails, not whether it is true. The same predictions viewed as longest run and number of switches are consistent with a failed independence assumption (pp. 67–68).

## L3 — Walkthrough

### Opening: vampires and natural frequencies (pp. 49–51)
**Setup.** A test detects vampirism 95% of the time: $\Pr(\text{positive}\mid\text{vampire})=0.95$. It gives false positives: $\Pr(\text{positive}\mid\text{mortal})=0.01$. Vampires are 0.1% of people: $\Pr(\text{vampire})=0.001$ (p. 49).

$$\Pr(\text{vampire}\mid\text{positive})=\frac{\Pr(\text{positive}\mid\text{vampire})\Pr(\text{vampire})}{\Pr(\text{positive})}$$

$$\Pr(\text{positive})=\Pr(\text{positive}\mid\text{vampire})\Pr(\text{vampire})+\Pr(\text{positive}\mid\text{mortal})\bigl(1-\Pr(\text{vampire})\bigr)$$

Result: 0.08683729, about 8.7% (R code 3.1, p. 49). When the condition is very rare, a test that finds all true cases can still carry little information. Most positives are false positives (p. 49).

**Why the author dislikes this example (p. 50).**
1. It is not specifically Bayesian. All the probabilities are frequencies of events, so all major statistical philosophies would use Bayes' theorem here. Bayesian inference is distinguished by a broad view of probability, not by the theorem.
2. It makes inference look harder than it is, because the formula "descends from the sky".

**Frequency format.** In 100,000 people, 100 are vampires. Of these, 95 test positive. Of the 99,900 mortals, 999 test positive. Positives: $95+999=1094$, so $\Pr(\text{vampire}\mid\text{positive})=95/1094\approx0.087$ (p. 50). Why this format helps is contentious. **Some people think** psychology works better with counts, since we meet counts, not probabilities, in daily life. The author says "Maybe so" (p. 50).

**Using this in the chapter.** The posterior is a probability distribution, so we can draw samples from it. The sampled events are parameter values. Parameter distributions express relative plausibility, not a physical random process. Inside the computer, parameters are as empirical as a coin flip (p. 50).

**Two reasons to sample early (p. 51).**
- Sampling turns calculus into data summary. An integral is just the total probability in an interval, so with samples it is a count. With many parameters, summarizing one focal parameter needs a complicated integral, but only a simple summary of samples.
- Some of the most capable posterior-computation methods produce only samples. Many of these are MCMC variants, which the book uses from Chapter 8.

*Intuition note.* Many people find counting people easier than juggling conditional probabilities. Samples do the same for posteriors: they are a crowd of imagined parameter values that we can count.

**Rethinking box: why statistics can't save bad science (pp. 51–52).** The same logic applies to testing hypotheses. Let $\Pr(\text{sig}\mid\text{true})=0.95$ (power), $\Pr(\text{sig}\mid\text{false})=0.05$, and base rate $\Pr(\text{true})=0.01$. Then Bayes gives $\Pr(\text{true}\mid\text{pos})\approx0.16$. Cutting the false-positive rate to 1% raises it to around 0.5. The author says the most important step is to improve the base rate, which "requires thinking, not testing" (p. 52).

### 3.1 Sampling from a grid-approximate posterior (pp. 52–53)
Grid posterior for 6 water in 9 tosses (R code 3.2): `p_grid` has 1000 points, flat prior, `dbinom(6, size=9, prob=p_grid)`, normalized (p. 52). Then (R code 3.3):

`samples <- sample(p_grid, prob=posterior, size=1e4, replace=TRUE)`

Picture a well-mixed bucket in which each value appears in proportion to its posterior probability. Scooping 10,000 values gives samples with the same proportions as the posterior (p. 52). `plot(samples)` and `dens(samples)` show that the density estimate resembles the grid posterior (Figure 3.1). With 1e5 or 1e6 samples it gets closer (p. 53).

### 3.2 Sampling to summarize (pp. 53–61)
Summary questions fall into three kinds: intervals of defined boundaries, intervals of defined probability mass, and point estimates (p. 53).

**3.2.1 Intervals of defined boundaries (pp. 53–54).**
- Grid: `sum(posterior[p_grid < 0.5])` gives 0.1718746 (R 3.6). With more than one parameter even this sum is not simple (p. 54).
- Samples: `sum(samples < 0.5)/1e4` gives 0.1726 (R 3.7). It differs slightly because the draws differ (p. 54).
- Between 0.5 and 0.75: `sum(samples > 0.5 & samples < 0.75)/1e4` gives 0.6059, about 61% (R 3.8, p. 54).
- `sum` counts because R treats TRUE as 1 and FALSE as 0 (Overthinking box, p. 54).

**3.2.2 Intervals of defined mass (pp. 54–58).** These are usually called confidence intervals. A posterior one may be called a credible interval, though the terms may be used interchangeably (p. 54). Treat the samples as data and ask for percentiles.
- Lower 80%: `quantile(samples, 0.8)` gives 0.7607608 (R 3.9, p. 55).
- Middle 80%: `quantile(samples, c(0.1, 0.9))` gives 0.4464464 and 0.8118118 (R 3.10, p. 56).

Intervals with equal mass in each tail are **percentile intervals (PI)**. They communicate shape well if the distribution is not too asymmetrical (p. 56).

**Skewed example (3 water in 3 tosses, flat prior; R 3.11, p. 56).** The posterior has its maximum at $p=1$.
- `PI(samples, prob=0.5)` gives 0.7037037 to 0.9329329 (R 3.12). It leaves out the most probable values near $p=1$, so it can mislead about the shape (p. 56).
- The **HPDI** (highest posterior density interval) is the narrowest interval containing the stated mass. `HPDI(samples, prob=0.5)` gives 0.8408408 to 1.0000000 (R 3.13, p. 56). Width is 0.16 versus 0.23 for the PI (p. 57).
- The Figure 3.3 caption says such a region always includes the most probable parameter value (p. 57).

**PI versus HPDI (p. 57).** In most cases they are very similar. They differ here only because the posterior is highly skewed. For 6 in 9 they are nearly identical, and for a bell-shaped posterior the choice hardly matters.
- *HPDI disadvantages:* it is more computationally intensive, has greater simulation variance (sensitivity to the number of samples), and is harder for audiences to understand. Ordinary non-Bayesian intervals are nearly always percentile intervals, of sampling distributions.
- *Author's advice:* if the interval type changes inferences, plot the whole posterior. The entire posterior is the Bayesian estimate and intervals only summarize it (p. 57).

*Intuition note.* A percentile interval trims equal slices from both tails, even when one tail is where the data point. The HPDI keeps the most plausible values and drops the least plausible ones.

**Rethinking boxes (p. 58).**
- *Why 95%:* it is convention. The author says it is hard to defend beyond convention, and cites Fisher's 1925 remark as unenthusiastic. The author suggests nested intervals such as 67%, 89%, 97% with the median. They are prime numbers, easy to remember, and avoid inviting unconscious hypothesis tests.
- *What confidence intervals mean:* in strict non-Bayesian inference, "probability 0.95 that the true value lies in the interval" is never correct. The correct reading is that 95% of intervals from many repeated studies would contain it. Whichever reading you use, a 95% interval does not contain the true value 95% of the time. History shows "chronic overconfidence". The 95% is a small-world number, true only in the model's logical world.

**3.2.3 Point estimates (pp. 58–61).** The Bayesian estimate is the entire posterior, so a point estimate is hardly ever necessary (p. 58). Example: 3 water in 3 tosses.
- MAP (maximum a posteriori, the mode): `p_grid[which.max(posterior)]` gives 1 (R 3.14). `chainmode(samples, adj=0.01)` gives 0.9985486 (R 3.15, p. 59).
- Mean 0.8005558 and median 0.8408408 (R 3.16). The three differ (p. 59).

**Loss functions.** A loss function gives the cost of using any particular point estimate. Different loss functions imply different point estimates (p. 59).

**Bet example.** You guess $d$ for $p$. You win \$100 for an exact guess, minus an amount proportional to $|d-p|$. The expected-winnings-maximizing (loss-minimizing) value is the posterior median (p. 59). The author shows this by calculation, not proof. The expected loss for $d=0.5$ is a posterior-weighted average:

`sum(posterior*abs(0.5 - p_grid))` gives 0.3128752 (R 3.17, p. 60).

For every $d$ at once, `sapply(p_grid, function(d) sum(posterior*abs(d - p_grid)))` (R 3.18). Then `p_grid[which.min(loss)]` gives 0.8408408 (R 3.19), the posterior median (p. 60).

**Conclusions (p. 61).**
- Absolute loss leads to the median. Quadratic loss $(d-p)^2$ leads to the posterior mean.
- When the posterior is symmetrical and normal-looking, median and mean converge. For 6 in 9 they are barely different.
- **Hurricane example:** damage rises fast with wind speed, so the loss is asymmetric. The optimal estimate would tend to be larger than the mean or median. The real decision is whether to evacuate, so a point estimate may be unnecessary.
- Scientists usually do not think about loss functions, so reported means or MAPs mostly describe the posterior's shape. The author advises communicating as much of the posterior, data and model as you can. "Premature decisions to accept or reject hypotheses can cost lives."

*Intuition note.* "Best single number" depends on how you pay for being wrong. Paying by distance gives the median. Paying by squared distance gives the mean.

### 3.3 Sampling to simulate prediction (pp. 61–68)
Simulated observations are useful for four reasons: model checking, software validation (recover known parameters), research design (such as power analysis), and forecasting (pp. 61–62).

**3.3.1 Dummy data (pp. 62–63).** The globe model assumes a fixed true $p$, and tosses give water and land in proportion $p$ and $1-p$. Likelihoods work in both directions. Given data, they give plausibility. Given parameters, they define a distribution of possible observations to sample from. So Bayesian models are always generative. Many non-Bayesian models are also generative, but many are not (p. 62). Simulated data is called **dummy data**:

$$\Pr(w\mid n,p)=\frac{n!}{w!(n-w)!}\,p^{w}(1-p)^{n-w}$$

With $n=2$, $p=0.7$: `dbinom(0:2, size=2, prob=0.7)` gives 0.09, 0.42, 0.49 (R 3.20). So 9% for $w=0$, 42% for $w=1$ and 49% for $w=2$ (p. 62).
- `rbinom(1, size=2, prob=0.7)` gives one simulated count (R 3.21). `rbinom(10, ...)` gives ten (R 3.22, p. 62).
- 100,000 draws (R 3.23) give frequencies 0.08904, 0.41948, 0.49148, close to the exact values apart from simulation variance (p. 63).
- With 9 tosses (R 3.24, Figure 3.5), most simulated samples do not contain water in the true proportion 0.7. There is a one-to-many relationship between data and data-generating processes (p. 63).

**Rethinking: sampling distributions (pp. 63–64).** Non-Bayesian traditions infer parameters through the sampling distribution. Here inference is never done directly through it. The posterior is deduced logically, and samples from it only help. Neither kind of "sampling" is a physical act.

**3.3.2 Model checking (p. 64).** This means (1) checking that the fitting worked and (2) judging adequacy for some purpose.
- *Did the software work?* Compare implied predictions (retrodictions) with the data used to fit. An exact match is neither expected nor desired. No correspondence at all probably means the software did something wrong. This cannot prove the software correct but often catches silly mistakes.
- *Is the model adequate?* The goal is not to test whether assumptions are "true", since all models are false. It is to see how the model fails, as a path to comprehension and revision. Judgment decides which failures matter.
- The author expects us to do better with the whole posterior than with a point estimate. A single value discards uncertainty information and leads to overconfidence (p. 64).

**Two uncertainties (p. 65).**
1. Observation uncertainty: even with $p$ known, the next toss is uncertain unless $p=0$ or $p=1$.
2. Uncertainty about $p$, given by the posterior. It carries over to everything that depends on $p$.

To **propagate** parameter uncertainty, compute the sampling distribution of outcomes at each $p$ and average these using the posterior probabilities. The result is the **posterior predictive distribution** (Figure 3.6, p. 65). The model predicts the data well, since the most likely observation is the observed one. Using only the peak value of $p$ gives a narrower, overconfident distribution, more like the one for $p=0.6$ in the middle row. It would make the model seem more consistent with the data than it is (p. 65).

**Computation.**
- One value: `w <- rbinom(1e4, size=9, prob=0.6)` (R 3.25, p. 65).
- Propagating uncertainty: `w <- rbinom(1e4, size=9, prob=samples)` (R 3.26). Each sampled $p$ generates one observation, so the output is averaged over the posterior. (added step) `samples` and `w` both have length $10^4$.
- The observed 6 water lies in the middle of the predictions. Much of the spread comes from the binomial process, not from uncertainty about $p$ (p. 66).

*Intuition note.* Using the posterior samples as the $p$ values makes each simulated dataset come from a plausible world. The pile of simulated datasets shows what the model expects, including how unsure it is about $p$.

**Checking the independence assumption (pp. 66–68).** The model treats each toss as independent. This is questionable, since the globe's orientation when tossed could influence the result (p. 67). The observed sequence is W L W W W L W L W. Two new views of the data (Figure 3.7, p. 67):
- Longest run: 3 (of W). The simulations are consistent with this. It is the most common simulated value, with much spread.
- Number of switches between W and L: 6. The simulations are less consistent with it, since most simulated samples have fewer switches than observed (p. 67–68).

This fits lack of independence, with each toss negatively correlated with the last. Whether the mis-specification matters depends on interests. If tosses do tend to switch, each toss provides less information about $p$. The wrong model will still converge on the correct proportion in the long run, but more slowly than its posterior suggests (p. 68).

**Rethinking: what does "more extreme" mean? (p. 68)** Ordinary p-values (tail-area probabilities) view data as the model expects it, which is weak model checking. Figure 3.7's definitions of "extreme" challenge the model more. Model fitting is objective, but model checking is "inherently subjective", which lets expertise and imagination help. The author notes that golems have terrible imaginations.

### 3.4 Summary (p. 68)
Samples from the posterior turn integral calculus into data summary. They give intervals, point estimates and posterior predictive checks. Posterior predictive checks combine parameter uncertainty with outcome uncertainty from the likelihood. They help verify software and find inadequacies.

### 3.5 Practice (pp. 69–70)
Easy (3E1–3E7) uses the fixed-seed samples of R code 3.27. Medium (3M1–3M5) uses 8 water in 15 tosses and an alternative prior. Hard (3H1–3H5) uses the birth data (100 two-child families; 111 boys among 200 births; R 3.28–3.30, p. 70).

## Toy example (ours, not from the text)
Flat prior on three grid values $p\in\{0.25,0.5,0.75\}$. Data: 2 water in 2 tosses. Likelihood $\propto p^2$: $0.0625,\ 0.25,\ 0.5625$. Sum $=0.875$. Posterior: $1/14,\ 4/14,\ 9/14\approx 0.071,\ 0.286,\ 0.643$.

**Frequency format.** Imagine 14 posterior draws: 1 of 0.25, 4 of 0.5, 9 of 0.75.
- Boundary interval: $\Pr(p<0.6)$ = draws below 0.6 / 14 = $(1+4)/14=5/14\approx0.357$.
- Median: sorted draws put 0.25 first, then four 0.5s (positions 2–5), then 0.75 from position 6 on. Positions 7 and 8 are both 0.75, so the median is 0.75.
- Absolute loss, expected $|d-p|$, from the posterior:
  - $d=0.25$: $(4\times0.25+9\times0.5)/14=5.5/14\approx0.393$.
  - $d=0.5$: $(1\times0.25+0+9\times0.25)/14=2.5/14\approx0.179$.
  - $d=0.75$: $(1\times0.5+4\times0.25+0)/14=1.5/14\approx0.107$.
  - The minimum is at $d=0.75$, the median, as in the chapter.
- Prediction: chance both of 2 new tosses are water. Averaging over the posterior: $(1\times0.0625+4\times0.25+9\times0.5625)/14=6.125/14=0.4375$. Using only the MAP $p=0.75$: $0.75^2=0.5625$. The plug-in version is overconfident, since it throws away uncertainty about $p$.

## Concepts
- [[bayes-theorem]] — used to invert $\Pr(\text{positive}\mid\text{vampire})$ into $\Pr(\text{vampire}\mid\text{positive})$ (p. 49)
- [[base-rate-neglect]] — a low base rate makes most positives false even for an accurate test (p. 49)
- [[posterior-distribution]] — the whole estimate, a function mapping each parameter value to a plausibility (p. 58)
- [[monte-carlo-integration]] — replacing integrals by counts over samples; the author does not use this name here (p. 51)
- [[markov-chain-monte-carlo-mcmc]] — a family of methods; some of the most capable posterior-computation methods produce only samples, and many of these are MCMC variants, used from Chapter 8 (p. 51)
- [[credible-interval]] — posterior interval of defined mass; the author notes that "confidence interval" may be used interchangeably (p. 54)
- [[frequentist-vs-bayesian-inference]] — in strict non-Bayesian inference, a confidence interval is read via repeated studies, not as a probability about the parameter (p. 58)
- [[posterior-predictive-distribution]] — outcome distributions at each $p$, averaged over the posterior (p. 65)
- [[posterior-predictive-check]] — compare simulated predictions with data, in several ways, to see how the model fails (p. 67)
- [[grid-approximation]] (new) — posterior computed on a grid of parameter values, then normalized (p. 52)
- [[percentile-interval]] (new) — interval with equal mass in each tail (p. 56)
- [[hpdi]] (new) — narrowest interval containing the stated posterior mass (p. 56)
- [[point-estimate-loss-function]] (new) — a point estimate depends on a loss rule: absolute loss gives the median, quadratic loss the mean (pp. 59–61)
- [[dummy-data-generative-model]] (new) — data simulated from the likelihood given parameters (p. 62)
- [[natural-frequencies]] (new) — presenting probabilities as counts (p. 50)
- [[small-world-number]] (new) — a probability valid inside the model's logical world only (p. 58)

## Canonical instances
- [[vampire-test]] — 95% sensitivity, 1% false positives, 0.1% base rate give 8.7% (p. 49)
- [[scientific-hypothesis-testing-base-rate]] — power 0.95, false-positive rate 0.05, base rate 0.01 give about 0.16 (p. 51)
- [[globe-tossing]] — 6/9 and 3/3 posteriors, sampling, predictive checks (pp. 52, 56, 65)
- [[hurricane-evacuation-loss]] — an asymmetric loss function (p. 61)
- [[birth-sex-data]] — 100 two-child families, used in the hard exercises (p. 70)

## Bridges (candidates)
- [same-math] Posterior samples as Monte Carlo draws ↔ simulation: expectations and probabilities are sample averages and fractions
- [same-math] Posterior predictive averaging ↔ marginalization: $\sum_p \Pr(p\mid\text{data})\Pr(\tilde w\mid p)$ (the formula is ours; the text describes it in words)
- [structural-analogy] Rare-condition test logic ↔ hypothesis testing: positive findings with a low base rate are mostly false
- [structural-analogy] Choosing a point estimate by loss ↔ decision theory: the cost rule picks the summary

## Questions this raises
- How does the sampling approach change when the posterior has many parameters and the samples come from MCMC?
- Which discrepancy statistics (such as runs or switches) should one pick, and how many checks are enough?
- If the toss outcomes were negatively correlated, how would we build a model that includes this?
- What would a principled loss function look like for a real research decision such as accepting a hypothesis?

## Exercises worth doing
- Ex. 3E1–3E3 (p. 69) — boundary intervals from samples — difficulty: easy
- Ex. 3E6–3E7 (p. 69) — HPDI versus PI of the same mass — difficulty: easy
- Ex. 3M3–3M4 (p. 69) — posterior predictive probabilities for new data — difficulty: medium
- Ex. 3M5 (p. 69) — effect of an informative prior — difficulty: medium
- Ex. 3H3–3H5 (p. 70) — predictive checks and the independence assumption — difficulty: hard

## Reading notes
- Printed = pdf − 14.
- Figure 3.2 caption says the lower 80% ends at "about 0.75"; R code 3.9 gives 0.7607608. Both appear in the text.
- The text writes "50% percentile confidence interval" (p. 56) and calls PI/HPDI "confidence intervals" in the Figure 3.3 caption. In the same section it also uses "credible interval".
- Page 66 says "the right-hand plot in Figure 3.6", but the page image shows the posterior predictive distribution as the bottom panel.
- Footnote numbers (47–60) appear in the text, but the endnote texts are not in these pages.
- The text layer of the figures was garbled. Numbers were checked against the page images.

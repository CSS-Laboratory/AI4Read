---
id: griffiths-2006-optimal/main
work: griffiths-2006-optimal
unit: paper
pages: 767-773
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Optimal Predictions in Everyday Cognition

## L0 — One line
When people predict a total duration or extent from one observed sample, their guesses, for most of the quantities tested, closely match a Bayesian predictor that uses the real-world statistics of that kind of event as its prior.

## L1 — The gist (≤ 120 words)
Perception and memory are often modelled as optimal inference. Cognitive judgments are often described as error-prone heuristics that are insensitive to priors. The authors asked people to predict totals, such as a life span or a movie's gross, from one observed value $t$. They compared answers with a Bayesian model whose prior was the empirical distribution of each quantity. For most quantities people matched the model, including very different shapes of prediction function for Gaussian, power-law and Erlang (exponential-tailed) priors. Errors on pharaoh reigns suggest people know the form of a distribution but may misjudge its parameters. The result suggests that, at least for everyday prediction tasks, people's implicit priors are calibrated to the world.

**Prerequisites:** Bayes' rule; prior, likelihood and posterior; median; basic integrals of powers and exponentials; the idea of Gaussian, power-law and exponential-tailed distributions.

## L2 — Key ideas (5–10 bullets)
- The task is to estimate $t_{total}$ from one sample $t$, assuming $t$ is uniform on $[0,t_{total}]$. For a given $t$, the form of the posterior is determined entirely by the prior $p(t_{total})$ (pp. 767–768, 773).
- The predicted value is the posterior median. Its shape depends on the prior family: Gaussian gives a nonlinear function; power law gives a constant multiple of $t$; Erlang gives $t$ plus a constant (pp. 768, 773).
- The empirical priors were approximately Gaussian for life spans and movie run times, power law for movie grosses and poem lengths, and Erlang for representatives' terms and pharaohs' reigns (p. 769).
- Median human predictions were indistinguishable from the optimal ones for five quantities. The model had no parameters fitted to the human data. This conflicts with prior-insensitive heuristics and with one fixed uninformative prior (p. 770).
- Predictions stayed close to optimal even for the irregular cake-baking prior (p. 771).
- Pharaoh predictions were slightly too high, but they fitted a subjective Erlang prior with larger $\beta$. The authors suggest people know the form of a distribution but not its parameters (p. 771).
- Predictions can reveal implicit priors. For waiting times, the best-fitting prior was a power law with $\gamma=2.43$ (p. 771).

## L3 — Walkthrough

### Introduction and the Bayesian model (pp. 767–768)
- **Authors' framing:** Perception and memory are often explained as near-optimal inference with accurate priors. Cognitive judgments under uncertainty are often characterized, after Kahneman, Tversky and colleagues, as error-prone heuristics insensitive to priors (p. 767). This looks at odds with people's ability to predict well from sparse data in the real world (p. 767).
- The test: people predict the duration or extent of everyday phenomena. Their answers are compared with a Bayesian model (p. 767).
- Example: predict a man's total life span $t_{total}$ from his current age $t$:
$$p(t_{total}\mid t)\propto p(t\mid t_{total})\,p(t_{total}) \tag{1}$$
 (p. 767).
- **Likelihood:** assume we are equally likely to meet him at any point in his life. Then $p(t\mid t_{total})=1/t_{total}$ for $0\le t\le t_{total}$ and $0$ outside (pp. 767–768). The authors compare this uniform-sampling assumption to the Copernican anthropic principle and the generic-view principle (p. 768).
- **Prior:** actuarial data show life spans (ignoring infant mortality) are approximately Gaussian, with $\mu\approx75$ and $\sigma\approx16$ years (p. 768).
- **Prediction:** take the median of $p(t_{total}\mid t)$, the point where a longer or shorter true value is equally likely. The median as a function of $t$ is the *prediction function* (p. 768).
- **Gaussian prior:** the prediction function is nonlinear. For $t$ far below $\mu$ it is about $\mu$. Near $\mu$ it rises slowly and converges towards $t$, staying slightly above it (p. 768). Examples: about 75 years for a man met at 18, 39 or 51; several more years for 75; not much longer for 96 (p. 768).
- **Power-law prior** $p(t_{total})\propto t_{total}^{-\gamma}$, $\gamma>0$ (movie grosses). The prediction is a constant multiple of $t$ that depends on $\gamma$. For the best-fitting power law for grosses, the predicted total is about 50% above the current gross: $40M → 60M$, $6M → 9M$ (p. 768). The authors call such constant-multiple rules clearly inappropriate for life spans: a 10-year-old girl would get 15 years and her 75-year-old grandfather 112 (p. 768).
- **Erlang prior** $p(t_{total})\propto t_{total}\exp(-t_{total}/\beta)$, $\beta>0$. This is a gamma distribution with $k$ fixed at 2 (footnote 2). The best guess is $t$ plus a constant set by $\beta$ (pp. 768–769).
- Figure 1 summarizes the shapes. Gaussian: slope below 1, intercept near $\mu$. Power law: linear, zero intercept, variable slope. Erlang: slope exactly 1, nonzero intercept (p. 768).

*Intuition note:* The observed $t$ says only that the total is at least $t$. The prior supplies the rest. A prior with a heavy tail makes "so far" scale into "total". A prior with a bounded typical range keeps the predicted total near the typical total.

### Appendix: the prediction problem (p. 773)
Given $t$ uniform on $[0,t_{total}]$:
$$p(t_{total}\mid t)=\frac{p(t\mid t_{total})p(t_{total})}{p(t)}\tag{A1}$$
$$p(t)=\int_0^\infty p(t\mid t_{total})p(t_{total})\,dt_{total}\tag{A2}$$
Since $p(t\mid t_{total})=1/t_{total}$ for $t_{total}\ge t$ and $0$ otherwise,
$$p(t)=\int_t^\infty\frac{p(t_{total})}{t_{total}}\,dt_{total}\tag{A3}$$
So the posterior's form is fixed by the prior.

**Power law,** $p(t_{total})\propto t_{total}^{-\gamma}$. The prior is improper if $\gamma\le1$, but the posterior is still proper.
$$p(t)\propto\int_t^\infty t_{total}^{-(\gamma+1)}dt_{total}=-\tfrac1\gamma t_{total}^{-\gamma}\Big|_t^\infty=\tfrac1\gamma t^{-\gamma}$$
$$p(t_{total}\mid t)=\frac{t_{total}^{-(\gamma+1)}}{\tfrac1\gamma t^{-\gamma}}=\frac{\gamma t^\gamma}{t_{total}^{\gamma+1}},\quad t_{total}\ge t\tag{A4}$$

**Erlang,** $p(t_{total})\propto t_{total}\exp(-t_{total}/\beta)$.
$$p(t)\propto\int_t^\infty \exp\{-t_{total}/\beta\}dt_{total}=-\beta\exp\{-t_{total}/\beta\}\Big|_t^\infty=\beta\exp\{-t/\beta\}$$
$$p(t_{total}\mid t)=\frac{\exp\{-t_{total}/\beta\}}{\beta\exp\{-t/\beta\}}=\frac1\beta\exp\{-(t_{total}-t)/\beta\},\quad t_{total}\ge t\tag{A5}$$
**Gaussian:** no simple analytic posterior (p. 773).

**Predicting.** The prediction $t^*$ is the posterior median, with $P(t_{total}>t^*\mid t)=.5$, where
$$P(t_{total}>t^*\mid t)=\int_{t^*}^\infty p(t_{total}\mid t)\,dt_{total}\tag{A6}$$
- Power law:
$$P(t_{total}>t^*\mid t)=\int_{t^*}^\infty\frac{\gamma t^\gamma}{t_{total}^{\gamma+1}}dt_{total}=-\Big(\frac{t}{t_{total}}\Big)^\gamma\Big|_{t^*}^\infty=\Big(\frac t{t^*}\Big)^\gamma\tag{A7}$$
 Setting this to .5 gives $t^*=2^{1/\gamma}t$.
- Erlang:
$$P(t_{total}>t^*\mid t)=\int_{t^*}^\infty\frac1\beta\exp\{-(t_{total}-t)/\beta\}dt_{total}=\exp\{-(t^*-t)/\beta\}\tag{A8}$$
 Setting this to .5 gives $t^*=t+\beta\log 2$.
- Gaussian: $t^*$ comes from numerical integration and optimization (p. 773).

*Intuition note:* Under the power law, the chance that the total exceeds a multiple of $t$ does not depend on the scale of $t$. So the median is a fixed multiple of $t$. Under the Erlang prior, the remaining time has a fixed exponential distribution whatever $t$ is. So the median adds a fixed amount.

### Method (pp. 769–770)
- **Priors from data:** the sources are in Table 1. Examples: 5,302 movie grosses, 1,000 poem lengths, 126 pharaoh reigns (p. 769).
- **Participants:** two groups of undergraduates, 208 and 142. Each made one prediction for each of five phenomena, within a booklet of unrelated experiments (pp. 769–770).
- **Stimuli:** each prediction used one of five values of $t$, assigned randomly between subjects. Examples: $1, 6, 10, 40, 100$ million dollars for grosses; $18, 39, 61, 83, 96$ years for life spans; $1, 3, 7, 11, 23$ years for pharaohs (p. 770).
- **Instructions:** give intuitions, no complicated calculations. Each question gave a short context and asked for $t_{total}$ given $t$ (p. 770).

### Results (pp. 770–771)
- **Filtering:** responses were removed if they were non-numeric or less than "$t_{total}$" as printed (see Reading notes). Analyzed counts ranged from 126 (cakes) to 197 (poems, life spans) (p. 770).
- **Marriages:** 52% answered "forever". This matches the proportion of marriages that do not end in divorce, but it blocked median-based analysis. Marriages were not analyzed further (p. 770).
- **Main result:** judgments for life spans, movie run times, movie grosses, poem lengths and representatives' terms were indistinguishable from optimal predictions based on empirical priors (Fig. 2). Prediction functions had different shapes for Gaussian, power-law and Erlang priors. The model had no free parameters tuned to the human data (p. 770).
- **Implications:** inconsistent with claims of prior-insensitive non-Bayesian heuristics (Kahneman et al.; Tversky & Kahneman). Also inconsistent with Bayesian models that use one uninformative prior $p(t_{total})\propto1/t_{total}$ for every phenomenon (Gott and others) (p. 770).
- **Pharaohs:** predictions had the Erlang form but were slightly too high. In a follow-up, 35 undergraduates gave the typical reign. The median was 30 years, which corresponds to $\beta=17.9$ (true value about 9.34). This subjective prior fits the judgments closely (p. 771).
- **Cakes:** the true distribution is irregular, yet judgments stayed close to the ideal predictions (p. 771).
- **Waiting times:** the true distribution is controversial. Traditional Poisson-process models imply exponential tails. Several recent analyses suggest power laws may fit better. The authors fitted Gaussian, power-law and Erlang prediction functions to median judgments by least squares. The power law with $\gamma=2.43$ fitted best. If predictions are near-optimal for the true distribution, this is qualitatively consistent with the power-law models (p. 771).

### Discussion (pp. 771–772)
- People's judgments were close to the optimal ones across settings. They revealed implicit beliefs surprisingly consistent with world statistics, paralleling perception and memory (p. 771).
- **Pharaoh errors:** errors and between-participant variance were substantially larger here. Most participants probably had little direct experience of pharaohs. Judgments were consistent with knowing the correct form but misjudging its parameters (p. 771).
- **Hypothesis (suggested, not tested):** people may predict by analogy with familiar phenomena, such as modern monarchs. They would then adjust the mean downward by an uncertain, insufficient amount. This would fit the error pattern and could be adaptive (p. 771).
- **Broader claim:** Bayesian models have been proposed for words, concepts, generalization and causal relations. They have not typically tried to establish optimality in real-world environments. At least for a range of everyday prediction tasks, people adopt priors accurately calibrated to world statistics. The scope and depth of this correspondence is a challenge for future work (p. 772).

## Toy example (ours)
Meet an event that has lasted $t=10$ so far.
- **Power law, $\gamma=1$:** $t^*=2^{1/1}\cdot10=20$. Check with A7: $P(t_{total}>20\mid t=10)=(10/20)^1=0.5$.
- **Power law, $\gamma=2$:** $t^*=2^{1/2}\cdot10\approx14.14$. Check: $(10/14.14)^2=0.5$.
- **Erlang, $\beta=10$:** $t^*=10+10\cdot0.693=16.93$. Check with A8: $\exp\{-6.93/10\}=\exp(-0.693)=0.5$.
- **Scaling $t$ to 100 (the multiples and the added constant do not depend on $t$):** the power law gives 200, 141.4 and the Erlang gives 106.93.

Same data, different priors give different rules: multiply for the power law, add for the Erlang.

## Concepts
- [[bayes-theorem]] — Eq. 1 combines likelihood and prior to give a posterior over $t_{total}$ (p. 767)
- [[prior-distribution]] — expectations about a class of events, here its empirical distribution of totals (p. 768)
- [[likelihood]] — $p(t\mid t_{total})=1/t_{total}$ for $t\le t_{total}$ (p. 767)
- [[posterior-distribution]] — $p(t_{total}\mid t)$, whose form is fixed by the prior (pp. 768, 773)
- [[rational-analysis]] — judging cognition against the optimal solution given world statistics (p. 767); the paper does not use this label for its own approach, and it appears only inside reference titles (p. 772)
- [[principle-of-indifference]] — related only loosely: the fixed uninformative prior $1/t_{total}$ is an alternative the data are inconsistent with (p. 770)
- [[prediction-function]] (new) — the posterior median of $t_{total}$ as a function of $t$ (p. 768)
- [[uniform-sampling-assumption]] (new) — the observation point $t$ is uniform on $[0,t_{total}]$ (p. 767)
- [[power-law-prior]] (new) — $p(t_{total})\propto t_{total}^{-\gamma}$; median prediction $2^{1/\gamma}t$ (pp. 768, 773)
- [[erlang-prior]] (new) — $p(t_{total})\propto t_{total}e^{-t_{total}/\beta}$; median prediction $t+\beta\log2$ (pp. 768, 773)
- [[improper-prior]] (new) — a prior whose integral diverges; for $\gamma\le1$ the posterior is still proper (p. 773)
- [[prediction-by-analogy]] (new) — hypothesis that people borrow a distribution's form from familiar cases (p. 771)

## Canonical instances
- [[life-span-prediction]] — Gaussian prior, nonlinear prediction function (pp. 768, 770)
- [[movie-gross-prediction]] — power-law prior, a constant multiple of $t$ (p. 768)
- [[pharaoh-reigns]] — right form, wrong parameter ($\beta$ 17.9 vs about 9.34) (p. 771)
- [[waiting-time-prior-inference]] — power law with $\gamma=2.43$ fitted from judgments (p. 771)
- [[cake-baking-times]] — an irregular prior, still near-optimal (p. 771)
- [[marriage-length-prediction]] — not analyzed because 52% said "forever" (p. 770)

## Bridges (candidates)
- [same-math] Median prediction under a power-law prior ↔ scale invariance: $P(t_{total}>kt\mid t)=k^{-\gamma}$ (for $k\ge1$) does not depend on $t$
- [structural-analogy] Predicting $t_{total}$ from $t$ ↔ the Copernican principle in cosmology and the generic-view principle in vision (named on p. 768): each assumes the sample is typical
- [structural-analogy] People's prior mirroring world statistics ↔ rational analysis of memory (Anderson), cited as a parallel on p. 771
- [metaphor] Prediction by analogy ↔ hierarchical or transfer learning: form shared from familiar classes, parameters set by data

## Questions this raises
- How do people learn world priors so accurately? From direct experience, or from indirect sources?
- If people use prediction by analogy, how could we test it directly?
- Are the median responses of a group the same as the predictions of each person? Only group medians are analyzed.
- How far does the match extend beyond everyday magnitudes (the "scope and depth" question, p. 772)?

## Reading notes
- Printed pages 767–773 match the page labels (offset 0). Page 772 holds the end of the Discussion, the references and the start of the appendix; page 773 continues the appendix.
- **Misprint (appendix, p. 773):** in the Erlang derivation the integral for $p(t)$ is printed with lower limit $0$, but it is then evaluated on $[t,\infty)$. A3 requires lower limit $t$. I used $t$.
- The filtering rule (p. 770) says responses "less than $t_{total}$" were removed. This presumably means less than $t$, since $t_{total}$ is the answer. This is my reading, not stated in the text.
- The fitted prior values ($\gamma=2.43$, $\beta=17.9$) are as printed. The figure shows the prediction curves, but I cannot give exact values from it.
- The text says people's responses were "indistinguishable" from optimal. No statistical test is described in these pages; Figure 2 shows medians with bootstrap error bars.
- The text layer's equation characters were garbled; I checked all equations against the page image.

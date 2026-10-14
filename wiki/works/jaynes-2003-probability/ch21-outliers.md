---
id: jaynes-2003-probability/ch21-outliers
work: jaynes-2003-probability
unit: "21 Outliers and robustness"
pages: 615-626
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Outliers and robustness

## L0 — One line
Whether to discard or keep an outlier depends on prior information about the apparatus, and Jaynes argues that a Bayesian mixture model of "good" and "bad" data, if flexible enough, delivers robustness automatically when it is desirable, with no ad hoc rule.

## L1 — The gist (≤ 120 words)
One of n measurements lies far from the rest. Should we throw it out or keep it? Jaynes argues that "throw it out" and "keep it" are each reasonable under different prior beliefs about how reliable the apparatus is. Ad hoc rejection rules and Huber/Tukey-style "robust" estimators ignore this. He models each datum as coming from a good distribution G or a bad distribution B, with unknown purity u. The posterior for θ then uses a quasi-likelihood: a prior-weighted average of good-data likelihoods over every possible good/bad labelling. Known outliers are usually discarded; suspect data deserve, intuitively, less credence; Jaynes blames an overly dogmatic model (u = 1) for the apparent non-robustness of Bayesian estimates.

**Prerequisites:** Bayes' theorem; likelihood and marginal posterior; nuisance parameters; exchangeability and de Finetti's theorem (Ch. 18); sample mean and variance.

## L2 — Key ideas
- Two opposed positions, "reject the outlier" and "an outlier may be the key datum", reflect different prior information about the apparatus; fixed rejection criteria such as Chauvenet's ignore this (pp. 615–616).
- Jaynes argues that any robustness property precise enough to compare estimators transitively implies an optimality principle. He adds that robustness costs performance when the model is right (pp. 617–618).
- Jaynes holds that robust/resistant methods are intuitive approximations to what a full Bayesian analysis gives automatically (pp. 618–619).
- The two-model model treats each datum as good (from G) or bad (from B). An exchangeable prior on the labels (their probability depends only on how many are good) gives the mixture $uG+(1-u)B$ (pp. 619–620).
- The marginal posterior of θ uses a quasi-likelihood: a prior-weighted average of good-distribution likelihoods over all good/bad assignments (pp. 622–624).
- Known "pure outliers" are discarded, because their factor is usually independent of θ. If that factor did depend on θ, the outliers' values would themselves be evidence about θ (pp. 624–625).
- In the receding-datum example, the apparent Bayesian non-robustness comes from a dogmatic model that assumes u = 1. Jaynes says flexible models show robustness automatically, and, by an analogy, suggests that Bayesian methods are criticised more because their errors are more visible (pp. 625–626).

## L3 — Walkthrough

### Introduction (p. 615)
We measure θ with n independent measurements $x_1,\dots,x_n$. Clustered data are easy. But one value $x_j$ may lie far from the other $n-1$. What 'best' estimate and what accuracy should we report? Jaynes recalls Chapters 4–5, where surprising data can revive "dead" hypotheses, and says it appears something similar may be at work here. He treats only outliers and leaves other unexpected structure as an exercise (p. 615).

### 21.1 The experimenter's dilemma (pp. 615–617)
- **Position (I):** something went wrong with the apparatus, so throw the outlier out. **Position (II):** discarding data because they are unexpected is dishonest; the outlier may be the most significant datum (pp. 615–616).
- Jaynes's diagnosis: the positions reflect different *prior information* about the apparatus, and the ad hoc rules (e.g. the Chauvenet criterion, "two standard deviations") ignore it. What is needed is "straightforward probability analysis", not more *ad hockeries* (p. 616).
- (I) seems reasonable if we know the apparatus is unreliable and likely to break down without warning; then a wild outlier seems far more likely to be an apparatus failure than a real effect (p. 616).
- (II) is reasonable for someone with absolute confidence, for example that a voltmeter is reliable to ±0.5% and cannot be off by 5%. Then the outlier is a significant event (p. 616).
- Real experimenters are almost always in between (p. 616).
- For clustered data, the report $(\theta)_{\rm est}=A\pm B$ is naturally $A=\bar x=n^{-1}\sum x_i$. The sample variance is $s^2\equiv n^{-1}\sum (x_i-\bar x)^2=\overline{x^2}-\bar x^2$. One might first take $B=s$, since the scatter indicates reproducibility and one might suppose also accuracy; a more educated intuition improves this to $B=s/\sqrt n$:
$$(\theta)_{\rm est}=\bar x\pm\frac{s}{\sqrt n}\tag{21.1}$$
This would not be called wildly unreasonable, although it is not shown optimal (pp. 616–617).
- So far the discussion seems to consider only two actions: keep the outlier at full credence, or discard it. Is there a defensible middle position? (p. 617)

*Intuition note:* How much an odd value should be trusted depends on how much you trusted the instrument before. A fixed cut-off cannot encode that.

### 21.2 Robustness (pp. 617–619)
- **Huber's view:** methods should be *robust* (insensitive to the exact error distribution) or *resistant* (large errors in a few data do not matter much). Jaynes characterises these as still intuitive, ad hoc procedures that take no explicit note of prior information (p. 617).
- Jaynes says there could be some merit in this view, but that the Tukey/Mosteller school carries it to the point of deprecating all considerations of optimality (p. 617).
- **Jaynes's argument:** if "more robust" can be defined precisely enough to compare estimators transitively, then within a set S of feasible estimators an "optimally robust" one exists. Jaynes: as soon as the property is defined with enough precision to allow transitive comparisons, an optimality principle follows inexorably; so one cannot consistently advocate a well-defined inference property and at the same time reject optimality principles (pp. 617–618).
- Robustness has a price in performance when the model is correct. Jaynes says the "most robust" procedure of all (the "optimal" one if only robustness is asked for) ignores model, data and prior information and considers all parameters zero, all hypotheses false (p. 618).
- The sample median is cited as more robust than the mean. But values above or below the median can move arbitrarily without changing it, so relevant information is lost (p. 618). Footnote 3 makes a similar point about admissibility: an estimator that always answers $\theta^*=5$ is admissible if 5 is in the parameter space (p. 618).
- **Jaynes's claim:** Bayesian analysis "properly applied" delivers robustness automatically when desirable. Present robust methods are intuitive approximations to a full Bayesian analysis (p. 618).
- Here the *model* is in doubt, which is part of the prior information. Data and prior information are two parts of the total evidence and enter probability theory the same way, as in the horse-racing case of Sec. 5.6 (pp. 618–619).
- Reasoning unresponsive to the model is also somewhat unresponsive to the data. Jaynes's answer is "Sometimes": in problems where we are unsure of the model but nevertheless sure of the meaning of its parameters. If we are sure of the model, robustness wastes data. Jaynes says that if the sampling distribution represents our prior knowledge properly, Bayesian analysis gives robustness/resistance when we are unsure of the model and optimal performance when we are sure of it (p. 619).
- **Concession:** Tukey-style devices can handle one-time contingencies not worth modelling. But they are "one-man" operations with no criterion others can judge. A consistent normative theory means, by Cox's theorems, a Bayesian theory (p. 619).

*Intuition note:* Reasoning that is unresponsive to changes in the model must also, in some way, be unresponsive to changes in the data. A method that is "safe" against every model gives up information when one model is in fact right.

### 21.3 The two-model model (pp. 619–620)
- Good sampling distribution $G(x|\theta)$ (21.2). Bad distribution $B(x|\eta)$ (21.3), with η an uninteresting parameter. Data $D=(x_1,\dots,x_n)$ (21.4).
- We do not know which data are good. An obvious outlier, or a datum where $G\ll B$, is suspect (p. 620).
- Define $q_i=1$ if datum i is good and $q_i=0$ if bad (21.5). Prior information is a joint prior $p(q_1\cdots q_n|I)$ over the $2^n$ sequences (21.6) (p. 620).

### 21.4 Exchangeable selection (pp. 620–622)
- **Exchangeable prior:** the probability of a good/bad sequence depends only on the counts r good and $n-r$ bad. By de Finetti (Ch. 18):
$$p(q_1\cdots q_n|I)=\int_0^1 du\,u^r(1-u)^{n-r}g(u)\tag{21.7}$$
Here u is the "purity" of the data (the closer to 1 the better), and g(u) may, for present purposes, be thought of as its prior density (p. 620).
- Hence the sampling distribution is a mixture:
$$p(x|\theta,\eta,u)=uG(x|\theta)+(1-u)B(x|\eta),\quad 0\le u\le1\tag{21.8}$$
θ is the parameter of interest, and $(\eta,u)$ are nuisance parameters. No new principles beyond Ch. 6 are needed (pp. 620–621).
- **Special case, binary hypothesis testing:** $p(u|I)=p_0\,\delta(1-u)+p_1\,\delta(u)$ (21.9), with $H_0$ = all data from $G(x|\theta)$ and $H_1$ = all from $B(x|\eta)$ (21.10). Here $p_0=p(H_0|I)$ and $p_1=1-p_0$ (p. 621).
- A full solution tends to become intricate, but often much of the detail contributes little to the conclusions sought (which might be only the first few moments or percentiles), so good approximate algorithms may suffice (p. 621).
- Intuition: if $G$ is tiny for $|x|>1$ while $B$ has long tails, then a datum with $|y|>1$ is suspect, and intuitively one feels we should give it a little less credence ("hedge our bets"). If a datum's validity is suspect, intuition suggests that our conclusions ought to be less sensitive to its exact value, which Jaynes says is just about the condition of robustness, now with a rationale. As $|x|\to\infty$ the datum is practically certain to be bad, and intuition probably tells us to disregard it altogether (p. 621).
- Tukey's "redescending psi function" does this by intuition. Jaynes says these works typically either ignore Bayesian methods or criticise them as non-robust, never offering factual evidence, and he proposes to examine an actual Bayesian calculation (pp. 621–622).

### 21.5 The general Bayesian solution (pp. 622–624)
Joint posterior with normalising constant A:
$$f(\theta,\eta,u|DI)=A\,f(\theta,\eta,u|I)\,L(\theta,\eta,u)\tag{21.11}$$
$$L(\theta,\eta,u)=\prod_{i=1}^n\big[uG(x_i|\theta)+(1-u)B(x_i|\eta)\big]\tag{21.12}$$
$$p(\theta|DI)=\iint d\eta\,du\,f(\theta,\eta,u|DI)\tag{21.13}$$
Factor the prior: $f(\theta,\eta,u|I)=h(\eta,u|\theta,I)f(\theta|I)$ (21.14). Then
$$f(\theta|D,I)=\frac{f(\theta|I)\,\overline L(\theta)}{\int d\theta\,f(\theta|I)\overline L(\theta)}\tag{21.15}$$
with the **quasi-likelihood**
$$\overline L(\theta)\equiv\iint d\eta\,du\,L(\theta,\eta,u)\,h(\eta,u|\theta,I).\tag{21.16}$$
Expanding the product (p. 622):
$$\overline L(\theta)=\iint d\eta\,du\,h(\eta,u|\theta,I)\Big[u^nL(\theta)+u^{n-1}(1-u)\sum_{j}B(x_j|\eta)L_j(\theta)+u^{n-2}(1-u)^2\sum_{j<k}B(x_j|\eta)B(x_k|\eta)L_{jk}(\theta)+\cdots+(1-u)^nB(x_1|\eta)\cdots B(x_n|\eta)\Big]\tag{21.17}$$
where
$$L(\theta)\equiv\prod_{i=1}^nG(x_i|\theta),\quad L_j(\theta)\equiv\prod_{i\ne j}G(x_i|\theta),\quad L_{jk}(\theta)\equiv\prod_{i\ne j,k}G(x_i|\theta),\ \text{etc.}\tag{21.18}$$
These are good-distribution likelihoods using all the data, all but $x_j$, all but $x_j,x_k$, and so on (p. 623).

Interpretation (p. 623):
- The coefficient of $L(\theta)$ is $\int du\,u^n h(u|\theta,I)$ (21.19), the probability, given θ and I, that all data are good.
- The coefficient of $L_j(\theta)$ is $\int du\,u^{n-1}(1-u)\int d\eta\,B(x_j|\eta)h(\eta,u|\theta,I)$ (21.20). It is the probability that the j-th datum is bad with value $x_j$ and the others are good. The factor (21.21) is the joint density that $x_j$ is bad, the other $n-1$ are good and η lies in $(\eta,\eta+d\eta)$.
- Usually h does not depend on θ, since u refers to a different context; Jaynes keeps the generality to expose later points (p. 623).

In words, a compact restatement of (21.22):
$$\overline L(\theta)=\sum_{\text{labellings}}\text{prob(that labelling)}\times\text{(likelihood from the data labelled good)},$$
from "all good" down to "all bad" (p. 623). The quasi-likelihood is a prior-weighted average over every possible assumption about which data are good (p. 624).

*Intuition note:* The quasi-likelihood does not decide once and for all which points are outliers. It averages the good-data likelihoods over all possible labellings, each weighted by the prior probability of that assumption.

### 21.6 Pure outliers (pp. 624–625)
- Suppose $G(x|\theta)=0$ for $|x|>1$ (21.23), while B is positive on a wider interval. Then any datum with $|x|>1$ is certainly bad (p. 624).
- Intuition says throw it out. Example: $x_j=1.432$, $x_k=2.176$, all other $|x|<1$. Only one term of (21.17) survives:
$$\overline L(\theta)=\iint du\,d\eta\,h(\eta,u|\theta,I)B(x_j|\eta)B(x_k|\eta)L_{jk}(\theta)=C_{jk}(\theta)L_{jk}(\theta)\tag{21.24}$$
- Jaynes says throwing them out is "almost right": $C_{jk}$ is almost always independent of θ, and constant factors do not matter, so the quasi-likelihood reduces to the one obtained by throwing the outliers away. More generally, a known outlier should be thrown out if the probability of getting that particular outlier is independent of θ (pp. 624–625).
- Rarely, $C_{jk}$ may depend on θ. Then the outliers' values are themselves evidence about θ. Bayes' theorem "relentlessly seeks out" every relevant factor (p. 624).
- In general, a datum is known with certainty to be an outlier only if $G(x_i|\theta)=0$ for all θ. Every likelihood containing $x_i$ is then zero, so the posterior is as if $x_i$ had never been observed (p. 625).

### 21.7 One receding datum (pp. 625–626)
- Ten observations, location parameter; one datum recedes to 100 standard deviations of G (p. 625).
- **Model with G only:** if G is Gaussian $N(\theta,\sigma)$ and the prior for θ is wide (say $>1000\sigma$), the estimate under quadratic loss stays the sample average. The far datum drags it about ten standard deviations from the mean of the other nine. Jaynes says this is presumably why Bayesian methods are sometimes charged with failure to be robust/resistant (p. 625).
- Jaynes: that model asserts dogmatically $u=1$. Someone who truly held this would rightly treat the far datum as highly significant, and discoveries have come from such confidence (p. 625).
- If intuition insists the datum be thrown out, then we do not really believe $u=1$ strongly enough to adhere to it in the face of the surprising datum. The fix is the model (21.8). The fault lies in the dogmatic model, not in Bayesian methods (p. 625).
- Bayesian methods contain robust/resistant qualities and show them when a sufficiently flexible model permits. In probability theory, failure to notice a feature may amount to making irrational assumptions about it (p. 625).
- Why are Bayesian methods criticised more? His analogy: a city with better crime detection looks more criminal. Errors undetected are errors uncriticised (p. 626).
- The model can be extended (a three-model model, parameters in (21.6)), but it already covers outliers and conventional hypothesis testing (p. 626).

## Toy example (ours, not from the text)
Data values are in {0, 1, 9}. Two candidate θ values, A and B, with equal prior. Good distribution: $G(0|A)=0.9$, $G(1|A)=0.1$, $G(9|A)=0$; $G(0|B)=0.1$, $G(1|B)=0.9$, $G(9|B)=0$. Bad distribution: uniform, $B(x)=1/3$. Take $u=0.9$ known (a point-mass $g(u)$, an exchangeable prior). Data: $x_1=1$, $x_2=9$ (9 is a pure outlier).

Expand (21.17) with $n=2$. Here $L=G(1)G(9)=0$ and $L_1=G(9)=0$, while $L_2=G(1|\theta)$. So
$\overline L=u(1-u)B(9)G(1|\theta)+(1-u)^2B(1)B(9)=0.09\cdot\tfrac13G(1|\theta)+0.01\cdot\tfrac19=0.03\,G(1|\theta)+0.001111$.

- θ=A: $0.03(0.1)+0.001111=0.004111$.
- θ=B: $0.03(0.9)+0.001111=0.028111$.
- Sum $=0.032222$. Posterior: A $=0.1276$, B $=0.8724$.

Discarding 9 outright gives A = 0.1, B = 0.9. The mixture result is close but hedges slightly. The constant term is the "both bad" contribution. A model with $u=1$ would give $G(1|\theta)G(9|\theta)=0$ for both θ, so no posterior at all. This is the dogmatic-model failure of Sec. 21.7.

## Concepts
- [[outlier-two-model-mixture]] (new) — each datum comes from good G(x|θ) or bad B(x|η), mixed with weight u (pp. 619–620)
- [[quasi-likelihood]] (new) — likelihood for θ averaged over nuisance (η, u); a prior-weighted sum over good/bad labellings (pp. 622–624)
- [[exchangeability]] — good/bad label probabilities depend only on counts, so a de Finetti mixture in u applies (p. 620)
- [[robust-resistant-estimation]] (new) — insensitivity to the error model, or to large errors in a few data; Jaynes says it costs performance (pp. 617–618)
- [[nuisance-parameter]] (new) — a parameter (here η, u) integrated out when estimating θ (p. 621)
- [[likelihood]] — product of mixture densities (21.12); leave-out versions $L_j$ are good-data likelihoods (pp. 622–623)
- [[posterior-distribution]] — marginal posterior for θ computed by (21.15) (p. 622)
- [[prior-distribution]] — prior information about the apparatus is, for Jaynes, the crucial factor in judging reject vs keep (p. 616); in the model it enters through the prior for u (p. 620)
- [[coxs-theorem]] — Jaynes cites it to say a consistent normative inference theory is Bayesian (p. 619)

## Canonical instances
- [[chauvenet-criterion]] — an ad hoc rejection rule that ignores prior information (p. 616)
- [[sample-median-vs-mean]] — the median is "robust" but discards information (p. 618)
- [[receding-datum-gaussian]] — with the G-only model, one datum 100σ away pulls the estimate about 10σ (p. 625)
- [[binary-hypothesis-test-as-special-case]] — prior on u concentrated at 0 and 1 (p. 621)
- [[crime-detection-analogy]] — the more efficient city looks worse; errors undetected are uncriticised (p. 626)

## Bridges (candidates)
- [same-math] Quasi-likelihood mixture over good/bad labels ↔ bayesian: marginal likelihood averaged over a latent discrete variable — the sum over labellings is a marginalisation.
- [same-math] Mixture model $uG+(1-u)B$ with latent q_i ↔ bayesian: hierarchical model with exchangeable latent indicators (de Finetti).
- [structural-analogy] Robustness–accuracy trade-off ↔ information-theory: minimax/universal coding — performance is traded across a model class.
- [metaphor] Model dogmatism ($u=1$) ↔ bayesian: prior with zero probability on alternatives (Sec. 4.4 multiple hypotheses).

## Questions this raises
- With G Gaussian and B a broad distribution, how does the posterior mean for θ change as one datum recedes, and does it match redescending psi functions quantitatively? (The text promises this but these pages stop at 21.7.)
- How sensitive are conclusions to the prior g(u), and to the choice of B?
- When would $C_{jk}(\theta)$ actually depend on θ, so that outliers carry information about θ?
- Jaynes says robust methods "approximate" the Bayesian analysis. What measure of performance would test that?

## Exercises worth doing
- Ex. 21.1 (p. 617) — show any sampling distribution with a rounded top, $p(x|\theta)=a_0-a_1(x-\theta)^2+\cdots$, gives the mean as estimate when the data are closely clustered — difficulty: medium

## Reading notes
- Printed page = pdf − 30. The unit as given ends at 21.7 (p. 626). The text layer drops several math symbols (e.g. summation and integral signs, the bar over $L$ in (21.15)–(21.24), $\ne$ in (21.18), $\ll$); equations here were transcribed from the page images.
- Minor typos in the source: "that you entitled" (p. 615). In (21.21) the source prints $h(\eta,u|\theta I)$ without the comma used elsewhere, e.g. $h(\eta,u|\theta,I)$ in (21.14).
- On p. 624, "scanning (21.24)" and on p. 625 "every likelihood in (21.24)" appear to mean the expansion (21.17), which comes before it; this reading is my inference.
- Jaynes's characterisations of Huber, Tukey and Mosteller are his own, not neutral summaries.

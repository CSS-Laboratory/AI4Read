---
id: stone-2022-information/appf-rules
work: stone-2022-information
unit: Appendices F–H (The Rules of Probability; The Gaussian Distribution; Key Equations)
pages: 259–266
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Appendices F–H: Probability rules, the Gaussian, and key equations

## L0 — One line
Joint probabilities of independent outcomes multiply, and the product, sum and Bayes rules, the Gaussian density and a list of the book's key entropy equations are collected in these appendices.

## L1 — The gist (≤ 120 words)
These appendices collect basic probability rules, the Gaussian distribution and a list of the book's key equations. Appendix F illustrates the multiplication rule for independent outcomes with a coin-flip count (p(h) = 0.9), then states conditional probability, the product rule, the sum rule (marginalisation) and Bayes' rule. Appendix G describes the Gaussian density, its parameters, the central limit theorem and the cumulative distribution function. Appendix H lists the book's key equations: entropy, joint and conditional entropy, the chain rule, mutual information, channel capacity (including the Gaussian case), marginalisation, the rate distortion function and transfer entropy. They serve as reference material.

**Prerequisites:** percentages and averages; sums and integrals as notation; logarithms; the idea of a random variable.

## L2 — Key ideas
- For independent outcomes, the joint probability is the product of the individual probabilities; a counting example with 100 pairs of flips illustrates this (p. 259–261).
- Conditional probability is p(x|y) = p(x,y)/p(y); multiplying through by p(y) gives the product rule (p. 261).
- Summing (or integrating) a joint distribution over one variable gives the marginal distribution of the other (p. 261–262).
- Bayes' rule follows from writing p(x,y) in both orders and dividing by p(x); it names the posterior, likelihood, prior and marginal likelihood (p. 262).
- The Gaussian density has a peak at the mean µ, and σ sets its spread. The central limit theorem (sample means from almost any distribution become increasingly Gaussian as the sample size grows) may account for why it is so common (p. 263–264).
- The Gaussian cumulative distribution function (cdf) Φ(x) is the probability that a randomly chosen Gaussian value is less than or equal to x (p. 264).
- The key-equation sheet gives the chain rule and several equal forms of mutual information (p. 265–266).
- It also gives the channel capacity $C=\tfrac12\log(1+P/N)$ for iid Gaussian input and noise, the rate distortion function (the smallest rate needed to represent $X$ as a distorted version at a given distortion level) and transfer entropy (the information past values of $X$ give about the current $Y$ beyond what the past of $Y$ gives) (p. 266).

## L3 — Walkthrough

### Appendix F — The Rules of Probability

**Independent outcomes (p. 259–261).** If outcomes are independent, the probability of the outcome set is the product of the individual probabilities (p. 259). Example: a coin with $p(x_h)=0.9$ and $p(x_t)=1-0.9=0.1$, flipped twice. Four ordered pairs are possible. A joint probability such as $p(x_h,x_t)$ is the probability of "head first, tail second" (p. 259).

Imagine 100 pairs of flips. Table F.1 (p. 259), where round brackets mean ordered and curly brackets mean unordered:

| Outcome | h | t | {h,h} | {t,t} | (h,t) | (t,h) | {t,h} |
|---|---|---|---|---|---|---|---|
| N | 90 | 10 | 81 | 1 | 9 | 9 | 18 |
| N/100 | 0.90 | 0.10 | 0.81 | 0.01 | 0.09 | 0.09 | 0.18 |

The author's counting, on average (p. 260):
- Heads among 100 first flips: $90 = 0.9\times100$ (F.1).
- The second flip does not depend on the first, so of these 90 about $81 = 0.9\times 90$ are heads (F.2).
- Substituting F.1: $81 = 0.9\times(0.9\times100)=0.81\times100$ (F.3). So $p(x_h)^2=0.9^2=0.81$.
- Two tails: $1=0.1\times10$ of 100 pairs (p. 260).
- $(x_h,x_t)$: $9=0.1\times 90$ of 100 pairs, i.e. $(0.1\times0.9)\times100=p(x_h)p(x_t)\times100$ (p. 260–261).
- $(x_t,x_h)$ also gives 9 (p. 260–261). Head and tail in either order: $18=9+9$ (p. 261).

The three unordered probabilities, 0.81, 0.01 and 0.18, sum to one. Each pair's probability is the product of its single-flip probabilities (p. 261).

*Intuition note:* Take a fraction of a fraction. If 90% of first flips are heads and 90% of those are followed by heads, then 81% of pairs are two heads. This works because the second flip ignores the first.

**Conditional probability (p. 261).**
$$p(x|y)=p(x,y)/p(y)\tag{F.4}$$
"|" is read "given that".

**Product rule (p. 261).**
$$p(x,y)=p(x|y)p(y)\tag{F.5}$$

**Sum rule / marginalisation (p. 261–262).** The sum rule is also called the law of total probability. For a discrete variable:
$$p(x)=\sum_i p(x,y_i)\tag{F.6}$$
Applying the product rule:
$$p(x)=\sum_i p(x|y_i)p(y_i)\tag{F.7}$$
For a continuous variable (p. 262):
$$p(x)=\int_y p(x,y)\,dy=\int_y p(x|y)p(y)\,dy\tag{F.8}$$
This is marginalisation. It gives the marginal probability $p(x)$ of the joint distribution $p(X,Y)$ at $X=x$ (p. 262).

**Bayes' rule (p. 262).** Swapping $x$ and $y$ in F.5, with $p(y,x)=p(x,y)$:
$$p(y,x)=p(y|x)p(x)\tag{F.9}$$
$$p(y|x)p(x)=p(x|y)p(y)\tag{F.10}$$
Dividing by $p(x)$:
$$p(y|x)=\frac{p(x|y)p(y)}{p(x)}\tag{F.11}$$
In the Bayesian framework, $p(y|x)$ is the posterior, $p(x|y)$ the likelihood, $p(y)$ the prior and $p(x)$ the marginal likelihood. The rule holds for every individual value, so it holds for distributions (p. 262):
$$p(Y|X)=\frac{p(X|Y)p(Y)}{p(X)}\tag{F.12}$$
Here $p(Y|X)$ is a family of posterior distributions (one per value of $x$), $p(X|Y)$ the corresponding family of likelihood functions, $p(X)$ the marginal likelihood distribution and $p(Y)$ the prior distribution (p. 262).

*Intuition note:* The joint probability can be factored in two orders, and Bayes' rule just equates them. It turns "how likely is the data given the cause" into "how likely is the cause given the data".

### Appendix G — The Gaussian Distribution

**Definition (p. 263).** The Gaussian (normal, bell-curve) pdf with mean $\mu$ and standard deviation $\sigma$ is
$$p(x)=k\,e^{-(x-\mu)^2/(2\sigma^2)}\tag{G.1}$$
with $e=2.718$ and $k=1/(\sigma\sqrt{2\pi})$, which makes the area under the curve equal one. Define (minus) the exponent as
$$z=\frac12\left(\frac{x-\mu}{\sigma}\right)^2\tag{G.2}$$
so $p(x)=k\,e^{-z}$, and $p(x)$ gets larger as $z$ gets smaller (p. 263).

**Behaviour (p. 263).** At $x=\mu$, $z=0$ and $p(x)=k$, its biggest value. As $x$ moves away from $\mu$, $z$ grows and $p(x)$ falls. Changing $\mu$ moves the curve along the $x$-axis. Increasing $\sigma$ rescales $(x-\mu)$ and so increases the spread.

**Central limit theorem (p. 264).** In essence, as the sample size $n$ grows, the distribution of sample means from almost any distribution becomes increasingly Gaussian. The author notes that almost every physical quantity (e.g. human height) is affected by multiple factors, so it is effectively a weighted mean. This suggests such quantities should be Gaussian, and "may account" for the ubiquity of the Gaussian in nature.

**Cumulative distribution function (p. 264).**
$$\Phi(x)=\frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{x}e^{-(t-\mu)^2/(2\sigma^2)}\,dt\tag{G.3}$$
For a given $x$, $\Phi(x)$ is the probability that a random Gaussian value is less than or equal to $x$. Figure G.1 shows the pdf and cdf for $\mu=0$, $\sigma=1$ (p. 264).

*Intuition note:* The exponent $z$ is half the square of the distance of $x$ from the mean, measured in standard deviations. The larger $z$ is, the smaller the density. The cdf is the area accumulated up to $x$.

### Appendix H — Key Equations (p. 265–266)
The page lists these equations without derivation. The logarithm base is not stated on these pages.

- **Entropy:** $H(X)=\sum_{i=1}^m p(x_i)\log\frac1{p(x_i)}$ (H.1); $H(X)=\int_x p(x)\log\frac1{p(x)}dx$ (H.2).
- **Joint entropy:** $H(X,Y)=\sum_{i=1}^m\sum_{j=1}^m p(x_i,y_j)\log\frac1{p(x_i,y_j)}$ (H.3); the double-integral form is (H.4). Also $H(X,Y)=I(X,Y)+H(X|Y)+H(Y|X)$ (H.5).
- **Conditional entropy:** $H(Y|X)=\sum_i\sum_j p(x_i,y_j)\log\frac1{p(y_j|x_i)}$ (H.6); $H(X|Y)=\sum_i\sum_j p(x_i,y_j)\log\frac1{p(x_i|y_j)}$ (H.7); the integral forms are (H.8)–(H.9). $H(X|Y)=H(X,Y)-H(Y)$ (H.10); $H(Y|X)=H(X,Y)-H(X)$ (H.11).
- **Chain rule for entropy:** $H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)$ (H.12).
- **Mutual information:** $I(X,Y)=\sum_i\sum_j p(x_i,y_j)\log\frac{p(x_i,y_j)}{p(x_i)p(y_j)}$ (H.13); the integral form is (H.14). Equal forms: $H(X)+H(Y)-H(X,Y)$ (H.15) $=H(X)-H(X|Y)$ (H.16) $=H(Y)-H(Y|X)$ (H.17) $=H(X,Y)-[H(X|Y)+H(Y|X)]$ (H.18).
- **Channel capacity:** $C=\max_{p(X)}I(X,Y)$ bits (H.19). If the input $X$ has variance $P$, the noise $\eta$ has variance $N$, and both are iid Gaussian, then $I(X,Y)=C$ with
$$C=\frac12\log\left(1+\frac PN\right)\text{ bits}\tag{H.20}$$
where $P/N$ is the signal to noise ratio.
- **Marginalisation:** $p(x_i)=\sum_{j=1}^m p(x_i,y_j)$, $p(y_j)=\sum_{i=1}^m p(x_i,y_j)$ (H.21); integrals over $y$ and $x$ in (H.22).
- **Rate distortion:** $R(D)$ is the smallest rate that must be allocated to represent $X$ as a distorted version $\hat X$ at distortion level $D$:
$$R(D)=\min_{p(\hat x|x):\,\mathrm{E}[d(x,\hat x)]\le D} I(X;\hat X)\text{ bits}\tag{H.23}$$
- **Transfer entropy:** the average information that past values $x_{\text{past}}$ give about $y_t$, over and above what $y_{\text{past}}$ gives:
$$T_{x_{\text{past}}\to y_t}=I(y_t;y_{\text{past}},x_{\text{past}})-I(y_t,y_{\text{past}})\text{ bits}\tag{H.24}$$

*Intuition note:* Every form of mutual information measures the same overlap between the uncertainties of $X$ and $Y$. The Gaussian capacity formula says reliable bits per use grow only as the logarithm of the signal-to-noise ratio.

## Toy example (ours, not from the text)
Two coins, equally likely to be picked (prior $p(\text{fair})=p(\text{biased})=0.5$). The fair coin has $p(h)=0.5$; the biased coin has $p(h)=0.9$. We observe one head.
- Sum rule (F.7): $p(h)=0.5\times0.5+0.9\times0.5=0.25+0.45=0.70$.
- Bayes (F.11): $p(\text{biased}|h)=\frac{0.9\times0.5}{0.70}=\frac{0.45}{0.70}\approx0.643$.
- $p(\text{fair}|h)=\frac{0.25}{0.70}\approx0.357$. The two posteriors sum to $1$.
- Multiplication rule for two independent heads from the biased coin: $0.9\times0.9=0.81$, as in the appendix.

## Concepts
- [[independence]] (new) — outcomes whose joint probability is the product of individual probabilities (p. 259)
- [[conditional-probability]] (new) — $p(x|y)=p(x,y)/p(y)$ (p. 261)
- [[product-rule]] (new) — $p(x,y)=p(x|y)p(y)$ (p. 261)
- [[marginalisation]] (new) — summing or integrating a joint distribution over one variable (p. 261–262)
- [[bayes-rule]] (new) — posterior = likelihood × prior / marginal likelihood (p. 262)
- [[gaussian-distribution]] (new) — bell-curve pdf set by mean µ and standard deviation σ (p. 263)
- [[central-limit-theorem]] (new) — sample means from almost any distribution become increasingly Gaussian as $n$ grows (p. 264)
- [[entropy H(X)]] — $\sum p\log(1/p)$, or its integral form (p. 265)
- [[joint and conditional entropy]] — H.3–H.11 (p. 265)
- [[chain rule]] — $H(X,Y)=H(X)+H(Y|X)$ (p. 265)
- [[mutual information I(X;Y)]] — H.13–H.18 (p. 266)
- [[channel capacity]] — $\max_{p(X)}I(X,Y)$ (p. 266)
- [[Shannon–Hartley formula]] — here only the form $C=\frac12\log(1+P/N)$ with iid Gaussian input and noise; no bandwidth term appears on these pages (p. 266)
- [[rate–distortion function]] — H.23 (p. 266)
- [[transfer entropy]] — H.24 (p. 266)

## Canonical instances
- [[biased-coin-pairs]] — 100 pairs of flips with $p(h)=0.9$ show that independent joint probabilities multiply (p. 259–261)
- [[gaussian-pdf-and-cdf-figure]] — Figure G.1, $\mu=0$, $\sigma=1$ (p. 264)

## Bridges (candidates)
- [structural-analogy] Marginalisation (H.21) ↔ entropy: marginals $p(x_i)$ from the joint give $H(X)$ from $p(X,Y)$.
- [structural-analogy] Bayes' rule (prior → posterior) ↔ statistics: updating beliefs after data.
- [metaphor] CLT "many small factors" ↔ social science: aggregate outcomes as weighted means of many influences.

## Questions this raises
- What exactly does "independent" require beyond the coin example, and how does it show up in $I(X,Y)$?
- Why does the Gaussian give the capacity formula H.20 in particular?
- What assumptions on the "almost any distribution" does the CLT need?
- How is transfer entropy (H.24) estimated from data?

## Reading notes
- Printed = pdf − 16.
- Misprint on p. 260: the text for the pair $(x_t,x_h)$ says "10 heads in the set of 100 first flips" and "$9=0.1\times90$ of the corresponding nine second flips to yield a tail". This is garbled. The count only works as 10 *tails* first, then $9=0.9\times10$ heads second. I used the table values (9) only. A typo, "does not depend on of the outcome", is on p. 260.
- Footnote marks 73 (Bayes' rule) and 15 (CLT) point to a reference list not in these pages.
- Appendix H notation varies between $I(X,Y)$ and $I(X;\hat X)$ as printed. The logarithm base is not stated on these pages.

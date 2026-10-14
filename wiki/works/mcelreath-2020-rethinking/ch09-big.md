---
id: mcelreath-2020-rethinking/ch09-big
work: mcelreath-2020-rethinking
unit: Chapter 9. Big Entropy and the Generalized Linear Model
pages: 267-289
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Big Entropy and the Generalized Linear Model

## L0 — One line
When choosing a likelihood (or prior), bet on the distribution with the biggest entropy that fits what you know, then attach linear models to its parameters through link functions.

## L1 — The gist (≤ 120 words)
The chapter asks how to choose probability distributions, for likelihoods and priors, when convention is not enough. Answer: choose the distribution with maximum information entropy (a measure of how many ways a distribution can arise) among those consistent with stated constraints, because it can arise in the most ways and adds the fewest extra assumptions. The Gaussian and binomial are derived as maximum entropy solutions under different constraints. Generalized linear models attach a linear model to a likelihood parameter of such a distribution, through a link function (logit or log) that keeps the parameter in its allowed range. This matters because link functions make predictor effects non-constant and make parameters hard to read alone.

**Prerequisites:** logarithms and factorials (counting arrangements); information entropy and KL divergence (Chapter 6); Gaussian and binomial likelihoods; linear regression; a first derivative.

## L2 — Key ideas (5–10 bullets)
- Entropy is a way of counting: the distribution that can be realized in the most ways has the biggest entropy, and it is the most conservative one that obeys its constraints (pp. 269–271).
- The Wallis derivation shows that (1/N) log of the multiplicity approaches Shannon entropy, with no appeal to "information" (p. 272).
- The Gaussian has maximum entropy among continuous distributions on the real line with a given variance (pp. 273–275).
- The binomial has maximum entropy when only two unordered outcomes exist and the expected value is constant; this matches the counting derivation of Chapter 2 (pp. 275–279).
- A GLM puts a linear model on a likelihood parameter. The likelihood is chosen by maximum entropy, and a link function maps the linear model onto the parameter's range (pp. 280–281, 284).
- Logit and log links are the two common choices. They make the effect of any predictor depend on its current value, so every predictor "interacts with itself" (pp. 284–287).
- A coefficient alone does not give the size of an effect on the outcome. Compare models with information criteria only if they share the same type of likelihood (p. 288).
- Maximum entropy can also be used to build priors that carry background knowledge while assuming as little else as possible (pp. 288–289).

## L3 — Walkthrough

### Introduction (pp. 267–268)
- Tangled cords are the opening image. There are vastly more ways for cords to be knotted than untied, so we "bet on entropy" without knowing the physics (p. 267).
- Models force us to choose distributions: a prior for each parameter and a likelihood for the data. Conventional choices (wide Gaussian priors, Gaussian likelihood) work well in many cases but are often not the best (p. 267).
- **Principle:** bet on the distribution with the biggest entropy. Three justifications are given (pp. 267–268):
  1. It is the widest, least informative distribution consistent with what we think we know. For a likelihood it is the distribution we get by counting the ways outcomes can arise under the constraints.
  2. Nature tends to produce high-entropy empirical distributions. Processes that repeatedly add fluctuations tend toward the Gaussian shape, which holds no information about the process except location and variance. Other processes give other maximum entropy distributions.
  3. Historical: it tends to work. There is no guarantee in the large world, but no approach has one.
- A **generalized linear model (GLM)** replaces a parameter of a likelihood with a linear model. The likelihood need not be Gaussian, and linear models can attach to any or all of its shape parameters (p. 268).
- Maximum entropy recovers the most common likelihoods and gives a rationale for choosing among them (p. 268).
- **Rethinking (Bayesian updating):** the author states that the posterior has the greatest entropy relative to the prior (smallest cross entropy) among distributions consistent with the constraints and data (p. 268).

### 9.1 Maximum entropy (pp. 268–275)
**Information entropy.** From Chapter 6, the unique measure of uncertainty meeting three criteria (continuous, grows with the number of events, additive) is
$$H(p) = -\sum_i p_i \log p_i .$$
It is the average log-probability, with the sign flipped (p. 268).

**Principle (author's plain statement):** the distribution that can happen the most ways is also the one with the biggest entropy. It is the most conservative distribution that obeys its constraints (p. 269).

**Pebbles in buckets (pp. 269–271).**
- Setup: 10 numbered pebbles are tossed so each is equally likely to land in any of 5 buckets. Every particular arrangement is equally likely. But "distributions of pebbles" (counts per bucket) differ in how many arrangements produce them (p. 269).
- Counts of arrangements (Fig. 9.1) and entropies computed in R (code 9.1–9.3) (pp. 269–270):

| Plot | Pebbles per bucket | Ways | Entropy H |
|---|---|---|---|
| A | 0,0,10,0,0 | 1 | 0.0000000 |
| B | 0,1,8,1,0 | 90 | 0.6390319 |
| C | 0,2,6,2,0 | 1260 | 0.9502705 |
| D | 1,2,4,2,1 | 37800 | 1.4708085 |
| E | 2,2,2,2,2 | 113400 | 1.6094379 |

- Dividing log(ways) by 10 gives log ways per pebble (code 9.4). Plotted against $H$ (Fig. 9.1, bottom right), the points lie close to a line. Entropy approximates log ways per pebble, and the approximation improves with more pebbles; it is already very good at 10 (pp. 270–271).
- The number of ways for the maximum entropy distribution eclipses that of any other. Distributions near it also eclipse less similar ones. So it is "the center of gravity for the highly plausible distributions" (p. 271).
- Its plausibility is conditional on the assumptions (constraints and data) (p. 271).
- The author derives two examples (Gaussian, binomial) graphically, not rigorously. Intuition comes with experience, and the principle can be used before it is fully understood (p. 271).
- **Rethinking (intuition):** intuition only guides method development. What justifies information entropy is that it has worked on many problems, not the three criteria used to derive it (p. 271).

> **Intuition note.** Think of entropy as a count of arrangements, on a log scale. The flattest distribution allowed by your constraints is the one that the most arrangements produce. So betting on it is betting on the largest pile of possibilities.

**Overthinking: the Wallis derivation (pp. 271–272).**
- Setup: $M$ buckets, $N$ stones tossed uniformly at random. Keep the candidate $p_i = n_i/N$ only if it meets the constraints. The most frequently occurring candidate is the "fairest" one that still obeys them (p. 271).
- Its probability is multinomial, with $W$ the multiplicity (the number of ways a set of counts can be realized):
$$\Pr(n_1,\dots,n_M)=\frac{N!}{n_1!\cdots n_M!}\prod_{i=1}^{M}\left(\frac1M\right)^{n_i}=\frac{N!}{n_1!\cdots n_M!}\left(\frac1M\right)^{N}=W\left(\frac1M\right)^{N}$$
- Maximizing $W$ is the same as maximizing $\frac1N\log W$. With $n_i = Np_i$:
$$\frac1N\log W=\frac1N\Big(\log N!-\sum_i\log[(Np_i)!]\Big)$$
- For large $N$, use Stirling's approximation $\log N!\approx N\log N-N$:
$$\frac1N\log W\approx\frac1N\Big(N\log N-N-\sum_i\big(Np_i\log(Np_i)-Np_i\big)\Big)=-\sum_i p_i\log p_i$$
- This is Shannon's entropy. Among distributions satisfying the constraints, the maximizer spreads probability as evenly as possible (p. 272).
- **Generalization:** if the prior chance of landing in bucket $i$ is $q_i$, the quantity to maximize is
$$\frac1N\log\Pr(n_1,\dots,n_M)\approx-\sum_i p_i\log(p_i/q_i)$$
This is negative KL divergence. So maximum entropy also minimizes the distance from the prior, among distributions consistent with the constraints. The author calls this minimum cross-entropy. Bayesian updating can be expressed as a maximum entropy problem in which the data are constraints (p. 272).

#### 9.1.1 Gaussian (pp. 272–275)
- Chapter 4's random walk (1000 people flipping coins) gives a Gaussian from adding many small factors. Unbalanced outcomes are possible, but vastly more flip sequences give an approximately balanced outcome. The bell curve appears because so many detailed states produce it (pp. 272–273).
- So if all you know about continuous values is their variance (or that it is finite), the safest bet is one of these bell-shaped configurations (p. 273).
- **Generalized normal density** (a family with shape parameter $\beta$), used to compare distributions of equal variance (p. 273):
$$\Pr(y\mid\mu,\alpha,\beta)=\frac{\beta}{2\alpha\Gamma(1/\beta)}\,e^{-\left(\frac{|y-\mu|}{\alpha}\right)^{\beta}}$$
- Fig. 9.2 (left) shows a Gaussian and three generalized normals, all with variance $\sigma^2=1$. Two are more peaked with thicker tails. One is thicker in the middle with thinner tails (pp. 273–274).
- Fig. 9.2 (right): the generalized normal is exactly Gaussian at $\beta=2$, and entropy is maximized exactly there. The author says the result is not limited to symmetric families; even in skewed generalized families the bell curve has maximum entropy (p. 274).
- Why: entropy rises as a distribution gets flatter, so moving mass to the tails would raise it. But a perfectly uniform distribution would have infinite variance. The variance constraint forces most probability into a small area around the mean. The Gaussian is as spread out as possible given fixed variance (p. 274).
- **Take-home:** if you assume only a finite variance, the Gaussian is the most conservative distribution. If you are comfortable assuming more, and the assumptions are good, maximum entropy leads to other distributions (p. 274).

**Overthinking: proof of Gaussian maximum entropy (pp. 274–275).** Let $p(x)=(2\pi\sigma^2)^{-1/2}\exp(-(x-\mu)^2/(2\sigma^2))$ and let $q(x)$ be any density with variance $\sigma^2$, both on the whole real line. The mean does not matter, since entropy does not depend on location.
1. $H(p)=-\int p\log p\,dx=\tfrac12\log(2\pi e\sigma^2)$ (p. 274).
2. KL divergence (author's notation: $H(q)=-\int q\log q\,dx$ and $H(q,p)=\int q\log p\,dx$, with no minus sign):
$$D_{KL}(q,p)=\int_{-\infty}^{\infty}q(x)\log\frac{q(x)}{p(x)}dx=-H(q,p)-H(q)$$
3. $D_{KL}\ge0$, so $-H(q,p)\ge H(q)$ (p. 274).
4. $H(q,p)$ is an average over $x$:
$$H(q,p)=\mathrm E\log\Big[(2\pi\sigma^2)^{-1/2}\exp\Big(-\frac{(x-\mu)^2}{2\sigma^2}\Big)\Big]=-\tfrac12\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\mathrm E\big((x-\mu)^2\big)$$
5. The last expectation is the variance, constrained to $\sigma^2$ (p. 275):
$$H(q,p)=-\tfrac12\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sigma^2=-\tfrac12\big(\log(2\pi\sigma^2)+1\big)=-\tfrac12\log(2\pi e\sigma^2)$$
6. This equals $-H(p)$. From $-H(q,p)\ge H(q)$ it follows that $H(p)\ge H(q)$ (p. 275).

> **Intuition note.** The proof compares any rival density $q$ to the Gaussian $p$ by KL divergence, which can never be negative. The variance constraint fixes how much "spread" $q$ is allowed. Spread is what entropy rewards, so no $q$ can beat the Gaussian.

#### 9.1.2 Binomial (pp. 275–280)
- Binomial: with two possible events and constant chance $p$ over $n$ trials, the probability of $y$ events of type 1 is
$$\Pr(y\mid n,p)=\frac{n!}{y!(n-y)!}p^y(1-p)^{n-y}$$
The factorial fraction counts ordered sequences with count $y$. The probability of one unique sequence is $\Pr(y_1,\dots,y_n\mid n,p)=p^y(1-p)^{n-y}$ (p. 275).
- Claim to show: the binomial has maximum entropy among distributions with (1) only two unordered events and (2) constant expected value (p. 275).

**Example 1 (p. 275–276).**
- Draw 2 marbles with replacement. The sequences are ww, bw, wb, bb. The expected number of blue is exactly 1.
- Candidates (Fig. 9.3):

| Dist. | ww | bw | wb | bb |
|---|---|---|---|---|
| A | 1/4 | 1/4 | 1/4 | 1/4 |
| B | 2/6 | 1/6 | 1/6 | 2/6 |
| C | 1/6 | 2/6 | 2/6 | 1/6 |
| D | 1/8 | 4/8 | 2/8 | 1/8 |

- A is binomial with $n=2$, $p=0.5$: $\Pr(ww)=(1-p)^2$, $\Pr(bw)=p(1-p)$, $\Pr(wb)=(1-p)p$, $\Pr(bb)=p^2$ (p. 276).
- All four have expected value 1 (code 9.5). Entropies (code 9.6): A 1.386294, B 1.329661, C 1.329661, D 1.213008. A is flat and cannot be flatter, so it has the largest entropy (p. 276).

**Example 2 (pp. 277–278).**
- Example 1 is special because a flat distribution fits the constraint. Now require expected value 1.4 blue in two draws, i.e. $p=0.7$. The binomial is $\{0.09,0.21,0.21,0.49\}$ (code 9.7) with entropy 1.221729 (code 9.8) (p. 277).
- The author simulates 100000 random distributions with expected value 1.4 (function `sim.p`, code 9.9–9.10). Fig. 9.4 shows the distribution of their entropies. The maximum observed entropy is 1.221728 (code 9.12), almost the same as the binomial's. Its distribution is $\{0.0898, 0.2104, 0.2099, 0.4898\}$ (code 9.13) (p. 278).
- Lower entropy goes with less even distributions (A to D in Fig. 9.4). The author states that among the infinitely many distributions with this expected value, only the binomial has the greatest entropy (p. 278).

**Three lessons (pp. 278–279).**
1. With two unordered outcomes and constant expected counts, the binomial is the most conservative distribution.
2. If the expected value is unknown, the same logic gives a binomial with unknown $np$, to be estimated (Chapter 10). The binomial plays for such outcomes the role the Gaussian plays for continuous outcomes with finite variance. Other constraints give other maximum entropy distributions.
3. The Chapter 2 "garden of forking data" counted ways a sequence can arise and gave the same likelihoods. Entropy maximization is "abbreviated counting" that maps constraints to distributions. There is no guarantee the result is best for the real problem. But no other distribution reflects the assumptions more conservatively. Any other distribution implies hidden "phantom assumptions" (p. 279).

**Rethinking: conditional independence (p. 279).** The distributions do not require observations to be uncorrelated in general. They require independence after accounting for predictors, a modeling assumption. It fails if one observed event directly causes the next (the author's example: buying a Nick Cave album because someone else did).

**Overthinking: binomial maximum entropy (p. 280).** This extends the Gaussian proof and also yields the defining constraint.
1. $p$ is the binomial over sequences. $p_i$ is the probability of a sequence $i$ with $x_i$ successes and $n-x_i$ failures. $q$ is another distribution on the same sequences. KL gives
$$-H(q,p)\ge H(q)\implies-\sum_i q_i\log p_i\ge-\sum_i q_i\log q_i$$
2. Let $\lambda=\sum_i p_ix_i$. Then
$$-H(q,p)=-\sum_i q_i\log\Big[\Big(\frac\lambda n\Big)^{x_i}\Big(1-\frac\lambda n\Big)^{n-x_i}\Big]=-\sum_i q_i\Big(x_i\log\Big[\frac\lambda n\Big]+(n-x_i)\log\Big[1-\frac\lambda n\Big]\Big)$$
3. After some algebra:
$$-H(q,p)=-\sum_i q_i\Big(x_i\log\Big[\frac{\lambda}{n-\lambda}\Big]+n\log\Big[\frac{n-\lambda}{n}\Big]\Big)=-n\log\Big[\frac{n-\lambda}{n}\Big]-\log\Big[\frac{\lambda}{n-\lambda}\Big]\underbrace{\sum_i q_ix_i}_{\bar q}$$
4. $\bar q$ is the expected value of $q$, and no other term depends on $q_i$. So expected value is the constraint that defines the class for which the binomial is the maximum entropy distribution (p. 280).
5. The author then says that setting $\bar q=\lambda$ gives $H(q)=H(p)$, and for any other expected value $H(p)>H(q)$ (p. 280). (See Reading notes on this step.)
6. $\log[\lambda/(n-\lambda)]$ is the log of the odds of success (expected successes over expected failures), the "log odds". It features in Chapter 11 binomial models (p. 280).

### 9.2 Generalized linear models (pp. 280–288)
- Earlier Gaussian models: $y_i\sim\text{Normal}(\mu_i,\sigma)$, $\mu_i=\alpha+\beta x_i$. For a continuous outcome far from any bound, this has maximum entropy (p. 280).
- For discrete or bounded outcomes (e.g. counts) a Gaussian likelihood is not the most powerful choice. It cannot be trusted for sensible predictions, since it would predict negative counts when the mean is near zero (p. 280).
- **GLM form:** use all prior knowledge of the outcome's constraints to choose a maximum entropy distribution, then replace a shape parameter with a linear model (p. 281):
$$y_i\sim\text{Binomial}(n,p_i),\qquad f(p_i)=\alpha+\beta x_i$$
- Two changes from the Gaussian model. The first is principled: the maximum entropy likelihood (binomial for counts from $n$ trials with constant expected value $np$). The second is an "epicycle", a modeling trick that works descriptively, not causally: the **link function** $f$ (p. 281).
- Why a link is needed: rarely is there a parameter $\mu$ for the mean, and parameters are rarely unbounded in both directions. The binomial's mean $np$ depends on both parameters. $n$ is usually known, so the linear model attaches to $p$. But $p\in[0,1]$, and $\alpha+\beta x_i$ can leave that range (Fig. 9.5) (p. 281).
- **Rethinking: Histomancy (p. 282).** Choosing a likelihood by inspecting the histogram of the outcome is called "Histomancy". The author calls it a false god. At most, a Gaussian likelihood assumes that the residuals look Gaussian, not the aggregate outcome. Combined male and female weights are not Gaussian but may be a mixture of Gaussians. Likewise, at most a Poisson likelihood assumes variance equals mean after conditioning on predictors. Hence the need for principles.

#### 9.2.1 Meet the family (pp. 282–284)
- The **exponential family** contains the common modeling distributions. The author says every member is a maximum entropy distribution for some set of constraints. Other statistical traditions use the same distributions with other justifications (p. 282).
- Fig. 9.6 shows the gamma, normal, binomial, Poisson and exponential. Gray arrows mark generative relationships: exponential →(sum)→ gamma; gamma →(large mean)→ normal; exponential →(count events)→ binomial; exponential →(count events, low rate)→ Poisson; binomial →(low probability, many trials)→ Poisson (p. 283, figure). You need not know these to use the distributions (p. 282).
- **Exponential:** non-negative; for distance and duration. If an event's probability is constant in time or space, the distribution of events tends toward exponential. Maximum entropy among non-negative continuous distributions with the same average displacement. One parameter: rate $\lambda$, or average displacement $\lambda^{-1}$ (p. 282).
- **Gamma:** non-negative; unlike the exponential it can peak above zero. Arises if an event needs two or more exponentially distributed events first (the author's example: age of cancer onset, approximately gamma). Maximum entropy among distributions with the same mean and the same average logarithm. Two parameters, with at least three common parameterizations, so care is needed (p. 283).
- **Poisson:** a count distribution; a special case of the binomial. With very large (usually unknown) $n$ and very small $p$, the binomial converges to a Poisson with rate $\lambda=np$. Used for counts that never approach a theoretical maximum. It has maximum entropy under exactly the same constraints as the binomial. One parameter, $\lambda$ (pp. 283–284).
- You need not memorize all exponential family members, and an outcome distribution need not belong to the family. If you have good reasons for another one, use it, but check its performance (p. 284).
- **Rethinking: a likelihood is a prior (p. 284).** Likelihoods are priors for the data, conditional on parameters. There is no correct likelihood, only better and worse ones by context. Useful inference does not require the data to be actually distributed as the likelihood, just as it does not require the posterior to resemble the prior.

#### 9.2.2 Linking linear models to distributions (pp. 284–287)
- For any outcome distribution (the author's joke example is "Zaphod"): $y_i\sim\text{Zaphod}(\theta_i,\phi)$, $f(\theta_i)=\alpha+\beta x_i$. A link function maps the linear space of $\alpha+\beta x_i$ onto the non-linear space of a parameter $\theta$ and prevents negative distances or probabilities above 1 (p. 284).
- **Logit link** (parameter is a probability mass in $[0,1]$):
$$y_i\sim\text{Binomial}(n,p_i),\quad \text{logit}(p_i)=\alpha+\beta x_i,\quad \text{logit}(p_i)=\log\frac{p_i}{1-p_i}$$
The odds are the probability the event happens divided by the probability it does not. Solving for $p_i$ gives the logistic (inverse-logit) (p. 285):
$$p_i=\frac{\exp(\alpha+\beta x_i)}{1+\exp(\alpha+\beta x_i)}$$
- Fig. 9.7: the log-odds scale is linear and unbounded. The logistic compresses it between 0 and 1, so equal steps on the log-odds scale give smaller and smaller changes in probability far from zero (p. 285).
- Example from Fig. 9.7: at $x=0$ the log-odds are 0. A half-unit increase in $x$ raises the probability by about 0.25. Each further half-unit raises it less. The author argues a good probability model must behave this way: an almost-guaranteed event cannot become much more probable (pp. 285–286).
- **Key lesson:** no GLM coefficient such as $\beta$ gives a constant change on the outcome scale. Every predictor effectively interacts with itself and with every other predictor, whether or not interactions are modeled. This makes visualizing counterfactual predictions more important (p. 286).
- **Log link** (parameter positive). The author's example models a Gaussian standard deviation: $y_i\sim\text{Normal}(\mu,\sigma_i)$, $\log(\sigma_i)=\alpha+\beta x_i$. The mean $\mu$ is constant. The inverse link is $\sigma_i=\exp(\alpha+\beta x_i)$ (p. 286).
- Fig. 9.8: a log link means exponential scaling of the outcome with the predictor. One unit on the log scale is an order of magnitude on the original scale (p. 287).
- Caution: an exponential relationship cannot continue forever, so predictions far outside the fitted range may fail. The author's examples: height versus weight, and hurricane damage versus wind speed, which may be capped when everything is destroyed (p. 287).
- **Rethinking: sensitivity analysis (p. 287).** Link functions are assumptions. If in doubt, explore how changing them (or likelihoods, linear models, priors, fitting) affects inference. The author says to report all results, whether or not conclusions change. This is the opposite of p-hacking, where many analyses are tried and only the significant one is reported.

**Overthinking: parameters interacting with themselves (p. 287).**
- Gaussian mean $\mu=\alpha+\beta x$ gives $\partial\mu/\partial x=\beta$, constant.
- For binomial $p=\exp(\alpha+\beta x)/(1+\exp(\alpha+\beta x))$, the derivative is
$$\frac{\partial p}{\partial x}=\frac{\beta}{2\big(1+\cosh(\alpha+\beta x)\big)}$$
It contains $x$, so the effect of a change in $x$ depends on $x$: an interaction with itself.

> **Intuition note.** A link function turns a straight-line model into a curve on the scale you care about. Because the curve bends, the same step in a predictor buys a different change in the outcome depending on where you stand. So a single coefficient is not "the effect".

#### 9.2.3 Absolute and relative differences (p. 288)
- Each parameter is a relative difference on the linear-model scale, ignoring other parameters. We usually care about absolute differences in outcomes, which involve all parameters. A big beta-coefficient may not mean a big effect on the outcome (p. 288).

#### 9.2.4 GLMs and information criteria (p. 288)
- Chapter 6's information criteria and regularizing priors apply to GLMs (p. 288).
- But WAIC and other criteria cannot decide between likelihood types (e.g. Gaussian vs binomial). Deviance is partly a normalizing constant, which changes its magnitude but not fit to data. The constants subtract out when models share the same outcome distribution type. They do not subtract out otherwise, so differences can mislead (p. 288).
- Rule: compare with information criteria only models using the same type of likelihood. Models with different likelihoods can be compared, but not with these criteria. Maximum entropy usually motivates an easy likelihood choice for ordinary regressions (p. 288).

### 9.3 Maximum entropy priors (pp. 288–289)
- Weakly informative priors are conventional for GLMs. They let the data dominate and tame pathologies (p. 288).
- Sometimes (rarely) parameters refer to things with background information. Then maximum entropy can build a prior that embodies that information while assuming as little else as possible (p. 288).
- The book does not use it. When you meet it, read it as including relevant background while introducing no other assumptions by accident (p. 289).

### 9.4 Summary (p. 289)
- The chapter is conceptual. Maximum entropy is an empirically successful way to choose likelihoods. Entropy measures the number of ways a distribution can arise under stated assumptions. GLMs follow naturally, but link functions add complexity in specification, estimation and interpretation (p. 289).

## Toy example (ours, not from the text)
**Part 1: entropy counts arrangements.** Toss 4 numbered pebbles into 2 buckets. Counts per bucket and ways $=4!/(n_1!\,n_2!)$:
- (4,0): $24/(24\cdot1)=1$ way. Entropy $=0$.
- (3,1): $24/(6\cdot1)=4$ ways. $H=-(0.75\ln0.75+0.25\ln0.25)=0.21576+0.34657=0.56233$.
- (2,2): $24/(2\cdot2)=6$ ways. $H=-(0.5\ln0.5+0.5\ln0.5)=0.69315$.

Log ways per pebble are $\ln1/4=0$, $\ln4/4=0.34657$, $\ln6/4=0.44794$. The ordering matches the entropy ordering. The numbers differ because $N=4$ is small; the text says the approximation improves as pebbles increase (p. 270). The evenly split distribution can be realized the most ways and has the biggest entropy.

**Part 2: a link compresses.** Take logit link with $\alpha=0,\beta=1$, so $p=e^x/(1+e^x)$:
- $x=0$: $p=1/2=0.5$
- $x=1$: $2.71828/3.71828=0.7311$
- $x=2$: $7.38906/8.38906=0.8808$
- $x=3$: $20.0855/21.0855=0.9526$

Successive gains: $0.2311,\ 0.1497,\ 0.0718$. They shrink even though each step in $x$ is one unit. The derivative formula agrees at $x=0$: $1/(2(1+\cosh0))=1/(2\cdot2)=0.25$. At $x=1$: $\cosh1=1.5431$, so $1/(2\cdot2.5431)=0.1966$.

## Concepts
- [[principle-of-indifference-maximum-entropy]] — choose the distribution that can arise the most ways, equivalently with biggest entropy, that fits the stated constraints; it is the most conservative one (p. 269)
- [[information-entropy]] (new) — $H(p)=-\sum p_i\log p_i$; here treated as approximately log number of ways per observation (pp. 268, 270)
- [[multiplicity-wallis-derivation]] (new) — $W$, the number of ways a set of counts can occur; $\frac1N\log W\to-\sum p_i\log p_i$ (p. 272)
- [[kl-divergence]] — used to prove maximum entropy results (Gaussian, binomial) and as the quantity minimized when the prior is not flat (pp. 272, 274)
- [[gaussian-max-entropy]] (new) — the Gaussian has maximum entropy among continuous distributions on the real line with fixed variance (pp. 274–275)
- [[binomial-max-entropy]] (new) — the binomial has maximum entropy for two unordered outcomes with constant expected value (pp. 275, 280)
- [[generalized-linear-model]] (new) — a model that puts a linear model on a parameter of a (maximum entropy) likelihood, via a link function (pp. 268, 281)
- [[link-function]] (new) — maps the linear model onto the allowed range of a likelihood parameter (pp. 281, 284)
- [[logit-link]] (new) — $\text{logit}(p)=\log\frac{p}{1-p}$; its inverse is the logistic (pp. 284–285)
- [[log-link]] (new) — maps positive parameters to the linear scale; the inverse is exponentiation (p. 286)
- [[exponential-family]] (new) — family of common GLM distributions, each maximum entropy under some constraints (p. 282)
- [[conditional-independence]] (new) — observations independent after accounting for predictors; a modeling assumption (p. 279)
- [[sensitivity-analysis]] (new) — varying assumptions and reporting all results (p. 287)
- [[histomancy]] (new) — the author's name for choosing a likelihood by inspecting the outcome histogram; criticised (p. 282)
- [[cross-validation-loo-waic]] — information criteria are comparable only across models with the same likelihood type (p. 288)

## Canonical instances
- [[pebbles-in-buckets]] — counting arrangements links entropy to number of ways (pp. 269–271)
- [[generalized-normal-family]] — equal-variance densities with Gaussian entropy maximum at shape 2 (pp. 273–274)
- [[marbles-expected-value-simulation]] — 100000 random distributions with mean 1.4 never beat the binomial's entropy (pp. 277–278)
- [[logistic-compression]] — Fig. 9.7: logit link flattens effects near 0 and 1 (p. 285)
- [[hurricane-damage-exponential]] — exponential growth from a log link cannot continue forever (p. 287)

## Bridges (candidates)
- [same-math] Wallis multiplicity and Stirling's approximation ↔ information theory: Shannon entropy as the rate of growth of log counts — the derivation is literally this.
- [same-math] Maximum entropy with a non-flat prior $q$ ↔ Bayesian updating: minimizing KL from the prior under constraints (author states the data-as-constraints version, p. 272).
- [structural-analogy] Entropy as "most ways" ↔ statistical mechanics: many microstates produce the observed macrostate, as with the knotted cords (p. 267).
- [structural-analogy] Logit and log links ↔ transformations in regression more generally: mapping a bounded parameter onto the whole real line.
- [metaphor] "Phantom assumptions" of non-maximum-entropy distributions ↔ hidden confounders: unstated structure that shapes conclusions.

## Questions this raises
- What other constraints (e.g. fixed mean and bounded support, or fixed mean and mean log) lead to which distributions beyond the Gaussian, exponential, gamma and binomial?
- When the link function distorts a model, how large must a sensitivity analysis be to count as reassuring?
- How do we compare models with different likelihoods if WAIC cannot be used?
- If the likelihood is a prior for the data, how should we check whether it is a "better" one in a given context?

## Reading notes
- Printed pages 267–289 are covered; printed p. 290 is blank. Printed = pdf − 14.
- Some figure text layers are garbled (e.g. Fig. 9.6 labels). The page images were used to read the distribution names and arrow labels.
- Sign convention: in the Overthinking proofs (pp. 274, 280), $H(q,p)$ is defined as $\int q\log p$ and $\sum q\log p$, without a minus sign. The proofs are consistent with that definition.
- p. 280, step 5 of the binomial proof: the preceding inequality $H(q)\le-H(q,p)$ and the result that $-H(q,p)=H(p)$ when $\bar q=\lambda$ support $H(q)\le H(p)$. The printed text says "$H(q)=H(p)$" and, for other expected values, "$H(p)>H(q)$". I report it as printed.
- The chapter has no numbered exercises.
- Footnote numbers (127–139) appear in the text, but the footnote text is not in these pages.

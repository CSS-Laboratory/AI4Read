---
id: mackay-2003-information/ch02-probability
work: mackay-2003-information
unit: "2 — Probability, Entropy, and Inference"
pages: "pdf 34–58 (printed page numbers not given in the text layer)"
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
---

# Probability, Entropy, and Inference

## L0 — One line
Probability is a calculus for both frequencies and degrees of belief, and Shannon information content, entropy and relative entropy are simple averages of log-probabilities whose basic inequalities all follow from convexity (Jensen's inequality).

## L1 — The gist (≤ 120 words)
The chapter sets up the tools for the rest of the book. First come ensembles, joint, marginal and conditional probability, the product and sum rules, and Bayes' theorem. These are used for forward problems (compute data from a model) and inverse problems (infer hidden causes from data). Then it defines the Shannon information content h(x) = log2 1/P(x), the entropy H(X) as its average, and the relative entropy D_KL(P‖Q). It proves that H(X) ≤ log|A_X| and that D_KL ≥ 0 (Gibbs' inequality) using Jensen's inequality for convex functions. Many exercises and solutions follow: Bayes' rule in practice, high-dimensional shells, the chain rule of entropy, and a repetition-code error calculation.

## L2 — Key ideas
- **Ensemble and joint ensemble.** An ensemble is a triple (outcome, alphabet, probabilities). From a joint P(x,y) you get marginals by summing and conditionals by normalizing rows or columns. English letter pairs are the running example. (pdf 34–35)
- **Product rule, sum rule, Bayes' theorem.** The product rule P(x,y|H) = P(x|y,H)P(y|H) is also called the chain rule. Bayes' theorem follows from it. Everything in inference is built from these three. (pdf 36)
- **Base-rate effect.** A "95% reliable" test with 1% prevalence gives only a 16% posterior probability of disease, so the likelihood alone is not the answer. (pdf 37)
- **Two meanings of probability.** Probabilities describe frequencies, or degrees of belief. The Cox axioms justify using the same rules for beliefs. Inference always needs assumptions, so it is "subjective" in that sense. (pdf 38)
- **Forward vs inverse probability, and prediction.** Inverse problems use the posterior ∝ likelihood × prior. Predictions should marginalize over hypotheses, not use only the best hypothesis. The likelihood principle says only P(observed data | θ) matters. (pdf 39–44)
- **Entropy and its relatives.** h(x) = log2 1/P(x), H(X) = Σ P(x) log 1/P(x), 0 ≤ H ≤ log|A_X|, H(X,Y) = H(X)+H(Y) iff independent, and the recursive decomposition (2.43–2.44). (pdf 44–46)
- **Gibbs' inequality.** D_KL(P‖Q) ≥ 0 with equality only if P = Q. The book calls it probably its most important inequality. D_KL is not symmetric. (pdf 46)
- **Jensen's inequality.** For convex f, E[f(x)] ≥ f(E[x]). Choosing the right function and random variable proves both H ≤ log|A_X| and Gibbs' inequality. (pdf 47, 56)
- **Exercises build intuition.** In high dimensions most volume of a sphere is in a thin shell near the surface. The bus-stop paradox shows that the interval around a random time is longer than a typical interval. (pdf 49, 54, 58)

## L3 — Walkthrough

### Opening remark on notation (pdf 34)
The author separates a random variable, its value, and the proposition that it has that value. He then promises to use the simplest notation in each chapter, for example saying "true" for "true with probability 1". (pdf 34)

### 2.1 Probabilities and ensembles (pdf 34–36)
**Ensemble.** An ensemble X is a triple $(x, \mathcal A_X, \mathcal P_X)$. The outcome x takes a value in $\mathcal A_X=\{a_1,\dots,a_I\}$ with probabilities $\mathcal P_X=\{p_1,\dots,p_I\}$, where $P(x=a_i)=p_i$, $p_i\ge 0$ and $\sum_{a_i\in\mathcal A_X}P(x=a_i)=1$. $\mathcal A$ stands for "alphabet". The running example is a random letter from an English document: 27 outcomes (a–z and a space "-"), with probabilities in figure 2.1. For example, e has 0.0913, the space has 0.1928 and z has 0.0007. (pdf 34)

**Subset.**
$$P(T)=P(x\in T)=\sum_{a_i\in T}P(x=a_i)\tag{2.1}$$
For the vowels $V=\{a,e,i,o,u\}$:
$$P(V)=0.06+0.09+0.06+0.07+0.03=0.31.\tag{2.2}$$
(pdf 34)

**Joint ensemble.** XY has outcomes that are ordered pairs (x,y). P(x,y) is the joint probability. The two variables are not necessarily independent. (pdf 34)

**Marginal probability.**
$$P(x=a_i)\equiv\sum_{y\in\mathcal A_Y}P(x=a_i,y).\tag{2.3}$$
$$P(y)\equiv\sum_{x\in\mathcal A_X}P(x,y).\tag{2.4}$$
(pdf 35)

**Conditional probability.**
$$P(x=a_i\mid y=b_j)\equiv\frac{P(x=a_i,y=b_j)}{P(y=b_j)}\quad\text{if }P(y=b_j)\ne0.\tag{2.5}$$
If $P(y=b_j)=0$ the conditional is undefined. (pdf 35)

**Example 2.1.** XY is two successive letters of an English document (figure 2.2). The two marginals P(x) and P(y) are identical and equal to the monogram distribution of figure 2.1. The conditionals P(y|x) and P(x|y) come from normalizing rows and columns (figure 2.3). Given x = q, the two most probable y are u and the space. The space is common after q because the source text uses the word FAQ a lot. Given y = u, the two most probable x are n and o. (pdf 35–36)

**Rules of probability.** H denotes the assumptions behind the probabilities. (pdf 36)
- Product rule, also called the chain rule:
$$P(x,y\mid\mathcal H)=P(x\mid y,\mathcal H)P(y\mid\mathcal H)=P(y\mid x,\mathcal H)P(x\mid\mathcal H).\tag{2.6}$$
- Sum rule:
$$P(x\mid\mathcal H)=\sum_yP(x,y\mid\mathcal H)\tag{2.7}$$
$$=\sum_yP(x\mid y,\mathcal H)P(y\mid\mathcal H).\tag{2.8}$$
- Bayes' theorem:
$$P(y\mid x,\mathcal H)=\frac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{P(x\mid\mathcal H)}\tag{2.9}$$
$$=\frac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{\sum_{y'}P(x\mid y',\mathcal H)P(y'\mid\mathcal H)}.\tag{2.10}$$
- Independence: X and Y are independent (X⊥Y) iff
$$P(x,y)=P(x)P(y).\tag{2.11}$$

**Exercise 2.2 and solution.** The variables of figure 2.2 are not independent. If they were, all conditionals P(y|x) would be the same function of y whatever x is (compare figure 2.3). (pdf 36, 52)

> Intuition note: Everything in probability is bookkeeping on a table of joint probabilities. Summing a row or column gives a marginal. Dividing by a marginal gives a conditional. Bayes' theorem just turns "row-normalized" into "column-normalized".

**Example 2.3 (Jo's disease test).** a = 1 means Jo has the disease. b = 1 means the test is positive. The test is 95% reliable:
$$P(b{=}1|a{=}1)=0.95,\ P(b{=}1|a{=}0)=0.05,\ P(b{=}0|a{=}1)=0.05,\ P(b{=}0|a{=}0)=0.95,\tag{2.13}$$
and prevalence is
$$P(a{=}1)=0.01,\quad P(a{=}0)=0.99.\tag{2.14}$$
The joint is P(a,b) = P(a)P(b|a). By the sum rule,
$$P(b{=}1)=P(b{=}1|a{=}1)P(a{=}1)+P(b{=}1|a{=}0)P(a{=}0).\tag{2.15}$$
Bayes' theorem gives:
$$P(a{=}1|b{=}1)=\frac{P(b{=}1|a{=}1)P(a{=}1)}{P(b{=}1|a{=}1)P(a{=}1)+P(b{=}1|a{=}0)P(a{=}0)}\tag{2.16}$$
$$=\frac{0.95\times0.01}{0.95\times0.01+0.05\times0.99}\tag{2.17}$$
$$=0.16.\tag{2.18}$$
So despite the positive result Jo has the disease with probability only 16%. The "man in the street" wrongly says 95%. (pdf 37)

> Intuition note: Most positives come from the large healthy group (0.05 × 0.99), not from the small sick group (0.95 × 0.01). The prior matters as much as the test.

### 2.2 The meaning of probability (pdf 37–39)
- **Two uses.** Probabilities describe frequencies of outcomes in random experiments. But "frequency" and "random" are hard to define without circularity, for example for a coin's frequency of heads being 1/2. The author does not try to settle this. (pdf 37–38)
- **Degrees of belief.** Probabilities can also describe beliefs about propositions that are not random variables. Examples: whether Mr. S. was the murderer, or whether a cheque signature is genuine. (pdf 38)
- **Cox axioms (box 2.4).** B(x) is the degree of belief in x, and $\bar x$ is not-x.
  - Axiom 1: beliefs can be ordered, so they map onto real numbers.
  - Axiom 2: there is a function f with $B(x)=f[B(\bar x)]$.
  - Axiom 3: there is a function g with $B(x,y)=g[B(x|y),B(y)]$.
  - Beliefs satisfying these can be mapped to probabilities with P(false)=0, P(true)=1, 0 ≤ P(x) ≤ 1, $P(x)=1-P(\bar x)$ and $P(x,y)=P(x|y)P(y)$. (pdf 38)
- **Bayesian viewpoint.** Two people with the same assumptions and data draw identical conclusions. This is also called the subjective interpretation. Its advocates say: "you cannot do inference without making assumptions." (pdf 38)
- **Warning.** This view is not universally held. Statistics in the 20th century was dominated by non-Bayesian methods that allow probabilities only for random variables. (pdf 38)

### 2.3 Forward probabilities and inverse probabilities (pdf 39–43)
**Forward problems.** These use a generative model, which is a process assumed to give rise to data. The task is to compute the distribution or expectation of some quantity depending on the data. (pdf 39)
- Exercise 2.4: an urn has K balls, B black and W = K − B white. Fred draws N times with replacement. Find the distribution, mean, variance and standard deviation of n_B, for N = 5 and N = 400 with B = 2, K = 10.
- Exercise 2.5: $z=\dfrac{(n_B-f_BN)^2}{Nf_B(1-f_B)}$, where $f_B=B/K$. Find E[z], the distribution of z for N = 5 and f_B = 1/5, and P(z<1). (2.19)

**Inverse problems.** These use the same kind of model but compute the conditional probability of unobserved variables given the observed ones. This always needs Bayes' theorem. (pdf 39)

**Example 2.6 (eleven urns).** Urn u ∈ {0,…,10} holds u black and 10−u white balls out of ten. Fred picks u uniformly (P(u)=1/11) and draws N = 10 times with replacement. He gets n_B = 3 blacks. What is P(u | n_B, N), from Bill's point of view? (pdf 39–40)
$$P(u,n_B\mid N)=P(n_B\mid u,N)P(u).\tag{2.20}$$
$$P(u\mid n_B,N)=\frac{P(u,n_B\mid N)}{P(n_B\mid N)}\tag{2.21}$$
$$=\frac{P(n_B\mid u,N)P(u)}{P(n_B\mid N)}.\tag{2.22}$$
With $f_u\equiv u/10$,
$$P(n_B\mid u,N)=\binom{N}{n_B}f_u^{\,n_B}(1-f_u)^{N-n_B}.\tag{2.23}$$
The denominator is a marginal:
$$P(n_B\mid N)=\sum_uP(u,n_B\mid N)=\sum_uP(u)P(n_B\mid u,N).\tag{2.24}$$
$$P(u\mid n_B,N)=\frac{P(u)P(n_B\mid u,N)}{P(n_B\mid N)}\tag{2.25}$$
$$=\frac{1}{P(n_B\mid N)}\frac1{11}\binom{N}{n_B}f_u^{\,n_B}(1-f_u)^{N-n_B}.\tag{2.26}$$
The normalizing constant is $P(n_B=3\mid N=10)=0.083$. Figure 2.6 gives the posterior:

| u | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P(u \| n_B=3, N=10) | 0 | 0.063 | 0.22 | 0.29 | 0.24 | 0.13 | 0.047 | 0.0099 | 0.00086 | 0.0000096 | 0 |

The values u = 0 and u = 10 have posterior 0. Urn 0 has no black balls, and urn 10 has no white balls. (pdf 40)

**Terminology.** (pdf 40–41)
- P(u) is the *prior* of u.
- P(n_B | u, N) is the *likelihood* of u. For fixed u it is a probability over n_B. For fixed n_B it is a likelihood function of u. Likelihood and probability are not synonyms.
- The rule: "Never say 'the likelihood of the data'. Always say 'the likelihood of the parameters'." The likelihood function is not a probability distribution. (pdf 41)
- P(u | n_B, N) is the *posterior*.
- The normalizing constant P(n_B | N) is the *evidence* or *marginal likelihood*. It is unimportant for comparing hypotheses but important in complex modelling.
- With parameters θ, data D and hypothesis space H:
$$P(\boldsymbol\theta\mid D,\mathcal H)=\frac{P(D\mid\boldsymbol\theta,\mathcal H)P(\boldsymbol\theta\mid\mathcal H)}{P(D\mid\mathcal H)}\tag{2.27}$$
$$\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}.\tag{2.28}$$

**Prediction (Example 2.6 continued).** What is the probability that ball N+1 is black, given n_B = 3, N = 10? (pdf 41)
$$P(\text{ball}_{N+1}\text{ is black}\mid n_B,N)=\sum_uP(\text{ball}_{N+1}\text{ is black}\mid u,n_B,N)P(u\mid n_B,N).\tag{2.29}$$
With replacement, the first factor is just $f_u=u/10$, so
$$P(\text{ball}_{N+1}\text{ is black}\mid n_B,N)=\sum_uf_uP(u\mid n_B,N).\tag{2.30}$$
$$P(\text{ball}_{N+1}\text{ is black}\mid n_B=3,N=10)=0.333.\tag{2.31}$$
The comment: the common practice of picking the most plausible hypothesis (u = 3) would give 0.3. Marginalizing over u gives a "slightly more moderate, less extreme" prediction. (pdf 41)

> Intuition note: Do not bet on one hypothesis when the data leave several alive. Weight each hypothesis's prediction by its posterior probability. That is just the sum rule.

**Inference as inverse probability.**
- **Example 2.7 (bent coin).** A coin has unknown heads-probability f_H. After n_H heads in N tosses, what is the distribution of f_H, and the probability that toss N+1 is a head? (N = 10, n_H = 3; or N = 300, n_H = 29.) (pdf 42)
  - This is like example 2.6 but f_H is a fixed unknown parameter, not a random variable in the frequentist sense.
  - We must assume a prior P(f_H). Here P(f) denotes a probability density. In real data modelling "priors are subjective and so are likelihoods", for example the assumption that draws are independent. (pdf 42)
- **Densities.** The probability that v lies in (a,b) is $\int_a^b dv\,P(v)$. P(v)dv is dimensionless, and P(v) has dimensions inverse to v. Densities greater than 1 are normal provided $\int_a^b dv\,P(v)\le1$. (pdf 42)
- **Exercise 2.8.** Take a uniform prior P(f_H) = 1. Sketch the posterior and the probability that the (N+1)th toss is heads for (a) N=3, n_H=0; (b) N=3, n_H=2; (c) N=10, n_H=3; (d) N=300, n_H=29. The beta integral to use:
$$\int_0^1dp_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!\,F_b!}{(F_a+F_b+1)!}.\tag{2.32}$$
(pdf 42)
- **Prior ≠ guess.** A prior is a density over f_H, not the statement "I guess f_H = 1/2". If the prior is symmetric about 1/2, the first toss has
$$P(x_1=\text{head})=\int df_H\,P(f_H)P(x_1=\text{head}\mid f_H)=\int df_H\,P(f_H)f_H=1/2.\tag{2.33}$$
Later tosses depend on the whole prior, not just its mean. (pdf 43)

**Data compression and inverse probability.** Example 2.9 asks for a program that compresses a binary file with n_1 = 29 ones and n_0 = 271 zeros. Compression exploits predictability. A compressor must implicitly answer "what is the probability that the next character is a 1?". The author claims this is like example 2.7. He states that "data compression and data modelling are one and the same", and that example 2.9 is solved in Chapter 6. (pdf 43)

**The likelihood principle.** (pdf 43–44)
- Example 2.10: urn A has 1 black and 2 white balls. Urn B has 2 black and 1 white. An urn is chosen at random and a black ball is drawn. P(urn A)?
- Example 2.11: urn A has 5 balls (1 black, 2 white, 1 green, 1 pink). Urn B has 500 balls (200 black, 100 white, 50 yellow, 40 cyan, 30 sienna, 25 green, 25 silver, 20 gold, 10 purple). A black ball is drawn. P(urn A)?
- The text does not state the numeric answers. (Added step: both give $\frac{1/5}{1/5+2/5}=\frac{1/3}{1/3+2/3}=1/3$, since in each case urn A has black-probability half of urn B's.) The point is that the details of other outcomes are irrelevant.
- **Likelihood principle:** given a generative model P(d|θ) and an observed d_1, all inferences and predictions should depend only on the function P(d_1|θ). Many classical statistical methods violate it. (pdf 44)

### 2.4 Definition of entropy and related functions (pdf 44–45)
**Shannon information content** of outcome x, in bits:
$$h(x)=\log_2\frac1{P(x)}.\tag{2.34}$$
"Bit" also names a 0/1 variable, and context decides which meaning is meant. In table 2.9, h(z) = 10.4 bits and h(e) = 3.5 bits. The other values include a: 4.1, space: 2.4, q: 10.3, j: 10.7. (pdf 44)

**Entropy** of an ensemble is the average information content:
$$H(X)\equiv\sum_{x\in\mathcal A_X}P(x)\log\frac1{P(x)},\tag{2.35}$$
with the convention $0\times\log1/0\equiv0$, because $\lim_{\theta\to0^+}\theta\log1/\theta=0$. It is measured in bits. It is also written H(**p**), and it is also called the uncertainty of X. (pdf 44)

**Example 2.12.** The entropy of a random English letter is about 4.11 bits, found by averaging the fourth column of table 2.9 under the third. The table's sum row shows 4.1. (pdf 44)

**Properties.** (pdf 45)
- H(X) ≥ 0, with equality iff p_i = 1 for one i.
- Entropy is maximized by the uniform distribution:
$$H(X)\le\log|\mathcal A_X|\quad\text{with equality iff }p_i=1/|\mathcal A_X|\text{ for all }i.\tag{2.36}$$
- **Redundancy** of X:
$$1-\frac{H(X)}{\log|\mathcal A_X|}.\tag{2.37}$$
The book will not use it.
- **Joint entropy:**
$$H(X,Y)=\sum_{xy\in\mathcal A_X\mathcal A_Y}P(x,y)\log\frac1{P(x,y)}.\tag{2.38}$$
- Additivity for independent variables:
$$H(X,Y)=H(X)+H(Y)\ \text{ iff }\ P(x,y)=P(x)P(y).\tag{2.39}$$
- The definitions so far are for discrete distributions over finite sets. Infinite sets may give infinite entropy. Continuous densities are treated in section 11.3, and more definitions come in section 8.1.

> Intuition note: Rare outcomes are very informative (z: 10.4 bits), and common ones are barely informative (space: 2.4 bits). Entropy is the average of this surprise. It is zero when the outcome is certain and largest when all outcomes are equally likely.

### 2.5 Decomposability of the entropy (pdf 45–46)
**Example.** x ∈ {0,1,2} is made by flipping a fair coin to decide whether x = 0, then, if not, flipping a second fair coin to choose between 1 and 2:
$$P(x{=}0)=\tfrac12;\ P(x{=}1)=\tfrac14;\ P(x{=}2)=\tfrac14.\tag{2.40}$$
Brute force:
$$H(X)=\tfrac12\log2+\tfrac14\log4+\tfrac14\log4=1.5.\tag{2.41}$$
Decomposition: learning whether x = 0 is a binary variable with entropy $H(\tfrac12,\tfrac12)=\tfrac12\log2+\tfrac12\log2=1$ bit. The second flip is experienced only half the time:
$$H(X)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac12,\tfrac12).\tag{2.42}$$
**General form:**
$$H(\mathbf p)=H(p_1,1-p_1)+(1-p_1)H\!\left(\frac{p_2}{1-p_1},\frac{p_3}{1-p_1},\dots,\frac{p_I}{1-p_1}\right).\tag{2.43}$$
**Grouped form, for any m:**
$$\begin{aligned}H(\mathbf p)={}&H\big[(p_1+\dots+p_m),(p_{m+1}+\dots+p_I)\big]\\&+(p_1+\dots+p_m)H\!\left(\frac{p_1}{p_1+\dots+p_m},\dots,\frac{p_m}{p_1+\dots+p_m}\right)\\&+(p_{m+1}+\dots+p_I)H\!\left(\frac{p_{m+1}}{p_{m+1}+\dots+p_I},\dots,\frac{p_I}{p_{m+1}+\dots+p_I}\right).\end{aligned}\tag{2.44}$$

**Example 2.13.** A source emits a numeral (prob. 1/3, 10 equiprobable), a vowel (prob. 1/3, 5 equiprobable) or one of 21 consonants (prob. 1/3, equiprobable). Using (2.44):
$$\log3+\tfrac13(\log10+\log5+\log21)=\log3+\tfrac13\log1050\simeq\log30\text{ bits}.$$
(pdf 46)

> Intuition note: Entropy is "how much do I learn in the first, coarse question, plus the expected extra I learn in the fine question". This is how uncertainty adds up step by step.

### 2.6 Gibbs' inequality (pdf 46)
**Relative entropy / Kullback–Leibler divergence** between P and Q over the same alphabet:
$$D_{KL}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}.\tag{2.45}$$
**Gibbs' inequality:**
$$D_{KL}(P\|Q)\ge0\quad\text{with equality only if }P=Q.\tag{2.46}$$
In general $D_{KL}(P\|Q)\ne D_{KL}(Q\|P)$, so it is not strictly a "distance". It matters in pattern recognition and neural networks as well as in information theory. The author calls this probably the most important inequality in the book. It is proved with convexity. (pdf 46)

### 2.7 Jensen's inequality for convex functions (pdf 47–48)
**Convex (⌣).** f is convex over (a,b) if every chord lies above the function. For all x_1, x_2 ∈ (a,b) and 0 ≤ λ ≤ 1:
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\tag{2.47}$$
It is *strictly* convex if equality holds only for λ = 0 and 1. Concave (⌢) is defined similarly. Strictly convex examples: x², eˣ and e⁻ˣ for all x; log(1/x) and x log x for x > 0 (figure 2.11). (pdf 47)

**Jensen's inequality.** For convex f:
$$\mathcal E[f(x)]\ge f(\mathcal E[x]).\tag{2.48}$$
If f is strictly convex and equality holds, x is a constant. For concave f the direction reverses. Physical picture: masses p_i placed on a convex curve at (x_i, f(x_i)) have their centre of gravity (E[x], E[f(x)]) above the curve. (pdf 47)

> Intuition note: Averaging first and then applying a "smile-shaped" function gives less than applying it first and then averaging. The gap vanishes only when there is no spread.

**Example 2.15.** Three squares have mean area 100 m² and mean side 10 m. Let x be the side, with probability 1/3 on each, and f(x) = x² (strictly convex). Then E[x] = 10 and E[f(x)] = 100 = f(E[x]). Equality holds, so x is constant. All three sides are equal and the largest square has area 100 m². (pdf 47)

**Maximization.** If f(**x**) is concave and there is a point where ∂f/∂x_k = 0 for all k, then f has its maximum there:
$$\frac{\partial f}{\partial x_k}=0\ \text{for all }k.\tag{2.49}$$
The converse fails: f(x) = −|x| is maximized at x = 0 where the derivative is undefined. Also f(p) = log p on (0,1) is maximized on the boundary at p = 1, where the gradient is 1. (pdf 48)

**Exercise 2.14 and solution (Jensen's inequality for finite distributions).** Given (2.60), $f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)$, we must show for $\sum p_i=1$, $p_i\ge0$ (2.61):
$$\sum_{i=1}^Ip_if(x_i)\ge f\Big(\sum_{i=1}^Ip_ix_i\Big).$$
The proof is by recursion starting from the right-hand side. It does not handle p_i = 0 cases. Use convexity with $\lambda=p_1/\sum_{i=1}^Ip_i=p_1$, then with $\lambda=p_2/\sum_{i=2}^Ip_i$, and so on:
$$\begin{aligned}f\Big(\sum_{i=1}^Ip_ix_i\Big)&=f\Big(p_1x_1+\sum_{i=2}^Ip_ix_i\Big)\\&\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]\Big[f\Big(\sum_{i=2}^Ip_ix_i\Big/\sum_{i=2}^Ip_i\Big)\Big]\\&\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]\Big[\frac{p_2}{\sum_{i=2}^Ip_i}f(x_2)+\frac{\sum_{i=3}^Ip_i}{\sum_{i=2}^Ip_i}f\Big(\sum_{i=3}^Ip_ix_i\Big/\sum_{i=3}^Ip_i\Big)\Big],\end{aligned}\tag{2.62}$$
"and so forth." (pdf 53)

### 2.8 Exercises (pdf 48–50, with solutions in 2.10)

**Sums of random variables (Ex. 2.16).** (a) Distribution of the sum and of the absolute difference of two dice. (b) Rough distribution of the sum of 100 dice. (c) How to label two cubical dice with {0,…,6} so that the sum is uniform on 1–12. (d) Can 100 dice be labelled so the sum is uniform? A margin note links this to the central-limit theorem. (pdf 48)

**Inference problems.**
- Ex. 2.17: if q = 1 − p and a = ln p/q, show
$$p=\frac1{1+\exp(-a)},\tag{2.50}$$
relate it to tanh, and find p as a function of b = log₂ p/q.
- Ex. 2.18: for binary x, show
$$\log\frac{P(x{=}1|y)}{P(x{=}0|y)}=\log\frac{P(y|x{=}1)}{P(y|x{=}0)}+\log\frac{P(x{=}1)}{P(x{=}0)}.\tag{2.51}$$
- Ex. 2.19: for d_1, d_2 conditionally independent given x,
$$\frac{P(x{=}1|\{d_i\})}{P(x{=}0|\{d_i\})}=\frac{P(d_1|x{=}1)}{P(d_1|x{=}0)}\frac{P(d_2|x{=}1)}{P(d_2|x{=}0)}\frac{P(x{=}1)}{P(x{=}0)}.\tag{2.52}$$
(pdf 48)

**Life in high-dimensional spaces (Ex. 2.20).** Show that the fraction of an N-dimensional sphere's volume in the shell between radius r − ε and r is
$$f=1-\Big(1-\frac\epsilon r\Big)^N.\tag{2.53}$$
Evaluate for N = 2, 10, 1000 with ε/r = 0.01 and 0.5. Implication: uniformly distributed points in a high-dimensional sphere are very likely in a thin shell near the surface. (pdf 49)

**Expectations and entropies.**
$$\mathcal E[f(x)]=\langle f(x)\rangle=\sum_xP(x)f(x).\tag{2.54}$$
- Ex. 2.21–2.24: expectations where f depends on P(x), with p_a = 0.1, p_b = 0.2, p_c = 0.7.
- Ex. 2.22: E[1/P(x)] for an arbitrary ensemble.
- Ex. 2.25: prove H(X) ≤ log|A_X| (hint: Jensen).
- Ex. 2.26: prove Gibbs' inequality.
- Ex. 2.27: prove the decomposition (2.43–2.44). (pdf 49)
- Ex. 2.28: a four-outcome variable chosen by a tree of bent coins with biases f, then g or h. Find the distribution, the entropy using (2.44) and H₂, and dH/df (hint: dH₂(x)/dx = log((1−x)/x)).
- Ex. 2.29: flip a coin until the first head. Find the entropy of the number of flips, for fair and biased coins. (pdf 50)

### 2.9 Further exercises (pdf 50–52)
- **Forward probability.**
  - Ex. 2.30: for draws without replacement, P(first white) = P(second white).
  - Ex. 2.31: coin of diameter a on a b × b grid, answer $(1-a/b)^2$.
  - Ex. 2.32: Buffon's needle, answer 2a/πb for a < b, and the "noodle" generalization 2A/πb.
  - Ex. 2.33: forming a triangle from a broken stick.
  - Ex. 2.34: tails and heads until the first head, and the distribution of the estimator $\hat f=h/(h+t)$, a sampling problem with no Bayes.
  - Ex. 2.35: rolls between sixes, with the clock-strikes-one and Poissonville bus paradox. The text states 6 minutes average wait and 12 minutes between the missed and the next bus. (pdf 50–51)
- **Conditional probability.**
  - Ex. 2.36: Fred and his brothers Alf and Bob.
  - Ex. 2.37: islanders who tell the truth 1/3 of the time.
  - Ex. 2.38: repetition code R₃ on a binary symmetric channel, computed by the binomial method and by the sum-rule method, with
$$P(\text{error})=\sum_{\mathbf r}P(\mathbf r)P(\text{error}\mid\mathbf r).\tag{2.55}$$
  - Ex. 2.39: Zipf's law
$$p_n\simeq\begin{cases}0.1/n&n\in1,\dots,12\,367\\0&n>12\,367.\end{cases}\tag{2.56}$$
What is the entropy of English per word if words are drawn at random from this distribution? The author notes that Shannon made numerical errors in his own version of this calculation. (pdf 51–52)

### 2.10 Solutions (pdf 52–58)
- **Ex. 2.4** (pdf 52). Binomial:
$$P(n_B\mid f_B,N)=\binom N{n_B}f_B^{\,n_B}(1-f_B)^{N-n_B}\tag{2.57}$$
$$\mathcal E[n_B]=Nf_B\tag{2.58}$$
$$\mathrm{var}[n_B]=Nf_B(1-f_B).\tag{2.59}$$
With f_B = 1/5 and N = 5: mean 1, variance 4/5, standard deviation 0.89. With N = 400: mean 80, variance 64, standard deviation 8.
- **Ex. 2.5** (pdf 52). The numerator is (n_B − E[n_B])². The denominator is the variance of n_B, which is the expectation of the numerator. So E[z] = 1 (z is a χ²-type quantity). For N = 5 and f_B = 1/5: Nf_B = 1, var = 4/5. Only n_B = 1 gives z < 1, so P(z<1) = P(n_B=1) = 0.4096.
- **Ex. 2.16** (pdf 53). (a) The sum has P = {1,2,3,4,5,6,5,4,3,2,1}/36 for outcomes 2,…,12. (b) One die has mean 3.5 and variance 35/12. So 100 dice have mean 350 and variance 3500/12 ≃ 292, roughly Gaussian by the central-limit theorem. (c) The unique solution is one ordinary die and one with faces 6,6,6,0,0,0. (d) Yes, for example label the rth die with {0,1,2,3,4,5} × 6^r. A margin note asks whether this contradicts the central-limit theorem.
- **Ex. 2.17** (pdf 53–54). From $a=\ln p/q$ we get $p/q=e^a$ (2.63) and $\frac p{1-p}=e^a$ (2.64), so
$$p=\frac{e^a}{e^a+1}=\frac1{1+\exp(-a)}.\tag{2.65}$$
With $\tanh(a)=\dfrac{e^a-e^{-a}}{e^a+e^{-a}}$ (2.66):
$$f(a)\equiv\frac1{1+\exp(-a)}=\frac12\Big(\frac{1-e^{-a}}{1+e^{-a}}+1\Big)=\frac12\Big(\frac{e^{a/2}-e^{-a/2}}{e^{a/2}+e^{-a/2}}+1\Big)=\frac12(\tanh(a/2)+1).\tag{2.67}$$
For base 2, $p=\dfrac1{1+2^{-b}}$ (2.68).
- **Ex. 2.18** (pdf 54).
$$P(x|y)=\frac{P(y|x)P(x)}{P(y)}\tag{2.69}$$
$$\Rightarrow\frac{P(x{=}1|y)}{P(x{=}0|y)}=\frac{P(y|x{=}1)}{P(y|x{=}0)}\frac{P(x{=}1)}{P(x{=}0)}\tag{2.70}$$
and taking logs gives (2.71).
- **Ex. 2.19** (pdf 54). Conditional independence means
$$P(x,d_1,d_2)=P(x)P(d_1|x)P(d_2|x).\tag{2.72}$$
So the posterior ratio is the likelihood ratio of {d_i} times the prior ratio (2.73), and the likelihood ratio factorizes into one factor per data point (2.74).
- **Ex. 2.20** (pdf 54). Volume is
$$V(r,N)=\frac{\pi^{N/2}}{(N/2)!}r^N\tag{2.75}$$
but only V ∝ r^N is needed:
$$\frac{r^N-(r-\epsilon)^N}{r^N}=1-\Big(1-\frac\epsilon r\Big)^N.\tag{2.76}$$

| | N=2 | N=10 | N=1000 |
|---|---|---|---|
| ε/r = 0.01 | 0.02 | 0.096 | 0.99996 |
| ε/r = 0.5 | 0.75 | 0.999 | 1 − 2⁻¹⁰⁰⁰ |

For large N, essentially all the mass is in the shell however small ε is.
- **Ex. 2.21–2.24** (pdf 55).
$$\mathcal E[f(x)]=0.1\times10+0.2\times5+0.7\times10/7=3,\tag{2.77}$$
and since f = 1/P(x) here, E[1/P(x)] = 3 (2.78). For general X,
$$\mathcal E[1/P(x)]=\sum_{x}P(x)\frac1{P(x)}=\sum_x1=|\mathcal A_X|.\tag{2.79}$$
E[g(x)] = p_b = 0.2 (2.80). P(P(x) ∈ [0.15, 0.5]) = p_b = 0.2 (2.81). $P(|\log\frac{P(x)}{0.2}|>0.05)=p_a+p_c=0.8$ (2.82).
- **Ex. 2.25** (pdf 55–56). Differentiation proof, not recommended. Use natural logs:
$$H(X)=\sum_ip_i\ln\frac1{p_i}\tag{2.83}$$
$$\frac{\partial H(X)}{\partial p_i}=\ln\frac1{p_i}-1.\tag{2.84}$$
Maximize under $\sum p_i=1$ with a Lagrange multiplier:
$$G(\mathbf p)\equiv H(X)+\lambda\Big(\sum_ip_i-1\Big)\tag{2.85}$$
$$\frac{\partial G}{\partial p_i}=\ln\frac1{p_i}-1+\lambda.\tag{2.86}$$
Setting it to zero:
$$\ln\frac1{p_i}-1+\lambda=0\tag{2.87}$$
$$\Rightarrow\ln\frac1{p_i}=1-\lambda,\tag{2.88}$$
so all p_i are equal. The curvature is
$$\frac{\partial^2G}{\partial p_i\partial p_j}=-\frac1{p_i}\delta_{ij},\tag{2.89}$$
which is negative definite. The author warns that this route is risky, since maxima can lie on a boundary. *Recommended proof (Jensen).* Choosing $f(u)=\log\frac1u=-\log u$ (2.90) with u = P(x) gives an inequality in the wrong direction. Instead take
$$u=1/P(x),\tag{2.91}$$
so that
$$H(X)=-\mathcal E[f(1/P(x))]\le-f(\mathcal E[1/P(x)]),\tag{2.92}$$
and since E[1/P(x)] = |A_X| (Ex. 2.22),
$$H(X)\le-f(|\mathcal A_X|)=\log|\mathcal A_X|.\tag{2.93}$$
Equality holds only if 1/P(x) is constant, so P is uniform. (pdf 55–56)
- **Ex. 2.26** (pdf 56). With $D_{KL}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}$ (2.94), take f(u) = log 1/u and u = Q(x)/P(x):
$$D_{KL}(P\|Q)=\mathcal E[f(Q(x)/P(x))]\tag{2.95}$$
$$\ge f\Big(\sum_xP(x)\frac{Q(x)}{P(x)}\Big)=\log\frac1{\sum_xQ(x)}=0,\tag{2.96}$$
with equality only if u is constant, that is, Q = P. *Second solution:* use expectations under Q, f(u) = u log u and u = P(x)/Q(x):
$$D_{KL}(P\|Q)=\sum_xQ(x)\frac{P(x)}{Q(x)}\log\frac{P(x)}{Q(x)}=\sum_xQ(x)f\Big(\frac{P(x)}{Q(x)}\Big)\tag{2.97}$$
$$\ge f\Big(\sum_xQ(x)\frac{P(x)}{Q(x)}\Big)=f(1)=0.\tag{2.98}$$
(pdf 56)
- **Ex. 2.28** (pdf 57). $H(X)=H_2(f)+fH_2(g)+(1-f)H_2(h)$ (2.99).
- **Ex. 2.29** (pdf 57). $P(x)=(1-f)^{x-1}f$ (2.100). After a tail, the future looks like the start, so
$$H(X)=H_2(f)+(1-f)H(X)\tag{2.101}$$
$$\Rightarrow H(X)=H_2(f)/f.\tag{2.102}$$
- **Ex. 2.34** (pdf 57). $P(t)=(1/2)^t\,(1/2)$ for t ≥ 0 (2.103). Expected heads = 1. Expected tails:
$$\mathcal E[t]=\sum_{t=0}^\infty t\,(1/2)^t\,\tfrac12\tag{2.104}$$
and the recurrence
$$\mathcal E[t]=\tfrac12(1+\mathcal E[t])+\tfrac12\cdot0\ \Rightarrow\ \mathcal E[t]=1.\tag{2.105}$$
The estimator is $\hat f=1/(1+t)$, with the distribution plotted in figure 2.12 for f = 1/2.
- **Ex. 2.35** (pdf 57–58).
  - (a) The mean number of rolls from one six to the next is 6. The distribution is
$$P(r_1=r)=\Big(\frac56\Big)^{r-1}\frac16,\ r\in\{1,2,\dots\}\tag{2.106}$$
which is exponential:
$$P(r_1=r)=e^{-\alpha r}/Z,\quad\alpha=\ln(6/5).\tag{2.107}$$
  - (b) From the clock to the next six: mean 6.
  - (c) Back in time to the previous six: mean 6.
  - (d) The mean from the six before the clock to the six after it is the sum of (b) and (c) less one: 11.
  - (e) The explanation uses the bus picture. Passengers arrive uniformly and buses after gaps longer than 6 minutes are overcrowded. So two-thirds of passengers can be on overcrowded buses while only one-third of buses are overcrowded. Both claims can be true. Figure 2.13 shows P(r_1 > 6) ≈ 1/3 and, for $r_{tot}$ with $P(r_{tot}=r)=r(5/6)^{r-1}(1/6)^2$, P(r_tot > 6) ≈ 2/3. The means are 6 and 11.
- **Ex. 2.38** (pdf 58). *Binomial method:* $p_B=3f^2(1-f)+f^3$. *Sum-rule method:*
$$P(\mathbf r{=}000)=\tfrac12(1-f)^3+\tfrac12f^3\tag{2.108}$$
$$P(\mathbf r{=}001)=\tfrac12f(1-f)^2+\tfrac12f^2(1-f)=\tfrac12f(1-f)\tag{2.109}$$
$$P(s{=}1|\mathbf r{=}000)=\frac{f^3}{(1-f)^3+f^3}\tag{2.110}$$
$$P(s{=}1|\mathbf r{=}001)=\frac{(1-f)f^2}{f(1-f)^2+f^2(1-f)}=f.\tag{2.111}$$
So
$$P(\text{error}|\mathbf r{=}000)=\frac{f^3}{(1-f)^3+f^3}\tag{2.112}$$
$$P(\text{error}|\mathbf r{=}001)=f.\tag{2.113}$$
Some bits are better determined than others: the per-case error probability is about f³ or f. The average is
$$P(\text{error})=2\big[\tfrac12(1-f)^3+\tfrac12f^3\big]\frac{f^3}{(1-f)^3+f^3}+6\big[\tfrac12f(1-f)\big]f=f^3+3f^2(1-f).$$
- **Ex. 2.39** (pdf 58). The entropy is 9.7 bits per word. The text gives no derivation.

## Toy example (ours, not from the text)
**Part 1: Bayes with prediction.** Two coins, A (heads prob. 0.5) and B (heads prob. 0.8). We pick one with prior 1/2 each and see one head.
- Joint weights: A: 0.5 × 0.5 = 0.25; B: 0.5 × 0.8 = 0.40. Evidence: 0.25 + 0.40 = 0.65.
- Posterior: P(A|head) = 0.25/0.65 = 0.385; P(B|head) = 0.40/0.65 = 0.615.
- Marginalized prediction of a second head: 0.385 × 0.5 + 0.615 × 0.8 = 0.1923 + 0.4923 = 0.685.
- "Best hypothesis" prediction (B only): 0.8. As in example 2.6, marginalizing is more moderate.

**Part 2: Entropy and the asymmetry of KL.** Let P = (0.5, 0.5) and Q = (0.75, 0.25) over two symbols.
- Information contents of Q: h = log₂(1/0.75) = 0.415 bits and log₂(1/0.25) = 2 bits.
- H(Q) = 0.75 × 0.415 + 0.25 × 2 = 0.311 + 0.5 = 0.811 bits. This is below log₂ 2 = 1, as (2.36) requires.
- D_KL(P‖Q) = 0.5 log₂(0.5/0.75) + 0.5 log₂(0.5/0.25) = 0.5(−0.585) + 0.5(1) = 0.208 bits.
- D_KL(Q‖P) = 0.75 log₂(0.75/0.5) + 0.25 log₂(0.25/0.5) = 0.75(0.585) + 0.25(−1) = 0.439 − 0.25 = 0.189 bits.
- Both are ≥ 0 (Gibbs) and unequal (asymmetry).

## Concepts
- [[bit]] — unit of information content; also a 0/1 variable (pdf 44)
- [[self-information-surprisal]] — Shannon information content h(x) = log₂ 1/P(x) (pdf 44)
- [[entropy-hx]] — average Shannon information content, H(X) = Σ P(x) log 1/P(x), also called uncertainty (pdf 44)
- [[joint-and-conditional-entropy]] — joint entropy H(X,Y) defined, additive iff independent; conditional entropy is not yet defined here (pdf 45)
- [[chain-rule]] — here the probability product rule P(x,y) = P(x|y)P(y), plus the entropy decomposition (2.43–2.44) (pdf 36, 46)
- [[redundancy]] — 1 − H(X)/log|A_X| (pdf 45)
- [[relative-entropy-kl-divergence]] — D_KL(P‖Q) = Σ P log P/Q, non-negative, asymmetric (pdf 46)
- [[bayes-theorem]] (new) — posterior = likelihood × prior / evidence, equations 2.9–2.10 and 2.27–2.28 (pdf 36, 41)
- [[jensen-inequality]] (new) — E[f(x)] ≥ f(E[x]) for convex f (pdf 47)
- [[gibbs-inequality]] (new) — D_KL ≥ 0, proved with Jensen (pdf 46, 56)
- [[likelihood-principle]] (new) — inference depends on the data only through P(d_1|θ) (pdf 44)
- [[forward-and-inverse-probability]] (new) — computing data from a model vs inferring hidden variables from data (pdf 39)
- [[marginalization]] (new) — predicting by summing over hypotheses weighted by their posterior (pdf 41)
- [[cox-axioms]] (new) — consistency rules that map degrees of belief to probabilities (pdf 38)
- [[high-dimensional-shell-concentration]] (new) — most volume of an N-sphere lies in a thin outer shell (pdf 54)

## Canonical instances
- [[english-letter-ensemble]] — 27-symbol letter distribution; H ≈ 4.11 bits; h(z) = 10.4, h(e) = 3.5 (pdf 34, 44)
- [[english-bigram-ensemble]] — joint ensemble of adjacent letters with identical marginals (pdf 35)
- [[jo-disease-test]] — 95% reliable test, 1% prevalence, posterior 0.16 (pdf 37)
- [[eleven-urns]] — inverse probability and prediction with posterior table and 0.333 prediction (pdf 39–41)
- [[bent-coin-inference]] — unknown bias with a prior, and the link to compression (pdf 42–43)
- [[repetition-code-r3-error]] — P(error) = f³ + 3f²(1−f) via the sum rule (pdf 58)
- [[zipf-word-entropy]] — 9.7 bits per word under the 1/n law (pdf 52, 58)
- [[poissonville-bus-paradox]] — mean interval 6 vs 11 between sixes or buses (pdf 51, 57–58)

## Bridges (candidates)
- [same-math] Posterior ∝ likelihood × prior (2.28) ↔ machine learning: the same update used in Bayesian parameter estimation. It is literally the same formula.
- [same-math] D_KL(P‖Q) ≥ 0 via Jensen (2.95–2.96) ↔ statistics: the same convexity argument is used for the non-negativity of the log-likelihood-ratio expectation. Both are the same inequality on Σ P log P/Q.
- [structural-analogy] Entropy decomposition (2.43) ↔ probability: the product rule P(x,y) = P(x)P(y|x) applied to the log-probability. Averaging −log of the product rule gives a sum.
- [structural-analogy] Marginalizing over u for prediction (2.30) ↔ decision theory: averaging over model uncertainty instead of plugging in a point estimate.
- [structural-analogy] The "wrong-direction Jensen" lesson (choose u = 1/P(x)) ↔ optimization: choosing the right convex function and variable for a bound.
- [metaphor] Shell concentration in high dimensions ↔ typical sets: most probability sits away from the "centre". The later typical-set idea is similar in spirit, but the chapter does not make this link.

## Questions this raises
- If the prior is subjective, how sensitive are posteriors to it, for example in the bent-coin problem with N = 10 and n_H = 3 under different priors?
- Why does the author say data compression and data modelling are "one and the same"? How does a compressor use the predictive probability P(next = 1 | past)?
- Can the likelihood principle be reconciled with classical tests, whose answers depend on outcomes that did not happen?
- Entropy was defined for discrete alphabets. What changes for continuous densities, given that densities can exceed 1 (section 11.3)?

## Exercises worth doing
- Ex. 2.4 (pdf 39) — forward probability with the binomial; builds mean and variance fluency — difficulty: easy
- Ex. 2.8 (pdf 42) — posterior and prediction for the bent coin with a uniform prior using the beta integral — difficulty: medium
- Ex. 2.20 (pdf 49) — shell volume in high dimensions — difficulty: medium
- Ex. 2.25 (pdf 49) — H ≤ log|A_X| via Jensen; choosing the right function — difficulty: hard
- Ex. 2.26 (pdf 49) — Gibbs' inequality — difficulty: hard
- Ex. 2.35 (pdf 50) — waiting-time paradox — difficulty: medium
- Ex. 2.38 (pdf 51) — repetition code error by two methods; connects Bayes' rule to coding — difficulty: medium

## Reading notes
- The text layer shows the printed page as "?". The page images show printed numbers 22–46 for pdf pages 34–58 (printed = pdf − 12). I cite pdf numbers as instructed.
- The text layer drops some symbols, such as ε in Ex. 2.20 and many equations. I checked the equations against the page images.
- Solutions to Ex. 2.14 and 2.39 are brief. Ex. 2.39 only states the answer, 9.7 bits per word, with no derivation. Ex. 2.27 and Ex. 2.30–2.33 have no solutions in this unit.
- Pdf 38 labels the Cox axioms "Box 2.4" and the text cites "figure 2.4". This is a minor inconsistency in the source.
- Ex. 2.14's proof, as printed, excludes cases with some p_i = 0. The author says so.
- Example 2.10 and 2.11 numeric answers are not in the text. I computed 1/3 for both and marked it (added step).
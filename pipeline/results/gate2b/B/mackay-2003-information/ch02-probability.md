---
id: mackay-2003-information/ch02-probability
work: mackay-2003-information
unit: "2 Probability, Entropy, and Inference"
pages: 22–46
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
spec_version: 1.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Probability, Entropy, and Inference

## L0 — One line
Probability can describe both frequencies and degrees of belief; with Bayes' theorem it solves inverse problems, and its average-surprise measure, entropy, obeys inequalities (Gibbs, Jensen) that the rest of the book uses.

## L1 — The gist (≤ 120 words)
This chapter sets up the book's probability tools. It defines ensembles, joint, marginal and conditional probabilities, the product and sum rules, and Bayes' theorem. Probability serves both for frequencies and for degrees of belief (the Bayesian view). Inverse-probability examples (a disease test, eleven urns) show how prior, likelihood, posterior and evidence combine. They also show why a prediction should average over hypotheses. The chapter then defines Shannon information content, entropy and relative entropy, with proofs of Gibbs' inequality and the entropy bound via Jensen's inequality. Exercises cover high-dimensional spheres, dice sums and waiting times.

**Prerequisites:** sums and base-2 logarithms; conditional probability; expectation and variance; binomial coefficients; basic derivatives (and the idea of a convex curve).

## L2 — Key ideas (5–10 bullets)
- An *ensemble* (outcome, alphabet, probabilities) plus joint, marginal and conditional probabilities give a vocabulary for everything else. The product rule, sum rule and Bayes' theorem follow from the definitions (pp. 22–24).
- Bayes' theorem corrects an error the man in the street might make: reading a "95% reliable" test as a 95% chance of disease. With a 1% base rate the answer is 16% (p. 25).
- Probability can describe frequencies or degrees of belief. Beliefs satisfying the Cox axioms can be mapped onto probabilities. The author calls this the Bayesian (subjective) view; Bayesian advocates hold that you cannot do inference without making assumptions (p. 26).
- Forward problems start from a generative model (a model of the process that produces data) and compute the distribution of data-dependent quantities. Inverse problems compute unobserved variables given the observed data, using Bayes' theorem: posterior (belief after the data) = likelihood (probability of the observed data under each hypothesis) × prior (belief before the data) / evidence (the normalising constant). "Likelihood" is a function of the parameters, not a probability distribution over them (pp. 27–29).
- Predictions should marginalise over (average over) the posterior of the hypothesis, not use only the single most plausible hypothesis (eleven urns: 0.333 vs 0.3) (p. 29).
- The likelihood principle: given a generative model, once an outcome is observed, all inferences and predictions should depend only on the likelihood function of that outcome. The author says many classical methods violate it (p. 32).
- Shannon information content h(x) = log₂ 1/P(x) (in bits; rarer outcomes carry more). Entropy is its average over outcomes. It is maximal for the uniform distribution, additive for independent variables, and decomposes recursively (pp. 32–34).
- Gibbs' inequality (relative entropy, a difference measure between two distributions P and Q, is ≥ 0) and the bound H ≤ log|A_X| both follow from Jensen's inequality for convex functions (functions whose chords lie above the curve) (pp. 34–35, 44).
- For large N, almost all the volume of an N-dimensional sphere lies in a thin surface shell; a waiting-time exercise poses an apparent paradox: the interval spanning a random moment averages eleven rolls, not six (pp. 37, 39, 42, 46).

## L3 — Walkthrough

### Opening remark on notation (p. 22)
The author notes that one should sometimes distinguish a random variable, its value, and the proposition that it has that value. In practice he uses the simplest notation. For example, "true with probability 1" is usually just called "true" (p. 22).

### 2.1 Probabilities and ensembles (pp. 22–25)
**Ensemble.** An ensemble $X$ is a triple $(x, \mathcal{A}_X, \mathcal{P}_X)$. The outcome $x$ is the value of a random variable taking values in $\mathcal{A}_X=\{a_1,\dots,a_I\}$ with probabilities $\mathcal{P}_X=\{p_1,\dots,p_I\}$. Here $P(x=a_i)=p_i$, $p_i\ge 0$ and $\sum_{a_i\in\mathcal{A}_X}P(x=a_i)=1$. $\mathcal{A}$ stands for "alphabet" (p. 22).
- Example: a letter drawn from an English document. There are 27 outcomes, a–z and a space "–". Fig. 2.1 gives the probabilities, e.g. space 0.1928, e 0.0913, z 0.0007 (p. 22).
- Shorthand: $P(x=a_i)$ may be written $P(a_i)$ or $P(x)$ (p. 22).

**Probability of a subset** $T\subseteq\mathcal{A}_X$:
$$P(T)=P(x\in T)=\sum_{a_i\in T}P(x=a_i)\tag{2.1}$$
With $V=\{\mathtt{a,e,i,o,u}\}$ the author gets $P(V)=0.06+0.09+0.06+0.07+0.03=0.31$ (2.2) (p. 22).

**Joint ensemble.** $XY$ is an ensemble whose outcomes are ordered pairs $(x,y)$. $P(x,y)$ is the joint probability. The two variables are not necessarily independent (p. 22).

**Marginal probability** (p. 23):
$$P(x=a_i)\equiv\sum_{y\in\mathcal{A}_Y}P(x=a_i,y)\tag{2.3}$$
$$P(y)\equiv\sum_{x\in\mathcal{A}_X}P(x,y)\tag{2.4}$$

**Conditional probability** (p. 23):
$$P(x=a_i\mid y=b_j)\equiv\frac{P(x=a_i,y=b_j)}{P(y=b_j)}\quad\text{if }P(y=b_j)\ne 0\tag{2.5}$$
If $P(y=b_j)=0$ the conditional probability is undefined (p. 23).

**Example 2.1 (bigrams).** $XY$ is two successive letters of an English document (Fig. 2.2). Its two marginals $P(x)$ and $P(y)$ are identical and equal the monogram distribution of Fig. 2.1. Normalising rows gives $P(y\mid x)$ and normalising columns gives $P(x\mid y)$ (Fig. 2.3). Given first letter q, the two most probable second letters are u and space. The space is common because the source document uses the word FAQ heavily. Given second letter u, the two most probable first letters are n and o (pp. 23–24).

**Rules of probability** ($\mathcal{H}$ = the assumptions behind the probabilities) (p. 24):
- Product rule (also called the chain rule here):
$$P(x,y\mid\mathcal{H})=P(x\mid y,\mathcal{H})P(y\mid\mathcal{H})=P(y\mid x,\mathcal{H})P(x\mid\mathcal{H})\tag{2.6}$$
- Sum rule:
$$P(x\mid\mathcal{H})=\sum_y P(x,y\mid\mathcal{H})\tag{2.7}$$
$$=\sum_y P(x\mid y,\mathcal{H})P(y\mid\mathcal{H})\tag{2.8}$$
- Bayes' theorem:
$$P(y\mid x,\mathcal{H})=\frac{P(x\mid y,\mathcal{H})P(y\mid\mathcal{H})}{P(x\mid\mathcal{H})}\tag{2.9}$$
$$=\frac{P(x\mid y,\mathcal{H})P(y\mid\mathcal{H})}{\sum_{y'}P(x\mid y',\mathcal{H})P(y'\mid\mathcal{H})}\tag{2.10}$$
- Independence: $X$ and $Y$ are independent ($X\perp Y$) if and only if
$$P(x,y)=P(x)P(y)\tag{2.11}$$

Exercise 2.2 asks whether $X,Y$ of Fig. 2.2 are independent (p. 24). The printed solution is "no": if they were independent, all conditional distributions $P(y\mid x)$ would be identical functions of $y$ (p. 40).

**Example 2.3 (Jo's test).** Let $a=1$ mean Jo has the disease and $b=1$ mean a positive test. The test is "95% reliable". The prevalence among people of Jo's age and background is 1% (p. 25).
$$P(b{=}1\mid a{=}1)=0.95,\ P(b{=}1\mid a{=}0)=0.05,\ P(b{=}0\mid a{=}1)=0.05,\ P(b{=}0\mid a{=}0)=0.95\tag{2.13}$$
$$P(a{=}1)=0.01,\quad P(a{=}0)=0.99\tag{2.14}$$
From $P(a)$ and $P(b\mid a)$ one gets $P(a,b)=P(a)P(b\mid a)$. By the sum rule the chance of a positive result is
$$P(b{=}1)=P(b{=}1\mid a{=}1)P(a{=}1)+P(b{=}1\mid a{=}0)P(a{=}0)\tag{2.15}$$
**The man in the street** might say "the test is 95% reliable, so a positive result means a 95% chance of disease". The author calls this incorrect (p. 25). Bayes' theorem gives
$$P(a{=}1\mid b{=}1)=\frac{P(b{=}1\mid a{=}1)P(a{=}1)}{P(b{=}1\mid a{=}1)P(a{=}1)+P(b{=}1\mid a{=}0)P(a{=}0)}\tag{2.16}$$
$$=\frac{0.95\times0.01}{0.95\times0.01+0.05\times0.99}\tag{2.17}$$
$$=0.16\tag{2.18}$$
Despite the positive result the probability of disease is only 16% (p. 25). (added step: the numerator is 0.0095 and the denominator is 0.0095+0.0495 = 0.059.)

*Intuition note.* A test result is evidence, and it must be weighed against how common the disease is. Healthy people are so numerous that their 5% false positives outnumber the true positives.

### 2.2 The meaning of probability (pp. 25–27)
Probabilities can be used in two ways (p. 25):
1. **Frequencies of outcomes in random experiments.** The author notes that defining "frequency" and "random" without circularity is hard. "Average fraction of heads in long sequences" needs the word "average", which is hard to define without a synonym of probability. He will not try to resolve this (pp. 25–26).
2. **Degrees of belief in propositions** that do not involve random variables. His examples are Mr. S. being the murderer, Jefferson having a child by one of his slaves, Bacon writing Shakespeare's plays, and a signature on a cheque being genuine (p. 26).

The man in the street uses both senses. The author says some books on probability restrict probability to frequencies of repeatable random experiments (p. 26).

**Cox axioms (Box 2.4, p. 26).** $B(x)$ is the degree of belief in proposition $x$, $\bar x$ is its negation, and $B(x\mid y)$ is the belief in $x$ assuming $y$.
- Axiom 1: beliefs can be ordered, and the ordering is transitive. Consequence: beliefs can be mapped onto real numbers.
- Axiom 2: there is a function $f$ with $B(x)=f[B(\bar x)]$.
- Axiom 3: there is a function $g$ with $B(x,y)=g[B(x\mid y),B(y)]$.
- If beliefs satisfy these axioms, they can be mapped onto probabilities satisfying $P(\text{false})=0$, $P(\text{true})=1$, $0\le P(x)\le1$, $P(\bar x)=1-P(x)$ and $P(x,y)=P(x\mid y)P(y)$ (box caption, p. 26).

**Author's conclusion.** Degrees of belief can be mapped onto probabilities if they satisfy the Cox axioms. Probabilities can then describe assumptions and inferences given those assumptions. Two people with the same assumptions and the same data will draw identical conclusions (p. 26). This is the Bayesian, or subjective, viewpoint, because probabilities depend on assumptions. **Advocates of the Bayesian approach** do not see this as a defect, since in their view "you cannot do inference without making assumptions" (p. 26).

The author says he will sometimes take a Bayesian approach for granted. He warns that this is not globally held: statistics was dominated for most of the 20th century by non-Bayesian methods in which probabilities describe only random variables. The big difference is that Bayesians also use probabilities to describe inferences (pp. 26–27).

*Intuition note.* "Probability" here is a bookkeeping system for uncertain statements. Beliefs that satisfy the simple consistency rules of the Cox axioms can be mapped onto probabilities.

### 2.3 Forward probabilities and inverse probabilities (pp. 27–32)
**Forward probability.** A generative model describes a process assumed to produce data. The task is to compute the distribution or expectation of some quantity that depends on the data (p. 27).
- Exercise 2.4 (p. 27): an urn with $K$ balls, $B$ black and $W=K-B$ white. Fred draws with replacement $N$ times. Find the distribution, mean, variance and standard deviation of $n_B$ for $N=5$ and $N=400$ with $B=2$, $K=10$.
- Printed solution (p. 40): with $f_B\equiv B/K$, $n_B$ is binomial,
$$P(n_B\mid f_B,N)=\binom{N}{n_B}f_B^{n_B}(1-f_B)^{N-n_B}\tag{2.57}$$
$$\mathcal{E}[n_B]=Nf_B\tag{2.58}$$
$$\mathrm{var}[n_B]=Nf_B(1-f_B)\tag{2.59}$$
For $f_B=1/5$: $N=5$ gives mean 1, variance 4/5, standard deviation 0.89. $N=400$ gives mean 80, variance 64, standard deviation 8 (p. 40).
- Exercise 2.5 (p. 27): $z=\dfrac{(n_B-f_BN)^2}{Nf_B(1-f_B)}$ (2.19). Printed result: $\mathcal{E}[z]=1$ (the numerator's expectation is the variance in the denominator). For $N=5$, $f_B=1/5$: $P(z<1)=P(n_B=1)=0.4096$ (p. 40).

**Inverse probability.** There is also a generative model, but we compute the conditional probability of unobserved variables given the observed ones. This "invariably requires" Bayes' theorem (p. 27).

**Example 2.6 (eleven urns)** (pp. 27–28). There are eleven urns $u\in\{0,\dots,10\}$, each with ten balls. Urn $u$ has $u$ black balls and $10-u$ white. Fred picks an urn at random and draws $N$ times with replacement. Bill watches without knowing $u$. After $N=10$ draws with $n_B=3$ blacks, what is the probability of each $u$ from Bill's viewpoint?

Joint and conditional:
$$P(u,n_B\mid N)=P(n_B\mid u,N)P(u)\tag{2.20}$$
$$P(u\mid n_B,N)=\frac{P(u,n_B\mid N)}{P(n_B\mid N)}\tag{2.21}$$
$$=\frac{P(n_B\mid u,N)P(u)}{P(n_B\mid N)}\tag{2.22}$$
Here $P(u)=\tfrac1{11}$ for all $u$. With $f_u\equiv u/10$ (p. 28):
$$P(n_B\mid u,N)=\binom{N}{n_B}f_u^{n_B}(1-f_u)^{N-n_B}\tag{2.23}$$
The denominator is obtained by the sum rule:
$$P(n_B\mid N)=\sum_uP(u,n_B\mid N)=\sum_uP(u)P(n_B\mid u,N)\tag{2.24}$$
$$P(u\mid n_B,N)=\frac{P(u)P(n_B\mid u,N)}{P(n_B\mid N)}\tag{2.25}$$
$$=\frac{1}{P(n_B\mid N)}\frac1{11}\binom{N}{n_B}f_u^{n_B}(1-f_u)^{N-n_B}\tag{2.26}$$
This is column 3 of Fig. 2.5 normalised. The normalising constant is $P(n_B=3\mid N=10)=0.083$. The posterior (Fig. 2.6) is:

| u | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $P(u\mid n_B{=}3,N)$ | 0 | 0.063 | 0.22 | 0.29 | 0.24 | 0.13 | 0.047 | 0.0099 | 0.00086 | 0.0000096 | 0 |

Equation (2.26) holds for all $u$, including the end-points. $u=0$ gets zero posterior because no black balls could be drawn, and $u=10$ gets zero because there are no white balls. Hypotheses $u=1,\dots,9$ have non-zero posterior (p. 28).

**Terminology (pp. 28–29).**
- $P(u)$ is the *prior*; $P(n_B\mid u,N)$ is the *likelihood* of $u$.
- Likelihood and probability are not synonyms. $P(n_B\mid u,N)$ is a function of both $n_B$ and $u$. For fixed $u$ it defines a probability over $n_B$. For fixed $n_B$ it defines the likelihood of $u$ (p. 28).
- Rule: never say "the likelihood of the data"; say "the likelihood of the parameters". The likelihood function is not a probability distribution (p. 29).
- $P(u\mid n_B,N)$ is the *posterior*. The constant $P(n_B\mid N)$ does not depend on $u$, so it is unimportant for relative probabilities. In complex data-modelling problems it becomes important and is called the *evidence* or *marginal likelihood* (p. 29).
- General form, with $\boldsymbol\theta$ the unknown parameters, $D$ the data and $\mathcal{H}$ the hypothesis space:
$$P(\boldsymbol\theta\mid D,\mathcal{H})=\frac{P(D\mid\boldsymbol\theta,\mathcal{H})P(\boldsymbol\theta\mid\mathcal{H})}{P(D\mid\mathcal{H})}\tag{2.27}$$
$$\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}\tag{2.28}$$

**Prediction (Example 2.6 continued, p. 29).** What is the probability that the next ball is black? By the sum rule:
$$P(\text{ball}_{N+1}\text{ black}\mid n_B,N)=\sum_uP(\text{ball}_{N+1}\text{ black}\mid u,n_B,N)P(u\mid n_B,N)\tag{2.29}$$
Draws are with replacement, so the first factor is $f_u=u/10$ whatever $n_B,N$ are:
$$=\sum_uf_uP(u\mid n_B,N)\tag{2.30}$$
Using Fig. 2.6, this gives $0.333$ (2.31) (p. 29).
- **Widespread statistical practice (as the author describes it):** first pick the most plausible hypothesis ($u=3$) and then predict assuming it is true. That gives 0.3.
- The author's view: the correct prediction marginalises over $u$ and takes uncertainty into account. Marginalisation here gives "slightly more moderate, less extreme" predictions (p. 29).

*Intuition note.* The posterior over urns is a weighted list of possible worlds. A prediction is the weighted average of what each world predicts, not what the single favourite world predicts.

**Example 2.7 (bent coin)** (p. 30). Bill tosses a coin with unknown bias $f_H$ $N$ times and gets $n_H$ heads (e.g. $N=10$, $n_H=3$; or $N=300$, $n_H=29$). What is the distribution of $f_H$, and the probability that toss $N{+}1$ is a head?
- The author says this has a subjective element. Under a restricted definition ("probabilities are frequencies of random variables") the coin's bias is a fixed unknown parameter, not a random variable. Yet he asks whether the two examples do not seem to have an essential similarity (p. 30).
- We must assume a prior $P(f_H)$, which corresponds to $P(u)$ in the urns. Likelihoods also rest on assumptions (e.g. independent draws). In real problems "priors are subjective and so are likelihoods" (p. 30).
- Densities: $P(\cdot)$ now also denotes probability densities. $\Pr(a<v<b)=\int_a^b dv\,P(v)$. $P(v)\,dv$ is dimensionless, while $P(v)$ has dimensions inverse to $v$. Densities greater than 1 are normal as long as $\int_a^bdv\,P(v)\le1$ for any interval (p. 30).
- Exercise 2.8 (p. 30): with uniform prior $P(f_H)=1$, solve the problem for $(N,n_H)=(3,0),(3,2),(10,3),(300,29)$. The beta integral to use is
$$\int_0^1dp_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!F_b!}{(F_a+F_b+1)!}\tag{2.32}$$
- **Prior ≠ guess.** A prior over $f_H$ is a density that gives the degree of belief that $f_H$ lies in any interval. It is not a statement such as "I guess $f_H=1/2$". If the prior is symmetric about 1/2, then
$$P(x_1=\text{head})=\int df_H\,P(f_H)P(x_1=\text{head}\mid f_H)=\int df_H\,P(f_H)f_H=1/2\tag{2.33}$$
but predictions for later tosses depend on the whole prior, not only its mean (p. 31).

**Example 2.9 (data compression)** (p. 31). Compress a binary file of 300 characters with $n_1=29$ ones and $n_0=271$ zeros. A compressor must, implicitly or explicitly, answer "what is the probability that the next character is a 1?" The author says this is similar in character to Example 2.7. A theme of the book is that data compression and data modelling are the same and should be addressed by inverse probability. Example 2.9 is solved in Chapter 6 (p. 31).

**The likelihood principle (Examples 2.10, 2.11; pp. 31–32).**
- Example 2.10: urn A has 1 black and 2 white balls; urn B has 2 black and 1 white. One urn is chosen at random and one ball drawn. It is black. What is the probability that the urn is A?
- Example 2.11: urn A has 5 balls (1 black, 2 white, 1 green, 1 pink). Urn B has 500 balls (200 black, 100 white, 50 yellow, 40 cyan, 30 sienna, 25 green, 25 silver, 20 gold, 10 purple). One fifth of A's balls and two fifths of B's are black. A black ball is drawn. What is the probability that the urn is A?
- The author asks whether each answer depends on the detailed contents of the urns. His point: the details of the other possible outcomes are irrelevant. All that matters is how the probability of the outcome that happened varies with the hypothesis, i.e. the likelihood (p. 32).
- **Likelihood principle.** Given a generative model $P(d\mid\boldsymbol\theta)$ and an observed outcome $d_1$, all inferences and predictions should depend only on the function $P(d_1\mid\boldsymbol\theta)$ (p. 32). The author says many classical statistical methods violate it (p. 32).

### 2.4 Definition of entropy and related functions (pp. 32–33)
**Shannon information content** of an outcome, measured in bits:
$$h(x)=\log_2\frac1{P(x)}\tag{2.34}$$
"Bit" also names a variable that is 0 or 1; context shows which meaning is intended (p. 32). Table 2.9 gives $h$ for each letter: $z$ has 10.4 bits, $e$ has 3.5 bits, space has 2.4 bits (p. 32). The author says the next chapters will show that $h$ is a natural measure of information content (p. 32).

**Entropy** of an ensemble is the average Shannon information content:
$$H(X)\equiv\sum_{x\in\mathcal{A}_X}P(x)\log\frac1{P(x)}\tag{2.35}$$
with the convention $0\times\log1/0\equiv0$, since $\lim_{\theta\to0^+}\theta\log1/\theta=0$. It is measured in bits. It may be written $H(\mathbf p)$, and it is also called the uncertainty of $X$ (p. 32).

**Example 2.12.** The entropy of a random English letter is about 4.11 bits, using the probabilities of Table 2.9 (p. 32).

**Properties (p. 33).**
- $H(X)\ge0$, with equality iff $p_i=1$ for one $i$.
- $H(X)\le\log|\mathcal{A}_X|$, with equality iff $p_i=1/|\mathcal{A}_X|$ for all $i$ (2.36).
- **Redundancy** (not used further in the book): $1-\dfrac{H(X)}{\log|\mathcal{A}_X|}$ (2.37).
- **Joint entropy:**
$$H(X,Y)=\sum_{xy\in\mathcal{A}_X\mathcal{A}_Y}P(x,y)\log\frac1{P(x,y)}\tag{2.38}$$
- Additivity: $H(X,Y)=H(X)+H(Y)$ iff $P(x,y)=P(x)P(y)$ (2.39).
- These definitions are for discrete distributions over finite sets. They can be extended to infinite sets, but the entropy may then be infinite. The continuous case is deferred to section 11.3 (p. 33).

*Intuition note.* Rare outcomes are more informative, and entropy is the average of that surprise. It is largest when all outcomes are equally likely and zero when the outcome is certain.

### 2.5 Decomposability of the entropy (pp. 33–34)
**Example.** $x\in\{0,1,2\}$ is made by a fair coin flip deciding whether $x=0$. If not, a second fair flip decides between 1 and 2. So $P(x{=}0)=\tfrac12$, $P(x{=}1)=P(x{=}2)=\tfrac14$ (2.40) (p. 33).
- Brute force: $H(X)=\tfrac12\log2+\tfrac14\log4+\tfrac14\log4=1.5$ (2.41) (p. 33).
- Decomposition: first learn whether $x=0$ (a binary variable with entropy $H(\tfrac12,\tfrac12)=1$ bit). Then, half the time, learn the second flip (also 1 bit):
$$H(X)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac12,\tfrac12)\tag{2.42}$$
(p. 34).

**General form** for $\mathbf p=\{p_1,\dots,p_I\}$ (p. 34):
$$H(\mathbf p)=H(p_1,1-p_1)+(1-p_1)H\!\left(\frac{p_2}{1-p_1},\frac{p_3}{1-p_1},\dots,\frac{p_I}{1-p_1}\right)\tag{2.43}$$
and for any $m$:
$$H(\mathbf p)=H[(p_1+\dots+p_m),(p_{m+1}+\dots+p_I)]+(p_1+\dots+p_m)H\!\left(\frac{p_1}{p_1+\dots+p_m},\dots,\frac{p_m}{p_1+\dots+p_m}\right)+(p_{m+1}+\dots+p_I)H\!\left(\frac{p_{m+1}}{p_{m+1}+\dots+p_I},\dots,\frac{p_I}{p_{m+1}+\dots+p_I}\right)\tag{2.44}$$

**Example 2.13.** A source emits a character from $\{0,\dots,9,\mathtt a,\dots,\mathtt z\}$. With probability 1/3 it is a numeral, with probability 1/3 a vowel (5 vowels) and with probability 1/3 one of the 21 consonants. Within each class all characters are equiprobable (p. 34).
$$H=\log3+\tfrac13(\log10+\log5+\log21)=\log3+\tfrac13\log1050\simeq\log30\text{ bits}$$
(p. 34).

*Intuition note.* Entropy can be computed in stages. First reveal which group the outcome is in; then reveal the outcome inside the group, weighting that second entropy by the chance that the group occurs.

### 2.6 Gibbs' inequality (p. 34)
**Relative entropy (Kullback–Leibler divergence)** between $P(x)$ and $Q(x)$ over the same alphabet:
$$D_{\mathrm{KL}}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}\tag{2.45}$$
**Gibbs' inequality:** $D_{\mathrm{KL}}(P\|Q)\ge0$ (2.46), with equality only if $P=Q$. In general $D_{\mathrm{KL}}(P\|Q)\neq D_{\mathrm{KL}}(Q\|P)$, so it is sometimes called the "KL distance" but is not strictly a distance. The author says it is important in pattern recognition and neural networks as well as information theory, and calls Gibbs' inequality "probably the most important inequality in this book" (p. 34). The proof is given in the solution to Exercise 2.26 (see 2.10 below).

*Intuition note.* KL divergence is never negative. It is zero only when the two distributions are the same. In general it is not symmetric, so it is not strictly a distance.

### 2.7 Jensen's inequality for convex functions (pp. 35–36)
**Convex.** A function $f(x)$ is convex (⌣, "convex-smile") over $(a,b)$ if every chord lies above the function. For all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$:
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)\tag{2.47}$$
It is strictly convex if equality holds only for $\lambda=0$ and $\lambda=1$. Concave (⌢) is the mirror image (p. 35).
- Strictly convex examples: $x^2$, $e^x$, $e^{-x}$ for all $x$; $\log(1/x)$ and $x\log x$ for $x>0$ (p. 35).

**Jensen's inequality.** If $f$ is convex and $x$ is a random variable,
$$\mathcal{E}[f(x)]\ge f(\mathcal{E}[x])\tag{2.48}$$
If $f$ is strictly convex and $\mathcal{E}[f(x)]=f(\mathcal{E}[x])$, then $x$ is a constant. For concave $f$ the inequality reverses (p. 35).
- Physical version: masses $p_i$ placed on a convex curve at $(x_i,f(x_i))$ have their centre of gravity, at $(\mathcal{E}[x],\mathcal{E}[f(x)])$, above the curve (p. 35).

**Proof (Exercise 2.14, printed solution, p. 41).** Given convexity (2.60), $f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)$, we want $\sum_ip_if(x_i)\ge f(\sum_ip_ix_i)$ (2.61) for $\sum p_i=1$, $p_i\ge0$. The proof works from the right-hand side by recursion. It does not handle cases where some $p_i=0$. In the first line $\lambda=p_1/\sum_{i=1}^Ip_i=p_1$, and in the second line $\lambda=p_2/\sum_{i=2}^Ip_i$:
$$f\Big(\sum_{i=1}^Ip_ix_i\Big)=f\Big(p_1x_1+\sum_{i=2}^Ip_ix_i\Big)$$
$$\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]\Big[f\Big(\sum_{i=2}^Ip_ix_i\Big/\sum_{i=2}^Ip_i\Big)\Big]$$
$$\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]\Big[\frac{p_2}{\sum_{i=2}^Ip_i}f(x_2)+\frac{\sum_{i=3}^Ip_i}{\sum_{i=2}^Ip_i}f\Big(\sum_{i=3}^Ip_ix_i\Big/\sum_{i=3}^Ip_i\Big)\Big]\tag{2.62}$$
"and so forth" (p. 41).

**Example 2.15 (three squares).** Average area $\bar A=100\,\mathrm m^2$ and average side length $\bar l=10$ m. Let $x$ be a side length, with probability 1/3 on each of $l_1,l_2,l_3$. Then $\mathcal{E}[x]=10$ and $\mathcal{E}[f(x)]=100$ with $f(x)=x^2$, which is strictly convex. Since $\mathcal{E}[f(x)]=f(\mathcal{E}[x])$, $x$ is constant. All three lengths are equal and the largest square has area $100\,\mathrm m^2$ (p. 35).

**Convexity and maximisation (p. 36).** If $f(\mathbf x)$ is concave and there is a point where $\partial f/\partial x_k=0$ for all $k$ (2.49), then $f$ has its maximum there. The converse does not hold. Examples: $f(x)=-|x|$ is maximised at $x=0$, where the derivative is undefined; $f(p)=\log p$ on $p\in(0,1)$ is maximised on the boundary at $p=1$, where the gradient is 1 (as printed) (p. 36).

*Intuition note.* For a bowl-shaped function, the average of the heights is at least the height at the average position. Applying this to well-chosen functions proves the entropy bound and Gibbs' inequality (p. 44).

### 2.8 Exercises (pp. 36–38)
The exercises are listed with their printed solutions (section 2.10).
- **2.16 Sums of random variables** (p. 36). (a) Distribution of the sum and the absolute difference of two dice. (b) Sum of 100 dice (central-limit theorem). (c) Label two cubes with $\{0,\dots,6\}$ so the sum is uniform on 1–12. (d) Can 100 dice give a uniform sum?
- **2.17** (p. 36). If $q=1-p$ and $a=\ln p/q$, show $p=1/(1+\exp(-a))$ (2.50). Relate it to $\tanh$, and find $p$ for $b=\log_2p/q$.
- **2.18** (p. 36). The log posterior ratio for binary $x$ is
$$\log\frac{P(x{=}1\mid y)}{P(x{=}0\mid y)}=\log\frac{P(y\mid x{=}1)}{P(y\mid x{=}0)}+\log\frac{P(x{=}1)}{P(x{=}0)}\tag{2.51}$$
- **2.19** (p. 36). If $d_1,d_2$ are conditionally independent given binary $x$:
$$\frac{P(x{=}1\mid\{d_i\})}{P(x{=}0\mid\{d_i\})}=\frac{P(d_1\mid x{=}1)}{P(d_1\mid x{=}0)}\frac{P(d_2\mid x{=}1)}{P(d_2\mid x{=}0)}\frac{P(x{=}1)}{P(x{=}0)}\tag{2.52}$$
- **2.20 High dimensions** (p. 37). The fraction of an $N$-dimensional sphere's volume within $\epsilon$ of the surface (radius between $r-\epsilon$ and $r$) is
$$f=1-\Big(1-\frac\epsilon r\Big)^N\tag{2.53}$$
Implication: uniformly distributed points in a high-dimensional sphere are very likely to be in a thin shell near the surface (p. 37).
- **2.21–2.24** (pp. 37, 43). Expectations $\mathcal{E}[f(x)]=\langle f(x)\rangle=\sum_xP(x)f(x)$ (2.54), including cases where $f$ depends on $P(x)$.
- **2.25, 2.26, 2.27** (p. 37). Prove $H\le\log|\mathcal{A}_X|$, Gibbs' inequality, and the decomposition (2.43–2.44).
- **2.28** (p. 38). A four-outcome variable built from three bent coins (biases $f$, $g$, $h$) via a tree.
- **2.29** (p. 38). The entropy of the number of flips until the first head.

### 2.9 Further exercises (pp. 38–39)
Forward probability (p. 38):
- 2.30: without replacement, the first and second ball are equally likely to be white.
- 2.31: circular coin of diameter $a$ on a $b\times b$ grid; the author gives the answer $(1-a/b)^2$.
- 2.32: Buffon's needle; the author gives $2a/\pi b$ for $a<b$, and $2A/\pi b$ expected crossings for a random curve of length $A$ ("Buffon's noodle").
- 2.33: a triangle from two random cuts of a unit segment.
- 2.34: an unbiased coin flipped until one head; Fred estimates the bias by $\hat f=h/(h+t)$. This is a forward (sampling-theory) problem; do not use Bayes' theorem.
- 2.35: waiting times for sixes on a die rolled once per second.

Conditional probability (p. 39):
- 2.36: Fred and his brothers Alf and Bob, and the conditional probability that Fred is older than Bob given that he is older than Alf.
- 2.37: islanders who tell the truth one third of the time.
- 2.38: the error probability of the repetition code $R_3$ on a binary symmetric channel, by a binomial method and by a sum-rule method. The sum-rule route uses $P(\text{error})=\sum_{\mathbf r}P(\mathbf r)P(\text{error}\mid\mathbf r)$ (2.55).

Also 2.39 (p. 40): word frequencies follow $p_n\simeq0.1/n$ for $n=1,\dots,12\,367$ and 0 beyond (2.56) (Zipf's law). If English is generated by picking words at random from this distribution, what is its entropy per word? The author notes that Shannon's published calculation contains numerical errors.

### 2.10 Solutions (pp. 40–46)
Printed solutions are summarised here; for some only final results are given.
- **2.2, 2.4, 2.5:** see above (p. 40).
- **2.14:** Jensen's proof, given above (p. 41).
- **2.16** (p. 41). (a) The sum of two dice has probabilities $\{1,2,3,4,5,6,5,4,3,2,1\}/36$ for outcomes 2–12. (b) One die has mean 3.5 and variance 35/12. One hundred dice have mean 350 and variance $3500/12\simeq292$, and by the central-limit theorem the distribution is roughly Gaussian. (c) The unique solution is one ordinary die and one with faces 6, 6, 6, 0, 0, 0. (d) Yes, e.g. label the $r$th die with $\{0,\dots,5\}\times6^r$. The author invites the reader to think whether this contradicts the central-limit theorem.
- **2.17** (p. 41–42). From $a=\ln p/q$: $p/q=e^a$ (2.63), $p/(1-p)=e^a$ (2.64), so $p=e^a/(e^a+1)=1/(1+\exp(-a))$ (2.65). Using $\tanh(a)=\frac{e^a-e^{-a}}{e^a+e^{-a}}$ (2.66):
$$f(a)\equiv\frac1{1+\exp(-a)}=\frac12\Big(\frac{1-e^{-a}}{1+e^{-a}}+1\Big)=\frac12\Big(\frac{e^{a/2}-e^{-a/2}}{e^{a/2}+e^{-a/2}}+1\Big)=\frac12(\tanh(a/2)+1)\tag{2.67}$$
For $b=\log_2p/q$: $p=1/(1+2^{-b})$ (2.68).
- **2.18** (p. 42). From Bayes, $P(x\mid y)=P(y\mid x)P(x)/P(y)$ (2.69). The ratio for $x=1$ over $x=0$ cancels $P(y)$ (2.70), and taking logs gives (2.71).
- **2.19** (p. 42). Conditional independence means $P(x,d_1,d_2)=P(x)P(d_1\mid x)P(d_2\mid x)$ (2.72). So the posterior ratio is a prior ratio times one factor per data point, (2.73)–(2.74).
- **2.20** (p. 42). Only the scaling $V(r,N)\propto r^N$ is needed (the full volume is $\pi^{N/2}r^N/(N/2)!$, 2.75). The shell fraction is $\frac{r^N-(r-\epsilon)^N}{r^N}=1-(1-\epsilon/r)^N$ (2.76). Final table:

| | N = 2 | N = 10 | N = 1000 |
|---|---|---|---|
| ε/r = 0.01 | 0.02 | 0.096 | 0.99996 |
| ε/r = 0.5 | 0.75 | 0.999 | $1-2^{-1000}$ |

No matter how small $\epsilon$ is, for large enough $N$ essentially all the mass is in the surface shell (p. 42).
- **2.21–2.24** (p. 43), with $p_a=0.1$, $p_b=0.2$, $p_c=0.7$.
  - $\mathcal{E}[f(x)]=0.1\times10+0.2\times5+0.7\times10/7=3$ (2.77). Since $f(x)=1/P(x)$ for each $x$, $\mathcal{E}[1/P(x)]=3$ (2.78).
  - For any ensemble, $\mathcal{E}[1/P(x)]=\sum_x1=|\mathcal{A}_X|$ (2.79).
  - $\mathcal{E}[g(x)]=p_b=0.2$ (2.80).
  - $P(P(x)\in[0.15,0.5])=p_b=0.2$ (2.81). $P(|\log\frac{P(x)}{0.2}|>0.05)=p_a+p_c=0.8$ (2.82).
- **2.25** (pp. 43–44). Two methods.
  - *By differentiation (author: not recommended).* Use natural logs temporarily. $H=\sum_ip_i\ln\frac1{p_i}$ (2.83), $\frac{\partial H}{\partial p_i}=\ln\frac1{p_i}-1$ (2.84). Enforce $\sum p_i=1$ with a Lagrange multiplier: $G(\mathbf p)=H+\lambda(\sum_ip_i-1)$ (2.85), $\frac{\partial G}{\partial p_i}=\ln\frac1{p_i}-1+\lambda$ (2.86). At a maximum $\ln\frac1{p_i}-1+\lambda=0$ (2.87), so $\ln\frac1{p_i}=1-\lambda$ (2.88) and all $p_i$ are equal. The curvature is $\frac{\partial^2G}{\partial p_i\partial p_j}=-\frac1{p_i}\delta_{ij}$ (2.89), negative definite, so the extremum is a maximum. The author warns that this method is risky, since a maximum may lie on a boundary where the derivative is not zero (p. 43).
  - *By Jensen (recommended).* Choosing $f(u)=\log\frac1u=-\log u$ (convex) with $u=P(x)$ gives an inequality in the wrong direction. Instead take $u=1/P(x)$:
$$H(X)=-\mathcal{E}[f(1/P(x))]\le-f(\mathcal{E}[1/P(x)])\tag{2.92}$$
Since $\mathcal{E}[1/P(x)]=|\mathcal{A}_X|$ (2.79), $H(X)\le-f(|\mathcal{A}_X|)=\log|\mathcal{A}_X|$ (2.93). Equality holds only if $u=1/P(x)$ is constant, i.e. $P(x)$ is constant for all $x$ (p. 44). (added step: $f(1/P)=\log P$, so $\mathcal{E}[f(1/P)]=-H$.)
- **2.26 (Gibbs' inequality, p. 44).** First proof: let $f(u)=\log1/u$ and $u=Q(x)/P(x)$, with the expectation over $P$.
$$D_{\mathrm{KL}}(P\|Q)=\mathcal{E}[f(Q(x)/P(x))]\tag{2.95}$$
$$\ge f\Big(\sum_xP(x)\frac{Q(x)}{P(x)}\Big)=\log\Big(\frac1{\sum_xQ(x)}\Big)=0\tag{2.96}$$
(The last step uses $\sum_xQ(x)=1$ (added step).) Equality only if $u=Q/P$ is constant, i.e. $Q=P$. Second proof: let $f(u)=u\log u$ and $u=P(x)/Q(x)$, with the expectation over $Q$.
$$D_{\mathrm{KL}}(P\|Q)=\sum_xQ(x)\frac{P(x)}{Q(x)}\log\frac{P(x)}{Q(x)}=\sum_xQ(x)f\Big(\frac{P(x)}{Q(x)}\Big)\tag{2.97}$$
$$\ge f\Big(\sum_xQ(x)\frac{P(x)}{Q(x)}\Big)=f(1)=0\tag{2.98}$$
with equality only if $P/Q$ is constant (p. 44).
- **2.28** (p. 45). $H(X)=H_2(f)+fH_2(g)+(1-f)H_2(h)$ (2.99), where $H_2$ is the binary entropy function (its definition is not printed in these pages; by (2.43) it is the entropy of $\{x,1-x\}$).
- **2.29** (p. 45). Final result for the fair-coin and biased-coin cases: $H(X)=H_2(f)/f$ (2.102), with $P(x)=(1-f)^{x-1}f$.
- **2.34** (p. 45). The number of tails has $P(t)=(1/2)^t\cdot\frac12$ for $t\ge0$ (2.103). The expected number of heads is 1 by the problem's definition. $\mathcal{E}[t]=\sum_tt(1/2)^t\frac12=1$, shown via $\mathcal{E}[t]=\tfrac12(1+\mathcal{E}[t])+\tfrac12\cdot0$ (2.104–2.105). The distribution of $\hat f=1/(1+t)$ for $f=1/2$ is plotted in Fig. 2.12, and $P(\hat f)$ is the probability of the corresponding $t$.
- **2.35** (pp. 45–46), final results only. The mean number of rolls from a six to the next six is six. From a random time (the clock striking) to the next six it is six. Going back in time to the most recent six it is six. From the six before the clock to the six after it, it is eleven. The author gives Poissonville bus hints in place of an explanation of (e). The distribution of $r_1$ has $P(r_1>6)\approx1/3$, while $P(r_{\rm tot}>6)\approx2/3$ (Fig. 2.13).
- **2.38** (p. 46), final result: both methods give $P(\text{error})=f^3+3f^2(1-f)$.
- **2.39** (p. 46): the entropy is 9.7 bits per word.

*Intuition note.* The author does not explain the paradox in the printed solution; he gives a hint (p. 46): when buses arrive at random, more passengers meet the long gaps than the short ones, so a typical passenger sits in a longer-than-average gap. The eleven rolls in (d), against six in (a), is presumably the effect this hint points to.

## Toy example (ours, not from the text)
Two urns, each with 10 balls. Urn L has 2 black balls ($f=0.2$) and urn H has 8 ($f=0.8$). A fair coin picks the urn, so the prior is $P(L)=P(H)=0.5$. We draw 2 balls with replacement and see two blacks. What is the probability that the next ball is black?

1. Likelihoods (binomial, $N=2$, $n_B=2$): $P(\text{BB}\mid L)=0.2^2=0.04$ and $P(\text{BB}\mid H)=0.8^2=0.64$.
2. Evidence by the sum rule: $P(\text{BB})=0.5\times0.04+0.5\times0.64=0.02+0.32=0.34$.
3. Posterior by Bayes: $P(L\mid\text{BB})=0.02/0.34=0.0588$ and $P(H\mid\text{BB})=0.32/0.34=0.9412$ (these sum to 1).
4. Prediction by marginalising: $P(\text{next black})=0.2\times0.0588+0.8\times0.9412=0.01176+0.75294=0.7647$ (equivalently $0.26/0.34$).
5. Compare "pick the most plausible urn": H, predicting 0.8. Marginalising gives the slightly more moderate 0.765, the same effect as 0.333 vs 0.3 in the eleven-urns example.

## Concepts
- [[ensemble]] (new) — triple of outcome, alphabet and probabilities; defines a random variable (p. 22)
- [[joint-and-conditional-entropy]] — here only joint entropy $H(X,Y)$ is defined (2.38); additive iff independent (p. 33)
- [[marginalization]] (new) — summing a joint probability over other variables (the sum rule), used for evidence and predictions (pp. 23, 24, 29)
- [[product-rule]] (new) — $P(x,y)=P(x\mid y)P(y)$; the author also calls it the chain rule (for probabilities here, not entropies) (p. 24)
- [[bayes-theorem]] — posterior from likelihood and prior, normalised by a sum over hypotheses (p. 24)
- [[independence]] (new) — $P(x,y)=P(x)P(y)$, iff (p. 24)
- [[probability-as-extended-logic]] — the author's Cox-axiom route: consistent beliefs map to probabilities (p. 26)
- [[cox-theorem]] — the author states the three Cox axioms and that consistent beliefs can be mapped to probabilities (p. 26)
- [[subjective-probability]] — author's "Bayesian/subjective interpretation": probabilities depend on assumptions (p. 26)
- [[frequentist-vs-bayesian-inference]] — frequencies only vs. beliefs about unknowns; author says non-Bayesian methods dominated 20th-century statistics (pp. 25–27)
- [[forward-probability]] (new) — compute data distributions from a generative model (p. 27)
- [[inverse-probability]] (new) — compute unobserved variables given observed ones, by Bayes' theorem (p. 27)
- [[prior-distribution]] — $P(u)$ or $P(\theta\mid\mathcal H)$: a density or distribution, not a point guess (pp. 29, 31)
- [[likelihood]] — $P(D\mid\theta)$ as a function of $\theta$; not a probability distribution; "likelihood of the parameters" (pp. 28–29)
- [[posterior-distribution]] — $P(\theta\mid D,\mathcal H)$ (p. 29)
- [[marginal-likelihood]] — the evidence $P(D\mid\mathcal H)$, the normalising constant (p. 29)
- [[posterior-predictive-distribution]] — prediction by averaging over the posterior, eqs. 2.29–2.31 (p. 29)
- [[likelihood-principle]] (new) — inferences depend only on the likelihood function of the observed outcome (p. 32)
- [[self-information]] — Shannon information content $h(x)=\log_2 1/P(x)$ (p. 32)
- [[entropy]] — average Shannon information content, $H(X)$ (2.35) (p. 32)
- [[redundancy]] — $1-H(X)/\log|\mathcal A_X|$ (2.37) (p. 33)
- [[entropy-decomposability]] (new) — recursive formulas (2.43–2.44) (p. 34)
- [[kl-divergence]] — relative entropy $D_{\rm KL}(P\|Q)$; non-negative and asymmetric (p. 34)
- [[gibbs-inequality]] (new) — $D_{\rm KL}\ge0$ with equality only if $P=Q$ (p. 34)
- [[convexity]] (new) — chord-above-curve definition, eq. 2.47 (p. 35)
- [[jensen-inequality]] (new) — $\mathcal E[f(x)]\ge f(\mathcal E[x])$ for convex $f$ (p. 35)
- [[concentration-in-high-dimensions]] (new) — in an $N$-dimensional sphere most volume lies near the surface (pp. 37, 42)

## Canonical instances
- [[english-letter-ensemble]] — 27-letter distribution and information contents; entropy ≈ 4.11 bits (pp. 22, 32)
- [[english-bigrams]] — joint ensemble with equal marginals; conditional distributions by row/column normalisation (pp. 23–24)
- [[jo-disease-test]] — positive result from a 95%-reliable test with 1% prevalence gives 16% (p. 25)
- [[eleven-urns]] — inverse-probability example: posterior over urns after 3 blacks in 10 draws, and prediction 0.333 (pp. 27–29)
- [[bent-coin]] — inference about an unknown bias with a prior; compared with eleven urns (p. 30)
- [[binary-file-compression-example]] — 29 ones and 271 zeros; compression as prediction, solved in Ch. 6 (p. 31)
- [[urn-a-b-likelihood-principle]] — Examples 2.10 and 2.11 for the likelihood principle (p. 31)
- [[three-squares-jensen]] — equality case of Jensen forces equal side lengths (p. 35)
- [[repetition-code-r3]] — $P(\text{error})=f^3+3f^2(1-f)$ (pp. 39, 46)
- [[zipf-law-english-entropy]] — $p_n\simeq0.1/n$, entropy 9.7 bits per word (pp. 40, 46)
- [[poissonville-buses]] — waiting-time paradox; mean 6-minute wait, 12 minutes between buses (pp. 39, 46)

## Bridges (candidates)
- [structural-analogy] Posterior/prior/likelihood/evidence ↔ model comparison: the evidence $P(D\mid\mathcal H)$ is the normalising constant; the author says it becomes important in data-modelling problems of any complexity (p. 29).
- [same-math] $D_{\mathrm{KL}}(P\|Q)\ge0$ via Jensen ↔ information theory: the relative entropy of the canon, with the same formula (2.45).
- [structural-analogy] Shell concentration in high-dimensional spheres ↔ typical set: mass sits away from the centre, in a thin region (canon link; not stated in this unit).
- [structural-analogy] Marginalising over $u$ for prediction ↔ posterior predictive distribution in Bayesian workflow (pp. 28–29).
- [same-math] Log posterior odds = log likelihood ratio + log prior odds (2.51) ↔ logistic function: $p=1/(1+e^{-a})$ (2.50) (Ex. 2.17–2.18, pp. 36, 41–42).
- [metaphor] Data compression as prediction of the next symbol ↔ inference: the author says both are inverse-probability problems (p. 31).

## Questions this raises
- If the likelihood principle holds, how should one assess a procedure's long-run performance, which classical methods care about?
- How do the 16% disease result and the 0.333 urn prediction change as the prior changes? What sensitivity to the prior is acceptable?
- How is relative entropy $D_{\rm KL}(P\|Q)$ interpreted as extra bits when coding data from $P$ with a code built for $Q$ (not covered in this unit)?
- Why do waiting intervals that contain a random moment have a longer mean than ordinary intervals (Ex. 2.35)?

## Exercises worth doing
- Ex. 2.8 (p. 30) — posterior of an unknown coin bias with a uniform prior and the predictive probability for the next toss; the direct counterpart of eleven urns — difficulty: medium
- Ex. 2.20 (p. 37) — shows that in high dimensions volume lives in a thin shell — difficulty: medium
- Ex. 2.29 (p. 38) — entropy of a geometric distribution by both brute force and decomposition — difficulty: medium
- Ex. 2.35 (p. 38) — waiting time (length-biased sampling) paradox — difficulty: medium
- Ex. 2.38 (p. 39) — computing the error probability of $R_3$ by two routes, one of which uses the sum rule and posteriors — difficulty: medium

## Reading notes
- Printed page numbers are the PDF page numbers minus 12 (the first page of the unit is printed page 22). Page labels also carry the printed numbers, which are used throughout.
- The text layer prints convex/concave symbols as "^" and "_"; the images show convex as ⌣ (smile) and concave as ⌢ (frown) (p. 35).
- Figures 2.2, 2.3, 2.5 and 2.11 are images (areas of squares, curves); I describe them but do not reproduce them.
- Exercise difficulty ratings are printed as numbers in square brackets (e.g. [2]); the scale is not defined in these pages. My easy/medium labels are my own reading. The marker "3C" on Ex. 2.39 is also unexplained here.
- A triangle (▷) marks some exercises; these pages do not explain it, and I did not rely on it. Exercises 2.8, 2.27, 2.30–2.33, 2.36 and 2.37 have no printed solution in these pages. The solution to 2.39 gives only the final number (9.7 bits per word).
- The author warns that his proof of Jensen's inequality does not handle cases where some $p_i=0$ (p. 41).
- No unreadable symbols were found. The first line of the (2.96) derivation ends in $\log(1/\sum_xQ(x))=0$, which uses $\sum_x Q(x)=1$ left implicit by the author.
- The unit begins and ends on printed pp. 22 and 46; section 2.10 (solutions) is part of this unit.

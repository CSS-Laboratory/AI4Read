---
id: mackay-2003-information/ch02-probability
work: mackay-2003-information
unit: "2 Probability, Entropy, and Inference"
pages: "22–46 (printed numbers are visible in the page images; this digest cites PDF pages, pdf 34–58)"
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
spec_version: 1.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Probability, Entropy, and Inference

## L0 — One line
Probability is the tool for inference (Bayes' theorem turns "data given hypothesis" into "hypothesis given data"), and entropy, relative entropy and Jensen's inequality are the basic quantities and tool for measuring and bounding uncertainty.

## L1 — The gist (≤ 120 words)
The chapter first sets up the vocabulary of probability: ensembles, joint, marginal and conditional probability, the product and sum rules, Bayes' theorem, and independence. It argues that probability can quantify degrees of belief (the Cox axioms). Forward problems compute data from a model; inverse problems use Bayes' theorem to infer hidden variables from data. Worked examples include a medical test, eleven urns and a bent coin. The second half defines Shannon information content and entropy and states their basic properties: non-negativity, the maximum at the uniform distribution, additivity, and decomposability. It then introduces relative entropy with Gibbs' inequality, and proves these inequalities with Jensen's inequality in the exercise solutions. Many exercises follow, with solutions. (pdf 34–58)

## L2 — Key ideas
- An ensemble is a random variable together with its alphabet and probabilities. Joint, marginal and conditional probabilities are linked by the product rule, the sum rule and Bayes' theorem. Everything later in the book is built from these. (pdf 34–36)
- A 95%-reliable test with 1% prevalence gives only a 16% posterior probability of disease. Inference needs Bayes' theorem and the prior, not just the test's reliability. (pdf 37)
- Probability can describe degrees of belief as well as frequencies. The Cox axioms justify this. In the Bayesian view, subjectivity is unavoidable: "you cannot do inference without making assumptions" (pdf 38).
- Forward problems go from a model to the data distribution. Inverse problems go from the data to the unobserved variables, using prior × likelihood / evidence. Predictions should marginalize over hypotheses rather than use only the best one (0.333 vs 0.3 in the urn example). (pdf 39–41)
- The likelihood principle says inference depends on the data only through the likelihood function of the observed outcome. "Likelihood" is a function of parameters, not a probability distribution. (pdf 41, 43, 44)
- Information content is $h(x)=\log_2 1/P(x)$ and entropy is its average. $H\ge 0$, $H\le\log|\mathcal A_X|$ with equality for the uniform distribution, and $H(X,Y)=H(X)+H(Y)$ iff $X,Y$ are independent. (pdf 44–45)
- Entropy is decomposable: it can be computed by revealing the outcome in stages (2.43–2.44). This often makes entropy calculations short. (pdf 45–46)
- Relative entropy $D_{\rm KL}(P\|Q)\ge 0$ (Gibbs' inequality) with equality iff $P=Q$. It is not symmetric. It follows from Jensen's inequality for convex functions. (pdf 46–47, 56)
- In high dimensions, almost all the volume of a sphere lies in a thin shell near the surface (Ex. 2.20). This foreshadows typicality. (pdf 49, 54)

## L3 — Walkthrough

### Preface remarks (pdf 34)
The chapter and Chapter 8 spend time on notation. The author distinguishes a random variable, its value, and the proposition that the variable takes that value. He then adopts the simplest notation possible, for example saying "true" for "true with probability 1". (pdf 34)

### 2.1 Probabilities and ensembles (pdf 34–36)
**Ensemble.** An ensemble $X$ is a triple $(x,\mathcal A_X,\mathcal P_X)$. The outcome $x$ takes a value in $\mathcal A_X=\{a_1,\dots,a_I\}$ with probabilities $\mathcal P_X=\{p_1,\dots,p_I\}$, where $P(x=a_i)=p_i$, $p_i\ge 0$ and $\sum_{a_i\in\mathcal A_X}P(x=a_i)=1$. ($\mathcal A$ stands for "alphabet".) (pdf 34)

The running example is a random letter from an English document: 27 outcomes (a–z plus a space "-"). Figure 2.1 gives the probabilities. For instance $a$ = 0.0575, $e$ = 0.0913, $z$ = 0.0007, space = 0.1928. (pdf 34)

**Probability of a subset.** For $T\subseteq\mathcal A_X$:
$$P(T)=P(x\in T)=\sum_{a_i\in T}P(x=a_i). \tag{2.1}$$
With $V=\{a,e,i,o,u\}$:
$$P(V)=0.06+0.09+0.06+0.07+0.03=0.31. \tag{2.2}$$
(pdf 34)

**Joint ensemble.** A joint ensemble $XY$ has outcomes that are ordered pairs $(x,y)$ with $x\in\mathcal A_X$, $y\in\mathcal A_Y$. $P(x,y)$ is the joint probability. The two variables are not necessarily independent. (pdf 34)

**Marginal probability.**
$$P(x=a_i)\equiv\sum_{y\in\mathcal A_Y}P(x=a_i,y), \tag{2.3}$$
$$P(y)\equiv\sum_{x\in\mathcal A_X}P(x,y). \tag{2.4}$$
(pdf 35)

**Conditional probability.**
$$P(x=a_i\mid y=b_j)\equiv\frac{P(x=a_i,y=b_j)}{P(y=b_j)}\quad\text{if }P(y=b_j)\ne 0. \tag{2.5}$$
If $P(y=b_j)=0$ the conditional probability is undefined. (pdf 35)

**Example 2.1.** The pair $XY$ is two successive letters of an English document (bigrams, figure 2.2). Its two marginals $P(x)$ and $P(y)$ are identical and equal to the monogram distribution of figure 2.1. Normalizing rows gives $P(y\mid x)$ and normalizing columns gives $P(x\mid y)$ (figure 2.3). Given $x=\mathrm q$, the most probable second letters are u and space (space because the source text uses the word FAQ a lot). Given $y=\mathrm u$, the most probable first letters are n and o. (pdf 35–36)

**Rules of probability.** $\mathcal H$ denotes the assumptions behind the probabilities.

- Product rule (also called the chain rule here):
$$P(x,y\mid\mathcal H)=P(x\mid y,\mathcal H)P(y\mid\mathcal H)=P(y\mid x,\mathcal H)P(x\mid\mathcal H). \tag{2.6}$$
- Sum rule:
$$P(x\mid\mathcal H)=\sum_y P(x,y\mid\mathcal H) \tag{2.7}$$
$$\qquad\;=\sum_y P(x\mid y,\mathcal H)P(y\mid\mathcal H). \tag{2.8}$$
- Bayes' theorem:
$$P(y\mid x,\mathcal H)=\frac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{P(x\mid\mathcal H)} \tag{2.9}$$
$$\qquad\qquad=\frac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{\sum_{y'}P(x\mid y',\mathcal H)P(y'\mid\mathcal H)}. \tag{2.10}$$
- Independence: $X\perp Y$ iff
$$P(x,y)=P(x)P(y). \tag{2.11}$$
(pdf 36)

Exercise 2.2 asks whether $X,Y$ in figure 2.2 are independent. The solution says no: independence would make all rows $P(y\mid x)$ identical. (pdf 36, 52)

**Example 2.3 (Jo's test).** Let $a=1$ mean Jo has the disease and $a=0$ mean she does not. Let $b=1$ mean a positive test and $b=0$ a negative one. The test is 95% reliable:
$$P(b{=}1\mid a{=}1)=0.95,\; P(b{=}1\mid a{=}0)=0.05,\; P(b{=}0\mid a{=}1)=0.05,\; P(b{=}0\mid a{=}0)=0.95. \tag{2.13}$$
The prevalence is
$$P(a{=}1)=0.01,\quad P(a{=}0)=0.99. \tag{2.14}$$
From the marginal and the conditional we get the joint $P(a,b)=P(a)P(b\mid a)$. By the sum rule,
$$P(b{=}1)=P(b{=}1\mid a{=}1)P(a{=}1)+P(b{=}1\mid a{=}0)P(a{=}0). \tag{2.15}$$
Bayes' theorem gives
$$P(a{=}1\mid b{=}1)=\frac{P(b{=}1\mid a{=}1)P(a{=}1)}{P(b{=}1\mid a{=}1)P(a{=}1)+P(b{=}1\mid a{=}0)P(a{=}0)} \tag{2.16}$$
$$=\frac{0.95\times 0.01}{0.95\times0.01+0.05\times0.99} \tag{2.17}$$
$$=0.16. \tag{2.18}$$
Despite the positive result, the probability of disease is only 16%. The "95% chance" reading is the man-in-the-street error. (pdf 37)

*Intuition note.* Most people tested are healthy, so a 5% false-positive rate on 99% of people produces more positives than a 95% hit rate on 1% of people. The prior matters.

### 2.2 The meaning of probability (pdf 37–39)
Probabilities can describe (i) frequencies of outcomes in random experiments or (ii) degrees of belief in propositions. A frequency definition is hard to make noncircular: to say a coin's frequency of heads is 1/2 you must define "average", which tends to use a synonym of probability. The author does not try to resolve this. (pdf 37–38)

Degrees of belief apply to non-repeatable propositions, for example whether Mr. S. was the murderer, whether a signature on a cheque is genuine, or whether Bacon wrote Shakespeare's plays. (pdf 38)

**Cox axioms (Box 2.4).** Let $B(x)$ be the degree of belief in $x$, $\bar x$ the negation of $x$, and $B(x\mid y)$ the belief in $x$ assuming $y$.

- Axiom 1: beliefs can be ordered, and the ordering is transitive. As a consequence they can be mapped to real numbers.
- Axiom 2: there is a function $f$ with $B(x)=f[B(\bar x)]$.
- Axiom 3: there is a function $g$ with $B(x,y)=g[B(x\mid y),B(y)]$.

Beliefs satisfying these can be mapped onto probabilities with $P(\text{false})=0$, $P(\text{true})=1$, $0\le P(x)\le1$, $P(x)=1-P(\bar x)$ and $P(x,y)=P(x\mid y)P(y)$. (pdf 38)

Consequences: two people with the same assumptions and data draw identical conclusions. This is the Bayesian (or subjective) view. Bayesians say subjectivity is not a defect, since you cannot do inference without assumptions. The author warns that this view is not universally held. Non-Bayesian statistics, dominant in the 20th century, lets probabilities describe only random variables. The big difference is that Bayesians also use probabilities to describe inferences. (pdf 38–39)

### 2.3 Forward probabilities and inverse probabilities (pdf 39–43)
**Forward probability.** A generative model describes how data arise. The task is to compute the distribution or expectation of some quantity that depends on the data. (pdf 39)

*Exercise 2.4.* An urn has $K$ balls, $B$ black. Fred draws with replacement $N$ times. Find the distribution, mean and variance of $n_B$, for $N=5$ and $N=400$ with $B=2$, $K=10$. (pdf 39)
*Solution (pdf 52).* With $f_B=B/K$:
$$P(n_B\mid f_B,N)=\binom{N}{n_B}f_B^{n_B}(1-f_B)^{N-n_B}, \tag{2.57}$$
$$\mathcal E[n_B]=Nf_B,\quad \mathrm{var}[n_B]=Nf_B(1-f_B). \tag{2.58–2.59}$$
For $N=5$: mean 1, variance 4/5, standard deviation 0.89. For $N=400$: mean 80, variance 64, standard deviation 8. (pdf 52)

*Exercise 2.5.* Define
$$z=\frac{(n_B-f_BN)^2}{Nf_B(1-f_B)}. \tag{2.19}$$
*Solution (pdf 52).* The numerator is $(n_B-\mathcal E[n_B])^2$ and the denominator is $\mathrm{var}[n_B]$, which is the expectation of the numerator. So $\mathcal E[z]=1$. ($z$ is a chi-squared-type quantity.) For $N=5$, $f_B=1/5$: only $n_B=1$ gives $z<1$, so $P(z<1)=P(n_B=1)=0.4096$. (pdf 52)

**Inverse probability.** It also uses a generative model, but computes the conditional probability of unobserved variables given the observed ones. This requires Bayes' theorem. (pdf 39)

**Example 2.6 (eleven urns).** Urn $u\in\{0,\dots,10\}$ has $u$ black and $10-u$ white balls. Fred picks an urn at random and draws $N=10$ times with replacement, getting $n_B=3$ blacks. What is the probability that the urn Fred is using is urn $u$, from Bill's point of view (Bill does not know $u$)? That is, find $P(u\mid n_B{=}3,N{=}10)$. (pdf 39)
$$P(u,n_B\mid N)=P(n_B\mid u,N)P(u), \tag{2.20}$$
$$P(u\mid n_B,N)=\frac{P(u,n_B\mid N)}{P(n_B\mid N)}=\frac{P(n_B\mid u,N)P(u)}{P(n_B\mid N)}. \tag{2.21–2.22}$$
Here $P(u)=1/11$. With $f_u\equiv u/10$,
$$P(n_B\mid u,N)=\binom{N}{n_B}f_u^{n_B}(1-f_u)^{N-n_B}, \tag{2.23}$$
$$P(n_B\mid N)=\sum_uP(u,n_B\mid N)=\sum_uP(u)P(n_B\mid u,N), \tag{2.24}$$
$$P(u\mid n_B,N)=\frac{P(u)P(n_B\mid u,N)}{P(n_B\mid N)} \tag{2.25}$$
$$\qquad\;=\frac{1}{P(n_B\mid N)}\frac1{11}\binom{N}{n_B}f_u^{n_B}(1-f_u)^{N-n_B}. \tag{2.26}$$
The normalizer is $P(n_B{=}3\mid N{=}10)=0.083$. The posterior is (figure 2.6): $u=0$: 0; 1: 0.063; 2: 0.22; 3: 0.29; 4: 0.24; 5: 0.13; 6: 0.047; 7: 0.0099; 8: 0.00086; 9: 0.0000096; 10: 0. The end points have zero posterior because urn 0 has no black balls and urn 10 has no white balls. (pdf 40)

**Terminology.** $P(u)$ is the prior. $P(n_B\mid u,N)$ is the likelihood of $u$. For fixed $u$ it is a probability over $n_B$. For fixed $n_B$ it is the likelihood function of $u$. The author insists: never say "the likelihood of the data", say "the likelihood of the parameters"; the likelihood function is not a probability distribution. $P(u\mid n_B,N)$ is the posterior. The normalizer $P(n_B\mid N)$ is the evidence, or marginal likelihood. For parameters $\boldsymbol\theta$, data $D$, hypothesis space $\mathcal H$:
$$P(\boldsymbol\theta\mid D,\mathcal H)=\frac{P(D\mid\boldsymbol\theta,\mathcal H)P(\boldsymbol\theta\mid\mathcal H)}{P(D\mid\mathcal H)}, \tag{2.27}$$
$$\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}. \tag{2.28}$$
(pdf 40–41)

**Prediction (Example 2.6 continued).** What is the probability that the next ball is black, given $n_B=3$, $N=10$? By the sum rule,
$$P(\text{ball}_{N+1}\text{ black}\mid n_B,N)=\sum_uP(\text{ball}_{N+1}\text{ black}\mid u,n_B,N)P(u\mid n_B,N). \tag{2.29}$$
Because drawing is with replacement, the first factor is $f_u=u/10$:
$$=\sum_uf_uP(u\mid n_B,N), \tag{2.30}$$
$$=0.333. \tag{2.31}$$
The common statistical practice would pick the most plausible urn ($u=3$) and predict 0.3. Marginalizing over $u$ gives a more moderate, less extreme prediction. (pdf 41)

*Intuition note.* Do not pretend the best hypothesis is certain. Average the predictions of all hypotheses, weighted by their posterior probability.

**Inference as inverse probability — Example 2.7 (bent coin).** Bill tosses a coin $N$ times and gets $n_H$ heads, where $f_H$ is unknown. Find the distribution of $f_H$ and the probability that toss $N+1$ is a head (e.g. $N=10$, $n_H=3$; or $N=300$, $n_H=29$). This looks like Example 2.6, but $f_H$ is a fixed unknown parameter, not a random variable in the frequentist sense. We must assume a prior $P(f_H)$. Priors, and also likelihoods (for example, the independence of draws), are subjective assumptions. (pdf 42)

*Probability densities (author's aside).* $P(\cdot)$ now also denotes densities. $P(v\in(a,b))=\int_a^b dv\,P(v)$. $P(v)dv$ is dimensionless, and the density has the inverse dimensions of $v$. Densities greater than 1 are normal. (pdf 42)

*Exercise 2.8.* Assume the uniform prior $P(f_H)=1$. Solve for (a) $N=3,n_H=0$; (b) $N=3,n_H=2$; (c) $N=10,n_H=3$; (d) $N=300,n_H=29$. A hint is given, the beta integral:
$$\int_0^1dp_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!F_b!}{(F_a+F_b+1)!}. \tag{2.32}$$
(pdf 42; no solution given in this unit.)

A prior is not a guess of the parameter's value. It is a density expressing belief that $f_H$ lies in each interval. If the prior is symmetric about 1/2,
$$P(x_1=\text{head})=\int df_H\,P(f_H)P(x_1{=}\text{head}\mid f_H)=\int df_H\,P(f_H)f_H=1/2. \tag{2.33}$$
But later predictions depend on the whole prior, not just its mean. (pdf 43)

**Example 2.9 (data compression).** Compress a binary file with $n_1=29$ ones and $n_0=271$ zeros. A compressor must implicitly answer "what is the probability the next character is a 1?". The author's theme is that compression and modelling are the same problem and both use inverse probability. The example is solved in Chapter 6. (pdf 43)

**The likelihood principle.** Examples 2.10 and 2.11 give two urn problems.
- Example 2.10: urn A has one black and two white balls. Urn B has two black and one white. A black ball is drawn. What is $P(\text{urn A})$?
- Example 2.11: urn A has five balls (one black, two white, one green, one pink). Urn B has 500 balls (200 black, 100 white, and other colours). A black ball is drawn. What is $P(\text{urn A})$?

Only the probability of the outcome that actually happened under each hypothesis matters: 1/3 vs 2/3 in the first case, 1/5 vs 2/5 in the second. The rest of each urn is irrelevant. (pdf 43–44)

> The likelihood principle: given a generative model $P(d\mid\boldsymbol\theta)$ and an observed outcome $d_1$, all inferences and predictions should depend only on the function $P(d_1\mid\boldsymbol\theta)$. (pdf 44)

Many classical statistical methods violate it. (pdf 44)

### 2.4 Definition of entropy and related functions (pdf 44–45)
**Shannon information content:**
$$h(x)=\log_2\frac1{P(x)},\quad\text{measured in bits.} \tag{2.34}$$
("Bit" also means a 0/1 variable; context decides.) In table 2.9, $z$ has $h=10.4$ bits and $e$ has $h=3.5$ bits; space has 2.4 bits. (pdf 44)

**Entropy of an ensemble:**
$$H(X)\equiv\sum_{x\in\mathcal A_X}P(x)\log\frac1{P(x)}, \tag{2.35}$$
with the convention $0\times\log1/0\equiv0$, since $\lim_{\theta\to0^+}\theta\log1/\theta=0$. It is measured in bits. It can also be written $H(\mathbf p)$, and it is also called the uncertainty of $X$. (pdf 44)

**Example 2.12.** The entropy of a random English letter is about 4.11 bits. This is the average of the fourth column of table 2.9 under the $p_i$. (pdf 44)

**Properties.**
- $H(X)\ge0$, with equality iff $p_i=1$ for one $i$.
- Entropy is maximized by the uniform distribution:
$$H(X)\le\log|\mathcal A_X|\quad\text{with equality iff }p_i=1/|\mathcal A_X|\ \forall i. \tag{2.36}$$
(pdf 45)

**Redundancy:**
$$1-\frac{H(X)}{\log|\mathcal A_X|}. \tag{2.37}$$
The author will not use it in the book. (pdf 45)

**Joint entropy and additivity:**
$$H(X,Y)=\sum_{xy\in\mathcal A_X\mathcal A_Y}P(x,y)\log\frac1{P(x,y)}, \tag{2.38}$$
$$H(X,Y)=H(X)+H(Y)\iff P(x,y)=P(x)P(y). \tag{2.39}$$
The definitions apply to discrete finite alphabets. They can be extended to infinite sets, where entropy may be infinite. Continuous densities are treated in section 11.3. (pdf 45)

*Intuition note.* Entropy is the average surprise of an outcome. Rare outcomes carry many bits, but they are rare, so the average is largest when no outcome is favoured.

### 2.5 Decomposability of the entropy (pdf 45–46)
**Example.** $x\in\{0,1,2\}$ is generated by a fair coin deciding whether $x=0$, then, if not, a second fair coin choosing between 1 and 2:
$$P(x{=}0)=\tfrac12,\;P(x{=}1)=\tfrac14,\;P(x{=}2)=\tfrac14. \tag{2.40}$$
Brute force:
$$H(X)=\tfrac12\log2+\tfrac14\log4+\tfrac14\log4=1.5. \tag{2.41}$$
Decomposition: the first reveal has entropy $H(\tfrac12,\tfrac12)=1$ bit. The second reveal happens only half the time and has 1 bit:
$$H(X)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac12,\tfrac12). \tag{2.42}$$
(pdf 45–46)

**General forms.**
$$H(\mathbf p)=H(p_1,1-p_1)+(1-p_1)H\!\left(\frac{p_2}{1-p_1},\frac{p_3}{1-p_1},\dots,\frac{p_I}{1-p_1}\right), \tag{2.43}$$
and for any $m$:
$$H(\mathbf p)=H\big[(p_1+\dots+p_m),(p_{m+1}+\dots+p_I)\big]+(p_1+\dots+p_m)H\!\left(\frac{p_1}{p_1+\dots+p_m},\dots,\frac{p_m}{p_1+\dots+p_m}\right)$$
$$\qquad+(p_{m+1}+\dots+p_I)H\!\left(\frac{p_{m+1}}{p_{m+1}+\dots+p_I},\dots,\frac{p_I}{p_{m+1}+\dots+p_I}\right). \tag{2.44}$$
(pdf 46)

**Example 2.13.** A source emits a character from $\{0,\dots,9,a,\dots,z\}$. With probability 1/3 it is a numeral (10, equiprobable), with 1/3 a vowel (5, equiprobable), and with 1/3 a consonant (21, equiprobable). Solution:
$$\log3+\tfrac13(\log10+\log5+\log21)=\log3+\tfrac13\log1050\simeq\log30\text{ bits}. $$
(pdf 46)

*Intuition note.* Total uncertainty = uncertainty about which group + average uncertainty about the member within the group.

### 2.6 Gibbs' inequality (pdf 46)
**Relative entropy (Kullback–Leibler divergence)** between $P$ and $Q$ over the same alphabet:
$$D_{\rm KL}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}. \tag{2.45}$$
**Gibbs' inequality:**
$$D_{\rm KL}(P\|Q)\ge0\quad\text{with equality only if }P=Q. \tag{2.46}$$
In general $D_{\rm KL}(P\|Q)\ne D_{\rm KL}(Q\|P)$, so it is not strictly a distance. The author calls Gibbs' inequality "probably the most important inequality in this book", and says it can be proved using convexity. (pdf 46)

*Intuition note.* Believing $Q$ when the truth is $P$ always costs you on average. You can never gain by being wrong.

### 2.7 Jensen's inequality for convex functions (pdf 47–48)
**Convex (smile) function.** $f$ is convex over $(a,b)$ if every chord lies above the function. For all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$:
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2). \tag{2.47}$$
It is strictly convex if equality holds only at $\lambda=0,1$. Concave ("frown") is defined similarly. Strictly convex examples: $x^2$, $e^x$, $e^{-x}$ for all $x$, and $\log(1/x)$, $x\log x$ for $x>0$. (pdf 47)

**Jensen's inequality.** If $f$ is convex and $x$ is a random variable,
$$\mathcal E[f(x)]\ge f(\mathcal E[x]). \tag{2.48}$$
If $f$ is strictly convex and equality holds, then $x$ is constant. For concave $f$ the inequality reverses. Physical picture: masses $p_i$ on a convex curve have their centre of gravity $(\mathcal E[x],\mathcal E[f(x)])$ above the curve. (pdf 47)

*Exercise 2.14* asks for a proof. The solution (pdf 53) proves by recursion from the right-hand side that $\sum_ip_if(x_i)\ge f(\sum_ip_ix_i)$ given (2.60), the convexity inequality. The steps are:
$$f\Big(\sum_{i=1}^Ip_ix_i\Big)=f\Big(p_1x_1+\sum_{i=2}^Ip_ix_i\Big)\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]\Big[f\Big(\sum_{i=2}^Ip_ix_i\Big/\sum_{i=2}^Ip_i\Big)\Big], \tag{2.62}$$
using $\lambda=p_1/\sum_{i=1}^Ip_i=p_1$. The next line applies convexity again with $\lambda=p_2/\sum_{i=2}^Ip_i$, and so on. Cases with some $p_i=0$ are left to the "pedantic reader". (pdf 53)

**Example 2.15.** Three squares have average area $\bar A=100\,\mathrm m^2$ and average side length $\bar l=10$ m. Let $x$ be the side length, with probability 1/3 each. Then $\mathcal E[x]=10$ and $\mathcal E[f(x)]=100$ with $f(x)=x^2$, which is strictly convex. So $\mathcal E[f(x)]=f(\mathcal E[x])$ and the three lengths are equal. The largest square has area $100\,\mathrm m^2$. (pdf 47)

**Convexity and maximization.** If $f(\mathbf x)$ is concave and there is a point where
$$\frac{\partial f}{\partial x_k}=0\ \text{ for all }k, \tag{2.49}$$
then $f$ has its maximum there. The converse fails. For example, $f(x)=-|x|$ is maximized at $x=0$ where the derivative is undefined. Also, $\log p$ on $(0,1)$ is maximized at the boundary $p=1$, where the gradient is 1. (pdf 48)

*Intuition note.* For a convex function, averaging first and then applying $f$ gives a smaller value than applying $f$ first and then averaging. Equality needs no spread at all.

### 2.8 Exercises (pdf 48–50)
Statements only (answers are given for some in 2.10).
- *Sums of random variables* (Ex. 2.16): the distribution of the sum of two dice and of 100 dice (central-limit theorem); labelling two dice so the sum is uniform on 1–12; whether 100 dice can give a uniform sum. (pdf 48)
- *Inference problems.* Ex. 2.17: if $q=1-p$ and $a=\ln p/q$, then
$$p=\frac1{1+\exp(-a)}, \tag{2.50}$$
and its relation to $\tanh$; the base-2 version. Ex. 2.18: the log posterior ratio
$$\log\frac{P(x{=}1\mid y)}{P(x{=}0\mid y)}=\log\frac{P(y\mid x{=}1)}{P(y\mid x{=}0)}+\log\frac{P(x{=}1)}{P(x{=}0)}. \tag{2.51}$$
Ex. 2.19: with $d_1,d_2$ conditionally independent given $x$,
$$\frac{P(x{=}1\mid\{d_i\})}{P(x{=}0\mid\{d_i\})}=\frac{P(d_1\mid x{=}1)}{P(d_1\mid x{=}0)}\frac{P(d_2\mid x{=}1)}{P(d_2\mid x{=}0)}\frac{P(x{=}1)}{P(x{=}0)}. \tag{2.52}$$
(pdf 48)
- *Life in high-dimensional spaces* (Ex. 2.20): the fraction of an $N$-dimensional sphere's volume in the shell between $r-\epsilon$ and $r$ is
$$f=1-\Big(1-\frac\epsilon r\Big)^N. \tag{2.53}$$
Implication: uniformly distributed points in a high-dimensional sphere lie very likely in a thin shell near the surface. (pdf 49)
- *Expectations and entropies.* The expectation is
$$\mathcal E[f(x)]=\langle f(x)\rangle=\sum_xP(x)f(x). \tag{2.54}$$
Ex. 2.21–2.24 are numerical (with $p_a=0.1,p_b=0.2,p_c=0.7$) and ask what happens when $f$ depends on $P(x)$. Ex. 2.25 asks to prove $H\le\log|\mathcal A_X|$. Ex. 2.26 asks to prove Gibbs' inequality. Ex. 2.27 asks to prove decomposability. (pdf 49)
- Ex. 2.28: the four-outcome tree with biases $f,g,h$; find $H(X)$ and its derivative with respect to $f$. Ex. 2.29: the entropy of the number of flips until the first head. (pdf 50)

### 2.9 Further exercises (pdf 50–52)
Statements for forward probability (Ex. 2.30–2.35), conditional probability (2.36–2.37), and further problems (2.38–2.39).
- Ex. 2.30: the first and second balls drawn without replacement are equally likely to be white.
- Ex. 2.31 (coin on grid, answer $(1-a/b)^2$).
- Ex. 2.32 (Buffon's needle, answer $2a/\pi b$ if $a<b$; the noodle generalization $2A/\pi b$).
- Ex. 2.33 (triangle from two random cuts).
- Ex. 2.34: an unbiased coin is flipped until the first head; estimate $\hat f=h/(h+t)$.
- Ex. 2.35 (waiting-time paradox): the mean number of rolls between sixes is 6, but the interval straddling a random time is longer. The bus-stop version: Poissonville gives a 6-minute average wait but 12 minutes between the missed bus and the next one. Clockville gives 3 and 6 minutes.
- Ex. 2.36: Fred and his two brothers. Ex. 2.37: islanders who tell the truth one third of the time.
- Ex. 2.38: the error probability of the repetition code R3 on a binary symmetric channel, computed two ways: by the binomial method and by the sum rule, $P(\text{error})=\sum_{\mathbf r}P(\mathbf r)P(\text{error}\mid\mathbf r)$. (2.55)
- Ex. 2.39: Zipf's law
$$p_n\simeq\begin{cases}0.1/n&n=1,\dots,12\,367\\0&n>12\,367\end{cases} \tag{2.56}$$
and the entropy of English per word if words are drawn independently from it.
(pdf 50–52)

### 2.10 Solutions (pdf 52–58)
- **Ex. 2.4, 2.5** (above): binomial distribution, $z$ has expectation 1 and $P(z<1)=0.4096$. (pdf 52)
- **Ex. 2.14**: proof of Jensen's inequality (above, pdf 53).
- **Ex. 2.16.**
  (a) The probabilities of the sums 2,…,12 are $\{1,2,3,4,5,6,5,4,3,2,1\}/36$.
  (b) One die has mean 3.5 and variance 35/12. The sum of 100 has mean 350 and variance $3500/12\simeq292$, roughly Gaussian by the central-limit theorem.
  (c) The unique labelling is one ordinary die and one with faces 6,6,6,0,0,0.
  (d) Yes; label die $r$ with $\{0,1,2,3,4,5\}\times6^r$. The author leaves a question: does this contradict the central-limit theorem? (pdf 53)
- **Ex. 2.17.** From $a=\ln p/q$: $p/q=e^a$, so
$$\frac{p}{1-p}=e^a,\quad p=\frac{e^a}{e^a+1}=\frac1{1+\exp(-a)}. \tag{2.63–2.65}$$
With $\tanh(a)=\frac{e^a-e^{-a}}{e^a+e^{-a}}$ (2.66),
$$f(a)\equiv\frac1{1+\exp(-a)}=\frac12\Big(\frac{1-e^{-a}}{1+e^{-a}}+1\Big)=\frac12\Big(\frac{e^{a/2}-e^{-a/2}}{e^{a/2}+e^{-a/2}}+1\Big)=\frac12(\tanh(a/2)+1). \tag{2.67}$$
For base 2, $b=\log_2p/q$ gives
$$p=\frac1{1+2^{-b}}. \tag{2.68}$$
(pdf 53–54)
- **Ex. 2.18.** From $P(x\mid y)=P(y\mid x)P(x)/P(y)$ (2.69), divide the two cases $x=1$, $x=0$ so that $P(y)$ cancels (2.70), then take logs (2.71). (pdf 54)
- **Ex. 2.19.** Conditional independence means
$$P(x,d_1,d_2)=P(x)P(d_1\mid x)P(d_2\mid x), \tag{2.72}$$
so the posterior ratio splits into one factor per data point times the prior ratio (2.73–2.74). (pdf 54)
- **Ex. 2.20.** The volume is $V(r,N)=\frac{\pi^{N/2}}{(N/2)!}r^N$ (2.75), but only $V\propto r^N$ matters:
$$\frac{r^N-(r-\epsilon)^N}{r^N}=1-\Big(1-\frac\epsilon r\Big)^N. \tag{2.76}$$
Table:

  | $N$ | 2 | 10 | 1000 |
  |---|---|---|---|
  | $\epsilon/r=0.01$ | 0.02 | 0.096 | 0.99996 |
  | $\epsilon/r=0.5$ | 0.75 | 0.999 | $1-2^{-1000}$ |

  However small $\epsilon$ is, for large $N$ almost all the mass is in the shell. (pdf 54)
- **Ex. 2.21–2.24.** $\mathcal E[f(x)]=0.1\times10+0.2\times5+0.7\times10/7=3$ (2.77). Since $f=1/P(x)$ here, $\mathcal E[1/P(x)]=3$ (2.78). In general
$$\mathcal E[1/P(x)]=\sum_xP(x)\frac1{P(x)}=|\mathcal A_X|. \tag{2.79}$$
$\mathcal E[g(x)]=p_b=0.2$ (2.80). $P(P(x)\in[0.15,0.5])=p_b=0.2$ (2.81). $P(|\log(P(x)/0.2)|>0.05)=p_a+p_c=0.8$ (2.82). (pdf 55)
- **Ex. 2.25 (max entropy).** Two proofs. *By differentiation* (not recommended; boundary maxima are a risk), in natural logs:
$$H(X)=\sum_ip_i\ln\frac1{p_i},\quad\frac{\partial H}{\partial p_i}=\ln\frac1{p_i}-1, \tag{2.83–2.84}$$
$$G(\mathbf p)\equiv H(X)+\lambda\Big(\sum_ip_i-1\Big),\quad\frac{\partial G}{\partial p_i}=\ln\frac1{p_i}-1+\lambda. \tag{2.85–2.86}$$
At a maximum, $\ln\frac1{p_i}-1+\lambda=0$ (2.87), so $\ln\frac1{p_i}=1-\lambda$ (2.88): all $p_i$ are equal. The curvature is
$$\frac{\partial^2G}{\partial p_i\partial p_j}=-\frac1{p_i}\delta_{ij}, \tag{2.89}$$
negative definite, so it is a maximum. *By Jensen* (recommended): $f(u)=\log\frac1u=-\log u$ is convex, but taking $u=P(x)$ gives an inequality in the wrong direction (2.90). Instead take
$$u=1/P(x), \tag{2.91}$$
$$H(X)=-\mathcal E[f(1/P(x))]\le-f(\mathcal E[1/P(x)]), \tag{2.92}$$
and by Ex. 2.22 $\mathcal E[1/P(x)]=|\mathcal A_X|$, so
$$H(X)\le-f(|\mathcal A_X|)=\log|\mathcal A_X|. \tag{2.93}$$
Equality holds only if $u=1/P(x)$ is constant, i.e. $P$ is uniform. (pdf 55–56)
- **Ex. 2.26 (Gibbs).** First proof: $f(u)=\log1/u$, $u=Q(x)/P(x)$, expectation under $P$:
$$D_{\rm KL}(P\|Q)=\mathcal E[f(Q(x)/P(x))]\ge f\Big(\sum_xP(x)\frac{Q(x)}{P(x)}\Big)=\log\Big(\frac1{\sum_xQ(x)}\Big)=0, \tag{2.95–2.96}$$
with equality only if $Q/P$ is constant, i.e. $Q=P$. Second proof: expectation under $Q$ with $f(u)=u\log u$, $u=P(x)/Q(x)$:
$$D_{\rm KL}(P\|Q)=\sum_xQ(x)\frac{P(x)}{Q(x)}\log\frac{P(x)}{Q(x)}=\sum_xQ(x)f\Big(\frac{P(x)}{Q(x)}\Big)\ge f\Big(\sum_xQ(x)\frac{P(x)}{Q(x)}\Big)=f(1)=0. \tag{2.97–2.98}$$
(pdf 56)
- **Ex. 2.28.** With $H_2$ the binary entropy,
$$H(X)=H_2(f)+fH_2(g)+(1-f)H_2(h). \tag{2.99}$$
(pdf 57)
- **Ex. 2.29.** The first head on toss $x$ has probability
$$P(x)=(1-f)^{x-1}f. \tag{2.100}$$
After a tail the situation resets, so
$$H(X)=H_2(f)+(1-f)H(X), \tag{2.101}$$
$$H(X)=H_2(f)/f. \tag{2.102}$$
(pdf 57)
- **Ex. 2.34.** The number of tails has
$$P(t)=\Big(\tfrac12\Big)^t\tfrac12,\ t\ge0. \tag{2.103}$$
$\mathcal E[\text{heads}]=1$. $\mathcal E[t]=\sum_{t=0}^\infty t(\tfrac12)^t\tfrac12$ (2.104), which equals 1 via the recurrence
$$\mathcal E[t]=\tfrac12(1+\mathcal E[t])+\tfrac12\cdot0\ \Rightarrow\ \mathcal E[t]=1. \tag{2.105}$$
The estimator is $\hat f=1/(1+t)$, with the distribution of $\hat f$ equal to that of $t$ (figure 2.12). (pdf 57)
- **Ex. 2.35.** (a) The next six occurs on roll $r$ with
$$P(r_1=r)=\Big(\tfrac56\Big)^{r-1}\tfrac16,\ r\ge1, \tag{2.106}$$
an exponential distribution
$$P(r_1=r)=e^{-\alpha r}/Z,\ \alpha=\ln(6/5). \tag{2.107}$$
The mean is 6. (b) Mean rolls from the clock to the next six: 6. (c) Mean rolls going back to the most recent six: 6. (d) The interval straddling the clock has mean $6+6-1=11$. (e) The author does not explain the difference between (a) and (d) directly; instead he gives a hint (pdf 58). In Poissonville, buses arrive at random with a mean gap of six minutes, and passengers arrive at a uniform rate, so buses after gaps longer than six minutes are overcrowded. The passengers' representative says two thirds of passengers are on overcrowded buses; the operator says only one third of buses are overcrowded. The author asks whether both claims can be true. Figure 2.13 compares $P(r_1=r)$ with
$$P(r_{\rm tot}=r)=r\Big(\tfrac56\Big)^{r-1}\Big(\tfrac16\Big)^2,$$
with $P(r_1>6)\approx1/3$ and $P(r_{\rm tot}>6)\approx2/3$. (pdf 57–58)
- **Ex. 2.38 (R3 code).** The binomial method gives $p_B=3f^2(1-f)+f^3$. The sum-rule method gives marginals
$$P(\mathbf r{=}000)=\tfrac12(1-f)^3+\tfrac12f^3, \tag{2.108}$$
$$P(\mathbf r{=}001)=\tfrac12f(1-f)^2+\tfrac12f^2(1-f)=\tfrac12f(1-f), \tag{2.109}$$
and posteriors
$$P(s{=}1\mid\mathbf r{=}000)=\frac{f^3}{(1-f)^3+f^3}, \tag{2.110}$$
$$P(s{=}1\mid\mathbf r{=}001)=\frac{(1-f)f^2}{f(1-f)^2+f^2(1-f)}=f. \tag{2.111}$$
Case-by-case errors: $P(\text{error}\mid\mathbf r{=}000)=\frac{f^3}{(1-f)^3+f^3}$ (2.112), $P(\text{error}\mid\mathbf r{=}001)=f$ (2.113). Averaging (2 cases like 000/111, 6 like 001):
$$P(\text{error})=2\big[\tfrac12(1-f)^3+\tfrac12f^3\big]\frac{f^3}{(1-f)^3+f^3}+6\big[\tfrac12f(1-f)\big]f=f^3+3f^2(1-f).$$
So the two methods agree. Some inferred bits are better determined than others: given $\mathbf r$, a particular bit is wrong with probability about $f^3$ or about $f$. (pdf 58)
- **Ex. 2.39.** The entropy is 9.7 bits per word. (pdf 58)

## Toy example (ours, not from the text)
*Part A — decomposition.* Let $P=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$.
- Brute force: $H=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=0.5+0.5+0.375+0.375=1.75$ bits.
- Decomposition (2.43): $H(p_1,1-p_1)=H(\tfrac12,\tfrac12)=1$ bit. The remaining distribution is $(\frac{1/4}{1/2},\frac{1/8}{1/2},\frac{1/8}{1/2})=(\tfrac12,\tfrac14,\tfrac14)$ with entropy $0.5\cdot1+0.25\cdot2+0.25\cdot2=1.5$. So $H=1+\tfrac12\times1.5=1.75$. ✓.

*Part B — asymmetry of KL.* Let $P=(\tfrac12,\tfrac12)$ and $Q=(\tfrac14,\tfrac34)$, with $\log_2 3\approx1.585$.
- $D_{\rm KL}(P\|Q)=\tfrac12\log_2\tfrac{1/2}{1/4}+\tfrac12\log_2\tfrac{1/2}{3/4}=\tfrac12(1)+\tfrac12(1-1.585)=0.5-0.2925=0.2075$ bits.
- $D_{\rm KL}(Q\|P)=\tfrac14\log_2\tfrac{1/4}{1/2}+\tfrac34\log_2\tfrac{3/4}{1/2}=\tfrac14(-1)+\tfrac34(0.585)=-0.25+0.4388=0.1888$ bits.

Both are positive, as Gibbs' inequality says, and they are not equal.

## Concepts
- [[ensemble]] — a random variable with its alphabet and probabilities; a joint ensemble is a pair (new) (pdf 34)
- [[bayes-theorem]] — turns $P(x\mid y)$ and the prior into $P(y\mid x)$; the engine of inverse probability (new) (pdf 36)
- [[bayesian-inference]] — posterior = likelihood × prior / evidence; probabilities describe beliefs under stated assumptions (new) (pdf 38, 41)
- [[likelihood-principle]] — inference depends on the data only through the likelihood of the observed outcome (new) (pdf 44)
- [[joint-and-conditional-entropy]] — the joint entropy $H(X,Y)$ is defined, and is additive iff $X,Y$ are independent; conditional entropy is not yet defined here (pdf 45)
- [[chain-rule]] — the "product rule" (2.6), also called the chain rule here (pdf 36); the decomposition (2.43) is the entropy analogue
- [[self-information]] — $h(x)=\log_2 1/P(x)$, measured in bits (pdf 44)
- [[bit]] — the unit of Shannon information content (pdf 44)
- [[entropy]] — $H(X)=\sum P(x)\log 1/P(x)$, the average information content; $0\le H\le\log|\mathcal A_X|$ (pdf 44–45)
- [[redundancy]] — $1-H(X)/\log|\mathcal A_X|$ (pdf 45)
- [[entropy-decomposability]] — computing entropy by staged revelation, (2.43–2.44) (new) (pdf 46)
- [[relative-entropy-kl-divergence]] — $D_{\rm KL}(P\|Q)\ge0$, non-symmetric (pdf 46)
- [[jensen-inequality]] — $\mathcal E[f(x)]\ge f(\mathcal E[x])$ for convex $f$ (new) (pdf 47)
- [[maximum-entropy-principle]] — only the fact that the uniform distribution maximizes entropy appears (2.36, Ex. 2.25); the principle itself is not discussed here (pdf 45, 55–56)
- [[volume-concentration-in-high-dimensions]] — most of a high-dimensional sphere's volume lies near its surface (new) (pdf 49, 54)

## Canonical instances
- [[english-letter-distribution]] — 27-outcome distribution and its entropy of about 4.11 bits (pdf 34, 44)
- [[english-bigrams]] — the joint ensemble of adjacent letters, with equal marginals but not independent (pdf 35–36, 52)
- [[jo-disease-test]] — 95%-reliable test, 1% prevalence, 16% posterior (pdf 37)
- [[eleven-urns]] — inverse probability and prediction by marginalization (0.333) (pdf 39–41)
- [[bent-coin-inference]] — unknown bias, subjective prior, link to compression (pdf 42–43)
- [[zipf-law-entropy]] — Zipf's law and the entropy of English per word, 9.7 bits (pdf 52, 58)
- [[repetition-code-r3-error]] — error probability $f^3+3f^2(1-f)$ derived two ways (pdf 51, 58)
- [[waiting-time-paradox]] — Poissonville vs Clockville buses; the mean of the straddling interval is 11 rolls (pdf 50–51, 57–58)

## Bridges (candidates)
- [same-math] Likelihood × prior / evidence (2.28) ↔ machine learning: Bayesian posterior over model parameters — the same formula, with parameters in place of the urn index.
- [same-math] $D_{\rm KL}(P\|Q)$ (2.45) ↔ statistics: the expected log-likelihood ratio between two models, with Gibbs' inequality as its non-negativity.
- [structural-analogy] Decomposability of entropy (2.43) ↔ coding: building a code by successive binary splits, where branch entropies are weighted by branch probability (here decomposition is only used to compute $H$).
- [structural-analogy] Log posterior odds = log likelihood ratio + log prior odds (2.51) ↔ evidence accumulation in cognitive science and sequential testing: evidence adds up in log space, one term per datum (2.52).
- [structural-analogy] Marginalizing over $u$ instead of using the best $u$ (2.30) ↔ ensemble methods and model averaging in forecasting.
- [structural-analogy] Waiting-time paradox ↔ sampling bias in surveys: random sampling over-represents large units, as passengers over-represent crowded buses.
- [metaphor] High-dimensional shell concentration ↔ typicality in later chapters (a long sequence is almost never near the "centre" of the distribution).

## Questions this raises
- If the prior is subjective, how sensitive are posteriors to the choice of prior? How does the answer to Ex. 2.8 change with a non-uniform prior?
- The text says compression and modelling are "one and the same". How exactly does the cost in bits of encoding a file relate to $\log 1/P$ of the model's predictions (Example 2.9, solved in Ch. 6)?
- What is the operational meaning of $D_{\rm KL}$ as extra bits, rather than just a non-negative number?
- Does the 9.7 bits per word under Zipf's law mean anything for actual English, given that words are not independent?

## Exercises worth doing
- Ex. 2.8 (pdf 42) — bent-coin posterior with a uniform prior; uses the beta integral and gives the predictive probability; links to Ch. 6 — difficulty: medium
- Ex. 2.14 (pdf 47) — prove Jensen's inequality; the tool behind Gibbs and max entropy — difficulty: medium
- Ex. 2.20 (pdf 49) — shell volume in high dimensions; builds intuition for typicality — difficulty: medium
- Ex. 2.26 (pdf 49) — prove Gibbs' inequality; the most important inequality in the book — difficulty: hard
- Ex. 2.35 (pdf 50) — waiting-time paradox; shows how conditioning changes means — difficulty: medium
- Ex. 2.38 (pdf 51) — R3 error probability by the binomial and sum-rule methods; connects Bayes to coding — difficulty: medium

## Reading notes
- The page tags show no printed page number; the images show printed pages 22–46 (so printed = PDF − 12). This digest cites PDF pages, as instructed.
- There is no page image for pdf 43, so I used the text layer there. It reads cleanly. The figures 2.7 and 2.8 (urns) are omitted from the text.
- The text layer of equations is garbled in places (the pdf 44 table, pdf 53 equation 2.62, pdf 55 equations). I checked each against the page images where they were available.
- (2.2): the vowel terms are rounded to two decimals (0.06+0.09+0.06+0.07+0.03 = 0.31); the exact figure-2.1 values sum to about 0.311.
- Exercise 2.34's solution defines $\hat f=1/(1+t)$ because the coin is stopped at the first head, so $h=1$.
- Exercises 2.8, 2.27, 2.30–2.33, 2.36, 2.37 have no solution in this unit. Ex. 2.39's solution is only the number 9.7 bits.
- The author remarks that Shannon's own 1950 calculation of Ex. 2.39 contains numerical errors (pdf 52).

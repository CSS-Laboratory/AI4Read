---
id: mackay-2003-information/ch02-probability
work: mackay-2003-information
unit: "2 Probability, Entropy, and Inference"
pages: 22-46
fields: [information-theory, bayesian]
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
# Probability, Entropy, and Inference

## L0 — One line
Probability rules (product, sum, Bayes) let us both predict data from a model and infer a model from data, and the same chapter defines entropy and relative entropy, whose key property (Gibbs' inequality) follows from convexity.

## L1 — The gist (≤ 120 words)
This chapter sets up the basic tools: ensembles, joint, marginal and conditional probability, and Bayes' theorem. It separates forward problems (data from a model) from inverse problems (the model from the data). It treats probability both as frequencies and as degrees of belief, shows by urn and coin examples how to infer and predict, then defines information content, entropy and relative entropy. Gibbs' inequality, proved with Jensen's inequality, shows that relative entropy is never negative. Why it matters: later chapters treat compression and inference as the same inverse-probability task.

**Prerequisites:** sums and logarithms; conditional probability; binomial coefficient; derivative and integral; mean and variance.

## L2 — Key ideas (5–10 bullets)
- An ensemble is a random variable with its alphabet and probabilities. Joint, marginal and conditional probabilities follow from the product and sum rules, and Bayes' theorem comes from the product rule (pp. 22–24).
- Bayes' theorem must be used for inference: a "95% reliable" test with a 1% base rate gives only a 16% chance of disease after a positive result (p. 25).
- Probabilities may describe frequencies or degrees of belief. Beliefs obeying the Cox axioms (simple consistency rules for degrees of belief) can be mapped onto probabilities. This is the Bayesian (subjective) view; its advocates hold that you cannot do inference without making assumptions (pp. 25–26).
- Inverse-probability vocabulary: prior, likelihood, posterior, evidence. Likelihood is a function of the parameters, not a probability distribution over them (pp. 28–29).
- Predictions should marginalize over the unknown hypothesis (sum over it, weighted by its posterior probabilities), not plug in the single best one. The likelihood principle says inferences should depend on the data only through the likelihood of the observed outcome (pp. 29, 32).
- Shannon information content $h(x)=\log_2 1/P(x)$ and entropy $H(X)$ (its average) are measured in bits. $H\le\log|\mathcal A_X|$, with equality iff $P$ is uniform. Entropy decomposes recursively (pp. 32–34).
- Relative entropy $D_{\rm KL}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}$ is defined for two distributions on the same alphabet and is not symmetric. Gibbs' inequality $D_{\rm KL}(P\|Q)\ge0$ and the entropy bound both follow from Jensen's inequality, $E[f(x)]\ge f(E[x])$ for convex $f$ (a function whose chords lie above it) (pp. 34–35, 43–44).
- In high dimensions, a uniformly distributed point lies, with very high probability, in a thin shell near the surface of a sphere (pp. 37, 42).

## L3 — Walkthrough

### Preface remarks (p. 22)
The author says he will sometimes distinguish a random variable, its value, and the proposition that it has that value. He otherwise uses the simplest notation, e.g. "true" for "true with probability 1" (p. 22).

### 2.1 Probabilities and ensembles (pp. 22–25)
**Ensemble.** An ensemble $X$ is a triple $(x,\mathcal A_X,\mathcal P_X)$. The outcome $x$ takes a value in the alphabet $\mathcal A_X=\{a_1,\dots,a_I\}$ with probabilities $\mathcal P_X=\{p_1,\dots,p_I\}$. Here $P(x=a_i)=p_i$, $p_i\ge0$ and $\sum_{a_i\in\mathcal A_X}P(x=a_i)=1$ (p. 22). Example: a random letter from an English document, with 27 outcomes a–z and a space (figure 2.1; space has $p=0.1928$, e has $0.0913$) (p. 22).

**Subset probability.**
$$P(T)=P(x\in T)=\sum_{a_i\in T}P(x=a_i)\tag{2.1}$$
For the vowels, $P(V)=0.06+0.09+0.06+0.07+0.03=0.31$ (2.2). These are rounded values (p. 22).

**Joint ensemble $XY$.** Each outcome is an ordered pair $x,y$ with joint probability $P(x,y)$. The two variables are not necessarily independent (p. 22).

**Marginal and conditional probability** (p. 23):
$$P(x=a_i)\equiv\sum_{y\in\mathcal A_Y}P(x=a_i,y),\qquad P(y)\equiv\sum_{x\in\mathcal A_X}P(x,y)\tag{2.3, 2.4}$$
$$P(x=a_i\mid y=b_j)\equiv\frac{P(x=a_i,y=b_j)}{P(y=b_j)}\quad\text{if }P(y=b_j)\neq0\tag{2.5}$$
If $P(y=b_j)=0$, the conditional probability is undefined (p. 23).

**Example 2.1 (bigrams).** $XY$ is two successive letters (figure 2.2). Its two marginals are identical, both equal to the monogram distribution of figure 2.1. Normalizing rows gives $P(y\mid x)$, and normalizing columns gives $P(x\mid y)$ (figure 2.3). Given first letter q, the likeliest second letters are u and space (the document uses the word FAQ a lot). Given second letter u, the likeliest first letters are n and o (pp. 23–24).

**Rules** (with $\mathcal H$ = the assumptions behind the probabilities) (p. 24):
- Product rule (also called the chain rule): $P(x,y\mid\mathcal H)=P(x\mid y,\mathcal H)P(y\mid\mathcal H)=P(y\mid x,\mathcal H)P(x\mid\mathcal H)$ (2.6).
- Sum rule: $P(x\mid\mathcal H)=\sum_y P(x,y\mid\mathcal H)=\sum_yP(x\mid y,\mathcal H)P(y\mid\mathcal H)$ (2.7, 2.8).
- Bayes' theorem (from the product rule): $P(y\mid x,\mathcal H)=\dfrac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{P(x\mid\mathcal H)}=\dfrac{P(x\mid y,\mathcal H)P(y\mid\mathcal H)}{\sum_{y'}P(x\mid y',\mathcal H)P(y'\mid\mathcal H)}$ (2.9, 2.10).
- Independence: $X$ and $Y$ are independent (written $X\perp Y$) if and only if $P(x,y)=P(x)P(y)$ (2.11) (p. 24).

Solution to Ex. 2.2: the bigram variables are not independent. If they were, all conditionals $P(y\mid x)$ would be the same function of $y$ for every $x$ (p. 40).

**Example 2.3 (Jo's test).** Let $a=1$ mean Jo has the disease and $a=0$ that she does not. Let $b=1$ be a positive test and $b=0$ a negative one (p. 25).
- The test is 95% reliable: $P(b=1\mid a=1)=0.95$, $P(b=1\mid a=0)=0.05$, $P(b=0\mid a=1)=0.05$, $P(b=0\mid a=0)=0.95$ (2.13).
- Prevalence: $P(a=1)=0.01$, $P(a=0)=0.99$ (2.14).
- The joint is $P(a,b)=P(a)P(b\mid a)$. By the sum rule, $P(b=1)=P(b=1\mid a=1)P(a=1)+P(b=1\mid a=0)P(a=0)$ (2.15).

**Man in the street:** "the test is 95% reliable, so Jo's positive result implies that there is a 95% chance that Jo has the disease". The author calls this incorrect. Bayes' theorem gives (p. 25):
$$P(a=1\mid b=1)=\frac{0.95\times0.01}{0.95\times0.01+0.05\times0.99}=0.16\tag{2.16–2.18}$$
Despite the positive result, Jo has the disease with probability only 16%.

*Intuition note.* Most people tested are healthy, so even the small 5% error rate on them produces more positives than the 95% hit rate on the few sick people. The prior (here, the 1% base rate) must be combined with the test's reliability.

### 2.2 The meaning of probability (pp. 25–27)
Probabilities can describe frequencies of outcomes in random experiments. The author notes that defining "frequency" and "random" without circularity is hard, and he does not try to settle it (pp. 25–26). They can also describe degrees of belief in propositions that involve no random variable. His examples are whether Mr. S. murdered Mrs. S., or whether a signature on a cheque is genuine (p. 26). Some books restrict probability to frequencies in repeatable experiments (p. 26).

**Cox axioms (Box 2.4).** Write $B(x)$ for degree of belief in $x$, $\overline x$ for not-$x$, and $B(x\mid y)$ for belief in $x$ assuming $y$ (p. 26).
- Axiom 1: degrees of belief can be ordered, and the order is transitive. Consequence: beliefs map onto real numbers.
- Axiom 2: there is a function $f$ with $B(x)=f[B(\overline x)]$.
- Axiom 3: there is a function $g$ with $B(x,y)=g[B(x\mid y),B(y)]$.

If beliefs satisfy these axioms, they can be mapped onto probabilities with $P(\text{false})=0$, $P(\text{true})=1$, $0\le P(x)\le1$, $P(\overline x)=1-P(x)$ and $P(x,y)=P(x\mid y)P(y)$ (Box 2.4, p. 26).

Under the rules of probability, two people who make the same assumptions and receive the same data draw identical conclusions. This use of probability is the Bayesian, or subjective, viewpoint, because probabilities depend on assumptions. Its advocates do not see this as a defect since, in their view, "you cannot do inference without making assumptions" (p. 26). The author warns that the Bayesian approach is not globally held. Statistics in most of the 20th century was dominated by non-Bayesian methods, which allow probabilities to describe only random variables (p. 26). The big difference is that Bayesians also use probabilities to describe inferences (pp. 26–27).

### 2.3 Forward probabilities and inverse probabilities (pp. 27–32)
**Forward probability.** A generative model describes a process assumed to produce data. The task is to compute the distribution or expectation of some quantity that depends on the data. Ex. 2.4: an urn of $K$ balls ($B$ black); draw $N$ times with replacement; find the distribution, mean, variance and standard deviation of the number of blacks $n_B$. Ex. 2.5: with $f_B\equiv B/K$, compute the expectation of
$$z=\frac{(n_B-f_BN)^2}{Nf_B(1-f_B)}\tag{2.19}$$
(p. 27). The printed solutions are (p. 40):
- $n_B$ is binomial: $P(n_B\mid f_B,N)=\binom N{n_B}f_B^{n_B}(1-f_B)^{N-n_B}$ (2.57).
- $E[n_B]=Nf_B$ and ${\rm var}[n_B]=Nf_B(1-f_B)$ (2.58, 2.59).
- For $f_B=1/5$: with $N=5$, mean 1, variance 4/5, standard deviation 0.89; with $N=400$, mean 80, variance 64, standard deviation 8.
- $z$ has expectation 1, since its numerator is $(n_B-E[n_B])^2$ and its denominator is ${\rm var}[n_B]$. For $N=5$, $f_B=1/5$, $P(z<1)=P(n_B=1)=0.4096$.

**Inverse probability.** This also uses a generative model, but we compute the conditional probability of unobserved variables given the observed ones. This "invariably requires" Bayes' theorem (p. 27).

**Example 2.6 (eleven urns).** Urn $u\in\{0,\dots,10\}$ holds $u$ black and $10-u$ white balls. Fred picks an urn at random and draws $N$ times with replacement. Bill, who does not know $u$, sees $n_B$ blacks. With $N=10$, $n_B=3$: what is the posterior probability $P(u\mid n_B,N)$ of each urn, from Bill's view? (p. 27)
$$P(u,n_B\mid N)=P(n_B\mid u,N)P(u)\tag{2.20}$$
$$P(u\mid n_B,N)=\frac{P(u,n_B\mid N)}{P(n_B\mid N)}=\frac{P(n_B\mid u,N)P(u)}{P(n_B\mid N)}\tag{2.21, 2.22}$$
The prior is $P(u)=1/11$. With $f_u\equiv u/10$:
$$P(n_B\mid u,N)=\binom N{n_B}f_u^{n_B}(1-f_u)^{N-n_B}\tag{2.23}$$
$$P(n_B\mid N)=\sum_uP(u,n_B\mid N)=\sum_uP(u)P(n_B\mid u,N)\tag{2.24}$$
$$P(u\mid n_B,N)=\frac{P(u)P(n_B\mid u,N)}{P(n_B\mid N)}=\frac1{P(n_B\mid N)}\frac1{11}\binom N{n_B}f_u^{n_B}(1-f_u)^{N-n_B}\tag{2.25, 2.26}$$
The normalizing constant is $P(n_B=3\mid N=10)=0.083$ (p. 28). The posterior (figure 2.6) is:

| $u$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $P(u\mid n_B=3,N=10)$ | 0 | 0.063 | 0.22 | 0.29 | 0.24 | 0.13 | 0.047 | 0.0099 | 0.00086 | 0.0000096 | 0 |

Urns 0 and 10 get probability zero, since urn 0 has no blacks and urn 10 has no whites. Urns 1–9 have non-zero posterior probability (p. 28).

**Terminology** (pp. 28–29). In (2.25), $P(u)$ is the *prior* and $P(n_B\mid u,N)$ is the *likelihood* of $u$. Likelihood and probability are not synonyms. For fixed $u$, $P(n_B\mid u,N)$ is a probability over $n_B$. For fixed $n_B$ it defines the likelihood of $u$. The author's rule: "Never say 'the likelihood of the data'. Always say 'the likelihood of the parameters'." The likelihood function is not a probability distribution (p. 29). $P(u\mid n_B,N)$ is the *posterior*. The normalizing constant $P(n_B\mid N)$ is the *evidence* or *marginal likelihood*. It does not matter for comparing hypotheses, but it becomes important in most complex data-modelling problems (p. 29). With parameters $\boldsymbol\theta$, data $D$ and hypothesis space $\mathcal H$:
$$P(\boldsymbol\theta\mid D,\mathcal H)=\frac{P(D\mid\boldsymbol\theta,\mathcal H)P(\boldsymbol\theta\mid\mathcal H)}{P(D\mid\mathcal H)}\tag{2.27}$$
$$\text{posterior}=\frac{\text{likelihood}\times\text{prior}}{\text{evidence}}\tag{2.28}$$

**Prediction (Example 2.6 continued).** What is the probability that the next ball is black, given $n_B=3$, $N=10$? By the sum rule, and since draws are with replacement, so that $P(\text{ball}_{N+1}\text{ black}\mid u,n_B,N)=f_u$ (p. 29):
$$P(\text{ball}_{N+1}\text{ black}\mid n_B,N)=\sum_uP(\text{ball}_{N+1}\text{ black}\mid u,n_B,N)P(u\mid n_B,N)=\sum_uf_uP(u\mid n_B,N)\tag{2.29, 2.30}$$
Using figure 2.6, this is $0.333$ (2.31). **Comment.** Many statisticians predict by picking the most plausible hypothesis (here $u=3$) and then assuming it true. That would give 0.3. The author says the correct prediction marginalizes over $u$, and here gives "slightly more moderate, less extreme predictions" (p. 29).

*Intuition note.* Since Bill does not know the urn, the posterior weights over urns are averaged into the prediction. The weight on urns 4–7 pulls the answer above 0.3.

**Example 2.7 (bent coin).** Bill tosses a coin $N$ times; $n_H$ heads occur. The head probability $f_H$ is unknown. What is the distribution of $f_H$, and the probability that toss $N+1$ is a head? Examples: $N=10,n_H=3$; $N=300,n_H=29$ (p. 30). Under a frequency-only definition of probability, this differs from the urns, because the urn $u$ was a random variable, whereas the bias $f_H$ would not normally be called one: it is just a fixed but unknown parameter. The author asks whether the two examples nonetheless seem essentially similar (p. 30). Solving it needs a prior $P(f_H)$, which is subjective. The likelihood also rests on assumptions, such as independent draws. The author concludes: "priors are subjective and so are likelihoods" (p. 30).

**Densities** (p. 30). $P(\cdot)$ now also denotes probability densities. The probability that $v$ lies in $(a,b)$ is $\int_a^b dv\,P(v)$. $P(v)\,dv$ is dimensionless, so $P(v)$ has dimensions inverse to $v$. Densities greater than 1 are fine if $\int_a^bdv\,P(v)\le1$ for every interval.

Ex. 2.8 (uniform prior $P(f_H)=1$; cases $N=3,n_H=0$; $N=3,n_H=2$; $N=10,n_H=3$; $N=300,n_H=29$) is set with the beta integral (p. 30):
$$\int_0^1dp_a\,p_a^{F_a}(1-p_a)^{F_b}=\frac{\Gamma(F_a+1)\Gamma(F_b+1)}{\Gamma(F_a+F_b+2)}=\frac{F_a!F_b!}{(F_a+F_b+1)!}\tag{2.32}$$
**Prior is not a guess** (p. 31). A prior is a density specifying prior belief that $f_H$ lies in $(f,f+\delta f)$, not a statement like "I guess $f_H=1/2$". If the prior is symmetric about 1/2, then $P(x_1=\text{head})=\int df_H\,P(f_H)f_H=1/2$ (2.33). But predictions for later tosses depend on the whole prior, not just its mean.

**Data compression (Example 2.9, p. 31).** The task is to compress a binary file of 300 characters with $n_1=29$ ones and $n_0=271$ zeros. A compressor must, implicitly or explicitly, answer "what is the probability that the next character is a 1?". The author considers this similar in character to Example 2.7. He states that "data compression and data modelling are one and the same", both to be tackled by inverse probability. The example is solved in Chapter 6 (p. 31).

**The likelihood principle** (pp. 31–32). Example 2.10: urn A has 1 black and 2 white balls, urn B has 2 black and 1 white. A black ball is drawn from a randomly chosen urn. Example 2.11: urn A has 5 balls (1 black, 2 white, 1 green, 1 pink); urn B has 500 balls, 200 of them black (one fifth of A's balls are black and two fifths of B's). A black ball is drawn. The source prints no answers. (added step) With equal prior 1/2 for each urn, in both cases the posterior of A is 1/3: Ex. 2.10 gives $\frac{1/3}{1/3+2/3}=1/3$ and Ex. 2.11 gives $\frac{1/5}{1/5+2/5}=1/3$. The source's point: details of other outcomes are irrelevant, and only the likelihood matters.

> The likelihood principle: given a generative model $P(d\mid\boldsymbol\theta)$ and an observed outcome $d_1$, all inferences and predictions should depend only on the function $P(d_1\mid\boldsymbol\theta)$ (p. 32).

The author adds that many classical statistical methods violate it (p. 32).

### 2.4 Definition of entropy and related functions (pp. 32–33)
**Shannon information content** of outcome $x$:
$$h(x)=\log_2\frac1{P(x)}\tag{2.34}$$
It is measured in bits. The word "bit" also names a variable that is 0 or 1; context decides (p. 32). In table 2.9, $h(\mathrm z)=10.4$ bits and $h(\mathrm e)=3.5$ bits (p. 32). The author says that later chapters will establish it as a natural measure of information content (p. 32).

**Entropy** of an ensemble is the average information content:
$$H(X)\equiv\sum_{x\in\mathcal A_X}P(x)\log\frac1{P(x)}\tag{2.35}$$
with $0\times\log1/0\equiv0$, since $\lim_{\theta\to0^+}\theta\log1/\theta=0$. It is measured in bits and may be written $H(\mathbf p)$. Another name is the *uncertainty* of $X$ (p. 32).

**Example 2.12.** The entropy of a random English letter is about 4.11 bits, found by averaging $\log1/p_i$ under $p_i$. (Table 2.9 prints the sum as 4.1.) (p. 32)

**Properties** (p. 33):
- $H(X)\ge0$, with equality iff $p_i=1$ for one $i$.
- $H(X)\le\log|\mathcal A_X|$, with equality iff $p_i=1/|\mathcal A_X|$ for all $i$ (2.36).

The *redundancy* is $1-\dfrac{H(X)}{\log|\mathcal A_X|}$ (2.37). The book does not use it later. The *joint entropy* is $H(X,Y)=\sum_{xy}P(x,y)\log\frac1{P(x,y)}$ (2.38). Entropy is additive for independent variables: $H(X,Y)=H(X)+H(Y)$ iff $P(x,y)=P(x)P(y)$ (2.39). These definitions are for discrete distributions over finite sets. They extend to infinite sets, though entropy may then be infinite. Continuous densities are treated in section 11.3 (p. 33).

*Intuition note.* Rare outcomes carry many bits and common ones few. Entropy is the average, so it is largest when all outcomes are equally likely, and zero when one outcome is certain.

### 2.5 Decomposability of the entropy (pp. 33–34)
**Example.** Let $x\in\{0,1,2\}$ be made by a fair coin deciding whether $x=0$ and, if not, a second fair coin deciding between 1 and 2. Then $P(0)=\tfrac12$, $P(1)=\tfrac14$, $P(2)=\tfrac14$ (2.40). Brute force: $H(X)=\tfrac12\log2+\tfrac14\log4+\tfrac14\log4=1.5$ (2.41). By decomposition, the first revelation has entropy $H(\tfrac12,\tfrac12)=1$ bit. The second occurs half the time:
$$H(X)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac12,\tfrac12)\tag{2.42}$$
General case:
$$H(\mathbf p)=H(p_1,1-p_1)+(1-p_1)H\!\left(\frac{p_2}{1-p_1},\frac{p_3}{1-p_1},\dots,\frac{p_I}{1-p_1}\right)\tag{2.43}$$
and for any $m$ (p. 34):
$$H(\mathbf p)=H[(p_1+\dots+p_m),(p_{m+1}+\dots+p_I)]+(p_1+\dots+p_m)H\!\left(\frac{p_1}{p_1+\dots+p_m},\dots,\frac{p_m}{p_1+\dots+p_m}\right)+(p_{m+1}+\dots+p_I)H\!\left(\frac{p_{m+1}}{p_{m+1}+\dots+p_I},\dots,\frac{p_I}{p_{m+1}+\dots+p_I}\right)\tag{2.44}$$
**Example 2.13.** A source emits a numeral (prob. 1/3, 10 equiprobable), a vowel (1/3, 5) or a consonant (1/3, 21). Then $H=\log3+\tfrac13(\log10+\log5+\log21)=\log3+\tfrac13\log1050\simeq\log30$ bits (p. 34).

*Intuition note.* Reveal the answer in stages: the entropy is the cost of the first stage plus the cost of each later stage, weighted by how often you reach it.

### 2.6 Gibbs' inequality (p. 34)
The *relative entropy* or Kullback–Leibler divergence between $P(x)$ and $Q(x)$ over the same alphabet is
$$D_{\rm KL}(P\|Q)=\sum_xP(x)\log\frac{P(x)}{Q(x)}\tag{2.45}$$
It satisfies Gibbs' inequality, $D_{\rm KL}(P\|Q)\ge0$ with equality only if $P=Q$ (2.46). In general $D_{\rm KL}(P\|Q)\neq D_{\rm KL}(Q\|P)$, so it is "not strictly a distance". The author calls Gibbs' inequality "probably the most important inequality in this book" and says it can be proved using convexity (p. 34).

### 2.7 Jensen's inequality for convex functions (pp. 35–36)
A function $f$ is *convex* ("convex-smile", ∪-shaped) over $(a,b)$ if every chord lies above the function: for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$,
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)\tag{2.47}$$
It is *strictly* convex if equality holds only for $\lambda=0$ and $\lambda=1$. Concave is the same with the inequality reversed (p. 35). Strictly convex examples: $x^2$, $e^x$, $e^{-x}$ for all $x$; $\log(1/x)$ and $x\log x$ for $x>0$ (p. 35).

**Jensen's inequality.** If $f$ is convex and $x$ is a random variable,
$$E[f(x)]\ge f(E[x])\tag{2.48}$$
If $f$ is strictly convex and $E[f(x)]=f(E[x])$, then $x$ is a constant. For concave $f$ the inequality reverses (p. 35). Physical picture: masses $p_i$ on a convex curve at $(x_i,f(x_i))$ have their centre of gravity at $(E[x],E[f(x)])$, above the curve (p. 35).

**Proof, Ex. 2.14** (given: (2.60) $f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)$; to show (2.61) $\sum_ip_if(x_i)\ge f(\sum_ip_ix_i)$ for $p_i\ge0$, $\sum p_i=1$). Work by recursion from the right-hand side. The proof does not handle cases where some $p_i=0$ (p. 41).
$$f\Big(\sum_{i=1}^Ip_ix_i\Big)=f\Big(p_1x_1+\sum_{i=2}^Ip_ix_i\Big)\le p_1f(x_1)+\Big[\sum_{i=2}^Ip_i\Big]f\Big(\sum_{i=2}^Ip_ix_i\Big/\sum_{i=2}^Ip_i\Big)\tag{2.62, first step}$$
Here $\lambda=p_1/\sum_{i=1}^Ip_i=p_1$. The second step applies convexity again with $\lambda=p_2/\sum_{i=2}^Ip_i$ to the last term, "and so forth" (p. 41).

**Example 2.15.** Three squares have mean area 100 m² and mean side length 10 m. Let $x$ be the side length, uniform over three lengths, with $f(x)=x^2$ strictly convex. Then $E[x]=10$ and $E[f(x)]=100=f(E[x])$, so $x$ is constant. All sides are equal, and the largest square has area 100 m² (p. 35).

*Intuition note.* Averaging after applying a convex function gives at least as much as applying it to the average. For a strictly convex function, if the two agree exactly, there was no spread to begin with.

**Convexity and maximization** (p. 36). If $f(\mathbf x)$ is concave and some point has $\partial f/\partial x_k=0$ for all $k$ (2.49), then $f$ has its maximum there. The converse fails: $f(x)=-|x|$ is maximized at $x=0$, where the derivative is undefined. Also $f(p)=\log p$ on $p\in(0,1)$ is maximized at the boundary $p=1$, where the gradient $df/dp=1$ (p. 36).

### 2.8 Exercises (pp. 36–38) and their solutions (pp. 40–45)
**Sums of random variables (Ex. 2.16, p. 36).** (a) The sum of two dice takes values 2–12 with probabilities $\tfrac1{36},\tfrac2{36},\tfrac3{36},\tfrac4{36},\tfrac5{36},\tfrac6{36},\tfrac5{36},\tfrac4{36},\tfrac3{36},\tfrac2{36},\tfrac1{36}$. (b) One die has mean 3.5 and variance 35/12. Hence 100 dice have mean 350 and variance $3500/12\simeq292$, and by the central-limit theorem the sum is roughly Gaussian (confined to the integers). (c) The unique labelling giving a uniform sum over 1–12 is one ordinary die and one with faces 6,6,6,0,0,0. (d) Yes: label the $r$th die with $\{0,1,2,3,4,5\}\times6^r$ (p. 41). The margin asks whether this contradicts the central-limit theorem (p. 41).

**Inference problems.**
- Ex. 2.17: if $q=1-p$ and $a=\ln p/q$, then $p=1/(1+\exp(-a))$ (2.50, 2.63–2.65). This equals $\tfrac12(\tanh(a/2)+1)$ (2.67). With $b=\log_2p/q$, $p=1/(1+2^{-b})$ (2.68) (pp. 36, 41–42).
- Ex. 2.18: for binary $x$, Bayes' theorem gives $\log\frac{P(x=1\mid y)}{P(x=0\mid y)}=\log\frac{P(y\mid x=1)}{P(y\mid x=0)}+\log\frac{P(x=1)}{P(x=0)}$ (2.51) (pp. 36, 42).
- Ex. 2.19: if $d_1,d_2$ are conditionally independent given binary $x$, then $P(x,d_1,d_2)=P(x)P(d_1\mid x)P(d_2\mid x)$ (2.72). So the posterior ratio is $\frac{P(d_1\mid x=1)}{P(d_1\mid x=0)}\frac{P(d_2\mid x=1)}{P(d_2\mid x=0)}\frac{P(x=1)}{P(x=0)}$ (2.52, 2.73–2.74). It has one factor per data point times the prior ratio (pp. 36, 42).

**High dimensions (Ex. 2.20, p. 37).** The fraction of a sphere's volume in the shell between radii $r-\epsilon$ and $r$ is
$$f=1-\left(1-\frac\epsilon r\right)^N\tag{2.53}$$
This uses only $V(r,N)\propto r^N$ (2.75, 2.76). Printed values (p. 42):

| | $N=2$ | $N=10$ | $N=1000$ |
|---|---|---|---|
| $\epsilon/r=0.01$ | 0.02 | 0.096 | 0.99996 |
| $\epsilon/r=0.5$ | 0.75 | 0.999 | $1-2^{-1000}$ |

Implication: uniformly distributed points in a high-dimensional sphere lie very likely in a thin shell near the surface (p. 37).

**Expectations and entropies (Ex. 2.21–2.24).** With $p_a=0.1,p_b=0.2,p_c=0.7$ (p. 43):
- If $f(a)=10,f(b)=5,f(c)=10/7$ (so $f=1/P$), then $E[f(x)]=E[1/P(x)]=3$ (2.77, 2.78).
- For any ensemble, $E[1/P(x)]=\sum_xP(x)/P(x)=|\mathcal A_X|$ (2.79).
- $E[g(x)]=0.2$ for $g=(0,1,0)$ (2.80).
- $P(P(x)\in[0.15,0.5])=0.2$ (2.81) and $P(|\log P(x)/0.2|>0.05)=p_a+p_c=0.8$ (2.82).

**Ex. 2.25: $H(X)\le\log|\mathcal A_X|$, equality iff $p_i=1/|\mathcal A_X|$** (statement p. 37; solution pp. 43–44).
- *Jensen method (recommended).* Take $f(u)=\log\frac1u=-\log u$ (convex) and $u=1/P(x)$ (2.90, 2.91). The choice $u=P(x)$ would give the inequality in the wrong direction. Then
$$H(X)=-E[f(1/P(x))]\le-f(E[1/P(x)])=-f(|\mathcal A_X|)=\log|\mathcal A_X|\tag{2.92, 2.93}$$
using $E[1/P(x)]=|\mathcal A_X|$. Equality holds only if $u=1/P(x)$ is constant, i.e. $P(x)$ is constant (p. 44).
- *Differentiation method (not recommended; the risk is a maximum on the boundary).* Using natural logs, $H=\sum p_i\ln\frac1{p_i}$ and $\partial H/\partial p_i=\ln\frac1{p_i}-1$ (2.83, 2.84). Add a Lagrange multiplier: $G(\mathbf p)=H+\lambda(\sum_ip_i-1)$, with $\partial G/\partial p_i=\ln\frac1{p_i}-1+\lambda$ (2.85, 2.86). Setting this to zero gives $\ln\frac1{p_i}=1-\lambda$ (2.87, 2.88), so all $p_i$ are equal. The curvature $\partial^2G/\partial p_i\partial p_j=-\delta_{ij}/p_i$ is negative definite, so this is a maximum (2.89) (p. 43).

**Ex. 2.26: Gibbs' inequality** (statement p. 37; solution p. 44).
- *First proof.* Take $f(u)=\log1/u$ and $u=Q(x)/P(x)$, with expectation under $P$:
$$D_{\rm KL}(P\|Q)=E[f(Q(x)/P(x))]\ge f\Big(\sum_xP(x)\frac{Q(x)}{P(x)}\Big)=\log\frac1{\sum_xQ(x)}=0\tag{2.95, 2.96}$$
with equality only if $Q(x)/P(x)$ is constant, i.e. $Q=P$.
- *Second proof (expectation under $Q$).* Take $f(u)=u\log u$ and $u=P(x)/Q(x)$:
$$D_{\rm KL}(P\|Q)=\sum_xQ(x)f\Big(\frac{P(x)}{Q(x)}\Big)\ge f\Big(\sum_xQ(x)\frac{P(x)}{Q(x)}\Big)=f(1)=0\tag{2.97, 2.98}$$

*Intuition note.* Relative entropy is never negative, and it is zero only when $Q=P$. The proof works because $-\log$ and $u\log u$ are convex and the averages inside them add to 1.

Ex. 2.27 (prove decomposability (2.43–2.44)) has no printed solution in these pages (p. 37).

**Ex. 2.28 and 2.29 (p. 38).** For $x\in\{0,1,2,3\}$ chosen by a first coin of bias $f$ and then a coin of bias $g$ or $h$, decomposition gives $H(X)=H_2(f)+fH_2(g)+(1-f)H_2(h)$ (2.99), where $H_2$ is the binary entropy function. For flips until the first head with head-probability $f$, $P(x)=(1-f)^{x-1}f$ (2.100). The recursion $H(X)=H_2(f)+(1-f)H(X)$ (2.101) gives $H(X)=H_2(f)/f$ (2.102) (p. 45).

### 2.9 Further exercises (pp. 38–40)
**Forward probability.** Ex. 2.30 (without replacement, the first and second balls are equally likely white), 2.31 (coin on a grid; answer given in the text: $(1-a/b)^2$), 2.32 (Buffon's needle; answer given: $2a/\pi b$ if $a<b$) and 2.33 (triangle from two random cut points) are stated without printed solutions (p. 38).
- Ex. 2.34: an unbiased coin is flipped until the first head. $P(t)=(\tfrac12)^t\tfrac12$ for $t\ge0$ tails (2.103). $E[\text{heads}]=1$ and $E[t]=\sum t(\tfrac12)^t\tfrac12=1$, since $E[t]=\tfrac12(1+E[t])+\tfrac12\cdot0$ (2.104, 2.105). Fred's estimate $\hat f=1/(1+t)$ has the distribution of figure 2.12 (p. 45). This is a sampling-theory problem; the exercise says not to use Bayes' theorem (p. 38).
- Ex. 2.35 (die rolled once per second; the clock strikes) and the bus-stop version (pp. 38–39, 45–46). Printed results: the mean gap from one six to the next is 6, with $P(r_1=r)=(5/6)^{r-1}(1/6)$ (2.106), an exponential distribution with $\alpha=\ln(6/5)$ (2.107). From the clock to the next six the mean is 6, and going back to the last six also 6. The gap from the six before the clock to the six after has mean $6+6-1=11$. In Poissonville the missed-to-next-bus interval is 12 minutes, against 6 in Clockville. Figure 2.13 gives $P(r_{\rm tot}=r)=r(5/6)^{r-1}(1/6)^2$, with $P(r_1>6)\approx1/3$ and $P(r_{\rm tot}>6)\approx2/3$. The author gives a hint, not a full explanation: passengers pile onto buses that follow gaps longer than 6 minutes. The passengers' representative claims that two-thirds of passengers were on overcrowded buses, while the bus operator says only one third of buses are overcrowded; the author asks whether both can be true, and the caption of figure 2.13 gives $P(r_1>6)\approx1/3$ and $P(r_{\rm tot}>6)\approx2/3$ (p. 46).

**Conditional probability.** Ex. 2.36 (Fred, Alf and Bob: $P(F>B)$ before and after learning $F>A$) and Ex. 2.37 (islanders tell the truth 1/3 of the time; another says "yes" that a statement was true) have no printed solutions (p. 39).

**Ex. 2.38: repetition code R3 on a binary symmetric channel with flip probability $f$** (pp. 39, 46). The exercise compares two methods, which agree:
- *Binomial method.* $p_B=3f^2(1-f)+f^3$ (from the solution to Ex. 1.2).
- *Sum-rule method.* $P(\mathbf r=000)=\tfrac12(1-f)^3+\tfrac12f^3$ (2.108), and $P(\mathbf r=001)=\tfrac12f(1-f)^2+\tfrac12f^2(1-f)=\tfrac12f(1-f)$ (2.109). The posteriors are $P(s=1\mid\mathbf r=000)=\frac{f^3}{(1-f)^3+f^3}$ (2.110) and $P(s=1\mid\mathbf r=001)=f$ (2.111). The error probabilities given $\mathbf r$ are $\frac{f^3}{(1-f)^3+f^3}$ and $f$ (2.112, 2.113). Then
$$P({\rm error})=\sum_{\mathbf r}P(\mathbf r)P({\rm error}\mid\mathbf r)=2[\tfrac12(1-f)^3+\tfrac12f^3]\frac{f^3}{(1-f)^3+f^3}+6[\tfrac12f(1-f)]f=f^3+3f^2(1-f)$$
The first two terms cover $\mathbf r=000$ and $111$. The other six outcomes share one probability and one error probability, $f$ (p. 46).

The author notes that the average error probability of R3 is about $3f^2$, but given $\mathbf r$ a particular bit is wrong with probability about $f^3$ or $f$ (p. 46).

**Ex. 2.39 (Zipf's law).** The word frequencies $p_n\simeq0.1/n$ for $n=1,\dots,12\,367$ (and 0 beyond) give a printed entropy of 9.7 bits per word. The text says Shannon made numerical errors in his version of this calculation (pp. 40, 46).

## Toy example (ours, not from the text)
Two coins in a bag: coin A is fair ($P({\rm head})=0.5$) and coin B is biased ($P({\rm head})=0.8$). Pick one at random (prior $\tfrac12,\tfrac12$) and toss it once. It shows heads.

- *Posterior (Bayes, as in (2.9, 2.10)).* The evidence is $P(H)=0.5\times0.5+0.8\times0.5=0.25+0.40=0.65$. So $P(B\mid H)=0.40/0.65=8/13\approx0.615$ and $P(A\mid H)=0.25/0.65=5/13\approx0.385$.
- *Likelihood is not a probability over the coin.* As a function of the coin, the likelihoods are $0.5$ and $0.8$, which sum to $1.3$, not 1.
- *Prediction by marginalizing (as in (2.29, 2.30)).* With the same coin tossed again, $P(H_2\mid H_1)=0.5\cdot\tfrac5{13}+0.8\cdot\tfrac8{13}=\tfrac{2.5+6.4}{13}=\tfrac{8.9}{13}\approx0.685$.
- *Plug-in prediction.* The most probable coin is B, which would predict 0.8. The marginalized prediction 0.685 is more moderate, as the author says for the urn example.

## Concepts
- [[ensemble]] (new) — triple (outcome, alphabet, probabilities); a random variable with its alphabet and probabilities (p. 22)
- [[bayes-theorem]] — posterior from likelihood and prior, derived from the product rule, equations (2.9), (2.10) (p. 24)
- [[product-rule-chain-rule]] — $P(x,y\mid\mathcal H)=P(x\mid y,\mathcal H)P(y\mid\mathcal H)$; the author also calls it the chain rule (p. 24)
- [[sum-rule-marginalization]] (new) — marginal by summing over the other variable; basis of prediction by marginalizing (pp. 23–24, 29)
- [[prior-distribution]] — probability density or distribution over the unknown, not a "guess" of its value (pp. 28, 31)
- [[likelihood]] — $P(\text{data}\mid\text{parameters})$ as a function of the parameters; not a probability distribution over them (p. 29)
- [[posterior-distribution]] — conditional probability of the unknown given the data (p. 29)
- [[marginal-likelihood-evidence]] — normalizing constant $P(D\mid\mathcal H)$, in (2.27)–(2.28) (p. 29)
- [[likelihood-principle]] (new) — inferences depend on the data only through $P(d_1\mid\boldsymbol\theta)$ (p. 32)
- [[forward-vs-inverse-probability]] (new) — forward: quantities produced by a generative model; inverse: unobserved variables given observed ones (p. 27)
- [[posterior-predictive-distribution]] — prediction by averaging over the posterior of the unknown (p. 29)
- [[subjective-probability]] — probability as degree of belief that depends on assumptions (p. 26)
- [[cox-theorem]] — beliefs satisfying the Cox axioms map onto probabilities (the author states the axioms, not the theorem name) (p. 26)
- [[frequentist-vs-bayesian]] — probabilities only for random variables vs. also for beliefs about unknowns (p. 26)
- [[probability-density]] (new) — dimensional density; may exceed 1 so long as intervals have probability ≤ 1 (p. 30)
- [[self-information-surprisal]] — $h(x)=\log_2 1/P(x)$, "Shannon information content", in bits (p. 32)
- [[bit]] — the unit of $h$ and $H$; also a variable valued 0 or 1 (p. 32)
- [[entropy]] — $H(X)=\sum P(x)\log\frac1{P(x)}$, the average information content, also called uncertainty (p. 32)
- [[redundancy]] — $1-H(X)/\log|\mathcal A_X|$, as defined here; not used later in the book (p. 33)
- [[joint-entropy-additivity]] — $H(X,Y)$ defined; additive iff independent (p. 33)
- [[entropy-decomposability]] (new) — entropy of a distribution = entropy of a coarse grouping + weighted entropies within groups, (2.43)–(2.44) (p. 34)
- [[relative-entropy-kl-divergence]] — $D_{\rm KL}(P\|Q)$; not symmetric, so not strictly a distance (p. 34)
- [[gibbs-inequality]] (new) — $D_{\rm KL}(P\|Q)\ge0$, with equality only if $P=Q$ (p. 34)
- [[jensen-inequality]] (new) — $E[f(x)]\ge f(E[x])$ for convex $f$ (p. 35)
- [[convex-function]] (new) — every chord lies above the function, (2.47) (p. 35)

## Canonical instances
- [[english-letter-ensemble]] — 27-symbol alphabet; monogram and bigram distributions; entropy about 4.11 bits (pp. 22–23, 32)
- [[jo-disease-test]] — 95% reliable test with a 1% base rate gives a 16% posterior (p. 25)
- [[eleven-urns]] — inverse probability, posterior table, prediction 0.333 (pp. 27–29)
- [[bent-coin-inference]] — unknown bias; the prior is subjective; uniform-prior exercise (pp. 30–31)
- [[binary-file-compression]] — compression as inverse probability; 29 ones and 271 zeros (p. 31)
- [[two-urn-likelihood-principle]] — Examples 2.10 and 2.11 (pp. 31–32)
- [[sphere-shell-high-dimension]] — volume concentrates near the surface (pp. 37, 42)
- [[repetition-code-R3]] — error probability by two methods, $f^3+3f^2(1-f)$ (pp. 39, 46)
- [[waiting-time-paradox]] — gaps seen from a random time point are longer: 11 vs 6 rolls; 12 vs 6 minutes (pp. 38–39, 46)
- [[zipf-word-entropy]] — 9.7 bits per word under the $1/n$ law (pp. 40, 46)

## Bridges (candidates)
- [same-math] log posterior-ratio = log likelihood-ratio + log prior-ratio, (2.51) ↔ bayesian: the logistic (sigmoid) form of Ex. 2.17 is the inverse of log-odds — same algebra.
- [same-math] $D_{\rm KL}(P\|Q)\ge0$ (Gibbs) ↔ information-theory: cross-entropy $=H+D_{\rm KL}$ is minimized by the true distribution — same quantity, as the concept list defines it (the unit does not state this).
- [structural-analogy] Marginalizing over $u$ for prediction ↔ bayesian: posterior predictive vs. plug-in estimates — both average over hypotheses.
- [structural-analogy] Volume in a thin shell for large $N$ ↔ information-theory: typical-set concentration — both say mass sits away from the centre or mode (canon link; not stated in this unit).
- [structural-analogy] Entropy decomposition (2.43) ↔ information-theory: chain rule $H(X,Y)=H(X)+H(Y\mid X)$ — information revealed in stages.

## Questions this raises
- If the likelihood principle holds, how should we judge methods whose answers depend on outcomes that did not occur?
- How should a prior be chosen when none is specified, as in the bent-coin problem? How much does the answer then depend on it?
- Why does compressing a file amount to predicting the next symbol (Example 2.9, solved in Chapter 6)?
- How does the shell effect in high dimensions change what we expect samples from a distribution to look like?

## Exercises worth doing
- Ex. 2.8 (p. 30) — solve the bent coin with a uniform prior using the beta integral; compare with Example 2.6's prediction — difficulty: medium
- Ex. 2.20 (p. 37) — volume of a thin shell; shows high-dimensional concentration — difficulty: medium
- Ex. 2.35 (p. 38) — waiting-time paradox with dice and buses — difficulty: medium
- Ex. 2.37 (p. 39) — inverting a statement made by a lying or truthful informant with Bayes — difficulty: medium
- Ex. 2.39 (p. 40) — compute the entropy of a Zipf distribution of words — difficulty: hard (marked 3C)

## Reading notes
- Printed page = pdf − 12 (pdf 34 = printed 22).
- Box 2.4 on p. 26 is called "figure 2.4" in the running text; the page image shows it as a box.
- The vowel sum in (2.2) uses rounded values: $0.06+0.09+0.06+0.07+0.03=0.31$.
- Example 2.12 gives entropy "about 4.11 bits"; table 2.9 prints the sum as 4.1.
- Solutions to Ex. 2.8, 2.27, 2.30–2.33, 2.36, 2.37 and the explanation for 2.35(e) are not printed in these pages. Answers to Examples 2.10–2.11 are not printed; the value 1/3 above is our added step.
- Exercise margin marks (▷, difficulty ratings, solution page references) appear throughout; the 3C on Ex. 2.39 is as printed.
- Text-layer equations were garbled in places; all equations above were checked against the page images.

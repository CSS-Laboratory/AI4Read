---
id: deisenroth-2020-mml/ch06-probability-p1
work: deisenroth-2020-mml
unit: "6 Probability and Distributions (part 1/2): §6.1–§6.4.5 and the start of §6.4.6"
pages: 172–196
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Probability and Distributions (part 1/2)

## L0 — One line
Probability is a mathematical structure (probability space → random variable → distribution) obeying two rules, the sum rule and the product rule; Bayes' theorem follows from the product rule, and summary statistics and independence describe and compare distributions.

## L1 — The gist (≤ 120 words)
How can uncertainty in data, models and predictions be handled mathematically? The chapter builds a probability space (outcomes, events, probability) and turns it into random variables with distributions (probability mass, density and cumulative distribution functions: pmf, pdf, cdf). The sum rule and the product rule are the two basic rules; the product rule gives Bayes' theorem for inferring hidden variables from observations. Summary statistics (mean, median, mode, variance, covariance, correlation) describe distributions. Their empirical versions are computed from data. The unit also covers how these statistics behave under sums and affine maps, and independence. It ends by treating zero-mean random variables as vectors, with covariance as inner product and correlation as cosine.

**Prerequisites:** sets and functions; sums and integrals; matrices, transposes and affine maps $Ax+b$; inner product and orthogonality; positive semidefinite matrices.

## L2 — Key ideas
- Jaynes' criteria for plausible reasoning (real-valued, common-sense, consistent), via the Cox–Jaynes theorem, lead to the rules of probability (p. 174). Probability theory can be seen as a generalisation of Boolean logic (p. 173).
- A random variable is a function $X:\Omega\to\mathcal T$. Its distribution is $P_X = P\circ X^{-1}$, the probability of pre-images (p. 175, p. 177).
- Discrete variables use a pmf; continuous variables use a density $f\ge 0$ integrating to 1, and $P(X=x)=0$. A density may exceed 1 (p. 181, p. 182).
- Two rules suffice: the sum rule (marginalise) and the product rule (factorise) (p. 184). Bayes' theorem follows directly: posterior = likelihood × prior / evidence (p. 185).
- Mean, median and mode are different notions of "average". The expected value is linear. Covariance is $\mathbb E[xy^\top]-\mathbb E[x]\mathbb E[y]^\top$; the covariance matrix is symmetric positive semidefinite (p. 188–190).
- Under an affine map $y=Ax+b$: mean $A\mu+b$, covariance $A\Sigma A^\top$ (p. 194).
- Independence implies zero covariance, but not conversely ($y=x^2$ example). Conditional independence ($p(x,y\mid z)=p(x\mid z)p(y\mid z)$ for all $z$) can equivalently be written $p(x\mid y,z)=p(x\mid z)$ (p. 195).
- For zero-mean variables, $\langle X,Y\rangle=\mathrm{Cov}[x,y]$ is an inner product. Length is the standard deviation; correlation is cos θ; uncorrelated means orthogonal (p. 196).

## L3 — Walkthrough

### Chapter introduction (p. 172–173)
- Probability, loosely speaking, concerns the study of uncertainty. It can be thought of as a fraction of times an event occurs, or as a degree of belief (p. 172).
- Machine learning quantifies uncertainty in data, in the model and in predictions (p. 172).
- A **random variable** is a function mapping outcomes of random experiments to the properties we care about. A **probability distribution** measures the probability of an outcome or set of outcomes (p. 172).
- The treatment is deliberately "slightly hand wavy" so that rigour does not hide intuition. Figure 6.1 maps the chapter's concepts (p. 172–173).

### 6.1 Construction of a Probability Space (p. 172–178)
**6.1.1 Philosophical issues (p. 172–174).**
- Classical Boolean logic does not allow certain forms of plausible reasoning to be expressed. If A is false, B becomes less plausible, though classical logic lets us conclude nothing. If B is true, it seems A becomes more plausible (p. 173).
- Example: a friend is late. H1 (on time) is logically ruled out. H2 (traffic) is tempting but not logically required. H3 (abducted by aliens) is possible but quite unlikely (p. 173).
- So probability theory can be seen as a generalisation of Boolean logic. In ML it is often applied this way to formalise the design of automated reasoning systems (p. 173).
- Jaynes' three criteria that must apply to plausibilities (p. 173–174):
  1. Plausibilities are real numbers.
  2. They are based on common-sense rules.
  3. Reasoning must be consistent, in three senses: (a) non-contradiction (same result by different means gives the same plausibility); (b) honesty (all available data are used); (c) reproducibility (equal states of knowledge give equal plausibility).
- The Cox–Jaynes theorem proves these sufficient to define the universal rules for plausibility $p$, up to an arbitrary monotonic transformation. These rules are the rules of probability (p. 174).
- Remark: the *Bayesian* reading uses probability as the user's degree of uncertainty ("subjective probability"). The *frequentist* reading uses relative frequency of events, in the limit of infinite data (p. 174).
- The phrase "probability distribution" is used for several distinct concepts, so the reader often has to work out the meaning from context. One trick is to check whether the variable is categorical (discrete) or continuous (p. 174).

> **Intuition note.** Common-sense consistency requirements, if taken seriously, force you to use the rules of probability. In this sense probability extends the true/false values of logic to degrees of plausibility.

**6.1.2 Probability and random variables (p. 174–177).** Three ideas are often confused: the probability space, the random variable, and the distribution (law) of a random variable (p. 174).
- Kolmogorov's axioms give three ingredients (p. 175):
  - **Sample space** $\Omega$: the set of all possible outcomes. Two coin tosses give $\{hh,tt,ht,th\}$.
  - **Event space** $\mathcal A$: a collection of subsets of $\Omega$ whose membership we can observe at the end of the experiment. For discrete distributions it is often the power set of $\Omega$.
  - **Probability** $P$: each $A\in\mathcal A$ gets a number $P(A)\in[0,1]$, and $P(\Omega)=1$.
- ML often avoids the space $(\Omega,\mathcal A,P)$ and uses the **target space** $\mathcal T$ (elements are *states*). A **random variable** is a function $X:\Omega\to\mathcal T$ (p. 175).
- Example: count heads in two tosses: $X(hh)=2$, $X(ht)=X(th)=1$, $X(tt)=0$, so $\mathcal T=\{0,1,2\}$. For finite $\Omega$ and $\mathcal T$, $X$ is essentially a lookup table. For $S\subseteq\mathcal T$ we assign $P_X(S)\in[0,1]$ (p. 175).
- Margin note: "random variable" is neither random nor a variable; it is a function (p. 175).
- Remark: $\Omega$ has other names in other books ("state space", "sample description space", "possibility space", "event space") (p. 175–176).

**Example 6.1 (p. 176).** Draw two coins with replacement from a bag of US ($) and UK (£) coins; a draw gives $ with probability 0.3.
- $\Omega=\{(\$,\$),(\$,£),(£,\$),(£,£)\}$. $X$ counts the $ draws: $X((\$,\$))=2$, $X((\$,£))=X((£,\$))=1$, $X((£,£))=0$ (6.1–6.4).
- Draws are independent because of replacement (Section 6.4.5). Two outcomes map to $X=1$. The pmf is
$$P(X=2)=0.3\cdot0.3=0.09\tag{6.5}$$
$$P(X=1)=P((\$,£))+P((£,\$))=0.3\cdot(1-0.3)+(1-0.3)\cdot0.3=0.42\tag{6.6}$$
$$P(X=0)=(1-0.3)\cdot(1-0.3)=0.49\tag{6.7}$$

**Probability of the output vs. of the samples (p. 177).** The pre-image of $S\subseteq\mathcal T$ is $X^{-1}(S)=\{\omega\in\Omega: X(\omega)\in S\}$.
$$P_X(S)=P(X\in S)=P(X^{-1}(S))=P(\{\omega\in\Omega: X(\omega)\in S\})\tag{6.8}$$
- $P_X=P\circ X^{-1}$ is the **law** or **distribution** of $X$ (p. 177).
- Remark: if $\mathcal T$ is finite or countably infinite, $X$ is a *discrete* random variable. For continuous random variables only $\mathcal T=\mathbb R$ or $\mathbb R^D$ is considered (p. 177).

> **Intuition note.** A random variable relabels outcomes with the quantity you care about. Its probabilities come from adding up the probabilities of all outcomes that map to that label.

**6.1.3 Statistics (p. 177–178).**
- Probability starts from a model of a process and derives what happens. Statistics observes what happened and infers the underlying process. ML is close to statistics in its goals (p. 177).
- ML also cares about generalisation error: performance on future instances not seen so far. This analysis is mostly beyond this chapter (p. 177–178).

### 6.2 Discrete and Continuous Probabilities (p. 178–183)
- For a discrete target space we specify $P(X=x)$, the **probability mass function** (pmf). For a continuous one we specify interval probabilities $P(a\le X\le b)$. By convention we use $P(X\le x)$, the **cumulative distribution function** (cdf) (p. 178).
- *Univariate* means one random variable (states non-bold $x$). *Multivariate* means several, usually a vector (bold $\boldsymbol x$) (p. 178).

**6.2.1 Discrete probabilities (p. 178–180).**
- The joint probability of two discrete variables is
$$P(X=x_i,Y=y_j)=\frac{n_{ij}}{N}\tag{6.9}$$
 where $n_{ij}$ is the number of events with states $x_i,y_j$ and $N$ the total (p. 178). It is the probability of the intersection of the two events (p. 178).
- Lazy notation: $p(x,y)$ is the joint, $p(x)$ the marginal, $p(y\mid x)$ the conditional. $X\sim p(x)$ means $X$ is distributed according to $p(x)$ (p. 179).

**Example 6.2 (p. 179–180).** $X$ has 5 states, $Y$ has 3 (Figure 6.2, a $3\times5$ table of counts $n_{ij}$). Column sum $c_i=\sum_{j=1}^3 n_{ij}$, row sum $r_j=\sum_{i=1}^5 n_{ij}$.
$$P(X=x_i)=\frac{c_i}{N}=\frac{\sum_{j=1}^{3}n_{ij}}{N}\tag{6.10}$$
$$P(Y=y_j)=\frac{r_j}{N}=\frac{\sum_{i=1}^{5}n_{ij}}{N}\tag{6.11}$$
$$\sum_{i=1}^5 P(X=x_i)=1\quad\text{and}\quad\sum_{j=1}^3 P(Y=y_j)=1\tag{6.12}$$
The conditional probability is a fraction of a row or column:
$$P(Y=y_j\mid X=x_i)=\frac{n_{ij}}{c_i}\tag{6.13}$$
$$P(X=x_i\mid Y=y_j)=\frac{n_{ij}}{r_j}\tag{6.14}$$
- Discrete distributions model *categorical variables* (finite sets of unordered values), e.g. degree taken or letters in handwriting recognition. They are also used to build models that combine finitely many continuous distributions (p. 180).

> **Intuition note.** A joint distribution is a table of counts divided by $N$. Marginals are row/column totals. Conditionals renormalise one row or column.

**6.2.2 Continuous probabilities (p. 180–182).**
- The book pretends real random variables behave like finite discrete ones. This is imprecise for infinite repetition and for drawing a point from an interval (p. 180).
- Remark: two technicalities in continuous spaces. The set of all subsets is too badly behaved for the event space, so $\mathcal A$ must be restricted (complements, intersections, unions). The "size" of a set is its *measure* (cardinality, length, volume). Sets that behave well and have a topology form a *Borel σ-algebra*. The book uses real-valued random variables with their Borel σ-algebra; $\mathbb R^D$-valued ones are vectors of these (p. 180–181).
- **Definition 6.1 (pdf).** $f:\mathbb R^D\to\mathbb R$ is a probability density function if (1) $\forall \boldsymbol x: f(\boldsymbol x)\ge 0$ and (2) its integral exists and
$$\int_{\mathbb R^D} f(\boldsymbol x)\,\mathrm d\boldsymbol x=1\tag{6.15}$$
 For a pmf the integral is replaced by a sum (p. 181).
- A random variable is associated with $f$ by
$$P(a\le X\le b)=\int_a^b f(x)\,\mathrm dx\tag{6.16}$$
 This association is the law or distribution of $X$ (p. 181).
- Remark: for continuous $X$, $P(X=x)$ is zero. This is like taking $a=b$ in (6.16) (p. 181).
- **Definition 6.2 (cdf).** For $X=[X_1,\dots,X_D]^\top$ with states $\boldsymbol x=[x_1,\dots,x_D]^\top$:
$$F_X(\boldsymbol x)=P(X_1\le x_1,\dots,X_D\le x_D)\tag{6.17}$$
 It can be written through the pdf as
$$F_X(\boldsymbol x)=\int_{-\infty}^{x_1}\!\!\cdots\int_{-\infty}^{x_D} f(z_1,\dots,z_D)\,\mathrm dz_1\cdots\mathrm dz_D\tag{6.18}$$
 Margin note: some cdfs have no corresponding pdf (p. 181).
- Remark: two concepts must be distinguished: the pdf $f(x)$ (a nonnegative function with total mass one), and the *law* (the association of $X$ with $f$) (p. 181).
- Later the notation $f$, $F_X$ is mostly dropped, but care is needed in Section 6.7 (p. 182).

**6.2.3 Contrasting discrete and continuous distributions (p. 182–183).**
- For discrete variables, normalisation implies each state's probability is in $[0,1]$. For continuous variables, normalisation (6.15) does **not** imply that the density is $\le 1$ everywhere (p. 182).
- **Example 6.3 (p. 182–183).** Discrete uniform $Z$ with states $\{-1.1,0.3,1.5\}$, each with $P=\tfrac13$ (Figure 6.3a). The state values are deliberately meaningless; their ordering should be ignored. A continuous uniform $X$ on $0.9\le X\le1.6$ (Figure 6.3b) can have density height above 1, but must satisfy
$$\int_{0.9}^{1.6}p(x)\,\mathrm dx=1\tag{6.19}$$
- Remark: discrete states have no structure in general (red, green, blue). When they take numerical values, we can order them and use expected values (p. 183).
- ML notation hides the difference between $\Omega$, $\mathcal T$ and $X$. For $x\in\mathcal T$, $p(x)$ is the probability that $X$ has outcome $x$. Table 6.1: discrete, "point probability" $P(X=x)$ = pmf, no interval version. Continuous, "point probability" $p(x)$ = pdf, "interval probability" $P(X\le x)$ = cdf (p. 183).
- The cdf is also often called the "distribution". The book uses "probability distribution" for both pmfs and pdfs, "technically incorrect", and relies on context (p. 183).

> **Intuition note.** A density is probability per unit length, not a probability itself. Its integral over an interval gives a probability, so its height can exceed 1.

### 6.3 Sum Rule, Product Rule, and Bayes' Theorem (p. 183–186)
- Probability is treated as an extension of logic. The rules follow from the desiderata of Section 6.1.1 (Jaynes, 2003, ch. 2). Once distributions are defined, there are only two fundamental rules (p. 183–184).
- **Sum rule (marginalisation property)**, with $\mathcal Y$ the target-space states of $Y$:
$$p(\boldsymbol x)=\begin{cases}\sum_{\boldsymbol y\in\mathcal Y}p(\boldsymbol x,\boldsymbol y)&\text{if }\boldsymbol y\text{ is discrete}\\[2pt] \int_{\mathcal Y}p(\boldsymbol x,\boldsymbol y)\,\mathrm d\boldsymbol y&\text{if }\boldsymbol y\text{ is continuous}\end{cases}\tag{6.20}$$
 It relates the joint to a marginal, and can be applied to any subset of variables. For $\boldsymbol x=[x_1,\dots,x_D]^\top$:
$$p(x_i)=\int p(x_1,\dots,x_D)\,\mathrm d\boldsymbol x_{\setminus i}\tag{6.21}$$
 where $\setminus i$ means "all except $i$" (p. 184).
- Remark: many computational challenges of probabilistic modelling come from the sum rule. High-dimensional sums or integrals are generally hard: no known polynomial-time algorithm computes them exactly (p. 184).
- **Product rule:**
$$p(\boldsymbol x,\boldsymbol y)=p(\boldsymbol y\mid\boldsymbol x)\,p(\boldsymbol x)\tag{6.22}$$
 Every joint of two variables factorises into a marginal and a conditional. Since the order is arbitrary, also $p(\boldsymbol x,\boldsymbol y)=p(\boldsymbol x\mid\boldsymbol y)p(\boldsymbol y)$. For continuous variables the rule is stated with pdfs (p. 184–185).
- **Bayes' theorem.** Setting: prior knowledge $p(\boldsymbol x)$ about an unobserved (latent) $\boldsymbol x$, and a relation $p(\boldsymbol y\mid\boldsymbol x)$ to an observable $\boldsymbol y$ (p. 185).
$$p(\boldsymbol x\mid\boldsymbol y)=\frac{p(\boldsymbol y\mid\boldsymbol x)\,p(\boldsymbol x)}{p(\boldsymbol y)}\tag{6.23}$$
 (posterior = likelihood × prior / evidence). Derivation, a direct consequence of the product rule:
$$p(\boldsymbol x,\boldsymbol y)=p(\boldsymbol x\mid\boldsymbol y)p(\boldsymbol y)\tag{6.24}$$
$$p(\boldsymbol x,\boldsymbol y)=p(\boldsymbol y\mid\boldsymbol x)p(\boldsymbol x)\tag{6.25}$$
$$p(\boldsymbol x\mid\boldsymbol y)p(\boldsymbol y)=p(\boldsymbol y\mid\boldsymbol x)p(\boldsymbol x)\iff p(\boldsymbol x\mid\boldsymbol y)=\frac{p(\boldsymbol y\mid\boldsymbol x)p(\boldsymbol x)}{p(\boldsymbol y)}\tag{6.26}$$
- **Prior** $p(\boldsymbol x)$: subjective knowledge before data. Any sensible prior may be chosen, but it must have nonzero pdf/pmf on all plausible $\boldsymbol x$, even rare ones (p. 185).
- **Likelihood** $p(\boldsymbol y\mid\boldsymbol x)$: how $\boldsymbol x$ and $\boldsymbol y$ are related. For discrete distributions it is the probability of the data $\boldsymbol y$ given the latent variable $\boldsymbol x$. It is not a distribution in $\boldsymbol x$, only in $\boldsymbol y$. Say "likelihood of $\boldsymbol x$ (given $\boldsymbol y$)" or "probability of $\boldsymbol y$ given $\boldsymbol x$", never "likelihood of $\boldsymbol y$" (p. 185).
- **Posterior** $p(\boldsymbol x\mid\boldsymbol y)$: what we know about $\boldsymbol x$ after observing $\boldsymbol y$ (p. 185).
- **Marginal likelihood / evidence:**
$$p(\boldsymbol y):=\int p(\boldsymbol y\mid\boldsymbol x)p(\boldsymbol x)\,\mathrm d\boldsymbol x=\mathbb E_X[p(\boldsymbol y\mid\boldsymbol x)]\tag{6.27}$$
 It integrates the numerator of (6.23) over $\boldsymbol x$, so it does not depend on $\boldsymbol x$ and normalises the posterior. It is the expected likelihood under the prior, and matters for model selection (Section 8.6). It is often hard to compute (p. 186).
- Bayes' theorem inverts the relation given by the likelihood ("probabilistic inverse") (p. 186).
- Remark: the full posterior keeps all information from prior and data. Summarising it (e.g. by its maximum) loses information. In model-based reinforcement learning, the text says Deisenroth et al. (2015) show that the full posterior over transition functions gives very data-efficient learning, while using only the maximum leads to consistent failures (p. 186).

> **Intuition note.** Bayes' theorem is the product rule written in two ways and divided by $p(\boldsymbol y)$. It turns the probability of the data given the cause into the probability of the cause given the data.

### 6.4 Summary Statistics and Independence (p. 186–196)
A *statistic* is a deterministic function of a random variable. The section covers mean and variance, then independence and inner products as ways to compare two variables (p. 186).

**6.4.1 Means and covariances (p. 187–191).**
- For the exponential family (Section 6.6), the statistics of the variable capture all possible information (p. 187).
- **Definition 6.3 (expected value).** For $g:\mathbb R\to\mathbb R$ and $X\sim p(x)$:
$$\mathbb E_X[g(x)]=\int_{\mathcal X}g(x)p(x)\,\mathrm dx\ \ (\text{continuous})\tag{6.28}$$
$$\mathbb E_X[g(x)]=\sum_{x\in\mathcal X}g(x)p(x)\ \ (\text{discrete})\tag{6.29}$$
 Discrete variables here have numerical outcomes (p. 187).
- Multivariate: element-wise, in $\mathbb R^D$:
$$\mathbb E_X[g(\boldsymbol x)]=\begin{bmatrix}\mathbb E_{X_1}[g(x_1)]\\ \vdots\\ \mathbb E_{X_D}[g(x_D)]\end{bmatrix}\tag{6.30}$$
- **Definition 6.4 (mean).** The mean is the expected value with $g$ the identity:
$$\mathbb E_X[\boldsymbol x]=\begin{bmatrix}\mathbb E_{X_1}[x_1]\\ \vdots\\ \mathbb E_{X_D}[x_D]\end{bmatrix}\in\mathbb R^D\tag{6.31}$$
$$\mathbb E_{X_d}[x_d]:=\begin{cases}\int_{\mathcal X}x_d\,p(x_d)\,\mathrm dx_d&\text{continuous}\\ \sum_{x_i\in\mathcal X}x_i\,p(x_d=x_i)&\text{discrete}\end{cases}\tag{6.32}$$
- **Median**: the "middle" value. For continuous variables, the value where the cdf is 0.5. For asymmetric or long-tailed distributions it is closer to human intuition of "typical" than the mean, and it is more robust to outliers. Its generalisation to higher dimensions is non-trivial because there is no obvious way to sort (p. 188).
- **Mode**: the most frequent value (discrete), or a peak of the density (continuous). A density may have several modes, possibly very many in high dimensions, so finding all modes can be computationally challenging (p. 188).
- **Example 6.4 (p. 188–189).** The two-dimensional mixture
$$p(\boldsymbol x)=0.4\,\mathcal N\!\left(\boldsymbol x\,\Big|\,\begin{bmatrix}10\\2\end{bmatrix},\begin{bmatrix}1&0\\0&1\end{bmatrix}\right)+0.6\,\mathcal N\!\left(\boldsymbol x\,\Big|\,\begin{bmatrix}0\\0\end{bmatrix},\begin{bmatrix}8.4&2.0\\2.0&1.7\end{bmatrix}\right)\tag{6.33}$$
 is bimodal, but one of its marginals is unimodal. The horizontal bimodal marginal shows mean and median can differ. It is tempting to take the 2-D median as the pair of 1-D medians, but this is made difficult because no ordering of 2-D points can be defined: there is more than one way to define "<" so that $\begin{bmatrix}3\\0\end{bmatrix}<\begin{bmatrix}2\\3\end{bmatrix}$ (p. 189).
- **Linearity (Remark, p. 189).** For $f(\boldsymbol x)=ag(\boldsymbol x)+bh(\boldsymbol x)$, $a,b\in\mathbb R$:
$$\mathbb E_X[f(\boldsymbol x)]=\int f(\boldsymbol x)p(\boldsymbol x)\,\mathrm d\boldsymbol x\tag{6.34a}$$
$$=\int[ag(\boldsymbol x)+bh(\boldsymbol x)]p(\boldsymbol x)\,\mathrm d\boldsymbol x\tag{6.34b}$$
$$=a\int g(\boldsymbol x)p(\boldsymbol x)\,\mathrm d\boldsymbol x+b\int h(\boldsymbol x)p(\boldsymbol x)\,\mathrm d\boldsymbol x\tag{6.34c}$$
$$=a\,\mathbb E_X[g(\boldsymbol x)]+b\,\mathbb E_X[h(\boldsymbol x)]\tag{6.34d}$$
- **Definition 6.5 (covariance, univariate).**
$$\mathrm{Cov}_{X,Y}[x,y]:=\mathbb E_{X,Y}\big[(x-\mathbb E_X[x])(y-\mathbb E_Y[y])\big]\tag{6.35}$$
 By linearity of expectations:
$$\mathrm{Cov}[x,y]=\mathbb E[xy]-\mathbb E[x]\mathbb E[y]\tag{6.36}$$
 Subscripts are often dropped. $\mathrm{Cov}[x,x]$ is the **variance** $\mathbb V_X[x]$; its square root is the **standard deviation** $\sigma(x)$ (p. 190).
- **Definition 6.6 (covariance, multivariate).** For $\boldsymbol x\in\mathbb R^D$, $\boldsymbol y\in\mathbb R^E$:
$$\mathrm{Cov}[\boldsymbol x,\boldsymbol y]=\mathbb E[\boldsymbol x\boldsymbol y^\top]-\mathbb E[\boldsymbol x]\mathbb E[\boldsymbol y]^\top=\mathrm{Cov}[\boldsymbol y,\boldsymbol x]^\top\in\mathbb R^{D\times E}\tag{6.37}$$
- **Definition 6.7 (variance)** of $X$ with states $\boldsymbol x\in\mathbb R^D$ and mean $\boldsymbol\mu$:
$$\mathbb V_X[\boldsymbol x]=\mathrm{Cov}_X[\boldsymbol x,\boldsymbol x]\tag{6.38a}$$
$$=\mathbb E_X[(\boldsymbol x-\boldsymbol\mu)(\boldsymbol x-\boldsymbol\mu)^\top]=\mathbb E_X[\boldsymbol x\boldsymbol x^\top]-\mathbb E_X[\boldsymbol x]\mathbb E_X[\boldsymbol x]^\top\tag{6.38b}$$
$$=\begin{bmatrix}\mathrm{Cov}[x_1,x_1]&\mathrm{Cov}[x_1,x_2]&\cdots&\mathrm{Cov}[x_1,x_D]\\ \mathrm{Cov}[x_2,x_1]&\mathrm{Cov}[x_2,x_2]&\cdots&\mathrm{Cov}[x_2,x_D]\\ \vdots&\vdots&\ddots&\vdots\\ \mathrm{Cov}[x_D,x_1]&\cdots&\cdots&\mathrm{Cov}[x_D,x_D]\end{bmatrix}\tag{6.38c}$$
- The $D\times D$ matrix (6.38c) is the **covariance matrix**. It is symmetric and positive semidefinite. The diagonal holds the variances of the marginals (6.39, same as (6.21)). Off-diagonal entries are cross-covariances $\mathrm{Cov}[x_i,x_j]$, $i\ne j$ (p. 190–191).
- Remark: the book generally assumes covariance matrices are positive definite and skips the low-rank semidefinite corner cases (p. 191).
- **Definition 6.8 (correlation).** The normalised covariance:
$$\mathrm{corr}[x,y]=\frac{\mathrm{Cov}[x,y]}{\sqrt{\mathbb V[x]\mathbb V[y]}}\in[-1,1]\tag{6.40}$$
 The correlation matrix is the covariance matrix of standardised variables $x/\sigma(x)$. Positive correlation: when $x$ grows, $y$ is expected to grow. Negative: as $x$ increases, $y$ decreases (Figure 6.5) (p. 191).

> **Intuition note.** Covariance is the average product of deviations from the means: it tends to be positive when the two variables lie on the same side of their means and negative when they lie on opposite sides. The variance of each variable affects the covariance, so dividing by the standard deviations gives the correlation, a number in $[-1,1]$ (p. 191).

**6.4.2 Empirical means and covariances (p. 191–192).**
- 6.4.1 gives *population* statistics. From data we use two steps: define a statistic of $N$ identical random variables $X_1,\dots,X_N$, then plug in the observed realisations $x_1,\dots,x_N$ (p. 191–192).
- **Definition 6.9.**
$$\bar{\boldsymbol x}:=\frac1N\sum_{n=1}^N\boldsymbol x_n,\quad \boldsymbol x_n\in\mathbb R^D\tag{6.41}$$
$$\boldsymbol\Sigma:=\frac1N\sum_{n=1}^N(\boldsymbol x_n-\bar{\boldsymbol x})(\boldsymbol x_n-\bar{\boldsymbol x})^\top\tag{6.42}$$
 $\boldsymbol\Sigma$ is $D\times D$, symmetric and positive semidefinite (p. 192).
- Margin note: the book uses this empirical covariance, which is a biased estimate. The unbiased ("corrected") version has $N-1$ in the denominator (p. 192).

**6.4.3 Three expressions for the variance (p. 192–193).**
- (i) Standard definition:
$$\mathbb V_X[x]:=\mathbb E_X[(x-\mu)^2]\tag{6.43}$$
 This is the mean of $Z:=(X-\mu)^2$. Computing it empirically needs two passes: first the mean, then the squared deviations (p. 192).
- (ii) **Raw-score formula**, "mean of the square minus square of the mean":
$$\mathbb V_X[x]=\mathbb E_X[x^2]-(\mathbb E_X[x])^2\tag{6.44}$$
 It needs one pass (accumulate $x_i$ and $x_i^2$). If implemented that way it can be numerically unstable: if the two terms are huge and approximately equal, we may lose numerical precision in floating-point arithmetic (margin note). It can be useful in ML, e.g. for deriving the bias–variance decomposition (p. 193).
- (iii) Pairwise differences. The author says that expanding the square shows:
$$\frac1{N^2}\sum_{i,j=1}^N(x_i-x_j)^2=2\left[\frac1N\sum_{i=1}^N x_i^2-\left(\frac1N\sum_{i=1}^N x_i\right)^2\right]\tag{6.45}$$
 The right side is twice the raw-score expression. So $N^2$ pairwise distances can be computed from $N$ deviations from the mean: pairwise distances and distances from the centre are equivalent (p. 193).

> **Intuition note.** Spread can be measured against one centre point, or between all pairs of points. (6.45) says the two are the same thing up to a factor 2, but the first needs only $O(N)$ terms.

**6.4.4 Sums and transformations of random variables (p. 193–194).** For $X,Y$ with states $\boldsymbol x,\boldsymbol y\in\mathbb R^D$:
$$\mathbb E[\boldsymbol x+\boldsymbol y]=\mathbb E[\boldsymbol x]+\mathbb E[\boldsymbol y]\tag{6.46}$$
$$\mathbb E[\boldsymbol x-\boldsymbol y]=\mathbb E[\boldsymbol x]-\mathbb E[\boldsymbol y]\tag{6.47}$$
$$\mathbb V[\boldsymbol x+\boldsymbol y]=\mathbb V[\boldsymbol x]+\mathbb V[\boldsymbol y]+\mathrm{Cov}[\boldsymbol x,\boldsymbol y]+\mathrm{Cov}[\boldsymbol y,\boldsymbol x]\tag{6.48}$$
$$\mathbb V[\boldsymbol x-\boldsymbol y]=\mathbb V[\boldsymbol x]+\mathbb V[\boldsymbol y]-\mathrm{Cov}[\boldsymbol x,\boldsymbol y]-\mathrm{Cov}[\boldsymbol y,\boldsymbol x]\tag{6.49}$$
- **Affine transformation.** $X$ has mean $\boldsymbol\mu$ and covariance $\boldsymbol\Sigma$; $\boldsymbol y=\boldsymbol A\boldsymbol x+\boldsymbol b$ with deterministic $\boldsymbol A,\boldsymbol b$ (if $\boldsymbol y\in\mathbb R^E$, $\boldsymbol A$ is $E\times D$; added step). Then (p. 194)
$$\mathbb E_Y[\boldsymbol y]=\mathbb E_X[\boldsymbol A\boldsymbol x+\boldsymbol b]=\boldsymbol A\mathbb E_X[\boldsymbol x]+\boldsymbol b=\boldsymbol A\boldsymbol\mu+\boldsymbol b\tag{6.50}$$
$$\mathbb V_Y[\boldsymbol y]=\mathbb V_X[\boldsymbol A\boldsymbol x+\boldsymbol b]=\mathbb V_X[\boldsymbol A\boldsymbol x]=\boldsymbol A\mathbb V_X[\boldsymbol x]\boldsymbol A^\top=\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top\tag{6.51}$$
- Cross-covariance of $\boldsymbol x$ with $\boldsymbol y=\boldsymbol A\boldsymbol x+\boldsymbol b$:
$$\mathrm{Cov}[\boldsymbol x,\boldsymbol y]=\mathbb E[\boldsymbol x(\boldsymbol A\boldsymbol x+\boldsymbol b)^\top]-\mathbb E[\boldsymbol x]\mathbb E[\boldsymbol A\boldsymbol x+\boldsymbol b]^\top\tag{6.52a}$$
$$=\mathbb E[\boldsymbol x]\boldsymbol b^\top+\mathbb E[\boldsymbol x\boldsymbol x^\top]\boldsymbol A^\top-\boldsymbol\mu\boldsymbol b^\top-\boldsymbol\mu\boldsymbol\mu^\top\boldsymbol A^\top\tag{6.52b}$$
$$=\boldsymbol\mu\boldsymbol b^\top-\boldsymbol\mu\boldsymbol b^\top+\big(\mathbb E[\boldsymbol x\boldsymbol x^\top]-\boldsymbol\mu\boldsymbol\mu^\top\big)\boldsymbol A^\top\tag{6.52c}$$
$$\overset{(6.38b)}{=}\boldsymbol\Sigma\boldsymbol A^\top\tag{6.52d}$$

> **Intuition note.** A shift $\boldsymbol b$ moves the mean but not the spread. The matrix $\boldsymbol A$ moves the mean like any vector and reshapes the spread as $\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top$.

**6.4.5 Statistical independence (p. 194–195).**
- **Definition 6.10.** $X,Y$ are statistically independent if and only if
$$p(\boldsymbol x,\boldsymbol y)=p(\boldsymbol x)p(\boldsymbol y)\tag{6.53}$$
 Intuitively, knowing $\boldsymbol y$ adds no information about $\boldsymbol x$ (and vice versa) (p. 194).
- If independent: $p(\boldsymbol y\mid\boldsymbol x)=p(\boldsymbol y)$; $p(\boldsymbol x\mid\boldsymbol y)=p(\boldsymbol x)$; $\mathbb V_{X,Y}[\boldsymbol x+\boldsymbol y]=\mathbb V_X[\boldsymbol x]+\mathbb V_Y[\boldsymbol y]$; $\mathrm{Cov}_{X,Y}[\boldsymbol x,\boldsymbol y]=\mathbf 0$ (p. 194).
- The last point may not hold in converse. Covariance measures only linear dependence, so nonlinearly dependent variables can have zero covariance (p. 194).
- **Example 6.5.** Let $\mathbb E_X[x]=0$ and $\mathbb E_X[x^3]=0$, and $y=x^2$ (so $Y$ depends on $X$). Then
$$\mathrm{Cov}[x,y]=\mathbb E[xy]-\mathbb E[x]\mathbb E[y]=\mathbb E[x^3]=0\tag{6.54}$$
- i.i.d.: "independent and identically distributed" variables $X_1,\dots,X_N$ are common in ML. For more than two variables, "independent" usually means *mutually* independent (all subsets independent). "Identically distributed" means same distribution (p. 195).
- **Definition 6.11 (conditional independence).** $X\perp\!\!\!\perp Y\mid Z$ if and only if
$$p(\boldsymbol x,\boldsymbol y\mid\boldsymbol z)=p(\boldsymbol x\mid\boldsymbol z)p(\boldsymbol y\mid\boldsymbol z)\quad\text{for all }\boldsymbol z\in\mathcal Z\tag{6.55}$$
 It must hold for every $\boldsymbol z$. Given $\boldsymbol z$, the joint of $\boldsymbol x,\boldsymbol y$ factorises. Independence is the special case $X\perp\!\!\!\perp Y\mid\emptyset$ (p. 195).
- By the product rule, $p(\boldsymbol x,\boldsymbol y\mid\boldsymbol z)=p(\boldsymbol x\mid\boldsymbol y,\boldsymbol z)p(\boldsymbol y\mid\boldsymbol z)$ (6.56). Comparing with (6.55), $p(\boldsymbol y\mid\boldsymbol z)$ appears in both, so
$$p(\boldsymbol x\mid\boldsymbol y,\boldsymbol z)=p(\boldsymbol x\mid\boldsymbol z)\tag{6.57}$$
 an alternative definition: given $\boldsymbol z$, knowing $\boldsymbol y$ does not change knowledge of $\boldsymbol x$ (p. 195).

> **Intuition note.** Independence means the joint is the product of the marginals. Covariance measures only linear dependence, so zero covariance is a weaker condition.

**6.4.6 Inner products of random variables (starts p. 195; this part ends mid-subsection, p. 196).**
- For uncorrelated $X,Y$:
$$\mathbb V[x+y]=\mathbb V[x]+\mathbb V[y]\tag{6.58}$$
 This looks like the Pythagorean theorem $c^2=a^2+b^2$, since variances are in squared units (p. 195).
- Random variables can be treated as vectors in a vector space. For zero-mean $X,Y$,
$$\langle X,Y\rangle:=\mathrm{Cov}[x,y]\tag{6.59}$$
 is an inner product: covariance is symmetric, positive definite and linear in either argument (p. 196). Margin note: $\mathrm{Cov}[x,x]=0\iff x=0$.
- Length: 
$$\|X\|=\sqrt{\mathrm{Cov}[x,x]}=\sqrt{\mathbb V[x]}=\sigma[x]\tag{6.60}$$
 A "longer" variable is more uncertain; length 0 means deterministic (p. 196).
- Angle:
$$\cos\theta=\frac{\langle X,Y\rangle}{\|X\|\,\|Y\|}=\frac{\mathrm{Cov}[x,y]}{\sqrt{\mathbb V[x]\mathbb V[y]}}\tag{6.61}$$
 This is the correlation (Def. 6.8). With Definition 3.7, $X\perp Y\iff\langle X,Y\rangle=0$, i.e. $X,Y$ are orthogonal iff $\mathrm{Cov}[x,y]=0$ (uncorrelated). Figure 6.6 shows the Pythagorean picture with sides $\sqrt{\mathrm{var}[x]}$, $\sqrt{\mathrm{var}[y]}$ and hypotenuse $\sqrt{\mathrm{var}[x+y]}$ (p. 196).
- A Remark on the Euclidean distance begins at the bottom of p. 196 and continues in the next part.

> **Intuition note.** Treat centred random variables as arrows. Their lengths are standard deviations and the cosine of the angle between them is the correlation. Uncorrelated means perpendicular, so variances add like squared sides of a right triangle.

## Toy example (ours, not from the text)
Take 100 observations of two binary variables, with counts $n_{ij}$: $(x_1,y_1)=30$, $(x_1,y_2)=10$, $(x_2,y_1)=20$, $(x_2,y_2)=40$, $N=100$.
- **Joint and marginals.** $P(x_1,y_1)=30/100=0.30$. Column sums: $c_1=30+10=40$, $c_2=20+40=60$, so $P(x_1)=0.4$, $P(x_2)=0.6$. Row sums: $r_1=30+20=50$, $r_2=10+40=50$, so $P(y_1)=0.5$.
- **Conditional and product rule.** $P(y_1\mid x_1)=30/40=0.75$. Check: $0.75\cdot0.4=0.30=P(x_1,y_1)$ ✓.
- **Evidence by the sum rule.** $P(y_1\mid x_2)=20/60=1/3$. $P(y_1)=0.75\cdot0.4+\tfrac13\cdot0.6=0.30+0.20=0.50$ ✓ (matches the row sum).
- **Bayes.** $P(x_1\mid y_1)=\dfrac{0.75\cdot0.4}{0.5}=0.6$. Direct count: $n_{11}/r_1=30/50=0.6$ ✓.
- **Not independent.** $P(x_1)P(y_1)=0.4\cdot0.5=0.20\ne0.30=P(x_1,y_1)$.
- **Covariance and correlation.** Code $x_1,y_1\mapsto0$ and $x_2,y_2\mapsto1$. $\mathbb E[x]=0.6$, $\mathbb E[y]=0.5$, $\mathbb E[xy]=P(x_2,y_2)=0.40$. By (6.36), $\mathrm{Cov}=0.40-0.6\cdot0.5=0.10$. $\mathbb V[x]=\mathbb E[x^2]-0.36=0.6-0.36=0.24$ and $\mathbb V[y]=0.5-0.25=0.25$. By (6.40), $\mathrm{corr}=0.10/\sqrt{0.24\cdot0.25}=0.10/\sqrt{0.06}\approx0.10/0.2449\approx0.41$, which is $\cos\theta$ in (6.61).

## Concepts
- [[probability-space]] (new) — triple $(\Omega,\mathcal A,P)$: outcomes, observable events, probabilities with $P(\Omega)=1$ (p. 175)
- [[random-variable]] (new) — a function $X:\Omega\to\mathcal T$, not random and not a variable (p. 175)
- [[probability-distribution-law]] (new) — $P_X=P\circ X^{-1}$; also loosely used for pmf/pdf/cdf (p. 177, p. 183)
- [[pmf-pdf-cdf]] (new) — pmf: $P(X=x)$; pdf: nonnegative, integrates to 1; cdf: $P(X\le x)$ (p. 178, p. 181)
- [[sum-rule-marginalization]] (new) — $p(x)=\sum_y p(x,y)$ or $\int p(x,y)\,\mathrm dy$ (p. 184)
- [[product-rule]] (new) — $p(x,y)=p(y\mid x)p(x)$ (p. 184)
- [[bayes-theorem]] (new) — posterior = likelihood × prior / evidence, a consequence of the product rule (p. 185)
- [[expected-value]] (new) — $\mathbb E_X[g(x)]$, a linear operator; mean is $g=$ identity (p. 187–189)
- [[mean-median-mode]] (new) — three notions of "average"; the median has no obvious multivariate generalisation, and densities may have very many modes, so finding all of them is hard (p. 188)
- [[covariance matrix]] — $\mathbb E[\boldsymbol{xx}^\top]-\mathbb E[\boldsymbol x]\mathbb E[\boldsymbol x]^\top$; symmetric positive semidefinite (p. 190)
- [[correlation]] (new) — covariance divided by the product of standard deviations, in $[-1,1]$ (p. 191)
- [[empirical-mean-covariance]] (new) — data-based estimates (6.41–6.42); the covariance uses the biased $1/N$ (p. 192)
- [[raw-score-variance]] (new) — $\mathbb E[x^2]-(\mathbb E[x])^2$; one pass but possibly numerically unstable (p. 193)
- [[statistical-independence]] (new) — $p(x,y)=p(x)p(y)$; implies zero covariance, not conversely (p. 194)
- [[conditional-independence]] (new) — factorisation of $p(x,y\mid z)$ for all $z$ (p. 195)
- [[iid]] (new) — independent, identically distributed variables (p. 195)
- [[dot (inner) product]] — here $\langle X,Y\rangle=\mathrm{Cov}[x,y]$ on zero-mean random variables (p. 196)
- [[cosine similarity]] — here correlation is the cosine of the angle between random variables (p. 196)
- [[orthogonality]] — here: uncorrelated ⟺ $\mathrm{Cov}=0$ (p. 196)

## Canonical instances
- [[two-coin-draw-with-replacement]] — pmf of $X$ = number of $ from $P(\$)=0.3$: 0.09, 0.42, 0.49 (p. 176)
- [[friend-is-late]] — hypotheses H1–H3 as plausible reasoning beyond Boolean logic (p. 173)
- [[uniform-discrete-vs-continuous]] — density can exceed 1 but integrates to 1 (p. 182–183)
- [[bimodal-gaussian-mixture]] — a bimodal density whose marginal shows that mean and median can differ (p. 188–189)
- [[x-and-x-squared-uncorrelated]] — zero covariance without independence (p. 194)

## Bridges (candidates)
- [same-math] correlation $=\cos\theta$ (6.61) ↔ linear-algebra: cosine similarity — the inner product of normalised (centred) vectors.
- [same-math] covariance matrix symmetric PSD (p. 190) ↔ linear-algebra: spectral theorem — real symmetric PSD matrices have orthonormal eigenbases and nonnegative eigenvalues.
- [same-math] $\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top$ (6.51) ↔ linear-algebra: how a linear map transforms a quadratic form / covariance of linearly mapped data.
- [structural-analogy] conditional probability tables $P(Y\mid X)$ (columns sum to 1) ↔ Markov (stochastic) matrix — nonnegative columns summing to 1.
- [structural-analogy] raw-score variance instability (p. 193) ↔ numerical stability: algebraically equal formulas can differ in rounding behaviour.
- [metaphor] probability as "logic with degrees" ↔ Boolean logic as a limiting case.

## Questions this raises
- If covariance captures only linear dependence, which statistics detect nonlinear dependence such as $y=x^2$?
- Why is the evidence $p(\boldsymbol y)$ so often intractable, and what is done when it is?
- How does the biased $1/N$ empirical covariance compare with the unbiased $1/(N-1)$ version, and does the difference matter for large $N$?
- Does the geometry of random variables (angles, Pythagoras) extend to non-zero-mean or multivariate variables (a margin note says multivariate can be treated similarly)?

## Reading notes
- **Part boundaries.** This part starts at the opening of Chapter 6 (printed p. 172) and ends at the bottom of printed p. 196, where a Remark in §6.4.6 (on using the Euclidean distance) begins and is cut off. The rest of §6.4.6, §6.5 onwards and the chapter's exercises are in the next part. The split is at a section boundary in the source notes, but the page range stops mid-subsection.
- **Page offset:** printed = pdf − 6.
- The text layer of Figure 6.1 (p. 173) is garbled. I used the page image. Equations were checked against the images; none was unreadable.
- A margin note on p. 192 says the derivations are exercises at the end of the chapter. They are not in this unit, so there is no Exercises section.
- Loose phrasing in the source: p. 193 says the sum of $N^2$ pairwise differences is the empirical variance, but (6.45) shows that the normalised sum equals *twice* the raw-score variance. I followed (6.45).
- Cross-reference to "(8.44)" on p. 186 and forward references to Sections 6.5–6.7 and Chapter 8 point outside these pages.
- The book is a free "Draft (2024-01-15)" version (footer on pages); running headers show "Probability and Distributions".

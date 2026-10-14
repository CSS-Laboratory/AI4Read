---
id: jaynes-2003-probability/ch19-physical
work: jaynes-2003-probability
unit: "19 Physical measurements"
pages: 589-600
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Physical measurements

## L0 — One line
Applying Bayes' theorem to the "equations of condition" with Gaussian errors and a uniform prior gives the weighted least-squares estimate $\hat x=(\tilde AWA)^{-1}\tilde AWy$ and its accuracy $(\tilde AWA)^{-1}$, without any guess about linear combinations.

## L1 — The gist (≤ 120 words)
How should one combine more measurements than unknowns, each with its own accuracy, into best estimates and error bars? This is the problem that defeated Euler. Older practice conjectured that estimates are linear combinations of the data and then had to choose the combination. Jaynes instead applies Bayes' theorem to the linear model with independent Gaussian errors, which he treats as a description of knowledge, not a claim about error frequencies. The posterior is Gaussian. Its mean gives the best estimate, and the inverse of $K=\tilde AWA$ gives the covariance. A three-experiment example for $e$ and $m$ shows a surprising case where a good measurement is irrelevant. The underdetermined case needs prior information such as maximum entropy.

**Prerequisites:** matrix multiplication, transpose, inverse and rank; Gaussian density; Bayes' theorem; the maximum-entropy idea.

## L2 — Key ideas
- Measurements are modelled as linear equations of condition $y=Ax+\delta$. Overdetermined means $N>n$ (more observations than unknowns). Euler had $N=75$, $n=8$ (p. 591).
- The old approach assumed estimates $\hat x=(BA)^{-1}By$ and left $B$ open. Chapter 13's decision theory replaces this guess with a posterior calculation (p. 591–592).
- A Gaussian error law is a state of knowledge fixed by the first two moments through maximum entropy. It is not an assumption about frequencies (p. 592–593).
- With Gaussian errors and a uniform prior, the posterior is Gaussian. Its mean is $\hat x=(\tilde AWA)^{-1}\tilde AWy$, so $B=\tilde AW$. Its covariance is $K^{-1}$ (p. 594, 596, 597).
- If $N<n$, $K$ is singular and the data fix only a feasible set. Extra prior information, e.g. maximum entropy, is needed (p. 594–595).
- In the $e,m$ example, the ±5% measurement of $e^2/m$ improves the errors only modestly. A ±2% measurement gets much higher weight and improves them more, $e$ roughly twice as much as $m$ (p. 598–599).
- A good measurement can drop out of an estimate. Probability theory finds this directly, and Jaynes argues it is not an offence like discarding relevant data (p. 599–600).
- With heavy-tailed errors the posterior may be multimodal. Then point estimates and probable errors are not an honest summary, and the whole posterior should be given (p. 600).

## L3 — Walkthrough

### 19.1 Reduction of equations of condition
**Set-up (p. 589–590).** Three experiments measure $e$ (±2%), $e/m$ (±1%) and $e^2/m$ (±5%). Take rough values $e_0,m_0$ and write the true values as $e=e_0(1+x_1)$, $m=m_0(1+x_2)$ (19.1), with $x_1,x_2$ small. The data are $M_1=e_0(1+y_1)$, $M_2=\frac{e_0}{m_0}(1+y_2)$, $M_3=\frac{e_0^2}{m_0}(1+y_3)$ (19.2). The $y_i$ are known. To first order the true quantities are $e/m=\frac{e_0}{m_0}(1+x_1-x_2+\cdots)$ and $e^2/m=\frac{e_0}{m_0}(1+2x_1-x_2+\cdots)$ (19.3). Exact measurements would give $y_1=x_1$, $y_2=x_1-x_2$, $y_3=2x_1-x_2$ (19.4). With errors $\delta_i$ (fractional errors of each measurement):
$$y_i=\sum_j a_{ij}x_j+\delta_i,\qquad A=\begin{pmatrix}1&0\\1&-1\\2&-1\end{pmatrix}\tag{19.5–19.6}$$

**General form (p. 591).** $y_i=\sum_{j=1}^n a_{ij}x_j+\delta_i$ (19.7), i.e. $y=Ax+\delta$ (19.8), with $A$ of shape $N\times n$, $y\in\mathbb R^N$, $x\in\mathbb R^n$.

**Old reasoning (p. 591).** $A$ is not square, so it has no inverse when $N>n$. Multiply by an $n\times N$ matrix $B$ with $(BA)^{-1}$ existing:
$$By=BAx+B\delta,\tag{19.9}$$
$$x=(BA)^{-1}B(y-\delta).\tag{19.10}$$
If $p(\delta_i)=p(-\delta_i)$, so $\langle\delta_i\rangle=0$, then for given $B$ the best estimate "by almost any reasonable loss function criterion" is
$$\hat x=(BA)^{-1}By.\tag{19.11}$$
Different $B$ give different estimates. Euler had billions of choices. Least squares was a popular criterion for choosing $B$. Jaynes will reach the same solution by different reasoning.

*Intuition note.* Any $B$ for which $(BA)^{-1}$ exists turns the overdetermined system into a solvable one, but different $B$ give different estimates. The real question is which $B$ is best.

### 19.2 Reformulation as a decision problem
By Chapter 13, the best estimate under any loss function comes from the posterior: apply Bayes' theorem, then minimise expected loss over the posterior (p. 592). Linearity of $\hat x$ in $y$ was only a conjecture. Applying Bayes' theorem to the equations of condition should show whether the estimate is linear. If it is, the theorem should also give the best $B$ and the accuracy, which least squares does not give (p. 592).

**19.2.1 Sermon on Gaussian error distributions (p. 592–593).**
- **Orthodox view:** errors are sums of many small independent imperfections, so the central limit theorem gives a Gaussian *frequency* distribution. Jaynes says this argument is fine but misleading. It suggests that a Gaussian assignment "assumes" something false when the true frequencies are not Gaussian (p. 592). Footnote 1 notes that, in general, the Gaussian approximation is good only for total errors that can arise in many different ways.
- **Jaynes' view:** the Gaussian assignment describes our state of knowledge. We hardly ever know more than the general magnitude of the errors, which can reasonably be interpreted as fixing the first two moments. Maximum entropy then gives independent Gaussians. The region of probable noise vectors is as large as it can be under that constraint (p. 592–593).
- Learning that the true frequencies are Gaussian would not help, because that is what we already predicted. Knowing a specific departure from Gaussian would confine errors to a smaller region $\Omega_1\subset\Omega$. Data in $\Omega-\Omega_1$ would then count as signal, and Bayes' theorem handles this automatically (p. 593).
- Conclusion: given second moments, a non-Gaussian frequency distribution will not make inferences worse. Knowledge of it would make them better (p. 593).

**Assignment (p. 593).** With weights $w_i=1/\langle\delta_i^2\rangle$,
$$p(\delta_1\cdots\delta_N)\,d\delta=(\text{const.})\exp\Big\{-\tfrac12\sum_i w_i\delta_i^2\Big\}d\delta,\tag{19.12}$$
e.g. $w_1=1/(0.02)^2=2500$ (19.13). Weights are taken as known. From (19.7) and (19.12) the sampling density is
$$p(y|x)=C_1\exp\Big\{-\tfrac12\sum_i w_i\Big[y_i-\sum_j a_{ij}x_j\Big]^2\Big\}.\tag{19.14}$$
With uniform priors on the $x_j$, the posterior has the same form in $x$ (19.15, p. 594).

**Completing the square (p. 594).** Expand:
$$\sum_i w_i\Big(y_i-\sum_j a_{ij}x_j\Big)^2=\sum_{j,k}K_{jk}x_jx_k-2\sum_j L_jx_j+\sum_i w_iy_i^2\tag{19.16}$$
(the page prints $x_ix_k$, a misprint for $x_jx_k$), with
$$K_{jk}=\sum_i w_ia_{ij}a_{ik},\quad L_j=\sum_i w_iy_ia_{ij};\qquad K=\tilde AWA,\ L=\tilde AWy,\tag{19.17–19.18}$$
where $W_{ij}=w_i\delta_{ij}$ is diagonal, $N\times N$, $K$ is $n\times n$ and $L$ has length $n$. Write the posterior as
$$p(x|y)=C_3\exp\Big\{-\tfrac12\sum_{j,k}K_{jk}(x_j-\hat x_j)(x_k-\hat x_k)\Big\}\tag{19.19}$$
Comparing with (19.16) gives $\sum_kK_{jk}\hat x_k=L_j$ (19.20). If $K$ is nonsingular, $\hat x$ is unique.

*Intuition note.* The posterior is a bell-shaped cloud in parameter space. Its centre solves the linear equations (19.20), and $K$ measures how sharply the cloud is peaked.

### 19.3 The underdetermined case: K is singular (p. 594–595)
If $N<n$, $K$ has rank at most $N$, so it is singular. Then (19.20) has infinitely many solutions, and the maximum likelihood lies on a linear manifold of dimension $n-N$. A maximum-likelihood solution still exists:
$$x^*=\tilde A(A\tilde A)^{-1}y\tag{19.21}$$
It gives $y=Ax^*$, so the quadratic form vanishes. This "canonical inverse" can be computed by maximum entropy. Adding any $z$ with $Az=0$ gives $x^*+z$ with equal likelihood, so the solutions form a manifold $\Delta$ of dimension $n-N$.

Exercise 19.1 asks to show that $x^*$ also minimises $\sum(x_i^*)^2$ on $\Delta$. Jaynes remarks that there seems to be no compelling reason to want minimum length (p. 595).

The data restrict $x$ to a feasible set $\Delta$ but cannot choose a point in it. Prior information can supply the choice. These "generalized inverse" problems, such as image reconstruction, probably make up most real problems. Maximum entropy often resolves them, as Chapters 11 and 20 describe (p. 595).

### 19.4 The overdetermined case: K can be made nonsingular (p. 595–596)
$\sum_{jk}K_{jk}q_jq_k=\sum_iw_i(\sum_ja_{ij}q_j)^2\ge0$ (19.22). So if $K$ has rank $n$, it is positive definite. With $N\ge n$ this holds unless the problem was badly set up:
- An observation with $w_i=0$ carries no information, so drop it (reduce $N$).
- If some $q\neq0$ has $\sum_ja_{ij}q_j=0$ for all $i$, then $x$ and $x+cq$ give identical data. The columns of $A$ are linearly dependent, so drop that parameter and its column of $A$.

After such removals, if cogent observations $\ge$ relevant parameters, $K$ is positive definite and
$$\hat x_k=\sum_j(K^{-1})_{kj}L_j\tag{19.23}$$
$$\hat x=(\tilde AWA)^{-1}\tilde AWy\tag{19.24}$$
In the Gaussian case with uniform prior, the best estimates are therefore linear in $y$, as in (19.11), with the best choice
$$B=\tilde AW\tag{19.25}$$
Jaynes says this was "perhaps first found by Gauss" and repeated by Laplace (p. 596).

### 19.5 Numerical evaluation (p. 596–597)
Weights: $w_1=2500$, $w_2=1/(0.01)^2=10\,000$, $w_3=1/(0.05)^2=400$ (19.26). Then
$$B=\tilde AW=\begin{pmatrix}w_1&w_2&2w_3\\0&-w_2&-w_3\end{pmatrix}\ (2\times3),\tag{19.27}$$
$$K=\begin{pmatrix}w_1+w_2+4w_3&-(w_2+2w_3)\\-(w_2+2w_3)&w_2+w_3\end{pmatrix},\tag{19.28}$$
$$K^{-1}=\frac1{|K|}\begin{pmatrix}w_2+w_3&w_2+2w_3\\w_2+2w_3&w_1+w_2+4w_3\end{pmatrix},\quad |K|=w_1w_2+w_2w_3+w_3w_1\tag{19.29–19.30}$$
$$(\tilde AWA)^{-1}\tilde AW=\frac1{|K|}\begin{pmatrix}w_1(w_2+w_3)&-w_2w_3&w_2w_3\\w_1(w_2+2w_3)&-w_2(w_1+2w_3)&w_3(w_2-w_1)\end{pmatrix}\tag{19.31}$$
$$\hat x_1=\frac{w_1(w_2+w_3)y_1+w_2w_3(y_3-y_2)}{|K|},$$
$$\hat x_2=\frac{w_1w_2(y_1-y_2)+w_2w_3(y_3-2y_2)+w_3w_1(2y_1-y_3)}{|K|}\tag{19.32}$$
Numerically ($|K|=3\times10^7$):
$$\hat x_1=\tfrac{13}{15}y_1+\tfrac2{15}(y_3-y_2),\qquad \hat x_2=\tfrac56(y_1-y_2)+\tfrac2{15}(y_3-2y_2)+\tfrac1{30}(2y_1-y_3)\tag{19.33}$$
(the page prints $(y_2-y_3)$ in the first line; see Reading notes). These are weighted averages of estimates from pairs of experiments. Experiment 1 gives $y_1$ for $x_1$. Experiments 2 and 3 give $e$ as $(e^2/m)(e/m)^{-1}$, and $\frac{(e_0^2/m_0)(1+y_3)}{(e_0/m_0)(1+y_2)}\approx e_0(1+y_3-y_2)$ (19.34). So the two independent estimates of $x_1$ are combined with weights 13/15 and 2/15. $\hat x_2$ is a weighted average of three estimates that are not independent (p. 597).

### 19.6 Accuracy of the estimates (p. 597–599)
From (19.19): $\langle(x_j-\hat x_j)(x_k-\hat x_k)\rangle=(K^{-1})_{jk}$ (19.35, 19.36). So $(x_j)_{\rm est}=\hat x_j\pm\sqrt{(K^{-1})_{jj}}$ (19.37). Equations (19.24) and (19.37) are "the general solution of the problem, which Euler needed" (p. 598). Here
$$(x_1)_{\rm est}=\hat x_1\pm\sqrt{\tfrac{w_2+w_3}{|K|}},\quad (x_2)_{\rm est}=\hat x_2\pm\sqrt{\tfrac{w_1+w_2+4w_3}{|K|}}\tag{19.38}$$
numerically $\pm0.0186$ and $\pm0.0216$ (19.39). So $e$ is known to ±1.86% and $m$ to ±2.16%.

**Value of the ±5% experiment.** Setting $w_3\to0$ gives $\hat x_1=y_1$, $\hat x_2=y_1-y_2$ (19.40) and $K^{-1}=\frac1{w_1w_2}\begin{pmatrix}w_2&w_2\\w_2&w_1+w_2\end{pmatrix}$ (19.41). The results are $x_1=y_1\pm0.020$ and $x_2=y_1-y_2\pm0.024$ (19.42; see Reading notes). A poor measurement adds little to accurate ones.

**Improved $e^2/m$ at ±2%** ($w_1=w_3=2500$, $w_2=10\,000$):
$$\hat x_1=0.556y_1+0.444(y_3-y_2),$$
$$\hat x_2=0.444(y_1-y_2)+0.444(y_3-2y_2)+0.112(2y_1-y_3)\tag{19.43}$$
with $x_1=\hat x_1\pm0.0149$ and $x_2=\hat x_2\pm0.020$ (19.44). The accuracy of $e$ improves roughly twice as much as that of $m$, since $e^2/m$ contains $e$ squared but $m$ only to the first power (p. 599).

Exercise 19.2 asks for a general program. If the weights are not known, partial prior information about them gives a prior $p(w|I)$, which causes "no new difficulties of principle" (p. 599).

*Intuition note.* Each experiment contributes precision $w_i$ along the direction $a_i$ in parameter space. Adding these contributions gives $K$, and the final uncertainty is its inverse.

### 19.7 Comments
**19.7.1 A paradox (p. 599–600).** In (19.32), $y_3$ enters $\hat x_2$ once with a positive and once with a negative coefficient. If $w_1=w_2$ the $y_3$ terms cancel and $\hat x_2=y_1-y_2$ (19.45). So the $e^2/m$ measurement is used in estimating $m$ only because the $e$ and $e/m$ measurements differ in accuracy. If they are equal, then however accurate $e^2/m$ is, it should be ignored for $m$. Jaynes expects intuition to revolt but says "check the derivation" (p. 600). He argues that $e^2/m$ is irrelevant for $m$ when $e$ and $e/m$ have equal accuracy. He invites the reader to suppose $e^2/m$ were known exactly from the start and to see why it is still irrelevant. So this is not the offence of discarding relevant data criticised in Chapter 17. Exercise 19.3 asks the reader to confirm this with $w_1=w_2=1$, $w_3=100$.

**Loss functions and error laws (p. 600).** With wider-tailed errors, e.g. Cauchy $p(\delta)\propto(1+w\delta^2/2)^{-1}$, the posterior $p(x_1x_2|y_1y_2y_3)$ may have several peaks.
- A quadratic loss, or any "concave" loss (the author's parenthetical: doubling the error more than doubles the loss), then gives estimates between the peaks, which are very unlikely.
- With a convex loss, the equation for the best estimator may have several solutions.

Jaynes reads this as a sign that our knowledge is too complicated for best estimates and probable errors. The honest description is the full posterior, which is a limitation of decision theory.

## Toy example (ours)
One unknown $x$, two measurements $y_1=x+\delta_1$, $y_2=x+\delta_2$. Then $A=\binom11$ ($N=2$, $n=1$). Accuracies are $\sigma_1=0.5$ and $\sigma_2=1$, so $w_1=1/0.25=4$ and $w_2=1/1=1$. Data: $y=(0.10,\,0.20)$.
- $K=\tilde AWA=4\cdot1\cdot1+1\cdot1\cdot1=5$.
- $L=\tilde AWy=4(0.10)+1(0.20)=0.60$.
- $\hat x=L/K=0.12$. Check as a weighted average: $\tfrac45(0.10)+\tfrac15(0.20)=0.08+0.04=0.12$.
- $K^{-1}=1/5$, so the sd is $\sqrt{0.2}\approx0.447$. This is smaller than $\sigma_1=0.5$: the weaker measurement still helps a little, while $\hat x$ stays close to the better one.

## Concepts
- [[equations-of-condition]] (new) — overdetermined linear system $y=Ax+\delta$ relating data to small parameter corrections (p. 590–591)
- [[bayes-theorem]] — applied directly to $y=Ax+\delta$ to get the posterior and the best estimate, instead of conjecturing a linear form (p. 592)
- [[maximum-entropy-principle]] — given only the error magnitude (second moments), it yields independent Gaussians; it also resolves underdetermined problems (p. 592, 595)
- [[posterior-distribution]] — here Gaussian, with mean $\hat x$ and covariance $K^{-1}$ (p. 594, 597)
- [[likelihood]] — the Gaussian sampling density (19.14) with weights $w_i=1/\langle\delta_i^2\rangle$ (p. 593)
- [[generalized-inverse-problem]] (new) — $N<n$: the data give only a feasible manifold, and prior information must pick a point (p. 595)
- [[gaussian-as-state-of-knowledge]] (new) — the Gaussian is a description of knowledge, not an assumption about error frequencies (p. 592)

## Canonical instances
- [[euler-jupiter-saturn]] — 8 parameters from 75 observations, which defeated Euler and was solved by Laplace (p. 589, 591)
- [[electron-e-m-measurement]] — three experiments on $e$, $e/m$ and $e^2/m$ combined to estimate $e$ and $m$ (p. 589–599)
- [[cauchy-error-multimodal]] — wider-tailed errors give a multimodal posterior, and point estimates mislead (p. 600)

## Bridges (candidates)
- [same-math] Weighted least squares $\hat x=(\tilde AWA)^{-1}\tilde AWy$ ↔ bayesian: posterior mean in a Gaussian linear model with flat prior — same formula (p. 596)
- [structural-analogy] Underdetermined solution $x^*=\tilde A(A\tilde A)^{-1}y$ chosen by minimum length or maximum entropy ↔ information-theory: choosing among data-consistent models by an entropy criterion (p. 594–595)
- [structural-analogy] Gaussian as the maximum-entropy law under moment constraints ↔ information-theory: exponential family / Gibbs distribution (p. 592)
- [metaphor] A good measurement carrying no information once others are fixed ↔ information-theory: conditional independence or zero mutual information (p. 600)

## Questions this raises
- Why does $y_3$ drop out exactly when $w_1=w_2$? What does the geometry of the rows of $A$ say about this?
- How does the answer change if the weights $w_i$ are unknown and given a prior, as mentioned on p. 599?
- Which prior information, beyond minimum length, should select a point on the feasible set when $N<n$?
- How should one summarise the result when the posterior is multimodal?

## Exercises worth doing
- Ex. 19.1 (p. 595) — shows the canonical inverse minimises $\sum x_i^{*2}$ on the feasible manifold — difficulty: medium
- Ex. 19.2 (p. 599) — implements the general solution (19.24), (19.37) and checks it on the $e,m$ problem — difficulty: medium
- Ex. 19.3 (p. 600) — resolves the "paradox": $w_1=w_2=1$, $w_3=100$ — difficulty: medium

## Reading notes
- Printed page = pdf − 30.
- (19.33) prints $\tfrac{2}{15}(y_2-y_3)$ in $\hat x_1$. (19.32) gives $(y_3-y_2)$, the text after (19.34) says $(y_3-y_2)$ is the estimate from experiments 2 and 3, and (19.43) uses $(y_3-y_2)$. This looks like a sign misprint.
- (19.16) shows $x_ix_k$ where $x_jx_k$ is meant. The sentence introducing (19.14) says "true values $\{x_1,\ldots,x_N\}$" where $x_n$ is meant.
- (19.42) prints $x_2=y_1-y_2\pm0.024$. From (19.41), $\sqrt{(w_1+w_2)/(w_1w_2)}=\sqrt{5\times10^{-4}}\approx0.0224$, so 0.024 looks like a misprint. The first line prints $\pm1/w_1$ without a root sign, but $\sqrt{1/w_1}=0.020$ is meant.
- (19.39) gives 0.0216. Direct computation gives $\sqrt{4.7\times10^{-4}}\approx0.02168$, which rounds to 0.0217.
- p. 600 refers to "(19.22)" and "(19.26)" for the estimator, which look like loose cross-references; the estimator equations are (19.20) and (19.32).
- The "concave"/"convex" wording on p. 600 is reproduced as printed.

---
id: murphy-2023-pml2/ch02-probability-p3
work: murphy-2023-pml2
unit: "2 Probability (part 3/3): end of 2.4, then 2.5 Transformations of random variables, 2.6 Markov chains, 2.7 Divergence measures"
pages: 44-62
fields: [bayesian]
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
# Transformations of random variables, Markov chains, and divergences between distributions

## L0 — One line
Densities change under transformations by a Jacobian rule, Markov chains settle into a stationary distribution under stated conditions, and distributions can be compared through density ratios (f-divergences) or through differences of expectations (IPMs such as MMD).

## L1 — The gist (≤ 120 words)
This part of Chapter 2 finishes the maximum-entropy link to the exponential family. It then answers three questions. How does a density change when a random variable is transformed? Answer: the change-of-variables formula, Monte Carlo, and the probability integral transform. How does a sequence model with one-step memory behave, how are its parameters estimated, and when does it have a long-run distribution? Answer: Markov chains, n-gram counts, and irreducibility/aperiodicity/ergodicity. How can two distributions be compared? Answer: f-divergences (ratio-based) and integral probability metrics (difference-based), with total variation as the one measure in both families. A binary classifier can estimate the density ratio (with equal class priors) and, for a particular loss, plays the role of a witness function.

**Prerequisites:** pdf/cdf, Jacobian and determinant, matrix multiplication and eigenvectors, Jensen's inequality, Bayes' rule, log-likelihood, inner products and kernels.

## L2 — Key ideas
- Under a bijection $y=f(x)$, $p_y(y)=p_x(f^{-1}(y))\,|\det J_{f^{-1}}(y)|$; the mode of $p_y$ need not be the transform of the mode of $p_x$ (pp. 44–45).
- Monte Carlo approximates $p_y$ when the Jacobian is hard; the probability integral transform shows $P_X(X)\sim\mathrm{Unif}(0,1)$. This yields the KS test and inverse-cdf sampling (pp. 45–46).
- The Markov assumption gives $p(x_{1:T})=p(x_1)\prod_t p(x_t|x_{t-1})$. For finite states, $n$-step transitions are matrix powers $\mathbf A^n$; higher-order models reduce to first-order ones on an augmented state (pp. 47–49).
- Counts give the MLE of a Markov chain; with sparse $n$-gram data this overfits, and MAP estimation with a uniform Dirichlet prior (with $\alpha=1$) gives add-one smoothing (pp. 50–51).
- A stationary distribution solves $\pi=\pi\mathbf A$. An irreducible, aperiodic finite chain has a limiting distribution equal to its unique stationary one. For regular chains, detailed balance is sufficient but not necessary for stationarity (pp. 52–55).
- f-divergences compare densities by ratio and include KL, alpha, Hellinger and $\chi^2$. IPMs compare by $\sup_f|\mathbb E_P f-\mathbb E_Q f|$ and include Wasserstein-1, MMD and TV (pp. 55–61).
- MMD equals the distance between kernel mean embeddings, computed by the kernel trick; kernel choice matters a lot (pp. 58–60).
- A classifier trained to separate $P$ from $Q$ estimates $r=P/Q$; its risk links to f-divergences, and with a particular loss it acts as an IPM witness function (pp. 61–62).

## L3 — Walkthrough

### End of 2.4: maximum entropy and the exponential family
- The normalizer of the max-entropy distribution is $Z=\sum_x q(x)\exp\left(-\sum_k\lambda_k f_k(x)\right)$ (2.256) (p. 44).
- This has the exponential-family form. Here $f(x)$ is the vector of sufficient statistics, $-\lambda$ the natural parameters, and $q(x)$ the base measure (p. 44).
- Matching first and second moments with $f_1=x$, $f_2=x^2$ gives the Gaussian (p. 44).

### 2.5 Transformations of random variables
Setting: $x\sim p_x$, $y=f(x)$ deterministic; we want $p_y$ (p. 44).

**2.5.1 Invertible transformations.** A bijection is injective (one-to-one) and surjective (onto), so it has an inverse (Fig. 2.11) (p. 44). For a bijection $f:\mathbb R^n\to\mathbb R^n$:
$$p_y(\boldsymbol y)=p_x\!\left(f^{-1}(\boldsymbol y)\right)\left|\det\left[\mathbf J_{f^{-1}}(\boldsymbol y)\right]\right|\tag{2.257}$$
Here $\mathbf J_{f^{-1}}$ is the Jacobian (matrix of partial derivatives) of the inverse mapping, with entries $\partial x_i/\partial y_j$, an $n\times n$ matrix (2.258) (p. 44). If $\mathbf J$ is triangular, the determinant is the product of the diagonal terms:
$$\det(\mathbf J)=\prod_{i=1}^n\frac{\partial x_i}{\partial y_i}\tag{2.259}$$
(p. 45).

*Intuition note:* A transformation stretches or squeezes space. The Jacobian determinant measures the local stretch, so the density is rescaled to keep total probability equal to 1. Because the rescaling varies from point to point, the mode of the transformed density need not be the image of the original mode (Fig. 2.12).

**2.5.2 Monte Carlo approximation.** If the Jacobian is hard to compute, draw $\boldsymbol x^s\sim p(\boldsymbol x)$, set $\boldsymbol y^s=f(\boldsymbol x^s)$, and use the empirical pdf
$$p_{\mathcal D}(\boldsymbol y)=\frac1S\sum_{s=1}^S\delta(\boldsymbol y-\boldsymbol y^s)\tag{2.260}$$
(p. 45). Example: $x\sim\mathcal N(6,1)$ and $f(x)=\frac1{1+\exp(-x+5)}$. Fig. 2.12 shows the mode of the transformed distribution is not the transform of the original mode (p. 45).

**2.5.3 Probability integral transform (PIT).** Let $X$ have cdf $P_X$ and $Y=P_X(X)$. Then
$$P_Y(y)=\Pr(P_X(X)\le y)\tag{2.261}$$
$$=\Pr(X\le P_X^{-1}(y))=P_X(P_X^{-1}(y))=y\tag{2.262}$$
so $Y$ is uniform (p. 45). Fig. 2.13 checks this by sampling from three different pdfs: the empirical cdf of $y_n=P_X(x_n)$ is linear and the kernel-density estimate is roughly flat (pp. 45–46). Two uses follow.
- **KS test.** Compare the empirical cdf $P_n$ with the theoretical cdf $P$ using $D_n=\max_x|P_n(x)-P(x)|$ (2.263). $D_n$ should approach 0 as $n\to\infty$ if samples come from $P$ (p. 46).
- **Sampling.** If $u_n\sim\mathrm{Unif}(0,1)$, then $x_n=P_X^{-1}(u_n)$ is a sample from the distribution with cdf $P_X$ (p. 46).

*Intuition note:* Pushing a variable through its own cdf flattens it to a uniform. Run backwards, this turns uniform random numbers into samples from any distribution whose cdf can be inverted.

### 2.6 Markov chains
Markov assumption: if $\boldsymbol x_t$ is a sufficient statistic of the past, then $p(\boldsymbol x_{t+\tau}|\boldsymbol x_t,\boldsymbol x_{1:t-1})=p(\boldsymbol x_{t+\tau}|\boldsymbol x_t)$ for any $\tau\ge0$ (2.264) (p. 46). Then
$$p(\boldsymbol x_{1:T})=p(\boldsymbol x_1)\prod_{t=2}^T p(\boldsymbol x_t|\boldsymbol x_{t-1})\tag{2.265}$$
(p. 47).

**2.6.1 Parameterization.**
- *Kernels (2.6.1.1).* $p(\boldsymbol x_t|\boldsymbol x_{t-1})$ is the transition function, transition kernel or Markov kernel. If it does not depend on time, the model is homogeneous, stationary or time-invariant. This is parameter tying: a fixed number of parameters covers any number of variables (p. 47).
- *Matrices (2.6.1.2).* For $X_t\in\{1,\dots,K\}$ (a finite-state chain), $\mathbf A$ is $K\times K$ with $A_{ij}=p(X_t=j|X_{t-1}=i)$. Rows sum to one ($\sum_jA_{ij}=1$), so $\mathbf A$ is a stochastic matrix (p. 47).
- A stationary finite-state chain is equivalent to a stochastic automaton, drawn as a state transition diagram whose arcs are the non-zero entries of $\mathbf A$ (p. 48).
- Examples: the 2-state $\mathbf A=\begin{pmatrix}1-\alpha&\alpha\\\beta&1-\beta\end{pmatrix}$ (2.266), and the left-to-right 3-state $\mathbf A=\begin{pmatrix}A_{11}&A_{12}&0\\0&A_{22}&A_{23}\\0&0&1\end{pmatrix}$ (2.267) (p. 48).
- The $n$-step matrix is $A_{ij}(n)\triangleq p(X_{t+n}=j|X_t=i)$ (2.268), with $\mathbf A(1)=\mathbf A$. Chapman–Kolmogorov: $A_{ij}(m+n)=\sum_{k=1}^KA_{ik}(m)A_{kj}(n)$ (2.269), i.e. $\mathbf A(m+n)=\mathbf A(m)\mathbf A(n)$ (2.270). Hence $\mathbf A(n)=\mathbf A\,\mathbf A(n-1)=\dots=\mathbf A^n$ (2.271), so multi-step simulation is "powering up" the matrix (p. 48).
- *Higher order (2.6.1.3).* An order-$n$ model: $p(\boldsymbol x_{1:T})=p(\boldsymbol x_{1:n})\prod_{t=n+1}^Tp(\boldsymbol x_t|\boldsymbol x_{t-n:t-1})$ (2.272). $n=1$ is a bigram model, $n=2$ trigram, in general an $n$-gram model (p. 49).
- Any higher-order model converts to first order by augmenting the state. For $n=2$, let $\tilde{\boldsymbol x}_t=(\boldsymbol x_{t-1},\boldsymbol x_t)$; then $p(\tilde{\boldsymbol x}_{1:T})=p(\tilde{\boldsymbol x}_2)\prod_{t=3}^Tp(\tilde{\boldsymbol x}_t|\tilde{\boldsymbol x}_{t-1})=p(\boldsymbol x_1,\boldsymbol x_2)\prod_{t=3}^Tp(\boldsymbol x_t|\boldsymbol x_{t-1},\boldsymbol x_{t-2})$ (2.273). The rest of the section treats first-order models only (p. 49).

**2.6.2 Application: language modeling.** A language model generates or scores word sequences. A finite-state Markov LM with memory $m=n-1$ is an $n$-gram model (p. 49). Fig. 2.16 shows text from a 10-gram character model trained on the King James Bible, given the prefix "christians" (p. 49). Most LMs now use recurrent nets with unbounded memory, but simple $n$-gram models can still do well with enough data (p. 49). Uses include priors for spelling correction, speech recognition, and conditional generation (p. 49).

**2.6.3 Parameter estimation.**
- *MLE (2.6.3.1).* For parameters $\boldsymbol\theta=(\boldsymbol\pi,\mathbf A)$:
$$p(\boldsymbol x_{1:T}|\boldsymbol\theta)=\pi(x_1)A(x_1,x_2)\cdots A(x_{T-1},x_T)=\prod_{j=1}^K\pi_j^{\mathbb I(x_1=j)}\prod_{t=2}^T\prod_{j=1}^K\prod_{k=1}^KA_{jk}^{\mathbb I(x_t=k,x_{t-1}=j)}\tag{2.274–2.275}$$
For $N$ sequences $\boldsymbol x_i=(x_{i1},\dots,x_{i,T_i})$:
$$\log p(\mathcal D|\boldsymbol\theta)=\sum_i\log p(\boldsymbol x_i|\boldsymbol\theta)=\sum_jN_j^1\log\pi_j+\sum_j\sum_kN_{jk}\log A_{jk}\tag{2.276}$$
with counts $N_j^1\triangleq\sum_i\mathbb I(x_{i1}=j)$, $N_{jk}\triangleq\sum_i\sum_{t=1}^{T_i-1}\mathbb I(x_{i,t}=j,x_{i,t+1}=k)$, $N_j=\sum_kN_{jk}$ (2.277) (p. 50).
- With Lagrange multipliers for the sum-to-one constraints, the MLE is the normalized counts: $\hat\pi_j=N_j^1/\sum_{j'}N^1_{j'}$, $\hat A_{jk}=N_{jk}/N_j$ (2.278). The author's derivation is cited elsewhere, not given here. Often $N_j^1$ is replaced by $N_j$ so one sequence suffices (p. 50).
- $N_j$ are unigram statistics and $N_{jk}$ bigram statistics. Fig. 2.17 shows character bigram counts from *The Time Machine* (p. 51).
- *Sparse data (2.6.3.2).* For large $n$, contexts number $K^{n-1}$ and many $N_{jk}$ are 0, which causes overfitting. With $K\sim50{,}000$ words, a bigram model has about 2.5 billion free parameters. Predicting an unseen string as impossible would be a severe overfit (footnote 9: Chomsky's "colourless green ideas sleep furiously"). Brute force is to gather lots of data, e.g. Google's $n$-gram models ($n=1:5$) from a trillion words; the author calls this unsatisfying because humans learn from much less (p. 51).
- *MAP (2.6.3.3).* With a uniform Dirichlet prior $\mathbf A_{j:}\sim\mathrm{Dir}(\alpha\mathbf 1)$, the estimate is $\hat A_{jk}=\frac{N_{jk}+\alpha}{N_j+K\alpha}$ (2.279) (p. 51). If $\alpha=1$ this is add-one smoothing. Its weakness is that it treats all $n$-grams as equally likely; the author points to a more sophisticated approach based on hierarchical Bayes (Section 3.7.3) (p. 51).

**2.6.4 Stationary distribution.**
*2.6.4.1 Definition.* Let $\pi_t(j)=p(X_t=j)$ and let $\boldsymbol\pi$ be a row vector. Then $\pi_1(j)=\sum_i\pi_0(i)A_{ij}$ (2.280), i.e. $\boldsymbol\pi_1=\boldsymbol\pi_0\mathbf A$. If $\boldsymbol\pi=\boldsymbol\pi\mathbf A$, the chain has reached its stationary (invariant, equilibrium) distribution, and "Once we enter the stationary distribution, we will never leave" (p. 52). For Fig. 2.18(a), writing $\boldsymbol\pi=\boldsymbol\pi\mathbf A$ out gives (2.281) and so $\pi_1(A_{12}+A_{13})=\pi_2A_{21}+\pi_3A_{31}$. In general
$$\pi_i\sum_{j\ne i}A_{ij}=\sum_{j\ne i}\pi_jA_{ji}\tag{2.282}$$
These are the global balance equations. Solve them with $\sum_j\pi_j=1$ (p. 52).

*2.6.4.2 Computing it.*
- Solve $\mathbf A^{\mathsf T}\boldsymbol v=\boldsymbol v$ and set $\boldsymbol\pi=\boldsymbol v^{\mathsf T}$. An eigenvector for eigenvalue 1 exists because $\mathbf A\mathbf 1=\mathbf 1$ and $\mathbf A$, $\mathbf A^{\mathsf T}$ share eigenvalues. Normalize $\boldsymbol v$ to sum to one (pp. 52–53).
- Eigenvectors are only guaranteed real if all $A_{ij}>0$ (p. 53).
- A more general method handles zeros and ones. There are $K$ constraints from $\boldsymbol\pi(\mathbf I-\mathbf A)=\mathbf 0$ and one from $\boldsymbol\pi\mathbf 1=1$. Solve $\boldsymbol\pi\mathbf M=\boldsymbol r$ with $\mathbf M=[\mathbf I-\mathbf A,\mathbf 1]$ ($K\times(K+1)$) and $\boldsymbol r=[0,\dots,0,1]$ ($1\times(K+1)$). This is overconstrained, so drop the last column of $\mathbf I-\mathbf A$ and the last 0 of $\boldsymbol r$ (2.283) (p. 53).
- For Fig. 2.18(a) the result is $\boldsymbol\pi=[0.4,0.4,0.2]$, and $\boldsymbol\pi=\boldsymbol\pi\mathbf A$ holds (p. 53).

*2.6.4.3 When does one exist?*
- Fig. 2.18(b), with state 4 absorbing: $(0,0,0,1)$ and $(0.5,0.5,0,0)$ are both stationary. Starting from state 3, one ends in either with equal probability. The graph has two disjoint components (p. 53).
- A necessary condition for a unique stationary distribution is that any state can reach any other. Such a chain is irreducible (p. 53).
- Fig. 2.15(a) is irreducible if $\alpha,\beta>0$. With $\alpha=\beta=0.9$, $\boldsymbol\pi=(0.5,0.5)$. With $\alpha=\beta=1$ the chain alternates and the long-term distribution depends on the start (p. 53).
- A chain has a limiting distribution if $\pi_j=\lim_{n\to\infty}A^n_{ij}$ exists and is independent of the start $i$, for all $j$. Then $p(X_t=j)=\sum_ip(X_0=i)A_{ij}(t)\to\pi_j$ (2.284) (p. 53).
- The period of state $i$ is $d(i)\triangleq\gcd\{t:A_{ii}(t)>0\}$. State $i$ is aperiodic if $d(i)=1$. A self-loop is sufficient but not necessary. A chain is aperiodic if all states are. In Fig. 2.18(a), $d(1)=d(2)=d(3)=1$ (pp. 53–54).
- **Theorem 2.6.1:** every irreducible, aperiodic finite-state chain has a limiting distribution, equal to its unique stationary distribution $\boldsymbol\pi$ (p. 54).
- A regular chain has $A^n_{ij}>0$ for some $n$ and all $i,j$. Every regular finite chain has a unique stationary distribution. Irreducibility plus a self-transition in every state is sufficient for regularity (p. 54).
- For infinite state spaces (stated without proof), one also needs every state to be recurrent (return with probability 1). A non-recurrent state is transient; state 3 in Fig. 2.18(b) is transient. Finite irreducible chains are recurrent (p. 54).
- Random walk on the integers with $A_{i,i+1}=p$, $A_{i,i-1}=1-p$, start at 0. If $p\ne0.5$ the chain is not recurrent, although irreducible. If $p=0.5$ it is recurrent, but the expected return time is infinite, which prevents a stationary distribution (p. 54).
- A state is non-null recurrent if its expected return time is finite. A state is ergodic if aperiodic, recurrent and non-null, and a chain is ergodic if all its states are.
- **Theorem 2.6.2:** every irreducible, ergodic chain has a limiting distribution equal to its unique stationary distribution. This generalizes Theorem 2.6.1 (p. 54).

*Intuition note:* Irreducibility removes dependence on separate "islands", and aperiodicity removes forced cycling. With both (and, for infinite spaces, finite return times), the start state is forgotten.

*2.6.4.4 Detailed balance.* The chain is time reversible if some $\boldsymbol\pi$ satisfies $\pi_iA_{ij}=\pi_jA_{ji}$ (2.285). **Theorem 2.6.3:** if the chain is regular and satisfies detailed balance wrt $\boldsymbol\pi$, then $\boldsymbol\pi$ is a stationary distribution. Proof: $\sum_i\pi_iA_{ij}=\sum_i\pi_jA_{ji}=\pi_j\sum_iA_{ji}=\pi_j$ (2.286) (p. 55). The condition is sufficient but not necessary; Fig. 2.18(a) has a stationary distribution without detailed balance (p. 55).

### 2.7 Divergence measures between distributions
- A divergence $D(P,Q)$ is not required to be symmetric. A two-sample test asks whether samples from $P$ and $Q$ come from the same distribution, by comparing $D$ to a threshold (Fig. 2.19). A goodness-of-fit test compares an empirical $P$ with a model $Q$ (p. 55).
- Two approaches: difference $P-Q$, or ratio $P/Q$ (p. 55).

**2.7.1 f-divergence.** With density ratio $r=p/q$ and convex $f:\mathbb R_+\to\mathbb R$ with $f(1)=0$:
$$D_f(p\|q)=\int q(\boldsymbol x)f\!\left(\frac{p(\boldsymbol x)}{q(\boldsymbol x)}\right)d\boldsymbol x\tag{2.287}$$
By Jensen's inequality $D_f\ge0$, and $D_f(p\|p)=0$ (p. 55). Special cases:
- *KL (2.7.1.1):* $f(r)=r\log r$ gives $D_{\mathrm{KL}}(p\|q)=\int p\log\frac pq\,d\boldsymbol x$ (2.288) (p. 56).
- *Alpha (2.7.1.2):* $f(x)=\frac4{1-\alpha^2}(1-x^{\frac{1+\alpha}2})$ gives
$$D^A_\alpha(p\|q)\triangleq\frac4{1-\alpha^2}\left(1-\int p^{(1+\alpha)/2}q^{(1-\alpha)/2}d\boldsymbol x\right),\ \alpha\ne\pm1\tag{2.289}$$
Minka's version is $D^M_\alpha=\frac1{\alpha(1-\alpha)}\left(1-\int p^\alpha q^{1-\alpha}d\boldsymbol x\right)$ (2.290). Conversion: $D^A_{\alpha'}=D^M_\alpha$ with $\alpha'=2\alpha-1$. The author uses Minka's (p. 56).
- Fig. 2.20 (Gaussian $q$ fitted to a two-Gaussian mixture $p$): as $\alpha\to-\infty$, $q$ prefers to match one mode of $p$; as $\alpha\to\infty$, it prefers to cover all of $p$. As $\alpha\to0$ the divergence tends to $D_{\mathrm{KL}}(q\|p)$, as $\alpha\to1$ to $D_{\mathrm{KL}}(p\|q)$, and at $\alpha=0.5$ it equals the Hellinger distance (p. 57).
- *Hellinger (2.7.1.3):* $D_H^2(p\|q)\triangleq\frac12\int\left(p^{1/2}-q^{1/2}\right)^2d\boldsymbol x=1-\int\sqrt{p\,q}\,d\boldsymbol x$ (2.291). It is a valid metric (symmetric, nonnegative, triangle inequality). It equals, up to constants, the f-divergence with $f(r)=(\sqrt r-1)^2$, since $\int q\left(\frac{p^{1/2}}{q^{1/2}}-1\right)^2=\int q\left(\frac{p^{1/2}-q^{1/2}}{q^{1/2}}\right)^2=\int(p^{1/2}-q^{1/2})^2$ (2.292) (p. 57).
- *Chi-squared (2.7.1.4):* $\chi^2(p,q)\triangleq\frac12\int\frac{(q-p)^2}{q}d\boldsymbol x$ (2.293). It equals, up to constants, the f-divergence with $f(r)=(r-1)^2$, since $\int q\left(\frac pq-1\right)^2=\int q\left(\frac{p-q}q\right)^2=\int\frac1q(p-q)^2$ (2.294) (p. 57).

**2.7.2 Integral probability metrics (IPMs).** Using $P-Q$:
$$D_{\mathcal F}(P,Q)\triangleq\sup_{f\in\mathcal F}\left|\mathbb E_{p(\boldsymbol x)}[f(\boldsymbol x)]-\mathbb E_{q(\boldsymbol x')}[f(\boldsymbol x')]\right|\tag{2.295}$$
$\mathcal F$ is a class of "smooth" functions. The maximizing $f$ is the witness function (Fig. 2.21) (p. 57). Choosing $\mathcal F$ as an RKHS (function space defined by a positive definite kernel) gives MMD. Choosing bounded Lipschitz functions, $\|f\|_L=\sup_{x\ne x'}\frac{|f(x)-f(x')|}{\|x-x'\|}\le1$ (2.296), gives the Wasserstein-1 distance
$$W_1(P,Q)\triangleq\sup_{\|f\|_L\le1}\left|\mathbb E_{p}[f(\boldsymbol x)]-\mathbb E_{q}[f(\boldsymbol x')]\right|\tag{2.297}$$
(pp. 57–58).

**2.7.3 Maximum mean discrepancy.** MMD, from samples, uses positive definite kernels and handles high-dimensional inputs. It is used for two-sample tests and for training implicit generative models (p. 58).
- *As IPM:* $\mathrm{MMD}(P,Q;\mathcal F)=\sup_{f\in\mathcal F:\|f\|\le1}\left[\mathbb E_p f(\boldsymbol x)-\mathbb E_qf(\boldsymbol x')\right]$ (2.298), with $f(\boldsymbol x)=\langle f,\boldsymbol\phi(\boldsymbol x)\rangle_{\mathcal F}=\sum_{l=1}^\infty f_l\phi_l(\boldsymbol x)$ (2.299) and $\|f\|^2_{\mathcal F}=\sum_lf_l^2\le1$ (p. 58).
- By linearity of expectation, $\mathbb E_p[f]=\langle f,\mathbb E_p[\boldsymbol\phi(\boldsymbol x)]\rangle=\langle f,\boldsymbol\mu_P\rangle$ (2.300). $\boldsymbol\mu_P$ is the kernel mean embedding. Hence $\mathrm{MMD}=\sup_{\|f\|\le1}\langle f,\boldsymbol\mu_P-\boldsymbol\mu_Q\rangle=\|\boldsymbol\mu_P-\boldsymbol\mu_Q\|$ (2.301), because the maximizing unit vector is parallel to the difference in feature means (pp. 58–59).
- With $\boldsymbol\phi(x)=[x,x^2]$, MMD compares the first two moments. A Gaussian kernel is equivalent to infinitely large feature vectors, so effectively all moments. MMD $=0$ iff $P=Q$, provided the kernel is non-degenerate (p. 59).
- *Kernel trick (2.7.3.2).* For samples $\mathcal X=\{\boldsymbol x_n\}_{n=1}^N$ and $\mathcal X'=\{\boldsymbol x'_m\}_{m=1}^M$, with empirical embeddings $\boldsymbol\mu_P=\frac1N\sum\boldsymbol\phi(\boldsymbol x_n)$ and $\boldsymbol\mu_Q=\frac1M\sum\boldsymbol\phi(\boldsymbol x'_m)$:
$$\mathrm{MMD}^2(\mathcal X,\mathcal X')=\Big\|\tfrac1N\sum_n\boldsymbol\phi(\boldsymbol x_n)-\tfrac1M\sum_m\boldsymbol\phi(\boldsymbol x'_m)\Big\|^2\tag{2.302}$$
$$=\tfrac1{N^2}\sum_{n,n'}\boldsymbol\phi(\boldsymbol x_n)^{\mathsf T}\boldsymbol\phi(\boldsymbol x_{n'})-\tfrac2{NM}\sum_{n,m}\boldsymbol\phi(\boldsymbol x_n)^{\mathsf T}\boldsymbol\phi(\boldsymbol x'_m)+\tfrac1{M^2}\sum_{m,m'}\boldsymbol\phi(\boldsymbol x'_{m'})^{\mathsf T}\boldsymbol\phi(\boldsymbol x'_m)\tag{2.303}$$
Replacing each inner product by $\mathcal K(\cdot,\cdot)$ gives (2.304) (p. 59).
- *Linear time (2.7.3.3).* MMD costs $O(N^2)$. The UME statistic costs $O(N)$. The idea: evaluating $\mathrm{witness}^2(\boldsymbol v)=(\boldsymbol\mu_Q(\boldsymbol v)-\boldsymbol\mu_P(\boldsymbol v))^2$ (2.305) at a set of test locations $\boldsymbol v_1,\dots,\boldsymbol v_J$ is enough to detect a difference. So $\mathrm{UME}^2(P,Q)=\frac1J\sum_{j=1}^J[\boldsymbol\mu_P(\boldsymbol v_j)-\boldsymbol\mu_Q(\boldsymbol v_j)]^2$ (2.306), with $\boldsymbol\mu_P(\boldsymbol v)=\mathbb E_p[\mathcal K(\boldsymbol x,\boldsymbol v)]$. The normalized version, NME, can be maximized over the $\boldsymbol v_j$ to raise test power, giving an interpretable test (pp. 59–60).
- *Kernel choice (2.7.3.4).* Effectiveness crucially depends on the kernel. For the Gaussian kernel $\mathcal K_\sigma=\exp(-\frac1{2\sigma^2}\|\boldsymbol x-\boldsymbol x'\|^2)$, Fig. 2.22 shows the effect of decreasing $\sigma$ on the witness function. MMD is differentiable wrt kernel parameters, so $\sigma^2$ can be chosen to maximize test power. For images, features $\boldsymbol h$ from a pre-trained CNN layer give $\mathcal K_\sigma(\boldsymbol h(\boldsymbol x),\boldsymbol h(\boldsymbol x'))$, the kernel inception distance (p. 60).

**2.7.4 Total variation.** $D_{\mathrm{TV}}(p,q)\triangleq\frac12\|p-q\|_1=\frac12\int|p-q|\,d\boldsymbol x$ (2.307). It is the f-divergence with $f(r)=|r-1|/2$, because $\frac12\int q\left|\frac pq-1\right|=\frac12\int q\left|\frac{p-q}q\right|=\frac12\int|p-q|$ (2.308). It is also an IPM, and is the only divergence that is both an IPM and an f-divergence (Fig. 2.23) (p. 61).

**2.7.5 Density ratio estimation (DRE) with a classifier.** Label $y=1$ for points from $P$ and $y=0$ for $Q$; $p(y=1)=\pi$. By Bayes' rule:
$$\frac{P(\boldsymbol x)}{Q(\boldsymbol x)}=\frac{p(\boldsymbol x|y{=}1)}{p(\boldsymbol x|y{=}0)}=\frac{p(y{=}1|\boldsymbol x)p(\boldsymbol x)}{p(y{=}1)}\Big/\frac{p(y{=}0|\boldsymbol x)p(\boldsymbol x)}{p(y{=}0)}=\frac{p(y{=}1|\boldsymbol x)}{p(y{=}0|\boldsymbol x)}\frac{1-\pi}{\pi}\tag{2.309–2.310}$$
If $\pi=0.5$, fit a classifier $h(\boldsymbol x)=p(y=1|\boldsymbol x)$ and set $r=h/(1-h)$ (the DRE trick) (p. 61). With log-loss, the risk is
$$R(h)=\mathbb E_{p(\boldsymbol x|y)p(y)}[-y\log h-(1-y)\log(1-h)]=\pi\,\mathbb E_P[-\log h]+(1-\pi)\mathbb E_Q[-\log(1-h)]\tag{2.311–2.312}$$
(p. 62).

Let $R^\ell_{h^*}=\inf_{h\in\mathcal F}R(h)$ be the minimum risk for loss $\ell$. [NWJ09] show that for every f-divergence some loss $\ell$ gives $-D_f(P,Q)=R^\ell_{h^*}$. With $\tilde y\in\{-1,1\}$, the author's examples are (p. 62):
- total variation ↔ hinge loss $\max(0,1-\tilde yh)$;
- Hellinger ↔ exponential loss $\exp(-\tilde yh)$;
- $\chi^2$ ↔ logistic loss $\log(1+\exp(-\tilde yh))$.

IPM link: take $\ell(\tilde y,h)=-2\tilde yh$ and $p(\tilde y=\pm1)=0.5$. Then
$$R_{h^*}=\inf_h\int\ell(\tilde y,h(\boldsymbol x))p(\boldsymbol x|\tilde y)p(\tilde y)\,d\boldsymbol x\,d\tilde y\tag{2.313}$$
$$=\inf_h0.5\!\int\!\ell(1,h)p(\boldsymbol x|\tilde y{=}1)d\boldsymbol x+0.5\!\int\!\ell(-1,h)p(\boldsymbol x|\tilde y{=}{-}1)d\boldsymbol x\tag{2.314}$$
$$=\inf_h\int h(\boldsymbol x)Q(\boldsymbol x)d\boldsymbol x-\int h(\boldsymbol x)P(\boldsymbol x)d\boldsymbol x\tag{2.315}$$
$$=\sup_h-\int hQ\,d\boldsymbol x+\int hP\,d\boldsymbol x\tag{2.316}$$
The author says this matches (2.295), so the classifier plays the role of the witness function (p. 62). (Footnote 11: if $Q$ is also optimized adversarially, one recovers a GAN; here $Q$ is known.)

*Intuition note:* A classifier that separates $P$ from $Q$ works by picking up where the two densities differ. With equal class priors its odds $h/(1-h)$ give the density ratio, and for suitable losses its minimum risk is linked to an f-divergence or to the IPM form.

## Toy example (ours, not from the text)
Two-state chain $\mathbf A=\begin{pmatrix}0.9&0.1\\0.5&0.5\end{pmatrix}$ (rows sum to 1).
- $\mathbf A(2)=\mathbf A\mathbf A$. Row 1: $[0.9\cdot0.9+0.1\cdot0.5,\ 0.9\cdot0.1+0.1\cdot0.5]=[0.86,0.14]$. Row 2: $[0.5\cdot0.9+0.5\cdot0.5,\ 0.5\cdot0.1+0.5\cdot0.5]=[0.70,0.30]$.
- $\mathbf A(3)=\mathbf A(2)\mathbf A$. Row 1: $[0.86\cdot0.9+0.14\cdot0.5,\ 0.86\cdot0.1+0.14\cdot0.5]=[0.844,0.156]$. Row 2: $[0.7\cdot0.9+0.3\cdot0.5,\ 0.7\cdot0.1+0.3\cdot0.5]=[0.78,0.22]$. The rows are moving together.
- Stationary $\boldsymbol\pi$: $\pi_1=0.9\pi_1+0.5\pi_2\Rightarrow0.1\pi_1=0.5\pi_2$, so $\pi_1=5\pi_2$. With $\pi_1+\pi_2=1$: $\boldsymbol\pi=(5/6,1/6)\approx(0.833,0.167)$.
- Detailed balance (2.285): $\pi_1A_{12}=\frac56\cdot0.1=\frac1{12}$ and $\pi_2A_{21}=\frac16\cdot0.5=\frac1{12}$ ✓. All entries are positive, so the chain is regular and Theorem 2.6.3 applies.
- Total variation (2.307) between row 1 of $\mathbf A(3)$ and $\boldsymbol\pi$: $\frac12(|0.844-0.8333|+|0.156-0.1667|)\approx0.0107$. This is small, consistent with convergence.
- MLE from the sequence 1,1,1,2,1,1,2,2,1,1: the nine transitions give $N_{11}=4$, $N_{12}=2$, $N_{21}=2$, $N_{22}=1$, so $N_1=6$, $N_2=3$ and $\hat{\mathbf A}=\begin{pmatrix}4/6&2/6\\2/3&1/3\end{pmatrix}$ (2.278). Add-one smoothing (2.279, $K=2$) gives $\begin{pmatrix}5/8&3/8\\3/5&2/5\end{pmatrix}$.

## Concepts
- [[principle-of-indifference-maximum-entropy]] — max-entropy distribution with feature constraints is exponential family; moments $x,x^2$ give the Gaussian (p. 44)
- [[change-of-variables]] (new) — $p_y(y)=p_x(f^{-1}(y))|\det J_{f^{-1}}(y)|$ for bijections (p. 44)
- [[monte-carlo-integration]] — here: approximate $p_y$ by pushing samples through $f$ and using an empirical pdf (p. 45)
- [[probability-integral-transform]] (new) — $P_X(X)\sim\mathrm{Unif}(0,1)$; basis of KS test and inverse-cdf sampling (p. 45)
- [[kolmogorov-smirnov-test]] (new) — $D_n=\max_x|P_n(x)-P(x)|$ compares empirical and theoretical cdfs (p. 46)
- [[markov-chain]] (new) — sequence with $p(x_t|x_{1:t-1})=p(x_t|x_{t-1})$; transition matrix $\mathbf A$, $n$-step matrix $\mathbf A^n$ (pp. 46–48)
- [[n-gram-model]] (new) — Markov model of order $n-1$ (memory $m=n-1$ in 2.6.2), or order $n$ as named in 2.6.1.3 (pp. 49, 51)
- [[add-one-smoothing]] (new) — uniform Dirichlet prior with $\alpha=1$ on transition rows, to avoid zero counts (p. 51)
- [[stationary-distribution]] (new) — $\boldsymbol\pi=\boldsymbol\pi\mathbf A$; the long-run distribution when it exists (p. 52)
- [[ergodicity-irreducibility-aperiodicity]] (new) — conditions guaranteeing a unique limiting stationary distribution (pp. 53–54)
- [[detailed-balance]] (new) — $\pi_iA_{ij}=\pi_jA_{ji}$; sufficient, not necessary, for stationarity of regular chains (p. 55)
- [[markov-chain-monte-carlo-mcmc]] — only mentioned as an application of stationary distributions (p. 51)
- [[f-divergence]] (new) — $\int qf(p/q)$ with convex $f$, $f(1)=0$ (p. 55)
- [[kl-divergence]] — the f-divergence with $f(r)=r\log r$ (p. 56)
- [[integral-probability-metric]] (new) — $\sup_f|\mathbb E_Pf-\mathbb E_Qf|$; maximizer is the witness function (p. 57)
- [[maximum-mean-discrepancy]] (new) — IPM over the RKHS unit ball; equals $\|\boldsymbol\mu_P-\boldsymbol\mu_Q\|$ (pp. 58–59)
- [[total-variation-distance]] (new) — $\frac12\int|p-q|$; both an IPM and an f-divergence (p. 61)
- [[density-ratio-estimation]] (new) — estimate $P/Q$ from a classifier's odds (p. 61)
- [[bayes-theorem]] — used to turn class-conditionals into the density ratio (p. 61)

## Canonical instances
- [[logistic-transform-of-gaussian]] — $x\sim\mathcal N(6,1)$, $y=1/(1+e^{-x+5})$; the mode does not map to the mode (p. 45)
- [[bible-character-ngram]] — 10-gram character model on the King James Bible generating text (p. 49)
- [[time-machine-bigram-counts]] — character bigram counts and row-normalized version (p. 50)
- [[three-state-chain-fig-2-18a]] — stationary $\boldsymbol\pi=[0.4,0.4,0.2]$; has stationarity without detailed balance (pp. 53, 55)
- [[reducible-four-state-chain-fig-2-18b]] — absorbing state, two stationary distributions, transient state 3 (pp. 53–54)
- [[integer-random-walk]] — irreducible but non-recurrent for $p\ne0.5$; recurrent but no stationary distribution at $p=0.5$ (p. 54)
- [[kernel-inception-distance]] — MMD on CNN features (p. 60)

## Bridges (candidates)
- [same-math] stationary distribution of a chain ↔ Bayesian: MCMC — the target posterior is made the stationary distribution of a chain (the unit only says MCMC is an application, p. 51).
- [same-math] uniform Dirichlet prior on transition rows (add-$\alpha$) ↔ Conjugate prior — counts plus pseudo-counts $\alpha$ (Dirichlet–categorical updating).
- [same-math] DRE trick via Bayes' rule ↔ Bayes' theorem — posterior odds times prior odds correction gives the likelihood ratio.
- [structural-analogy] alpha-divergence mode-matching vs mode-covering ↔ Variational inference — direction of KL decides whether $q$ hugs one mode or spreads (Fig. 2.20).
- [structural-analogy] inverse-cdf sampling via PIT ↔ Monte Carlo integration — turning uniform draws into draws from a target.
- [metaphor] classifier as witness function ↔ adversarial training — footnote 11 notes GANs arise when $Q$ is also optimized.

## Questions this raises
- When $\pi_i A_{ij}=\pi_jA_{ji}$ fails, how else can one verify a stationary distribution, and how fast does the chain approach it?
- Which f-divergence (or IPM) is best for a given two-sample or goodness-of-fit task, and why do they differ in sensitivity to tails and modes?
- How should the kernel in MMD be chosen without leaking power in high dimensions?
- Beyond add-one smoothing, how does a hierarchical Bayes treatment (Section 3.7.3) make $n$-gram estimates non-uniform?

## Reading notes
- This part starts mid-section 2.4 (printed p. 44, the end of the maximum-entropy discussion, from eq. 2.256) and ends at the end of 2.7.5 (printed p. 62, eq. 2.316). The chapter is split at a section boundary.
- Page offset: printed = pdf − 34. Page footers alternate between the author/licence line and "Online version. December 10, 2025".
- Text layer and images agree on all equations I checked.
- Misprints and inconsistencies found in the images:
  - p. 44: "disribution".
  - p. 55 (2.286): the proof ends with $\boldsymbol\pi=\mathbf A\boldsymbol\pi$. The row-vector convention of p. 52 and the sum $\sum_i\pi_iA_{ij}=\pi_j$ give $\boldsymbol\pi=\boldsymbol\pi\mathbf A$.
  - p. 62 (2.316): as printed, "$\sup$" equals the negative of the "$\inf$" in (2.315). Added step: $\inf_hX=-\sup_h(-X)$. So a minus sign (and an absolute value, as in 2.295) is implicit in the author's "matches".
  - p. 49: in 2.6.2 the labels (unigram for $m=1$, bigram for $m=2$) are off by one against $m=n-1$ and against 2.6.1.3. The $n$-gram Concepts line lists both usages.
  - p. 51: eq. (2.279) is reproduced as printed. The unit gives no derivation, and I did not verify it.
  - p. 62: the loss–divergence pairings are reported as the author states them. I did not verify them from these pages.
  - p. 57: the claim that $\alpha=0.5$ "equals" the Hellinger distance is reported as stated. Constant factors are not discussed.
- Proofs the author omits or cites elsewhere (MLE via Lagrange multipliers, Theorems 2.6.1 and 2.6.2, the TV claim, the NWJ result) are not reconstructed here.

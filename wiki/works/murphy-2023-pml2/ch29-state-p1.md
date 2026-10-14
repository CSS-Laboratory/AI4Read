---
id: murphy-2023-pml2/ch29-state-p1
work: murphy-2023-pml2
unit: "29 State-space models (part 1/3): §29.1 Introduction, §29.2 HMMs, §29.3 HMM applications, §29.4 HMM parameter learning (up to §29.4.4.1)"
pages: 979–996
fields: [bayesian]
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
# State-space models (part 1/3): HMMs, their uses, and how to fit them

## L0 — One line
A hidden Markov model is a state-space model with a discrete hidden state, and its parameters can be learned by EM (expectation-maximisation, called Baum-Welch for HMMs), by SGD (stochastic gradient descent) on the forward-algorithm likelihood, by spectral methods, or by Bayesian posterior sampling.

## L1 — The gist (≤ 120 words)
A state-space model has a hidden Markov state that generates the observations. The goal is to infer the state, and sometimes to forecast. This part defines the general model, then focuses on HMMs (discrete hidden state). It lists observation models: categorical, Gaussian, GMM (Gaussian mixture model), autoregressive and neural. It shows three applications: time-series segmentation, protein alignment and spelling correction. It then covers parameter learning: EM (expectation-maximisation) with expected counts, SGD (stochastic gradient descent), spectral methods, and Bayesian inference with blocked Gibbs sampling. The unit matters because HMMs let us infer hidden states from observations, and this part shows how to fit their parameters from data.

**Prerequisites:** conditional independence and graphical models; Markov chains; EM and the expected complete-data log likelihood; the forwards-backwards algorithm (Murphy Ch. 9, assumed, not rederived here); Gaussian, Poisson and Dirichlet distributions.

## L2 — Key ideas (5–10 bullets)
- An SSM is a Markov hidden state plus observations. It is more common to assume the observations are conditionally independent given the state, which gives the factorised joint (29.6) (p. 979).
- An HMM has $z_t \in \{1,\dots,K\}$, an initial distribution $\pi$ and a row-stochastic transition matrix $A$ (each row sums to one). The observation model can be categorical, Gaussian, GMM, autoregressive or neural (pp. 980–984).
- The scaled likelihood trick turns a discriminative classifier $p(z_t\mid y_t)$ into an HMM likelihood by dividing by $p(z_t)$ (p. 984).
- HMM applications: Poisson segmentation with $K$ chosen by an approximate marginal likelihood, profile HMMs for protein alignment, and spelling correction as noisy-channel decoding (pp. 984–990).
- Baum-Welch (EM) alternates forwards-backwards marginals with normalised expected counts. It converges to a local optimum, so initialisation matters (pp. 990–993).
- SGD on $\log p(y_{1:T}\mid\theta)=\sum_t\log Z_t$ is an alternative to EM, which is a batch algorithm that does not scale well to many sequences. It needs constraint handling or reparameterisation (p. 994).
- Spectral methods avoid the non-convex likelihood by working with predictive distributions in visible space (pp. 994–995).
- Bayesian HMMs use blocked Gibbs sampling or collapsed inference. With conjugate priors the parameter step is easy (pp. 995–996).

## L3 — Walkthrough

### 29.1 Introduction (pp. 979–980)
An SSM is a partially observed Markov model. The hidden state $z_t$ follows a Markov process and generates observations $y_t$. The main goal is to infer the hidden states. We may also want to predict future observations (p. 979).

General form, with inputs $u_t$, process noise $q_t$ and observation noise $r_t$ (p. 979):
$$z_t = f(z_{t-1}, u_t, q_t)\tag{29.1}$$
$$y_t = h(z_t, u_t, y_{1:t-1}, r_t)\tag{29.2}$$
Here $z_t\in\mathbb R^{N_z}$, $u_t\in\mathbb R^{N_u}$ and $y_t\in\mathbb R^{N_y}$. $f$ is the transition function and $h$ the observation function. As a probabilistic model (p. 979):
$$p(z_t\mid z_{t-1},u_t)=p(z_t\mid f(z_{t-1},u_t)),\qquad p(y_t\mid z_t,u_t,y_{1:t-1})=p(y_t\mid h(z_t,u_t,y_{1:t-1}))\tag{29.3, 29.4}$$
$$p(y_{1:T},z_{1:T}\mid u_{1:T})=\Big[p(z_1\mid u_1)\prod_{t=2}^T p(z_t\mid z_{t-1},u_t)\Big]\Big[\prod_{t=1}^T p(y_t\mid z_t,u_t,y_{1:t-1})\Big]\tag{29.5}$$
If $y_t$ depends on $z_t$ and $y_{t-1}$, the model is an *autoregressive SSM* (Fig. 29.1a). A sufficiently expressive $z_t$ can implicitly represent $y_{1:t-1}$. So it is more common to assume the observations are conditionally independent given the state (p. 979):
$$p(y_{1:T},z_{1:T}\mid u_{1:T})=\Big[p(z_1\mid u_1)\prod_{t=2}^T p(z_t\mid z_{t-1},u_t)\Big]\Big[\prod_{t=1}^T p(y_t\mid z_t,u_t)\Big]\tag{29.6}$$
With no inputs, this gives the unconditional generative model (Fig. 29.1b) (p. 980):
$$p(y_{1:T},z_{1:T})=\Big[p(z_1)\prod_{t=2}^T p(z_t\mid z_{t-1})\Big]\Big[\prod_{t=1}^T p(y_t\mid z_t)\Big]\tag{29.7}$$

*Intuition note:* The hidden state is a summary of the past. If it is rich enough, the observations do not need to talk to each other, only to the state. This is why (29.7) is a product of simple local terms.

### 29.2 Hidden Markov models (pp. 980–984)
An HMM is an SSM with discrete hidden states $z_t\in\{1,\dots,K\}$. Observations may be discrete, continuous or mixed (p. 980).

**29.2.1 Conditional independence.** The graph is Fig. 29.1(b). The hidden states are Markovian and the observations are iid given the hidden states (p. 980).

**29.2.2 State transition model.**
$$p(z_1=j)=\pi_j\tag{29.8}$$
$$p(z_t=j\mid z_{t-1}=i)=A_{ij}\tag{29.9}$$
Row $i$ of $A$ is the outgoing distribution from state $i$. $A$ is *row stochastic*, meaning each row sums to one (p. 981).

**29.2.3 Discrete likelihoods** (pp. 981–982).
- Single discrete observation: $p(y_t=k\mid z_t=j)=y_{jk}$ (29.10). This is the observation matrix, written $B_{jk}$ later (see Reading notes).
- $D$ discrete observations per step, factorial model: $p(y_t\mid z_t=j)=\prod_{d=1}^D \mathrm{Cat}(y_{td}\mid y_{d,j,:})$ (29.11).
- Binary case: $\prod_{d=1}^D \mathrm{Ber}(y_{td}\mid y_{d,j})$ (29.12).
- Fig. 29.2 shows samples from an HMM with 5 hidden states and 10 Bernoulli observables (p. 981).

**29.2.4 Gaussian likelihoods.** $p(y_t\mid z_t=j)=\mathcal N(y_t\mid\mu_j,\Sigma_j)$ (29.13) (p. 982).
- *Lily-pad picture:* each state emits from a 2d Gaussian ellipse, and a frog hops between pads. It stays on a pad for a while (same $z_t$) and then jumps (a transition). The observed points are droplets near the current pad. The HMM is thus like a Gaussian mixture model, but with temporal correlation between datapoints (p. 982).
- GMM-HMM: an $M$-component mixture per state, $p(y_t\mid z_t=j)=\sum_{k=1}^M w_{jk}\mathcal N(y_t\mid\mu_{jk},\Sigma_{jk})$ (29.14) (p. 982).

**29.2.5 Autoregressive likelihoods.** The standard HMM assumes conditional independence, which is often untrue in practice. We can add arcs $y_{t-1}\to y_t$ (Fig. 29.1a), giving an *auto-regressive HMM* (p. 982). For continuous data:
$$p(y_t\mid y_{t-1},z_t=j,\theta)=\mathcal N(y_t\mid E_j y_{t-1}+\mu_j,\Sigma_j)\tag{29.15}$$
This is linear regression whose parameters are chosen by the current state. In econometrics it is called a *regime switching Markov model* (p. 983). Order-$L$ extension (p. 983):
$$p(y_t\mid y_{t-L:t-1},z_t=j,\theta)=\mathcal N\Big(y_t\,\Big|\,\sum_{\ell=1}^L W_{j,\ell}y_{t-\ell}+\mu_j,\Sigma_j\Big)\tag{29.16}$$
The AR-HMM combines two Markov chains. The hidden chain captures long-range dependencies and the observed chain captures short-range ones. Since all visible nodes are observed, extra arcs between them only change the likelihood and do not complicate posterior inference (p. 983).

*2d example (Linderman)* (p. 983):
- There are 5 states with a left-to-right transition matrix. The last state returns to the first, so the chain cycles through the states.
- $y_t\in\mathbb R^2$. $E_j$ is a rotation matrix with a small angle of 7 degrees. The $\mu_j$ are points 72 degrees apart on a circle about the origin.
- If the model stays in state $j$ long enough, the observations converge to $y_{*,j}=E_j y_{*,j}+\mu_j$. Rearranging (added step): $(I-E_j)y_{*,j}=\mu_j$, so $y_{*,j}=(I-E_j)^{-1}\mu_j$ (p. 983).
- In the sampled trajectory (Fig. 29.5), the first observation is the yellow dot (state 2) at $(-0.8,0.5)$. It converges to $y_{*,2}=(-2.0,3.8)$. After a jump to state 3 it adds an offset $\mu_3$ to the last observation. It then converges to $y_{*,3}=(-4.3,-0.8)$ (p. 983).

**29.2.6 Neural network likelihoods.** For high-dimensional data such as images, one can use a normalizing flow per state as a class-conditional generative model. Discriminative classifiers are much easier to train. The likelihood per state can be rewritten (p. 984):
$$p(y_t\mid z_t=j)=\frac{p(z_t=j\mid y_t)\,p(y_t)}{p(z_t=j)}\propto\frac{p(z_t=j\mid y_t)}{p(z_t=j)}\tag{29.17}$$
$p(y_t)$ is dropped because it does not depend on $z_t$. $p(z_t=j\mid y_t)$ is the classifier output. $p(z_t=j)$ can be computed from the stationary distribution of the Markov chain, or empirically if the state sequence is known. This is the *scaled likelihood trick*. A hybrid CNN-HMM was used for digit sequences on street signs (p. 984).

*Intuition note:* Bayes' rule turns "state given data" into "data given state", up to a factor that does not depend on the state. So a classifier can stand in for a generative model inside the HMM.

### 29.3 HMMs: applications (pp. 984–990)

**29.3.1 Time series segmentation (pp. 984–986).** Aim: split a count series into $K$ regimes. Each regime $k$ has a Poisson observation model, $p(y_t\mid z_t=k)=\mathrm{Poi}(y_t\mid\lambda_k)$ (29.18).
- Prior and transitions, with $K=4$ and $p=0.95$ (29.19–29.20): $z_1\sim\mathrm{Cat}(1/4,1/4,1/4,1/4)$. Then $z_t\mid z_{t-1}$ equals $z_{t-1}$ with probability $p$ and otherwise goes to each other state with probability $\frac{1-p}{4-1}$ (p. 985).
- Estimation: MAP for $\lambda_{1:K}$ with a log-Normal(5,5) prior. The log rates are optimised by gradient descent, initialised at a random value centred on the log overall count mean (p. 986).
- Result: the 4 regimes were recovered, as generated. The true rates are $\lambda=(40,3,20,50)$ with changepoints at times $(10,30,35)$ (p. 986).
- Choosing $K$: fit $K=1{:}6$ (Fig. 29.7). For $K\ge3$ the fits are very similar, because several states map to one regime. Pick the $K$ with highest marginal likelihood, approximated by maximising over $\lambda$ (empirical Bayes) (p. 986):
$$p(y_{1:T}\mid K)\approx\max_\lambda\sum_z p(y_{1:T},z_{1:T}\mid\lambda,K)\tag{29.21}$$
The peak is at $K=3$ or $4$. It then declines, which the author attributes to the Bayesian Occam's razor effect (Fig. 29.8) (p. 986).

**29.3.2 Protein sequence alignment (pp. 986–988).** Goal: decide whether a test sequence $y_{1:T}$ belongs to a protein family and, if so, how it aligns to the family's canonical representation (p. 986).
- Start from aligned family sequences, from which a consensus sequence is built. This gives a *position-specific scoring matrix* (PSSM) $\theta_t(v)=p(y_t=v)$, estimated by counting (p. 986).
- Turn the PSSM into an HMM with 3 states per position: match $M$, insert $I$, delete $D$.
  - Match: $p(y_t=v\mid z_t=M)=\theta_t(v)$.
  - Insert: uniform, $p(y_t=v\mid z_t=I)=1/V$, with $V$ the vocabulary size.
  - Delete: $p(y_t=-\mid z_t=D)$, where "−" is a special padding symbol (pp. 986–987).
- Matches and deletions advance one consensus location. Insertions stay in place via an $I\to I$ self-transition (Fig. 29.9). This is the *profile HMM* (p. 987).
- The forwards algorithm gives $p(y_{1:T}\mid\theta)$ in $O(T)$ time. Family membership is tested by thresholding the log-odds $L(y)=\log p(y\mid\theta)/p(y\mid\mathcal M_0)$, with $\mathcal M_0$ a baseline such as the uniform distribution (p. 987).
- If the string matches, the Viterbi algorithm gives the alignment (Fig. 29.10). Without aligned sequences, Baum-Welch gives the MLE of $\theta$ from unaligned sequences (pp. 987–988).

**29.3.3 Spelling correction (pp. 988–990).** Goal: infer the words $z_{1:T}$ the user meant, given what was typed, $y_{1:T}$ (p. 988).

*29.3.3.1 Baseline.* The prior is a unigram language model, $p(z_{1:T})=\prod_t p(z_t)$, with word probabilities from normalised corpus counts. No Markov structure is used (p. 988). The observation model is a *noisy channel*: the message is corrupted by substitution, transposition, deletion or insertion errors. If $y$ differs from $z$ by $d$ such errors, their *edit distance* is $d$. With $\mathcal D(z,d)$ the set of words at edit distance $d$ from $z$ (the text writes $\mathcal D(y,d)$ in the definition and $\mathcal D(z,\cdot)$ in the formula):
$$p(y\mid z)=\begin{cases}p_1&y=z\\p_2&y\in\mathcal D(z,1)\\p_3&y\in\mathcal D(z,2)\\p_4&\text{otherwise}\end{cases},\qquad p_1>p_2>p_3>p_4\tag{29.22}$$
Combining likelihood and prior scores each candidate correction (Norvig's model). Flaw: smaller edit distance is not always more likely. For example, "reciet" is corrected to "recite" rather than "receipt". The fix is to learn the noise model from labelled $(z,y)$ pairs. Sources named: web-search query rewrites (as in Etsy search), manually collected data, or automatically generated misspellings (p. 988).

*29.3.3.2 HMM model.* Context helps, for example "advice" versus "advise" depends on noun versus verb. Replace the unigram prior by a first-order language model, $p(z_{1:T})=\prod_t p(z_t\mid z_{t-1})$, with bigram counts from clean text. The observation model is unchanged. The top $N$ hidden sequences cost $O(NTK^2)$. A naive $K$ equals the vocabulary size and is slow. Exploiting the sparsity of $p(y\mid z)$ gives small candidate lists per position and a sparse belief state $\alpha_t$ (p. 989).

*29.3.3.3 Extended HMM.* [LDZ11; LDZ12] also model merged words ("home page"→"homepage"), split words ("illinoisstate"→"illinois state") and within-word errors. A *silent state*, which emits no symbol, handles the token-count mismatch. Fig. 29.11 denoises "goverment home page of illinoisstate" into "government homepage of illinois state" (pp. 989–990). A seq2seq RNN or transformer is an alternative. It can work very well but often needs much more training data, which is a problem for low-resource languages (p. 990).

### 29.4 HMMs: parameter learning (pp. 990–996)

**29.4.1 Baum-Welch (EM) (p. 990).** EM is an iterative bound-optimisation algorithm. For HMMs it is called Baum-Welch and gives an approximate MLE.

*29.4.1.1 Log likelihood.* With $\theta=(\pi,A,B)$, the joint of one sequence is
$$p(y_{1:T},z_{1:T}\mid\theta)=[p(z_1\mid\pi)]\Big[\prod_{t=2}^T p(z_t\mid z_{t-1},A)\Big]\Big[\prod_{t=1}^T p(y_t\mid z_t,B)\Big]\tag{29.23}$$
$$=\Big[\prod_{k=1}^K\pi_k^{\mathbb I(z_1=k)}\Big]\Big[\prod_{t=2}^T\prod_{j=1}^K\prod_{k=1}^K A_{jk}^{\mathbb I(z_{t-1}=j,z_t=k)}\Big]\Big[\prod_{t=1}^T\prod_{k=1}^K p(y_t\mid B_k)^{\mathbb I(z_t=k)}\Big]\tag{29.24}$$
$z_{1:T}$ is hidden, so we optimise the expected complete-data log likelihood, with expectation under the previous parameters (p. 990):
$$Q(\theta,\theta^{\text{old}})=\mathbb E_{p(z_{1:T}\mid y_{1:T},\theta^{\text{old}})}[\log p(y_{1:T},z_{1:T}\mid\theta)]\tag{29.25}$$
This sums easily over $N$ sequences (Fig. 29.12). $Q$ gives a lower bound on $\log p(y_{1:T}\mid\theta)$, so the procedure is guaranteed to converge to a local optimum. If suitably initialised, it can be shown to converge to (close to) one of the global optima [YBW15] (p. 990).

*29.4.1.2 E step.* Run forwards-backwards on each sequence $n$ (length $T_n$). It returns the node and edge marginals (p. 991):
$$\gamma_{n,t}(j)\triangleq p(z_t=j\mid y_{n,1:T_n},\theta^{\text{old}}),\quad\xi_{n,t}(j,k)\triangleq p(z_{t-1}=j,z_t=k\mid y_{n,1:T_n},\theta^{\text{old}})\tag{29.26, 29.27}$$
Expected counts, pooled over time (the parameters are tied) and over sequences:
$$\mathbb E[N_k^1]=\sum_{n=1}^N\gamma_{n,1}(k),\quad\mathbb E[N_k]=\sum_{n=1}^N\sum_{t=2}^{T_n}\gamma_{n,t}(k),\quad\mathbb E[N_{jk}]=\sum_{n=1}^N\sum_{t=2}^{T_n}\xi_{n,t}(j,k)\tag{29.28}$$
$$Q(\theta,\theta^{\text{old}})=\sum_{k=1}^K\mathbb E[N_k^1]\log\pi_k+\sum_{j=1}^K\sum_{k=1}^K\mathbb E[N_{jk}]\log A_{jk}+\sum_{n=1}^N\sum_{t=1}^{T_n}\sum_{k=1}^K p(z_t=k\mid y_{n,1:T_n},\theta^{\text{old}})\log p(y_{n,t}\mid\theta_k)\tag{29.29}$$

*29.4.1.3 M step.* Maximise subject to sum-to-one constraints. The result is normalised expected counts (p. 991):
$$\hat A_{jk}=\frac{\mathbb E[N_{jk}]}{\sum_{k'}\mathbb E[N_{jk'}]},\qquad\hat\pi_k=\frac{\mathbb E[N_k^1]}{N}\tag{29.30}$$
So $\hat A_{jk}$ is the expected number of $j\to k$ transitions divided by the expected number of transitions out of $j$ (p. 991).

Categorical observations (p. 992):
$$\mathbb E[M_{kv}]=\sum_{n=1}^N\sum_{t=1}^{T_n}\gamma_{n,t}(k)\,\mathbb I(y_{n,t}=v)=\sum_{n=1}^N\sum_{t:y_{n,t}=v}\gamma_{n,t}(k),\qquad\hat B_{kv}=\frac{\mathbb E[M_{kv}]}{\mathbb E[N_k]}\tag{29.31, 29.32}$$
Gaussian observations, with statistics $\overline{y}_k=\sum_n\sum_t\gamma_{n,t}(k)y_{n,t}$ and $\overline{yy^\top}_k=\sum_n\sum_t\gamma_{n,t}(k)y_{n,t}y_{n,t}^\top$ (29.33):
$$\hat\mu_k=\frac{\overline{y}_k}{\mathbb E[N_k]},\qquad\hat\Sigma_k=\frac{\overline{yy^\top}_k-\mathbb E[N_k]\hat\mu_k\hat\mu_k^\top}{\mathbb E[N_k]}\tag{29.34, 29.35}$$
A log prior is often added so that $\hat\Sigma_k$ is well-conditioned (p. 992). Algorithm 29.1 (p. 992): initialise $\theta$. Then loop: zero the expected counts; run forwards-backwards per sequence to get $\gamma,\xi$; accumulate the expected counts; recompute $(A,B,\pi)$.

*Intuition note:* The E step "soft-labels" every time step with a probability of being in each state. The M step then does ordinary counting with those fractional labels.

*29.4.1.4 Initialisation (p. 993).* Options: use some fully labelled data; ignore the Markov structure first and fit a mixture model (K-means or EM) for the observation parameters; or use random starts with multiple restarts and keep the best. Deterministic annealing can mitigate local minima. *Viterbi training* replaces the E-step sum over paths by statistics from the single most probable path. It sometimes gives better results [AG11].

*29.4.1.5 Casino HMM (p. 993).* The true model (Fig. 29.13a) has 2 states. State 1 has self-transition 0.95 and uniform emission 0.17 over six outcomes. State 2 has self-transition 0.90, with outcome 6 at 0.50 and the others at 0.10. Four sequences of length 5000 (20,000 observations) were generated. EM with random initial parameters ran for 200 iterations. The learned parameters are close to the truth, up to label switching (Fig. 29.13b) (p. 993).

**29.4.2 Parameter estimation using SGD (p. 994).** EM is a batch algorithm and does not scale well to many sequences. Online bound optimisation is possible but can take a lot of memory. Alternative: SGD on the log likelihood from the forwards algorithm:
$$\log p(y_{1:T}\mid\theta)=\sum_{t=1}^T\log p(y_t\mid y_{1:t-1},\theta)=\sum_{t=1}^T\log Z_t,\qquad Z_t\triangleq p(y_t\mid y_{1:t-1})=\sum_{j=1}^K p(z_t=j\mid y_{1:t-1})\,p(y_t\mid z_t=j)\tag{29.36, 29.37}$$
Constraints must hold: $A$ and $B$ row stochastic, $\Sigma_k$ positive semi-definite. EM keeps them automatically. With SGD one can reparameterise to an unconstrained form [BC94].
*Casino example:* SGD converges slightly more slowly than EM and does not decrease the NLL monotonically, even in the full-batch case. The final parameters are similar (Figs. 29.13c, 29.14).

**29.4.3 Spectral methods (p. 995).** The HMM log likelihood is not convex, so EM and SGD can give poor results through local optima. Alternative: marginalise out the hidden variables and use predictive distributions. For discrete HMMs with $B_{jk}=p(y_t=k\mid z_t=j)$, define the *predictive state representation* (PSR) vector $[y_t]_k\triangleq p(y_t=k\mid y_{1:t-1})$ (29.38).
- With $m$ hidden states and $n\ge m$ symbols, one can show [HKZ12; Joh12] that PSR vectors lie in an $m$-dimensional subspace of $\mathbb R^n$. Intuitively, $A$ combined with $B$ induces low-rank structure.
- A basis for this subspace can be estimated by SVD of the co-occurrence matrix $[P_2]_{ij}=p(y_t=i,y_{t-1}=j)$ (29.39). Third-order statistics $[P_3]_{ijk}=p(y_t=i,y_{t-1}=j,y_{t-2}=k)$ are also needed (29.40).
- Predictions can then be updated recursively entirely in visible space. This is *spectral estimation* or *tensor decomposition*.
- Spectral estimates can initialise EM, or be used as-is without EM.

**29.4.4 Bayesian HMMs (p. 995).** MLE can overfit and have numerical problems, especially with small samples. The Bayesian goal is $p(\theta\mid\mathcal D)$. A hierarchical Dirichlet process allows an unbounded number of states (HDP-HMM).
- Algorithms: variational Bayes EM, or blocked Gibbs. Blocked Gibbs alternates sampling latent sequences by forwards filtering backwards sampling, and sampling $\theta$ from its full conditional. The strong $z$–$\theta$ correlation makes this slow.
- Faster: marginalise the discrete latents with the forwards algorithm and run MCMC or SVI on the log posterior ("collapsed" inference):
$$\log p(\theta,\mathcal D)=\log p(\theta)+\sum_{n=1}^N\log p(y_{1:T,n}\mid\theta)\tag{29.41}$$

**29.4.4.1 Blocked Gibbs for HMMs (p. 996; section written by Xinglong Li).** Model: first-order AR-HMM (29.15) with parameters $\theta=\{\pi,A,E_1,\dots,E_K,\Sigma_1,\dots,\Sigma_K\}$. For simplicity the $\mu_j$ are assumed known, and observations are conditioned on $y_1$. Alternate between $p(z_{1:T}\mid y_{1:T},\theta)$ (forwards filtering backwards sampling) and $p(\theta\mid z_{1:T},y_{1:T})$, which is easy with conjugate priors:
$$\pi\sim\mathrm{Dir}(\breve\alpha_\pi),\quad A_{j\cdot}\sim\mathrm{Dir}(\breve\alpha_A)\tag{29.42}$$
$$\Sigma_j\sim\mathrm{IW}(\breve\nu_j,\breve\Psi_j),\quad E_j\mid\Sigma_j\sim\mathcal{MN}(\breve M_j,\Sigma_j,\breve V_j)\tag{29.43}$$
with $\breve\alpha_{\pi,k}=\breve\alpha_\pi/K$ and $\breve\alpha_{A,k}=\breve\alpha_A/K$. The matrix-normal inverse-Wishart prior is analogous to Bayesian multivariate linear regression. Log prior:
$$\log p(\theta)=c+\sum_{k=1}^K\frac{\breve\alpha_\pi}{K}\log\pi_k+\sum_{j=1}^K\sum_{k=1}^K\frac{\breve\alpha_A}{K}\log A_{jk}-\sum_{j=1}^K\Big(\frac{\breve\nu_j+N_y+1}{2}\log|\Sigma_j|+\frac12\mathrm{tr}(\breve\Psi_j\Sigma_j^{-1})\Big)-\sum_{j=1}^K\Big(\frac12\log|\Sigma_j|+\frac12\mathrm{tr}\big((E_j-\breve M_j)^\top\Sigma_j^{-1}(E_j-\breve M_j)\breve V_j\big)\Big)\tag{29.44}$$
Define $N_j=\sum_{t=2}^T\mathbb I(z_t=j)$ and $N_{jk}=\sum_{t=1}^{T-1}\mathbb I(z_t=j,z_{t+1}=k)$. The joint likelihood is
$$\log p(y_{1:T},z_{1:T}\mid\theta)=c+\sum_k\mathbb I(z_1=k)\log\pi_k+\sum_{j,k}N_{jk}\log A_{jk}-\sum_{j=1}^K\sum_{z_t=j}\Big(\tfrac12\log|\Sigma_j|+\tfrac12(y_t-E_jy_{t-1}-\mu_j)^\top\Sigma_j^{-1}(y_t-E_jy_{t-1}-\mu_j)\Big)\tag{29.45}$$
$$=c+\sum_k\mathbb I(z_1=k)\log\pi_k+\sum_{j,k}N_{jk}\log A_{jk}-\sum_{j=1}^K\Big(\tfrac{N_j}{2}\log|\Sigma_j|+\tfrac12(\hat Y_j-E_j\tilde Y_j)^\top\Sigma_j^{-1}(\hat Y_j-E_j\tilde Y_j)\Big)\tag{29.46}$$
Here $\hat Y_j=[y_t-\mu_j]_{z_t=j}$ and $\tilde Y_j=[y_{t-1}]_{z_t=j}$, and $\hat Y_j\sim\mathcal{MN}(\hat Y_j\mid E_j\tilde Y_j,\Sigma_j,I_{N_j})$ (p. 996). The unit's pages end here, before the conditional posteriors are stated.

## Toy example (ours, not from the text)
One sequence ($N=1$, $T=2$), $K=2$ states, Bernoulli observation. Observed $y=(1,0)$.
Parameters: $\pi=(0.6,0.4)$; $A=\begin{pmatrix}0.9&0.1\\0.2&0.8\end{pmatrix}$; $P(y=1\mid z=1)=0.8$, $P(y=1\mid z=2)=0.3$.

Joint $\pi_{z_1}\,p(y_1{=}1\mid z_1)\,A_{z_1z_2}\,p(y_2{=}0\mid z_2)$:
- (1,1): $0.6\cdot0.8\cdot0.9\cdot0.2=0.0864$
- (1,2): $0.6\cdot0.8\cdot0.1\cdot0.7=0.0336$
- (2,1): $0.4\cdot0.3\cdot0.2\cdot0.2=0.0048$
- (2,2): $0.4\cdot0.3\cdot0.8\cdot0.7=0.0672$

Total $p(y)=0.192$. E step with $T=2$: $\xi_2(j,k)$ equals joint/total, so $\xi_2=(0.45,\,0.175;\,0.025,\,0.35)$. These sum to 1. Then $\gamma_1(1)=0.45+0.175=0.625$ and $\gamma_1(2)=0.375$.
M step (29.30): row 1 sum $=0.625$, so $\hat A_{11}=0.45/0.625=0.72$ and $\hat A_{12}=0.28$. Row 2 sum $=0.375$, so $\hat A_{21}=0.025/0.375\approx0.067$ and $\hat A_{22}\approx0.933$. $\hat\pi=(0.625,0.375)/1$.
This is one EM update on one tiny sequence. It shows that the M step is just normalised soft counts.

## Concepts
- [[state-space-model]] (new) — hidden Markov state $z_t$ plus observations $y_t$ drawn from it; optional inputs (p. 979)
- [[hidden-markov-model]] (new) — SSM with discrete $z_t\in\{1..K\}$, parameters $\pi$, $A$ and an observation model (p. 980)
- [[autoregressive-hmm]] (new) — HMM with arcs $y_{t-1}\to y_t$; state-dependent linear regression (p. 982)
- [[scaled-likelihood-trick]] (new) — use $p(z\mid y)/p(z)$ from a classifier as the HMM likelihood (p. 984)
- [[profile-hmm]] (new) — match/insert/delete HMM for aligning sequences to a family consensus (p. 987)
- [[noisy-channel-model]] (new) — observed text is a corrupted version of a hidden message via edit errors (p. 988)
- [[baum-welch-em]] (new) — EM for HMMs using forwards-backwards marginals and expected counts (p. 990)
- [[predictive-state-representation]] (new) — vector of $p(y_t=k\mid y_{1:t-1})$; lies in a low-dimensional subspace (p. 995)
- [[spectral-estimation]] (new) — fit HMMs from low-order observable co-occurrence statistics via SVD or tensor decomposition (p. 995)
- [[label-switching]] (new) — learned states permuted relative to the truth because of unidentifiability (p. 993)
- [[marginal-likelihood-evidence]] — probability of data given $K$, approximated here by maximising over $\lambda$ (p. 986)
- [[bayesian-occams-razor]] — author's explanation for the fall in marginal likelihood for $K>4$ (p. 986)
- [[gibbs-sampling]] — blocked Gibbs alternates $z_{1:T}$ and $\theta$ (p. 996)
- [[conjugate-prior]] — Dirichlet and matrix-normal inverse-Wishart priors make the $\theta$ step easy (p. 996)

## Canonical instances
- [[casino-hmm]] — fitted by EM and SGD; learned states are label-switched (p. 993)
- [[poisson-hmm-changepoint]] — segmentation of count data; $K$ chosen by approximate marginal likelihood (p. 984)
- [[2d-ar-hmm-rotation]] — AR-HMM with rotation matrices and steady-state attractors (p. 983)
- [[spelling-correction-hmm]] — noisy channel plus bigram prior, silent state for merges and splits (pp. 988–990)
- [[lily-pad-frog]] — mental picture of a Gaussian HMM (p. 982)

## Bridges (candidates)
- [structural-analogy] Gaussian HMM ↔ Gaussian mixture model: clusters of observations, but with Markov temporal dependence between cluster labels (p. 982).
- [structural-analogy] Baum-Welch E/M steps ↔ EM for mixture models: soft responsibilities and normalised expected counts, with $\gamma$ and $\xi$ computed by forwards-backwards.
- [structural-analogy] Scaled likelihood trick ↔ Bayes' rule: $p(y\mid z)\propto p(z\mid y)/p(z)$ (29.17).
- [structural-analogy] $K$ selection by marginal likelihood ↔ Bayesian Occam's razor: more states fit no better, so evidence falls (p. 986).

## Questions this raises
- The text approximates the marginal likelihood by maximising over $\lambda$ (29.21). How far does this empirical-Bayes shortcut preserve the Occam penalty compared with integrating over $\lambda$?
- Why does the strong correlation between $z$ and $\theta$ slow blocked Gibbs, and why does collapsing the latents help?
- When are spectral estimates good enough to use without EM, and how do they compare with EM from random starts?
- How do the conditional posteriors for $\pi$, $A$, $E_j$ and $\Sigma_j$ follow from (29.44)–(29.46)? (They are cut off at the end of these pages.)

## Reading notes
- This unit is part 1 of 3 of Chapter 29. It starts at §29.1 (printed p. 979) and ends mid-§29.4.4.1 (p. 996), right after Eq. 29.46. The unit metadata says the split is at a section boundary, although these pages end mid-§29.4.4.1. Printed = pdf − 34.
- On alternate pages the footer reads "Online version. December 10, 2025"; the other pages show an author/licence footer.
- Eq. 29.10 prints the observation matrix as $y_{jk}$; the later text uses $B_{jk}$. Likely a notation slip.
- §29.2.4 says "3 hidden states", but the Fig. 29.3 caption says a 5-state HMM and five clusters are drawn.
- Eqs. 29.19–29.20 hard-code 4 states and use $K-1$ in the text.
- The text cites "Algorithm 11"; the algorithm is labelled Algorithm 29.1. Its line 11 cites only Eq. 29.30.
- Algorithm 29.1 and (29.28) sum $\mathbb E[N_k]$ from $t=2$, while $\mathbb E[M_{kv}]$ in (29.31) sums from $t=1$; (29.32) divides one by the other. I report this as printed. The algorithm also uses $x_{n,t}$ for observations.
- Fig. 29.14 caption labels two panels "(b)". Panel (c) is full-batch GD. Fig. 29.12's caption uses $x_t$.
- The text layer matched the images for all equations. There are no exercises in this unit.

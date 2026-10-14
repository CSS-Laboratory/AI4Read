---
id: murphy-2023-pml2/ch09-message
work: murphy-2023-pml2
unit: "Chapter 9. Message passing algorithms"
pages: 401–437
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
# Message passing algorithms (Murphy, PML2, Ch. 9)

## L0 — One line
On a sparse graph, posterior inference can be organised as messages passed between neighbouring nodes (dynamic programming): exact on chains and trees, an approximation on loopy graphs, while variable elimination is exact on any discrete graph at a cost exponential in the size of its largest intermediate factor.

## L1 — The gist (≤ 120 words)
How can we compute posterior marginals (the distribution of one variable), most probable states, or samples when a model's graph is sparse? On chains such as hidden Markov models (chains of hidden states), and on trees, passing messages between neighbours (forwards, then backwards) gives exact answers by dynamic programming (reusing subproblem results). On graphs with loops, the same updates ("loopy BP") may fail to converge and are an approximation, though they work well in some applications. Variable elimination (summing out variables) is exact on any discrete graph, but its cost is exponential in the size of its largest intermediate table. The junction tree algorithm reuses work across marginals. Inference can also be recast as differentiation or optimization.

**Prerequisites:** conditional probability and Bayes' rule; conditional independence in graphical models; matrix–vector products; log-sum-exp; basic exponential-family facts (only for §9.7); Gaussian conditioning (only for §9.7.2.1).

## L2 — Key ideas
- **Chain inference (HMM).** *Filtering* gives p(z_t | y_{1:t}) (state given past data). A backward message β_t(j)=p(y_{t+1:T}|z_t=j) carries future data. Multiplying and renormalising gives *smoothing*, p(z_t | y_{1:T}), in O(TK²) time for K states (pp. 403–405).
- **Normalise at every step.** The unnormalised joint form underflows (numbers too small for the computer). The normalised form is also interpretable and compatible with approximate inference (p. 407).
- **MAP vs marginals.** The Viterbi algorithm replaces sums by max and traces back the best (jointly most probable) path. The jointly most probable path can differ from the per-node most probable states (pp. 409–410, 416–417). Which is better depends on the loss (p. 417).
- **Trees.** The sum-product algorithm collects messages at a root, then distributes them back. Dividing out the incoming message reuses the already computed product. Stored messages give all marginals (pp. 414–415, 434).
- **Loopy BP** applies the same updates in parallel on graphs with cycles. It may not converge, and Pearl warned that the asymptotic equilibrium is not coherent. Damping (blending new messages with old ones) and residual scheduling (sending first the messages that changed most) help (pp. 417–423). For Gaussians, if it converges the means are exact but the variances are not (p. 424).
- **Applications.** Turbocodes, a popular error-correcting-code algorithm, can be viewed as LBP on a certain graph, and LDPC code graphs are locally tree-like, which matters for LBP's success (p. 425). It also drives affinity propagation, a clustering method (pp. 426–427).
- **Variable elimination (VE)** pushes sums inside products. Its cost is exponential in the largest intermediate factor, which depends on the elimination order. Treewidth is the smallest possible induced width, and finding the best order is NP-complete (pp. 428–432).
- **Hardness.** Exact inference in discrete models is NP-hard (even #P-hard), so we often have to resort to approximate methods (p. 433). The junction tree algorithm generalises VE to reuse messages (p. 434).
- **Inference as optimization.** The gradient of the log partition function (log of the normalising constant) gives marginals, so autodiff does inference (p. 435). Perturb-and-MAP (solve MAP on noise-perturbed parameters) draws posterior samples from MAP solves; with a suitably chosen noise distribution it gives exact samples (p. 436).

## L3 — Walkthrough

### 9.1 Introduction (p. 401)
- Goal: posterior inference (marginals, modes, samples) for distributions given by a probabilistic graphical model with sparse graph structure. The algorithms use the conditional independencies in the graph and dynamic programming (DP: solve subproblems, then combine) (p. 401).
- DP is implemented by local computations at nodes (or cliques) and *messages* sent to neighbours. Messages are read as distributions ("belief states") about a node given part of the graph's evidence, so the methods are also called belief propagation (BP) (p. 401).
- Roadmap: chain (§9.2), tree (§9.3), any graph including loops (§9.4). Messages on loopy graphs may give incorrect answers; then one may convert the graph to a tree (§9.5, §9.6) or pose inference as optimization (§9.7) (p. 401).

### 9.2 Belief propagation on chains (pp. 401–412)
Directed chain, discrete hidden variables (p. 401).

**9.2.1 Hidden Markov models.** State-space model with joint (p. 402):
$$p(y_{1:T},z_{1:T})=\Big[p(z_1)\prod_{t=2}^{T}p(z_t|z_{t-1})\Big]\Big[\prod_{t=1}^{T}p(y_t|z_t)\Big]\tag{9.1}$$
With discrete latent variables this is a hidden Markov model (HMM) (p. 402).

*9.2.1.1 Casino HMM* (pp. 402–403). Observed die rolls $y_t\in\{1,\dots,6\}$. Hidden $z_t\in\{1,2\}$ = fair or loaded. $A_{jk}=p(z_t=k|z_{t-1}=j)$, $B_{kl}=p(y_t=l|z_t=k)$. Figure 9.2 gives the transitions: fair→fair 0.95, fair→loaded 0.05, loaded→loaded 0.90, loaded→fair 0.1 (p. 402).
$$p(y_t|z_t=1)=\mathrm{Cat}(y_t|[1/6,\dots,1/6])\tag{9.2}$$
$$p(y_t|z_t=2)=\mathrm{Cat}(y_t|[1/10,1/10,1/10,1/10,1/10,5/10])\tag{9.3}$$
In a sampled sequence of length 300, a 6 occurred with frequency 0.149 in state 1 and 0.472 in state 2 (p. 403).

*9.2.1.2 Posterior inference.* The aim is the *smoothing distribution* $p(z_t|y_{1:T})$. By the Markov property (the conditioning on $y_{1:t}$ drops in the last factor) (p. 403):
$$p(z_t=j|y_{t+1:T},y_{1:t})\propto p(z_t=j,y_{t+1:T}|y_{1:t})=p(z_t=j|y_{1:t})\,p(y_{t+1:T}|z_t=j)\tag{9.4}$$
Plan: compute the *filtering distribution* $p(z_t=j|y_{1:t})$ forwards, the $p(y_{t+1:T}|z_t=j)$ backwards, then combine. Both passes take $O(TK^2)$ time (p. 403).

**9.2.2 Forwards algorithm.** This is the Bayes filter of §8.1.2 (p. 403). Definitions: belief vector $\alpha_t(j)\triangleq p(z_t=j|y_{1:t})$, local evidence $\lambda_t(j)\triangleq p(y_t|z_t=j)$, $A_{i,j}=p(z_t=j|z_{t-1}=i)$.

Predict step (p. 403):
$$\alpha_{t|t-1}(j)\triangleq p(z_t=j|y_{1:t-1})=\sum_i A_{i,j}\,\alpha_{t-1}(i)\tag{9.5}$$
Update step (p. 404):
$$\alpha_t(j)=\tfrac1{Z_t}\lambda_t(j)\alpha_{t|t-1}(j)=\tfrac1{Z_t}\lambda_t(j)\Big[\sum_i\alpha_{t-1}(i)A_{i,j}\Big]\tag{9.6}$$
$$Z_t\triangleq p(y_t|y_{1:t-1})=\sum_{j=1}^{K}\lambda_t(j)\alpha_{t|t-1}(j)\tag{9.7}$$
$$\boldsymbol\alpha_t=\mathrm{normalize}\big(\boldsymbol\lambda_t\odot(\mathbf A^{\mathsf T}\boldsymbol\alpha_{t-1})\big)\tag{9.8}$$
Shapes: $\boldsymbol\alpha_t,\boldsymbol\lambda_t\in\mathbb R^K$, $\mathbf A\in\mathbb R^{K\times K}$; $\odot$ is elementwise product (p. 404). Figure 9.3(a): in the casino run (T=300), the filtered probability of "loaded" generally rises in the right places (p. 404).

*Intuition note.* Each step is "predict with the transition matrix, then multiply by how well each state explains the new observation, then renormalise". The normaliser $Z_t$ is the probability of the new observation given the past.

**9.2.3 Forwards-backwards (FB)** (pp. 404–405). Forward pass as before. Backward pass computes the conditional likelihood
$$\beta_t(j)\triangleq p(y_{t+1:T}|z_t=j)\tag{9.9}$$
Combination (p. 405):
$$\gamma_t(j)=p(z_t=j|y_{t+1:T},y_{1:t})\propto p(z_t=j,y_{t+1:T}|y_{1:t})=p(z_t=j|y_{1:t})\,p(y_{t+1:T}|z_t=j)=\alpha_t(j)\beta_t(j)\tag{9.10–9.11}$$
$$\boldsymbol\gamma_t=\mathrm{normalize}(\boldsymbol\alpha_t\odot\boldsymbol\beta_t)\tag{9.12}$$
The two passes can be computed independently, but both need access to the local evidence $p(y_t|z_t)$. They are combined only at the end, hence "two-filter smoothing" (p. 405).

*9.2.3.1 Backwards recursion* (p. 405). Right to left:
$$\beta_{t-1}(i)=p(y_{t:T}|z_{t-1}=i)=\sum_j p(z_t=j,y_t,y_{t+1:T}|z_{t-1}=i)\tag{9.13–9.14}$$
$$=\sum_j p(y_{t+1:T}|z_t=j)\,p(z_t=j,y_t|z_{t-1}=i)\tag{9.15}$$
$$=\sum_j p(y_{t+1:T}|z_t=j)\,p(y_t|z_t=j)\,p(z_t=j|z_{t-1}=i)\tag{9.16}$$
$$=\sum_j\beta_t(j)\lambda_t(j)A_{i,j}\tag{9.17}$$
The struck-out terms in the source mark conditioning variables dropped by conditional independence. Matrix form and base case:
$$\boldsymbol\beta_{t-1}=\mathbf A(\boldsymbol\lambda_t\odot\boldsymbol\beta_t)\tag{9.18}$$
$$\beta_T(i)=p(y_{T+1:T}|z_T=i)=p(\emptyset|z_T=i)=1\tag{9.19}$$
"The probability of a non-event." $\boldsymbol\beta_t$ need not sum to 1, so it is not a distribution over states, but it is usually normalised to avoid underflow (p. 405).

*9.2.3.2 Example.* In Fig. 9.3(a–b), the posteriors conditioned on all data (past and future) are smoother than those conditioned on the past only (p. 405).

*Intuition note.* $\alpha_t$ summarises what the past says about $z_t$; $\beta_t$ summarises what the future observations say. Multiplying and renormalising uses all the data.

*9.2.3.3 Two-slice smoothed marginals* (p. 406). The joint of two neighbouring states:
$$p(z_t,z_{t+1}|y_{1:T})=p(z_t,z_{t+1}|y_{1:t},y_{t+1:T})\tag{9.20}$$
$$\propto p(y_{t+1:T}|z_t,z_{t+1},y_{1:t})\,p(z_t,z_{t+1}|y_{1:t})\tag{9.21}$$
$$=p(y_{t+1:T}|z_{t+1})\,p(z_t,z_{t+1}|y_{1:t})\tag{9.22}$$
$$=p(y_{t+1:T}|z_{t+1})\,p(z_t|y_{1:t})\,p(z_{t+1}|z_t)\tag{9.23}$$
$$=p(y_{t+1},y_{t+2:T}|z_{t+1})\,p(z_t|y_{1:t})\,p(z_{t+1}|z_t)\tag{9.24}$$
$$=p(y_{t+1}|z_{t+1})\,p(y_{t+2:T}|z_{t+1},y_{t+1})\,p(z_t|y_{1:t})\,p(z_{t+1}|z_t)\tag{9.25}$$
$$=p(y_{t+1}|z_{t+1})\,p(y_{t+2:T}|z_{t+1})\,p(z_t|y_{1:t})\,p(z_{t+1}|z_t)\tag{9.26}$$
In already computed quantities (shape $K\times K$ in matrix form: $\mathbf A$ is $K\times K$, $\boldsymbol\alpha_t$ is $K\times1$, $(\cdot)^{\mathsf T}$ is $1\times K$):
$$\xi_{t,t+1}(i,j)\propto\lambda_{t+1}(j)\beta_{t+1}(j)\alpha_t(i)A_{i,j}\tag{9.27}$$
$$\boldsymbol\xi_{t,t+1}\propto\mathbf A\odot\big[\boldsymbol\alpha_t(\boldsymbol\lambda_{t+1}\odot\boldsymbol\beta_{t+1})^{\mathsf T}\big]\tag{9.28}$$
$$\boldsymbol\xi_{t,t+1}\propto\mathbf A\odot\big[(\boldsymbol\lambda_t\odot\boldsymbol\alpha_{t|t-1})\odot(\boldsymbol\lambda_{t+1}\odot\boldsymbol\beta_{t+1})^{\mathsf T}\big]\tag{9.29}$$
(9.29) uses $\boldsymbol\alpha_t\propto\boldsymbol\lambda_t\odot\boldsymbol\alpha_{t|t-1}$. It is read as a product of incoming messages ($\alpha_{t|t-1}$, $\beta_{t+1}$, $\lambda_t$, $\lambda_{t+1}$) and the local factor $\mathbf A$ (Fig. 9.4), giving $p(z_t,z_{t+1},y_t,y_{t+1},y_{t+2:T}|y_{1:t-1})$ up to normalisation (p. 406).

*9.2.3.4 Numerically stable implementation* (p. 407). Many publications (e.g. Rab89) use the unnormalised joint
$$\alpha'_t(j)=p(z_t=j,y_{1:t})=\lambda_t(j)\Big[\sum_i\alpha'_{t-1}(i)A_{i,j}\Big]\tag{9.30}$$
The author instead uses the normalised conditional
$$\alpha_t(j)=p(z_t=j|y_{1:t})=\tfrac1{Z_t}\lambda_t(j)\Big[\sum_i\alpha_{t-1}(i)A_{i,j}\Big]\tag{9.31}$$
Reasons given for the joint form's problems: (1) it underflows quickly (e.g. if observations are independent of states, $p(z_t=j,y_{1:t})=p(z_t=j)\prod_{i\le t}p(y_i)$, exponentially small in $t$); (2) it is less interpretable (not a distribution over states); (3) it precludes approximate-inference methods that approximate posterior distributions. The two forms differ by a constant, $p(z_t=j|y_{1:t})=p(z_t=j,y_{1:t})/p(y_{1:t})$, so the algorithmic difference is one call to `normalize` (p. 407). In practice it is more stable to use log evidence $\ell_t(j)=\log p(y_t|z_t=j)$ and combine with the state prior via the log-sum-exp trick (Eq. 28.30) (p. 407).

**9.2.4 Forwards filtering backwards smoothing** (pp. 407–408). Alternative offline smoother (§8.1.3): filter first, then work from $t=T$ to $t=1$. It is widely used for continuous latent states, since $\beta_t$ is not always well defined when the state space is not discrete (p. 407). Assume by induction $\gamma_{t+1}(j)\triangleq p(z_{t+1}=j|y_{1:T})$ (9.32). Then (p. 408)
$$\xi_{t,t+1}(i,j)\triangleq p(z_t=i,z_{t+1}=j|y_{1:T})=p(z_t=i|z_{t+1}=j,y_{1:t})\,p(z_{t+1}=j|y_{1:T})\tag{9.33}$$
$$=\frac{p(z_{t+1}=j|z_t=i)\,p(z_t=i|y_{1:t})\,p(z_{t+1}=j|y_{1:T})}{p(z_{t+1}=j|y_{1:t})}\tag{9.34}$$
$$=\alpha_t(i)A_{i,j}\frac{\gamma_{t+1}(j)}{\alpha_{t+1|t}(j)}\tag{9.35}$$
$$\alpha_{t+1|t}(j)=p(z_{t+1}=j|y_{1:t})=\sum_{i'}A(i',j)\alpha_t(i')\tag{9.36}$$
The ratio in (9.35) divides out the old estimate of $z_{t+1}$ given $y_{1:t}$ and multiplies in the new estimate given $y_{1:T}$. Summing over $j$:
$$\gamma_t(i)=p(z_t=i|y_{1:T})=\sum_j\xi_{t,t+1}(i,j)=\alpha_t(i)\sum_j\Big[A_{i,j}\frac{\gamma_{t+1}(j)}{\alpha_{t+1|t}(j)}\Big]\tag{9.37}$$
Initialise with $\gamma_T(j)=\alpha_T(j)=p(z_T=j|y_{1:T})$ (p. 408).

**9.2.5 Time and space complexity** (pp. 408–409).
- Straightforward FB: $O(K^2T)$ time (a $K\times K$ matrix product per step). For large K (e.g. speech recognition) this is prohibitive. With a sparse transition matrix it can drop substantially; a sparse left-to-right matrix gives $O(TK)$ (p. 408).
- If states discretise a continuous space and $A_{i,j}\propto\rho(\mathbf z_j-\mathbf z_i)$, the predict step is a convolution,
$$\alpha_{t|t-1}(j)=\sum_i\alpha_{t-1}(i)A_{i,j}=\sum_i\alpha_{t-1}(i)\rho(j-i)\tag{9.38}$$
so with the Fast Fourier Transform FB runs in $O(TK\log K)$ (p. 408).
- A parallel prefix scan (suited to GPUs) can reduce inference to $O(\log T)$ time (p. 408).
- Memory: all $\boldsymbol\alpha_t$ must be stored until the backward pass. A divide-and-conquer scheme with checkpoints reduces space from $O(KT)$ to $O(K\log T)$, at the cost of time rising from $O(K^2T)$ to $O(K^2T\log T)$ (pp. 408–409).

**9.2.6 Viterbi algorithm** (pp. 409–411). The MAP estimate is (one of) the sequences with maximum posterior probability:
$$\mathbf z^*_{1:T}=\arg\max_{\mathbf z_{1:T}}p(\mathbf z_{1:T}|\mathbf y_{1:T})=\arg\max\log p(\mathbf z_{1:T}|\mathbf y_{1:T})\tag{9.39}$$
$$=\arg\max_{\mathbf z_{1:T}}\log\pi_1(z_1)+\log\lambda_1(z_1)+\sum_{t=2}^{T}[\log A(z_{t-1},z_t)+\log\lambda_t(z_t)]\tag{9.40}$$
This is a shortest path through the trellis (Fig. 9.5; nodes = states per time, weights = log probabilities), computed in $O(TK^2)$ time (p. 409).

*Forwards pass.* Recall $\alpha'_t(j)=\sum_{z_1..z_{t-1}}p(z_{1:t-1},z_t=j,y_{1:t})$ (9.41). Replace the sum by max:
$$\delta_t(j)\triangleq\max_{z_1,\dots,z_{t-1}}p(z_{1:t-1},z_t=j,y_{1:t})\tag{9.42}$$
the maximum probability of the data so far if we end in $j$ (p. 409). Key insight: the most probable path to $j$ at time $t$ consists of the most probable path to some state $i$ at $t-1$ followed by $i\to j$ (pp. 409–410):
$$\delta_t(j)=\lambda_t(j)\max_i\big[\delta_{t-1}(i)A_{i,j}\big],\qquad\delta_1(j)=\pi_j\lambda_1(j)\tag{9.43}$$
In the log domain, with $\delta'_t=-\log\delta_t$, $\lambda'_t=-\log p(y_t|z_t=j)$, $A'(i,j)=-\log p(z_t=j|z_{t-1}=i)$:
$$\delta'_t(j)=\lambda'_t(j)+\min_i\big[\delta'_{t-1}(i)+A'(i,j)\big]\tag{9.44}$$
Ancestor (best previous state):
$$a_t(j)\triangleq\arg\max_i\delta_{t-1}(i)A_{i,j}=\arg\min_i\ \delta'_{t-1}(i)+A'(i,j)\tag{9.45}$$
(p. 410).

*Backwards pass (traceback).* $z^*_t=a_{t+1}(z^*_{t+1})$ with $z^*_T=\arg\max_i\delta_T(i)$ (p. 410). If the MAP estimate is unique, this equals picking $\hat z_t=\arg\max_j\gamma_t(j)$ from FB ([WF01b]). With several posterior modes, the per-node choice may not find any of them, because each node breaks ties independently. Traceback conditions earlier nodes on the later choice, so ties are broken consistently (p. 410).

*Example* (pp. 410–411). Fig. 9.3(c) shows the Viterbi trace for the casino. Fig. 9.6 is a 3-state speech HMM with $y_{1:4}=(C_1,C_3,C_4,C_6)$, starting in $S_1$. $\delta_1(1)=0.5$, other $\delta_1(i)=0$. Transitions from $S_1$: self 0.3, to $S_2$ 0.7. $p(C_3|S_1)=0.3$, $p(C_3|S_2)=0.2$:
$$\delta_2(1)=\delta_1(1)A(1,1)\lambda_2(1)=0.5\cdot0.3\cdot0.3=0.045\tag{9.46}$$
$$\delta_2(2)=\delta_1(1)A(1,2)\lambda_2(2)=0.5\cdot0.7\cdot0.2=0.07\tag{9.47}$$
So state 2 is more probable at $t=2$. Following the red arrows back from the end gives the MAP path 1,2,2,3 (p. 411). Fig. 9.6(b) shows $\delta_3(2)=0.0441$, $\delta_3(3)=0.0007$, $\delta_4(3)=0.0022$ (image).

*Complexity.* Time $O(K^2T)$, space $O(KT)$, same as FB. If $A_{i,j}\propto\rho(\mathbf z_j-\mathbf z_i)$ as above, Viterbi can run in $O(TK)$ via the generalized distance transform (p. 411).

*N-best list* (pp. 411–412). Several paths can have equal likelihood. Viterbi returns one, and can be extended to the top-N paths, which gives a better summary of posterior uncertainty. Discriminative reranking of these using global features is widely used in speech recognition: the top interpretation of an acoustic signal for "recognize speech" might be "wreck a nice speech" or "wreck a nice beach", and reranking may promote the correct one. The top-N paths are often very similar to each other. More diverse sets can come from posterior sampling (§9.2.7) or a determinantal point process (p. 412).

**9.2.7 Forwards filtering backwards sampling** (p. 412). To draw $\mathbf z^s_{1:T}\sim p(\mathbf z_{1:T}|\mathbf y_{1:T})$, modify §9.2.4 to sample on the backward pass instead of computing marginals. The joint factorises right to left:
$$p(\mathbf z_{1:T}|\mathbf y_{1:T})=p(\mathbf z_T|\mathbf y_{1:T})\prod_{t=T-1}^{1}p(\mathbf z_t|\mathbf z_{t+1},\mathbf y_{1:T})\tag{9.48–9.49}$$
At step $t$, sample $\mathbf z^s_t$ from $p(\mathbf z_t|\mathbf z^s_{t+1},\mathbf y_{1:T})$ (p. 412).

### 9.3 Belief propagation on trees (pp. 412–417)
FB for HMMs (and the Kalman smoother of §8.2.3) can be seen as message passing on a chain. §9.3 generalises to trees (p. 412).

**9.3.1 Directed vs undirected trees** (pp. 412–413). Pairwise undirected model:
$$p^*(\mathbf z)\triangleq p(\mathbf z|\mathbf y)\propto\prod_{s\in\mathcal V}\psi_s(z_s|y_s)\prod_{(s,t)\in\mathcal E}\psi_{s,t}(z_s,z_t)\tag{9.50}$$
($\psi_{s,t}$: one pairwise potential per edge; $\psi_s$: local evidence per node; the conditioning on $\mathbf y$ is then dropped.) A tree can always be directed by choosing a root and orienting edges away from it. For Fig. 9.7, root 1 or root 2 give
$$p^*(\mathbf z)\propto p^*(z_1)p^*(z_2|z_1)p^*(z_3|z_2)p^*(z_4|z_2)\tag{9.51}$$
$$p^*(\mathbf z)\propto p^*(z_2)p^*(z_1|z_2)p^*(z_3|z_2)p^*(z_4|z_2)\tag{9.52}$$
These express the same conditional independencies, so they represent the same family (p. 413). For symmetry the author prefers the undirected form with potentials $\psi_s(z_s)\propto p^*(z_s)$, $\psi_{s,t}(z_s,z_t)=p^*(z_s,z_t)$:
$$p^*(\mathbf z)\propto\prod_{s\in\mathcal V}p^*(z_s)\prod_{(s,t)\in\mathcal E}\frac{p^*(z_s,z_t)}{p^*(z_s)p^*(z_t)}\tag{9.53}$$
For Fig. 9.7a:
$$p^*(z_1,z_2,z_3,z_4)\propto p^*(z_1)p^*(z_2)p^*(z_3)p^*(z_4)\frac{p^*(z_1,z_2)p^*(z_2,z_3)p^*(z_2,z_4)}{p^*(z_1)p^*(z_2)p^*(z_2)p^*(z_3)p^*(z_2)p^*(z_4)}\tag{9.54}$$
Cancelling terms:
$$\propto p^*(z_1,z_2)\frac{p^*(z_2,z_3)}{p^*(z_2)}\frac{p^*(z_2,z_4)}{p^*(z_2)}\tag{9.55}$$
$$=p^*(z_1)p^*(z_2|z_1)p^*(z_3|z_2)p^*(z_4|z_2)=p^*(z_2)p^*(z_1|z_2)p^*(z_3|z_2)p^*(z_4|z_2)\tag{9.56–9.57}$$
with $p^*(z_t|z_s)=p^*(z_s,z_t)/p^*(z_s)$. A tree can be represented as undirected or directed (p. 413).

**9.3.2 Sum-product algorithm** (pp. 414–415). Take the undirected tree (9.50), pick an arbitrary root, orient edges away so each node has one parent. *Pre-order* traversal: root first, top to bottom. *Post-order*: bottom to top, root last (p. 414).

$m_{s\to t}(z_t)$ is the message from $s$ to $t$. It summarises the belief state about $z_t$ given all evidence in the tree below the $s$–$t$ edge (p. 414).

*Upward (collect) pass.* Combine children's messages with local evidence, then send to the parent $t$ (p. 415):
$$\mathrm{bel}_s(z_s)\propto\psi_s(z_s)\prod_{t\in\mathrm{ch}_s}m_{t\to s}(z_s)\tag{9.58}$$
$$m_{s\to t}(z_t)=\sum_{z_s}\psi_{st}(z_s,z_t)\,\mathrm{bel}_s(z_s)\tag{9.59}$$
*Downward (distribute) pass.* At the root, $\mathrm{bel}(z)=p(z|\mathbf y)$ has seen all the evidence. The message from $s$ to child $t$ multiplies the messages from $s$'s *other* children $u$ (Fig. 9.9):
$$m_{s\to t}(z_t)=\sum_{z_s}\Big(\psi_s(z_s)\psi_{st}(z_s,z_t)\prod_{u\in\mathrm{ch}_s\setminus t}m_{u\to s}(z_s)\Big)\tag{9.60}$$
Instead, multiply all messages and divide out the one from $t$. The full product was already computed in (9.58) (p. 415):
$$m_{s\to t}(z_t)=\sum_{z_s}\psi_{st}(z_s,z_t)\frac{\mathrm{bel}_s(z_s)}{m_{t\to s}(z_s)}\tag{9.61}$$
**Author's reading:** one can think of $\mathrm{bel}_s(z_s)$ as the new posterior $p(z_s|\mathbf y)$ and of $m_{t\to s}(z_s)$ as the prior predictive $p(z_s|\mathbf y_t^-)$, where $\mathbf y_t^-$ is all evidence in the subtree rooted at $t$. Thus the ratio contains the new evidence that $t$ did not already know from its own subtree. Node $t$ updates
$$\mathrm{bel}_t(z_t)\propto\mathrm{bel}_t(z_t)\,m_{s\to t}(z_t)\tag{9.62}$$
(9.58) is the special case without division, since the upward pass has no message from the parent (p. 415). The analogy with (9.37): $\alpha_t(i)\to\mathrm{bel}_t(z_t=i)$, $A(i,j)\to\psi_{st}(i,j)$, $\gamma_{t+1}(j)\to\mathrm{bel}_s(z_s=j)$, $\alpha_{t+1|t}(j)\to m_{t\to s}(z_s=j)$. Fig. 9.8 gives the pseudocode. Directed trees with several roots (polytrees) are covered in Supplementary §9.1.1 (p. 415).

*Intuition note.* Each node first collects summaries from below, then the root pushes the global answer down. The division in (9.61) means $t$ is not told what its own subtree already told $s$.

**9.3.3 Max-product algorithm** (p. 416). Sum-product computes $\mathrm{bel}_i(k)=\gamma_i(k)=p(z_i=k|\mathbf y)=\sum_{\mathbf z_{-i}}p(z_i=k,\mathbf z_{-i}|\mathbf y)$ (9.63). Replacing the sum by max gives max-product BP and the *max marginals*
$$\zeta_i(k)=\max_{\mathbf z_{-i}}p(z_i=k,\mathbf z_{-i}|\mathbf y)\tag{9.64}$$
Two local estimates: $\hat z_i=\arg\max_k\gamma_i(k)$ (maximiser of the posterior marginal, **MPM**) and $\tilde z_i=\arg\max_k\zeta_i(k)$ (maximiser of the max marginal, **MMM**). The question is how they relate to the true MAP $\mathbf z^*=\arg\max_{\mathbf z}p(\mathbf z|\mathbf y)$ (p. 416).

*9.3.3.1 MMM and MAP* (p. 416). [YW04] showed that if the max marginals are unique and computed exactly (e.g. on a tree), then $\tilde{\mathbf z}=\mathbf z^*$. With ties (more than one globally optimal solution) this "local stitching" may give globally inconsistent results. On trees one can use a Viterbi-like traceback, clamping nodes to optimal values from the root down. Traceback does not work on general graphs. [YW04]'s alternative: run max-product BP, clamp nodes with unique max marginals, clamp one ambiguous node, condition on the clamped values, and repeat until ties are broken. This may need many rounds (p. 416).

*9.3.3.2 MPM and MAP* (pp. 416–417). In general MPM does not equal MAP, even with exact marginals, because MPM ignores dependencies or constraints in the prior (p. 416). **Example (error-correcting code, §5.5).** $p(\mathbf z,\mathbf y)=p(z_1)p(z_2)p(z_3|z_1,z_2)\prod_{i=1}^3p(y_i|z_i)$, all binary. Priors on $z_1,z_2$ uniform. $p(z_3=1|z_1,z_2)=\mathbb I(\mathrm{odd}(z_1,z_2))$, so $\mathbf z_{1:3}$ has an even number of 1s. Bit-flip channel with noise $\alpha=0.2$. Observe $\mathbf y=(1,0,0)$:
- exact posterior marginals: $\gamma_1=[0.3469,0.6531]$, $\gamma_2=[0.6531,0.3469]$, $\gamma_3=[0.6531,0.3469]$ (p. 416);
- exact max marginals: $\zeta_i=[0.3265,0.3265]$ for all $i$ (pp. 416–417);
- three global MAP estimates: $[0,0,0],[1,1,0],[1,0,1]$, each a valid codeword one bit flip from $\mathbf y$;
- MPM estimate $\hat{\mathbf z}=[1,0,0]$, not a legal codeword; MMM is not well defined (max marginals not unique) (p. 417).

Which is better depends on the loss. To minimise per-bit error ("bit error") use MPM; to minimise error on the whole sequence ("word error") use MAP, which takes global constraints into account. In speech, MPM may return "wreck a nice beach" while MAP, using the language-model prior, favours "recognize speech". Without strong constraints MPM can be more robust since it marginalises rather than maximises: in the casino example MPM makes 49 bit errors out of T=300, the MAP path 60 (p. 417).

*9.3.3.3 MPE and MAP* (p. 417). In the graphical-model literature, the jointly most likely setting of all latent variables is the **most probable explanation (MPE)**, and "MAP" means maximising some variables while summing out the rest. For query set $Q$, visible set $V$, remaining ("nuisance") variables $R$:
$$\mathbf z_Q^*=\arg\max_{\mathbf z_Q}\sum_{\mathbf z_R}p(\mathbf z_Q,\mathbf z_R|\mathbf z_V)\tag{9.65}$$
Pearl calls this MAP; the author calls it MPM to avoid clashing with the ML meaning of MAP (p. 417).

*Intuition note.* MAP picks the best whole configuration; MPM picks the best value for each variable separately. In the parity example, each bit separately prefers a pattern that is not a valid codeword.

### 9.4 Loopy belief propagation (pp. 417–428)
Loopy BP (LBP) runs BP on graphs with cycles. It may not converge, and even if it does, it is not clear that the estimates are valid (p. 417). **Pearl (1988), paraphrased:** with loops, local propagation will invariably run into trouble; messages may circulate indefinitely and may not converge. He adds that such oscillations do not normally occur in probabilistic networks, which tend to settle to a stable equilibrium. However, that asymptotic equilibrium is not coherent: it does not represent the posterior probabilities of all nodes (pp. 417–418). Despite this, Pearl advocated BP in loopy networks as an approximation scheme; [MWJ99] found empirically that it works on various graphical models; there is now some theory justifying it in certain cases (p. 418).

**9.4.1 Pairwise undirected graphs** (p. 418). Same equations as §9.3.2 but with no natural node order, so updates are done in parallel ("systolic array"). Initialise all messages to all-ones vectors. Each node absorbs messages, then sends:
$$\mathrm{bel}_s(z_s)\propto\psi_s(z_s)\prod_{t\in\mathrm{nbr}_s}m_{t\to s}(z_s)\tag{9.66}$$
$$m_{s\to t}(z_t)=\sum_{z_s}\Big(\psi_s(z_s)\psi_{st}(z_s,z_t)\prod_{u\in\mathrm{nbr}_s\setminus t}m_{u\to s}(z_s)\Big)\tag{9.67}$$
If the graph is a tree, convergence is guaranteed after $D(G)$ iterations, the diameter (largest distance between two nodes) (p. 418).

**9.4.2 Factor graphs** (pp. 418–419). Bipartite factor graph (variables and factors), following [KFL01]. Variables to factors, and factors to variables (Fig. 9.10):
$$m_{x\to f}(x)=\prod_{h\in\mathrm{nbr}(x)\setminus\{f\}}m_{h\to x}(x)\tag{9.68}$$
$$m_{f\to x}(x)=\sum_{\mathbf x'}f(x,\mathbf x')\prod_{x'\in\mathrm{nbr}(f)\setminus\{x\}}m_{x'\to f}(x')\tag{9.69}$$
Beliefs at convergence:
$$\mathrm{bel}(x)\propto\prod_{f\in\mathrm{nbr}(x)}m_{f\to x}(x)\tag{9.70}$$
Message order can come from heuristics such as a spanning tree with arbitrary root, adaptive *residual BP*, or fully parallel asynchronous implementations (p. 419).

**9.4.3 Gaussian BP** (pp. 419–421). Uses the linear-Gaussian calculus (§2.3.3). Computing a posterior mean in a linear-Gaussian system is equivalent to solving a linear system, so these methods also serve linear algebra (p. 419).

*Example: 1d interpolation* (p. 420). Unknown $f:\mathbb R\to\mathbb R$, $N$ noisy measurements $y_i$ at $x_i$, estimate $z_i=f(g_i)$ on $G$ grid points. With $x_i$ the measurement location closest to $g_i$:
$$\psi_i(z_{i-1},z_i)=\tfrac1{\sigma^2}(\hat y_i-y_i)^2,\quad\hat y_i=(1-\gamma_i)z_{i-1}+\gamma_iz_i,\quad\gamma_i=\frac{x_i-g_i}{g_i-g_{i-1}}\tag{9.71–9.73}$$
($\hat y_i$ is the predicted measurement.) A smoothness term encodes that $z_i$ is close to its neighbours:
$$\phi_i(z_{i-1},z_i)=\tfrac1{\tau^2}\delta_i^2,\quad\delta_i=z_i-z_{i-1}\tag{9.74–9.75}$$
$$p(\mathbf z|\mathbf x,\mathbf y,\mathbf g,\sigma^2,\tau^2)\propto\prod_{i=1}^{G}\psi_i(z_{i-1},z_i)\phi_i(z_{i-1},z_i)\tag{9.76}$$
For sine-wave data (Fig. 9.11), the model is a linear-Gaussian chain, so the posterior marginals from Gaussian BP are exact. It recovers the sine shape from the smoothness prior (p. 420). Extensions: non-linear Gaussian potentials via extended Kalman filter or moment matching (sigma points) generalised from chains to factor graphs; non-Gaussian via non-parametric or particle BP (p. 421).

**9.4.4 Convergence** (pp. 421–423). LBP may not converge, or may converge slowly (p. 421).

*9.4.4.1 When?* The tool is the *computation tree* (Fig. 9.12), which unrolls the messages passed over time. The key insight: $T$ iterations of LBP are equivalent to exact computation on a computation tree of height $T+1$. If the connection strengths on the edges are sufficiently weak, the leaves' influence on the root diminishes over time and convergence will occur (details in [MK05; WJ08]) (p. 421).

*9.4.4.2 Making LBP converge.* *Damping*, with factor $0\le\lambda\le1$ ($\lambda=1$ is the standard scheme; $\lambda\sim0.5$ is standard practice):
$$m^k_{t\to s}(x_s)=\lambda\,m_{t\to s}(x_s)+(1-\lambda)\,m^{k-1}_{t\to s}(x_s)\tag{9.77}$$
where $m_{t\to s}$ is the undamped message (p. 422). Fig. 9.13 (11×11 Ising grid, $w_{ij}\sim\mathrm{Unif}(-C,C)$, $C=11$): per the caption, damped asynchronous updating converges for all nodes, undamped asynchronous for about half, damped synchronous for few. *Double-loop algorithms* are guaranteed to converge to a local minimum of the objective LBP minimises, but are slow and complicated, and the marginals are usually not much more accurate. Oscillating marginals are sometimes a sign that the LBP approximation itself is poor (p. 422).

*9.4.4.3 Adaptive scheduling* (p. 423). *Synchronous* updates (all messages from old messages; analogous to Jacobi's method):
$$\mathbf m^{k+1}_{1:E}=(f_1(\mathbf m^k),\dots,f_E(\mathbf m^k))\tag{9.78}$$
*Asynchronous*, Gauss–Seidel-style updates in a fixed order, using new messages from earlier edges and old ones from later edges:
$$\mathbf m^{k+1}_i=f_i\big(\{\mathbf m^{k+1}_j:j<i\},\{\mathbf m^k_j:j>i\}\big)\tag{9.79}$$
Gauss–Seidel is known to converge faster for linear systems. Fig. 9.13 shows damped asynchronous updating converging more often than synchronous. *Residual BP* [EMK06] sends messages in order of the residual
$$r(s,t,k)=\|\log m_{s\to t}-\log m^k_{s\to t}\|_\infty=\max_j\Big|\log\frac{m_{s\to t}(j)}{m^k_{s\to t}(j)}\Big|\tag{9.80}$$
using a priority queue. After sending $m_{s\to t}$, messages $m_{t\to u}$, $u\in\mathrm{nbr}(t)\setminus s$, are recomputed and re-queued. [EMK06] showed experimentally that it converges more often and much faster than synchronous or fixed-order asynchronous updating. [SM07] bound the residual instead of computing it, about five times faster with similar final quality (p. 423).

**9.4.5 Accuracy** (pp. 423–424). On a single-loop graph, max-product LBP finds the correct MAP if it converges [Wei00]. For general graphs, error bounds on the marginals exist. For Gaussian models, if the method converges, the means are exact but the variances are not (beliefs typically overconfident) (pp. 423–424).

**9.4.6 Generalized BP** (p. 424). Clustering nodes that form tight loops (the cluster variational method) yields a hyper-graph (hyper-edges join sets of vertices), drawn as a poset diagram with arrow $e_1\to e_2$ if $e_2\subset e_1$ (Fig. 9.14). If the largest hyper-edge is allowed to be as large as the graph's treewidth, the hyper-graph can be a tree and the method is exact. This defines a continuum from LBP to exact inference (p. 424).

**9.4.7 Convex BP** (p. 424). The variational view (Supp. §10.4.3) shows the LBP optimisation problem, standard or generalised, is non-convex. A convex BP version will always converge (Supp. §10.4.4) (p. 424).

**9.4.8 Application: error-correcting codes** (pp. 424–426). Pearl proposed LBP in 1988 as a heuristic. The main impetus came when McEliece, MacKay and Cheng [MMC98] showed that turbocodes can be viewed as LBP on a certain graph (p. 425). The receiver infers the sent message $\mathbf x\in\{0,1\}^m$ from noisy $\mathbf y$: $\mathbf x^*=\arg\max_{\mathbf x}p(\mathbf x|\mathbf y)$. The model is a factor graph with parity constraints. A graph where each bit connects to $n$ factors and each factor to $k$ bits is an $(n,k)$ code (Fig. 9.15a: (2,3)). Parity factor:
$$\psi_{stu}(x_s,x_t,x_u)\triangleq\begin{cases}1&\text{if }x_s\otimes x_t\otimes x_u=1\\0&\text{otherwise}\end{cases}\tag{9.81}$$
($\otimes$ = xor.) If the degrees stay bounded as blocklength $m$ grows, it is a low-density parity check (LDPC) code. Random LDPC graphs are "locally tree-like": cycles have length $\sim\log m$, which is important to LBP's success. Per the Fig. 9.15 caption this is not the full explanation, since some code graphs have short loops. Such methods approach the lower bound in Shannon's channel coding theorem and are widely used, e.g. in cellphones (pp. 425–426).

**9.4.9 Application: affinity propagation** (pp. 426–427). A clustering method, an improvement on K-medoids, taking a pairwise similarity matrix as input. Each datapoint $i$ picks an exemplar $c_i\in\{1,\dots,N\}$. Some points choose themselves, which determines the number of clusters. Objective:
$$J(\mathbf c)=\sum_{i=1}^{N}S(i,c_i)+\sum_{k=1}^{N}\delta_k(\mathbf c)\tag{9.82}$$
$$\delta_k(\mathbf c)=\begin{cases}-\infty&\text{if }c_k\ne k\text{ but }\exists i:c_i=k\\0&\text{otherwise}\end{cases}\tag{9.83}$$
The penalty forbids choosing $k$ as exemplar unless $k$ chooses itself (p. 426). The factor graph (Fig. 9.16) has $N$ variables $c_i$ with $N$ states each (an $N^2$ binary-node version also exists). Max-product LBP finds a strong local maximum. Messages reduce to scalars: the *responsibility* $r_{i\to k}$ (how much $i$ thinks $k$ would be a good exemplar compared with the others $i$ has looked at) and the *availability* $a_{i\leftarrow k}$ (how strongly $k$ believes it should be an exemplar for $i$). It may oscillate, but with damping it is very reliable in practice. Cost: $O(N^2)$ if dense, $O(E)$ for sparse similarities (E = number of non-zero entries of $S$). The number of clusters is controlled by scaling the diagonal $S(i,i)$. In Fig. 9.17 (negative Euclidean distance, $S(i,i)$ = median similarity) the result is 3 clusters. [FD07a] report that it significantly outperforms K-medoids (p. 427).

**9.4.10 Emulating BP with GNNs** (pp. 427–428). PGM messages use fixed, non-learned update equations that work for any model, needing only the graph, parameters and evidence. GNNs are instead trained on labelled input–output pairs. [Yoo+18; Zha+19d] show that a GNN trained on exact marginals of a small PGM can work quite well on a test PGM of similar structure. *Deep unfolding* unrolls BP into a layered network, trained discriminatively for an end task, with BP only providing the architecture. These are useful when the PGM and the observed set of nodes are fixed and inference is repeated, an example of amortized inference (p. 428).

### 9.5 Variable elimination (pp. 428–433)
VE computes $p(\mathbf z_Q|\mathbf y)$ for any query set $Q$. Unlike loopy BP, it is guaranteed to give correct answers even when the graph has cycles. Discrete hidden nodes are assumed (p. 428).

**9.5.1 Derivation** (pp. 428–430). Example: the student network (§4.2.2.2), 8 binary variables, target $p(J)$. Brute-force enumeration over the other 7 variables costs $O(2^7)$:
$$p(J)=\sum_{L}\sum_S\sum_G\sum_H\sum_I\sum_D\sum_C p(C,D,I,G,S,L,J,H)\tag{9.84}$$
Better: push sums inside products (also called bucket elimination; "peeling" for pedigree trees) (p. 428). With the factorised joint (p. 429):
$$p(J)=\sum_{L,S}\psi_J(J,L,S)\sum_G\psi_L(L,G)\sum_H\psi_H(H,G,J)\sum_I\psi_S(S,I)\psi_I(I)\times\sum_D\psi_G(G,I,D)\sum_C\psi_C(C)\psi_D(D,C)$$
Evaluate right to left (Table 9.1):
$$\tau'_1(C,D)=\psi_C(C)\psi_D(D,C)\tag{9.85}$$
$$\tau_1(D)=\sum_C\tau'_1(C,D)\tag{9.86}$$
$$\tau'_2(G,I,D)=\psi_G(G,I,D)\tau_1(D)\tag{9.87}$$
$$\tau_2(G,I)=\sum_D\tau'_2(G,I,D)\tag{9.88}$$
and so on, through $\tau_3(G,S)$, $\tau_4(G,J)$, $\tau_5(J,L,S)$, $\tau_6(J,L)$, to $\tau_7(J)$ (Table 9.1, p. 430). Any marginal (e.g. $p(J)$, $p(J,H)$) can be computed this way. A conditional is a ratio of two marginals with visible variables clamped (p. 430):
$$p(J=j|I=1,H=0)=\frac{p(J=j,I=1,H=0)}{\sum_{j'}p(J=j',I=1,H=0)}\tag{9.89}$$

*Intuition note.* Summing a variable out only touches the factors that mention it. Each sum creates a new table $\tau$ that stands in for the eliminated variable.

**9.5.2 Complexity of VE** (pp. 430–432). Running time is exponential in the size of the largest factor, and some factors are new ones created by summation (e.g. a factor on G, I, S in Table 9.1). The *elimination order* matters: for Table 9.1's order the largest created factor has size 3 ($\tau_5(J,L,S)$); for Table 9.2's order ($G,I,S,L,H,C,D$) the largest are $\tau_1(I,D,L,J,H)$ and $\tau_2(D,L,S,J,H)$, much bigger (p. 430). Running VE "symbolically": eliminating $z_t$ connects all variables sharing a factor with it. The added edges are *fill-in edges* (Fig. 9.18; eliminating $I$ links $G$ and $S$ for)
$$\tau'_3(G,S,I)=\psi_S(S,I)\psi_I(I)\tau_2(G,I)\tag{9.90}$$
(p. 431). Let $\mathcal G_\prec$ be the undirected graph induced by elimination order $\prec$. The temporary factors correspond to its maximal cliques; for order $(C,D,I,H,G,S,L)$:
$$\{C,D\},\{D,I,G\},\{G,L,S,J\},\{G,J,H\},\{G,I,S\}\tag{9.91}$$
With $K$ states per variable the time is
$$\sum_{c\in\mathcal C(\mathcal G_\prec)}K^{|c|}\tag{9.92}$$
(p. 431). The *induced width* $w_\prec$ = largest clique in the induced graph minus 1, so VE costs $O(K^{w_\prec+1})$. The smallest possible induced width is the graph's *treewidth*. Finding the optimal elimination order is NP-complete (p. 432).

**9.5.3 Picking a good order** (p. 432). Cost exponential in treewidth also applies to Cholesky of sparse matrices and einsum contractions. A *perfect elimination ordering* adds no fill-in edges. Every already-triangulated graph (e.g. a tree) has one; such graphs are *decomposable*. Otherwise fill-in edges are needed. The greedy **min-fill** heuristic eliminates a node with no fill-ins, else the node causing the fewest; **min-weight** handles different numbers of states. Other methods mentioned: simulated annealing (sometimes better, much slower), continuous relaxation, randomised approximation, nested dissection (within $O(\log N)$ of optimal), constant-factor approximations, approximate minimum degree (AMD), and METIS for large graphs. For a planar graph with $N$ nodes the text states a treewidth of "optimal size $O(N^{3/2})$" (p. 432).

**9.5.4 Complexity of exact inference** (pp. 432–433). VE takes $O(NK^{w+1})$; for a dense graph $w=O(N)$, so exponential in $N$ (p. 432). Exact inference in discrete graphical models is NP-hard [DL93], by reduction from satisfiability. A 3-SAT problem is encoded as a directed model with deterministic links (Fig. 9.19). Clamp the final node $x$ on and arrange the CPTs so that $p(x=1)>0$ iff there is a satisfying assignment. Any posterior marginal needs $p(x=1)$, so inference solves SAT. Exact inference is even #P-hard [Rot96], intuitively because computing the normaliser means counting satisfying assignments. MAP estimation is provably easier for some model classes since, intuitively speaking, it only needs one satisfying assignment, not counting all of them. Even approximate inference is hard in general. With continuous hidden variables it can be harder still (e.g. a two-node $z\to y$ without a conjugate relation), and mixed discrete–continuous inference can also be hard. Consequently we often have to resort to approximate methods: variational (Ch. 10) and Monte Carlo (Ch. 11) (p. 433).

**9.5.5 Drawbacks of VE** (pp. 433–434). On a chain, VE for $p(z_T|\mathbf y)$ equals the forwards algorithm, $O(K^2T)$. Getting every marginal by repeated VE costs $O(K^2T^2)$, whereas FB gets all in $O(K^2T)$ because it caches messages and reuses them (caching is the core idea of DP) (pp. 433–434). The same holds on trees (Fig. 9.20): messages used for one marginal are re-used for others, so storing them gives all marginals in $O(K^2T)$ (§9.3). The open question is how to get this when the graph is not a tree (p. 434).

### 9.6 Junction tree algorithm (p. 434)
JTA generalises VE to compute all posterior marginals without redundant work, by DP. Steps: convert the graph to a *junction tree* (join tree / clique tree) and run BP on it. Run VE symbolically (§9.5.2) and add the fill-in edges; the resulting chordal graph is converted to a tree (Supp. §9.2.1); message passing uses a variant of §9.3.2 (Supp. §9.2.2). This unit gives no further details (p. 434).

### 9.7 Inference as optimization (pp. 435–437)
**9.7.1 Inference as backpropagation** (p. 435). For an undirected model written as an exponential family:
$$p(\mathbf x)=\tfrac1Z\prod_c\psi_c(\mathbf x_c)=\exp\Big(\sum_c\boldsymbol\eta_c^{\mathsf T}\mathcal T(\mathbf x_c)-\log A(\boldsymbol\eta)\Big)=\exp(\boldsymbol\eta^{\mathsf T}\mathcal T(\mathbf x)-\log A(\boldsymbol\eta))\tag{9.93}$$
$\boldsymbol\eta_c$: natural parameters; $\mathcal T$: sufficient statistics; $A=\log Z$ the log partition function. For discrete pairwise models, $\boldsymbol\eta=(\{\eta_{s;j}\},\{\eta_{s,t;j,k}\})$ are the log potentials and $\mathcal T$ the node and edge indicators. The mean of the sufficient statistics:
$$\boldsymbol\mu=\mathbb E[\mathcal T(\mathbf x)]=(\{p(x_s=j)\}_s,\{p(x_s=j,x_t=k)\}_{s\ne t})=(\{\mu_{s;j}\},\{\mu_{st;jk}\})\tag{9.94}$$
By Eq. (2.236), $\boldsymbol\mu=\nabla_{\boldsymbol\eta}A(\boldsymbol\eta)$. So given a function computing $A(\boldsymbol\eta)=\log Z(\boldsymbol\eta)$, automatic differentiation gives the gradient, from which node marginals are read. Evidence is handled by clamping entries to 0 or 1 in the node potentials. Several groups found this independently (p. 435).

*9.7.1.1 Example* (pp. 435–436). Chain $x_1-x_2-x_3$, $K$ states each; node potentials are $K\times1$ tensors, edge potentials $K\times K$:
$$Z(\boldsymbol\psi)=\sum_{x_1,x_2,x_3}\psi_1(x_1)\psi_2(x_2)\psi_3(x_3)\psi_{12}(x_1,x_2)\psi_{23}(x_2,x_3)\tag{9.95}$$
With $\boldsymbol\eta=\log\boldsymbol\psi$: $\boldsymbol\mu_s=\nabla_{\boldsymbol\eta_s}A(\boldsymbol\eta)$ and $\boldsymbol\mu_{s,t}=\nabla_{\boldsymbol\eta_{s,t}}A(\boldsymbol\eta)$. $Z$ is computed with `einsum` (tensor contraction), and two lines of JAX give the marginals (Listing 9.1: `logZ_fun` via `einsum("A,B,C,AB,BC", ...)`, then `grad`). For conditional inference ($p(x_s=k|x_t=e)$), multiply in one-hot indicators to clamp $x_t=e$, sum over the unclamped variables to get $Z_e$; its gradients give marginals given the evidence (p. 436).

*Intuition note.* The derivative of $\log Z$ with respect to a log-potential entry equals the probability of that entry, so any tool that can differentiate a $\log Z$ routine returns marginals.

**9.7.2 Perturb and MAP** (p. 436). To sample from a posterior using an optimiser: make $S$ copies of the model with perturbed parameters $\boldsymbol\theta_s=\boldsymbol\theta+\boldsymbol\epsilon_s$, and take $\mathbf x_s=\arg\max p(\mathbf x|\mathbf y;\boldsymbol\theta_s)$. For a suitably chosen noise distribution, this is perturb-and-MAP and can give exact posterior samples [PY10; PY11; PY14].

*9.7.2.1 Gaussian case* (pp. 436–437). Prior with $\mathbf G\in\mathbb R^{K\times N}$ (prior dependencies):
$$p(\mathbf x)\propto\mathcal N(\mathbf G\mathbf x|\boldsymbol\mu_p,\boldsymbol\Sigma_p)\propto\exp(-\tfrac12\mathbf x^{\mathsf T}\mathbf K_x\mathbf x+\mathbf h_x^{\mathsf T}\mathbf x)\tag{9.96}$$
$\mathbf K_x=\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\mathbf G$, $\mathbf h_x=\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\boldsymbol\mu_p$. Likelihood with $\mathbf H\in\mathbb R^{M\times N}$:
$$p(\mathbf y|\mathbf x)=\mathcal N(\mathbf y|\mathbf H\mathbf x+\mathbf c,\boldsymbol\Sigma_n)\propto\exp(-\tfrac12\mathbf x^{\mathsf T}\mathbf K_{y|x}\mathbf x+\mathbf h_{y|x}^{\mathsf T}\mathbf x-\tfrac12\mathbf y^{\mathsf T}\boldsymbol\Sigma_n^{-1}\mathbf y)\tag{9.97}$$
$\mathbf K_{y|x}=\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}\mathbf H$, $\mathbf h_{y|x}=\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}(\mathbf y-\mathbf c)$. Posterior (assuming $\mathbf K=\mathbf K_x+\mathbf K_{y|x}$ invertible):
$$p(\mathbf x|\mathbf y)=\mathcal N(\mathbf x|\boldsymbol\mu,\boldsymbol\Sigma)\tag{9.98}$$
$$\boldsymbol\Sigma^{-1}=\mathbf K=\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\mathbf G+\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}\mathbf H\tag{9.99}$$
$$\boldsymbol\mu=\mathbf K(\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\boldsymbol\mu_p+\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}(\mathbf y-\mathbf c))\ \text{[as printed; see Reading notes]}\tag{9.100}$$
Rows of $\mathbf G$ and $\mathbf H$ combine into the $L$ rows $\mathbf f_l^{\mathsf T}$ of $\mathbf F$. If $\boldsymbol\Sigma_p,\boldsymbol\Sigma_n$ are diagonal, the graph structure is determined by the sparsity of $\mathbf F$, and the posterior is a product of $L$ Gaussian "experts":
$$p(\mathbf x|\mathbf y)\propto\prod_{l=1}^{L}\exp(-\tfrac12\mathbf x^{\mathsf T}\mathbf K_l\mathbf x+\mathbf h_l^{\mathsf T}\mathbf x)\propto\prod_{l=1}^{L}\mathcal N(\mathbf f_l^{\mathsf T}\mathbf x;\mu_l,\Sigma_l)\tag{9.101}$$
with $\Sigma_l=\Sigma_{p,l,l}$, $\mu_l=\mu_{p,l}$ for $l\le K$, and $\Sigma_l=\Sigma_{n,l',l'}$, $\mu_l=y_{l'}-c_{l'}$ for $l>K$, $l'=l-K$ (p. 437).

Procedure: sample $\tilde{\boldsymbol\mu}_p\sim\mathcal N(\boldsymbol\mu_p,\boldsymbol\Sigma_p)$ and $\tilde{\mathbf y}\sim\mathcal N(\mathbf y,\boldsymbol\Sigma_n)$ (equivalent to perturbing each information-form linear term, $\tilde{\mathbf h}_l=\mathbf h_l+\mathbf f_l\Sigma_l^{-1/2}\epsilon_l$, $\epsilon_l\sim\mathcal N(0,1)$). Then compute the MAP (posterior mean) with the perturbed parameters:
$$\tilde{\mathbf x}=\mathbf K^{-1}\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\tilde{\boldsymbol\mu}_p+\mathbf K^{-1}\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}(\tilde{\mathbf y}-\mathbf c)\tag{9.102}$$
$$=\underbrace{\mathbf K^{-1}\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}}_{\mathbf A}(\boldsymbol\mu_p+\boldsymbol\epsilon_\mu)+\underbrace{\mathbf K^{-1}\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}}_{\mathbf B}(\mathbf y+\boldsymbol\epsilon_y-\mathbf c)\tag{9.103}$$
$$=\boldsymbol\mu+\mathbf A\boldsymbol\epsilon_\mu+\mathbf B\boldsymbol\epsilon_y\tag{9.104}$$
The author states $\mathbb E[\tilde{\mathbf x}]=\boldsymbol\mu$ and $\mathbb E[(\tilde{\mathbf x}-\boldsymbol\mu)(\tilde{\mathbf x}-\boldsymbol\mu)^{\mathsf T}]=\mathbf K^{-1}=\boldsymbol\Sigma$, so the method produces exact samples. *(added step)* The covariance follows from $\boldsymbol\epsilon_\mu\sim\mathcal N(0,\boldsymbol\Sigma_p)$, $\boldsymbol\epsilon_y\sim\mathcal N(0,\boldsymbol\Sigma_n)$ independent: $\mathbf A\boldsymbol\Sigma_p\mathbf A^{\mathsf T}+\mathbf B\boldsymbol\Sigma_n\mathbf B^{\mathsf T}=\mathbf K^{-1}(\mathbf G^{\mathsf T}\boldsymbol\Sigma_p^{-1}\mathbf G+\mathbf H^{\mathsf T}\boldsymbol\Sigma_n^{-1}\mathbf H)\mathbf K^{-1}=\mathbf K^{-1}$. The method is very scalable since MAP for sparse GMRFs (Gaussian Markov random fields) can use conjugate gradient solvers; alternatively LBP can often compute the exact posterior mean (p. 437).

*9.7.2.2 Discrete case* (p. 437). [PY11; PY14] extend this using Gumbel noise, $\epsilon=-\log(-\log u)$, $u\sim\mathrm{Unif}(0,1)$. Ideally it is added to all potentials; as a simple approximation, only to the unary (local evidence) terms. For a pairwise CRF the score is
$$S(\mathbf x;\mathbf c)=\log p(\mathbf x|\mathbf c)+\text{const}=\sum_i\log\phi_i(x_i)+\sum_{ij}\log\psi_{ij}(x_{i,j})\tag{9.105}$$
Perturb each entry $\phi_i(k)$ by adding $\epsilon_{ik}$, get $\tilde S$, and sample $\tilde{\mathbf x}=\arg\max\tilde S(\mathbf x;\mathbf c)$. This can use efficient MAP solvers for discrete models (Supp. §9.3), and can be used for parameter learning and partition-function estimation (p. 437).

## Toy example (ours, not from the text)
A 2-step HMM, $K=2$ states, to check forwards-backwards and Viterbi by hand. $\pi=(0.5,0.5)$; $\mathbf A=\begin{pmatrix}0.8&0.2\\0.4&0.6\end{pmatrix}$. The two observations give local evidence $\boldsymbol\lambda_1=(0.9,0.2)$ and $\boldsymbol\lambda_2=(0.1,0.6)$.

*Forwards.* $\pi\odot\boldsymbol\lambda_1=(0.45,0.10)$, $Z_1=0.55$, so $\boldsymbol\alpha_1=(9/11,2/11)\approx(0.818,0.182)$.
Predict: $\alpha_{2|1}(1)=0.8\cdot\tfrac9{11}+0.4\cdot\tfrac2{11}=\tfrac{7.2+0.8}{11}=\tfrac8{11}$; $\alpha_{2|1}(2)=0.2\cdot\tfrac9{11}+0.6\cdot\tfrac2{11}=\tfrac{1.8+1.2}{11}=\tfrac3{11}$.
Update: $\boldsymbol\lambda_2\odot\boldsymbol\alpha_{2|1}=(0.8/11,\,1.8/11)$, $Z_2=2.6/11$, so $\boldsymbol\alpha_2=(4/13,9/13)\approx(0.308,0.692)$.
Check: $Z_1Z_2=0.55\cdot2.6/11=0.13=p(y_1,y_2)$.

*Backwards.* $\boldsymbol\beta_2=(1,1)$. $\beta_1(1)=0.8\cdot0.1+0.2\cdot0.6=0.20$; $\beta_1(2)=0.4\cdot0.1+0.6\cdot0.6=0.40$.
$\boldsymbol\gamma_1\propto(\tfrac9{11}\cdot0.2,\ \tfrac2{11}\cdot0.4)=(1.8,0.8)/11$, so $\boldsymbol\gamma_1=(9/13,4/13)$; $\boldsymbol\gamma_2=\boldsymbol\alpha_2=(4/13,9/13)$.

*Brute force check.* $p(z_1,z_2,y_{1:2})=\pi(z_1)\lambda_1(z_1)A_{z_1z_2}\lambda_2(z_2)$: (1,1) $=0.5\cdot0.9\cdot0.8\cdot0.1=0.036$; (1,2) $=0.5\cdot0.9\cdot0.2\cdot0.6=0.054$; (2,1) $=0.5\cdot0.2\cdot0.4\cdot0.1=0.004$; (2,2) $=0.5\cdot0.2\cdot0.6\cdot0.6=0.036$. Sum $=0.130$. Then $p(z_1=1|\mathbf y)=0.09/0.13=9/13$ ✓ and $p(z_2=1|\mathbf y)=0.04/0.13=4/13$ ✓.

*Viterbi.* $\delta_1=(0.45,0.10)$. $\delta_2(1)=0.1\cdot\max(0.45\cdot0.8,\,0.10\cdot0.4)=0.1\cdot0.36=0.036$. $\delta_2(2)=0.6\cdot\max(0.45\cdot0.2,\,0.10\cdot0.6)=0.6\cdot0.09=0.054$. Since $\delta_2(2)>\delta_2(1)$, $z_2^*=2$, $a_2(2)=1$, so the MAP path is $(1,2)$ with joint probability 0.054, equal to the brute-force entry (1,2).

## Concepts
- [[belief-propagation]] — local messages between neighbouring nodes/cliques that let nodes agree on global marginals; exact on trees (pp. 401, 415) (new)
- [[dynamic-programming]] — solve subproblems and combine; here, caching messages for reuse (pp. 401, 434) (new)
- [[hidden-markov-model]] — chain model with discrete latent states and per-state observation distributions, eq. (9.1) (p. 402) (new)
- [[filtering-and-smoothing]] — filtering $p(z_t|y_{1:t})$ (forwards) vs smoothing $p(z_t|y_{1:T})$ (all data) (pp. 403–404) (new)
- [[forwards-backwards-algorithm]] — $\gamma_t\propto\alpha_t\odot\beta_t$ with backward recursion (9.18) (pp. 404–405) (new)
- [[viterbi-algorithm]] — max-product version of the forwards pass plus traceback; finds the MAP path (pp. 409–410) (new)
- [[sum-product-algorithm]] — tree BP: upward collect, downward distribute, eqs. (9.58)–(9.62) (pp. 414–415) (new)
- [[max-product-algorithm]] — sum replaced by max, giving max marginals (p. 416) (new)
- [[mpm-vs-map]] — per-node posterior-marginal maximiser vs jointly most probable configuration; which is better depends on the loss (pp. 416–417) (new)
- [[loopy-belief-propagation]] — the same updates run in parallel on cyclic graphs; approximate, may not converge (pp. 417–418) (new)
- [[computation-tree]] — unrolled message history; $T$ iterations of LBP equal exact inference on a tree of height $T+1$ (p. 421) (new)
- [[damping-and-residual-bp]] — partial message updating (9.77) and priority scheduling by residual (9.80) (pp. 422–423) (new)
- [[factor-graph]] — bipartite graph of variables and factors; carries higher-order potentials and parity constraints (pp. 418, 425) (new)
- [[variable-elimination]] — sum out variables one at a time, creating intermediate factors $\tau$ (pp. 428–430) (new)
- [[treewidth]] — smallest induced width over elimination orders; VE costs $O(K^{w+1})$ (p. 432) (new)
- [[junction-tree-algorithm]] — build clique tree from VE fill-in edges, run BP on it (p. 434) (new)
- [[inference-as-autodiff]] — marginals equal the gradient of $\log Z$ w.r.t. log potentials (p. 435) (new)
- [[perturb-and-map]] — draw posterior samples by MAP solves on noise-perturbed parameters (p. 436) (new)
- [[marginal-likelihood]] — here $Z_t=p(y_t|y_{1:t-1})$, the filtering normaliser (p. 404)
- [[posterior-distribution]] — here marginals/pairwise marginals $p(z_t|\mathbf y)$, $\xi_{t,t+1}$ (p. 403)

## Canonical instances
- [[casino-hmm]] — fair/loaded die HMM used to show filtering, smoothing, Viterbi, MPM vs MAP error counts (pp. 402–404, 417)
- [[viterbi-speech-example]] — 3-state, 7-symbol HMM with δ values 0.045, 0.07; MAP path 1,2,2,3 (pp. 410–411)
- [[parity-code-mpm-counterexample]] — 3-bit parity model where MPM gives a non-codeword (pp. 416–417)
- [[gaussian-bp-1d-interpolation]] — noisy sine data on a grid, exact beliefs (pp. 420–421)
- [[ising-grid-lbp]] — 11×11 grid showing effects of damping and scheduling (p. 422)
- [[ldpc-turbocode-lbp]] — LDPC factor graphs and LBP decoding (pp. 425–426)
- [[affinity-propagation]] — exemplar clustering by max-product LBP (pp. 426–427)
- [[student-network-ve]] — VE on the 8-variable student network, two elimination orders (pp. 428–431)
- [[3sat-as-graphical-model]] — reduction showing exact inference is NP-hard (p. 433)

## Bridges (candidates)
- [structural-analogy] forwards-backwards on a chain ↔ Kalman smoother: both are message passing on a chain (the text says both can be so interpreted, p. 412).
- [same-math] Viterbi / max-product ↔ shortest-path search: MAP is a shortest path in the trellis with log-probability weights (p. 409).
- [same-math] Gaussian BP posterior mean ↔ numerical linear algebra: computing the mean equals solving a linear system (p. 419).
- [structural-analogy] synchronous vs asynchronous LBP ↔ Jacobi vs Gauss–Seidel iterations for linear systems (p. 423).
- [structural-analogy] VE cost exponential in treewidth ↔ sparse Cholesky and einsum contraction cost (p. 432).
- [same-math] marginals as $\nabla_\eta\log Z$ ↔ exponential families: mean of sufficient statistics equals gradient of the log partition (p. 435).
- [structural-analogy] BP message updates ↔ graph neural network layers (deep unfolding, p. 428).

## Questions this raises
- When does damped or scheduled LBP give accurate marginals, and can one tell from the run itself (e.g. from oscillation) that the approximation is poor? (p. 422)
- How does the junction tree algorithm use the fill-in edges and cliques to define messages, and what is its cost relative to a single VE run? (p. 434)
- How good must the noise distribution in discrete perturb-and-MAP be, given that Gumbel noise is only added to unary terms as an approximation? (p. 437)
- How do the variational views of LBP, generalised BP and convex BP (Supp. §10.4) explain the convergence behaviour seen here? (p. 424)

## Reading notes
- Printed page = pdf page − 34. pdf 472 (printed 438) is blank. Running footer: "Probabilistic Machine Learning: Advanced Topics", online version, December 10, 2025. Chapter 9 sections 9.1–9.7 are covered. The Supplementary sections (9.1.1, 9.2, 9.3, 10.4) are only referenced.
- The text layers of pdf 453 and 461 were garbled (scanned figures); the page images were used.
- No exercises are printed in this unit.
- Probable misprints (as seen in images):
  - p. 403: "(TK²) time" lacks the "O".
  - p. 407: "state conditional log likelihoods λ_t(j)" should read ℓ_t(j) given the preceding sentence.
  - p. 408 (9.34): the denominator is typeset as $p(z_{t+1=j}|y_{1:t})$.
  - p. 421 (Fig. 9.12 caption): "higher degree than nodes 1 and 2" seems to mean nodes 1 and 4 (nodes 2 and 3 have degree 3 in the drawn graph).
  - p. 436: "θ_s = θ_s + ε_s" should be θ + ε_s.
  - p. 437 (9.100): $\boldsymbol\mu=\mathbf K(\dots)$ lacks the inverse; (9.102)–(9.104) use $\mathbf K^{-1}$ and $\boldsymbol\Sigma=\mathbf K^{-1}$.
  - p. 436 (Listing 9.1): the code uses `np.log` but imports only `jax.numpy as jnp`.
  - p. 432: the planar-graph treewidth "O(N^{3/2})" exceeds N−1, the largest possible value under the chapter's definition (largest clique minus 1), so the printed bound looks implausible as a treewidth.
  - p. 422 (Fig. 9.13): the in-figure legend (Synchronous / Asynchronous / No smoothing / True) is worded differently from the caption; the caption's description was used.
  - p. 420 (9.71), (9.74): printed as quadratic penalties without a negative exponential, although the text calls them potentials.

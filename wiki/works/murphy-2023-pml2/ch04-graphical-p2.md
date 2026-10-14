---
id: murphy-2023-pml2/ch04-graphical-p2
work: murphy-2023-pml2
unit: "4 Graphical models (part 2/3): end of 4.2.8, 4.3 Undirected graphical models, 4.4 CRFs (to 4.4.3.1)"
pages: 164-193
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Undirected graphical models (MRFs) and conditional random fields

## L0 — One line
When edge directions are unnatural, define a joint distribution as a normalised product of clique potentials (an MRF or energy-based model); this makes conditional independence easy to read, but the partition function makes learning and inference costly.

## L1 — The gist (≤ 120 words)
This part of Chapter 4 finishes directed models (naive Bayes, tree-augmented variants) and then develops undirected models. A Markov random field replaces conditional probability tables by clique potentials, normalised by a partition function. The unit covers special cases (Ising, Potts, Hopfield, Boltzmann machines, maxent, Gaussian MRFs), how conditional independence is read by simple graph separation, and how parameters are learned, where the partition function makes maximum likelihood costly. It then introduces conditional random fields, which model labels given inputs and are used for sequence labelling, parsing and image tasks.

**Prerequisites:** conditional independence and DAG factorisation; exponential family and log-partition-function gradients; Gaussian precision matrix; maximum likelihood; Gibbs sampling (by name only).

## L2 — Key ideas (5–10 bullets)
- Naive Bayes assumes features are conditionally independent given the class. A tree over the features gives a tree-augmented naive Bayes (TAN) model, and a class-dependent tree gives a Bayesian multinet (p. 164).
- An MRF (an undirected model, also called a UPGM) has one non-negative potential per maximal clique (a largest set of mutually adjacent nodes). For positive distributions, Hammersley–Clifford says the joint is the clique-potential product divided by the partition function $Z$ (pp. 165–166).
- Writing $\psi_c=\exp(-\mathcal E_c)$ gives the Gibbs/energy-based form. Ising, Potts, Hopfield, Boltzmann machines and RBMs are special cases with different potentials and graphs (pp. 166–174).
- Log-linear potentials give maximum-entropy (maxent) models. A Gaussian MRF has zeros in its precision matrix (the inverse covariance) at missing edges, while its covariance can be dense (pp. 175–178).
- In UPGMs, conditional independence is read by graph separation. The global, local and pairwise Markov properties coincide for positive densities. A DAG is moralised (co-parents joined, arrows dropped), after taking the ancestral graph (the query nodes and their ancestors), to use this (pp. 179–181).
- MLE needs $\mathbb E_{\text{model}}[\phi]$, which requires sampling from the model at each gradient step. Pseudolikelihood (a product of single-node conditionals) avoids this but has its own failure mode (pp. 183–185).
- A CRF models $p(y|x)$ with a globally normalised MRF over labels. This captures label dependencies and constraints in sequences, parse trees and image grids (pp. 186–193).
- CRF gradients are data features minus expected features under $p(y|x_n,\theta)$, and the objective is convex (p. 193).

## L3 — Walkthrough

### 4.2.8.2 Naive Bayes classifier (p. 164)
Model, with plates for repetition over feature index $d$ (and over cases $n$ when inferring parameters):
$$p(\boldsymbol x,y|\boldsymbol\theta)=p(y|\boldsymbol\pi)\prod_{d=1}^{D}p(x_d|y,\boldsymbol\theta_d)\tag{4.68}$$
Features are conditionally independent given class $y$; this is the "naive" assumption. The model often works surprisingly well and is extremely easy to fit (p. 164). $\theta_{dc}$ depends on $d$ and class $c$, while $x_{nd}$ depends on $n$ and $d$. This is drawn with nested plates sharing the index $d$ (p. 164).

### 4.2.8.3 Relaxing naive Bayes (p. 164)
Edges among the features, forced to form a tree, give the **tree-augmented naive Bayes (TAN)** model. If the tree topology depends on the class value $y$, the model is a **Bayesian multinet**, a supervised mixture of trees (Fig. 4.14, p. 164).

### 4.3 Undirected graphical models: motivation (p. 165)
- A DAG forces an edge direction. For an image, a DAG with 2d lattice topology (a Markov mesh) has conditional independence properties the author calls "rather unnatural" (p. 165).
- An undirected model (UPGM, MRF, Markov network) has no orientations. On a 2d lattice, the Markov blanket of a node is just its nearest neighbours (Fig. 4.15, p. 165).
- Advantages claimed: (1) symmetry, which suits spatial or relational data; (2) discriminative UPGMs (CRFs) work better than discriminative directed models. Disadvantages: (1) parameters are less interpretable and modular; (2) parameter estimation is costlier (p. 165).

### 4.3.1 Representing the joint (pp. 165–166)
There is no topological order, so the chain rule cannot be used. Instead each **maximal clique** $c$ (a clique that cannot be enlarged) gets a potential $\psi_c(\boldsymbol x_c;\boldsymbol\theta_c)$, which can be any non-negative function (p. 165).

**4.3.1.1 Hammersley–Clifford.** Suppose $p$ satisfies the CI properties implied by undirected graph $G$. Then
$$p(\boldsymbol x|\boldsymbol\theta)=\frac{1}{Z(\boldsymbol\theta)}\prod_{c\in\mathcal C}\psi_c(\boldsymbol x_c;\boldsymbol\theta_c)\tag{4.69}$$
$$Z(\boldsymbol\theta)\triangleq\sum_{\boldsymbol x}\prod_{c\in\mathcal C}\psi_c(\boldsymbol x_c;\boldsymbol\theta_c)\tag{4.70}$$
$Z$ (the **partition function**) makes the distribution sum to 1. The theorem holds only for positive distributions ($p>0$ for all $\boldsymbol x$), which rules out some models with hard constraints (p. 166).

**4.3.1.2 Gibbs distribution.** Define $\psi_c=\exp(-\mathcal E(\boldsymbol x_c;\boldsymbol\theta_c))$ (4.73). Then
$$p(\boldsymbol x|\boldsymbol\theta)=\frac{1}{Z(\boldsymbol\theta)}\exp(-\mathcal E(\boldsymbol x;\boldsymbol\theta)),\qquad \mathcal E(\boldsymbol x;\boldsymbol\theta)=\sum_c\mathcal E(\boldsymbol x_c;\boldsymbol\theta_c)\tag{4.71, 4.72}$$
Low energy means high probability. This is also called an **energy-based model** (p. 166).

*Intuition note.* An MRF scores a configuration by multiplying local compatibility factors, and $Z$ turns scores into probabilities. The price is that $Z$ sums over all configurations, which later causes much of the computational trouble.

### 4.3.2 Fully visible MRFs
**4.3.2.1 Ising models (pp. 167–168).** On a 2d lattice: $p(\boldsymbol x|\boldsymbol\theta)=\frac1{Z(\boldsymbol\theta)}\prod_{i\sim j}\psi_{ij}(x_i,x_j;\boldsymbol\theta)$ (4.74), where $i\sim j$ means neighbours. The Ising model has binary spins $x_i\in\{+1,-1\}$ and
$$\psi_{ij}(x_i,x_j;\boldsymbol\theta)=\begin{cases}e^{J_{ij}}&x_i=x_j\\ e^{-J_{ij}}&x_i\neq x_j\end{cases}\tag{4.75}$$
$J_{ij}$ is the coupling strength. Unconnected pairs have $J_{ij}=0$, and $J_{ij}=J_{ji}$. With a common $J$ this is (4.76). In energy form:
$$p(\boldsymbol x|\boldsymbol\theta)=\tfrac1{Z(J)}\exp(-\mathcal E(\boldsymbol x;J)),\qquad \mathcal E(\boldsymbol x;J)=-J\sum_{i\sim j}x_ix_j\tag{4.77, 4.78}$$
This uses $x_ix_j=+1$ if $x_i=x_j$ and $-1$ otherwise (p. 167). Temperature: $J'=J/T$, so colder means larger $J$ and tighter coupling (p. 167).
- $J<0$: antiferromagnetic, with spins wanting to differ. This is a *frustrated* system, since not all neighbours can differ on a 2d lattice. The infinite lattice gives a checkerboard (Fig. 4.16, p. 167–168).
- $J>0$: associative Markov network (ML name) or ferromagnetic model (physics name). Aligned neighbours have lower energy. For $J=1$ the distribution has two modes, all $+1$ and all $-1$, the *ground states* (p. 167).
- Samples (Fig. 4.17, from Gibbs sampling) become clumpier as temperature falls. As lattice size goes to infinity there is a critical value $J_c$ below which many large clusters occur and above which many small clusters occur. For the isotropic square lattice (citing [Geo88]):
$$J_c=\tfrac12\log(1+\sqrt2)\approx0.44\tag{4.79}$$
  The author's wording is "below" and "above", as printed (p. 168). A rapid change of global behaviour is a **phase transition** (p. 168).
- Unary terms ("external field") give $p(\boldsymbol x|\boldsymbol\theta)=\frac1{Z}\prod_i\psi_i(x_i)\prod_{i\sim j}\psi_{ij}$ (4.80). For binary nodes $\psi_i=e^{\alpha}$ if $x_i=+1$, $e^{-\alpha}$ if $x_i=-1$ (4.81). Hence
$$\mathcal E(\boldsymbol x|\boldsymbol\theta)=-\alpha\sum_ix_i-J\sum_{i\sim j}x_ix_j\tag{4.82}$$

**4.3.2.2 Potts models (pp. 169–170).** For $x_i\in\{1,\dots,K\}$: $\psi_{ij}(x_i{=}k,x_j{=}k')=e^{J_{ij}(k,k')}$ (4.83). The common special case is
$$\psi_{ij}=\begin{cases}e^{J}&k=k'\\ e^{0}&k\ne k'\end{cases}\tag{4.84}$$
This is the **Potts model**; it reduces to the Ising model if $J_{\text{potts}}=2J_{\text{ising}}$. For $J>0$ it is associative. The 2d phase transition (citing [MS96]) is
$$J_c=\log(1+\sqrt K)\tag{4.85}$$
Fig. 4.18 uses $K=10$, $J_c=1.426$, and shows $J=1.40,1.43,1.46$. With local evidence:
$$\mathcal E(\boldsymbol x|\boldsymbol\theta)=-\sum_i\sum_{k=1}^K\alpha_k\mathbb I(x_i=k)-J\sum_{i\sim j}\mathbb I(x_i=x_j)\tag{4.86}$$

**4.3.2.3 Potts models for protein structure prediction (p. 170).** The goal is to predict 3d shape from the 1d amino-acid sequence. In **direct coupling analysis (DCA)**:
1. Compute a multiple sequence alignment (MSA) of related sequences from one protein family (e.g. with HMMs). It is an $N\times T$ matrix $\mathbf X$, with $N$ sequences of length $T$ and $X_{ni}\in\{1,\dots,V\}$; $V=21$ is 20 amino acids plus a gap.
2. Fit a Potts model by MLE or an approximation such as pseudolikelihood. A sparsity-promoting MAP prior is also possible (footnote 5).
3. Select the edges with highest $J_{ij}$ ($i,j$ are residues). Highly coupled residues are likely in physical contact, because interacting residues must coevolve. This graph is the **contact map**.
4. Feed the contact map to a 3d structure predictor (e.g. AlphaFold, which won the 2018 CASP competition). Such methods learn $p(d(i,j)\,|\,\{c(i,j)\})$ with neural networks, where $d$ is 3d distance and $c$ the contact map (p. 170).

**4.3.2.4 Hopfield networks (pp. 170–172).** A Hopfield network is a fully connected Ising model with symmetric $\mathbf W=\mathbf W^\top$ and $x_i\in\{-1,+1\}$:
$$\mathcal E(\boldsymbol x)=-\tfrac12\boldsymbol x^\top\mathbf W\boldsymbol x\tag{4.87}$$
Its main use is as an *associative (content-addressable) memory*. Train on fully observed bit vectors, then present a partial pattern and do *pattern completion*: $\boldsymbol x^*=\arg\min_{\boldsymbol x}\mathcal E(\boldsymbol x)$ (4.88). This is solved by **iterative conditional modes (ICM)**, which sets each hidden variable to its most likely state given its neighbours:
$$\boldsymbol x^{t+1}=\operatorname{sgn}(\mathbf Wx^t)\tag{4.89}$$
This is a deterministic version of Gibbs sampling. In Fig. 4.19 (150×150 binary images), 30 ICM iterations recover full images from occluded inputs (p. 171).
Weights can be learned by MLE (4.3.9.1), but a simpler heuristic from [Hop82] is the outer-product method:
$$\mathbf W=\Big(\tfrac1N\sum_{n=1}^N\boldsymbol x_n\boldsymbol x_n^\top\Big)-\mathbf I\tag{4.90}$$
This divides by $N$ and zeroes the diagonal (each $x_nx_n^\top$ has diagonal 1 for $\pm1$ entries, *added step*). It makes the energy low for patterns matching training examples. It also stores inverses and other linear combinations, so memories "collide" beyond a limit. Hopfield proved that for random patterns the capacity is $\sim0.14N$ (p. 172).

### 4.3.3 MRFs with latent variables
- **4.3.3.1 Boltzmann machine** [AHS85] (p. 172): an Ising-like model with latent variables, an arbitrary graph, and states $x_i\in\{0,1\}$. Nodes are split into hidden $\boldsymbol z$ and visible $\boldsymbol x$ (Fig. 4.20a). Fully visible MRFs are limited because correlation can only be modelled by adding an edge.
- **4.3.3.2 RBM** (pp. 172–173): exact inference in a Boltzmann machine is intractable, and even approximate inference can be slow. An RBM restricts the graph to two layers with no within-layer edges. Hidden nodes are then conditionally independent given visible nodes: $p(\boldsymbol z|\boldsymbol x)=\prod_{k=1}^Kp(z_k|\boldsymbol x)$. A directed two-layer model differs: explaining away entangles latents in the posterior even if they are independent in the prior (p. 172).
  - For binary units the energy terms are $w_{dk}x_dz_k$. If $z_k=1$, unit $k$ adds $\boldsymbol w_k^\top\boldsymbol x$ to the energy (a "soft constraint"); if $z_k=0$ it has no opinion. This is a *product of experts*, since $p(\boldsymbol x|\boldsymbol z)\propto\prod_{k:z_k=1}\exp(\boldsymbol w_k^\top\boldsymbol x)$ (p. 173).
  - It acts like a mixture with $2^H$ components, with $\boldsymbol z$ a *distributed* representation. A standard mixture uses a *localist* one, $z\in\{1,K\}$ with $p(\boldsymbol x|z{=}k)\propto\exp(\boldsymbol w_k^\top\boldsymbol x)$ (p. 173).
  - Table 4.4 lists variants by (visible, hidden) type: binary/binary (binary RBM); Gaussian/binary; categorical/binary; multiple categorical/binary (replicated softmax, undirected LDA); Gaussian/Gaussian (undirected PCA); binary/Gaussian (undirected binary PCA). All are special cases of the exponential family harmonium (p. 173).
- **4.3.3.3 Deep Boltzmann machine** (p. 174), with bias terms dropped:
$$p(\boldsymbol x,\boldsymbol z_1,\boldsymbol z_2|\boldsymbol\theta)=\frac1{Z(\mathbf W_1,\mathbf W_2)}\exp(\boldsymbol x^\top\mathbf W_1\boldsymbol z_1+\boldsymbol z_1^\top\mathbf W_2\boldsymbol z_2)\tag{4.91}$$
- **4.3.3.4 Deep belief network** (p. 174): an RBM prior over a latent code, decoded by a directed model:
$$p(\boldsymbol x,\boldsymbol z_1,\boldsymbol z_2|\boldsymbol\theta)=p(\boldsymbol x|\boldsymbol z_1,\mathbf W_1)\frac1{Z(\mathbf W_2)}\exp(\boldsymbol z_1^\top\mathbf W_2\boldsymbol z_2)\tag{4.92}$$
  The author notes "DBN" is a confusing name since it is not a belief net, and proposes "deep Boltzmann network". DBNs train greedily and give fast bottom-up inference. They were one of the first deep models to train successfully but are no longer widely used (better supervised training, and VAEs) (p. 174).

### 4.3.4 Maximum entropy models (pp. 174–176)
The author recalls (Sec. 2.4.7) that the exponential family has maximum entropy subject to expected features matching empirical expectations: $p(\boldsymbol x|\boldsymbol\theta)=\frac1{Z(\boldsymbol\theta)}\exp(\boldsymbol\theta^\top\boldsymbol\phi(\boldsymbol x))$ (4.93). If $\boldsymbol\phi$ decomposes along a graph, the MRF is a **maximum entropy model** (a kind of EBM) (p. 175).

**4.3.4.1 Log-linear models.** With $\psi_c=\exp(\boldsymbol\theta_c^\top\boldsymbol\phi(\boldsymbol x_c))$ (4.94),
$$p(\boldsymbol x|\boldsymbol\theta)=\frac1{Z(\boldsymbol\theta)}\exp\Big(\sum_c\boldsymbol\theta_c^\top\boldsymbol\phi(\boldsymbol x_c)\Big)\tag{4.95}$$
Gaussian graphical models (GGM) and Ising models both use $\boldsymbol\phi([x_i,x_j])=[x_i,x_j,x_ix_j]$ (4.96, 4.97), so both are maxent models. Differences: a GGM has real-valued variables, and its $Z(\boldsymbol\theta)$ costs $O(D^3)$, while a Boltzmann machine's can cost $O(2^D)$. With hierarchical features on categorical variables this is a *log-linear model* in statistics. In ML the term is often used for any model of the form (4.95) (p. 175).

**4.3.4.2 Feature induction (spelling model, [DDL97]).**
- **Feature induction** (learning features in a maxent model) starts from base features and greedily adds new combinations ("feature pursuit"). The model is a distribution over variable-length strings (pp. 175–176).
- The model starts with no features (uniform). The first feature is $\phi_1(\boldsymbol x)=\sum_i\mathbb I(x_i\in\{a,\dots,z\})$ (4.98). After refitting by maximum likelihood, $\hat\theta_1=1.944$. A word with a lowercase letter in a position is about $e^{1.944}\approx7$ times as likely as the same word without one there (p. 176).
- The second feature checks adjacent lowercase pairs: $\phi_2=\sum_{i\sim j}\mathbb I(x_i\in\{a..z\},x_j\in\{a..z\})$ (4.99), giving $p(\boldsymbol x)=\frac1Z\exp(\theta_1\phi_1+\theta_2\phi_2)$ (4.100). Later features cover `s>`, `ing>` and regexes like `[0-9]`. Samples (annealed Gibbs) are gibberish with one feature and English-like with 1000 features (p. 176).
- A feature for every letter combination could represent any distribution but would overfit. The strength of maxent is choosing which features matter. Latent variables (4.3.3) are an alternative (p. 176).

### 4.3.5 Gaussian MRFs
**4.3.5.1 Standard GMRFs (pp. 177–178).** A GGM is a pairwise MRF:
$$p(\boldsymbol x)=\tfrac1{Z(\boldsymbol\theta)}\prod_{i\sim j}\psi_{ij}(x_i,x_j)\prod_i\psi_i(x_i)\tag{4.101}$$
$$\psi_{ij}=\exp(-\tfrac12x_i\Lambda_{ij}x_j)\ (4.102),\quad \psi_i=\exp(-\tfrac12\Lambda_{ii}x_i^2+\eta_ix_i)\ (4.103),\quad Z=(2\pi)^{D/2}|\boldsymbol\Lambda|^{-1/2}\ (4.104)$$
This is equivalent to the *information form* $p(\boldsymbol x)\propto\exp[\boldsymbol\eta^\top\boldsymbol x-\frac12\boldsymbol x^\top\boldsymbol\Lambda\boldsymbol x]$ (4.105), with canonical parameters $\boldsymbol\Lambda=\boldsymbol\Sigma^{-1}$ and $\boldsymbol\eta=\boldsymbol\Lambda\boldsymbol\mu$ (p. 177). If $\Lambda_{ij}=0$ there is no pairwise term, hence $x_i\perp x_j|\boldsymbol x_{-ij}$. These zeros are *structural zeros*, so $\ell_1$ regularisation can learn a sparse graph (graphical lasso) (p. 177).
The covariance $\boldsymbol\Sigma=\boldsymbol\Lambda^{-1}$ can be dense even if $\boldsymbol\Lambda$ is sparse. Example: AR(1) with correlation $\rho$, $T=7$. The precision (4.106) is tridiagonal, $\frac1{\tau^2}\times$ (diagonal $1,1{+}\rho^2,\dots,1{+}\rho^2,1$; off-diagonals $-\rho$). The covariance (4.107) is fully dense, with entries decaying as powers of $\rho$. In a chain UPGM every pair is marginally correlated even if they may be conditionally independent given a separator (p. 178).

*Intuition note.* Zeros in the precision matrix mean "conditionally independent given everything else". Marginal covariance mixes in indirect paths, so it can be dense even when the precision matrix is sparse.

**4.3.5.2 Nonlinear Gaussian MRFs (p. 178).** Let $p(\boldsymbol x)=\frac1Z\prod_c\psi_c(\boldsymbol x_c)$ with $\psi_c=\exp(-E_c)$ and
$$E_c(\boldsymbol x_c)=\tfrac12(f_c(\boldsymbol x_c)-\boldsymbol d_c)^\top\boldsymbol\Sigma_c^{-1}(f_c(\boldsymbol x_c)-\boldsymbol d_c)\tag{4.108–4.110}$$
($\boldsymbol d_c$ is optional local evidence, $f_c$ a measurement function.) If $f_c(\boldsymbol x)=\mathbf J_c\boldsymbol x+\boldsymbol b_c$ (4.111), then
$$E_c=\tfrac12\boldsymbol x_c^\top\underbrace{\mathbf J_c^\top\boldsymbol\Sigma_c^{-1}\mathbf J_c}_{\boldsymbol\Lambda_c}\boldsymbol x_c+\boldsymbol x_c^\top\underbrace{\mathbf J_c^\top\boldsymbol\Sigma_c^{-1}(\boldsymbol b_c-\boldsymbol d_c)}_{-\boldsymbol\eta_c}+\underbrace{\tfrac12(\boldsymbol b_c-\boldsymbol d_c)\boldsymbol\Sigma_c^{-1}(\boldsymbol b_c-\boldsymbol d_c)}_{k_c}\tag{4.112}$$
$$=\tfrac12\boldsymbol x_c^\top\boldsymbol\Lambda_c\boldsymbol x_c-\boldsymbol\eta_c^\top\boldsymbol x_c+k_c\tag{4.113}$$
a standard Gaussian factor. If $f_c$ is nonlinear, linearise around the current estimate $\boldsymbol x_c^0$:
$$f_c(\boldsymbol x_c)\approx f_c(\boldsymbol x_c^0)+\mathbf J_c(\boldsymbol x_c-\boldsymbol x_c^0)=\mathbf J_c\boldsymbol x_c+\underbrace{(f_c(\boldsymbol x_c^0)-\mathbf J_c\boldsymbol x_c^0)}_{\boldsymbol b_c}\tag{4.114}$$
$\mathbf J_c$ is the Jacobian of $f_c$. This gives a temporary Gaussian factor for inference, and the process can be iterated (p. 178).

**4.3.5.3 INLA (p. 179).** Setting: latent Gaussian models $p(\boldsymbol y,\boldsymbol x|\boldsymbol\theta)=p(\boldsymbol x|\boldsymbol\theta)\prod_ip(y_i|x_i,\boldsymbol\theta)$ with GMRF prior on latents $\boldsymbol x$. Getting $p(\boldsymbol\theta|\boldsymbol y)$ needs marginalising $\boldsymbol x$, which is in general intractable. INLA ("integrated nested Laplace approximation", [RMC09]) proceeds as follows.
1. $p(\boldsymbol\theta|\boldsymbol y)=p(\boldsymbol y|\boldsymbol\theta)p(\boldsymbol\theta)/p(\boldsymbol y)$, with $p(\boldsymbol y|\boldsymbol\theta)=\dfrac{p(\boldsymbol y|\boldsymbol x^*,\boldsymbol\theta)p(\boldsymbol x^*|\boldsymbol\theta)}{p(\boldsymbol x^*|\boldsymbol y,\boldsymbol\theta)}$ for any $\boldsymbol x^*$. INLA takes $\boldsymbol x^*$ as the mode of a Gaussian approximation to $p(\boldsymbol x|\boldsymbol y,\boldsymbol\theta)$. The normalised posterior over $\boldsymbol\theta$ is then approximated using $p(\boldsymbol\theta,\boldsymbol y)$ (e.g. with HMC if computing $\boldsymbol x^*$ is differentiable, or a grid for low dimensions).
2. Finding $\boldsymbol x^*$: let $f(\boldsymbol x)=\log p(\boldsymbol y|\boldsymbol x,\boldsymbol\theta)$. Its quadratic expansion at $\boldsymbol x_0$ is $\hat f(\boldsymbol x|\boldsymbol x_0)=f(\boldsymbol x_0)+(\boldsymbol x-\boldsymbol x_0)^\top\boldsymbol g_0+\frac12(\boldsymbol x-\boldsymbol x_0)^\top\mathbf H_0(\boldsymbol x-\boldsymbol x_0)$, with gradient $\boldsymbol g_0$ and Hessian $\mathbf H_0$. $\mathbf H_0$ is diagonal because the likelihood factorises over nodes.
3. With log prior $-\frac12(\boldsymbol x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\boldsymbol x-\boldsymbol\mu)$, the log joint is approximated by $L(\boldsymbol x|\boldsymbol x_0)=\log p(\boldsymbol x|\boldsymbol\theta)+\hat f(\boldsymbol x|\boldsymbol x_0)$. Grouping quadratic and linear terms and dropping constants:
$$L(\boldsymbol x|\boldsymbol x_0)=-\tfrac12\boldsymbol x^\top(-\mathbf H_0+\boldsymbol\Sigma^{-1})\boldsymbol x+\boldsymbol x^\top(\boldsymbol\Sigma^{-1}\boldsymbol\mu+\boldsymbol g_0-\mathbf H_0\boldsymbol x_0)$$
4. This is the log of a Gaussian with precision $\boldsymbol\Lambda_0=\boldsymbol\Sigma^{-1}-\mathbf H_0$ and precision-weighted mean $\boldsymbol\eta_0=\boldsymbol\Sigma^{-1}\boldsymbol\mu+\boldsymbol g_0-\mathbf H_0\boldsymbol x_0$. Its maximum is $\boldsymbol x_1=\boldsymbol\Lambda_0^{-1}\boldsymbol\eta_0$, found by solving a sparse linear system. Iterate to the global maximum $\boldsymbol x^*$. The posterior precision has the prior's sparsity pattern since $\mathbf H_0$ is diagonal.
5. Marginals: $p(x_i|\boldsymbol y)=\int p(x_i|\boldsymbol\theta,\boldsymbol y)p(\boldsymbol\theta|\boldsymbol y)d\boldsymbol\theta$. The integral is done numerically over a carefully selected set of points (like sigma points), which works only when $\dim\boldsymbol\theta$ is small. $p(x_i|\boldsymbol\theta,\boldsymbol y)$ comes from an inner Laplace approximation (p. 179).

### 4.3.6 Conditional independence properties
**4.3.6.1 Basic results (pp. 179–180).**
- **Global Markov property:** $\mathbf X_A\perp_G\mathbf X_B|\mathbf X_C$ iff $C$ separates $A$ from $B$ in $G$, i.e. after removing $C$ no path joins $A$ to $B$. Example (Fig. 4.23b): $\{X_1,X_2\}\perp\{X_6,X_7\}|\{X_3,X_4,X_5\}$.
- **Markov blanket** $\mathrm{mb}(t)$: the smallest set making $t$ independent of the rest, $t\perp\mathcal V\setminus\mathrm{cl}(t)\,|\,\mathrm{mb}(t)$ (4.115), where $\mathrm{cl}(t)=\mathrm{mb}(t)\cup\{t\}$. In a UPGM, one can show it is the immediate neighbours (**local Markov property**). Example: $\mathrm{mb}(X_5)=\{X_2,X_3,X_4,X_6,X_7\}$.
- **Pairwise Markov property:** $s\perp t|\mathcal V\setminus\{s,t\}\iff G_{st}=0$ (4.116).
- Examples from Fig. 4.23b: $X_1\perp X_7|\text{rest}$ (pairwise); $X_1\perp\text{rest}|X_2,X_3$ (local); the global example above.
- Global implies local implies pairwise (obvious). Less obviously, pairwise implies global, so all three coincide (Fig. 4.24), provided $p(\boldsymbol x)>0$. With deterministic constraints a distribution can be *unfaithful* to the graph, i.e. $I(p)\ne I(G)$ (footnote 8, p. 181). Practical use: pairwise CI is easiest to assess empirically, and a graph built from it yields global CI statements (p. 180).

**4.3.6.2 Undirected alternative to d-separation (p. 181).**
- Simply dropping edge directions is wrong. The v-structure $A\to B\leftarrow C$ differs from the chain $A-B-C$, which wrongly says $A\perp C|B$.
- **Moralisation:** connect "unmarried" co-parents, then drop arrows. In Fig. 4.23, join 2–3 (child 5) and 4–5–6 (child 7).
- Moralisation loses CI information. In Fig. 4.23a, d-separation gives $X_4\perp X_5|X_2$, but the added 4–5 edge (from child 7) destroys it. That edge is not needed if neither 7 nor its descendants are observed.
- **Procedure for $A\perp B|C$:** form the **ancestral graph** with respect to $U=A\cup B\cup C$ (remove nodes not in $U$ and not ancestors of $U$), moralise it, then use graph separation. Example: $U=\{X_2,X_4,X_5\}$ keeps nodes 1–5. Moralising adds 2–3 (Fig. 4.25b), and now $X_4\perp X_5|X_2$ is correctly obtained.

*Intuition note.* Separation in an undirected graph is simple, but marrying parents is a blunt tool. Restricting to the ancestral graph keeps only the part of the DAG that can matter for the query.

### 4.3.7 Generation (sampling) (pp. 181–182)
Sampling from a UPGM, even from the prior, can be slow because there is no variable ordering. Probabilities cannot be computed easily unless $Z$ is known. MCMC (Chapter 12) is common. For low treewidth and discrete or Gaussian potentials, the junction tree algorithm can draw samples by dynamic programming (p. 182).

### 4.3.8 Inference (p. 182)
Example: binary pixels $z_i$, noisy observations $x_i$:
$$p(\boldsymbol x,\boldsymbol z)=p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)=\Big[\tfrac1Z\sum_{i\sim j}\psi_{ij}(z_i,z_j)\Big]\prod_ip(x_i|z_i)\tag{4.117}$$
Here $p(\boldsymbol z)$ is an Ising prior and $p(x_i|z_i)=\mathcal N(x_i|z_i,\sigma^2)$, $z_i\in\{-1,+1\}$. The sum over $i\sim j$ is printed as in the source (a product would be expected by 4.74; see Reading notes). Mixing an undirected prior with directed likelihood edges is a **chain graph** (Fig. 4.26). The tasks are the posterior marginals $p(z_i|\boldsymbol x)$ or the MAP $\arg\max_{\boldsymbol z}p(\boldsymbol z|\boldsymbol x)$. Exact computation is intractable for large grids, so approximations are used: mean-field VI, Gibbs sampling, loopy belief propagation. Fig. 4.27 shows mean-field denoising with Ising prior $W_{ij}=1$ and Gaussian noise $\sigma=2$ (pp. 182–183).

### 4.3.9 Learning
Even fully observed MLE is expensive because of $Z(\boldsymbol\theta)$. The posterior $p(\boldsymbol\theta|\mathcal D)$ is "doubly intractable" because of the extra constant $p(\mathcal D)$. The text therefore focuses on MLE and MAP (pp. 182–183).

**4.3.9.1 Complete data (pp. 183–184).** Log-linear model:
$$p(\boldsymbol x|\boldsymbol\theta)=\tfrac1{Z(\boldsymbol\theta)}\exp\Big(\sum_c\boldsymbol\theta_c^\top\boldsymbol\phi_c(\boldsymbol x)\Big)\tag{4.118}$$
$$\ell(\boldsymbol\theta)=\tfrac1N\sum_n\Big[\sum_c\boldsymbol\theta_c^\top\boldsymbol\phi_c(\boldsymbol x_n)-\log Z(\boldsymbol\theta)\Big]\tag{4.119}$$
$$\frac{\partial\ell}{\partial\boldsymbol\theta_c}=\tfrac1N\sum_n\Big[\boldsymbol\phi_c(\boldsymbol x_n)-\frac{\partial}{\partial\boldsymbol\theta_c}\log Z(\boldsymbol\theta)\Big]\tag{4.120}$$
From Sec. 2.4.3, $\dfrac{\partial\log Z}{\partial\boldsymbol\theta_c}=\mathbb E[\boldsymbol\phi_c(\boldsymbol x)|\boldsymbol\theta]=\sum_{\boldsymbol x}p(\boldsymbol x|\boldsymbol\theta)\boldsymbol\phi_c(\boldsymbol x)$ (4.121). Hence
$$\frac{\partial\ell}{\partial\boldsymbol\theta_c}=\tfrac1N\sum_n[\boldsymbol\phi_c(\boldsymbol x_n)]-\mathbb E[\boldsymbol\phi_c(\boldsymbol x)]\tag{4.122}$$
The gradient is zero when
$$\mathbb E_{p_{\mathcal D}}[\boldsymbol\phi_c(\boldsymbol x)]=\mathbb E_{p(\boldsymbol x|\boldsymbol\theta)}[\boldsymbol\phi_c(\boldsymbol x)]\tag{4.123}$$
This is **moment matching**. The data term is the *clamped/positive phase* ($\boldsymbol x$ fixed to data), the model term the *unclamped/negative phase* ($\boldsymbol x$ generated by the model). For tabular potentials, *iterative proportional fitting (IPF)* solves these equations iteratively. In general gradient methods are needed. For decomposable graphs IPF converges in one iteration (footnote 9, p. 184).

*Intuition note.* The MLE adjusts parameters until the model reproduces the data's average feature values. The negative phase is the expensive part, because it needs the model's own statistics.

**4.3.9.2 Computational issues (p. 184).** The bottleneck is $\nabla_{\boldsymbol\theta}\log Z(\boldsymbol\theta)$ (with $\tilde p$ the unnormalised density):
$$\nabla_{\boldsymbol\theta}\log Z=\tfrac1{Z}\nabla_{\boldsymbol\theta}\!\int\tilde p\,d\boldsymbol x=\tfrac1Z\!\int\nabla_{\boldsymbol\theta}\tilde p\,d\boldsymbol x\tag{4.124}$$
$$=\tfrac1Z\!\int\tilde p\,\nabla_{\boldsymbol\theta}\log\tilde p\,d\boldsymbol x=\int\tfrac{\tilde p}{Z}\nabla_{\boldsymbol\theta}\log\tilde p\,d\boldsymbol x\tag{4.125}$$
$$=\mathbb E_{\boldsymbol x\sim p(\boldsymbol x;\boldsymbol\theta)}[\nabla_{\boldsymbol\theta}\log\tilde p(\boldsymbol x;\boldsymbol\theta)]\tag{4.126}$$
using $\nabla\log\tilde p=\frac1{\tilde p}\nabla\tilde p$ (log-derivative trick). So each SGD step needs samples from the model. Alternatives that avoid maximum likelihood are contrastive divergence (Sec. 24.2.2) and pseudolikelihood (below).

**4.3.9.3 Pseudolikelihood (pp. 184–185).** For fully visible MRFs/CRFs:
$$\ell_{PL}(\boldsymbol\theta)\triangleq\tfrac1N\sum_{n=1}^N\sum_{d=1}^D\log p(x_{nd}|\boldsymbol x_{n,-d},\boldsymbol\theta)\tag{4.127}$$
compared with $\ell_{ML}=\frac1N\sum_n\log p(\boldsymbol x_n|\boldsymbol\theta)$ (4.128). It is a product of full conditionals (a *composite likelihood*).
- For Gaussian MRFs, PL is equivalent to ML, though not in general. It is a consistent estimator in the large-sample limit.
- It is generally fast because each conditional only sums over the states of one node. It resembles fitting each conditional separately, but with parameters tied between adjacent nodes (Fig. 4.28).
- Experiments suggest PL works as well as exact ML for fully observed Ising models but is much faster. It was used to fit Potts models to protein data. For RBMs, [Mar+10] found PL worse than some stochastic ML methods.
- A subtler problem: each node assumes neighbours are known during training. If neighbour $j$ perfectly predicts node $i$, then $j$ learns to rely on $i$ and ignore other information such as local evidence $y_i$. At test time neighbours are unobserved and performance suffers. Hinton's analogy (footnote 10): denoising symmetric shapes such as Greek vases, where the symmetric pixel predicts $x_i$ perfectly (p. 185).

**4.3.9.4 Incomplete data (pp. 185–186).** Hidden variables arise e.g. in $p(\boldsymbol z)p(\boldsymbol x|\boldsymbol z)$ with only $\boldsymbol x$ observed (a *hidden Gibbs random field*), or in CRFs with latent alignments. For an unconditional log-linear model, $p(\boldsymbol x,\boldsymbol z|\boldsymbol\theta)=\tilde p(\boldsymbol x,\boldsymbol z|\boldsymbol\theta)/Z(\boldsymbol\theta)$ with $Z=\sum_{\boldsymbol x,\boldsymbol z}\exp(\boldsymbol\theta^\top\boldsymbol\phi(\boldsymbol x,\boldsymbol z))$ (4.129, 4.130). Then
$$\ell(\boldsymbol\theta)=\tfrac1N\sum_n\log\Big(\sum_{\boldsymbol z_n}p(\boldsymbol x_n,\boldsymbol z_n|\boldsymbol\theta)\Big)=\tfrac1N\sum_n\Big[\log\sum_{\boldsymbol z_n}\tilde p(\boldsymbol x_n,\boldsymbol z_n|\boldsymbol\theta)-\log Z(\boldsymbol\theta)\Big]\tag{4.131–4.133}$$
$$\log\sum_{\boldsymbol z_n}\tilde p(\boldsymbol x_n,\boldsymbol z_n|\boldsymbol\theta)=\log\sum_{\boldsymbol z_n}\exp(\boldsymbol\theta^\top\boldsymbol\phi(\boldsymbol x_n,\boldsymbol z_n))\triangleq\log Z(\boldsymbol\theta,\boldsymbol x_n)\tag{4.134}$$
$Z(\boldsymbol\theta,\boldsymbol x_n)$ is the partition function with $\boldsymbol x$ clamped at $\boldsymbol x_n$. So the log-likelihood is a difference of two log partition functions, one clamped and one unclamped. Differentiating:
$$\frac{\partial\ell}{\partial\boldsymbol\theta}=\tfrac1N\sum_n\Big[\mathbb E_{\boldsymbol z\sim p(\boldsymbol z|\boldsymbol x_n,\boldsymbol\theta)}[\boldsymbol\phi(\boldsymbol x_n,\boldsymbol z)]\Big]-\mathbb E_{(\boldsymbol z,\boldsymbol x)\sim p(\boldsymbol z,\boldsymbol x|\boldsymbol\theta)}[\boldsymbol\phi(\boldsymbol x,\boldsymbol z)]\tag{4.135}$$

### 4.4 Conditional random fields (pp. 186–187)
A **CRF** [LMP01] is an MRF over label nodes $\boldsymbol y$, conditioned on fixed inputs $\boldsymbol x$:
$$p(\boldsymbol y|\boldsymbol x,\boldsymbol\theta)=\frac1{Z(\boldsymbol x,\boldsymbol\theta)}\prod_c\psi_c(\boldsymbol y_c;\boldsymbol x,\boldsymbol\theta)\tag{4.136}$$
$Z$ now depends on $\boldsymbol x$. Log-linear potentials: $\psi_c=\exp(\boldsymbol\theta_c^\top\boldsymbol\phi_c(\boldsymbol x,\boldsymbol y_c))$ (4.137), a conditional maxent model. Nonlinear potentials such as DNNs are also possible. CRFs capture dependencies among outputs, so they are used for **structured prediction** (outputs in a structured space, often with constraints). Constraints may be hard (grammar rules) or soft (neighbouring pixels should usually share a label) (p. 187).

#### 4.4.1 1d CRFs (pp. 187–188)
For chain-structured models (Fig. 4.29):
$$p(\boldsymbol y_{1:T}|\boldsymbol x,\boldsymbol\theta)=\frac1{Z(\boldsymbol x,\boldsymbol\theta)}\prod_{t=1}^T\psi(y_t,\boldsymbol x_t;\boldsymbol\theta)\prod_{t=2}^T\psi(y_{t-1},y_t;\boldsymbol\theta)\tag{4.138}$$
Node potentials $\psi(y_t,\boldsymbol x_t)$ and edge potentials; here edge potentials are assumed independent of $\boldsymbol x$, though this is not required (p. 187).
An alternative is the directed *maximum entropy Markov model*:
$$p(\boldsymbol y_{1:T}|\boldsymbol x,\boldsymbol\theta)=p(y_1|\boldsymbol x_1;\boldsymbol\theta)\prod_{t=2}^Tp(y_t|y_{t-1},\boldsymbol x_t;\boldsymbol\theta)\tag{4.139}$$
Its conditionals are **locally normalised**, whereas the CRF is **globally normalised** through $Z(\boldsymbol x,\boldsymbol\theta)$. The author says the latter lets information propagate through the whole sequence (details in Sec. 4.5.3, outside this unit). CRFs were widely used in NLP in the 1980s–2010s and recently were mostly replaced by RNNs and transformers. Combining CRFs with DNNs merges data-driven features with prior knowledge about label constraints (p. 188).

**4.4.1.1 Noun phrase chunking (p. 188).** Tag each word with a part-of-speech label and a B/I/O label (begin / inside / outside a noun phrase) (Fig. 4.30). Edges between adjacent labels encode constraints. OBIIO and OBIOBIO are valid; OIBIO is not. The author encodes this by setting $\psi(y^{\text{BIO}}_{t-1}=*,y^{\text{BIO}}_t=B,\boldsymbol x_t;\boldsymbol\theta)=0$ for every $*$ except O (as printed; see Reading notes). The MAP label sequence then gives the noun-phrase spans (p. 189).

**4.4.1.2 Named entity recognition (p. 189).** Extend the labels to {B-Per, I-Per, B-Loc, I-Loc, B-Org, I-Org, Other}. Proper nouns are an open class and are ambiguous ("British Airways" is an organisation, "British Virgin Islands" a location). In a **skip-chain CRF** one might link all occurrences of the same word and force them to share a tag (Fig. 4.31: "Green" is a person in both places). The graph structure depends on the input, which the author calls an advantage over generative models. Inference is generally more expensive because of larger treewidth (p. 189).

**4.4.1.3 Natural language parsing (pp. 189–190).** A PCFG in Chomsky normal form has rules $\sigma\to\sigma'\sigma''$ or $\sigma\to x$, each with a probability. It defines a distribution over word sequences. The probability of a sequence is the sum over all trees generating it, computed in $O(T^3)$ by the inside–outside algorithm. A discriminative version is the CRF $p(\boldsymbol y|\boldsymbol x)\propto\exp(\boldsymbol w^\top\Psi(\boldsymbol x,\boldsymbol y))$, where $\Psi$ counts how often each production rule is used (Fig. 4.32, energy $E(\boldsymbol y|\boldsymbol x)=-\boldsymbol w^\top\Psi(\boldsymbol x,\boldsymbol y)$). A deep net can define the features (neural CRF parser) (p. 190).

#### 4.4.2 2d CRFs (pp. 190–193)
On image grids (Fig. 4.33):
$$p(\boldsymbol y|\boldsymbol x)=\frac1{Z(\boldsymbol x)}\Big[\sum_{i\sim j}\psi_{ij}(y_i,y_j)\Big]\prod_ip(y_i|\boldsymbol x_i)\tag{4.140}$$
(sum printed as in the source.)

**4.4.2.1 Semantic segmentation (p. 191).** The task is to label every pixel. A CNN with a softmax per pixel may miss long-range dependencies. CNN outputs are usually locally smooth, so a local grid CRF may add little. A **fully connected CRF** can capture long-range links (Fig. 4.34). Exact inference is intractable, but with Gaussian potentials an efficient mean-field algorithm exists [KK11]. [Zhe+15] implemented mean-field updates as an RNN for end-to-end training. Alternatively, unroll a finite number of iterations into a feedforward graph-structured network. Then the model trains end-to-end by gradient descent without handling the partition function or the non-convergence that can arise from combining approximate inference with standard CRF learning (p. 191).

**4.4.2.2 Deformable parts models (pp. 192–193).** Sliding-window detectors work well for rigid objects, but can work poorly with occlusion or deformable shapes. Instead, detect parts and enforce spatial coherence with a pairwise CRF. Node $y_i\in\{1,\dots,K\}$ is the location of part $i$, with pairwise potential $\psi(y_i,y_j|\boldsymbol x)=\exp(-d(y_i,y_j))$ ($d$ is distance, which may depend on $\boldsymbol x$) and local evidence $p(y_i|\boldsymbol x)$ from e.g. a CNN:
$$p(\boldsymbol y|\boldsymbol x)=\frac1{Z(\boldsymbol x)}\Big[\prod_ip(y_i|f(\boldsymbol x)_i)\Big]\Big[\prod_{(i,j)\in E}\psi(y_i,y_j|\boldsymbol x)\Big]\tag{4.141}$$
This is parts joined by springs (Fig. 4.35), called a pictorial structure or deformable parts model, with image-dependent spring strengths (p. 192–193). The global optimum $\boldsymbol y^*=\arg\max p(\boldsymbol y|\boldsymbol x,\boldsymbol\theta)$ costs $O(K^T)$ by brute force ($T$ nodes, $K$ locations each). Tree-structured exact inference costs $O(TK^2)$, and exploiting ordinal states reduces it to $O(TK)$. With a dynamic-programming inference module, DPMs can be written as CNNs, since gradients backpropagate through inference (p. 193).

#### 4.4.3 Parameter estimation (p. 193)
**4.4.3.1 Log-linear potentials.** With $\psi_c=\exp(\boldsymbol\theta_c^\top\boldsymbol\phi_c(\boldsymbol x,\boldsymbol y_c))$ (4.142):
$$\ell(\boldsymbol\theta)=\tfrac1N\sum_n\Big[\sum_c\boldsymbol\theta_c^\top\boldsymbol\phi_c(\boldsymbol y_{nc},\boldsymbol x_n)-\log Z(\boldsymbol x_n;\boldsymbol\theta)\Big],\quad Z(\boldsymbol x_n;\boldsymbol\theta)=\sum_{\boldsymbol y}\exp(\boldsymbol\theta^\top\boldsymbol\phi(\boldsymbol y,\boldsymbol x_n))\tag{4.143, 4.144}$$
$$\frac{\partial\ell}{\partial\boldsymbol\theta_c}=\tfrac1N\sum_n\Big[\boldsymbol\phi_c(\boldsymbol y_{nc},\boldsymbol x_n)-\frac{\partial}{\partial\boldsymbol\theta_c}\log Z(\boldsymbol x_n;\boldsymbol\theta)\Big]=\tfrac1N\sum_n\Big[\boldsymbol\phi_c(\boldsymbol y_{nc},\boldsymbol x_n)-\mathbb E_{p(\boldsymbol y|\boldsymbol x_n,\boldsymbol\theta)}[\boldsymbol\phi_c(\boldsymbol y,\boldsymbol x_n)]\Big]\tag{4.145, 4.146}$$
The author states the objective is convex, so many solvers apply, e.g. stochastic meta descent, an SGD variant with automatically adapted step size (p. 193).

*Intuition note.* The CRF gradient is the MRF gradient with one change: the expected features are taken per example, given its own input $\boldsymbol x_n$. So $Z$ is a sum over labels only, not over inputs.

## Toy example (ours, not from the text)
A two-node Ising model, one edge, $\phi(\boldsymbol x)=x_1x_2$ and $\mathcal E=-Jx_1x_2$ (as in 4.78). Take $J=\ln2$, so $e^{J}=2$ and $e^{-J}=0.5$.
- Unnormalised weights $\exp(Jx_1x_2)$: $(+,+)=2$, $(-,-)=2$, $(+,-)=0.5$, $(-,+)=0.5$.
- $Z=2+2+0.5+0.5=5$. Probabilities: $0.4,0.4,0.1,0.1$.
- Model expectation (negative phase): $\mathbb E[x_1x_2]=0.4+0.4-0.1-0.1=0.6$.
- Data: $N=4$ samples with $x_1x_2=+1,+1,+1,-1$, so the data mean (positive phase) is $(1+1+1-1)/4=0.5$.
- Gradient (4.122): $\partial\ell/\partial J=0.5-0.6=-0.1<0$, so $J$ should decrease.
- Moment matching (4.123): the enumeration gives $\mathbb E[x_1x_2]=\dfrac{e^J-e^{-J}}{e^J+e^{-J}}=\tanh J$ (added step). Setting $\tanh J=0.5$ gives $e^{2J}=\frac{1.5}{0.5}=3$, so $J=\tfrac12\ln3\approx0.549$.
- Note: computing $Z$ needed $2^2=4$ terms. With $D$ nodes it needs $2^D$, which is the cost behind (4.126).

## Concepts
- [[markov-random-field]] (new) — undirected model with potentials on maximal cliques; also UPGM or Markov network (p. 165)
- [[hammersley-clifford-theorem]] (new) — for positive $p$ satisfying the graph's CI properties, $p$ factorises over cliques (p. 166)
- [[partition-function]] (new) — $Z(\boldsymbol\theta)$, the sum of the unnormalised product over all states; makes $p$ sum to 1 (p. 166)
- [[energy-based-model]] (new) — $p\propto\exp(-\mathcal E)$ with low energy meaning high probability; the Gibbs distribution (p. 166)
- [[ising-potts-model]] (new) — pairwise MRFs with agreement potentials over binary (Ising) or $K$-state (Potts) nodes; phase transition at a critical $J_c$ (pp. 167–169)
- [[hopfield-network]] (new) — fully connected Ising model with symmetric $\mathbf W$, used as associative memory via ICM (p. 170)
- [[boltzmann-machine-rbm]] (new) — MRFs with latent units; RBM is bipartite, so hidden units are conditionally independent given visible (pp. 172–173)
- [[maximum-entropy-log-linear-model]] (new) — $p\propto\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ with graph-decomposed features (p. 175); relates to canon [[principle-of-indifference-maximum-entropy]]
- [[gaussian-mrf-precision]] (new) — Gaussian with sparse precision $\boldsymbol\Lambda$; zeros mean conditional independence, while $\boldsymbol\Sigma$ may be dense (p. 177)
- [[markov-properties-undirected]] (new) — global, local, pairwise Markov properties; equivalent for $p>0$ (p. 180)
- [[moralization]] (new) — connect co-parents and drop arrows; with the ancestral graph it tests DAG CI by separation (p. 181)
- [[moment-matching]] (new) — MLE condition: data feature expectation equals model feature expectation (p. 184)
- [[pseudolikelihood]] (new) — product of full conditionals as an MLE substitute avoiding $Z$ (p. 184)
- [[inla]] (new) — integrated nested Laplace approximation for latent Gaussian models (p. 179)
- [[conditional-random-field]] (new) — MRF over labels $\boldsymbol y$ conditioned on inputs $\boldsymbol x$; globally normalised by $Z(\boldsymbol x,\boldsymbol\theta)$ (p. 186)
- [[structured-prediction]] (new) — predicting outputs in structured spaces with dependencies and constraints (p. 187)
- [[gibbs-sampling]] — mentioned as the sampler used for Ising samples; ICM is its deterministic analogue (pp. 168, 171)
- [[variational-inference-and-elbo]] — mean-field VI mentioned for image denoising (p. 182)
- [[d-separation]] — compared with undirected separation (p. 181)

## Canonical instances
- [[ising-lattice-phase-transition]] — samples clump as coupling rises; $J_c\approx0.44$ for the square lattice (pp. 167–168)
- [[potts-protein-contact-map]] — Potts model on MSA gives residue contact maps (p. 170)
- [[hopfield-image-completion]] — recover occluded images; capacity $\sim0.14N$ (pp. 171–172)
- [[maxent-spelling-model]] — greedy feature induction, $\hat\theta_1=1.944$ (p. 176)
- [[ar1-precision-vs-covariance]] — tridiagonal precision, dense covariance (pp. 177–178)
- [[ising-image-denoising]] — Ising prior with Gaussian noise, mean-field inference (pp. 182–183)
- [[np-chunking-ner-crf]] — chain and skip-chain CRFs with BIO labels (pp. 188–189)
- [[deformable-parts-model]] — pictorial structures as a pairwise CRF with springs (pp. 192–193)

## Bridges (candidates)
- [same-math] CRF/MRF log-likelihood gradient (features minus expected features) ↔ exponential-family MLE: derivative of log-partition is expected sufficient statistics (Sec. 2.4.3, cited p. 183).
- [same-math] Maxent model with $\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ ↔ principle of indifference / maximum entropy: least-committal distribution matching feature expectations (p. 174–175).
- [same-math] INLA's Laplace step (Gaussian approximation about the mode) ↔ Laplace approximation to the posterior in Bayesian models (p. 179).
- [structural-analogy] Doubly intractable posterior over MRF parameters ↔ marginal likelihood $p(\mathcal D)$ as hard normaliser in Bayesian model comparison (p. 182).
- [structural-analogy] Moralisation (marrying co-parents) ↔ conditioning on a collider opens a path: co-parents must be linked (p. 181).
- [structural-analogy] RBM versus directed two-layer model ↔ explaining away in causal DAGs (p. 172).

## Questions this raises
- Why does pairwise Markov imply global Markov only for positive densities, and what do unfaithful distributions look like (footnote 8, p. 181)?
- When is pseudolikelihood a good approximation to ML, given that it is exact for Gaussian MRFs but fails when a neighbour is a perfect predictor (pp. 184–185)?
- How does global normalisation in a CRF let information propagate, compared with the locally normalised MEMM (p. 188, deferred to Sec. 4.5.3)?
- What does a sparse precision matrix mean for a Bayesian hierarchical or spatial model, and how does INLA exploit it (pp. 177, 179)?

## Reading notes
- This is part 2 of 3 of Chapter 4. It starts at the heading of Section 4.2.8.2 (naive Bayes), below Fig. 4.14 at the top of the page; Fig. 4.13, which the text cites, is not among these pages. It ends at the end of Section 4.4.3.1, p. 193. The split was at a section boundary of the part; later material is not covered. Printed page = pdf − 34. The unit contains no exercises.
- Page footers read "Probabilistic Machine Learning: Advanced Topics. Online version. December 10, 2025" and "(C) MIT Press. CC-BY-NC-ND license".
- On pdf 224 (p. 190) the text layer is garbled with leaked fragments of another document ("SVM Learning for Interdependent and Structured Output Spaces"). The page image shows only the clean figures (4.32, 4.33). Figure text on pp. 188–189 is also scrambled in the text layer, but the images are clear.
- Possible misprints, as printed: (4.117) and (4.140) write $\sum_{i\sim j}\psi_{ij}$ where (4.74) uses $\prod_{i\sim j}$. In (4.112) the last term lacks a transpose. Eq. (4.72) states "$\mathcal E(\boldsymbol x)>0$". Fig. 4.18's caption says size 128×128 while its axes run to about 64.
- (4.107): the printed covariance (entries $\tau^2\rho^{|i-j|+1}$) does not appear to equal the inverse of (4.106). In a T=3 analogue of (4.106), the inverse is $\tau^2\rho^{|i-j|}/(1-\rho^2)$ (checked at the (1,1) entry). The qualitative point (dense covariance, sparse precision) is unaffected.
- p. 188: the prose says "B must precede I", but the printed rule zeroes transitions into B from any non-O label. This also forbids I→B, e.g. in OIBIO. It is reported as printed.
- Quotation count: a few short phrases from the text are quoted (e.g. "rather unnatural", "soft constraint"); none is longer than 25 words.

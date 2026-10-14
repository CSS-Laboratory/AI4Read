---
id: murphy-2023-pml2/ch04-graphical-p1
work: murphy-2023-pml2
unit: "4 Graphical models (part 1/3): 4.1 Introduction and 4.2 Directed graphical models, up to 4.2.8.1"
pages: 143-163
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
# Graphical models (part 1/3): directed graphical models (Bayes nets)

## L0 — One line
A directed acyclic graph defines a joint distribution as a product of small local conditional distributions, and the graph's missing edges encode conditional independences that can be read off by d-separation and used for sampling, inference and learning.

## L1 — The gist (≤ 120 words)
How can we write a joint distribution over many variables compactly? Murphy's answer is the directed graphical model (Bayes net). Each node gets a conditional distribution given its parents, so the joint is a product of local terms. For a sparse graph this needs far fewer parameters than an unstructured joint. The graph also implies conditional independences, readable by d-separation (a path-blocking rule). Conditioning on a common child makes its parents dependent ("explaining away"). Ancestral sampling (parents first), inference and learning all follow the structure. With complete data, learning splits into one problem per node. With hidden variables it does not, so iterative optimization (EM or SGD) is used.

**Prerequisites:** conditional independence; chain rule of probability; Gaussian distributions and covariance; multinomial and Dirichlet distributions; maximum likelihood; gradients of log functions.

## L2 — Key ideas
- A DAG with a topological ordering gives the factorization $p(x_{1:N_G})=\prod_i p(x_i\mid x_{\text{pa}(i)})$. With at most $N_P$ parents and $K$ states, this needs $O(N_G K^{N_P+1})$ parameters instead of $O(K^{N_G})$ (exponentially fewer if the DAG is sparse) (p. 144).
- A linear-Gaussian Bayes net is a joint Gaussian with mean $\mu$ and covariance $\Sigma=US^2U^\top$, where $U=(I-W)^{-1}$ (p. 148).
- d-separation (rules for when observed nodes block a path: chain, fork, collider; checked by the Bayes ball algorithm) gives the global Markov property. The graph is an I-map of $p$ (it asserts no conditional independence that fails in $p$) iff $I(G)\subseteq I(p)$, where $I(\cdot)$ is the set of CI statements (pp. 149–151).
- Explaining away (Berkson's paradox): conditioning on a common effect makes independent causes dependent. In Murphy's examples the induced correlation could be mistaken for a causal link, but it is due to selection bias (pp. 151–153).
- The Markov blanket (parents, children, and co-parents, i.e. the other parents of its children) gives the full conditional of a node. The global, local, ordered and factorization properties are equivalent (pp. 153–154).
- Ancestral sampling (sample each node given its parents, in topological order) and inference (posterior over query nodes, summing out nuisance variables) are defined from the graph (pp. 154–155).
- With complete data the likelihood, prior and posterior factorize per node, so learning tabular conditional probability tables (CPTs) is counting (MLE) or counting plus Dirichlet pseudocounts (prior counts added to the observed counts) (pp. 157–159).
- With hidden variables the objective no longer decomposes; EM (expectation maximization, using expected counts) or SGD (stochastic gradient descent, with a gradient weighted by the posterior over hidden variables) is used (pp. 159–161).
- Plate notation compresses repeated nodes and shows parameters as nodes (p. 162).

## L3 — Walkthrough

### 4.1 Introduction (p. 143)
Probabilistic graphical models (PGMs) define joint distributions over random variables. Nodes are variables. The *lack* of edges encodes conditional independence (CI) assumptions. Murphy says "independence diagrams" would be a better name. The graph may be directed, undirected or mixed. Murphy opens with a Jordan quote: probability implements modularity and abstraction "through factorization and through averaging" (p. 143).

### 4.2 Directed graphical models (Bayes nets) (p. 143)
A DPGM is based on a directed acyclic graph (DAG: no directed cycles). Murphy says there is nothing inherently "Bayesian" in Bayes nets. They are just a way of defining distributions. Their probabilities are no more and no less subjective than in other probabilistic models, even though they are also called "belief networks" (p. 143).

#### 4.2.1 Representing the joint distribution (pp. 143–144)
Nodes can be ordered so that parents precede children (a topological ordering). The **ordered Markov property** says a node is conditionally independent of its other predecessors given its parents:
$$x_i \perp x_{\text{pred}(i)\setminus \text{pa}(i)} \mid x_{\text{pa}(i)} \tag{4.1}$$
With ordering $1:N_G$, the chain rule plus (4.1) gives
$$p(x_{1:N_G}) = p(x_1)p(x_2|x_1)\cdots p(x_{N_G}|x_{1:N_G-1}) = \prod_{i=1}^{N_G} p(x_i|x_{\text{pa}(i)}) \tag{4.2}$$
Here $p(x_i|x_{\text{pa}(i)})$ is the conditional probability distribution (CPD) of node $i$.

Parameter count (all variables discrete, $K$ states): an unstructured joint needs $O(K^{N_G})$ parameters. A DAG with at most $N_P$ parents per node needs $O(N_G K^{N_P+1})$, "exponentially fewer if the DAG is sparse" (p. 144).

*Intuition note:* The graph says which variables each variable directly depends on. Each node then needs only a small local table, and multiplying the tables rebuilds the whole joint.

#### 4.2.2 Examples
**4.2.2.1 Markov chains (pp. 144–145).** In the chain DAG (Fig. 4.1a) information cannot flow from past to future except via the present. So $x_t$ is a sufficient statistic for the past, and the model is first-order Markov:
$$p(x_{1:T}) = p(x_1)p(x_2|x_1)\cdots p(x_T|x_{T-1}) \tag{4.3}$$
For discrete states the CPD is a conditional probability table (CPT) $p(x_t=k|x_{t-1}=j)=\theta_{jk}$, with each row summing to 1 (p. 145). A second-order model (Fig. 4.1b) has
$$p(x_{1:T}) = p(x_1,x_2)\prod_{t=3}^T p(x_t|x_{t-2:t-1}) \tag{4.4}$$
In the limit of increasing order the DAG is fully connected. Then there are no useful CIs, "so the graphical model has no value" (p. 145).

**4.2.2.2 The "student" network (pp. 145–146).** Five discrete variables: D (difficulty: easy/hard), I (intelligence: low/high), G (grade A/B/C), S (SAT: bad/good), L (letter: bad/good). With topological order I, D, G, S, L the chain rule gives
$$p(D,I,G,L,S)=p(L|S,G,D,I)\,p(S|G,D,I)\,p(G|D,I)\,p(D|I)\,p(I) \tag{4.5}$$
$L$ is independent of earlier nodes given its parent $G$, and similarly for the other terms:
$$p(D,I,G,L,S)=p(L|G)\,p(S|I)\,p(G|D,I)\,p(D)\,p(I) \tag{4.6}$$
Edges: D→G, I→G, I→S, G→L (Fig. 4.2). Murphy calls splitting a joint into small local pieces "the key idea behind graphical models" (p. 145).

A tabular CPD has one categorical row per combination of parent values:
$$\theta_{ijk}\triangleq p(x_i=k\mid x_{\text{pa}(i)}=j) \tag{4.7}$$
$\theta_{i,:,:}$ is a row-stochastic matrix: $0\le\theta_{ijk}\le1$ and $\sum_{k=1}^{K_i}\theta_{ijk}=1$. Here $i\in[N_G]$ indexes nodes, $k\in[K_i]$ states, and $j\in[J_i]$ joint parent states with $J_i=\prod_{p\in\text{pa}(i)}K_p$ (p. 145). Examples from Fig. 4.2: $p(G|D{=}1,I{=}0)=[0.05,0.25,0.7]$ and $p(G|D{=}1,I{=}1)=[0.5,0.3,0.2]$ (p. 145). Other CPTs: $p(D)=[0.6,0.4]$, $p(I)=[0.7,0.3]$ (p. 146). A CPT has $O(K^{p+1})$ parameters (p. 146).

Queries: observing $G=C$ gives $p(I{=}\text{High}|G{=}C)=0.08$. Also observing a good SAT raises it to $p(I{=}\text{High}|G{=}C,S{=}\text{Good})=0.58$, and $p(D{=}\text{Hard}|G{=}C,S{=}\text{Good})=0.76$. This is **explaining away** (Berkson's paradox) (p. 146; see 4.2.6.1).

**4.2.2.3 Sigmoid belief nets (p. 147).** A two-layer deep generative model (Fig. 4.3a) has joint
$$p(x,z)=p(z_2)p(z_1|z_2)p(x|z_1)=\prod_{k=1}^{K_2}p(z_{2,k})\prod_{k=1}^{K_1}p(z_{1,k}|z_2)\prod_{d=1}^{D}p(x_d|z_1) \tag{4.8}$$
If all latent variables are binary and all latent CPDs are logistic regressions,
$$p(z_\ell|z_{\ell+1},\theta)=\prod_{k=1}^{K_\ell}\mathrm{Ber}\big(z_{\ell,k}\mid\sigma(w_{\ell,k}^\top z_{\ell+1})\big) \tag{4.9}$$
with $\sigma(u)=1/(1+e^{-u})$. This is a sigmoid belief net. For real-valued data the bottom layer might be
$$p(x|z_1,\theta)=\prod_{d=1}^D\mathcal N\big(x_d\mid w_{1,d,\mu}^\top z_1,\ \exp(w_{1,d,\sigma}^\top z_1)\big) \tag{4.10}$$
Adding directed edges among hidden variables within a layer (Fig. 4.3b) gives a deep autoregressive network (DARN) (p. 147).

#### 4.2.3 Gaussian Bayes nets (p. 148)
Take all variables real-valued with linear Gaussian CPDs:
$$p(x_i|x_{\text{pa}(i)})=\mathcal N(x_i\mid\mu_i+w_i^\top x_{\text{pa}(i)},\sigma_i^2) \tag{4.11}$$
Their product is a joint Gaussian $\mathcal N(x|\mu,\Sigma)$, $x\in\mathbb R^{N_G}$ (a directed Gaussian graphical model). Rewrite each CPD as
$$x_i=\mu_i+\sum_{j\in\text{pa}(i)}w_{i,j}(x_j-\mu_j)+\sigma_i z_i,\quad z_i\sim\mathcal N(0,1) \tag{4.12}$$
The global mean is the concatenation of the local means. Let $S=\text{diag}(\sigma)$, which is $N_G\times N_G$. In matrix form, with $W$ the $N_G\times N_G$ matrix of regression weights:
$$(x-\mu)=W(x-\mu)+Sz \tag{4.13}$$
Let $e\triangleq Sz$. Then $e=(I-W)(x-\mu)$. $W$ is lower triangular, so $I-W$ is lower triangular with 1s on the diagonal (4.14). Hence $I-W$ is always invertible, and with $U\triangleq(I-W)^{-1}$:
$$x-\mu=(I-W)^{-1}e=Ue=USz \tag{4.15}$$
$$\Sigma=\text{Cov}[x]=\text{Cov}[x-\mu]=\text{Cov}[USz]=US\,\text{Cov}[z]\,SU^\top=US^2U^\top \tag{4.16}$$
because $\text{Cov}[z]=I$. Footnote 1: without subtracting the parents' means in (4.12), the derivation is "much messier" (p. 148).

*Intuition note:* Each variable is a weighted sum of its parents plus fresh noise. Unrolling the sums (via $U$) writes every variable as a combination of independent noise terms. That is why the result is jointly Gaussian with covariance $US^2U^\top$.

#### 4.2.4 Conditional independence properties (p. 149)
$x_A\perp_G x_B|x_C$ means CI holds in graph $G$. $I(G)$ is the set of all CI statements encoded by the graph. $I(p)$ is the set of CI statements true in distribution $p$. $G$ is an **I-map** for $p$ (equivalently, $p$ is Markov wrt $G$) iff $I(G)\subseteq I(p)$: the graph asserts no CI that fails in $p$. So the graph is a safe proxy for $p$ when reasoning about its CIs. The fully connected graph is an I-map of every distribution because it asserts no CIs. $G$ is a **minimal I-map** of $p$ if it is an I-map and no $G'\subseteq G$ is (p. 149).

**4.2.4.1 Global Markov property (d-separation) (pp. 149–151).** An undirected path $P$ is **d-separated** by a set $C$ (the evidence) iff at least one holds (p. 149):
1. $P$ contains a chain $s\to m\to t$ or $s\leftarrow m\leftarrow t$ with $m\in C$.
2. $P$ contains a fork $s\leftarrow m\rightarrow t$ with $m\in C$.
3. $P$ contains a collider (v-structure) $s\rightarrow m\leftarrow t$ where $m\notin C$ and no descendant of $m$ is in $C$.

Set $A$ is d-separated from $B$ given $C$ iff every undirected path from every $a\in A$ to every $b\in B$ is d-separated by $C$. The global Markov property is
$$X_A\perp_G X_B|X_C \iff A \text{ is d-separated from } B \text{ given } C \tag{4.17}$$
**Bayes ball** [Sha98] checks this. Shade nodes in $C$, put balls at nodes in $A$, let them bounce by the rules (Fig. 4.4), and see whether any reaches $B$. Balls may travel against edge direction. They pass through chains and forks unless the middle node is shaded. They cannot pass through a v-structure unless it is shaded in the middle (p. 149).

Justification of the three rules (pp. 149–151):
- Chain $X\to Y\to Z$: $p(x,y,z)=p(x)p(y|x)p(z|y)$ (4.18). Then $p(x,z|y)=\frac{p(x)p(y|x)p(z|y)}{p(y)}=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y)$ (4.19). So $X\perp Z|Y$: observing the middle node splits the chain, as in a Markov chain (p. 150).
- Fork $X\leftarrow Y\to Z$: $p(x,y,z)=p(y)p(x|y)p(z|y)$ (4.20), so $p(x,z|y)=p(x|y)p(z|y)$ (4.21). Observing a root separates its children, as in naive Bayes (p. 150).
- V-structure $X\to Y\leftarrow Z$: $p(x,y,z)=p(x)p(z)p(y|x,z)$ (4.22), so $p(x,z|y)=\frac{p(x)p(z)p(y|x,z)}{p(y)}$ (4.23) and $X\not\perp Z|Y$. But $p(x,z)=p(x)p(z)$ (4.24): $X$ and $Z$ are marginally independent (p. 151). Conditioning on a common child makes its parents dependent. This is explaining away, inter-causal reasoning, or Berkson's paradox.

*Intuition note:* Chains and forks carry dependence until you observe the middle node. A collider blocks dependence until you observe it (or a descendant). Then the two causes must "compete" to explain it.

Boundary conditions (Fig. 4.5): a ball hitting a hidden leaf stops. A ball hitting an observed leaf bounces back. Reason: if $Y'$ is a (possibly noisy) copy of $Y$, observing $Y'$ effectively observes $Y$, so parents $X,Z$ must compete to explain it. If $Y$ and all its children are hidden, the ball does not bounce back (p. 151). Table 4.1 lists CI statements $X\perp Y|Z$ implied by the student DAG, e.g. D⊥I with empty $Z$, and D⊥L given G (p. 151).

**4.2.4.2 Explaining away (Berkson's paradox) (pp. 152–153).**
- *Two coins:* toss two coins 100 times and record only runs with at least one head, giving about 75 entries. Whenever coin 1 is recorded as tails, coin 2 is heads. Ignoring how the data were collected, one might infer a hidden common cause. The correct explanation is conditioning on a hidden common effect (the decision to record), which censors tail-tail outcomes. This is selection bias (p. 152).
- *Gaussian:* $p(x,y,z)=\mathcal N(x|-5,1)\mathcal N(y|5,1)\mathcal N(z|x+y,1)$ (4.25), graph $X\to Z\leftarrow Y$. Unconditionally $X$ and $Y$ are uncorrelated (Fig. 4.6a,b). Selecting only samples with $z>2.5$ makes them correlated (Fig. 4.6d, which shows a negative slope). This could lead us to "erroneously conclude" a causal relationship, but the dependency is due to selection bias (pp. 152–153).

**4.2.4.3 Markov blankets (p. 153).** The Markov blanket $\text{mb}(i)$ is the smallest set of nodes that makes node $i$ conditionally independent of all other nodes. In a DPGM it is
$$\text{mb}(i)\triangleq\text{ch}(i)\cup\text{pa}(i)\cup\text{copa}(i) \tag{4.26}$$
where co-parents are other parents of $i$'s children (Fig. 4.7). Derivation: partition nodes into $X_i$, parents $U$, children $Y$, co-parents $Z$, others $O$. Then
$$p(X_i|X_{-i})=\frac{p(X_i,X_{-i})}{\sum_x p(X_i=x,X_{-i})}=\frac{p(X_i,U,Y,Z,O)}{\sum_x p(X_i=x,U,Y,Z,O)} \tag{4.27, 4.28}$$
$$=\frac{p(X_i|U)\big[\prod_j p(Y_j|X_i,Z_j)\big]P(U,Z,O)}{\sum_x p(X_i=x|U)\big[\prod_j p(Y_j|X_i=x,Z_j)\big]P(U,Z,O)} \tag{4.29}$$
$P(U,Z,O)$ does not involve $X_i$ and cancels:
$$=\frac{p(X_i|U)\prod_j p(Y_j|X_i,Z_j)}{\sum_x p(X_i=x|U)\prod_j p(Y_j|X_i=x,Z_j)} \tag{4.30}$$
$$\propto p(X_i|\text{pa}(X_i))\prod_{Y_j\in\text{ch}(X_i)}p(Y_j|\text{pa}(Y_j)) \tag{4.31}$$
So the full conditional is
$$p(x_i|x_{-i})=p(x_i|x_{\text{mb}(i)})\propto p(x_i|x_{\text{pa}(i)})\prod_{k\in\text{ch}(i)}p(x_k|x_{\text{pa}(k)}) \tag{4.32}$$
Murphy says this is used in Gibbs sampling and mean-field variational inference (p. 153).

*Intuition note:* Only the factors that mention $X_i$ survive, namely its own CPD and its children's CPDs. The children's CPDs bring in the co-parents.

**4.2.4.4 Other Markov properties (p. 154).** The **local Markov property** is
$$i\perp\text{nd}(i)\setminus\text{pa}(i)\mid\text{pa}(i) \tag{4.33}$$
with $\text{nd}(i)=\{1,\dots,N_G\}\setminus\{i\cup\text{desc}(i)\}$. The ordered Markov property is
$$i\perp\text{pred}(i)\setminus\text{pa}(i)\mid\text{pa}(i) \tag{4.34}$$
It follows from the local one since $\text{pred}(i)\subseteq\text{nd}(i)$, and it justifies (4.2). Murphy states $G\Rightarrow L\Rightarrow O$ is obvious. $O\Rightarrow L\Rightarrow G$ is "less obvious, but nevertheless true" (proof in [KF09a]), so all three are equivalent. Any $p$ Markov wrt the graph factorizes as in (4.2) (the factorization property $F$). $O\Rightarrow F$ is obvious and the converse also holds (proof in [KF09a]) (p. 154).

#### 4.2.5 Generation (sampling) (p. 154)
Visit nodes in topological order and sample each given its parents' values. This gives independent samples from the joint and is called **ancestral sampling**.

#### 4.2.6 Inference (p. 155)
Inference means computing the posterior over query nodes $Q$ given visible nodes $V$, marginalizing nuisance variables $R=\{1..N_G\}\setminus\{Q,V\}$:
$$p_\theta(Q|V)=\frac{p_\theta(Q,V)}{p_\theta(V)}=\frac{\sum_R p_\theta(Q,V,R)}{p_\theta(V)} \tag{4.35}$$
(Use integrals for continuous variables.) For a single query node this is a posterior marginal. In the speech example $V=x$ (sound), $Q=z$ (words), $R=r$ (prosody, noise):
$$p_\theta(z|x)=\sum_r p_\theta(z,r|x)=\sum_r\frac{p_\theta(z,r,x)}{p_\theta(x)}=\sum_r\frac{p_\theta(z,r,x)}{\sum_{z',r'}p_\theta(z',r',x)} \tag{4.36}$$
Lumping $R$ into $Q$ gives hidden variables $H=Q\cup R$ and
$$p_\theta(h|x)=\frac{p_\theta(h,x)}{\sum_{h'}p_\theta(h',x)} \tag{4.37}$$
Cost depends on the graph's CI structure. In general inference is NP-hard. For chains, trees and other sparse graphs it is polynomial via dynamic programming (Chapter 9). Otherwise approximate methods are used (Chapter 7) (p. 155).

**4.2.6.1 Student example (p. 155, Fig. 4.8).** After observing $G=C$: $p(D{=}\text{Hard}|G{=}C)=0.63$ and $p(I{=}\text{High}|G{=}C)=0.08$. Murphy says the low grade is "more likely explained" by low intelligence than by a hard class. Adding SAT = Good: $p(I{=}\text{High}|G{=}C,\text{SAT}{=}\text{Good})=0.58$. Once we believe the student is intelligent, the C has to be explained by the class being hard, whose probability rises to 0.76 (Fig. 4.8b; see Reading notes for a typo in the text).

#### 4.2.7 Learning (pp. 155–161)
Structure learning is in Section 30.3. Here the structure $G$ is fixed and we do parameter learning, computing $p(\theta|D,G)$. One may treat $\theta$ as another hidden variable. In ML it is more common to use a point estimate such as the posterior mode $\hat\theta=\arg\max p(\theta|D)$. Murphy says this is "often reasonable" since parameters depend on all the data and so are less uncertain than other hidden variables (p. 156).

**4.2.7.1 Complete data (p. 157).** Fig. 4.9 shows a generative classifier with $N$ local variables $(x_n,y_n)$ (observed) and global parameter nodes $\theta_x,\theta_y$. The CI properties give
$$p(\theta,D)=p(\theta_x)p(\theta_y)\Big[\prod_{n=1}^N p(y_n|\theta_y)p(x_n|y_n,\theta_x)\Big] \tag{4.38}$$
$$=\Big[p(\theta_y)\prod_n p(y_n|\theta_y)\Big]\Big[p(\theta_x)\prod_n p(x_n|y_n,\theta_x)\Big] \tag{4.39}$$
$$\propto[p(\theta_y)p(D_y|\theta_y)]\,[p(\theta_x)p(D_{x|y}|\theta_x)] \tag{4.40}$$
with $D_y=\{y_n\}$ and $D_{x|y}=\{(x_n,y_n)\}$. Prior, likelihood and posterior all factorize, so each parameter's posterior can be computed independently. In general
$$p(\theta,D)=\prod_{i=1}^{N_G}p(\theta_i)p(D_i|\theta_i) \tag{4.41}$$
$$\hat\theta=\arg\max_\theta\prod_{i=1}^{N_G}p(D_i|\theta_i) \tag{4.42}$$
which can be solved node by node.

**4.2.7.2 MLE for CPTs (pp. 157–158).** The likelihood is a product of multinomials:
$$p(D|\theta)=\prod_{n=1}^N\prod_{i=1}^{N_G}p(x_{ni}|x_{n,\text{pa}(i)},\theta_i)=\prod_{n}\prod_i\prod_{j=1}^{J_i}\prod_{k=1}^{K_i}\theta_{ijk}^{\mathbb I(x_{ni}=k,\,x_{n,\text{pa}(i)}=j)} \tag{4.43, 4.44}$$
Sufficient statistics (counts): $N_{ijk}\triangleq\sum_{n=1}^N\mathbb I(x_{n,i}=k,x_{n,\text{pa}(i)}=j)$ (4.46). The MLE is the normalized empirical frequency:
$$\hat\theta_{ijk}=\frac{N_{ijk}}{\sum_{k'}N_{ijk'}} \tag{4.47}$$
Example: Table 4.2 has 7 student rows $(I,D,G,S,L)$. For node $G$ with parents $(I,D)$, Table 4.3 gives $N_{ijk}$ and MLE. For $(I,D)=(0,0)$: $N=[1,1,1]$ and $\hat\theta=[\frac13,\frac13,\frac13]$. For $(0,1)$: $N=[0,0,1]$ and $\hat\theta=[0,0,1]$. For $(1,0)$: $[1,0,0]$. For $(1,1)$: $N=[0,1,1]$ and $\hat\theta=[0,\frac12,\frac12]$. Fitting a tabular DPGM "reduces to a simple counting problem", but small samples give extreme estimates with many zeros (pp. 158–159).

**4.2.7.3 Posterior for CPTs (p. 159).** Put a Dirichlet prior on each CPT row, $\theta_{ij}\sim\text{Dir}(\alpha_{ij})$. Then $\theta_{ij}|D\sim\text{Dir}(N_{ij}+\alpha_{ij})$, with posterior mean
$$\bar\theta_{ijk}=\frac{N_{ijk}+\alpha_{ijk}}{\sum_{k'}(N_{ijk'}+\alpha_{ijk'})} \tag{4.48}$$
The MAP estimate has the same form with $\alpha_{ijk}-1$ in place of $\alpha_{ijk}$. With $\alpha_{ijk}=1$, row $(0,0)$ gives $[\frac26,\frac26,\frac26]$ and row $(1,1)$ gives $[\frac15,\frac25,\frac25]$ (Table 4.3).

**4.2.7.4 Incomplete data (pp. 159–160).** In Fig. 4.10 the $z_n$ are hidden. The likelihood is
$$p(D|\theta)=\sum_{z_{1:N}}\Big[\prod_n p(z_n|\theta_z)p(x_n|z_n,\theta_x)\Big]=\prod_{n=1}^N\sum_{z_n}p(z_n|\theta_z)p(x_n|z_n,\theta_x) \tag{4.49, 4.50}$$
$$\ell(\theta)=\sum_n\log\sum_{z_n}p(z_n|\theta_z)p(x_n|z_n,\theta_x) \tag{4.51}$$
The log does not distribute over $\sum_{z_n}$, so the objective does not decompose over nodes. Footnote 2: $\theta_x$ is no longer independent of $\theta_z$ because a path connects them via hidden $z_n$. So the MLE or posterior can no longer be found per node. Optimization (EM, SGD) finds a local optimum of this non-convex objective (p. 160).

**4.2.7.5 EM for CPTs (pp. 160–161).** EM alternates an E step (infer latent variables) and an M step (re-estimate parameters on the completed data). The E step returns expected sufficient statistics (ESS), not the full posterior. For tabular CPDs the complete-data log-likelihood and its expectation are
$$\log p(D|\theta)=\sum_{i=1}^{N_G}\sum_{j=1}^{J_i}\sum_{k=1}^{K_i}N_{ijk}\log\theta_{ijk} \tag{4.52}$$
$$\mathbb E[\log p(D|\theta)]=\sum_i\sum_j\sum_k\overline N_{ijk}\log\theta_{ijk} \tag{4.53}$$
$$\overline N_{ijk}=\sum_{n=1}^N\mathbb E\big[\mathbb I(x_{ni}=k,x_{n,\text{pa}(i)}=j)\big]=\sum_{n=1}^N p(x_{ni}=k,x_{n,\text{pa}(i)}=j\mid D_n,\theta^{old}) \tag{4.54}$$
where $D_n$ are the visible variables in case $n$. The term $p(x_{ni},x_{n,\text{pa}(i)}|D_n,\theta^{old})$ is a *family marginal*, computable with any GM inference algorithm. The M step is
$$\hat\theta_{ijk}=\frac{\overline N_{ijk}}{\sum_{k'}\overline N_{ijk'}} \tag{4.55}$$
MAP with a Dirichlet prior adds pseudocounts to the expected counts. Baum–Welch is the special case where the DPGM is an HMM (p. 161).

**4.2.7.6 SGD (p. 161).** EM is a batch algorithm. For large datasets SGD is more common. Collapse the model by marginalizing $z_n$:
$$p(x_n|\theta)=\sum_{z_n}p(z_n|\theta_z)p(x_n|z_n,\theta_x),\qquad \ell(\theta)=\log\prod_n p(x_n|\theta)=\sum_n\log p(x_n|\theta) \tag{4.56, 4.57}$$
The gradient is
$$\nabla_\theta\ell=\sum_n\nabla_\theta\log p(x_n|\theta)=\sum_n\frac1{p(x_n|\theta)}\nabla_\theta p(x_n|\theta) \tag{4.58, 4.59}$$
$$=\sum_n\frac1{p(x_n|\theta)}\nabla_\theta\Big[\sum_{z_n}p(z_n,x_n|\theta)\Big]=\sum_n\sum_{z_n}\frac{p(z_n,x_n|\theta)}{p(x_n|\theta)}\nabla_\theta\log p(z_n,x_n|\theta) \tag{4.60, 4.61}$$
$$=\sum_n\sum_{z_n}p(z_n|x_n,\theta)\nabla_\theta\log p(z_n,x_n|\theta) \tag{4.62}$$
and a minibatch approximation applies as usual (p. 161). The step from (4.60) to (4.61) uses $\nabla p=p\,\nabla\log p$ (added step).

*Intuition note:* The gradient is an average of the complete-data gradients, weighted by how probable each hidden value is given the data. In EM, the E step likewise works with posterior probabilities of the hidden variables to form expected counts (p. 160).

#### 4.2.8 Plate notation (p. 162)
With $N$ iid observations $x_n\sim p(x|\theta)$ (4.63), the joint is $p(D,\theta)=p(\theta)p(D|\theta)$ (4.64), and $p(D|\theta)=\prod_n p(x_n|\theta)$ (4.65). The order of the data does not matter, so the data are **exchangeable**. A **plate** is a box around repeated nodes, with the repetition count in its corner (Fig. 4.11). The model is "unrolled" to recover the repeated nodes.

**4.2.8.1 Factor analysis (pp. 162–163).** The model is $p(z)=\mathcal N(z|\mu_0,\Sigma_0)$ (4.66) and $p(x|z)=\mathcal N(x|Wz+\mu,\Psi)$ (4.67). Here $W$ is a $D\times L$ factor loading matrix and $\Psi$ is a diagonal $D\times D$ covariance. Fig. 4.12a shows scalar nodes, with edges for non-zero entries of $W$. Fig. 4.12b shows vector nodes, parameters as nodes, and a plate of size $N$. Fig. 4.13 (naive Bayes as a DPGM, without and with plates) appears at the end of this part; its text comes after this part.

## Toy example (ours)
A v-structure $X\to Y\leftarrow Z$ shows both the factorization and explaining away. $X$ and $Z$ are fair coins (1 = heads), and $Y=X\lor Z$ with a deterministic CPD $p(y|x,z)\in\{0,1\}$.
- Factorization (4.22): $p(x,z,y)=p(x)p(z)p(y|x,z)=\tfrac12\cdot\tfrac12\cdot p(y|x,z)$. So each of the four pairs $(x,z)$ has probability $\tfrac14$, with $y$ fixed: $(0,0)\to y{=}0$; $(1,0),(0,1),(1,1)\to y{=}1$.
- Marginal independence (4.24): $p(x{=}1,z{=}1)=\tfrac14=\tfrac12\cdot\tfrac12=p(x{=}1)p(z{=}1)$.
- Condition on $y=1$. $p(y{=}1)=\tfrac34$, so each of the three configurations has probability $\tfrac14/\tfrac34=\tfrac13$.
  - $p(x{=}1|y{=}1)=\tfrac13+\tfrac13=\tfrac23$, and likewise $p(z{=}1|y{=}1)=\tfrac23$.
  - $p(x{=}1,z{=}1|y{=}1)=\tfrac13\ne\tfrac23\cdot\tfrac23=\tfrac49$. So $X\not\perp Z|Y$.
- Explaining away: learning $z=1$ as well lowers $p(x{=}1)$ from $\tfrac23$ to $p(x{=}1|y{=}1,z{=}1)=\tfrac12$. Learning $z=0$ raises it to 1.

## Concepts
- [[directed-graphical-model]] (new) — DAG whose nodes are variables and whose joint is a product of CPDs given parents; "Bayesian" only in name (pp. 143–144)
- [[cpd-cpt]] (new) — conditional distribution of a node given its parents; for discrete nodes a row-stochastic table $\theta_{ijk}$ (pp. 144–145)
- [[conditional-independence-graph]] (new) — graph whose missing edges assert CIs; I-map iff $I(G)\subseteq I(p)$ (p. 149)
- [[d-separation]] — path-blocking rule (chain, fork, collider) giving the directed global Markov property; checked by Bayes ball (p. 149)
- [[fork-chain-collider]] — three elementary path structures; conditioning on a collider makes its parents dependent (pp. 149–151)
- [[explaining-away]] (new) — conditioning on a common effect couples its causes; also called Berkson's paradox, inter-causal reasoning (pp. 151–153)
- [[markov-blanket]] (new) — parents ∪ children ∪ co-parents; gives the full conditional of a node (p. 153)
- [[ancestral-sampling]] (new) — sample nodes in topological order, each given its parents (p. 154)
- [[gaussian-bayes-net]] (new) — linear-Gaussian CPDs give a joint Gaussian with $\Sigma=US^2U^\top$ (p. 148)
- [[conjugate-prior]] — Dirichlet prior on each CPT row; posterior $\text{Dir}(N_{ij}+\alpha_{ij})$ (p. 159)
- [[expectation-maximization]] (new) — for hidden variables: E step gives expected counts, M step normalizes them (pp. 160–161)
- [[exchangeability]] — here: order of iid data is irrelevant, so leaves can be permuted (p. 162)
- [[plate-notation]] (new) — box around repeated nodes with a repetition count (p. 162)

## Canonical instances
- [[student-network]] — five-variable Bayes net (D, I, G, S, L) used for factorization, explaining away, inference and counting-based learning (pp. 145–158)
- [[berkson-gaussian-example]] — $X\to Z\leftarrow Y$ Gaussian; selecting $z>2.5$ induces correlation between $X$ and $Y$ (pp. 152–153)
- [[two-coin-selection-bias]] — recording only runs with at least one head correlates the coins (p. 152)
- [[sigmoid-belief-net]] — binary latent layers with logistic-regression CPDs (p. 147)
- [[factor-analysis-dpgm]] — $z\to x$ linear Gaussian model drawn with plates (pp. 162–163)

## Bridges (candidates)
- [structural-analogy] Collider/explaining away ↔ causal inference: conditioning on a common effect opens a spurious path, as in selection bias — the text itself calls the two-coin and Gaussian cases selection bias.
- [same-math] Dirichlet-multinomial update of CPT rows ↔ Bayesian inference: posterior mean $=(N+\alpha)/\sum(N+\alpha)$ is the conjugate update.
- [same-math] Full conditional via Markov blanket (4.32) ↔ Gibbs sampling: the conditional used in Gibbs updates (the text points to Eq. 12.19).
- [structural-analogy] E step with expected counts ↔ latent-variable MLE: both use posterior probabilities of the hidden variables, in (4.54) and in (4.62).

## Questions this raises
- Does faithfulness (every CI in $p$ shown by the graph) hold generally, or can $I(G)\subsetneq I(p)$ hide extra independences?
- How should we compute family marginals efficiently for EM when the graph is dense (the text defers to Chapter 9)?
- When does a point estimate of $\theta$ (MLE or MAP) stop being reasonable and full posterior inference become necessary?
- How do undirected models encode independence, given that colliders have no direct counterpart there?

## Reading notes
- This is part 1/3 of Chapter 4. It starts at 4.1 (printed p. 143) and ends at the end of 4.2.8.1 (p. 163), at a section boundary. Naive Bayes text (4.2.8.2) and later sections are in later parts. Fig. 4.13 is shown here but not explained.
- Printed page numbers are given in the labels. Offset: printed = pdf − 34.
- Text/figure inconsistencies seen:
  - p. 144, Eq. (4.3): the last expression reads $\prod_{t=2}^T p(x_t|x_{1:t-1})$ in the image. The first expression, $p(x_t|x_{t-1})$, is the first-order form.
  - p. 148, Eq. (4.14): the third row is printed as $-w_{3,2}, -w_{3,1}$, though the row-1, row-2 pattern suggests $-w_{3,1}, -w_{3,2}$.
  - p. 155: the text says "$p(D=\text{Hard}|G=C)=0.76$" in the SAT=Good paragraph. Fig. 4.8b and p. 146 show 0.76 is conditional on both G=C and SAT=Good. Without SAT it is 0.63.
  - p. 153, Eq. (4.31) has an extra closing parenthesis.
- Cross-references to Chapters 6, 7, 9, 10, 12, 21, 28–30 and Figs. 22.1 and 4.23 point outside these pages and were not checked.

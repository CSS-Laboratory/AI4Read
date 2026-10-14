---
id: murphy-2023-pml2/ch28-latent-p2
work: murphy-2023-pml2
unit: "28 Latent factor models (part 2/2): end of GP-LVM, 28.4 non-Gaussian priors, 28.5 topic models, 28.6 ICA"
pages: 959-978
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Latent factor models with non-Gaussian priors, topic models and ICA

## L0 — One line
Replacing the Gaussian latent prior of factor analysis by gamma, Dirichlet, logistic-normal, Laplace or other non-Gaussian priors gives non-negative parts, mixed-membership topics, independent sources that can be recovered up to permutation and sign, and sparse codes.

## L1 — The gist (≤ 120 words)
Gaussian latent factor models leave a rotation unidentified, and their codes can be dense and signed, so harder to interpret. This unit asks what changes when the prior is not Gaussian. A gamma prior with Poisson likelihood includes non-negative matrix factorization (NMF) as a special case. A Dirichlet prior gives mixed-membership models and, for text, latent Dirichlet allocation (LDA) with variants (correlated, dynamic, LDA-HMM). An independent non-Gaussian prior lets independent components analysis (ICA) recover sources up to permutation and sign, as shown in an example. A Laplace prior with Gaussian noise gives sparse coding. Several ICA estimators (maximum likelihood, negentropy, total correlation, InfoMax) are shown equivalent. It also finishes the GP-LVM (dual of probabilistic PCA).

**Prerequisites:** Gaussian and Dirichlet distributions; maximum likelihood and MAP; PCA/factor analysis; change of variables for densities; entropy; SVD; basic graphical models.

## L2 — Key ideas (5–10 bullets)
- GP-LVM is the dual of probabilistic PCA: integrate out W and optimize Z. A linear kernel recovers PPCA; any Mercer kernel gives a nonlinear model fitted by gradients (p. 959).
- A gamma prior on latents with a Poisson likelihood is the GaP model. Its MLE for W with $\alpha_k=\beta_k=0$ is NMF, which learns local "parts" (p. 960–961).
- A Dirichlet prior on latents with a categorical likelihood is multinomial PCA (admixture, mixed membership). Latents add up to the mean parameters, so they are easier to read than Gaussian latents (p. 962–963).
- LDA applies this to words. The inferred document-level topic proportions can be used to disambiguate word senses (polysemy). Several inference methods exist; the number of topics is a model-selection problem (p. 964–967).
- Extensions address LDA's limits: logistic-normal prior for topic correlation (CTM), Gaussian random walk for drifting topics (DTM), and an HMM for syntax words (LDA-HMM) (p. 967–971).
- ICA: with $x=Az$, Gaussian latents leave a rotation unidentified. An independent, non-Gaussian prior (typically heavy-tailed) lets ICA recover the sources up to permutation and possible sign change, as shown on a uniform-source example (p. 972–974).
- ICA fitting reduces to optimizing an orthogonal matrix $V$ on whitened data. For orthogonal $V$, maximum likelihood, negentropy, total correlation and InfoMax (with $\phi$ a cdf) give equivalent objectives (p. 975–977).
- Sparse coding is a noisy, overcomplete ICA with a Laplace prior. Its learned filters are edge detectors, while PCA's are sinusoids (p. 977–978).

## L3 — Walkthrough

### End of the GP-LVM discussion (p. 959–960)
Probabilistic PCA (PPCA) as given: $p(z_i)=\mathcal N(z_i|0,I)$ (28.122), $p(y_i|z_i,\theta)=\mathcal N(y_i|Wz_i,\sigma^2 I)$ (28.123). Integrating out $z_i$ and maximizing over $W,\sigma^2$ gives
$$p(Y|W,\sigma^2)=(2\pi)^{-DN/2}|C|^{-N/2}\exp\!\Big(-\tfrac12\mathrm{tr}(C^{-1}Y^\top Y)\Big),\quad C=WW^\top+\sigma^2 I \tag{28.124}$$
The MLE of $W$ uses eigenvectors of $Y^\top Y$ (p. 959).

**Dual problem.** Put $p(W)=\prod_j\mathcal N(w_j|0,I)$, integrate out $W$ and maximize over $Z$:
$$p(Y|Z,\sigma^2)=\prod_{d=1}^D\mathcal N(Y_{:,d}|0,ZZ^\top+\sigma^2I) \tag{28.125}$$
$$=(2\pi)^{-DN/2}|K_z|^{-D/2}\exp\!\Big(-\tfrac12\mathrm{tr}(K_\sigma^{-1}YY^\top)\Big) \tag{28.126}$$
with $K=ZZ^\top$, $K_\sigma=K+\sigma^2 I$. The MLE of $Z$ uses eigenvectors of $K_\sigma$ and gives the same result as PPCA (details in [Law05]) (p. 959).

Reading this as a Gaussian process (GP) with linear kernel $\mathcal K(z_i,z_j)=z_i^\top z_j+\sigma^2\delta_{ij}$ (28.127) gives covariance $K=ZZ^\top+\sigma^2I$. So (28.126) is the likelihood of a product of independent GPs. Factor analysis is linear regression with unknown inputs; GP-LVM is GP regression with unknown inputs. The aim is a point estimate $\hat Z$ (Bayesian inference is also possible) (p. 959).

Advantage of the dual: any Mercer kernel can be used, $K_{ij}=\mathcal K(z_i,z_j)$. The MLE for $Z$ then needs gradient-based optimization, not eigenvalues (p. 959). Figure 28.19: mocap data (41 markers, 12 cameras, each point one body pose) with an ARD kernel; in 2d similar poses lie close together (p. 959–960).

*Intuition note:* PPCA can be fitted either by treating the weights $W$ as unknown or by treating the latent points $Z$ as unknown. The second view only needs a kernel matrix over points, so replacing the linear kernel by a nonlinear one gives a nonlinear embedding.

### 28.4 LFMs with non-Gaussian priors (p. 959)
Intro to (linear) latent factor models with non-Gaussian priors; Table 28.1 (not in this unit) summarizes them.

### 28.4.1 NMF (p. 960–961)
Take $p(z)=\prod_k \mathrm{Ga}(z_k|\alpha_k,\beta_k)$ (gamma prior). This gives a sparse, non-negative latent representation that can help interpretability. For sparse non-negative data such as word counts use $p(x|z)=\prod_{d=1}^D\mathrm{Poi}(x_d|w_d^\top z)$:
$$p(z,x)=\Big[\prod_k \mathrm{Ga}(z_k|\alpha_k,\beta_k)\Big]\Big[\prod_{d=1}^D\mathrm{Poi}(x_d|w_d^\top z)\Big]\tag{28.128}$$
This is the gamma-Poisson (GaP) model (Fig. 28.20a). $\alpha_k,\beta_k$ control the sparsity of $z_n$. With $\alpha_k=\beta_k=0$ and the MLE for $W$, one recovers non-negative matrix factorization (NMF) (p. 961).

Figure 28.21 (2429 face images, $19\times19$, 49 basis functions): NMF learns small localized *parts*, with sparse positive $z$. PCA gives signed coefficients and global bases. Vector quantization (a GMM) has one-hot $z$ and whole-image prototypes. Reconstruction quality is similar, but the learned representations differ (p. 961).

### 28.4.2 Multinomial PCA (p. 962–963)
A Dirichlet prior $p(z)=\mathrm{Dir}(z|\alpha)$ puts $z$ on the probability simplex $\mathbb S_K$. It is sparse and non-negative and satisfies $\sum_k z_k=1$, so components are not independent. With categorical data $x_d\in\{1,\dots,V\}$ and $p(x|z)=\prod_d\mathrm{Cat}(x_d|W_dz)$:
$$p(z,x)=\mathrm{Dir}(z|\alpha)\prod_{d=1}^D\mathrm{Cat}(x_d|W_dz)\tag{28.129}$$
(Fig. 28.20b). Names: user rating profile model, admixture model, mixed membership model, multinomial PCA (mPCA), simplex factor analysis (sFA) (p. 962).

**Roll-call example** [BJ06]: US Senate 2003, $x_{n,d}\in\{+1,-1,0\}$ for $n=1{:}100$ senators and $d=1{:}459$ bills (for / against / not voting). There is also the outcome $x_{101,d}\in\{+1,-1\}$. The model has 5 factors, fitted by variational EM. Figure 28.22 plots $\mathbb E[z_{nk}|x_n]$, the degree to which senator $n$ belongs to bloc $k$. Component 5 is the Democratic majority and component 2 the Republican majority (p. 962–963).

**Advantage over Gaussian prior.** $p(x_{nd}=v|z_n)=\sum_k z_{nk}w^d_{vk}$ (28.130), so latents combine additively into mean parameters. CatPCA (Section 28.3.5.2) has a Gaussian prior, so $W_dz_n$ can be negative and must go through a softmax, which makes $z_n$ harder to interpret (p. 963).

**Link to mixtures.** If $z_n$ were one-hot, mPCA would be a finite mixture of categoricals (one cluster generates $x$). mPCA allows partial membership in several clusters, hence "admixture"/"mixed membership" (p. 963).

*Intuition note:* A Dirichlet latent is a set of mixing proportions. Each output probability is a weighted average of the columns of $W$, so each weight can be read as "how much of component $k$".

### 28.5 Topic models; 28.5.1 LDA (p. 963–967)
Topic models adapt mPCA to sequences of tokens (words, genes). Words are conditionally independent given a latent topic vector $z$, which is a distribution over clusters; each word is drawn from its own local cluster (p. 963). Latent Dirichlet allocation (LDA) is the most common one (here "LDA" is not linear discriminant analysis); in genetics it is the admixture model (p. 963).

**28.5.1.1 Definition.** $x_{nl}\in\{1..V\}$ is word $l$ of document $n$ (length $L_n$):
$$p(x_{nl}=v|z_n)=\sum_k z_{nk}w_{kv},\quad z_n\sim\mathrm{Dir}(\alpha)\tag{28.131}$$
Adding a topic indicator $m_{nl}\in\{1..N_z\}$ with $p(m_{nl}|z_n)=\mathrm{Cat}(m_{nl}|z_n)$:
$$p(x_n,z_n,m_n)=\mathrm{Dir}(z_n|\alpha)\prod_{l=1}^{L_n}\mathrm{Cat}(m_{nl}|z_n)\,\mathrm{Cat}(x_{nl}|W[m_{nl},:])\tag{28.132}$$
where $W[k,:]=w_k$ is topic $k$'s word distribution (p. 964). Priors: $p(w_k)=\mathrm{Dir}(w_k|\beta 1_V)$ and $p(z_n)=\mathrm{Dir}(z_n|\alpha1_{N_z})$. Small enough $\beta$ encourages sparse topics, and small enough $\alpha$ sparse topic mixtures per document (Fig. 28.24) (p. 964). Probabilistic LSA [Hof99] has the same likelihood $p(x|z)$ but no prior on $z$; it is for posterior analysis of a fixed corpus, not a true generative model (p. 964).

**28.5.1.2 Polysemy.** Topics are distributions over co-occurring, hence semantically related, words. Fig. 28.25 (TASA corpus: 37,651 documents, 12,190,931 tokens) shows 3 topics that seem to correspond to three senses of "play": instrument, theatre, sports. The inferred document-level topic distribution disambiguates a word. Fig. 28.26 shows $\arg\max_k p(m_{nl}=k|x_n)$: the word "music" in a document makes the musical topic (77) more likely for "play" (p. 965–966).

**28.5.1.3 Inference.** Methods named: variational mean field [BNJ03a]; stochastic VI [HBB10]; collapsed Gibbs sampling, which marginalizes out the discrete latents [GS04]; amortized inference networks for the collapsed model [MB16; SS17b]. Spectral methods are fast and have provable guarantees (unlike MCMC/variational approximations of unknown quality), but need extra (reasonable) assumptions such as anchor words that uniquely identify a topic [Aro+13] (p. 966–967).

**28.5.1.4 Number of topics $N_z$** is model selection. Approaches: annealed importance sampling to approximate the evidence; cross-validation with test-set log likelihood; variational lower bound as a proxy for $\log p(\mathcal D|N_z)$; non-parametric Bayes (p. 967).

### 28.5.2 Correlated topic model (p. 967–968)
LDA cannot capture topic correlation (e.g. "business" with "finance"). Cause: a Dirichlet has a mean vector $\alpha$ but fixed covariance ($\Sigma_{ij}=-\alpha_i\alpha_j$ as printed), not a free parameter. Fix: the logistic normal,
$$p(z)=\int\mathrm{Cat}(z|\mathrm{softmax}(\epsilon))\,\mathcal N(\epsilon|\mu,\Sigma)\,d\epsilon\tag{28.133}$$
the correlated topic model (CTM) (p. 967). Versus CatPCA: CTM puts the normal on the *mean* parameters' logits, so $z_n$ is sparse and non-negative; CatPCA puts it on natural parameters, so $z_n$ is dense and can be negative. CTM: $x_{nl}\sim\mathrm{Cat}(W\,\mathrm{softmax}(\epsilon_n))$; CatPCA: $x_{nd}\sim\mathrm{Cat}(\mathrm{softmax}(W_dz_n))$ (p. 967).

Fitting is tricky because the prior on $\epsilon_n$ is not conjugate to the multinomial likelihood for $m_{nl}$; a variational mean-field approximation exists [BL07b]. After fitting, $\hat\Sigma$ can be turned into a sparse precision matrix $\hat\Sigma^{-1}$ by pruning weak edges, giving a Gaussian graphical model that visualizes topic correlations (Fig. 28.27, $K=50$, *Science* 1990–1999) (p. 967–968).

### 28.5.3 Dynamic topic model (p. 967–969)
LDA topics are static; they may drift (an article using the topic "neuroscience" is more likely to use words like "nerve" if written in the 1900s, and "calcium receptor" if written in the 2000s) (p. 967–968). Model the topic logits as a Gaussian random walk (state-space model) and map to probabilities with softmax:
$$w_k^t|w_k^{t-1}\sim\mathcal N(w_{t-1,k},\sigma^2 1_{N_w})\tag{28.134}$$
$$z_n^t\sim\mathrm{Dir}(\alpha1_{N_z})\tag{28.135}$$
$$m_{nl}^t|z_n^t\sim\mathrm{Cat}(z_n^t)\tag{28.136}$$
$$x_{nl}^t|m_{nl}^t=k,W^t\sim\mathrm{Cat}(\mathrm{softmax}(w_k^t))\tag{28.137}$$
This is the dynamic topic model [BL06] (Fig. 28.28). Inference: structured mean field using Kalman smoothing for exact inference on the linear-Gaussian chain of the $w_k^t$. Fig. 28.29 applies it to 100 years of *Science*. Amortized inference with learned word embeddings works much better with rare words: the dynamic embedded topic model [DRB19] (p. 969).

### 28.5.4 LDA-HMM (p. 969–971)
LDA treats words as exchangeable and ignores order. An HMM can only model short-range dependencies, so it cannot capture the overall gist of a document; HMMs can generate syntactically correct sentences, but not semantically plausible ones. LDA-HMM [Gri+04]: HMM states handle function/syntactic words; LDA handles content words. For document $n$, states $h_{nl}\in\{0,\dots,H\}$; if $h_{nl}=0$ the word comes from LDA (topic $m_{nl}$), otherwise from the HMM (p. 969–970):
$$p(z_n)=\mathrm{Dir}(z_n|\alpha1_{N_z}),\quad p(m_{nl}=k|z_n)=z_{nk}\tag{28.138–28.139}$$
$$p(h_{n,l}=j|h_{n,l-1}=i)=A_{ij}\tag{28.140}$$
$$p(x_{nl}=d|m_{nl}=k,h_{nl}=j)=\begin{cases}W_{kd}&j=0\\ B_{jd}&j>0\end{cases}\tag{28.141}$$
$W$: topic-word matrix; $B$: HMM state-word emission matrix; $A$: state transition matrix. Inference can be done with collapsed Gibbs sampling, analytically integrating out all continuous quantities (p. 970).

Results ($N_z=200$, $H=20$, Brown+TASA; Table 28.2): the HMM mostly takes syntactic words, LDA the semantic ones. Without the HMM, LDA topics are "polluted" by function words, which is why they are usually removed in preprocessing (p. 970–971). On NIPS (Fig. 28.31) the model separates roles of one word: "return" as verb vs noun; "graph" in "the left graph" (syntactic role) vs "the graph G" (semantic role). A POS tagger could in principle separate the first pair, but LDA-HMM is fully unsupervised, and a word can have the same POS tag but different roles, as with the two uses of "graph" (p. 971). Topic-RNN [Die+17] replaces the HMM by an RNN (p. 971).

### 28.6 ICA (p. 971–978)
The cocktail-party / blind source separation (BSS) problem: sensors record linear mixtures of sources; "blind" means nothing is known about the sources. The same structure arises for EEG/MEG, financial data and any dataset where latent factors mix linearly (Fig. 28.32) (p. 971–972).

**28.6.1 Noiseless ICA.** $x_n\in\mathbb R^D$ observed, $z_n\in\mathbb R^D$ sources (same dimension):
$$x_n=Az_n\tag{28.142}$$
$A$ is an invertible $D\times D$ mixing matrix (generative weights). Prior $p(z_n)=\prod_{j=1}^Dp_j(z_j)$, typically sparse. Each observation is a linear combination of independent components (28.143, printed index form; see Reading notes). Since the model is noiseless,
$$p(z_n|x_n,A)=\delta(z_n-Bx_n),\quad B=A^{-1}\text{ (recognition weights)}\tag{28.144}$$
(p. 972–973). Fig. 28.32: 500 iid samples of a 4d source; ICA matches the true sources up to permutation, while PCA does not (p. 973).

**28.6.2 Need for non-Gaussian priors.** From $x=Az$: $\mathbb E[x]=A\mathbb E[z]$, $\mathrm{Cov}[x]=A\,\mathrm{Cov}[z]A^\top$. Without loss of generality $\mathbb E[z]=0$ (centering) and $\mathrm{Cov}[z]=I$ (since $AA^\top$ can capture any correlation in $x$). So $z$ is uncorrelated with unit variance, as in factor analysis. This does not identify $A$ uniquely (Section 28.3.1.6), so an independent, non-Gaussian prior is needed (p. 973).

Example: two independent uniform sources (Fig. 28.33a), mixed by
$$A=0.3\begin{pmatrix}2&3\\2&1\end{pmatrix}\tag{28.145}$$
(Fig. 28.33b). Full-rank PCA ($K=D$) is ICA with a factored Gaussian prior. It whitens (sphers) the data so that $\mathrm{Cov}[z]=I$, but a further rotation is needed, and the symmetric Gaussian posterior gives no information on the angle. PCA finds the subspace ("half the problem"); ICA with an independent non-Gaussian prior finds the rotation, recovering sources up to permutation and possible sign change (Fig. 28.33d) (p. 974).

Priors are typically super-Gaussian (heavy tails), which helps identifiability. Laplace with mean 0, variance 1:
$$\log p(z)=-\sqrt2|z|-\log\sqrt2\tag{28.146}$$
It is not differentiable at the origin, so ICA more often uses the logistic distribution. With $\mu=0$, $s=\sqrt3/\pi$ (variance 1) and $\mathrm{sech}(x)=1/\cosh(x)$:
$$\log p(z)=\log\mathrm{sech}^2(z/2s)-\log(4s)=-2\log\cosh\!\Big(\tfrac{\pi}{2\sqrt3}z\Big)-\log\tfrac{4\sqrt3}{\pi}\tag{28.147}$$
(p. 974–975).

*Intuition note:* Whitening removes second-order structure, but a Gaussian cloud looks the same after any rotation. A non-Gaussian independent prior makes some rotations look "more independent" than others, which picks out the sources.

**28.6.3 Maximum likelihood.** Change of variables:
$$p_x(x)=p_z(z)|\det(A^{-1})|=p_z(Bx)|\det B|\tag{28.148}$$
Whiten first: $\tilde x=S^{-1/2}U^\top(x-\bar x)$, with $\Sigma=USU^\top$ the SVD of the covariance. Then replace $B$ by an orthogonal $V$:
$$p_x(\tilde x)=p_z(V\tilde x)|\det V|\tag{28.149}$$
$|\det V|$ is constant and is dropped, as is the tilde. The average negative log likelihood is
$$\mathrm{NLL}(V)=-\tfrac1N\log p(X|V)=-\tfrac1N\sum_{j=1}^{L}\sum_{n=1}^N\log p_j(v_j^\top x_n)\tag{28.150}$$
with $v_j$ the $j$-th row of $V$ and $p(z)=\prod_jp_j(z_j)$. Using the empirical expectation,
$$\mathrm{NLL}(V)=\sum_j\mathbb E[G_j(z_j)],\quad z_j=v_j^\top x,\ G_j(z_j)\triangleq-\log p_j(z_j)\tag{28.151}$$
This nonconvex objective is minimized subject to $V$ orthogonal. Options: projected gradient descent, natural gradient [Mac03], or the most popular, the approximate Newton method fast ICA [HO00], used for Fig. 28.32 (p. 975).

**28.6.4 Alternatives to MLE** — the text says each is equivalent to MLE (p. 975).

*28.6.4.1 Maximizing non-Gaussianity* (cf. projection pursuit). Kurtosis is sensitive to outliers. Negentropy:
$$\mathrm{negentropy}(z)\triangleq\mathbb H(\mathcal N(\mu,\sigma^2))-\mathbb H(z)\tag{28.152}$$
with $\mu=\mathbb E[z]$, $\sigma^2=\mathbb V[z]$. It is non-negative because the Gaussian has maximum entropy for fixed variance. Maximize
$$J(V)=\sum_j\mathrm{negentropy}(z_j)=\sum_j\mathbb H(\mathcal N(\mu_j,\sigma_j^2))-\mathbb H(z_j)\tag{28.153}$$
With $\mathbb E[z]=0$, $\mathrm{Cov}[z]=I$ the first term is constant, so
$$J(V)=\sum_j-\mathbb H(z_j)+\text{const}=\sum_j\mathbb E[\log p(z_j)]+\text{const}\tag{28.154}$$
which equals the log-likelihood (28.151) up to sign and constants (p. 976).

*28.6.4.2 Minimizing total correlation.*
$$\mathrm{TC}(z)=\sum_j\mathbb H(z_j)-\mathbb H(z)=D_{\mathrm{KL}}\Big(p(z)\,\Big\|\,\prod_jp_j(z_j)\Big)\tag{28.155}$$
It is zero iff the components of $z$ are mutually independent; minimizing it gives a disentangled representation (Section 21.3.1.1). With $z=Vx$: $\mathrm{TC}(z)=\sum_j\mathbb H(z_j)-\mathbb H(Vx)$ (28.156). For orthogonal $V$, $\mathbb H(Vx)=\mathbb H(x)$ is constant, so $\mathrm{TC}(z)=\sum_k\mathbb H(z_k)$ up to that constant. Minimizing it is equivalent to maximizing negentropy, hence to MLE (p. 976).

*28.6.4.3 InfoMax.* Let $z_j=\phi(v_j^\top x)+\epsilon$, $\epsilon\sim\mathcal N(0,1)$, $\phi$ a nonlinear scalar function. Maximize $\mathbb I(x;z)=\mathbb H(z)-\mathbb H(z|x)$; the second term is constant for constant-variance noise. One can show $\mathbb H(z)$ can be approximated by
$$\mathbb H(z)=\sum_j\mathbb E[\log\phi'(v_j^\top x)]+\log|\det V|\tag{28.157}$$
The last term drops for orthogonal $V$. If $\phi$ is a cdf, $\phi'$ is its pdf and this is equivalent to the log likelihood. For the logistic $\phi=\sigma$ the pdf is the logistic distribution. The text writes $\log\phi'(z)=\log\cosh(z)$ and says this matches (28.147) up to irrelevant constants. Conclusion: InfoMax is equivalent to MLE (p. 977).

**28.6.5 Sparse coding.** Allow Gaussian observation noise, a non-square $W$, and a Laplace prior:
$$p(z,x)=\Big[\prod_k\mathrm{Laplace}(z_k|0,1/\lambda)\Big]\mathcal N(x|Wz,\sigma^2I)\tag{28.158}$$
Each $x$ is a sparse combination of columns of $W$ (basis functions); $z$ holds the weights. This is sparse factor analysis with sparsity in the code $z$, not in $W$. Not all basis functions are active for any given observation, so $K$ can be allowed to exceed $D$ (overcomplete representation) (p. 977). For $N$ examples,
$$-\log p(X,Z|W)=\tfrac1{2\sigma^2}\sum_{n=1}^N\|x_n-Wz_n\|_2^2+\lambda\|z_n\|_1+\text{const}\tag{28.159}$$
$$=\tfrac1{2\sigma^2}\|X-WZ\|_F^2+\lambda\|Z\|_{1,1}+\text{const}\tag{28.160}$$
- MAP inference of $Z$ for fixed $W$ is **sparse coding**, solvable by sparse linear regression (Section 15.2.6). Footnote 6: a network can approximate the $\ell_1$ solution (predictive sparse decomposition).
- Estimating $W$ while marginalizing out $Z$ is **dictionary learning**. Because that is hard, one usually optimizes $W$ and $Z$ jointly ("maxing out" $Z$) by alternating: $Z|W$ is sparse regression, $W|Z$ is least squares (p. 977).

Fig. 28.34: on natural image patches (centered, unit norm), sparse coding learns bar and edge detectors like simple cells in mammalian primary visual cortex [OF96]; PCA gives sinusoidal gratings. Footnote 7: image covariance is translation invariant, and the eigenvectors of such a matrix are sinusoids, so PCA finds a Fourier basis (p. 978).

**28.6.6 Nonlinear ICA.** Various extensions exist; the resulting methods resemble variational autoencoders (Chapter 21) (p. 978).

## Toy example (ours, not from the text)
Two independent sources, each $\pm1$ with probability ½ (non-Gaussian). Mix them by an orthogonal matrix $R=\tfrac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$, so $x=Rz$.
- $z=(1,1)\to x=(0,\sqrt2)$; $(1,-1)\to(\sqrt2,0)$; $(-1,1)\to(-\sqrt2,0)$; $(-1,-1)\to(0,-\sqrt2)$, each with probability ¼.
- Whitened: $\mathbb E[x_1]=0$, $\mathbb E[x_1^2]=(0+2+2+0)/4=1$, same for $x_2$, and $\mathbb E[x_1x_2]=0$ since every product is 0. So the data are uncorrelated with unit variance.
- But $x_1,x_2$ are dependent: $P(x_1=\sqrt2,x_2=\sqrt2)=0$, while $P(x_1=\sqrt2)P(x_2=\sqrt2)=\tfrac14\cdot\tfrac14=\tfrac1{16}$.
- Rotate back with $V=R^\top=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}$: $V(0,\sqrt2)=(\sqrt2,\sqrt2)/\sqrt2=(1,1)$. Now $P(z_1=1,z_2=1)=\tfrac14=\tfrac12\cdot\tfrac12$, which is independence.
- If the sources were $\mathcal N(0,I)$, every rotation of $x$ would again be $\mathcal N(0,I)$ with independent components, so no rotation would be preferred. This is the identifiability argument of p. 974.

## Concepts
- [[gp-lvm]] (new) — GP-LVM: GP prior on a map from unknown latent inputs $Z$ to $Y$; point estimate of $Z$ (p. 959)
- [[nmf]] (new) — non-negative matrix factorization; MLE of the GaP model with $\alpha_k=\beta_k=0$ (p. 961)
- [[gamma-poisson-model]] (new) — gamma prior on latents, Poisson likelihood (p. 960)
- [[multinomial-pca]] (new) — Dirichlet latents on the simplex with categorical likelihood; admixture / mixed membership (p. 962)
- [[lda]] (new) — latent Dirichlet allocation: per-document Dirichlet topic mixture, per-word topic indicator (p. 963–964)
- [[correlated-topic-model]] (new) — LDA with logistic-normal prior, so topics can correlate (p. 967)
- [[dynamic-topic-model]] (new) — topic logits follow a Gaussian random walk over time (p. 969)
- [[lda-hmm]] (new) — HMM for syntactic words combined with LDA for semantic words (p. 969–970)
- [[ica]] (new) — $x=Az$ with independent, non-Gaussian sources; noiseless, square (p. 972)
- [[whitening]] (new) — linear transform making data covariance the identity; leaves a rotation (p. 974–975)
- [[negentropy]] (new) — entropy of a Gaussian with same variance minus entropy of $z$; non-Gaussianity measure (p. 976)
- [[total-correlation]] (new) — $\sum_j\mathbb H(z_j)-\mathbb H(z)$; KL from joint to product of marginals (p. 976)
- [[infomax]] (new) — maximize mutual information between input and noisy nonlinear encoder output (p. 976–977)
- [[sparse-coding]] (new) — MAP $Z$ for fixed $W$ under Laplace prior and Gaussian noise; dictionary learning estimates $W$ (p. 977)
- [[kl-divergence]] — appears in the total-correlation formula (p. 976)
- [[variational-inference-elbo]] — variational EM and mean field are used to fit mPCA, LDA, CTM, DTM (p. 963, 966–967, 969)
- [[gibbs-sampling]] — collapsed Gibbs for LDA and LDA-HMM (p. 966, 970)
- [[marginal-likelihood-evidence]] — evidence approximation for choosing the number of topics (p. 967)
- [[cross-validation-loo-waic]] — test-set log likelihood for choosing the number of topics (p. 967)

## Canonical instances
- [[gplvm-mocap]] — 2d GP-LVM embedding of motion-capture poses (p. 959–960)
- [[nmf-faces]] — NMF learns parts, VQ prototypes, PCA global signed bases (p. 961)
- [[senate-rollcall-mpca]] — 5-bloc mPCA on 2003 Senate votes (p. 962–963)
- [[tasa-play-topics]] — three topics for three senses of "play" (p. 965–966)
- [[science-ctm]] — correlated topics in *Science* 1990–1999 (p. 968)
- [[science-dtm]] — neuroscience topic drifting over 100 years (p. 969)
- [[lda-hmm-brown-tasa-nips]] — syntax/semantics split, "return", "graph" (p. 970–972)
- [[ica-uniform-sources]] — PCA whitens uniform sources, ICA recovers them (p. 973–974)
- [[sparse-coding-image-patches]] — edge detectors vs PCA sinusoids (p. 978)

## Bridges (candidates)
- [same-math] ICA objective via negentropy / total correlation / InfoMax ↔ Information theory: entropy, KL divergence, mutual information — the text derives the same objective from each (p. 976–977).
- [same-math] Sparse coding MAP objective (28.160) ↔ Regularized regression: lasso, Gaussian noise with $\ell_1$ penalty (p. 977).
- [same-math] Dynamic topic model chain on $w_k^t$ ↔ State-space models: linear-Gaussian chain, Kalman smoothing (p. 969).
- [structural-analogy] Topic proportions $z_n$ (mixed membership) ↔ Social science: individuals partly belonging to several blocs (roll-call example) (p. 963).
- [structural-analogy] LDA vs mixture models ↔ Clustering: mixed vs single-cluster assignment (p. 963).
- [metaphor] Cocktail-party problem ↔ separating mixed causes in observational data; the source gives no such link.

## Questions this raises
- Under what exact conditions on the source distributions is ICA identifiable? The text only illustrates this with the uniform/Gaussian contrast (p. 974).
- Can the number of topics $N_z$ be chosen reliably? The text lists four approaches without comparing them (p. 967).
- How good are collapsed Gibbs and mean-field approximations compared with spectral methods that have guarantees? What do the anchor-word assumptions cost (p. 966–967)?
- How do the nonlinear ICA methods mentioned at the end relate to VAEs (p. 978)?

## Reading notes
- **Unit boundaries.** Starts at printed p. 959 in the middle of the GP-LVM discussion ("model is as follows"; the section heading is on the previous page, not given). Ends at p. 978 with 28.6.6, the last section in these pages. Source note: split at a section boundary. Printed page = pdf − 34.
- Table 28.1 (summary of 28.4 models) is not in these pages.
- Eq. 28.126 prints $|K_z|$ whereas $K_\sigma=K+\sigma^2I$ is defined; the subscripts look inconsistent (reproduced as printed).
- Eq. 28.143 as printed, $x_{nj}=\sum_iA_{ij}z_{nj}$, does not match $x=Az$. Index-wise, (28.142) gives $x_{ni}=\sum_jA_{ij}z_{nj}$ (added step).
- Eq. 28.150 sums $j=1..L$ with $L$ undefined (presumably $D$). Eq. 28.160 writes $\|X-WZ\|_F^2$ although $X$ is said to hold examples in rows; shapes agree if $X$ is $D\times N$ and $Z$ is $K\times N$ (my reading).
- Eq. 28.157 discussion: the text states $\log\phi'(z)=\log\cosh(z)$ matches (28.147); (28.147) has $-2\log\cosh(\cdot)$ with a scaled argument. I could not reconcile them literally; treat the match as "up to constants and scaling".
- The Dirichlet covariance $-\alpha_i\alpha_j$ (p. 967) is reproduced as printed.
- Figures 28.23 and 28.28 label topic indicators $c_{nl}$ and $s_{nl}$; the text uses $m_{nl}$.
- Section 28.5.1.3 refers to Supplementary Sections 28.1.1–28.1.2, not included here.

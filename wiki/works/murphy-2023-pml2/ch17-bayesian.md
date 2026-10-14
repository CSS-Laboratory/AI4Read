---
id: murphy-2023-pml2/ch17-bayesian
work: murphy-2023-pml2
unit: "17 Bayesian neural networks"
pages: 647-680
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Bayesian neural networks

## L0 — One line
Because many different parameter settings of a deep network fit the training data well yet generalize differently, averaging predictions over the posterior (approximately, e.g. with ensembles of distinct modes) can improve accuracy and uncertainty representation. How well this works depends on the prior, the architecture and the approximation used.

## L1 — The gist (≤ 120 words)
How can Bayesian inference be applied to deep neural networks, and why might it help? The chapter covers priors over weights, functions and architectures. It surveys approximate posteriors: MC dropout, Laplace, variational inference, expectation propagation, last-layer methods, MCMC, SGD-trajectory methods and deep ensembles. It then covers ways to approximate predictions, and tempered ("cold") posteriors. It argues that averaging over many good solutions can improve generalization. It also shows where Bayesian averaging can fail: default priors under covariate shift, and overconfidence on out-of-distribution inputs. Finally it covers online inference and a hierarchical multi-task example. Posterior approximations differ in what they capture; deep ensembles capture several modes.

**Prerequisites:** posterior predictive distribution; Gaussian priors and Laplace approximation; ELBO/KL divergence; HMC/SGLD basics; Jacobian and Hessian; Kalman filter idea; hierarchical models.

## L2 — Key ideas (5–10 bullets)
- Networks are underspecified: many parameter settings fit the data but generalize differently. The Bayesian answer is to average predictions over the posterior, Eq. (17.1) (p. 647).
- A Gaussian prior on weights induces a prior over functions. Scale hyperparameters control steepness, centre shifts and "wiggliness" for sigmoid nets. The architecture can shape this prior even more strongly (pp. 648–651).
- Approximate posteriors differ in what they capture. Laplace (a Gaussian fitted at the most probable parameters, the MAP) is explicitly described as highly local (p. 653), and variational inference (VI) is drawn as local uncertainty around a mode (Fig. 17.6, p. 658). Hamiltonian Monte Carlo (HMC) is generally considered the "gold standard" but needs the full data at each step. Deep ensembles and MultiSWAG (a mixture of Gaussians, one per mode) represent several modes (pp. 651–660).
- Predictions from an approximate posterior can often be improved by linearizing the network around the MAP (GLM predictive); the Laplace bridge turns a Gaussian over logits into a Dirichlet that shows uncertainty about label probabilities. Distillation (training a fast student network to mimic the Monte Carlo average) speeds up prediction (pp. 661–664).
- Tempered posteriors raise the likelihood to a power $\alpha$; for a Gaussian prior the cold posterior is equivalent, with $\alpha = 1/T$. The text, citing [Kap+22], states that the cold-posterior effect is a consequence of underrepresenting label (aleatoric) uncertainty (pp. 664–665).
- Why Bayesian averaging helps: flat minima, mode connectivity, low effective dimensionality, and a prior (architecture) that makes structured data much more probable than random labels (pp. 665–669).
- "Being Bayesian" is not automatically robust. With default priors the Bayesian model average (BMA) can be hurt by covariate shift (a change in the input distribution), and MLP-based BNNs can be overconfident on out-of-distribution (OOD) inputs. A good hypothesis class and prior are needed (pp. 670–671).
- Online inference (data arriving in a stream) for networks uses sequential Laplace/elastic weight consolidation (EWC), the extended Kalman filter (EKF), assumed density filtering/probabilistic backpropagation (ADF/PBP) and variational continual learning (pp. 672–677).
- A hierarchical BNN pools shared structure across related tasks and beat separate MLPs in the multimoons example (pp. 677–680).

## L3 — Walkthrough

### 17.1 Introduction (p. 647)
- DNNs are usually trained by (penalized) maximum likelihood, which gives a single parameter setting. Large flexible models can represent many functions that fit the training data well yet generalize differently. This is called **underspecification** (p. 647).
- Considering all these models together can improve accuracy and uncertainty representation. This is done with the posterior predictive and Bayesian model averaging (BMA):
$$p(y|x,\mathcal D)=\int p(y|x,\theta)\,p(\theta|\mathcal D)\,d\theta,\qquad p(\theta|\mathcal D)\propto p(\theta)p(\mathcal D|\theta)\tag{17.1}$$
- Main challenges: specifying priors, and computing the posterior with many parameters and large datasets. Applying Bayes to DNNs is **Bayesian deep learning (BDL)**. **Deep Bayesian learning (DBL)** is the reverse: using deep models (e.g. amortized inference networks) to speed up inference for classical models (p. 647).

> **Intuition note.** A trained network is one guess about the world. When many guesses fit the data well but generalize differently, averaging them can improve accuracy and uncertainty estimates compared with trusting one. Eq. (17.1) is that average, weighted by posterior probability.

### 17.2 Priors for BNNs

**17.2.1 Gaussian priors (pp. 648–650).**
- MLP with $L-1$ hidden layers, activation $\varphi$, linear output (softmax etc. is folded into the loss):
$$f(x;\theta)=W_L(\cdots\varphi(W_1x+b_1))+b_L\tag{17.4}$$
(one hidden layer: $W_2\varphi(W_1x+b_1)+b_2$, Eq. 17.2; two: Eq. 17.3).
- Common prior: factored Gaussian, $W_\ell\sim\mathcal N(0,\alpha_\ell^2 I)$, $b_\ell\sim\mathcal N(0,\beta_\ell^2 I)$ (17.5).
- Xavier/Glorot initialization sets $\alpha_\ell^2=\frac{2}{n_{in}+n_{out}}$ (17.6). LeCun initialization sets $\alpha_\ell^2=\frac{1}{n_{in}}$ (17.7). Here $n_{in}$ is the fan-in (weights coming into a neuron) and $n_{out}$ the fan-out.
- Reparameterize: $W_\ell=\alpha_\ell\eta_\ell$, $\eta_\ell\sim\mathcal N(0,I)$, $b_\ell=\beta_\ell\epsilon_\ell$, $\epsilon_\ell\sim\mathcal N(0,I)$ (17.8). Each hyperparameter setting then defines a random function
$$f(x;\alpha,\beta)=\alpha_L\eta_L(\cdots\varphi(\alpha_1\eta_1x+\beta_1\epsilon_1))+\beta_L\epsilon_L\tag{17.9}$$
- Figure 17.1 samples 1-d functions from a sigmoid MLP, $L=2$, baseline $\alpha_1=5,\beta_1=1,\alpha_2=1,\beta_2=1$.
  - Raising $\alpha_1$ (to 25) makes the sigmoid shapes steeper.
  - Raising $\beta_1$ (to 5) lets the sigmoid centre shift further from the origin.
  - Raising $\alpha_2$ (to 5) makes functions more "wiggly" (larger dynamic range) (p. 649).
- This is specific to sigmoids. For ReLU with all biases zero ($\beta_\ell=0$), changing $\alpha_\ell$ only rescales the output, using $\varphi(\alpha z)=\alpha\varphi(z)$ for positive $\alpha$:
$$f(x;\alpha,\beta=0)=\alpha_L\cdots\alpha_1\,f(x;\alpha=1,\beta=0)\tag{17.10–17.11}$$
- In general the ratio of $\alpha$ to $\beta$ matters for how signals propagate through a randomly initialized model (p. 649). Random initialization is like sampling from this function prior. For infinitely wide networks the prior can be derived analytically: the neural network Gaussian process (Sec. 18.7) (p. 650).

**17.2.2 Sparsity-promoting priors (p. 650).** Priors such as the Laplace encourage most weights (or CNN channels) to be zero.

**17.2.3 Learning the prior (p. 650).**
- Grid search on cross-validation loss over $\alpha,\beta$ grows exponentially with the number of hyperparameters.
- Alternative: gradient-based optimization of the marginal likelihood (empirical Bayes / evidence maximization) (17.12). It can give sparse models, but computing it is difficult for large networks. The equation is printed with $\log$ inside the integral; see Reading notes.
- Learning the prior is more meaningful on a separate but related dataset. [SZ+22]: train on a large $\mathcal D_1$ to get $\hat\theta_1$, derive a low-rank Gaussian with SWAG, and use it as an informative prior when fine-tuning on $\mathcal D_2$ (MAP or approximate posterior). They call this "Bayesian transfer learning".

**17.2.4 Priors in function space (p. 650).** The link between parameter prior and preferred functions is typically not transparent. Options: priors from desired invariances; residual pathway priors [FBW21] for encoding locality, independencies and symmetries without constraining flexibility; kernel/GP-based priors (Sec. 18.1).

**17.2.5 Architectural priors (p. 651).**
- Architecture can have an even larger effect on the induced function distribution than the parametric prior. A CNN encodes translation equivariance and hierarchical structure. Transformers have weaker inductive bias and often need more data. Neural architecture search can be seen as structural prior learning.
- An untrained random CNN often works well for low-level image tasks (denoising, super-resolution, inpainting) ("deep image prior" [UVL18]). Pinto & Cox found untrained CNNs with the right structure can do well at face recognition. Zhang et al. found random CNN features can greatly improve other models such as kernel methods.

> **Intuition note.** A prior over weights is really a prior over functions. The author stresses that the architecture can matter even more than the weight-scale hyperparameters.

### 17.3 Posteriors for BNNs (p. 651)
Many approximate inference schemes exist, each with strengths and limits.

**17.3.1 Monte Carlo dropout (pp. 651–652).**
- Keep dropout on at test time. Drop hidden units with Bernoulli($p$), repeat $S$ times to get $S$ models, and average equally:
$$p(y|x,\mathcal D)\approx\frac1S\sum_{s=1}^S p(y|x,\theta^s)\tag{17.13}$$
where $\theta^s$ is the MAP estimate with some connections randomly dropped.
- Figure 17.2 (LeNet on rotated MNIST "1"s): it captures uncertainty from OOD inputs, yet the last three images are classified as 7 in the probabilities even though the logits show high uncertainty.
- Drawbacks: slow at test time (fixable by distillation, 17.3.10.3). **Objection ([Osb16; LF+21]):** MCD does not give proper uncertainty. It is variational inference only under a degenerate approximation, a mixture of two deltas (at 0 and at the MLE). This does not converge to the true posterior (a delta at the MLE) as data grow, because dropout probability $p$ stays constant. The pathology can be fixed if the noise rate is optimized [GHK17] (p. 652).

**17.3.2 Laplace approximation (pp. 652–653).**
- Gaussian centred at the MAP $\theta^*$. The text says "posterior prediction matrix" (read as the precision) equals the Hessian of the negative log joint at the mode. It is simple and can turn a pretrained model into a Bayesian one. The Hessian is expensive, and may not be positive definite because DNN log likelihoods are non-convex (p. 652).
- Notation ([Dax+21]): $f(x_n,\theta)\in\mathbb R^C$, $\theta\in\mathbb R^P$, residual $r(y;f)=\nabla_f\log p(y|f)$, per-input noise term $\Lambda(y;f)=-\nabla_f^2\log p(y|f)$, Jacobian $J\in\mathbb R^{C\times P}$ with $[J_\theta(x)]_{ci}=\partial f_c/\partial\theta_i$, Hessian $H\in\mathbb R^{C\times P\times P}$ (p. 652).
$$\nabla_\theta\log p(y|f(x,\theta))=J_\theta(x)^{T}r(y;f)\tag{17.14}$$
$$\nabla^2_\theta\log p(y|f(x,\theta))=H_\theta(x)^{T}r(y;f)-J_\theta(x)^{T}\Lambda(y;f)J_\theta(\theta)\tag{17.15}$$
- Dropping the network Hessian $H$ gives the **generalized Gauss–Newton (GGN)** approximation. It is guaranteed positive definite (the full Hessian is not) and cheaper (p. 653).
- With Gaussian prior $\mathcal N(\theta|m_0,S_0)$: $p(\theta|\mathcal D)\approx\mathcal N(\theta^*,\Sigma_{GGN})$ with
$$\Sigma_{GGN}^{-1}=\sum_{n=1}^N J_{\theta^*}(x_n)^T\Lambda(y_n;f_n)J_{\theta^*}(x_n)+S_0^{-1}\tag{17.16}$$
- Inversion costs $O(P^3)$. A diagonal approximation costs $O(P)$ time and space. KFAC [RBB18a, MG15] approximates each layer's covariance by a Kronecker product.
- Limitation: the Laplace approximation is highly local, using only the curvature at the MAP, so it may suffer from local optima and give overly compact or diffuse representations. Curvature is used only after training. VI can be more accurate for comparable cost (p. 653).

**17.3.3 Variational inference (pp. 653–654).**
- Fixed-form VI: choose $q_\psi(\theta)$ (often Gaussian $\mathcal N(\mu,\Sigma)$) and minimize $D_{KL}(q\|p)$ over $\psi$. The reparameterization trick gives low-variance ELBO gradients. The optimum often differs from the Laplace solution (p. 653).
- History: Hinton & Camp [HC93]; [Gra11] used a diagonal Gaussian (one univariate Gaussian per parameter, Fig. 17.3). **Bayes by backprop (BBB)** [Blu+15] adds the reparameterization trick. It is essentially SVI (Alg. 10.2) with the DNN likelihood and Gaussian prior and posterior (p. 653).
- Extensions (p. 654): local reparameterization trick [KSW15] (sample activations $a=Wz$, not weights; lower variance); VOGN [Osa+19a, Kha+18] (noisy natural gradient descent where the noise emulates VI); low-rank plus diagonal [Mis+18]; NAGVAC [Tra+20b], rank-one plus diagonal with only 3 times as many parameters as a point estimate and an analytic natural gradient.

**17.3.4 Expectation propagation (p. 654).** EP locally optimizes $D_{KL}(p\|q)$ instead of $D_{KL}(q\|p)$ ($p$ exact, $q$ approximate). ADF is a special case of EP (the first pass). [HLA15a] applied ADF to BNNs as **probabilistic backpropagation (PBP)**, with a Gaussian factor per parameter (details in 17.5.3).

**17.3.5 Last layer methods (pp. 654–655).**
- "Neural-linear": be Bayesian only about the final-layer weights, MAP for the rest. With logits $z=w_L^T\phi(x;\theta)$ this is a Bayesian GLM. Compute $p(w_L|\mathcal D)=\mathcal N(\mu_L,\Sigma_L)$ (e.g. Laplace). Then
$$p(z|x,\mathcal D)=\mathcal N(z\,|\,\mu_L\phi(x),\ \phi(x)\Sigma_L\phi(x)^T)\tag{17.17}$$
(as printed). It can pass through the softmax to give $p(y|x,\mathcal D)$.
- [KHH20]: it can reduce overconfidence far from training data. It ignores uncertainty in earlier layers, where most parameters reside.

**17.3.6 SNGP (p. 655).**
- Deep kernel learning feeds DNN features into a GP kernel. Problem: in classification, training log likelihood does not drop if far-apart points are projected close together on the correct side of the boundary. So OOD inputs can look close to the training set.
- SNGP (spectrally normalized GP) [Liu+20d, Liu+22a] constrains the feature extractor to be "distance preserving" via spectral normalization of the weights (bounding the Lipschitz constant). This preserves information needed for confidence but possibly irrelevant to the label, helping OOD detection.

**17.3.7 MCMC methods (pp. 655–656).**
- Neal [Nea96] used HMC. It is "generally considered the gold standard" because it makes no strong assumption on the posterior's form. Figure 17.4 fits a shallow MLP to two-moons by HMC; posterior std grows away from the training data (p. 655).
- Limitation: standard MCMC needs the full training set at each step. Stochastic-gradient MCMC (SGLD, Sec. 12.7.1) uses minibatches (p. 656).

**17.3.8 Methods based on the SGD trajectory (pp. 656–657).**
- [MHB17; SL18; CS18]: under some assumptions, SGD iterates at a fixed learning rate correspond to samples from a Gaussian approximation $\mathcal N(\theta|\hat\theta,\Sigma)$ centred at a local mode. This is like SG-MCMC without explicit noise and with a constant learning rate (p. 656).
- [Izm+18]: these SGD solutions surround the periphery of points of good generalization (Fig. 17.5), partly because SGD does not converge to an optimum unless the learning rate is annealed to 0. **Stochastic weight averaging (SWA):** average $S$ SGD samples, e.g. one per epoch, $\bar\theta=\frac1S\sum_s\theta_s$. The result tends to lie in a broader minimum than the SGD solutions and generalizes better (p. 656).
- Related: Polyak–Ruppert averaging (typically decaying learning rate, exponential moving average, mainly variance reduction); snapshot ensembles and fast geometric ensembles (cyclical learning rate, average the predictions $\frac1S\sum p(y|x,\theta_s)$ rather than the parameters). SWA can be seen as approximating the BMA of (17.1) with a single model at a flat "centre of mass" (pp. 656–657).
- **SWAG** [Mad+19]: Gaussian $\mathcal N(\theta|\bar\theta,\Sigma)$ with SWA mean and $\Sigma=(\Sigma_{diag}+\Sigma_{lr})/2$, where $\Sigma_{diag}=\mathrm{diag}(\overline{\theta^2}-(\bar\theta)^2)$, $\overline{\theta^2}=\frac1S\sum_s\theta_s^2$, and $\Sigma_{lr}=\frac1S\Delta\Delta^T$ is the sample covariance of the last $K$ deviations $\Delta_i=\theta_i-\bar\theta_i$ ($\bar\theta_i$ = running average of the first $i$ samples). It scales to large ResNets and ImageNet, with improved accuracy and calibration over SGD and no extra training overhead (p. 657).

**17.3.9 Deep ensembles (pp. 657–661).**
- Modern DNN posteriors are highly multi-modal, and different modes give very different functions, while functions within one mode may be similar. A local approximation therefore underestimates uncertainty and generalizes worse (p. 657).
- **Deep ensemble:** train $M$ models and use an equally weighted mixture of deltas at the MAP estimates:
$$p(\theta|\mathcal D)\approx\frac1M\sum_{m=1}^M\delta(\theta-\hat\theta_m)\tag{17.18}$$
Members can differ in seed, hyperparameters, architecture. A repulsive term can enforce functional diversity. Combining distinct modes is more effective than combining samples from one basin, especially under dataset shift (Fig. 17.6; p. 658).
- **17.3.9.1 MultiSWAG** [WI20]: fit a SWAG Gaussian in each mode, giving a Gaussian mixture
$$p(\theta|\mathcal D)\approx\frac1M\sum_{m=1}^M\mathcal N(\theta|\hat\theta_m,\Sigma_m)\tag{17.19}$$
It averages across basins and within each basin, and can produce any number of samples $S>M$ any-time (p. 658).
- **17.3.9.2 Random priors** [OAC18]: standard members trained on the same data can be too similar. Bootstrap sampling is one fix. Another: member $g_i(x;\theta_i)=t_i(x;\theta_i)+\beta p_i(x)$, a trainable net plus a fixed random "prior network" (17.20), with $\beta\ge0$ controlling data-independent variation. The trainable net models the residual. Figure 17.7: larger $\beta$ means more trust in the random priors, less in the data, hence a more diffuse posterior (pp. 658–659).
- **17.3.9.3** All BNN inference is approximate. Deep ensembles can approximate the BMA better than single-basin marginalization, because point masses from different basins represent greater functional diversity (p. 659).
- **17.3.9.4 vs classical ensembles:** bagging and random forests get diversity from data perturbation, which is necessary when the base learner is convex. Deep ensembles use the same data and features. Diversity comes from different initializations, seeds and SGD noise acting on a nonconvex loss. Explicitly enforcing diversity can provably improve performance [TB22] (pp. 659–660).
- **17.3.9.5 vs mixtures of experts and stacking:** with weights $p(m|\mathcal D)$ (marginal likelihood of model $m$), in the large-sample limit the mixture concentrates on the MAP model, so one component is selected. Deep ensembles always use $M$ equal weights. So BMA is not the same as ensembling, and ensembling can enlarge the expressive power of the predictive distribution compared to BMA. With input-dependent weights
$$p(y|x,\mathcal D)=\sum_m w_m(x)\,p(y|x,\theta_m)\tag{17.21}$$
the method is a mixture of experts if weights are non-zero and sum to one, and **stacking** if any positive weighted combination is allowed (weights usually fitted on hold-out data for robustness to misspecification) (p. 660).
- **17.3.9.6 Batch ensemble** [WTB20]: deep ensembles cost $M$ times the memory and time. Share slow weights $W$; member $m$ has fast weights $F_m$, with $W_m=W\odot F_m$ and rank-one $F_m=s_mr_m^T$ (Fig. 17.8) (p. 660). Memory overhead is $2M$ vectors per layer, negligible next to the quadratic cost of $W^l$. One layer's output:
$$y_n^m=\varphi(W_m^Tx_n)=\varphi((W\odot s_mr_m^T)^Tx_n)=\varphi(W^T(x_n\odot s_m)\odot r_m)\tag{17.22}$$
Vectorized for a minibatch, with $r_m,s_m$ replicated along the $B$ rows to form $R_m,S_m$:
$$Y_m=\varphi(((X\odot S_m)W)\odot R_m)\tag{17.23}$$
(Shapes, added step: $X,S_m$ are $B\times n_{in}$, $W$ is $n_{in}\times n_{out}$, $R_m$ and $Y_m$ are $B\times n_{out}$.) For training diversity, split the minibatch into $M$ sub-batches, sub-batch $m$ training $W_m$ (batch size $B/M$ per member). At test time replicate each input $M$ times (batch size $BM$). Batch ensemble outperforms MC dropout at negligible extra memory; the best result was batch ensemble plus MC dropout, in some cases near naive ensembles (p. 661).

> **Intuition note.** Local methods (Laplace, VI, SWAG) describe one hill of the posterior. Ensembles describe several hills, each roughly. Since different modes give very different functions, the text says a local approximation underestimates uncertainty; ensembles address this by covering several hills (p. 657).

**17.3.10 Approximating the posterior predictive (pp. 661–664).**
- With $q(\theta)\approx p(\theta|\mathcal D)$: $p(y|x,\mathcal D)=\int q(\theta)p(y|x,\theta)d\theta$ (17.24), approximated by Monte Carlo
$$p(y|x,\mathcal D)\approx\frac1S\sum_{s=1}^Sp(y|f(x,\theta^s)),\ \theta^s\sim q\tag{17.25}$$
- **17.3.10.1 Linearized (GLM) predictive** [IKB21]: samples from $q$ can give bad predictions because $f$ is highly nonlinear in $\theta$ and may behave differently far from the MAP. Replace $f$ by its linearization at $\theta^*$:
$$f^{\theta^*}_{lin}(x,\theta)=f(x,\theta^*)+J(x)(\theta-\theta^*)\tag{17.26}$$
with $J_{\theta^*}=\partial f/\partial\theta|_{\theta^*}$, called a "$P\times C$" Jacobian on p. 662 (see Reading notes). Then $p(y|x,\mathcal D)\approx\frac1S\sum_sp(y|f^{\theta^*}_{lin}(x,\theta^s))$ (17.27), which often works better than (17.25). It is linear in $\theta$ but nonlinear in $x$, so a GLM. For Gaussian $p(\theta|\mathcal D)\approx\mathcal N(\mu,\Sigma)$ the logits satisfy
$$p(z|x,\mathcal D)\approx\mathcal N(z\,|\,f(x,\mu),\,J(x)^T\Sigma J(x))\tag{17.28}$$
Using a probit approximation to the softmax, this Gaussian can be passed analytically through the final layer (Eq. 15.150), or the Laplace bridge can be used (p. 662).
- **17.3.10.2 Laplace bridge** [HKH22]: a point estimate $p_c$ of class probabilities conveys no uncertainty in the probability itself. Represent the output as a Dirichlet $\mathrm{Dir}(\pi|\alpha)$ instead of Categorical. This suits "soft" labels and ambiguous labels. One can train a model to output Dirichlet parameters (prior network [MG18]), or derive them post hoc from a Gaussian over logits $\mathcal N(z|m,V)$:
$$\alpha_i=\frac1{V_{ii}}\left(1-\frac2C+\frac{\exp(m_i)}{C^2}\sum_{j=1}^C\exp(-m_j)\right)\tag{17.29}$$
$C$ = number of classes; $p_c=\mathbb E[\pi_c]=\alpha_c/\alpha_0$, $\alpha_0=\sum_c\alpha_c$ (p. 662). The derivation assumes the Gaussian terms sum to zero, so first project onto that constraint:
$$p(z|x,\mathcal D)=\mathcal N\!\left(z\,\Big|\,m-\frac{V\mathbf{1}\mathbf{1}^Tm}{\mathbf 1^TV_*\mathbf 1},\ V-\frac{V\mathbf1\mathbf1^TV}{\mathbf1^TV\mathbf1}\right)=\mathcal N(z|m',V')\tag{17.30}$$
(printed with $V_*$ in one denominator; see Reading notes). To avoid sparse $\alpha$, [HKH22] also rescale: $m''=m'/\sqrt c$, $V''=V'/c$ with $c=\big(\sum_{ii}V'_{ii}\big)/\sqrt{C/2}$ (p. 663).
  - Dirichlet marginals are Beta, so marginals over each label's probability are easy. This gives an adaptive top-$k$ set, similar in spirit to conformal prediction but Bayesian (per-instance uncertainty). Sort labels by expected probability to get $\tilde\alpha$, then
$$p(\pi_1|x,\mathcal D)=\mathrm{Beta}(\tilde\alpha_1,\alpha_0-\tilde\alpha_1)\tag{17.31}$$
Compute the other marginals similarly and return all labels with significant overlap with the top label. Figure 17.9: this gives variable-sized outputs (pp. 663–664).
- **17.3.10.3 Distillation:** MC prediction is $S$ times slower than plug-in. Train a parametric "student" $p_s$ to minimize $\mathbb E[D_{KL}(p_t(y|x)\|p_s(y|x))]$, where the teacher $p_t$ is from (17.25). This was first proposed as "dark knowledge" [HVD14]. "Bayesian dark knowledge" [Kor+15] distills an HMC teacher; [BPK16; GBP18] distil MC dropout. A student is typically less flexible and may be overconfident, so a mixture-distribution student is safer (p. 664).

**17.3.11 Tempered and cold posteriors (pp. 664–665).**
- Classification likelihood: $p(y|x,\theta)=\mathrm{Cat}(y|\mathrm{softmax}(f(x;\theta)))$ (17.32). In practice BNNs often give better predictive accuracy if the likelihood is raised to a power $\alpha$ (tempered, $\alpha$- or power posterior):
$$\log p_{tempered}(\theta|\mathcal D)=\alpha\log p(y|X,\theta)+\log p(\theta)+\text{const}\tag{17.33}$$
- Cold posterior, $p_{cold}\propto p(\theta|X,y)^{1/T}$:
$$\log p_{cold}(\theta|\mathcal D)=\frac1T\log p(y|X,\theta)+\frac1T\log p(\theta)+\text{const}\tag{17.34}$$
"Cold" means $T<1$ (p. 664).
- For a Gaussian prior, the cold posterior equals the tempered posterior with a different prior variance:
$$\tfrac1T\log\mathcal N(\theta|0,\sigma^2_{cold}I)=-\tfrac1{2T\sigma^2_{cold}}\sum_i\theta_i^2+\text{const}\tag{17.35}$$
This equals $\log p_{tempered}(\theta)$ if $\sigma^2_{tempered}=T\sigma^2_{cold}$. Both methods reweight the likelihood by $\alpha=1/T$ (p. 665).
- Explanation ([Kap+22], as reported): cold posteriors result from underrepresenting aleatoric (label) uncertainty. On CIFAR-100 there should be essentially no uncertainty about training labels, yet softmax-likelihood Bayesian classifiers are very uncertain there. [Izm+21b]: the cold-posterior effect in all the examples of [Wen+20b] (the printed sentence lacks a verb; read as 'disappears') when data augmentation is removed. [Kap+22]: with the SGLD of [Wen+20b], augmentation acts like raising the likelihood to the power $1/K$ for minibatch size $K$, and cold posteriors counteract this. Tempering is not required: with a Dirichlet observation model for label noise there is no cold-posterior effect, even with augmentation. The curation hypotheses [Ait21] are a special case. Tempering is particularly useful when the model is misspecified [KJD21] (p. 665).

### 17.4 Generalization in Bayesian deep learning

**17.4.1 Sharp vs flat minima (pp. 665–666).**
- Some optimizers find sharp minima (narrow, deep holes; Fig. 17.10 right), which generally correspond to overfit models. Flat minima are more robust and generalize better. Reasons given: flat minima are regions of large posterior uncertainty, so samples there are less able to memorize irrelevant details [AS17]; sharp minima have longer description length (more bits of precision to locate) [Mac03].
- SGD often finds flat minima because its noise keeps it out of narrow regions, and in high dimensions flat regions occupy much greater volume. [SL18]: the probability that SGD enters a basin $\mathcal A$ is $p_{SGD}(\theta\in\mathcal A)\propto\int_{\mathcal A}e^{-\mathcal L(\theta)}d\theta$. This is proportional to the model evidence for that region and is parameterization-invariant. So SGD avoids low-evidence (sharp) regions however the model is parameterized, **contrary to the claims in [Din+17]** (p. 666).
- SGD can be viewed as approximately sampling the posterior; SWA finds a "centre of mass". If one must use one solution, a flat one better approximates the BMA of (17.1). A fuller BMA selects for flatness automatically, weighting regions by volume, without flatness definitions, reparameterization worries or unknown implicit regularization (p. 666).

**17.4.2 Mode connectivity (p. 666).** Two independently trained SGD solutions can be connected by a curve in a subspace along which training loss stays near zero [Gar+18c]. Yet different points give very different functions (Fig. 17.11). A BMA can combine them for much better performance than a single flat solution [Izm+19]. [Ben+21b] found large multidimensional simplexes of low-loss solutions that can be combined for improved performance.

**17.4.3 Effective dimensionality (pp. 667–668).**
- Parameters are often not well determined by the data; averaging over the posterior avoids using unwarranted degrees of freedom. Following [MBW20]:
$$N_{eff}(H,c)=\sum_{i=1}^k\frac{\lambda_i}{\lambda_i+c}\tag{17.36}$$
$\lambda_i$ = eigenvalues of the Hessian at a local mode, $c>0$ a regularization parameter. It counts well-determined parameters. A flat minimum has many poorly determined directions, hence low $N_{eff}$. Inference can then be done in a low-dimensional subspace [Izm+19]; the text says this implies networks can be significantly compressed (p. 667).
- Compression view: of two models with similar training loss, the one with lower $N_{eff}$ compresses the data better at the same fidelity. Figure 17.12 (CNNs on CIFAR-100): for models with low training loss, $N_{eff}$ closely tracks generalization. Parameter count alone is not a strong determinant, and models with more parameters can have lower $N_{eff}$. Wide but shallow models overfit; depth gives lower $N_{eff}$ and better compression (pp. 667–668).

**17.4.4 The hypothesis space of DNNs (pp. 668–669).**
- Zhang et al. [Zha+17]: CNNs fit CIFAR-10 with random labels to zero training error, yet generalize on noise-free test data. **Claim (reported):** this contradicts the classical understanding of generalization.
- **Author's resolution (Bayesian view):** CNNs are flexible (universal approximators), but their architecture encodes a prior over patterns. Random-label datasets can be represented but receive very low marginal likelihood since they strongly violate the prior. Datasets with labels consistent with input patterns get much higher marginal likelihood. The same happens for GPs [WI20] (p. 668).
- Distinguish a model's **support** (functions it can represent) from the distribution over it (**inductive bias**). We want large support plus a bias that puts mass on expected functions. Then the posterior converges to the true function after a small amount of data (Fig. 17.13: CNN posterior collapses quickly to the true model; linear model collapses quickly to a wrong solution; MLP collapses slowly) (pp. 668–669).

**17.4.5 PAC-Bayes (p. 669).** PAC-Bayes is described as a promising mechanism to derive non-vacuous generalization bounds for large stochastic networks. The train/generalization error difference is given by a term of the form
$$\sqrt{\frac{D_{KL}(Q\|P)+c}{2(N-1)}}\tag{17.37}$$
($c$ constant, $N$ training points, $P$ prior over parameters, $Q$ an arbitrary distribution chosen to optimize the bound). The author calls the chapter's perspective "complementary, and in some ways orthogonal": PAC-Bayes bounds concern the empirical risk of a single sample, not marginalization. They are not currently prescriptive (e.g. reducing parameters or compact priors does not typically improve generalization). Multimodal BMA, which matters for generalization, has "a minimal logarithmic effect" on the bounds. Bounds are loose, so one can improve them without improving generalization.

**17.4.6 OOD generalization for BNNs (pp. 670–671).**
- Bayesian methods are often assumed more robust under distribution shift, but there are subtleties (p. 670).
- **17.4.6.1 BMA with default priors.** Deep ensembles are significantly less overconfident under some covariate shifts [Ova+19]. But HMC, arguably the most accurate posterior approximation, often works poorly under shift [Izm+21b]. Fig. 17.14a: on pixelate corruption of CIFAR-10-C at highest intensity, the BMA underperforms MAP by 25 points (44% vs 69%).
  - [Izm+21a]: this is a foundational issue of BMA under covariate shift, caused by degeneracies in the training data plus a poor prior. Example: MNIST corner pixels are always black, so first-layer weights on them can take any value without changing outputs. MAP with a Gaussian prior drives them to zero, giving robustness to corruption there. The posterior for them equals the prior, so a BMA multiplies corruptions by random prior samples (Fig. 17.14b,c) (p. 670).
  - [Izm+21a] prove this is a special case: whenever there are linear dependencies in the training inputs (data on a hyperplane), a shift orthogonal to the hyperplane leaves the posterior equal to the prior in that direction, so the BMA is vulnerable while MAP is entirely robust. Fix: the **EmpCov prior** $p(w^1)=\mathcal N(0,\alpha\Sigma+\epsilon I)$, with $\Sigma=\frac1{n-1}\sum_ix_ix_i^T$ the empirical input covariance, $\alpha>0$ the scale and $\epsilon$ small to keep it positive definite. It is aligned with the principal components of the training inputs and makes the BNN much more robust (p. 671).
- **17.4.6.2 Overconfidence on OOD inputs.** MCMC can sometimes give appropriate uncertainty (e.g. SGLD MLP on MNIST vs fashion-MNIST), but not reliably. On a 2-d two-moons problem (Fig. 17.15) with an OOD blob, we would expect probability 0.5 there. Only the GP classifier and SNGP do so (SGD, deep ensemble, MC dropout, bootstrap, MCMC and VI do not). **Lesson:** "being Bayesian" helps only with a good hypothesis class. A standard-Gaussian-prior MLP is extremely unlikely to learn the compact boundary of Fig. 17.15g, which has negligible prior support. So use as complex a model class as affordable (p. 671).

**17.4.7 Model selection (p. 671).** The marginal likelihood has historically been used to choose architectures or hyperparameters [Mac92a]. Laplace-based methods [Imm+21; Dax+21] make it scalable. [Lot+22] argue it is much better to use the conditional marginal likelihood (Sec. 3.8.5).

> **Intuition note (17.4).** Bayesian averaging helps when the model class makes real-world patterns probable and random patterns improbable, and when it spreads weight over many good solutions. It does not help automatically: with default priors the BMA was worse than MAP under covariate shift (p. 670), and the text's lesson is that being Bayesian helps only with a good hypothesis class (p. 671).

### 17.5 Online inference (pp. 672–677)
Sequential Bayesian inference (data arrive in a stream) is one approach to online learning, widely used for continual learning (p. 672).

**17.5.1 Sequential Laplace (pp. 672–673).** [RBB18b]: let $p(\theta|\mathcal D_{1:t-1})\approx\mathcal N(\mu_{t-1},\Lambda_{t-1}^{-1})$, with Kronecker-factored precision. New mean by MAP:
$$\mu_t=\arg\max\ \log p(\mathcal D_t|\theta)+\log p(\theta|\mathcal D_{1:t-1})\tag{17.38}$$
$$=\arg\max\ \log p(\mathcal D_t|\theta)-\tfrac12(\theta-\mu_{t-1})\Lambda_{t-1}^{-1}(\theta-\mu_{t-1})\tag{17.39}$$
(as printed; see Reading notes). New precision: $\Lambda_t=\lambda H(\mu_t)+\Lambda_{t-1}$ (17.40), with $\lambda\ge0$ trading off new against old data. With a diagonal approximation this adds a quadratic penalty keeping the estimate near the old parameters: **elastic weight consolidation (EWC)** [Kir+17].

**17.5.2 Extended Kalman filtering (pp. 673–675).**
- Kalman filtering gives the exact posterior for linear regression with known variance, $p(y_t|u_t,\theta,\sigma^2)=\mathcal N(y_t|\theta^Tu_t,\sigma^2)$ (17.41), known as recursive least squares. For nonlinear regression $p(y_t|u_t,\theta,\sigma^2)=\mathcal N(y_t|f(\theta,u_t),\sigma^2)$ (17.42), use the extended Kalman filter (EKF) with the parameters as hidden state $\theta_t$: dynamics $f(\theta_t)=\theta_t$ (identity), observation $f(\theta_t,u_t)$, $R_t=\sigma^2$, $Q_t=qI$ with small $q$ (artificial process noise letting parameters drift; it can help to anneal $q$ from large to near 0) (p. 673).
- **Example (17.5.2.1):** data from $h^*(u)=x-10\cos(u)\sin(u)+u^3$ (as printed) plus Gaussian noise with $\sigma=3$. Model $f(\theta,u)=W_2\tanh(W_1u+b_1)+b_2$ (17.44), $W_1\in\mathbb R^{H\times1}$, $b_1\in\mathbb R^H$, $W_2\in\mathbb R^{1\times H}$, $b_2\in\mathbb R^1$, $H=6$, so $D=19$ parameters. Prior $\mathcal N(0,\Sigma_0)$, $\Sigma_0=100I$; linearizing at the prior mean 0 gives zero gradient, so an initial random sample is used. Figure 17.16 (after 10, 20, 30, 200 observations): the model adapts without a specified learning rate, and predictions become more confident as the posterior concentrates on the MLE (p. 674).
- **17.5.2.2:** in general $\sigma$ (which sets $R_t$ and hence the learning rate) and the prior strength $\Sigma_0$ (regularization) must be estimated; see [FNG00].
- **17.5.2.3:** the naive EKF costs $O(N_z^3)$. **Decoupled EKF** partitions weights into $G$ groups: $G=1$ is global EKF; one weight per group is fully diagonal and in practice no better than SGD since it ignores correlations; one group per neuron is **node decoupled EKF**. Another approach exploits low effective dimensionality: represent the weights as a point in a linear manifold (random basis, or PCA of SGD iterates) and run the EKF in that subspace (p. 675).

**17.5.3 Assumed density filtering (pp. 675–676).**
- ADF generalizes to DNNs by Gaussian moment matching of hidden activations at each layer, an alternative to the EKF's linearization. Likelihood: $p(y_t|u_t,w_t)=\mathrm{Expfam}(y_t|\ell^{-1}(f(u_t;w_t)))$ (17.45); e.g. binary classification $\mathrm{Ber}(y_t|\sigma(u_t^Tw_t))$ (17.46).
- **PBP** [HLA15b]: fully factorized posterior
$$p(w_t|\mathcal D_{1:t})\approx p_t(w_t)=\prod_{l=1}^L\prod_{i=1}^{D_l}\prod_{j=1}^{D_{l-1}+1}\mathcal N(w_{ijl}|\mu^t_{ijl},\tau^t_{ijl})\tag{17.47}$$
Expectation backpropagation [SHM14] is the special case with fixed variances $\tau=1$ (p. 675).
- For static parameters, the posterior after observation $t$ is $\hat p_t(w)=\frac1{Z_t}p(y_t|u_t,w)\mathcal N(w|\mu^{t-1},\Sigma^{t-1})$, $\Sigma^{t-1}=\mathrm{diag}(\tau^{t-1})$ (17.48). Project onto factored Gaussians [Min01a]:
$$\mu^t_{ijl}=\mu^{t-1}_{ijl}+\tau^{t-1}_{ijl}\frac{\partial\ln Z_t}{\partial\mu^{t-1}_{ijl}}\tag{17.49}$$
$$\tau^t_{ijl}=\tau^{t-1}_{ijl}-(\tau^{t-1}_{ijl})^2\left[\left(\frac{\partial\ln Z_t}{\partial\mu^{t-1}_{ijl}}\right)^2-2\frac{\partial\ln Z_t}{\partial\tau^{t-1}_{ijl}}\right]\tag{17.50}$$
- Forward pass: propagating $u_t$ through a model with Gaussian weights gives (approximately) Gaussian hidden units. For some activations (e.g. ReLU) the integrals are analytic, as in GP-neural networks. The final pre-link output is $\mathcal N(\eta_t|\mu,\Sigma)$, so $Z_t\approx\int p(y_t|\eta_t)\mathcal N(\eta_t|\mu,\Sigma)d\eta_t$ (17.51). Probit ($y\in\{-1,+1\}$, $p=\Phi(y\eta)$): $\int\Phi(y\eta)\mathcal N(h|\mu,\sigma)d\eta=\Phi\!\left(\frac{y\mu}{\sqrt{1+\sigma}}\right)$ (17.52, as printed). Logistic: use the probit approximation (Sec. 15.3.6). Multiclass softmax: a variational lower bound on $\log Z_t$ is in [GDFY16]. Then take gradients and update the moments (p. 676).

**17.5.4 Online variational inference (pp. 676–677).**
- Streaming variational Bayes [Bro+13]: the prior is the previous posterior. At step $t$:
$$\psi_t=\arg\min_\psi\ \mathbb E_{q(\theta|\psi)}[\ell_t(\theta)]+D_{KL}(q(\theta|\psi)\|q(\theta|\psi_{t-1}))\tag{17.53}$$
$$=\arg\min_\psi\ \mathbb E_{q(\theta|\psi)}[\ell_t(\theta)+\log q(\theta|\psi)-\log q(\theta|\psi_{t-1})]\tag{17.54}$$
with $\ell_t(\theta)=-\log p(\mathcal D_t|\theta)$. For DNNs this is **variational continual learning (VCL)** [Ngu+18]; FOO-VB is an efficient implementation [Zen+21] (p. 677).
- **Variational overpruning** [TT17]: the KL term can make the model too sparse. Unneeded weights get posterior equal to prior, and sampling these high-variance weights adds noise. The optimizer then sets the bias to a large negative value, turning the unit off ("dead units"), which stay stuck and leave too little capacity for new tasks (p. 677).
- **GVCL** [LST21], two steps. (1) Downweight the KL by $\beta<1$:
$$\mathcal L_t=\mathbb E_{q(\theta|\psi)}[\ell_t(\theta)]+\beta D_{KL}(q(\theta|\psi)\|q(\theta|\psi_{t-1}))\tag{17.55}$$
As $\beta\to0$ it recovers Hessian-based Laplace methods: diagonal posterior gives online EWC [Sch+18]; block-diagonal Kronecker-factored gives online structured Laplace [RBB18b]; low-rank precision gives SOLA [Yin+20]. (2) Temper prior and posterior (useful under misspecification): for Gaussians, raising to power $\lambda$ equals temperature $\tau=1/\lambda$, i.e. scaling the covariance by $\lambda^{-1}$ (as stated):
$$\mathcal L_t=\mathbb E_{q(\theta|\psi)}[\ell_t(\theta)]+\beta D_{KL}(q(\theta|\psi)^\lambda\|q(\theta|\psi_{t-1})^\lambda)\tag{17.56}$$
Optimized with SGD if the posterior is reparameterizable.

### 17.6 Hierarchical Bayesian neural networks (pp. 677–680)
- Setting: related datasets (e.g. medical images from different hospitals). Some aspects are shared (cell shapes), others idiosyncratic (staining dye). Use a hierarchical model: per-dataset parameters (random effects) drawn from a common prior (shared effects), extending the hierarchical GLMs of Sec. 15.5. Similar to domain generalization, except that here performance matters on all domains (pp. 677–678).
- **17.6.1 Multimoons example:** $J=18$ related binary classification tasks, each with its own decision boundary $p(y|x,w^j)$ (concept shift) but similar to a shared boundary $p(y|x,w^0)$. Each has $N_j=50$ training points (and 50 test points). Data: two-moons rotated by a different amount per task (Fig. 17.17). Model: MLP with 2 hidden layers of 5 neurons (p. 678).
- Separate MLPs per task work poorly (little data each); one pooled model does even worse (different "concepts" are mixed). Hierarchical model (Fig. 17.18): weight from unit $i$ to $k$ in layer $l$ for environment $j$ is a shared value plus a random offset, non-centered (Sec. 12.6.5):
$$w^j_{i,k,l}=w^0_{i,k,l}+\epsilon^j_{i,k,l}\times\sigma^0_l,\qquad\epsilon^j_{i,k,l}\sim\mathcal N(0,1)\tag{17.57}$$
A separate $\sigma^0_l$ per layer lets the model control shrinkage to the prior per layer. (Environment-specific $\sigma^j_l$ is possible, allowing different amounts of shift from the parent.) Hyperpriors: $\mathcal N(0,1)$ on $w^0_{i,k,l}$, $\mathcal N_+(1)$ on $\sigma^0_l$ (p. 679).
- Posterior by HMC. Average accuracy (train/test): non-hierarchical 86%/83%; hierarchical 91%/89% (p. 679). Figure 17.19: separate MLPs fail to learn the common Z-shaped boundary; the hierarchical model recovers it while still allowing group variation (p. 680).

> **Intuition note.** Each task alone has too little data to find the shared boundary shape. Tying task weights to a common parent lets tasks lend each other strength, and the per-layer $\sigma^0_l$ says how far each layer may deviate.

## Toy example (ours, not from the text)
**BMA versus a single MAP model.** Suppose three ensemble members (Eq. 17.18 style, equal weights $1/3$) give $p(y=1|x)$ as follows.
- Training-like input $x_a$: 0.95, 0.90, 0.97. Average $=(0.95+0.90+0.97)/3=2.82/3=0.94$. The members agree, so the average is confident and close to each member.
- OOD input $x_b$: members extrapolate differently, giving 0.90, 0.50, 0.10. Average $=(0.90+0.50+0.10)/3=1.50/3=0.50$. A single MAP model (member 1) says 0.90 while the average says 0.50 ("don't know"). This is the sense in which averaging over distinct modes can represent uncertainty that one mode hides.

**Effective dimensionality (Eq. 17.36).** Take Hessian eigenvalues $\lambda=(10,1,0.1)$ and $c=1$. Then $N_{eff}=\frac{10}{11}+\frac{1}{2}+\frac{0.1}{1.1}=0.90909+0.5+0.09091=1.5$. The network has 3 parameters, but only about 1.5 are "well determined"; the direction with $\lambda=0.1$ barely counts.

## Concepts
- [[bayesian-model-averaging]] (new) — predict by averaging $p(y|x,\theta)$ over the posterior, Eq. (17.1) (p. 647)
- [[posterior-predictive-distribution]] — $\int p(y|x,\theta)p(\theta|\mathcal D)d\theta$, approximated by MC averaging (17.25) (pp. 647, 661)
- [[underspecification]] (new) — many parameter settings fit the data well yet generalize differently (p. 647)
- [[prior-distribution]] — here a prior over weights that induces a prior over functions; the architecture can matter even more (pp. 648–651)
- [[marginal-likelihood]] — evidence $p(\mathcal D|\alpha,\beta)$; used to learn priors, choose models and explain why random labels are unlikely under a CNN (pp. 650, 668, 671)
- [[laplace-approximation]] (new) — Gaussian at the MAP with GGN curvature, Eq. (17.16) (pp. 652–653)
- [[variational-inference-elbo]] — fixed-form Gaussian $q$ minimizing $D_{KL}(q\|p)$; Bayes by backprop (p. 653)
- [[kl-divergence]] — VI minimizes $D_{KL}(q\|p)$, EP $D_{KL}(p\|q)$; also used in distillation and PAC-Bayes (pp. 653–654, 664, 669)
- [[hamiltonian-monte-carlo]] — HMC, "generally considered the gold standard" for BNN posteriors; needs the full data at each step (p. 655)
- [[mc-dropout]] (new) — dropout kept on at test time, equally weighted average (17.13); argued (by [Osb16; LF+21]) not to give proper uncertainty (pp. 651–652)
- [[swa-swag]] (new) — SWA averages SGD iterates; SWAG adds a low-rank plus diagonal Gaussian (pp. 656–657)
- [[deep-ensembles]] (new) — equal mixture of deltas at independently trained modes (17.18); MultiSWAG gives a mixture of Gaussians (pp. 657–658)
- [[tempered-posterior]] (new) — likelihood raised to $\alpha$; for a Gaussian prior the cold posterior equals a tempered posterior with a rescaled prior variance, both reweighting the likelihood by $\alpha=1/T$ (pp. 664–665)
- [[flat-minima]] (new) — wide low-loss regions; large posterior volume, shorter description length (pp. 665–666)
- [[mode-connectivity]] (new) — near-zero-loss curves linking different SGD solutions that give different functions (p. 666)
- [[effective-dimensionality]] (new) — $\sum\lambda_i/(\lambda_i+c)$: count of well-determined parameters (p. 667)
- [[pac-bayes]] (new) — bound with $\sqrt{(D_{KL}(Q\|P)+c)/(2(N-1))}$; judged complementary and not prescriptive here (p. 669)
- [[laplace-bridge]] (new) — convert a Gaussian over logits to Dirichlet parameters (17.29) (p. 662)
- [[sequential-updating]] — online BNN inference where the previous posterior becomes the prior (EWC, EKF, ADF, VCL) (pp. 672–677)
- [[variational-continual-learning]] (new) — streaming VB for DNNs; GVCL downweights KL by $\beta$ and tempers (pp. 676–677)
- [[hierarchical-model]] — task weights = shared parent + per-layer-scaled offset, Eq. (17.57) (p. 679)
- [[partial-pooling]] — per-layer $\sigma^0_l$ controls shrinkage towards the shared weights (p. 679)

## Canonical instances
- [[mlp-prior-functions-figure]] — sampled 1-d functions from a sigmoid MLP under different $\alpha,\beta$ (p. 649)
- [[two-moons-hmc]] — HMC-fitted MLP, uncertainty grows off-data (p. 656)
- [[random-prior-ensemble]] — effect of $\beta$ on ensemble diffuseness (p. 659)
- [[rademacher-free-random-label-cifar]] — Zhang et al.: CNN fits random CIFAR-10 labels yet generalizes; resolved via marginal likelihood (p. 668). *(Not an established id; proposal.)*
- [[mnist-corner-pixel-bma-failure]] — BMA vs MAP under covariate shift (p. 670)
- [[ekf-mlp-regression]] — sequential EKF fit, $H=6$, $D=19$ (pp. 673–674)
- [[multimoons-hierarchical-bnn]] — 18 rotated two-moons tasks; accuracy 86/83 vs 91/89 (pp. 678–680)

## Bridges (candidates)
- [same-math] Tempered posterior ($\alpha=1/T$ likelihood power) ↔ power/generalized posteriors under misspecification: the same reweighting of the likelihood.
- [same-math] EKF on a linear model = recursive least squares ↔ Kalman filtering: the text itself says the KF applied to linear regression is recursive least squares (p. 673).
- [same-math] Hierarchical BNN with non-centered weights (17.57) ↔ hierarchical GLMs / partial pooling: the same parent-plus-offset structure with scale $\sigma^0_l$.
- [structural-analogy] SGD with fixed learning rate as approximate posterior sampler ↔ MCMC (SGLD): both generate approximate posterior samples, differing in explicit noise and learning-rate schedule.
- [structural-analogy] $N_{eff}=\sum\lambda_i/(\lambda_i+c)$ ↔ effective degrees of freedom in regularized regression: each eigendirection counts less when it is weakly determined.
- [structural-analogy] Random labels getting low marginal likelihood ↔ Bayesian Occam's razor: a model spreading mass over many datasets gives each less.
- [metaphor] Flat minima as "large volume" regions ↔ entropy in statistical mechanics: volume weighting favours wide basins.

## Questions this raises
- When the posterior is strongly multimodal, how many modes does a deep ensemble need to approximate the BMA, and how would one check this?
- If a cold posterior is explained by misspecified label noise, what other model misspecifications could make tempering look necessary?
- Can a prior be designed (like EmpCov) so that BMA is robust to covariate shifts along directions the training data never varied?
- How should the weight $\beta$ on the KL term in GVCL be chosen when tasks arrive without boundaries?

## Reading notes
- Printed page = pdf − 34 (pdf 681 = p. 647); the printed numbers are visible on the page labels and images. Footer: "Probabilistic Machine Learning: Advanced Topics". Online version. December 10, 2025.
- Likely misprints in the source (checked against images):
  - Eq. (17.12) has $\log$ inside the integral; the evidence would be $\log\int p(\mathcal D|\theta)p(\theta|\alpha,\beta)d\theta$.
  - Eq. (17.15) ends with $J_\theta(\theta)$ (printed); (17.16) uses $J(x_n)$.
  - Sec. 17.3.2 and 17.5.1 say "posterior prediction matrix", presumably "precision".
  - Sec. 17.3.2 defines $J\in\mathbb R^{C\times P}$, but Sec. 17.3.10.1 calls $J$ a "$P\times C$" matrix.
  - Eq. (17.30) has $\mathbf 1^TV_*\mathbf1$ in one denominator.
  - The definition of $c$ after (17.30) is cramped in the text layer; in the image it reads $c=(\sum_{ii}V'_{ii})/\sqrt{C/2}$.
  - Eq. (17.39) uses $\Lambda_{t-1}^{-1}$ although $\Lambda$ was defined as the precision.
  - Eq. (17.43) mixes $x$ and $u$.
  - Eq. (17.52) uses $h,\sigma$ for $\eta$ and the variance.
  - In (17.53), the underbrace is labelled $-\mathcal L_t(\psi)$, while (17.55) uses $\mathcal L_t$ as a loss to minimize.
  - Fig. 17.8 labels factors $r_ms_m^T$ while the text writes $F_m=s_mr_m^T$.
  - Fig. 17.15's caption calls the OOD blob green; the plotted blob looks cyan.
  - The sentence after (17.11) is legible; it also states $\varphi(\alpha z)=0$ for any negative $\alpha$ (since the preactivation $z\ge0$); I reported only the positive-homogeneity use.
  - The Sec. 17.3.4 statement that ADF "is equivalent to the first pass of ADF" is a slip; I read it as the first pass of EP.
- Not digested: the referenced Supplementary Section 17.1 (decoupled EKF details), and all other chapters cited. Figures were used only for what the captions and visible plots state.
- No exercises in this unit.

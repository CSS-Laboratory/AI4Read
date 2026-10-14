---
id: murphy-2023-pml2/ch14-predictive
work: murphy-2023-pml2
unit: "14 Predictive models: an overview"
pages: 575–589
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
# Predictive models: an overview

## L0 — One line
Predictive models (fitted by ERM, MAP or Bayesian-style objectives) can be judged by proper scoring rules, calibration and joint predictions, and conformal prediction can wrap any of them in sets with a distribution-free coverage guarantee.

## L1 — The gist (≤ 120 words)
The chapter asks how to fit and how to evaluate models of $p(y|x)$. Fitting methods (MLE, ERM, MAP, Gibbs posterior, Bayes, variational inference, generalized Bayes) are presented as steps from plain risk minimization to risk plus a penalty that keeps the fit near a prior. Evaluation uses proper scoring rules and calibration. Marginal calibration can miss differences in joint predictions, so joint predictive distributions over $\tau$ outcomes can be compared by KL divergence or NLL (negative log likelihood). Finally, conformal prediction turns any predictor into prediction sets or intervals with finite-sample frequentist coverage, assuming only exchangeability. This matters because it gives checkable ways to trust predictions and their uncertainty.

**Prerequisites:** likelihood, KL divergence, expectation, softmax/logits, quantiles, exchangeability, basic Bayesian posterior.

## L2 — Key ideas
- MLE and ERM (empirical risk minimization) minimize a loss on the data. Adding a prior-based penalty gives MAP (maximum a posteriori). Putting a distribution $q$ on the parameters and adding a KL penalty to the prior gives the Gibbs posterior, the Bayes posterior (log loss, $\lambda=N$), VI (variational inference, with a restricted family) and generalized Bayes (pp. 576–577).
- A proper scoring rule is maximized in expectation only by the true conditional distribution. Log-likelihood and the Brier score are both proper (p. 578).
- Calibration means predicted probabilities match empirical frequencies. It is measured by the expected or marginal calibration error (ECE, MCE) and can be improved by Platt scaling, binning or temperature scaling (which rescale or bin the outputs), and often by label smoothing or Bayesian fitting (pp. 578–582).
- Platt and temperature scaling leave the top class unchanged, so accuracy is unaffected (p. 581).
- Equal marginal predictions can hide very different joint predictions, as in a two-coin example contrasting aleatoric (irreducible noise) and epistemic (parameter) uncertainty. So one evaluates joint predictive distributions (p. 582).
- Ranking agents by the intractable Bayes-optimal KL, by KL to the true environment, or by cross entropy (NLL) gives the same order, because the terms differ by constants (pp. 583–585).
- Conformal prediction: take the $\lceil (n+1)(1-\alpha)\rceil/n$ quantile $\hat q$ of calibration scores. The set $\{y: s(x,y)\le\hat q\}$ then covers the new label with probability at least $1-\alpha$ if the data are exchangeable (p. 586).
- The guarantee is frequentist and average-case, not per-instance. The aim is sets as small as possible, which needs a good score: the chapter gives softmax, adaptive-set, quantile-regression (CQR), scaled-residual and Bayes-posterior-density scores (pp. 586–588).

## L3 — Walkthrough

### 14.1 Introduction (p. 575)
The task is to predict $y$ from $x$ using $f$ estimated from $\mathcal D=\{(x_n,y_n)\}_{n=1}^N$. Uncertainty is modelled by $p(y|f(x))$. For discrete $\mathcal Y$ this is called a discriminative model (ML usage). For $\mathcal Y=\mathbb R$ it is a regression model. Statistics uses "regression" for both. The author uses "predictive model" for all of them (p. 575). A predictive model can be considered a special case of a conditional generative model. Its output is usually low-dimensional with one best answer, whereas generative outputs are high-dimensional with many correct answers (p. 575).

### 14.1.1 Types of model (pp. 575–576)
- **Parametric** models have a fixed number of parameters. They are usually less flexible but faster at prediction.
- **Non-parametric** models have parameters that grow with the training set. They are usually more flexible but can be slower at prediction.
- Non-parametric models typically compute similarities $s_n=\mathcal K(x,x_n)\ge 0$ and predict a weighted combination such as $\hat y=\sum_n s_n y_n$. A Gaussian process is an example (p. 575).
- Parametric models have the form $p(y|f(x;\theta))$, where $f$ predicts the parameters (mean or logits) of the output distribution.
  - If $f(x;\theta)=\theta^\top\phi(x)$ with fixed $\phi$, it is a generalized linear model (GLM).
  - If $f$ is non-linear but differentiable in $\theta$, e.g. $\theta_2^\top\phi(x;\theta_1)$, it is usually a neural network (p. 576).

### 14.1.2 Fitting with ERM, MLE, MAP (p. 576)
MLE:
$$\hat\theta=\arg\max_{\theta\in\Theta}p(\mathcal D|\theta)=\arg\max_\theta\log p(\mathcal D|\theta)\tag{14.1}$$
For $N$ iid samples, $p(\mathcal D|\theta)=\prod_n p(y_n|x_n,\theta)$. So one can minimize the scaled negative log likelihood:
$$\hat\theta=\arg\min_\theta\frac1N\sum_{n=1}^N[-\log p(y_n|x_n,\theta)]\tag{14.2}$$
Replace the log loss $\ell_n(\theta)=-\log p(y_n|x_n,\theta)$ by a general loss:
$$\hat\theta=\arg\min_\theta r(\theta),\qquad r(\theta)=\frac1N\sum_{n=1}^N\ell_n(\theta)\tag{14.3, 14.4}$$
$r$ is the empirical risk. This is empirical risk minimization (ERM). ERM can easily overfit, so it is common to add a regularizer ($\lambda\ge0$, $C$ a complexity measure):
$$\hat\theta=\arg\min_\theta r(\theta)+\lambda C(\theta)\tag{14.5}$$
With log loss, $C(\theta)=-\log\pi_0(\theta)$ for a prior $\pi_0$, and $\lambda=1$, one recovers the MAP estimate:
$$\hat\theta=\arg\max_\theta\log p(\mathcal D|\theta)+\log\pi_0(\theta)\tag{14.6}$$
It can be solved by standard optimization (p. 576).

### 14.1.3 Fitting with Bayes, VI, generalized Bayes (p. 577)
Instead of a point estimate, estimate a distribution $q(\theta)$ and minimize expected risk:
$$\hat q=\arg\min_{q\in\mathcal P(\Theta)}\mathbb E_{q}[r(\theta)]\tag{14.7}$$
If $\mathcal P(\Theta)$ is all distributions, the solution converges to a delta function on the MLE. So this alone does not prevent overfitting. Regularize with a KL penalty to the prior:
$$\hat q=\arg\min_q\mathbb E_q[r(\theta)]+\tfrac1\lambda D_{\mathrm{KL}}(q\,\|\,\pi_0)\tag{14.8}$$
The solution is the **Gibbs posterior**, widely used in PAC-Bayes:
$$\hat q(\theta)=\frac{e^{-\lambda r(\theta)}\pi_0(\theta)}{\int e^{-\lambda r(\theta')}\pi_0(\theta')d\theta'}\tag{14.9}$$
With log loss and $\lambda=N$ this becomes
$$\hat q(\theta)=\frac{e^{\sum_n\log p(y_n|x_n,\theta)}\pi_0(\theta)}{\int e^{\sum_n\log p(y_n|x_n,\theta')}\pi_0(\theta')d\theta'}\tag{14.10}$$
This equals the Bayes posterior:
$$\hat q(\theta)=\frac{p(\mathcal D|\theta)\pi_0(\theta)}{\int p(\mathcal D|\theta')\pi_0(\theta')d\theta'}\tag{14.11}$$
Restricting to a family $\mathcal Q(\Theta)\subset\mathcal P(\Theta)$ gives variational inference (VI):
$$\hat q=\arg\min_{q\in\mathcal Q}\mathbb E_q[-\log p(\mathcal D|\theta)]+D_{\mathrm{KL}}(q\|\pi_0)\tag{14.12}$$
Replacing the NLL by a general risk $r$, the KL by a general divergence $D$, and weighting by $\lambda$ gives generalized Bayesian inference:
$$\hat q=\arg\min_{q\in\mathcal Q}\mathbb E_q[r(\theta)]+\lambda D(q\|\pi_0)\tag{14.13}$$

*Intuition note:* Most of these fitting rules follow one pattern: "fit the data, but stay near a prior" (MLE and plain ERM have no such penalty). Different choices of loss, divergence and weight give MAP, the Bayes posterior, VI, or the Gibbs posterior used in PAC-Bayes.

### 14.2.1 Proper scoring rules (p. 578)
Let $S(p_\theta,(y,x))$ be the score of the predictive distribution when $y|x\sim p^*(y|x)$ ($p^*$ is the true conditional). For a Bayesian model, replace $p_\theta(y|x)$ with $p(y|x)=\int p_\theta(y|x)p(\theta|\mathcal D)d\theta$. Expected score:
$$S(p_\theta,p^*)=\int p^*(x)p^*(y|x)S(p_\theta,(y,x))\,dy\,dx\tag{14.14}$$
A rule is **proper** if $S(p_\theta,p^*)\le S(p^*,p^*)$, with equality iff $p_\theta(y|x)=p^*(y|x)$. So maximizing it forces the model to match the true probabilities.

The log-likelihood is proper by Gibbs inequality:
$$S(p_\theta,p^*)=\mathbb E_{p^*(x)p^*(y|x)}[\log p_\theta(y|x)]\le\mathbb E_{p^*(x)p^*(y|x)}[\log p^*(y|x)]\tag{14.15}$$
So minimizing NLL "should" give well-calibrated probabilities. In practice log loss can over-emphasize tail probabilities (p. 578). The **Brier score** is
$$S(p_\theta,(y,x))\triangleq\frac{-1}{C}\sum_{c=1}^C(p_\theta(y=c|x)-\mathbb I(y=c))^2\tag{14.16}$$
It is proportional to the squared error against the one-hot label. The minus sign makes larger better. The author says it is less sensitive to extremely rare or common classes, and that it is also proper (p. 578).

### 14.2.2 Calibration (pp. 578–582)
A model is **calibrated** if predicted probabilities match empirical frequencies. For example, predictions of $0.9$ should be right about 90% of the time (p. 578).

**14.2.2.1 ECE (p. 579).** Use $B$ bins $I_b=(\frac{b-1}B,\frac bB]$. $\mathcal B_b$ is the set of samples whose confidence falls in $I_b$. With $\hat y_n=\arg\max_c f(x_n)_c$ and $\hat p_n=\max_c f(x_n)_c$:
$$\mathrm{acc}(\mathcal B_b)=\frac1{|\mathcal B_b|}\sum_{n\in\mathcal B_b}\mathbb I(\hat y_n=y_n)\tag{14.17}$$
$$\mathrm{conf}(\mathcal B_b)=\frac1{|\mathcal B_b|}\sum_{n\in\mathcal B_b}\hat p_n\tag{14.18}$$
$$\mathrm{ECE}(f)=\sum_{b=1}^B\frac{|\mathcal B_b|}{B}\,|\mathrm{acc}(\mathcal B_b)-\mathrm{conf}(\mathcal B_b)|\tag{14.19}$$
Plotting accuracy against confidence gives a reliability diagram, whose gap is the red bars (Fig. 14.1). In the multiclass case ECE only looks at the top-label prediction. The marginal calibration error (MCE) covers all classes, with $w_c\in[0,1]$ the class importance ($w_c=1/C$ if all matter equally):
$$\mathrm{MCE}=\sum_{c=1}^Cw_c\,\mathbb E\big[(p(Y=c|f(x)_c)-f(x)_c)^2\big]\tag{14.20}$$
$$=\sum_{c}w_c\sum_{b=1}^B\frac{|\mathcal B_{b,c}|}{B}(\mathrm{acc}(\mathcal B_{b,c})-\mathrm{conf}(\mathcal B_{b,c}))^2\tag{14.21}$$
[Nix+19] call this static calibration error. They show that certain methods with good ECE may have poor MCE (p. 580).

**14.2.2.2 Improving calibration (p. 580).** Training with a proper rule such as NLL should in principle give a calibrated classifier. In practice, unbalanced datasets can give poor calibration.

**14.2.2.3 Platt scaling (p. 580).** For binary logit $z$ with $p=\sigma(z)$: $q=\sigma(az+b)$, with $a,b$ fitted by maximum likelihood on a validation set. Multiclass matrix scaling: $q=\mathrm{softmax}(\mathbf Wz+b)$. $\mathbf W$ has $K\times K$ parameters and can overfit, so in practice it is restricted to be diagonal.

**14.2.2.4 Histogram methods (p. 580).** Platt scaling assumes a strong shape for the calibration curve. Histogram binning partitions predicted probabilities into bins $p_m$ and replaces each with the empirical probability $q_m$. Isotonic regression requires $q=f(p)$ to be piecewise constant and monotonically non-decreasing. The scaling-binning calibrator applies a scaling method first, then bins, using the average of the scaled probabilities in each bin instead of the average of observed labels (Fig. 14.2). [KLM19] prove this gives better calibration because of lower estimator variance. The multiclass extension applies the binary method to $K$ one-vs-rest problems. This needs $K$ calibration models and gives an unnormalized distribution.

**14.2.2.5 Temperature scaling (pp. 580–581).** [Guo+17] observed that diagonal Platt scaling on DNNs often learned $w=(c,\dots,c)$. This suggests
$$q=\mathrm{softmax}(z/T),\quad T>0,$$
with $T$ fitted by maximum likelihood on validation data. It makes the distribution less peaky (Fig. 14.3). [Guo+17] show empirically that it gives the lowest ECE on a variety of DNN problems and is simpler and faster. Platt and temperature scaling do not change the most probable label, so accuracy is unchanged (p. 581).

**14.2.2.6 Label smoothing (pp. 581–582).** Replace the one-hot target $(0,1,0)$ by e.g. $(0.1,0.8,0.1)$. This often gives better-calibrated models.

**14.2.2.7 Bayesian methods (p. 582).** Bayesian fitting often gives more calibrated predictions because it represents parameter uncertainty. But [Ova+19] show that well-calibrated models, even Bayesian ones, often become mis-calibrated on inputs from a different distribution.

### 14.2.3 Beyond marginal probabilities (pp. 582–584)
Calibration assesses the marginal $p(y|x)$. This can fail to distinguish good from bad models, especially in online learning and sequential decisions. **Example (coin tosses), $Y_t\sim\mathrm{Ber}(\theta)$:**
- Agent 1 believes $\theta=2/3$.
- Agent 2 believes $\theta\in\{0,1\}$ with probabilities $1/3$ and $2/3$.
- Both predict the next outcome identically: $p(Y_1^i=0)=1/3$.

For $\tau$ future outcomes they differ. Agent 1 sees pure aleatoric (irreducible-noise) uncertainty:
$$p(Y_1^1=0,\dots,Y_\tau^1=0)=\frac1{3^\tau}\tag{14.22}$$
Agent 2 has epistemic (parameter) uncertainty:
$$p(Y^2_1=y_1,\dots,Y^2_\tau=y_\tau)=\begin{cases}1/3&y_1=\dots=y_\tau=0\\2/3&y_1=\dots=y_\tau=1\\0&\text{otherwise}\end{cases}\tag{14.23}$$
In a casino, repeatedly betting on heads is low-risk for agent 1 but very unwise for agent 2, for whom initial exploration would be worthwhile (p. 582).

So one should evaluate joint predictive distributions [Lu+22; Osb+21]. Setup: outcomes $y=Y_{T+1:T+\tau}$, inputs $x=X_{T:T+\tau-1}$, past data $\mathcal D_T=\{(X_t,Y_{t+1}):t=0,\dots,T-1\}$. Bayes-optimal predictive and the agent's approximation (a "belief state"):
$$P^B_T=p(y|x,\mathcal D_T)\tag{14.24}$$
$$Q_T=q(y|x,\mathcal D_T)\tag{14.25}$$
The natural metric is the KL between them, averaged over $x,\mathcal D_T$ drawn iid from the data-generating distribution with true unknown environment $\mathcal E$:
$$P(X,Y,\mathcal E)=P(X|\mathcal E)P(Y|X,\mathcal E)P(\mathcal E)\tag{14.26}$$
$$d^{KL}_{B,Q}=\mathbb E_{P(x,\mathcal D_T)}\big[D_{\mathrm{KL}}(P^B(y|x,\mathcal D_T)\|Q(y|x,\mathcal D_T))\big]\tag{14.27}$$
$$P(x,\mathcal D_T,\mathcal E)=P(\mathcal E)\underbrace{\prod_{t=0}^{T-1}P(X_t|\mathcal E)P(Y_{t+1}|X_t,\mathcal E)}_{P(\mathcal D_T|\mathcal E)}\underbrace{\prod_{t=T}^{T+\tau-1}P(x_t|\mathcal E)}_{P(x|\mathcal E)}\tag{14.28}$$
$P(x,\mathcal D_T)$ marginalizes over environments. Since $P^B$ is usually intractable, $d^{KL}_{B,Q}$ cannot be computed. But (proved in 14.2.3.1):
$$d^{KL}_{B,Q}=d^{KL}_{\mathcal E,Q}-\mathbb I(\mathcal E;y|\mathcal D_T,x)\tag{14.29}$$
The second term is constant with respect to the agent, and
$$d^{KL}_{\mathcal E,Q}=\mathbb E_{P(x,\mathcal D_T,\mathcal E)}[D_{\mathrm{KL}}(P(y|x,\mathcal E)\|Q(y|x,\mathcal D_T))]=\mathbb E_{P(y|x,\mathcal E)P(x,\mathcal D_T,\mathcal E)}\Big[\log\frac{P(y|x,\mathcal E)}{Q(y|x,\mathcal D_T)}\Big]\tag{14.30, 14.31}$$
So ranking agents by $d^{KL}_{\mathcal E,Q}$ equals ranking by $d^{KL}_{B,Q}$ (p. 583).

*Monte Carlo estimate (p. 583).* Sample $J$ environments $\mathcal E^j\sim P(\mathcal E)$, a training set $\mathcal D^j_T\sim P(\mathcal D_T|\mathcal E^j)$ from each, and $N$ length-$\tau$ vectors $(x^j_n,y^j_n)$ from $P(\cdot|\mathcal E^j)$. Then
$$\hat d^{KL}_{\mathcal E,Q}=\frac1{JN}\sum_{j=1}^J\sum_{n=1}^N\big[\log P(y^j_n|x^j_n,\mathcal E^j)-\log Q(y^j_n|x^j_n,\mathcal D^j_T)\big]\tag{14.32}$$
$$p_{jn}=\prod_{t=T}^{T+\tau-1}P(Y^j_{n,t+1}|X^j_{n,t},\mathcal E^j)\tag{14.33}$$
$$q_{jn}=\int Q(y^j_n|x^j_n,\theta)Q(\theta|\mathcal D^j_T)d\theta\approx\frac1M\sum_{m=1}^M\prod_{t=T}^{T+\tau-1}Q(Y^j_{n,t+1}|X^j_{n,t},\theta^j_m)\tag{14.34, 14.35}$$
with $\theta^j_m\sim Q(\theta|\mathcal D^j_T)$ (p. 584). This needs $P(Y|X)$ known, e.g. a synthetic generator like the "neural testbed" of [Osb+21]. If only empirical distributions $P^j$ exist, use cross entropy:
$$d^{KL}_{\mathcal E,Q}=\underbrace{\mathbb E_{P(x,y,\mathcal E)}[\log P(y|x,\mathcal E)]}_{\text{const}}-\underbrace{\mathbb E_{P(x,y,\mathcal D_T|\mathcal E)P(\mathcal E)}[\log Q(y|x,\mathcal D_T)]}_{d^{CE}_{\mathcal E,Q}}\tag{14.36, 14.37}$$
The second term is the empirical NLL. So ranking by NLL (cross entropy) gives the same order as $d^{KL}_{\mathcal E,Q}$ and hence $d^{KL}_{B,Q}$. Estimator:
$$\hat d^{CE}_{\mathcal E,Q}=-\frac1{JN}\sum_{j=1}^J\sum_{n=1}^N\log Q(y^j_n|x^j_n,\mathcal D^j_T)\tag{14.38}$$
Alternatively evaluate joint predictions on a downstream task. For $\tau>1$, good predictive accuracy correlates with good bandit performance [Osb+21] and with good transductive active learning [WSG21] (p. 584).

*Intuition note:* Two models can agree on every single next-step probability yet disagree on how outcomes are correlated. Scoring whole sequences ($\tau>1$) reveals this. Because the unknown-environment KL differs from the Bayes-optimal KL only by a constant, simple NLL on joint outcomes ranks agents correctly.

### 14.2.3.1 Proof of Eq. (14.29) (pp. 584–585)
Write the log-ratio as a sum (added step: insert and cancel $\log P(y|x,\mathcal D_T)$):
$$d^{KL}_{\mathcal E,Q}=\mathbb E\Big[\log\frac{P(y|x,\mathcal E)}{Q(y|x,\mathcal D_T)}\Big]=\mathbb E\Big[\log\frac{P(y|x,\mathcal D_T)}{Q(y|x,\mathcal D_T)}\Big]+\mathbb E\Big[\log\frac{P(y|x,\mathcal E)}{P(y|x,\mathcal D_T)}\Big]\tag{14.39, 14.40}$$
First term:
$$\sum P(x,y,\mathcal D_T)\log\frac{P(y|x,\mathcal D_T)}{Q}=\sum P(x,\mathcal D_T)\sum P(y|x,\mathcal D_T)\log\frac{P(y|x,\mathcal D_T)}{Q}=\mathbb E_{P(x,\mathcal D_T)}[D_{\mathrm{KL}}(P\|Q)]=d^{KL}_{B,Q}\tag{14.41–14.43}$$
Second term: since $\mathcal D_T$ carries no new information beyond $\mathcal E$,
$$P(y|x,\mathcal E)=P(y|\mathcal D_T,x,\mathcal E)=\frac{P(\mathcal E,y|\mathcal D_T,x)}{P(\mathcal E|\mathcal D_T,x)}\tag{14.44}$$
$$\mathbb E\Big[\log\frac{P(y|x,\mathcal E)}{P(y|x,\mathcal D_T)}\Big]=\sum P(\mathcal D_T,x)\sum P(\mathcal E,y|\mathcal D_T,x)\log\frac{P(\mathcal E,y|\mathcal D_T,x)}{P(y|\mathcal D_T,x)P(\mathcal E|\mathcal D_T,x)}=\mathbb I(\mathcal E;y|\mathcal D_T,x)\tag{14.45–14.47}$$
Hence $d^{KL}_{\mathcal E,Q}=d^{KL}_{B,Q}+\mathbb I(\mathcal E;y|\mathcal D_T,x)$ (14.48), which is (14.29) rearranged.

### 14.3 Conformal prediction (pp. 585–586)
Conformal prediction builds prediction sets or intervals with guaranteed frequentist coverage from any predictor $p(y|x)$. It is distribution-free: apart from exchangeability, it makes no assumption about the data-generating process or the model (p. 585). Exchangeability rules out serially correlated time series and distribution shift, though extensions exist (fn. 1, p. 585).

Procedure:
1. Choose a heuristic uncertainty notion, e.g. softmax score or variance, and define a conformal (non-conformity) score $s(x,y)\in\mathbb R$. Large values mean $y$ conforms badly to $x$.
2. Apply it to a calibration set of $n$ labeled examples not used to train $f$, giving $\mathcal S=\{s_i\}_{i=1}^n$. This is split conformal prediction (fn. 3, p. 586).
3. Given $\alpha$ (e.g. 0.1), take the $(1-\alpha)$ quantile $\hat q$ of $\mathcal S$. For finite $n$, replace $1-\alpha$ by $\lceil(n+1)(1-\alpha)\rceil/n$.
4. For a new $x_{n+1}$:
$$\mathcal T(x_{n+1})=\{y:s(x_{n+1},y)\le\hat q\}\tag{14.49}$$
**Result** (any $n\ge1$, $\alpha\in[0,1]$; the only assumption is that the $(x_i,y_i)$ are exchangeable, so the scores are too):
$$1-\alpha\le P^*(y_{n+1}\in\mathcal T(x_{n+1}))\le1-\alpha+\frac1{n+1}\tag{14.50}$$
*Proof of the lower bound* (assuming distinct scores). Sort $s_1<\dots<s_n$, so $\hat q=s_i$ with $i=\lceil(n+1)(1-\alpha)\rceil$. By exchangeability $s_{n+1}$ is equally likely to fall anywhere among the calibration points, so
$$P^*(s_{n+1}\le s_k)=\frac k{n+1},\quad k\in\{1,\dots,n+1\}\tag{14.51}$$
The event $\{y_{n+1}\in\mathcal T\}$ equals $\{s_{n+1}\le\hat q\}$, so
$$P^*(y_{n+1}\in\mathcal T(x_{n+1}))=P^*(s_{n+1}\le\hat q)=\frac{\lceil(n+1)(1-\alpha)\rceil}{n+1}\ge1-\alpha\tag{14.52}$$
The upper bound is in [Lei+18].

*Caveats (p. 586).* This is not a free lunch: outputting all labels always achieves the coverage. So one wants sets as small as possible (allowed to be larger for harder inputs), and this needs good scores. The guarantee is frequentist, about average behavior, not per-instance uncertainty as in the Bayesian approach.

*Intuition note:* If the new point is exchangeable with the $n$ calibration points, its score has a uniformly random rank among all $n+1$. Choosing the threshold at the right rank therefore fixes the chance of being covered, whatever the model is.

### 14.3.1 Conformalizing classification (p. 587)
Simplest: $s(x,y)=1-f(x)_y$, giving $\mathcal T(x)=\{y:f(x)_y\ge1-\hat q\}$. This gives the smallest average set size (proved in [SLW19]). But sets tend to be too large for easy examples and too small for hard ones. **Adaptive prediction sets** [RSC20]: sort softmax scores into permutation $\pi_{1:C}$ and set $s(x,y)=\sum_{c=1}^kf(x)_{\pi_c}$ with $k=\pi_y$. The set contains labels in decreasing probability order until $\hat q$ of the mass is covered (Fig. 14.5a). It uses all scores, which accounts for its better performance.

### 14.3.2 Conformalizing regression (pp. 587–588)
For $y\in\mathbb R$ computing (14.49) is expensive, so one computes an interval.

**Quantile regression (CQR).** Fit $t_\gamma(x)$, the predicted $\gamma$-quantile. E.g. $[t_{0.05},t_{0.95}]$ is an approximate 90% interval. Fitting uses the pinball loss:
$$\ell_\gamma(y,\hat t)=(\gamma-\mathbb I(y<\hat t))(y-\hat t)=(y-\hat t)\gamma\mathbb I(y>\hat t)+(\hat t-y)(1-\gamma)\mathbb I(y<\hat t)\tag{14.53}$$
Its minimizer is the $\gamma$-quantile: $\arg\min_{\hat t}\mathbb E_{p_Y}[\ell_\gamma(y,\hat t)]=P_Y^{-1}(\gamma)$. The regression quantiles are usually only approximately a 90% interval because the model may be mismatched. Fix it with
$$s(x,y)=\max(\hat t_{\alpha/2}(x)-y,\;y-\hat t_{\alpha/2}(x))\tag{14.54}$$
As printed, (14.54) uses $\hat t_{\alpha/2}$ in both arguments. The text describes $s$ as how far $y$ lies outside the interval, which would need the upper quantile in the second argument (see Reading notes).
$$\mathcal T(x)=[\hat t_{\alpha/2}(x)-\hat q,\;\hat t_{\alpha/2}(x)+\hat q]\tag{14.55}$$
The interval widens if $\hat q>0$ (base method overconfident) and narrows if $\hat q<0$ (underconfident) (p. 588).

**Predicted variances.** With an uncertainty score $u(x)$ (e.g. predicted standard deviation):
$$\mathcal T(x)=[f(x)-u(x)\hat q,\;f(x)+u(x)\hat q],\qquad s(x,y)=\frac{|y-f(x)|}{u(x)}\tag{14.56, 14.57}$$
This tends to be wider than CQR since it is symmetric around $f(x)$, and $u(x)$ may not scale properly with $\alpha$. It is a simple post-hoc method needing no retraining.

### 14.3.3 Conformalizing Bayes (p. 588)
With posterior predictive $f(x)_y=p(y|x)$, a perfect model would make the optimal set
$$\mathcal S(x)=\{y:f(x)_y>t\},\quad\int_{y\in\mathcal S(x)}f(x)_ydy=1-\alpha\tag{14.58}$$
It lacks the coverage if modelling assumptions are wrong. Conformalize with $s(x,y)=-f(x)_y$ and $\mathcal T(x)=\{y:f(x)_y>-\hat q\}$. [Hof21] prove it has the smallest average size (Bayes risk) among conformal procedures with $1-\alpha$ coverage, so it is optimal in both the Bayesian and frequentist sense.

### 14.3.4–14.3.5 No calibration set; generalizations (p. 589)
Without enough data to split, use full conformal prediction (refit $n$ times, leave-one-out style), the Bayesian add-one-in importance sampling of [FH21], or jackknife+ [Bar+19]. Conformal prediction generalizes to richer output sets [Ang+24]. [Yad+24] use "conformal abstention" so an LLM declines to answer when not confident.

## Toy example (ours)
Split conformal classification, $n=9$, $\alpha=0.2$.
- Calibration scores $s_i=1-f(x_i)_{y_i}$, sorted: 0.05, 0.10, 0.12, 0.20, 0.25, 0.31, 0.40, 0.55, 0.90.
- Index: $\lceil(n+1)(1-\alpha)\rceil=\lceil10\times0.8\rceil=8$. The quantile level is $8/9$. So $\hat q=s_{(8)}=0.55$.
- Guarantee: coverage $=8/(n+1)=8/10=0.8\ge1-\alpha$ (14.52).
- New input with softmax $f=(0.60,0.25,0.10,0.05)$ gives scores $1-f=(0.40,0.75,0.90,0.95)$. Keep labels with score $\le0.55$, i.e. $f\ge0.45$. $\mathcal T=\{\text{class }1\}$.
- A harder input with $f=(0.40,0.35,0.15,0.10)$ gives scores $(0.60,0.65,0.85,0.90)$, all above 0.55, so $\mathcal T=\emptyset$. This shows the simple softmax score can give an empty set. It is not a problem of the guarantee.

## Concepts
- [[empirical-risk-minimization]] (new) — minimize average loss $r(\theta)$, optionally plus $\lambda C(\theta)$ (p. 576)
- [[maximum-a-posteriori]] (new) — ERM with log loss and $C=-\log\pi_0$; maximizes $\log p(\mathcal D|\theta)+\log\pi_0$ (p. 576)
- [[gibbs-posterior]] (new) — minimizer of expected risk plus $\frac1\lambda$KL to prior; $\propto e^{-\lambda r}\pi_0$ (p. 577)
- [[generalized-bayesian-inference]] (new) — replace NLL by risk, KL by general divergence, weight by $\lambda$ (p. 577)
- [[variational-inference-elbo]] — minimize NLL-expectation plus KL over a restricted family $\mathcal Q$ (p. 577)
- [[kl-divergence]] — regularizer to prior and evaluation metric between predictives (pp. 577, 583)
- [[proper-scoring-rule]] (new) — expected score maximized only by the true distribution (p. 578)
- [[calibration]] (new) — predicted probabilities match empirical frequencies; measured by ECE/MCE (pp. 578–580)
- [[temperature-scaling]] (new) — $q=\mathrm{softmax}(z/T)$, $T$ fitted on a validation set; keeps the argmax (pp. 580–581)
- [[aleatoric-vs-epistemic-uncertainty]] (new) — irreducible noise vs uncertainty about parameters (p. 582)
- [[posterior-predictive-distribution]] — $p(y|x)=\int p_\theta(y|x)p(\theta|\mathcal D)d\theta$; evaluated jointly over $\tau$ outcomes (pp. 578, 582)
- [[conformal-prediction]] (new) — sets from the calibration-score quantile with coverage $\ge1-\alpha$ (pp. 585–586)
- [[exchangeability]] — the only assumption behind the conformal guarantee (p. 586)
- [[pinball-loss]] (new) — quantile loss whose minimizer is the $\gamma$-quantile (p. 587)
- [[frequentist-vs-bayesian-inference]] — conformal coverage is frequentist, average-case, not per-instance (p. 586)

## Canonical instances
- [[two-coin-agents]] — equal marginal prediction, different joint prediction (aleatoric vs epistemic) (p. 582)
- [[reliability-diagram-cifar100]] — ECE falls after temperature scaling (12.67 → 0.96) (p. 579)
- [[imagenet-fox-squirrel-prediction-sets]] — set size grows with difficulty (p. 585)
- [[neural-testbed]] — synthetic generator for evaluating joint predictions (p. 584)

## Bridges (candidates)
- [structural-analogy] Gibbs posterior $\propto e^{-\lambda r}\pi_0$ ↔ Bayes' theorem: with log loss and $\lambda=N$ the two coincide — a special case, not general (p. 577)
- [same-math] Pinball loss minimizer ↔ quantile regression / median ($\gamma=0.5$) (p. 588)
- [structural-analogy] Epistemic-vs-aleatoric split in joint predictions ↔ exchangeability and de Finetti mixtures: agent 2 is a mixture of iid coins (p. 582)
- [structural-analogy] Conformal rank argument ↔ permutation tests (uniform rank of an exchangeable point)

## Questions this raises
- Why can well-calibrated models become mis-calibrated under distribution shift, while conformal coverage also requires exchangeability?
- How large must $\tau$ be before joint-prediction metrics separate agents that marginal metrics cannot?
- Can scores be learned jointly with the model (fn. 4) without breaking the exchangeability argument?
- How do per-instance Bayesian uncertainty and average-case conformal coverage trade off?

## Reading notes
- Printed pages 575–589; printed 590 is blank. pdf = printed + 34.
- Misprints seen: "portional" for "proportional" (p. 578), "Illusration" (Fig. 14.5 caption), "$s_1<\cdots s_n$" with missing "<" (p. 586), and "$P(y|D,\mathcal D_T)$" in the denominator of (14.45), probably meant $P(y|x,\mathcal D_T)$.
- In the proof (p. 586) the index appears printed as $i=\lceil(n+1)(1-\alpha)\rceil/n$ (a fraction over $n$). An index should be an integer, so the "$/n$" belongs to the quantile level, not the index (my reading).
- Eq. (14.54) as printed uses $\hat t_{\alpha/2}$ in both arguments of the max. The surrounding text speaks of distance outside the interval, so presumably the upper quantile ($\hat t_{1-\alpha/2}$) should appear in the second argument. Fig. 14.5b labels $\hat t_{1-\alpha/2}$. This is my inference.
- (14.6) with $\lambda=1$ matches exactly if $r$ is the summed log loss. With the $1/N$ in (14.4), the equivalence needs $\lambda=1/N$ (my check). Likewise, (14.10) with $\lambda=N$ is consistent with the $1/N$-scaled $r$.
- Fig. 14.3's $T=2$ panel looks like about (0.57, 0.21, 0.21). My computation of $\mathrm{softmax}((3,0,1)/2)$ gives about (0.63, 0.14, 0.23). The $T=1$ panel matches (0.84, 0.04, 0.11).
- Eq. (14.50) writes $y^{n+1}$ (superscript) where $y_{n+1}$ is meant.
- In (14.37) the underbrace labelled $d^{CE}_{\mathcal E,Q}$ spans $\mathbb E[\log Q]$ without the minus sign, while (14.38) defines $\hat d^{CE}$ with a leading minus. The text calls the term the NLL, so the NLL is the negated term.
- Footer: "Online version. December 10, 2025", CC-BY-NC-ND.

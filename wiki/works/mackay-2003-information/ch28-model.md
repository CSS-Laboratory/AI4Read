---
id: mackay-2003-information/ch28-model
work: mackay-2003-information
unit: "27 Laplace's Method and 28 Model Comparison and Occam's Razor"
pages: 341-355
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Laplace's Method; Model Comparison and Occam's Razor

## L0 — One line
Bayesian inference ranks models by their evidence P(D | H), which automatically penalizes needless complexity through an "Occam factor", and Laplace's Gaussian approximation gives a way to approximate that evidence.

## L1 — The gist (≤ 120 words)
How can we compare models of different complexity when more complex models can always fit the data better? MacKay ranks models by their evidence P(D | H): the probability a model gave to the data that actually occurred. A flexible model spreads its predictions over many possible data sets, so it scores lower when the data fit a simpler model too. Approximately, evidence ≈ best-fit likelihood × Occam factor (in 1-D: posterior width ÷ prior width), computed with Laplace's Gaussian approximation. Worked examples: one box versus two behind a tree (about 1000 : 1) and "add 4" versus a cubic rule (about 4×10⁷ : 1). Minimum description length is a complementary message-length view.

**Prerequisites:** Bayes' theorem; Taylor expansion and second derivatives; Gaussian integral; determinant and eigenvalues of a matrix; logs base 2.

## L2 — Key ideas
- Laplace's method replaces an unnormalized density by a Gaussian at its peak. Its normalizing constant (the integral of the density) is then $P^*(\mathbf{x}_0)\sqrt{(2\pi)^K/\det \mathbf{A}}$ (p. 341). It depends on the choice of coordinates (p. 342).
- Occam's razor needs no built-in preference for simplicity. The data-dependent ratio $P(D\mid H_1)/P(D\mid H_2)$ already penalizes complex models, because they spread their predictions thinly (p. 344).
- Two levels of inference: fitting parameters inside a model, and comparing models. The evidence is the normalizer of level 1 and the score at level 2 (pp. 346–348).
- Evidence ≈ best-fit likelihood × Occam factor. In 1-D with a uniform prior, the Occam factor is $\sigma_{w|D}/\sigma_w$, the fraction of the prior parameter space that survives the data (pp. 348–349).
- Several parameters: the Occam factor is $P(\mathbf{w}_{MP}\mid H)\det^{-1/2}(\mathbf{A}/2\pi)$. If the posterior is roughly Gaussian, it needs only the Hessian $\mathbf{A}$ (the matrix of second derivatives of $-\ln$ posterior), already computed for error bars (p. 350).
- Worked examples give odds of about 4×10⁷:1 (arithmetic vs cubic rule) and about 1000:1 (one vs two boxes) (pp. 345, 351).
- Minimum description length (MDL), with message length $L=-\log_2 P$, can reproduce Bayesian model comparison. It also explains the evidence as a sum of on-line predictions, and the bits-back argument (send a posterior sample, then recover its random bits) gives $-\log P(D\mid H)$ up to a constant (pp. 352–353).
- Model comparison needs proper priors; improper priors make evidences and Occam factors meaningless (pp. 353–354).

## L3 — Walkthrough

### Chapter 27 — Laplace's method (pp. 341–342)
**Setup.** Let $P^*(x)$ be an unnormalized density with a peak at $x_0$. We want its normalizing constant (the integral over all $x$):
$$Z_P \equiv \int P^*(x)\,dx \tag{27.1}$$
Taylor-expand the log around the peak:
$$\ln P^*(x) \simeq \ln P^*(x_0) - \frac{c}{2}(x-x_0)^2 + \cdots \tag{27.2}$$
$$c = -\frac{\partial^2}{\partial x^2}\ln P^*(x)\Big|_{x=x_0} \tag{27.3}$$
(p. 341). Approximate $P^*$ by an unnormalized Gaussian and use that Gaussian's normalizer:
$$Q^*(x) \equiv P^*(x_0)\exp\!\left[-\frac{c}{2}(x-x_0)^2\right] \tag{27.4}$$
$$Z_Q = P^*(x_0)\sqrt{\frac{2\pi}{c}} \tag{27.5}$$
(p. 341).

**K dimensions.** For $\mathbf{x}\in\mathbb{R}^K$ (shape $K\times1$), let $\mathbf{A}$ ($K\times K$) be the matrix of second derivatives of $-\ln P^*$ at the maximum:
$$A_{ij} = -\frac{\partial^2}{\partial x_i\partial x_j}\ln P^*(\mathbf{x})\Big|_{\mathbf{x}=\mathbf{x}_0} \tag{27.6}$$
$$\ln P^*(\mathbf{x}) \simeq \ln P^*(\mathbf{x}_0) - \tfrac12(\mathbf{x}-\mathbf{x}_0)^{\mathsf T}\mathbf{A}(\mathbf{x}-\mathbf{x}_0)+\cdots \tag{27.7}$$
$$Z_P \simeq Z_Q = P^*(\mathbf{x}_0)\frac{1}{\sqrt{\det\frac{1}{2\pi}\mathbf{A}}} = P^*(\mathbf{x}_0)\sqrt{\frac{(2\pi)^K}{\det\mathbf{A}}} \tag{27.8}$$
(p. 341). Predictions can be made with $Q$. Physicists call this the saddle-point approximation (p. 341).

**Gaussian normalizer.**
$$\int d^K\mathbf{x}\,\exp\!\left[-\tfrac12\mathbf{x}^{\mathsf T}\mathbf{A}\mathbf{x}\right]=\sqrt{\frac{(2\pi)^K}{\det\mathbf{A}}} \tag{27.9}$$
Proof idea: rotate orthogonally to the basis $\mathbf{u}$ in which $\mathbf{A}$ is diagonal. The integral becomes a product of 1-D integrals
$$\int du_i\,\exp\!\left[-\tfrac12\lambda_i u_i^2\right]=\sqrt{\frac{2\pi}{\lambda_i}} \tag{27.10}$$
and the product of the eigenvalues $\lambda_i$ is $\det\mathbf{A}$ (p. 342).

**Basis dependence.** If $x$ is changed to a nonlinear function $u(x)$, with density $P(u)=P(x)\,|dx/du|$, the approximate constants $Z_Q$ will in general differ. MacKay calls this a defect, since the true $Z_P$ is basis-independent, or an opportunity, since one can look for the basis where the approximation is most accurate (p. 342).

*Intuition note:* Near a sharp peak the log-density looks like a parabola, so the density looks like a bell curve whose width is set by the curvature. The area under the bell curve is easy, and it stands in for the true area. Reparametrizing changes which bell curve you fit, so the answer changes.

Exercises 27.1–27.3 (p. 342) are listed under "Exercises worth doing".

### Chapter 28 — 28.1 Occam's razor (pp. 343–351)

**Motivation (pp. 343–344).** Figure 28.1 shows a tree and boxes. Behind the trunk there could be one box or two. Occam's razor says to prefer the simplest explanation that fits the data, which here is one box. The question is whether this is an ad hoc rule or has a convincing reason. The intuitive reason offered is that two boxes with the same height and colour would be a remarkable coincidence. To build artificial intelligences that interpret data correctly, this feeling must become a concrete theory (p. 343).

The razor is often justified aesthetically (Dirac's remark on mathematical beauty) or by past empirical success. MacKay's claim: "Coherent inference (as embodied by Bayesian probability) automatically embodies Occam's razor, quantitatively." (p. 344)

**Model comparison (p. 344).** By Bayes' theorem the posterior odds of $H_1$ over $H_2$ given data $D$ are
$$\frac{P(H_1\mid D)}{P(H_2\mid D)}=\frac{P(H_1)}{P(H_2)}\,\frac{P(D\mid H_1)}{P(D\mid H_2)} \tag{28.1}$$
- The first ratio holds prior beliefs. A prior bias for simplicity could be inserted there on aesthetic or empirical grounds, but it is not necessary.
- The second ratio, the data-dependent factor, embodies the razor automatically.
- Simple models tend to make precise predictions, and complex models are capable of making a greater variety of predictions (figure 28.3). So a complex $H_2$ must spread its predictive probability $P(D\mid H_2)$ more thinly over data space.
- If the data are compatible with both models, the simpler one therefore turns out more probable, with no subjective dislike of complexity needed; the prior just has to give equal probabilities to simplicity and complexity (p. 344).
- Figure 28.3 labels $P(D\mid H_i)$ the *evidence* for $H_i$. If equal priors are assigned and the data fall in region $C_1$, the less powerful $H_1$ is the more probable model (p. 344).

**Example: −1, 3, 7, 11 (pp. 344–345).** Predict the next two numbers. The popular answer is "15, 19" via "add 4". The alternative "−19.9, 1043.8" comes from the rule $x\to -x^3/11+9/11\,x^2+23/11$, which fits the four numbers equally well. Two theories:
- $H_a$: arithmetic progression "add $n$", $n$ an integer.
- $H_c$: $x\to cx^3+dx^2+e$ with $c,d,e$ fractions.

Take equal priors on the two theories.
- *Priors for $H_a$.* The added integer $n$ and the first number each lie anywhere in $[-50,50]$, which is 101 values each. Only $\{n=4,\ \text{first}=-1\}$ fits the data:
$$P(D\mid H_a)=\frac1{101}\frac1{101}=0.00010 \tag{28.2}$$
- *Priors for $H_c$.* Each fraction has a numerator in $[-50,50]$ and a denominator in $[1,50]$. The first number has the same prior as in $H_a$. Fractions are used because real parameters would give $D$ an infinitesimal probability relative to $H_a$. The fraction $c=-1/11$ can be written 4 ways ($-1/11,-2/22,-3/33,-4/44$), $d$ in 4 ways, $e$ in 2 ways:
$$P(D\mid H_c)=\frac1{101}\left(\frac4{101}\frac1{50}\right)\left(\frac4{101}\frac1{50}\right)\left(\frac2{101}\frac1{50}\right)=2.5\times10^{-12} \tag{28.3}$$
- *Result.* The odds in favour of $H_a$ are about forty million to one (p. 345).

The answer depends on subjective assumptions about the priors on $n,c,d,e$. Bayesians make no apology, since inference needs assumptions. But the quantitative prior details do not affect the qualitative effect: the complex theory "always suffers an 'Occam factor'" because it has more parameters and can predict more data sets. In larger problems the Occam factors typically grow and the sensitivity to prior details shrinks (p. 345).

**Bayesian methods and data analysis (p. 346).** Figure 28.4 shows the modelling cycle: gather data, create alternative models, fit each model, assign preferences to models, then choose actions or new data, or create new models. Bayes' theorem can be used only in the two inference boxes ("fit each model" and "assign preferences"). It does not tell you how to invent models. Fitting gives most probable parameters and error bars, often little different from orthodox statistics. Model comparison is where Bayesian methods are "in a class of their own" (figure 28.4 caption, p. 346). The epicycle example: the epicyclic model fits planetary data at least as well as the Copernican one but with more parameters. Two extra epicycle parameters per planet coincide with the sun's period and radius, which the source calls a coincidence (p. 346).

**Two levels of inference (pp. 346–347).**
- Level 1: assume one model is true and infer its parameters, summarized by most probable values and error bars.
- Level 2: compare the models in the light of the data.
- Both levels are distinct from decision theory. Inference assigns probabilities to hypotheses, and decision theory typically chooses actions to minimize expected loss. Comparing models does not mean choosing one: ideal Bayesian predictions sum over all models, weighted by their probabilities (p. 347).
- MacKay calls it a "popular myth" that Bayesians differ from orthodox statisticians only by subjective priors that rarely matter. At level 1 results often differ little. The less appreciated part is level 2 (p. 347).
- It is not possible simply to choose the best-fitting model: more complex models can always fit better, so maximum-likelihood model choice would lead inevitably to implausible, over-parameterized models that generalize poorly (p. 347).

**Level 1: model fitting (pp. 347–348).** A model $H_i$ has a prior $P(\mathbf{w}\mid H_i)$ over a parameter vector $\mathbf{w}$ and predictions $P(D\mid\mathbf{w},H_i)$.
$$P(\mathbf{w}\mid D,H_i)=\frac{P(D\mid\mathbf{w},H_i)P(\mathbf{w}\mid H_i)}{P(D\mid H_i)},\quad\text{i.e. Posterior}=\frac{\text{Likelihood}\times\text{Prior}}{\text{Evidence}} \tag{28.4}$$
The normalizer $P(D\mid H_i)$ is commonly ignored at level 1 and named the *evidence* for $H_i$. With $\mathbf{w}_{MP}$ the maximum of the posterior, $\mathbf{A}=-\nabla\nabla\ln P(\mathbf{w}\mid D,H_i)|_{\mathbf{w}_{MP}}$ (the Hessian) and $\Delta\mathbf{w}=\mathbf{w}-\mathbf{w}_{MP}$:
$$P(\mathbf{w}\mid D,H_i)\simeq P(\mathbf{w}_{MP}\mid D,H_i)\exp\!\left(-\tfrac12\Delta\mathbf{w}^{\mathsf T}\mathbf{A}\Delta\mathbf{w}\right) \tag{28.5}$$
So the posterior is locally Gaussian with covariance $\mathbf{A}^{-1}$, equivalent to error bars. Whether this is good depends on the problem. The posterior maximum and mean have no fundamental status in Bayesian inference, since both change under nonlinear reparametrization (pp. 347–348).

**Level 2: model comparison (p. 348).**
$$P(H_i\mid D)\propto P(D\mid H_i)P(H_i) \tag{28.6}$$
With equal priors, models are ranked by their evidence. The normalizer $P(D)=\sum_iP(D\mid H_i)P(H_i)$ is omitted because new models may be developed after the data arrive. Inference is open ended. The evidence can be computed for parametric and non-parametric models, in regression, classification or density estimation, so it is "transportable". It embodies the razor in all of them (p. 348).

**Evaluating the evidence (pp. 348–349).**
$$P(D\mid H_i)=\int P(D\mid\mathbf{w},H_i)P(\mathbf{w}\mid H_i)\,d\mathbf{w} \tag{28.7}$$
If the integrand has a strong peak at $\mathbf{w}_{MP}$ (figure 28.5), Laplace's method in 1-D gives peak height times width $\sigma_{w|D}$:
$$P(D\mid H_i)\simeq\underbrace{P(D\mid\mathbf{w}_{MP},H_i)}_{\text{best-fit likelihood}}\times\underbrace{P(\mathbf{w}_{MP}\mid H_i)\,\sigma_{w|D}}_{\text{Occam factor}} \tag{28.8}$$
The Occam factor has magnitude below one and penalizes $H_i$ for having the parameter (p. 349).

**Interpretation (p. 349).** Suppose the prior is uniform on a large interval $\sigma_w$. Then $P(w_{MP}\mid H_i)=1/\sigma_w$ and
$$\text{Occam factor}=\frac{\sigma_{w|D}}{\sigma_w} \tag{28.9}$$
- This is the ratio of posterior to prior accessible parameter volume: the factor by which the hypothesis space collapses when the data arrive.
- $H_i$ can also be viewed as a number of exclusive submodels, only one of which survives when the data arrive. The Occam factor is the inverse of that number.
- Its log measures the information gained about the parameters.
- Penalties: a complex model with many parameters, each free over a large range $\sigma_w$, will typically be penalized by a stronger Occam factor than a simpler model. Models needing fine tuning (small $\sigma_{w|D}$) are also penalized.
- The Occam factor depends on the number of parameters and on the prior probability assigned to them.
- The best evidence comes from a trade-off between this complexity measure and data misfit.
- In contrast to alternative complexity measures, it is straightforward to evaluate: it depends only on error bars already found when fitting (p. 349).

**Figure 28.6 (pp. 349–350).** Three models have equal priors and one parameter $w$ each. They have prior ranges $\sigma_w$ of different widths, and $H_3$ has the broadest. The data space is one-dimensional. Dots are samples from the joint $P(D,w\mid H_i)$, and each model has the same number of dots. For the observed $D$:
- $H_3$ has less evidence than $H_2$ because fewer of its dots lie on the line, i.e. its Occam factor $\sigma_{w|D}/\sigma_w$ is smaller.
- $H_1$ has the least evidence because its best fit is very poor.
- The most probable model is $H_2$ (p. 350).

**Several parameters (p. 350).** If the posterior is roughly Gaussian, with $\mathbf{A}=-\nabla\nabla\ln P(\mathbf{w}\mid D,H_i)$ of shape $K\times K$:
$$P(D\mid H_i)\simeq\underbrace{P(D\mid\mathbf{w}_{MP},H_i)}_{\text{best-fit likelihood}}\times\underbrace{P(\mathbf{w}_{MP}\mid H_i)\det{}^{-1/2}(\mathbf{A}/2\pi)}_{\text{Occam factor}} \tag{28.10}$$
This Gaussian approximation is expected to become more accurate as data increase. So Bayesian model comparison is a simple extension of maximum-likelihood model selection: multiply the best-fit likelihood by the Occam factor. If the Gaussian approximation is good, it needs only $\mathbf{A}$, and so is no more demanding than finding best-fit parameters and error bars (p. 350).

*Intuition note:* The evidence asks "how much of my prior guess-space did the data keep?". A model that could have predicted many different data sets typically keeps a smaller fraction, so it pays a bigger penalty. A model that needs only a narrow range of parameters relative to its prior range pays less.

### 28.2 Example: one or two boxes (p. 351)
Assumptions: a 50-pixel region, a trunk 10 pixels wide, and 16 distinguishable colours.
- **$H_1$** (one box) has four free parameters: three coordinates for the top three edges and one colour. $H_2$ (two boxes) has eight parameters plus a binary one saying which box is nearer.
- **Priors for $H_1$.** Separable and uniform. Location, width and height each have 20 distinguishable values, and colour has 16. Only one setting fits, and it predicts the data perfectly:
$$P(D\mid H_1)=\frac1{20}\frac1{20}\frac1{20}\frac1{16} \tag{28.11}$$
- **$H_2$.** Six of the nine parameters are well determined and three are partly constrained. For example, if the left box is furthest, its width is between 8 and 30 pixels, and if it is nearer, between 8 and 18. The ballpark answer takes the two unconstrained real variables to have half their values available and the binary variable completely undetermined:
$$P(D\mid H_2)\simeq\frac1{20}\frac1{20}\frac{10}{20}\frac1{16}\cdot\frac1{20}\frac1{20}\frac{10}{20}\frac1{16}\cdot\frac22 \tag{28.12}$$
- **Posterior ratio** (equal priors on $H_1,H_2$):
$$\frac{P(D\mid H_1)P(H_1)}{P(D\mid H_2)P(H_2)}=\frac{1}{\frac1{20}\frac{10}{20}\frac{10}{20}\frac1{16}} \tag{28.13}$$
$$=20\times2\times2\times16\simeq1000/1 \tag{28.14}$$
($20\cdot2\cdot2\cdot16=1280$; added step.) So the data favour the simpler hypothesis roughly 1000 to 1 (p. 351).
- **Reading the four factors as Occam factors.** $H_2$ pays two big ones ($1/20$ and $1/16$) for the suspicious coincidences that the box heights and colours match exactly. It pays two lesser ones for both boxes having an edge conveniently hidden behind the tree or each other (p. 351).

### 28.3 Minimum description length (MDL) (pp. 352–353)
**Message lengths.** The length $L(x)$ in bits of a lossless message corresponds to a probability model:
$$P(x)=2^{-L(x)},\qquad L(x)=-\log_2P(x) \tag{28.15}$$
The MDL principle (Wallace and Boulton, 1968) prefers models that communicate the data in the fewest bits. A two-part message names the model and then sends $D$ within it, to a pre-arranged precision $\delta D$, so $L(D,H)=L(H)+L(D\mid H)$.
- $L(H)$ defines an implicit prior $P(H)$, and $L(D\mid H)$ corresponds to a density $P(D\mid H)$.
$$L(D,H)=-\log P(H)-\log\big(P(D\mid H)\,\delta D\big) \tag{28.16}$$
$$=-\log P(H\mid D)+\text{const.} \tag{28.17}$$
- In principle MDL can always be read as Bayesian model comparison and vice versa (p. 352).
- The key term $L(D\mid H)$, corresponding to the evidence, is often imagined as a parameter block plus a data block (figure 28.8).
- Few parameters give a short parameter block but long residuals. More parameters lengthen the parameter block and shorten the data block. An intermediate model ($H_2$ in the figure) minimizes the sum (p. 352).

**Precision of parameters.** The precision $\delta D$ only adds a constant if it is small relative to the noise. The precision of $\mathbf{w}$ matters: coarser $\mathbf{w}$ shortens the parameter message but typically lengthens the data message. There is a non-trivial optimum. In simple Gaussian cases it can be solved (Wallace and Freeman, 1987) and is closely related to the posterior error bars $\mathbf{A}^{-1}$. The optimal parameter message length is "virtually identical" to the log of the Occam factor in (28.10), though the random element of truncation makes the encoding slightly sub-optimal. MacKay concludes that MDL has "no apparent advantages" over the direct probabilistic approach. It remains useful as a pedagogical tool, for motivating priors and for insight into ways of breaking the modelling task down (pp. 352–353).

**On-line learning and cross-validation (p. 353).** For sequential data $D=\mathbf{t}^{(1)},\dots,\mathbf{t}^{(N)}$:
$$\log P(D\mid H)=\log P(\mathbf{t}^{(1)}\mid H)+\log P(\mathbf{t}^{(2)}\mid\mathbf{t}^{(1)},H)+\cdots+\log P(\mathbf{t}^{(N)}\mid\mathbf{t}^{(1)}\dots\mathbf{t}^{(N-1)},H) \tag{28.18}$$
Leave-one-out cross-validation examines the average of just the last term under random re-orderings. The evidence sums how well the model predicted all the data, starting from scratch (p. 353).

**Bits-back encoding (Hinton and van Camp, 1993) (p. 353).**
- Send a random sample $\mathbf{w}$ from the posterior $P(\mathbf{w}\mid D,H)$ to small granularity $\delta\mathbf{w}$, with length $L(\mathbf{w}\mid H)=-\log[P(\mathbf{w}\mid H)\delta\mathbf{w}]$.
- Then send the data relative to $\mathbf{w}$, with length $L(D\mid\mathbf{w},H)=-\log[P(D\mid\mathbf{w},H)\delta D]$.
- After receiving the data, the receiver can deduce the random bits used to draw $\mathbf{w}$. These "bits back" number $-\log[P(\mathbf{w}\mid D,H)\delta\mathbf{w}]$. They need not count, because they could carry another optimally encoded message.
$$L(\mathbf{w}\mid H)+L(D\mid\mathbf{w},H)-\text{`Bits back'}=-\log\frac{P(\mathbf{w}\mid H)P(D\mid\mathbf{w},H)\,\delta D}{P(\mathbf{w}\mid D,H)}=-\log P(D\mid H)-\log\delta D \tag{28.19}$$
The last step uses $P(\mathbf{w}\mid H)P(D\mid\mathbf{w},H)/P(\mathbf{w}\mid D,H)=P(D\mid H)$ from (28.4) (added step). So the thought experiment yields the optimal description length. Frey (1998) turned bits-back into a practical compression method for latent-variable models (p. 353).

*Intuition note:* The bits-back argument shows the evidence corresponds to a message length: $-\log P(D\mid H)$ bits, plus a constant from the data precision. In the MDL picture, a more complex model needs a longer parameter block, which is traded off against a shorter data block.

### Further reading (pp. 353–354)
MacKay points to Jaynes (1983), Gull (1988), Loredo (1990) and MacKay (1992a), and to the textbooks Box and Tiao (1973) and Berger (1985). On improper priors (Dawid et al., 1996): for model comparison, proper priors are essential, because otherwise the evidences and Occam factors are meaningless. Without any intention to compare models it may be safe to use improper priors, but even then there are pitfalls. MacKay agrees with the advice to always use proper priors, tempered by encouragement to be smart and to recognize opportunities for approximation (pp. 353–354).

### 28.4 Exercises (pp. 354–355)
Exercises are listed below under "Exercises worth doing". No solutions are printed.

## Toy example (ours, not from the text)
Eight coin flips give a specific sequence with 4 heads and 4 tails. Compare $H_1$: fair coin, $p=1/2$ (no free parameter); and $H_2$: $p$ unknown, uniform prior on $(0,1)$. Priors on the models are equal.

1. $P(D\mid H_1)=(1/2)^8=1/256\approx0.003906$.
2. $P(D\mid H_2)=\int_0^1p^4(1-p)^4\,dp=\dfrac{4!\,4!}{9!}=\dfrac{576}{362880}=\dfrac1{630}\approx0.001587$ (standard Beta integral).
3. Odds for $H_1$: $630/256\approx2.46$. The more flexible model fits no better, since its best fit $p=1/2$ gives the same likelihood $1/256$, but it pays an Occam factor $\text{evidence}/\text{best fit}=256/630\approx0.406$.
4. Laplace check, matching (28.8)–(28.9): $\ln P^*=4\ln p+4\ln(1-p)$, so $c=4/p^2+4/(1-p)^2=16+16=32$ at $p=0.5$. Width $\sigma_{w|D}=\sqrt{2\pi/32}=\sqrt{0.19635}\approx0.443$. The prior is uniform on width 1, so the Occam factor is $0.443/1$ and $Z_Q\approx0.443/256\approx0.001731$, close to the exact $0.001587$.

## Concepts
- [[laplace-approximation]] (new) — replace a density by a Gaussian at its peak; $Z\simeq P^*(\mathbf{x}_0)\sqrt{(2\pi)^K/\det\mathbf{A}}$ (p. 341)
- [[saddle-point-approximation]] (new) — the physicists' name for the same approximation (p. 341)
- [[basis-dependence-of-laplace]] (new) — the approximate $Z_Q$ changes under nonlinear reparametrization, while the true $Z_P$ does not (p. 342)
- [[marginal-likelihood-evidence]] — $P(D\mid H)=\int P(D\mid\mathbf{w},H)P(\mathbf{w}\mid H)d\mathbf{w}$; the normalizer of the parameter posterior and the score used to rank models (pp. 347–348)
- [[occam-factor]] (new) — the factor below one multiplying the best-fit likelihood. In 1-D with a uniform prior it is $\sigma_{w|D}/\sigma_w$; in $K$ dimensions $P(\mathbf{w}_{MP}\mid H)\det^{-1/2}(\mathbf{A}/2\pi)$ (pp. 349–350)
- [[bayesian-occams-razor]] — the data-dependent ratio of evidences penalizes complex models without any prior bias for simplicity (p. 344)
- [[two-levels-of-inference]] (new) — level 1 fits parameters within a model, level 2 compares models; both are distinct from decision theory (p. 346)
- [[bayes-theorem]] — used for posterior over parameters (28.4) and over models (28.6) (pp. 347–348)
- [[likelihood]], [[prior-distribution]], [[posterior-distribution]] — as in (28.4) (p. 347)
- [[posterior-predictive-distribution]] — ideal predictions sum over all models weighted by their probabilities (p. 347)
- [[minimum-description-length-mdl]] — prefer the model giving the shortest total message; $L=-\log_2P$, so MDL maps onto Bayesian comparison (p. 352)
- [[cross-validation-loo-waic]] — here leave-one-out is contrasted with the evidence: it examines the average of just the last term of the on-line sum under random re-orderings (p. 353)
- [[sequential-updating]] — the log evidence as a sum of on-line predictive terms (28.18) (p. 353)
- [[bits-back-coding]] (new) — send a posterior sample, then recover its random bits; net cost $-\log P(D\mid H)$ plus a constant (p. 353)
- [[proper-vs-improper-priors]] (new) — model comparison requires proper priors (pp. 353–354)

## Canonical instances
- [[boxes-behind-tree]] — one vs two boxes; evidence ratio about 1000:1 (pp. 343, 351)
- [[arithmetic-vs-cubic-sequence]] — $H_a$ vs $H_c$ on −1, 3, 7, 11; odds about 4×10⁷:1 (pp. 344–345)
- [[epicycles-vs-copernicus]] — more parameters and a coincidence in the extra parameters (p. 346)
- [[three-model-hypothesis-space]] — figure 28.6, with three prior widths and $H_2$ the most probable (pp. 349–350)
- [[death-penalty-simpsons-paradox]] — the data of exercise 28.4 (pp. 354–355)

## Bridges (candidates)
- [same-math] MDL message length $L=-\log_2P$ ↔ information-theory: Shannon code length $-\log_2P(x)$ — the same relation, used to translate models into bits (p. 352)
- [same-math] Laplace approximation ↔ physics: saddle-point approximation — the source names them as the same method (p. 341)
- [structural-analogy] log Occam factor as information gained about parameters ↔ information-theory: reduction of uncertainty (entropy) from data — the source describes the log as "information gained" (p. 349)
- [structural-analogy] evidence as a product of on-line predictions (28.18) ↔ information-theory: chain rule for entropy and cumulative log-loss — a joint probability factorizes step by step
- [structural-analogy] evidence vs leave-one-out cross-validation ↔ bayesian: model-comparison scores — one rewards all sequential predictions, the other only the last (p. 353)

## Questions this raises
- How sensitive are evidence-based rankings to the prior ranges (such as ±50 or 20 pixels), and when do they change the winner?
- When is the Gaussian (Laplace) approximation to the evidence poor, and how can one choose a better basis?
- If ideal predictions average over all models, when is picking a single model a good enough approximation?
- Can the optimal precision in MDL be derived beyond the simple Gaussian cases?

## Exercises worth doing
(The book's difficulty marks [2] and [3] are rendered below as easy and medium.)
- Ex. 27.1 (p. 342) — Laplace approximations for a Poisson rate $\lambda$ with prior $1/\lambda$, in both $\lambda$ and $\log\lambda$; shows basis dependence — difficulty: easy
- Ex. 27.2 (p. 342) — Laplace for $\int f(a)^{u_1}(1-f(a))^{u_2}da$; error measured in bits against the exact answer — difficulty: easy
- Ex. 28.1 (p. 354) — evidence for a uniform model vs a one-parameter linear-density model on five data points — difficulty: medium
- Ex. 28.2 (p. 354) — evidence for a flat line vs a sloped line with Gaussian priors; model comparison in regression — difficulty: medium
- Ex. 28.3 (p. 354) — fair vs biased die, exactly (Dirichlet formulae) and by Laplace; basis choice matters — difficulty: medium
- Ex. 28.4 (p. 354) — evidence for four graphical-model hypotheses on the death-penalty table; prior sensitivity — difficulty: medium

## Reading notes
- Source unit combines ch. 27 (Laplace's Method, printed pp. 341–342) and ch. 28 (printed pp. 343–355). Printed = pdf − 12.
- The text layer of printed p. 343 is garbled by the figure, but the image is clear. Figure axes and labels on pp. 344, 346 and 350 come from the text layer and images.
- Eq. (28.14) prints "≃ 1000/1". The exact product is 1280.
- The source says the optimal MDL parameter message length is "virtually identical to the log of the Occam factor" (p. 352). It does not discuss the sign: a message length is positive, whereas the log of a factor below one is negative.
- Exercise 28.4 starts on p. 354 (the table) and its Simpson's paradox remark is on p. 355. Recomputing from the printed table: overall death-penalty rates are 19/160 (white defendants) and 17/166 (black defendants); for white victims 19/151 vs 11/63; for black victims 0/9 vs 6/103, so the remark matches. The printed 14% (white victim) matches 30/214; the printed 6% (black victim) is 6/112 ≈ 5.4%.
- Eq. (28.3) is printed as $0.0000000000025=2.5\times10^{-12}$. Eq. (28.2) is rounded to 0.00010 (exactly $1/101^2\approx0.000098$).

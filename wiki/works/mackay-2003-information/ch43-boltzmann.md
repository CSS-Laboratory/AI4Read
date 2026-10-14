---
id: mackay-2003-information/ch43-boltzmann
work: mackay-2003-information
unit: "43 Boltzmann Machines"
pages: 522-526
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Boltzmann Machines

## L0 — One line
A Boltzmann machine is a stochastic Hopfield network whose maximum-likelihood learning compares correlations measured on data ("waking") with correlations under its own model ("sleeping"); hidden units can induce higher-order correlations among visible units while the model keeps only pairwise weights.

## L1 — The gist (≤ 120 words)
Can a Hopfield network be turned into a generative probability model that learns from data? MacKay makes the network sample from $P(\mathbf x|\mathbf W)\propto\exp(\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x)$ by Gibbs sampling. Maximum likelihood then gives a gradient equal to the data correlation minus the model correlation. At $\mathbf W=0$ this reduces to the Hebb rule. Pairwise weights capture second-order statistics (averages of products of pairs of units), which are not enough for ensembles such as the shifter ensemble (lower half = shifted copy of upper half). Hidden (latent) units, with pairwise weights, allowed the labelled shifter ensemble to be learned. With hidden units the learning rule keeps the waking/sleeping form, but both terms need Monte Carlo, so machines are slow and little used.

**Prerequisites:** probability and Bayes' theorem; partial derivatives and $\ln$; Gibbs sampling and Monte Carlo averages; the Hopfield network of earlier chapters (energy, Hebb rule).

## L2 — Key ideas
- The Hopfield energy defines a Boltzmann distribution $P(\mathbf x|\mathbf W)=\exp[-E]/Z$. A stochastic activity rule samples from it by Gibbs sampling (p. 522).
- The log-likelihood gradient is $N[\langle x_ix_j\rangle_{\rm Data}-\langle x_ix_j\rangle_{P(\mathbf x|\mathbf W)}]$: a data term minus a model term (p. 523).
- The model term needs Monte Carlo. In the special case $\mathbf W=0$ the gradient can be evaluated exactly, and one gradient step then gives the Hebb rule (p. 523).
- The two terms are read as "waking" and "sleeping" phases. Learning stops changing the weights when dream correlations match real-world ones (pp. 523–524).
- Second-order statistics can be useless: for the plain shifter ensemble they convey no useful information, and the labelled one is still not learnable from them alone (p. 524).
- Explicit higher-order terms are easy to simulate but need far too many parameters (p. 525).
- Hidden units induce higher-order visible correlations with only pairwise weights. The learning rule keeps the waking/sleeping form, with visible units clamped in the waking term (pp. 525–526).
- Two Monte Carlo estimates per gradient make Boltzmann machines slow, so they are not in widespread use (p. 526).

## L3 — Walkthrough

### 43.1 From Hopfield networks to Boltzmann machines
The binary Hopfield network minimizes $E(\mathbf x)=-\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x$ (43.1). The continuous Hopfield network with $x_n=\tanh(a_n)$ can be viewed as approximating the associated distribution (p. 522):
$$P(\mathbf x|\mathbf W)=\frac{1}{Z(\mathbf W)}\exp[-E(\mathbf x)]=\frac1{Z(\mathbf W)}\exp\!\Big[\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x\Big]\tag{43.2}$$
This motivates a network that implements the distribution. The **Boltzmann machine** (stochastic Hopfield network; Hinton and Sejnowski, 1986) computes the activation $a_i$ (eq. 42.3, defined in an earlier chapter) and sets $x_i=+1$ with probability
$$\frac1{1+e^{-2a_i}},\quad\text{else }x_i=-1.\tag{43.3}$$
This rule implements Gibbs sampling for (43.2) (p. 522).

**Learning.** Given examples $\{\mathbf x^{(n)}\}_1^N$, adjust $\mathbf W$ so that (43.4), the same form as (43.2), matches them. Bayes' theorem gives the posterior over weights (p. 522):
$$P(\mathbf W|\{\mathbf x^{(n)}\})=\frac{\big[\prod_{n=1}^N P(\mathbf x^{(n)}|\mathbf W)\big]P(\mathbf W)}{P(\{\mathbf x^{(n)}\})}\tag{43.5}$$
MacKay keeps only the likelihood term and derives a maximum-likelihood algorithm. A full Bayesian approach might have advantages (p. 523). The log-likelihood is
$$\ln\prod_n P(\mathbf x^{(n)}|\mathbf W)=\sum_n\Big[\tfrac12\mathbf x^{(n)\rm T}\mathbf W\mathbf x^{(n)}-\ln Z(\mathbf W)\Big]\tag{43.6}$$
It is differentiated with respect to $w_{ij}$, with $\mathbf W$ symmetric ($w_{ji}=w_{ij}$). Exercise 43.1 asks to show
$$\frac{\partial}{\partial w_{ij}}\ln Z(\mathbf W)=\sum_{\mathbf x}x_ix_jP(\mathbf x|\mathbf W)=\langle x_ix_j\rangle_{P(\mathbf x|\mathbf W)}\tag{43.7}$$
Hence (p. 523):
$$\frac{\partial}{\partial w_{ij}}\ln P(\{\mathbf x^{(n)}\}|\mathbf W)=\sum_{n=1}^N\Big[x_i^{(n)}x_j^{(n)}-\langle x_ix_j\rangle_{P(\mathbf x|\mathbf W)}\Big]\tag{43.8}$$
$$=N\Big[\langle x_ix_j\rangle_{\rm Data}-\langle x_ix_j\rangle_{P(\mathbf x|\mathbf W)}\Big]\tag{43.9}$$
with $\langle x_ix_j\rangle_{\rm Data}\equiv\frac1N\sum_n x_i^{(n)}x_j^{(n)}$ (43.10) and $\langle x_ix_j\rangle_{P(\mathbf x|\mathbf W)}\equiv\sum_{\mathbf x}x_ix_jP(\mathbf x|\mathbf W)$ (43.11) (p. 523).

The data correlation is easy to compute. The model correlation is harder, but can be estimated by Monte Carlo: average $x_ix_j$ while iterating rule (43.3) (p. 523).

**Special case $\mathbf W=0$.** By symmetry the model correlation must be zero (p. 523). Gradient descent with rate $\eta$ then gives after one iteration
$$w_{ij}=\eta\sum_{n=1}^N x_i^{(n)}x_j^{(n)}\tag{43.12}$$
This is precisely the Hebb rule (eq. 16.5) used to train the Hopfield network (p. 523).

*Intuition note:* The model is pushed to reproduce the correlations seen in data. If the model already shows the same correlation, nothing changes. The Hebb rule is the first step from a model with no structure.

**Waking and sleeping.** Awake, the network measures real-world correlations and increases weights in proportion. Asleep, it "dreams" from model (43.4), measures model correlations, and decreases weights in proportion. If the dream correlations match the real ones, the weights do not change (pp. 523–524).

**Criticism.** So far all neurons are visible. The optimized model can capture the second-order statistics of the environment, the expected values $\langle x_ix_j\rangle$ of all pairwise products (p. 524).
- The real world, however, often has higher-order correlations that must be included if our description of it is to be effective. Often the second-order correlations in themselves may carry little or no useful information (p. 524).
- *Chairs.* A child easily separates chair images from carrots and parrots. MacKay expects the raw second-order statistics to be useless for describing chair images (p. 524).
- *Plain shifter ensemble* (Fig. 43.1a). The top 8 pixels are random. The bottom 8 are a copy shifted one pixel left, unshifted, or shifted one pixel right. The correlation between a pixel and any of the three pixels above it is $1/3$. Any other pixel pair has correlation zero. So second-order statistics convey no useful information (p. 524).
- *Labelled shifter ensemble* (Fig. 43.1b). Three extra label neurons mark "shift left", "no shift" or "shift right". The ensemble is still not learnable from second-order statistics alone: label–image correlations are zero (p. 524).

**Higher-order terms.** One could add them directly:
$$P'(\mathbf x|\mathbf W,\mathbf V,\dots)=\frac1{Z'}\exp\Big(\tfrac12\sum_{ij}w_{ij}x_ix_j+\tfrac16\sum_{ij}v_{ijk}x_ix_jx_k+\cdots\Big)\tag{43.13}$$
(the printed second sum is over "$ij$"; see Reading notes). Such machines are equally easy to simulate. The learning rule for $v_{ijk}$ is equivalent to that for $w_{ij}$ (Exercise 43.2 asks for the gradient) (p. 524). MacKay notes it is possible that the spines on biological neurons detect correlations between small numbers of incoming signals. However, describing chair images well would need an unimaginable number of terms. Fourth-order statistics alone in a $128\times128$ image need more than $10^7$ parameters (p. 525).

MacKay concludes that measuring moments is not a good way to describe underlying structure. Perhaps hidden (latent) variables are needed instead or in addition. This is the innovation of Hinton and Sejnowski (1986): hidden variables induce higher-order correlations among visible variables, while the model keeps only second-order interactions (p. 525).

### 43.2 Boltzmann machine with hidden units
Hidden neurons do not correspond to observed variables. They can play any role in the model and might take interpretable roles ("feature extraction"). The activity rule is unchanged (p. 525).

Notation: visible states $\mathbf x$, hidden states $\mathbf h$, generic state $\mathbf y\equiv(\mathbf x,\mathbf h)$. With visible units clamped to $\mathbf x^{(n)}$, the state is $\mathbf y^{(n)}=(\mathbf x^{(n)},\mathbf h)$. Learning is again by maximum likelihood, but the hidden states are unknown, so they are summed out (p. 525):
$$P(\mathbf x^{(n)}|\mathbf W)=\sum_{\mathbf h}P(\mathbf x^{(n)},\mathbf h|\mathbf W)=\sum_{\mathbf h}\frac1{Z(\mathbf W)}\exp\Big[\tfrac12[\mathbf y^{(n)}]^{\rm T}\mathbf W\mathbf y^{(n)}\Big]\tag{43.14}$$
$$Z(\mathbf W)=\sum_{\mathbf x,\mathbf h}\exp\Big[\tfrac12\mathbf y^{\rm T}\mathbf W\mathbf y\Big]\tag{43.15}$$
Equivalently $P(\mathbf x^{(n)}|\mathbf W)=Z_{\mathbf x^{(n)}}(\mathbf W)/Z(\mathbf W)$ (43.16), where $Z_{\mathbf x^{(n)}}(\mathbf W)=\sum_{\mathbf h}\exp[\tfrac12[\mathbf y^{(n)}]^{\rm T}\mathbf W\mathbf y^{(n)}]$ (43.17).

Differentiating "as before" gives again a waking minus a sleeping term (p. 525):
$$\frac{\partial}{\partial w_{ij}}\ln P(\{\mathbf x^{(n)}\}|\mathbf W)=\sum_n\Big\{\langle y_iy_j\rangle_{P(\mathbf h|\mathbf x^{(n)},\mathbf W)}-\langle y_iy_j\rangle_{P(\mathbf x,\mathbf h|\mathbf W)}\Big\}\tag{43.18}$$
*(added step)* From (43.16), $\ln P(\mathbf x^{(n)}|\mathbf W)=\ln Z_{\mathbf x^{(n)}}-\ln Z$. As in (43.7), the derivative of $\ln Z_{\mathbf x^{(n)}}$ is the correlation $\langle y_iy_j\rangle_{P(\mathbf h|\mathbf x^{(n)},\mathbf W)}$ (sum over hidden states only, visible units clamped), and the derivative of $\ln Z$ is the correlation over all states $(\mathbf x,\mathbf h)$. Subtracting and summing over $n$ gives (43.18).

- The first term is the correlation when the machine runs with visible units clamped to $\mathbf x^{(n)}$ and hidden units sampling freely from their conditional distribution.
- The second term is the correlation when the machine generates samples from its model distribution (p. 526).

*Intuition note:* Waking now means "fill in the hidden units given the data". Sleeping is still free dreaming. Hidden units can store the patterns that pairwise visible weights cannot.

Hinton and Sejnowski showed that non-trivial ensembles such as the labelled shifter ensemble can be learned this way. The hidden units act as feature detectors for patterns associated with one of the three shifts (p. 526).

The machine is time-consuming to simulate because the gradient is a difference of two Monte Carlo estimates. So Boltzmann machines are not in widespread use. Finding more efficient models with the same capabilities is an area of active research (p. 526).

### 43.3 Exercise
Exercise 43.3: can the "bars and stripes" ensemble (Fig. 43.2) be learned by a Boltzmann machine with no hidden units? MacKay says "You may be surprised!" (p. 526).

## Toy example (ours)
Two visible units, $x_1,x_2\in\{\pm1\}$, one weight $w=w_{12}=w_{21}$. We take the diagonal of $\mathbf W$ to be zero, so $\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x=wx_1x_2$.
- Model: $P(\mathbf x)=e^{wx_1x_2}/Z$ and $Z=2e^{w}+2e^{-w}$.
- Model correlation: $\langle x_1x_2\rangle=\dfrac{2e^w-2e^{-w}}{2e^w+2e^{-w}}=\tanh w$.
- Gibbs rule check: $P(x_1=+1|x_2=+1)=e^{w}/(e^{w}+e^{-w})=1/(1+e^{-2w})$, i.e. (43.3) with $a_1=wx_2$.
- Data, $N=4$: $(+,+),(-,-),(+,+),(+,-)$. Products: $1,1,1,-1$, so $\langle x_1x_2\rangle_{\rm Data}=2/4=0.5$.
- Gradient (43.9): $4[0.5-\tanh w]$.
- At $w=0$: $4\times0.5=2=\sum_n x_1^{(n)}x_2^{(n)}$. With $\eta=0.1$, $w=0.2$ after one step, which is the Hebb value (43.12).
- Next step: $\tanh0.2\approx0.197$, gradient $\approx4(0.303)=1.21$, so $w\approx0.2+0.121=0.321$.
- The gradient vanishes when $\tanh w=0.5$, i.e. $e^{2w}=3$, $w=\tfrac12\ln3\approx0.549$. There the model reproduces the data correlation.

## Concepts
- [[boltzmann-machine]] (new) — stochastic Hopfield network that samples from $\exp(\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x)/Z$ (p. 522)
- [[hopfield-network]] (new) — network minimizing energy $E(\mathbf x)=-\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x$ (p. 522)
- [[hebb-rule]] (new) — $w_{ij}\propto\sum_n x_i^{(n)}x_j^{(n)}$; equals one gradient step from $\mathbf W=0$ (p. 523)
- [[waking-sleeping-learning]] (new) — gradient = data correlation minus model correlation (pp. 523–524)
- [[hidden-units]] (new) — latent variables inducing higher-order visible correlations with pairwise weights (p. 525)
- [[second-order-statistics]] (new) — expected pairwise products $\langle x_ix_j\rangle$ of an ensemble (p. 524)
- [[maximum-likelihood-estimation]] (new) — choosing $\mathbf W$ to maximize the likelihood, dropping the prior $P(\mathbf W)$ (p. 523)
- [[gibbs-sampling]] — rule (43.3) is Gibbs sampling for (43.2) (p. 522)
- [[exponential-family-gibbs-distribution]] — $P\propto\exp(\tfrac12\mathbf x^{\rm T}\mathbf W\mathbf x)$ as an energy-based distribution (p. 522)
- [[monte-carlo-integration]] — model correlations estimated by averaging along simulation (p. 523)
- [[likelihood]] / [[bayes-theorem]] — posterior (43.5), of which only the likelihood is used (pp. 522–523)

## Canonical instances
- [[shifter-ensemble]] — plain and labelled; not learnable from second-order statistics alone (p. 524); Hinton and Sejnowski learned the labelled one with hidden units (p. 526)
- [[chair-images-ensemble]] — example where second-order pixel statistics are expected to be useless (p. 524)
- [[bars-and-stripes-ensemble]] — exercise on learnability without hidden units (p. 526)

## Bridges (candidates)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition.
- [same-math] Gibbs sampling activity rule ↔ bayesian: Gibbs sampling MCMC, updating one variable from its conditional distribution.
- [structural-analogy] Hidden units inducing higher-order visible correlations ↔ bayesian: latent-variable and hierarchical models explaining dependence among observables.
- [metaphor] Waking/sleeping phases ↔ cognition: learning by comparing perception with internal "dreaming" of the model.

## Questions this raises
- How do the hidden units' conditional samples $P(\mathbf h|\mathbf x^{(n)},\mathbf W)$ get computed in practice, and how long must the chains run?
- When does adding hidden units fully remove the need for explicit higher-order terms?
- What would a full Bayesian treatment of $P(\mathbf W|\text{data})$ add over maximum likelihood?
- Which more efficient models keep the same capabilities (the references on p. 526)?

## Exercises worth doing
- Ex. 43.1 (p. 523) — derive $\partial\ln Z/\partial w_{ij}$ as a model correlation; the key step behind all later gradients — difficulty: medium
- Ex. 43.2 (p. 525) — gradient for third-order weights $v_{ijk}$; shows it has the same waking/sleeping form — difficulty: medium
- Ex. 43.3 (p. 526) — can a Boltzmann machine without hidden units learn bars and stripes? — difficulty: hard

## Reading notes
- Printed pages 522–526 are pdf 534–538 (printed = pdf − 12).
- The activation $a_i$ in (43.3) refers to eq. 42.3, which is not in this unit. Eq. 16.5 (Hebb rule) and Exercise 22.12 are also referenced but not shown.
- Eq. (43.13) as printed has the cubic sum written over "$ij$" although it has indices $i,j,k$; I read this as a typographical slip (the $1/6$ factor suggests a sum over all three indices).
- The text says the model correlation at $\mathbf W=0$ is zero "by symmetry". (Our observation, not the author's:) the symmetry argument is clear for $i\ne j$; for $i=j$, $x_i^2=1$, so the model correlation is $1$, not $0$, and that case is not covered by the argument.
- The derivation of (43.18) is not shown in the text ("differentiating... as before"); the justification above is marked as an added step.
- Page images show Fig. 43.1 and Fig. 43.2 as small bitmaps; only their captions are used.

---
id: variational-inference-elbo
type: concept
fields: [bayesian, information-theory]
n_sources: 26
tiers: [reference, core]
grounding: digests
sources: [blei-2017-variational/main-p1, blei-2017-variational/main-p2, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch22-finite, gelman-2020-workflow/main-p1, mackay-2003-information/ch33-variational, mackay-2003-information/ch42-hopfield, mackay-2003-information/ch45-gaussian, murphy-2023-pml2/ch05-information-p2, murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch08-gaussian-p2, murphy-2023-pml2/ch10-variational-p1, murphy-2023-pml2/ch10-variational-p2, murphy-2023-pml2/ch11-monte, murphy-2023-pml2/ch14-predictive, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch19-beyond, murphy-2023-pml2/ch21-variational, murphy-2023-pml2/ch25-diffusion, murphy-2023-pml2/ch28-latent-p1, murphy-2023-pml2/ch28-latent-p2, murphy-2023-pml2/ch29-state-p3, murphy-2023-pml2/ch32-representation]
raw_ids: ["Variational inference & ELBO"]
canon_spine: bayesian
generated_by: build_kg.py
---

# variational-inference-elbo

## Canon spine entry

- **Variational inference & ELBO** (bayesian): approximate the posterior by optimizing a simpler distribution to maximize a lower bound on log evidence (grad)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 2, 6): approximate the posterior by optimizing a member of a family $\mathcal Q$ to minimize KL(q‖p(z|x)), equivalently maximize the ELBO
- [[blei-2017-variational/main-p2]] (p. 22): approximate $p(z\mid x)$ by optimizing a family member to be KL-closest; the ELBO is the objective
- [[gelman-2013-bda3/ch13-modal]] (pp. 331, 336): fit factorised $g$ by minimising $\mathrm{KL}(g\|p)$, equivalently raising the variational lower bound $\mathrm E_g\log(p(\theta,y)/g)$
- [[gelman-2013-bda3/ch22-finite]] (p. 524; ELBO not stated in this unit): variational Bayes also approximates marginals while averaging over indicators
- [[gelman-2020-workflow/main-p1]] (pp. 13, 15): fast, possibly inaccurate posterior approximation; also used as a mode-finding approximation
- [[murphy-2023-pml2/ch05-information-p2]] (p. 249): the rate–distortion Lagrangian $D+\beta R$ at $\beta=1$ is the negative of the VAE ELBO, $\mathcal L=-(D+R)$
- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 277): the ELBO as the stochastic objective in STL
- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 290): $\mathcal L(\theta,\{q_n\}|\mathcal D)$ from Jensen; lower bound on the log evidence [as `Variational inference & ELBO`]
- [[murphy-2023-pml2/ch07-inference]] (pp. 352–353): fit tractable $q$ by minimising KL to the posterior, i.e. maximising Ł
- [[murphy-2023-pml2/ch08-gaussian-p2]] (p. 399): globally minimizes exclusive KL with a tractable bound
- [[murphy-2023-pml2/ch10-variational-p1]] (pp. 439–441): approximate the posterior by maximizing the ELBO over a family $q_\psi$
- [[murphy-2023-pml2/ch10-variational-p2]] (p. 456): maximising a lower bound on $\log p(x)$ over a family $q$; this part gives ways to optimise and improve it
- [[murphy-2023-pml2/ch11-monte]] (p. 492): ELBO optimization can learn a good IS proposal
- [[murphy-2023-pml2/ch14-predictive]] (p. 577): minimize NLL-expectation plus KL over a restricted family $\mathcal Q$
- [[murphy-2023-pml2/ch17-bayesian]] (p. 653): fixed-form Gaussian $q$ minimizing $D_{KL}(q\|p)$; Bayes by backprop
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 712): SVGP maximises $\mathbb E_{q(f_X)}[\log p(y|f_X)]-D_{\rm KL}(q(f_Z)\|p(f_Z))$
- [[murphy-2023-pml2/ch19-beyond]] (p. 757): standard objective (19.33) contrasted with meta-learning (19.32)
- [[murphy-2023-pml2/ch21-variational]] (p. 796): the VAE objective: expected log-likelihood minus a KL to the prior; data-averaged forms in (21.16–21.22)
- [[murphy-2023-pml2/ch25-diffusion]] (p. 870): here the ELBO splits into $L_T$, $L_{t-1}$, $L_0$
- [[murphy-2023-pml2/ch28-latent-p1]] (p. 949, p. 957): used for ARD in MFA and for non-degenerate posteriors in expfam FA
- [[murphy-2023-pml2/ch28-latent-p2]] (p. 963, 966–967, 969): variational EM and mean field are used to fit mPCA, LDA, CTM, DTM
- [[murphy-2023-pml2/ch29-state-p3]] (p. 1038): ELBO used to train deep SSMs
- [[murphy-2023-pml2/ch32-representation]] (pp. 1060, 1071): only mentioned: VAEs train latent-variable models with variational inference, and VIB uses variational MI bounds

### information-theory

- [[mackay-2003-information/ch33-variational]] (p. 429): approximate posterior by Q(w;θ) minimizing F̃ ≥ −ln P(D|H); the author's names are ensemble learning and variational Bayes
- [[mackay-2003-information/ch42-hopfield]] (p. 508): here the Hopfield activity rule equals mean-field minimization of variational free energy
- [[mackay-2003-information/ch45-gaussian]] (p. 547): bounds on the unnormalized posterior for GP classification, not an ELBO as such

## Candidate bridges

- [same-math] VAE ELBO $=-(D+R)$ ↔ bayesian: variational inference ELBO — the author shows the objectives coincide at $\beta=1$ (p. 249). — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)

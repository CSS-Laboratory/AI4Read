---
id: elbo
type: concept
fields: [llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [prince-2023-udl/ch17-variational, prince-2023-udl/ch18-diffusion]
generated_by: build_kg.py
---

# elbo

## Definitions in the sources

### llm

- [[prince-2023-udl/ch17-variational]] (p. 333): lower bound on log Pr(x|ϕ) from Jensen's inequality; equals log-likelihood minus KL to the posterior [new]
- [[prince-2023-udl/ch18-diffusion]] (p. 358): lower bound on log-likelihood; here it needs no encoder parameters [new]

## Instances that use it

- [[bayesian-gaussian-mixture]] — unit-variance mixture with Gaussian prior on means; full CAVI derivation and ELBO — from [[blei-2017-variational/main-p1]]
- [[variational-autoencoder]] — ELBO with a Gaussian recognition model — from [[polyanskiy-2025-information/ch05-variational]]

## Candidate bridges

- [same-math] ELBO maximization ↔ bayesian: the Bayesian posterior as the optimum of "expected log likelihood − KL to prior" — Eq. (13) rewrites exactly as this balance — from [[blei-2017-variational/main-p1]] (bayesian → bayesian)
- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26). — from [[blei-2017-variational/main-p2]] (bayesian → other)
- [same-math] VB lower bound $\mathrm E_g\log(p(\theta,y)/g)$ ↔ bayesian canon, variational inference and ELBO — same objective, up to the constant $\log p(y)$. — from [[gelman-2013-bda3/ch13-modal]] (bayesian → unspecified)
- [same-math] variational free energy F̃ = D_KL(Q‖P) + F ↔ bayesian: ELBO, since F̃ = −ln P(D|H) + D_KL(Q‖posterior) is minus the lower bound on log evidence. — from [[mackay-2003-information/ch33-variational]] (information-theory → bayesian)
- [same-math] Reverse-KL/I-projection ↔ variational inference in Bayesian inference (canon: KL divergence & ELBO; not developed in this unit): the KL being minimized is $D_{KL}(q\|p)$. — from [[murphy-2023-pml2/ch05-information-p1]] (bayesian → bayesian)
- [same-math] VAE ELBO $=-(D+R)$ ↔ bayesian: variational inference ELBO — the author shows the objectives coincide at $\beta=1$ (p. 249). — from [[murphy-2023-pml2/ch05-information-p2]] (bayesian → bayesian)
- [same-math] Reparameterization gradient ↔ variational inference: the pathwise ELBO gradient used in stochastic VI (p. 275) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → other)
- [same-math] EM's ELBO (6.140–6.145) ↔ Bayesian inference: variational ELBO and KL to the posterior — the text itself says this bound is the basis of variational inference. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → bayesian)
- [structural-analogy] ELBO maximisation ↔ MCMC: both avoid $p(\mathcal D)$, one by a constant offset and one by density ratios — they differ in mechanism. — from [[murphy-2023-pml2/ch07-inference]] (bayesian → other)
- [structural-analogy] ELBO = expected energy − entropy ↔ statistical physics: free energy = energy − entropy — the text itself names the VFE (p. 440). — from [[murphy-2023-pml2/ch10-variational-p1]] (bayesian → complex-systems)
- [same-math] SVGP ELBO (18.142) ↔ bayesian: ELBO = expected log-likelihood minus KL from approximate posterior to prior, here with $q(f)=p(f_*,f_X|f_Z)q(f_Z)$. — from [[murphy-2023-pml2/ch18-gaussian-p2]] (bayesian → bayesian)
- [structural-analogy] IAF vs MAF speed swap ↔ ELBO vs MLE needs: fast sampling-plus-density versus fast arbitrary-point density. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other)
- [same-math] DDPM ELBO (§25.2.3) ↔ Bayesian: ELBO and KL from variational inference with a fixed (non-learned) variational posterior $q(x_{1:T}|x_0)$. — from [[murphy-2023-pml2/ch25-diffusion]] (bayesian → bayesian)
- [same-math] DMM/RSSM ELBO (29.171) ↔ variational inference: standard ELBO with reconstruction and KL terms. — from [[murphy-2023-pml2/ch29-state-p3]] (bayesian → other)
- [structural-analogy] ELBO gap equals KL to posterior ↔ llm (cross-entropy / log-loss): both are likelihood-based training objectives, here approximated by a bound. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] KL term in ELBO ↔ llm (KL penalty): the same KL divergence between two distributions, though used for a different purpose. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
- [same-math] Diffusion ELBO ↔ VAE: the Jensen lower bound with a reconstruction term and KL terms is the same derivation as in chapter 17, with a fixed encoder. — from [[prince-2023-udl/ch18-diffusion]] (llm → other)

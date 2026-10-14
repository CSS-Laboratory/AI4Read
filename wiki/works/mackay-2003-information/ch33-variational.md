---
id: mackay-2003-information/ch33-variational
work: mackay-2003-information
unit: 33 Variational Methods
pages: 422-436
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Variational Methods (MacKay, ch. 33)

## L0 — One line
Approximate an intractable distribution P by a simpler Q(θ) chosen to minimize the variational free energy, which equals D_KL(Q‖P) plus a constant, so that F̃ is also a bound on the true free energy (or on minus the log evidence).

## L1 — The gist (≤ 120 words)
Complicated distributions, such as Boltzmann distributions of spin systems or Bayesian posteriors, involve sums that are intractable to evaluate. The chapter approximates P by a simpler Q(x;θ). It chooses θ to minimize the variational free energy, which is D_KL(Q‖P) plus a constant (−ln Z, or −ln of the evidence P(D|H), the probability of the data given the model). F̃ is therefore a bound on that constant. The same recipe gives mean field theory, a variational posterior for an unknown Gaussian, and soft K-means as an EM (expectation–maximization: alternating assignment and update steps) algorithm. The author says the resulting approximations tend to be more compact than the true distribution. For simple enough Q, F̃ can be evaluated efficiently, so the hard sums are replaced by an optimization over θ.

**Prerequisites:** relative entropy and Gibbs' inequality; Boltzmann distribution and partition function; Gaussian and gamma densities; partial derivatives; Bayes' theorem; soft K-means (Ch. 20/22).

## L2 — Key ideas
- **Free energy = KL + constant.** βF̃(θ) = D_KL(Q‖P) + βF, so F̃ ≥ F with equality only at Q = P. Minimizing F̃ gives the Q closest to P in the D_KL(Q‖P) sense within the chosen family, and a lower bound Z̃ ≤ Z. (p. 423)
- **Separable Q on spins gives the mean field equations** a_m = β(Σ_n J_mn x̄_n + h_m), x̄_n = tanh(a_n). The variational view supplies an objective function behind them and allows richer Q. (pp. 425–426)
- **Mean field for the Ising model** shows symmetry breaking below T_c^mft = 4. But it overestimates the true T_c = 2.27, behaves the same in every dimension, and, having uncorrelated spins, lacks the large energy fluctuations that the real system shows near the critical temperature. (pp. 426–427)
- **Variational Bayes / ensemble learning** approximates the whole posterior P(w|D,H) by Q(w;θ). F̃ is bounded below by −ln P(D|H). (pp. 427–429)
- **Unknown Gaussian:** with Q = Q_µ Q_σ, alternating updates give a Gaussian for µ and a gamma for β. The mean of β agrees with that of the true posterior, 1/β̄ = S/(N−1) (S is a data statistic from Ch. 24), but c′ is too large by 1/2. (pp. 429–431)
- **Compactness:** author states that variational approximations always tend to be more compact than the true distribution. Exercise 33.5 shows it for Gaussians: variational minimization typically gives σ_Q matching the shortest length scale. (pp. 431, 435)
- **EM / soft K-means** is the variational recipe with Q_k for labels and a delta function for Q_θ. (pp. 432–433)
- **Other variational methods:** Jaakkola–Jordan upper and lower bounds; Bethe/Kikuchi free energies as further reading. (pp. 433–434)

## L3 — Walkthrough

### 33.1 Variational free energy minimization (pp. 422–424)
Mean field theory is a special case of the variational free energy approach of Feynman and Bogoliubov (p. 422). Relative entropy (defined over the same alphabet):
$$D_{KL}(Q\|P)=\sum_x Q(x)\ln\frac{Q(x)}{P(x)}\tag{33.1}$$
Gibbs' inequality: $D_{KL}(Q\|P)\ge 0$ with equality only if $Q=P$. In general $D_{KL}(Q\|P)\ne D_{KL}(P\|Q)$. Logs are natural, so the unit is nats (p. 422).

Statistical physics supplies distributions of this form (pp. 422–423):
$$P(\mathbf x|\beta,\mathbf J)=\frac{1}{Z(\beta,\mathbf J)}\exp[-\beta E(\mathbf x;\mathbf J)]\tag{33.2}$$
$$E(\mathbf x;\mathbf J)=-\tfrac12\sum_{m,n}J_{mn}x_mx_n-\sum_n h_nx_n,\quad \mathbf x\in\{-1,+1\}^N\tag{33.3}$$
$$Z(\beta,\mathbf J)\equiv\sum_{\mathbf x}\exp[-\beta E(\mathbf x;\mathbf J)]\tag{33.4}$$
Evaluating E for one x takes polynomial time in the number of spins. Evaluating Z is hard (Ch. 29). Values of E at a few points tell nothing about average properties. Z would give all thermodynamic properties (p. 423).

The method approximates P by a simpler ensemble Q(x;θ) with adjustable parameters θ. A by-product is a lower bound on Z. The objective is the variational free energy (p. 423):
$$\beta\tilde F(\theta)=\sum_x Q(x;\theta)\ln\frac{Q(x;\theta)}{\exp[-\beta E(x;J)]}\tag{33.5}$$
First form:
$$\beta\tilde F=\beta\sum_x Q\,E-\sum_x Q\ln\frac1Q\tag{33.6}$$
$$\equiv\beta\langle E\rangle_Q-S_Q\tag{33.7}$$
$S_Q$ is the entropy of Q, with $k_B=1$. Second form, using the definition of P:
$$\beta\tilde F=\sum_xQ\ln\frac{Q}{P(x|\beta,J)}-\ln Z\tag{33.8}$$
$$=D_{KL}(Q\|P)+\beta F,\qquad \beta F\equiv-\ln Z\tag{33.9, 33.10}$$
By Gibbs' inequality, F̃ ≥ F, with equality only for Q = P. Minimizing βF̃ gives a simplified Q, and βF̃ is an upper bound on βF. Equivalently $\tilde Z\equiv e^{-\beta\tilde F}$ is a lower bound on Z (p. 423).

Can F̃ be evaluated? ⟨E⟩_P (33.12), S (33.13) and Z (33.11) are presumed impossible to evaluate. But for a range of energy functions and sufficiently simple Q, F̃ can be evaluated efficiently (p. 424).

*Intuition note:* βF̃ differs from βF by exactly a KL divergence. So making F̃ small makes Q close to P in the KL(Q‖P) sense. The bound comes free.

### 33.2 Spin systems (pp. 424–426)
Take a separable Q with one parameter per spin (p. 424):
$$Q(\mathbf x;\mathbf a)=\frac1{Z_Q}\exp\Big(\sum_n a_nx_n\Big)\tag{33.14}$$
Spins are independent, so the entropy is a sum (exercise 4.2):
$$S_Q=\sum_n H_2^{(e)}(q_n)\tag{33.17}$$
$$q_n=\frac{e^{a_n}}{e^{a_n}+e^{-a_n}}=\frac1{1+\exp(-2a_n)}\tag{33.18}$$
$$H_2^{(e)}(q)=q\ln\frac1q+(1-q)\ln\frac1{1-q}\tag{33.19}$$
The mean energy is easy because each term $J_{mn}x_mx_n$ is a product of two independent variables. There are no self-couplings: $J_{mn}=0$ when $m=n$. With mean spin
$$\bar x_n=\frac{e^{a_n}-e^{-a_n}}{e^{a_n}+e^{-a_n}}=\tanh(a_n)=2q_n-1\tag{33.20}$$
we get (p. 425)
$$\langle E\rangle_Q=-\tfrac12\sum_{m,n}J_{mn}\bar x_m\bar x_n-\sum_nh_n\bar x_n\tag{33.22}$$
$$\beta\tilde F(\mathbf a)=\beta\Big(-\tfrac12\sum_{m,n}J_{mn}\bar x_m\bar x_n-\sum_nh_n\bar x_n\Big)-\sum_nH_2^{(e)}(q_n)\tag{33.23}$$
Derivative of the entropy, for $q=1/(1+e^{-2a})$:
$$\frac{\partial}{\partial q}H_2^{(e)}(q)=\ln\frac{1-q}{q}=-2a\tag{33.24}$$
Therefore
$$\frac{\partial}{\partial a_m}\beta\tilde F=\beta\Big[-\sum_nJ_{mn}\bar x_n-h_m\Big]\Big(2\frac{\partial q_m}{\partial a_m}\Big)-\ln\Big(\frac{1-q_m}{q_m}\Big)\frac{\partial q_m}{\partial a_m}$$
$$=2\frac{\partial q_m}{\partial a_m}\Big[-\beta\Big(\sum_nJ_{mn}\bar x_n+h_m\Big)+a_m\Big]\tag{33.25}$$
This is zero when
$$a_m=\beta\Big(\sum_nJ_{mn}\bar x_n+h_m\Big),\qquad \bar x_n=\tanh(a_n)\tag{33.26, 33.27}$$
F̃(a) may be multimodal. Every stationary point (maximum, minimum or saddle) satisfies these equations. Updating one $a_m$ (and $\bar x_m$) at a time with (33.26) is guaranteed to decrease βF̃ (p. 425). Figure 33.1 shows the two-spin system E = −x₁x₂ at β = 1.44. For fixed q₂ the function is convex in q₁, and vice versa (p. 425).

These are the mean field equations. $a_n$ is a fictitious field on an isolated spin n. (33.27) is its mean response. (33.26) sets the field from the mean state of the other spins (p. 425). The variational view helps for two reasons (pp. 425–426):
1. It attaches an objective function to the mean field equations. This can help identify other dynamical systems that minimize the same function.
2. It generalizes to other Q, for example Q with spin correlations. More freedom in Q tightens the bound, but the mean energy or entropy typically becomes harder to evaluate.

*Intuition note:* Each spin's field is set from the mean state of the other spins, not their fluctuating states. Updating one parameter at a time with that rule is guaranteed to decrease βF̃ (p. 425).

### 33.3 Ferromagnetic Ising model (pp. 426–427)
Every coupling $J_{mn}=J$ for neighbours, zero otherwise, and $h_n=h$. Use one parameter a in Q (33.28), with $q=1/(1+e^{-2a})$ (33.29), $\bar x=\tanh a$ (33.30), and
$$a=\beta(CJ\bar x+h)\tag{33.31}$$
where C is the number of couplings per spin (C = 4 in the 2-D rectangular case). Solve numerically; it is easiest to vary x̄ and solve for β (p. 426). Figure 33.2 uses C = 4, J = 1.

- **h = 0:** a pitchfork bifurcation occurs at the critical temperature $T_c^{mft}=4$. Above it there is one minimum at a = 0, x̄ = 0 (a uniform Q). Below it there are two symmetry-broken minima (spins mostly up, or mostly down). x̄ = 0 stays stationary but becomes a local maximum (p. 427).
- **h > 0:** there is a global minimum at positive x̄ at any temperature. If h < JC and T is small enough, a second local minimum (magnetization opposite to the field) appears together with a saddle point. This is a saddle-node bifurcation. It appears at a temperature below $T_c^{mft}$ (p. 427).

Per spin (p. 427):
$$\beta\tilde F=\beta\Big(-\frac C2J\bar x^2-h\bar x\Big)-H_2^{(e)}\Big(\frac{\bar x+1}{2}\Big)\tag{33.32}$$
Inadequacies (p. 427):
- $T_c^{mft}=4$ is nearly twice the true $T_c=2.27$.
- The variational model behaves the same in any dimension, including d = 1, where the true system has no phase transition. So the bifurcation should not be called a phase transition.
- Against a real 8×8 system (Fig. 33.3), a big difference is in the energy fluctuations. The real system has large fluctuations near criticality. Q has uncorrelated spins, so its energy variance scales linearly with the number of spins. Fig. 33.3 also shows F̃ lying above the true free energy (p. 428).

### 33.4 Variational methods in inference (pp. 427–429)
Posterior (33.33): $P(\mathbf w|D,\mathcal H)=P(D|\mathbf w,\mathcal H)P(\mathbf w|\mathcal H)/P(D|\mathcal H)$. Traditional fitting optimizes one w, the mode. The variational approach optimizes Q(w;θ) over the whole distribution (p. 429):
$$\tilde F(\theta)=\int d^k\mathbf w\,Q(\mathbf w;\theta)\ln\frac{Q(\mathbf w;\theta)}{P(D|\mathbf w,\mathcal H)P(\mathbf w|\mathcal H)}\tag{33.34}$$
F̃ is $-\ln P(D|\mathcal H)$ plus $D_{KL}(Q\|P(\mathbf w|D,\mathcal H))$. So it is bounded below by $-\ln P(D|\mathcal H)$, attained only at Q = posterior (p. 429). The method is also called ensemble learning or variational Bayes (p. 429).

### 33.5 Unknown Gaussian (pp. 429–431)
Posterior studied in Ch. 24 (S is not defined on these pages):
$$P(\mu,\sigma|\{x_n\})=\frac{\frac1{(2\pi\sigma^2)^{N/2}}\exp\!\big(-\frac{N(\mu-\bar x)^2+S}{2\sigma^2}\big)\frac1{\sigma_\mu}\frac1\sigma}{P(\{x_n\})}\tag{33.36}$$
Single assumption: $Q(\mu,\sigma)=Q_\mu(\mu)Q_\sigma(\sigma)$, with no restriction on the functional forms. Free energy (33.37) is $\int d\mu\,d\sigma\,Q_\mu Q_\sigma\ln\frac{Q_\mu Q_\sigma}{P(D|\mu,\sigma)P(\mu,\sigma)}$. Optimize $Q_\mu$ for fixed $Q_\sigma$, then the reverse (p. 429).

**Optimizing $Q_\mu$ (p. 430).** With $\beta\equiv1/\sigma^2$ and constants κ, κ′:
$$\tilde F=-\int d\mu\,Q_\mu\Big[\int d\sigma\,Q_\sigma\ln P(D|\mu,\sigma)+\ln\frac{P(\mu)}{Q_\mu}\Big]+\kappa\tag{33.38}$$
$$=\int d\mu\,Q_\mu\Big[\int d\sigma\,Q_\sigma\,N\beta\tfrac12(\mu-\bar x)^2+\ln Q_\mu\Big]+\kappa'\tag{33.39}$$
The dependence on $Q_\sigma$ collapses to the mean $\bar\beta\equiv\int d\sigma\,Q_\sigma\,\sigma^{-2}$ (33.40). The term $-N\bar\beta\tfrac12(\mu-\bar x)^2$ is the log of the posterior Gaussian at β = β̄. Since $\int Q\ln(Q/P)$ is minimized at Q = P:
$$Q_\mu^{opt}(\mu)=P(\mu|D,\bar\beta,\mathcal H)=\mathrm{Normal}(\mu;\bar x,\sigma^2_{\mu|D}),\quad \sigma^2_{\mu|D}=\frac1{N\bar\beta}\tag{33.41}$$

**Optimizing $Q_\sigma$ (pp. 430–431).** Use the density over β; the prior $P(\sigma)\propto1/\sigma$ becomes $P(\beta)\propto1/\beta$. With $Q_\mu=Q_\mu^{opt}$ (additive constants dropped):
$$\tilde F=-\int d\beta\,Q_\sigma(\beta)\Big[\int d\mu\,Q_\mu\ln P(D|\mu,\sigma)+\ln\frac{P(\beta)}{Q_\sigma(\beta)}\Big]\tag{33.42}$$
$$=\int d\beta\,Q_\sigma(\beta)\Big[(N\sigma^2_{\mu|D}+S)\beta/2-\big(\tfrac N2-1\big)\ln\beta+\ln Q_\sigma(\beta)\Big]\tag{33.43}$$
The β-dependent bracket is the log of a gamma distribution (eq. 23.15), so
$$Q^{opt}_\sigma(\beta)=\Gamma(\beta;b',c'),\quad \frac1{b'}=\tfrac12(N\sigma^2_{\mu|D}+S),\quad c'=\frac N2\tag{33.44, 33.45}$$
Applying (33.41) and (33.44) alternately converges in a few iterations (Fig. 33.4: 15 iterations; peaks at σ_N = 0.45 for P and σ_{N−1} = 0.5 for Q) (pp. 430–431).

**Direct solution (p. 431).** Both conditions must hold: $\sigma^2_{\mu|D}=1/(N\bar\beta)$ and $\bar\beta=b'c'$. The solution is
$$1/\bar\beta=S/(N-1)\tag{33.46}$$
*(added step: $\bar\beta=b'c'=\dfrac{N}{1/\bar\beta+S}$, so $1+\bar\beta S=N$.)* The true posterior over β is a gamma with $c'=(N-1)/2$ and $1/b'=S/2$ (eq. 24.13). It has the same mean value of β, with $1/\bar\beta=S/(N-1)$. The approximating $c'$ is too large by 1/2 (p. 431).

Author's boxed claim: "The approximations given by variational free energy minimization always tend to be more compact than the true distribution." (p. 431)

Conclusion (p. 431): the approximate posterior over β is a gamma with mean β̄ corresponding to $\sigma^2=S/(N-1)=\sigma^2_{N-1}$. The approximate posterior over µ is Gaussian with mean x̄ and standard deviation $\sigma_{N-1}/\sqrt N$. The approach is parameterization-independent, so it avoids the basis-dependence of MAP and Laplace's method. VIBES automates variational inference as BUGS does for Monte Carlo (p. 431).

*Intuition note:* Each factor of Q is optimal for its own variable with the other factor held fixed, and depends on the other factor only through an average (β̄ or σ²_{µ|D}). A separable Q cannot represent any µ–σ correlation. The author notes that the resulting c′ is too large by 1/2 (p. 431).

### 33.6 Interlude (pp. 431–432)
**A student asks** how to find a useful Q when P is too complex to compute. The author's answer: standard practice picks one best-fit x* (a likelihood or posterior maximum). That is a delta-function approximation to P(x|D). So any Q(x;θ), "no matter how crummy", is an improvement on the spike, and even a simple Gaussian does well (p. 432).

### 33.7 K-means and EM as a variational method (pp. 432–433)
Soft K-means (Ch. 20, 22) is an EM algorithm. Its "assignment" and "update" steps are the E-step and M-step. Neal and Hinton's view shows that soft K-means optimizes a variational objective; their derivation applies to any EM algorithm (p. 432).

θ are the mixture parameters (means, standard deviations, weights). The class labels $k_n$ are latent variables. Probability of everything (p. 432):
$$P(\{\mathbf x^{(n)},k_n\},\theta|\mathcal H)=P(\theta|\mathcal H)\prod_{n=1}^N\big[P(\mathbf x^{(n)}|k_n,\theta)P(k_n|\theta)\big]\tag{33.47}$$
The posterior (33.48) is this divided by $P(\{\mathbf x^{(n)}\}|\mathcal H)$. Approximate it by $Q_k(\{k_n\})Q_\theta(\theta)$ (33.49), with
$$\tilde F(Q_k,Q_\theta)=\sum_{\{k_n\}}\int d^D\theta\,Q_kQ_\theta\ln\frac{Q_kQ_\theta}{P(\{\mathbf x^{(n)},k_n\},\theta|\mathcal H)}\tag{33.50}$$
F̃ is bounded below by minus the log evidence, $-\ln P(\{\mathbf x^{(n)}\}|\mathcal H)$ (the printed sentence writes "minus the evidence, ln P(…)"). Assignment step: adjust $Q_k$ for fixed $Q_\theta$. Update step: adjust $Q_\theta$ for fixed $Q_k$ (p. 432).

Exactly soft K-means needs the further constraint $Q_\theta(\theta)=\delta(\theta-\theta^*)$ (33.51). This adds an infinite term $\int Q_\theta\ln Q_\theta$ to F̃, which is left out as a constant. The author warns that a delta-function Q is not a good idea if the aim is to minimize F̃ (p. 433).

Exercises 33.2–33.4 (p. 433) ask for the optimal $Q_k$ (the responsibilities), the optimal θ* (the K-means update step), and a generalization with a separable $Q_\theta$. The author adds that this removes the "kaboom" problem, but other artefacts can arise, involving local minima of F̃ (p. 433).

### 33.8 Other variational methods (pp. 433–434)
Jaakkola and Jordan build adjustable unnormalized upper and lower bounds $Q^U$, $Q^L$ on P. Their variational parameters are tuned to maximize $\sum_xQ^L(x)$ (33.52) and to minimize $\sum_xQ^U(x)$ (33.53). Normalized versions of the optimized bounds give approximate predictive distributions (pp. 433–434). Fig. 33.5 gives bounds on the logistic function $g(a)=1/(1+e^{-a})$ that are exponential or Gaussian in a (so easier to integrate):
$$g(a)\le\exp(\mu a-H_2^{e}(\mu)),\quad\mu\in[0,1]$$
$$g(a)\ge g(\nu)\exp\big[(a-\nu)/2-\lambda(\nu)(a^2-\nu^2)\big],\quad \lambda(\nu)=\frac{g(\nu)-1/2}{2\nu}$$
The figure uses µ = 0.505 and ν = −2.015 (p. 433).

**Further reading (p. 434).** The sum–product algorithm on a tree-like factor graph computes marginals correctly. On other graphs, if it converges, the fixed point is a stationary point (usually a minimum) of the Kikuchi free energy. If all factors involve one or two variables, this is the Bethe free energy.

### 33.9–33.10 Further exercises and solutions (pp. 434–436)
**Exercise 33.5 (results only).** The relative entropy of two 1-D zero-mean Gaussians is
$$\int dx\,\mathrm{Normal}(x;0,\sigma_Q)\ln\frac{\mathrm{Normal}(x;0,\sigma_Q)}{\mathrm{Normal}(x;0,\sigma_P)}=\frac12\Big(\ln\frac{\sigma_P^2}{\sigma_Q^2}-1+\frac{\sigma_Q^2}{\sigma_P^2}\Big)\tag{33.56}$$
- Approximating a 2-D Gaussian P (variances σ₁², σ₂² along two axes) by a spherical Q with variance σ_Q², minimizing F̃ gives $1/\sigma_Q^2=\tfrac12(1/\sigma_1^2+1/\sigma_2^2)$ (33.59).
- Minimizing $G=\int P\ln(P/Q)$ gives $\sigma_Q^2=\tfrac12(\sigma_1^2+\sigma_2^2)$ (33.62).
- For σ₁ = 10, σ₂ = 1: F̃ gives σ_Q ≃ √2, a factor √2 above σ₂ and almost independent of σ₁. G gives σ_Q ≃ 10/√2, a factor √2 below σ₁. Variational minimization typically matches the shortest length scale, so Q "might be viewed as too compact" (p. 435). Fig. 33.6 draws both fits (p. 436).

**Exercise 33.6 (author's solution).** The best variational Q is P itself. Failing that, a good variational Q is more compact than P. A good sampler is more heavy-tailed than P, and an over-compact distribution would be a lousy sampler with large variance (p. 436).

**Exercise 33.7 (p. 435)** asks for the proof that G(Q_X,Q_Y) is minimized at the marginals. It then asks for F(Q_X,Q_Y) = Σ Q_XQ_Y log₂(Q_XQ_Y/P) at the marginals, for the 4×4 table P(x,y), and for its three distinct minima.

## Toy example (ours, not from the text)
Two spins, E(x) = −x₁x₂, no field, β = 2. This is the Fig. 33.1 system at a different β.

**Exact.** The states ++ and −− have E = −1. The states +− and −+ have E = +1.
Z = 2e² + 2e⁻² = 2(7.38906 + 0.13534) = 15.0488.
βF = −ln Z = −2.7113.
Exact P: ++ and −− have 0.491 each, +− and −+ have 0.0090 each. By symmetry x̄ = 0.

**Variational.** Q is separable with q₁ = q₂ = q and x̄ = 2q − 1. From (33.23) with J₁₂ = J₂₁ = 1:
βF̃ = −β x̄² − 2H(q) = −2x̄² − 2H(q), in nats.

| x̄ | q | H(q) | βF̃ |
|---|---|---|---|
| 0 | 0.5 | ln 2 = 0.6931 | −0 − 1.3863 = −1.3863 |
| 0.8 | 0.9 | 0.9(0.10536) + 0.1(2.30259) = 0.3251 | −1.28 − 0.6502 = −1.9302 |
| 0.9 | 0.95 | 0.95(0.05129) + 0.05(2.99573) = 0.1985 | −1.62 − 0.3970 = −2.0170 |
| 0.96 | 0.98 | 0.98(0.02020) + 0.02(3.91202) = 0.0980 | −1.8432 − 0.1961 = −2.0393 |

- Every row is ≥ −2.7113, as the bound requires.
- The stationarity condition (33.26) gives a = 2x̄ (since βJ = 2) and x̄ = tanh(a). That is x̄ = tanh(2x̄), with a solution near x̄ ≈ 0.96. This matches the minimum of the table, about −2.04.
- Check of (33.9) at x̄ = 0: βF̃ − βF = −1.3863 + 2.7113 = 1.325. Direct computation: D_KL(uniform‖P) = ½ln(0.25/0.491) + ½ln(0.25/0.00899) = ½(−0.6750) + ½(3.3253) ≈ 1.325 ✓.
- The best Q (gap ≈ 0.67 nats) breaks symmetry (x̄ ≈ 0.96), while P is symmetric (x̄ = 0). Q cannot represent the correlation between the spins, so F̃ stays above F. The same thing happens in Fig. 33.2.

## Concepts
- [[relative-entropy-kl-divergence]] — D_KL(Q‖P) = Σ Q ln(Q/P) in nats; ≥ 0, zero only if Q = P, asymmetric (p. 422)
- [[variational-free-energy]] (new) — βF̃(θ) = β⟨E⟩_Q − S_Q = D_KL(Q‖P) + βF; objective minimized over Q (p. 423)
- [[partition-function]] (new) — Z = Σ exp(−βE); βF = −ln Z; Z̃ = e^{−βF̃} ≤ Z (p. 422–423)
- [[mean-field-theory]] (new) — separable Q on spins gives a_m = β(ΣJ x̄ + h), x̄ = tanh a (p. 425)
- [[variational-inference-elbo]] — approximate posterior by Q(w;θ) minimizing F̃ ≥ −ln P(D|H); the author's names are ensemble learning and variational Bayes (p. 429)
- [[marginal-likelihood-evidence]] — P(D|H); F̃ is bounded below by its negative log (p. 429)
- [[separable-approximation]] (new) — Q as a product of factors; alternating optimization of each factor with the others fixed (pp. 429, 432)
- [[em-algorithm]] (new) — E-step = assignment (Q_k), M-step = update (Q_θ; a delta function for exactly soft K-means); Neal–Hinton view as a variational optimization (pp. 432–433)
- [[jaakkola-jordan-bounds]] (new) — adjustable upper/lower bounds on a function, tuned to be tightest (p. 433)
- [[posterior-distribution]] — P(w|D,H), the target Q approximates (p. 427)

## Canonical instances
- [[ising-mean-field]] — T_c^mft = 4 vs true 2.27; pitchfork and saddle-node bifurcations (pp. 426–427)
- [[two-spin-free-energy-surface]] — Fig. 33.1: E = −x₁x₂, β = 1.44, convex in each q (p. 425)
- [[unknown-gaussian-variational]] — Q_µ Gaussian, Q_σ gamma; 1/β̄ = S/(N−1) (pp. 429–431)
- [[soft-k-means-as-em]] — delta-function Q_θ; "kaboom" problem (pp. 432–433)
- [[logistic-bounds-jaakkola-jordan]] — upper and lower bounds on g(a) (p. 433)
- [[gaussian-compactness-exercise]] — F̃ vs G fits of a spherical Gaussian to an elongated one (pp. 435–436)

## Bridges (candidates)
- [same-math] variational free energy F̃ = D_KL(Q‖P) + F ↔ bayesian: ELBO, since F̃ = −ln P(D|H) + D_KL(Q‖posterior) is minus the lower bound on log evidence.
- [same-math] mean field equations x̄ = tanh(β(ΣJx̄ + h)) ↔ statistical physics: Ising mean field theory; the chapter rederives them as stationarity of F̃.
- [structural-analogy] alternating Q_µ / Q_σ updates (p. 430) ↔ Gibbs sampling: both update one block given the others, but one passes averages, the other samples.
- [structural-analogy] choosing a Q with KL(Q‖P) (compact) vs KL(P‖Q) (G, spread out) ↔ information-theory: asymmetry of relative entropy.
- [metaphor] ensemble learning: a point estimate is a delta-function Q ↔ MAP estimation: the spike is the crudest member of the family.

## Questions this raises
- Why does minimizing D_KL(Q‖P) give Q more compact than P, while minimizing G = D_KL(P‖Q) gives a broader one? When does each matter?
- Could a richer Q (with spin correlations) recover the Ising critical behaviour at acceptable cost?
- Can the local minima of F̃ in EM/variational Bayes be avoided, and how do they distort the posterior?
- How tight is the F̃ bound as a guide to model comparison, given that P(D|H) is only bounded?

## Exercises worth doing
- Ex. 33.1 (p. 427) — sketch βF̃(x̄) for different T and h; builds intuition for bifurcations — difficulty: easy (book rating [2])
- Ex. 33.2 (p. 433) — show the optimal Q_k with delta-function Q_θ gives the responsibilities — difficulty: easy ([2])
- Ex. 33.3 (p. 433) — show the optimal θ* is the soft K-means update step — difficulty: medium ([3])
- Ex. 33.4 (p. 433) — separable Q_θ update; does "kaboom" persist? — difficulty: hard ([4])
- Ex. 33.5 (p. 434) — Gaussian compactness: derive the optimal σ_Q² for F̃ and for G (final results are in L3) — difficulty: medium ([2] in book)
- Ex. 33.7 (p. 434) — marginals minimize G; F has three minima for the given P(x,y) — difficulty: medium ([2])

## Reading notes
- Printed page = pdf − 12 (pdf 434 = p. 422).
- Fig. 33.4 caption and fig. 33.3 axes are readable in the images. The text layer of Fig. 33.5 is out of order, so the bounds were checked against the image.
- p. 432: the text after (33.50) says F̃ "is bounded below by minus the evidence, ln P({x}|H)". The bound is −ln P, as p. 429 gives; the printed phrase is loose.
- (33.36) prints the prior as $\frac1{\sigma_\mu}\frac1\sigma$. S is not defined on these pages; the text says only that this posterior was studied in Chapter 24.
- Solutions are printed here only for 33.5 and 33.6. The solution to 33.7 is not in these pages.

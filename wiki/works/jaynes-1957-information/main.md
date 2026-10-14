---
id: jaynes-1957-information/main
work: jaynes-1957-information
unit: paper
pages: 620–630
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Information Theory and Statistical Mechanics (Jaynes, 1957)

## L0 — One line
If statistical mechanics is read as inference from partial knowledge, then the maximum-entropy distribution consistent with the known averages gives the usual rules (partition function, Boltzmann distribution) without ergodic or equal-a-priori-probability assumptions.

## L1 — The gist (≤ 120 words)
Statistical mechanics has long needed extra physical hypotheses (ergodicity, metric transitivity, equal a priori probabilities). Jaynes asks whether it can be justified differently. His answer is to take Shannon's entropy as the measure of uncertainty and to choose, among all distributions that agree with the known averages, the one with maximum entropy. This choice is the least biased one. It yields the partition function and the Boltzmann and grand-canonical distributions. It treats temperature, pressure and angular momentum alike (with precautions), and it gives new predictions (pressure ensemble, nuclear polarization). Definite predictions arise only when, and to the extent that, the distribution is sharp. A failed sharp prediction most reasonably points to a wrong enumeration of states.

**Prerequisites:** Lagrange multipliers; logarithms; partial derivatives; expectation values; basic statistical-mechanics vocabulary (energy levels, free energy, temperature, volume). The paper names ergodicity, metric transitivity and equal a priori probabilities as extra hypotheses of the conventional approach and does not define them on these pages.

## L2 — Key ideas (5–10 bullets)
- Shannon's measure $-K\sum p_i\ln p_i$ is, up to the constant $K$, the measure of uncertainty fixed by three conditions: continuity, monotonic increase of $A(n)$ for uniform distributions, and a composition law (p. 630). Jaynes defers the proof that $A(n)=K\ln n$ is the only solution to Shannon (p. 622, p. 630). The paper then uses it as the primitive concept, with entropy as the starting point (p. 621).
- Maximum-entropy inference gives $p_i=\exp\{-[\lambda_0+\sum\lambda_k f_k(x_i)]\}$, with the multipliers fixed by derivatives of $\ln Z$ (p. 623). It extends Laplace's insufficient-reason principle with a positive criterion: maximal non-commitment (p. 623).
- With energy as the known average, the same formalism gives the Boltzmann distribution and the thermodynamic relations $F=-kT\ln Z$ and $S=-k\sum p\ln p$ (p. 623–624). The grand-canonical ensemble follows when particle numbers are uncertain (p. 624).
- Nothing in the general laws of motion adds information about the state at time $t$ beyond what measurement gives, so for equilibrium predictions prior knowledge that measured quantities are constant is redundant (p. 624). Metric transitivity is irrelevant to subjective probabilities (p. 625) and "far from necessary" for the calculation rules and for interpreting observed behavior (p. 627).
- In the model with density of possible values $x^n/\epsilon$, the max-entropy estimates become sharper as $n$ grows, with relative spread of order $n^{-1/2}$ (p. 626). This is how definite thermodynamic laws can emerge from little information.
- The theory predicts only to the extent that its distributions are sharp. Jaynes argues that a definite prediction that fails experimentally is evidence of new physics, because the most reasonable conclusion is that the enumeration of states was wrong (p. 627).
- Any exchanged conserved quantity (energy, volume, particle number, angular momentum) can play the role of energy. The multiplier conjugate to energy is the reciprocal temperature, $\lambda=1/T$, and a thermometer merely tells us which $\lambda$ to use (p. 628).

## L3 — Walkthrough

### Abstract and 1. Introduction (p. 620–621)
- Jaynes argues that statistical mechanics need not be regarded as a physical theory dependent on extra assumptions, and can be treated as a form of statistical inference (p. 620). He wants an argument that (a) is mathematically sound, (b) adds no arbitrary assumptions, and (c) covers nonequilibrium and irreversible processes automatically (p. 620–621).
- Gibbs's theory needed extra assumptions: "freezing up" of degrees of freedom, the generic definition of phase, and a natural phase-space volume unit $h^{3N}$. With quantum mechanics these originally arbitrary assumptions are now seen as necessary consequences of the laws of physics (p. 621).
- The same formula $-\sum p_i\log p_i$ in thermodynamics and information theory does not by itself connect them. A new viewpoint is needed to show that it is the same concept (p. 621).
- Shannon showed that the entropy expression has a meaning independent of thermodynamics. This allows a reversal of reasoning: entropy is the starting concept, and the fact that a distribution maximizes entropy under constraints is what justifies its use (p. 621).
- Scope: equilibrium properties only, using probabilities of stationary states. Density-matrix refinements and irreversible processes are left to later papers (p. 621).

### 2. Maximum-entropy estimates (p. 621–623)
- **Problem.** $x$ takes values $x_i$ ($i=1..n$) with unknown $p_i$. We know only
$$\langle f(x)\rangle=\sum_{i=1}^n p_i f(x_i)\tag{2-1}$$
$$\sum_i p_i=1\tag{2-2}$$
- Determining $\langle g(x)\rangle$ would need $n-2$ more conditions (p. 622). Laplace's Principle of Insufficient Reason assigns equal probabilities absent reason to think otherwise. Except where evident symmetry makes events "equally possible", Jaynes says the assumption may appear as arbitrary as any other, and it has been fertile in generating paradoxes for continuous variables (p. 622).
- **Two schools.** The objective school sees probability as an empirically measurable property (frequencies). The subjective school sees it as a formal expression of expectation given the available information. Jaynes calls the two mathematically identical but conceptually not unifiable (p. 622). He regards the subjective view as broader and says the present problem requires it (p. 622). The problem is to find an assignment that "avoids bias, while agreeing with whatever information is given" (p. 622).
- **Entropy.** Information theory gives a unique measure of uncertainty, positive, increasing with uncertainty, and additive for independent sources (Appendix A):
$$H(p_1\cdots p_n)=-K\sum_i p_i\ln p_i\tag{2-3}$$
with $K>0$. Jaynes calls it entropy and treats "entropy" and "uncertainty" as synonyms (p. 622).
- **Principle.** Use the distribution of maximum entropy subject to what is known. This is the only unbiased assignment, since any other adds information we do not have (p. 623). With multipliers $\lambda,\mu$:
$$p_i=e^{-\lambda-\mu f(x_i)}\tag{2-4}$$
$$\langle f(x)\rangle=-\frac{\partial}{\partial\mu}\ln Z(\mu)\tag{2-5}$$
$$\lambda=\ln Z(\mu)\tag{2-6}$$
$$Z(\mu)=\sum_i e^{-\mu f(x_i)}\tag{2-7}$$
$Z$ is the partition function (p. 623).
- **Several constraints.** Given $\langle f_r(x)\rangle=\sum_i p_i f_r(x_i)$ (2-8):
$$Z(\lambda_1,\dots,\lambda_m)=\sum_i\exp\{-[\lambda_1f_1(x_i)+\cdots+\lambda_mf_m(x_i)]\}\tag{2-9}$$
$$p_i=\exp\{-[\lambda_0+\lambda_1f_1(x_i)+\cdots+\lambda_mf_m(x_i)]\}\tag{2-10}$$
$$\langle f_r(x)\rangle=-\frac{\partial}{\partial\lambda_r}\ln Z\tag{2-11}$$
$$\lambda_0=\ln Z\tag{2-12}$$
With $K=1$ the entropy is
$$S_{\max}=\lambda_0+\lambda_1\langle f_1\rangle+\cdots+\lambda_m\langle f_m\rangle\tag{2-13}$$
The variance, and (when $f_r$ also depends on parameters $\alpha_k$) the estimated derivatives, are
$$\Delta^2 f_r=\langle f_r^2\rangle-\langle f_r\rangle^2=\frac{\partial^2}{\partial\lambda_r^2}\ln Z\tag{2-14}$$
$$\Big\langle\frac{\partial f_r}{\partial\alpha_k}\Big\rangle=-\frac{1}{\lambda_r}\frac{\partial}{\partial\alpha_k}\ln Z\tag{2-15}$$
Jaynes states (2-14) and (2-15) without derivation; for (2-15) he says it is "easily shown" (p. 623).
- *Intuition note:* The recipe is: write down everything you know as averages and pick the flattest distribution that matches them. Lagrange multipliers give this flattest distribution an exponential form (2-10). All the numbers you need come from derivatives of one function, $\ln Z$.
- **Relation to insufficient reason.** Max-entropy reduces to equal probabilities when only the possibilities are enumerated. It differs by being justified positively, as maximally noncommittal about missing information, not negatively ("no reason to think otherwise") (p. 623). It gives positive weight to every situation not excluded by the data, which Jaynes says is similar in effect to an ergodic property (p. 623).
- **Alternative measure.** $-\sum p_i^2$ has similar qualitative properties but is harder to use. Conditional maxima cannot be found by a stationary property with Lagrange multipliers, because the distribution that makes it stationary under prescribed averages does not in general satisfy $p_i\ge0$. More importantly, Shannon's measure is the only one satisfying the composition law, so deductions from other measures, carried far enough, "will eventually lead to contradictions" (p. 623; Jaynes expects this).

### 3. Application to statistical mechanics (p. 623–626)
- With energy levels $E_i(\alpha_1,\alpha_2,\dots)$ (the $\alpha$ are volume, fields etc.) and only $\langle E\rangle$ known, (2-10) gives the Boltzmann distribution. Identifications:
$$\lambda_1=1/kT\tag{3-1}$$
$$U-TS=F(T,\alpha_1,\dots)=-kT\ln Z\tag{3-2}$$
$$S=-\frac{\partial F}{\partial T}=-k\sum_i p_i\ln p_i\tag{3-3}$$
$$\beta_i=kT\frac{\partial}{\partial\alpha_i}\ln Z\tag{3-4}$$
The forces $\beta_i$ (pressure etc.) are max-entropy estimates of $\partial E_i/\partial\alpha_k$ (p. 624). Thermodynamic and information entropy differ only by Boltzmann's constant, which Jaynes says may be regarded as a correction factor needed because temperature is measured in arbitrary units (p. 624, fn. 15).
- **Variable particle numbers.** If $n_s$ are unknown and $\langle E\rangle,\langle n_1\rangle,\dots$ are given:
$$Z=\sum_{n_1n_2\cdots}\sum_i\exp\{-[\lambda_1n_1+\lambda_2n_2+\cdots+\beta E_i(\alpha_k|n_s)]\}\tag{3-5}$$
This is the quantum-mechanical grand canonical ensemble, with
$$\mu_i=-kT\lambda_i\tag{3-6}$$
$$\langle n_i\rangle=\partial F/\partial\mu_i\tag{3-7}$$
$$F=-kT\lambda_0,\quad \lambda_0=\ln Z,$$
$$F(T,\alpha,\mu)=\langle E\rangle-TS+\mu_1\langle n_1\rangle+\mu_2\langle n_2\rangle+\cdots\tag{3-8}$$
(p. 624).
- **Key principle (Jaynes's italics):** "there is nothing in the general laws of motion that can provide us with any additional information about the state of a system beyond what we have obtained from measurement" (p. 624). The statement refers to interpreting the state at time $t$ from measurements at time $t$. Predicting time-dependent phenomena still needs the equations of motion. For equilibrium predictions only quantities observed to be constant in time are allowed as initial information, and prior knowledge that they are constant is then redundant (p. 624).
- **Consequence.** If new integrals of motion were discovered, our equations would not be completely changed unless new data gave information about the likely values of the new constants. Even a proof that a system is not metrically transitive would give no rational basis for excluding a region of phase space allowed by the information. Practically this equals an ergodic hypothesis, whether or not systems are ergodic (p. 624).
- **Subjective vs objective.** For objective probabilities metric transitivity would be crucial. For subjective ones it is irrelevant, yet the predictions are the same. The theory touches physics only in enumerating the possible states (p. 624–625).
- **Why does it predict well?** The information is minute, so one might expect no definite predictions. Jaynes's answer is that for systems with many degrees of freedom the distributions of macroscopic quantities have a single very sharp peak. Then average, most probable, median and so on coincide (p. 625).
- **Model (3-9).** Let $n$ be a non-negative integer and $\epsilon$ small:
$$x_1^{\,n+1}=\epsilon,\qquad x_{i+1}-x_i=\epsilon/x_i^{\,n}$$
For small $\epsilon$ sums become integrals with density $\rho(x)=x^n/\epsilon$ (p. 625).
- **Problem A:** given $\langle x\rangle$, estimate $x^2$.
$$Z(\lambda)=\int_0^\infty\rho(x)e^{-\lambda x}dx=\frac{n!}{\epsilon\lambda^{n+1}},\qquad \langle x\rangle=-\frac{\partial}{\partial\lambda}\ln Z=\frac{n+1}{\lambda}$$
$$\langle x^2\rangle\{\langle x\rangle\}=Z^{-1}\int_0^\infty x^2\rho(x)e^{-\lambda x}dx=\frac{n+2}{n+1}\langle x\rangle^2\tag{3-10}$$
- **Problem B:** given $\langle x^2\rangle$, estimate $x$.
$$Z(\lambda)=\int_0^\infty\rho(x)\exp(-\lambda x^2)dx=\frac{\pi^{1/2}\,n!}{2^{n+1}(n/2)!}\frac{1}{\epsilon\lambda^{\frac12(n+1)}}$$
$$\langle x^2\rangle=-\frac{\partial}{\partial\lambda}\ln Z=\frac{n+1}{2\lambda}$$
$$\langle x\rangle\{\langle x^2\rangle\}=Z^{-1}\int_0^\infty x\rho(x)\exp(-\lambda x^2)dx=\Big(\frac{n+1}{2}\Big)^{1/2}\frac{(\tfrac12 n)!}{[\tfrac12(n+1)]!}\langle x^2\rangle^{1/2}\tag{3-11}$$
- Fig. 1 plots both "regression lines" for $n=1$; Fig. 2 plots the slopes against $n$. As $n\to\infty$ both lines approach 45°, so for large $n$ there is a practically definite relation between $\langle x\rangle$ and $\langle x^2\rangle$, whichever is "given" (p. 625–626).
- **Spread.** In problem A:
$$\langle x^2\rangle-\langle x\rangle^2=\langle x\rangle^2/(n+1)\tag{3-12}$$
- For a well-behaved $g(x)$ with a power series about $x=\langle x\rangle$ (p. 626):
$$\langle g(x)\rangle=g(\langle x\rangle)+g''(\langle x\rangle)\frac{\langle x\rangle^2}{2(n+1)}+O\!\left(\tfrac1{n^2}\right)\tag{3-13}$$
$$\Delta^2(g)=\langle g^2\rangle-\langle g\rangle^2=[g'(\langle x\rangle)]^2\frac{\langle x\rangle^2}{n+1}+O\!\left(\tfrac1{n^2}\right)\tag{3-14}$$
A sufficient condition for $x$ to be well determined by $\langle g\rangle$ is that $x$ be a sufficiently smooth monotonic function of $g$. The relative standard deviations of all sufficiently well-behaved functions fall like $n^{-1/2}$. The parameter $n$ is compared to the number of degrees of freedom of a macroscopic system (p. 626).
- *Intuition note:* In this model, knowing one average pins down other averages more and more tightly as $n$ grows. Jaynes compares $n$ to the number of degrees of freedom of a macroscopic system. Definite laws can therefore come out of very little information.

### 4. Subjective and objective statistical mechanics (p. 626–627)
- Many statements have two readings. The Maxwellian velocity distribution is both the distribution realizable in the most ways and a verified experimental fact. Entropy is both a measure of ignorance and a measurable quantity (p. 626).
- **Objection (most often advanced against the subjective interpretation of entropy):** for equilibrium conditions entropy is an experimentally measurable quantity whose most important properties were first found empirically (p. 626). Jaynes replies that he frankly recognizes that the probabilities involved in prediction from partial information can have only a subjective significance, and that inventing a fictitious ensemble does not change this. He reasons that, as in common sense, little relevant information gives a broad distribution, meaning "no definite conclusion" (p. 626).
- **Jaynes's claim (italics in source):** the theory makes definite predictions about experimental behavior only when, and to the extent that, it leads to sharp distributions. Where the data are weak, the result is still the best possible given the information (p. 626).
- Verified predictions are those where the distribution of measured macroscopic quantities has enormously sharp peaks. This requires that each of the overwhelming majority of microstates with appreciable weight gives the same macroscopic behavior. Jaynes calls this "macroscopic uniformity", and it is the objective content of the calculations, not the probabilities per se (p. 626–627). Choosing at random one state out of each $10^{10^{10}}$ and arbitrarily assigning zero probability to all the others would in most cases have no discernible effect on the macroscopic predictions (p. 627).
- If a definite prediction fails experimentally, this cannot be explained away by insufficient initial information, since then the theory would not have given a sharp distribution. The most reasonable conclusion is that the enumeration of possible states was wrongly given. Experimental proof that a definite prediction is incorrect gives evidence of new laws of physics. Jaynes cites the failures of classical statistical mechanics resolved by quantum theory (p. 627).
- Prediction and interpretation are different problems. Interpretation (inferring microscopic causes) needs objective probabilities (fractions of time in a state) and a different, "objective" statistical mechanics. One can never deduce the objective probabilities of individual states from macroscopic measurements; many different probability assignments are experimentally indistinguishable, and severe unknown constraints on the states could exist. Jaynes concludes that, although it is now a relevant question, metric transitivity is far from necessary for justifying the prediction rules or for interpreting observed behavior (p. 627). Bohm and Schützer reached similar conclusions by different arguments (p. 627).

### 5. Generalized statistical mechanics (p. 627–629)
- Since the principles of max-entropy inference are independent of any physical properties, it appears that in subjective statistical mechanics all measurable quantities may be treated on the same basis as energy, subject to certain precautions (p. 627). Vary the functions $f_k(x_i)$ and the expectations $\langle f_k\rangle$ independently:
$$\delta\lambda_0=\delta\ln Z=-\sum_k[\delta\lambda_k\langle f_k\rangle+\lambda_k\langle\delta f_k\rangle]\tag{5-1}$$
$$\delta S=\sum_k\lambda_k[\delta\langle f_k\rangle-\langle\delta f_k\rangle]=\sum_k\lambda_k\,\delta Q_k\tag{5-2}$$
$$\delta Q_k=\delta\langle f_k\rangle-\langle\delta f_k\rangle\tag{5-3}$$
- $\delta Q_k$ generalizes infinitesimal heat ("heat of the $k$th type"). $\lambda_k$ is the integrating factor, called "statistically conjugate" to $f_k$. The words "heat" and "temperature" are kept for their conventional sense (p. 627).
- **Temperature measurement.** Energy is rarely measured directly. Define a *heat bath* $\sigma_2$: (a) its energy levels are so closely spaced as to form a continuum macroscopically; (b) its max-entropy entropy $S_2$ is a monotonic function of $\langle E_2\rangle$; (c) it can be put in *thermal contact* with another system $\sigma_1$, exchanging only energy, with interaction energy $E_{12}$ small. A *thermometer* is a heat bath with a pointer reading average energy, scaled to give $T$:
$$1/T\equiv dS_2/d\langle E_2\rangle\tag{5-4}$$
(p. 628).
- For the combined system $\Sigma=\sigma_1+\sigma_2$, the interaction may allow transitions between $(ij)$ and $(mn)$ if $E_{1i}+E_{2j}=E_{1m}+E_{2n}$. With no knowledge of the matrix elements, there is no rational basis to exclude any such transition. So $p_{ij}$ may depend on the energies only through $E_{1i}+E_{2j}$ (p. 628, fn. 18 admits lacking rigor, to be supplied by the density matrix). Then
$$Z(\lambda)=\sum_{ij}\exp[-\lambda(E_{1i}+E_{2j})]=Z_1(\lambda)Z_2(\lambda)\tag{5-5}$$
$$Z_1=\sum_i e^{-\lambda E_{1i}},\quad Z_2=\sum_j e^{-\lambda E_{2j}}\tag{5-6}$$
$$\langle E_2\rangle=-\frac{\partial}{\partial\lambda}\ln Z_2(\lambda)\tag{5-7}$$
$$\lambda=dS_2/d\langle E_2\rangle=1/T\tag{5-8}$$
$$p_{ij}=p_i(1)\,p_j(2)\tag{5-9}$$
$$S(\Sigma)=S_1+S_2\tag{5-10}$$
(p. 628).
- Conclusion: the thermometer only tells us which $\lambda$ to use for $\sigma_1$. Its detailed properties need not be considered. Any conserved, exchangeable quantity can replace energy, e.g. in a "volume bath", "particle bath" or "momentum bath" (p. 628).
- *Intuition note:* A thermometer is information about one number, $\lambda$. After reading it we use the same exponential-form distribution as if we had measured the average energy.
- **Pressure ensemble.** For levels $E_i(V)$ with $\langle E\rangle$, $\langle V\rangle$ given (p. 629):
$$Z(\lambda,\mu)=\int_0^\infty dV\sum_i\exp[-\lambda E_i(V)-\mu V]$$
A short calculation gives $P=-\langle\partial E_i/\partial V\rangle=\mu/\lambda$, so $\mu=\lambda P=P/kT$. The distribution is proportional to
$$\exp\Big\{-\Big[\frac{E_i(V)+PV}{kT}\Big]\Big\}\tag{5-11}$$
This is the "pressure ensemble" of Lewis and Siegert (p. 629).
- **Nuclear polarization effect.** $\sigma_1$ is a nucleus of spin $I$; $\sigma_2$ is the rest, an angular-momentum bath that can exchange angular momentum but not energy with $\sigma_1$. Given $T$ and that $\sigma_2$ rotates about the $z$ axis with macroscopic angular velocity $\omega$ (p. 629):
$$Z_2(\beta,\lambda)=\sum_{n,m_2}\exp[-\beta E_2(n,m_2)-\lambda m_2]\tag{5-12}$$
$$\langle m_2\rangle=-\frac{\partial}{\partial\lambda}\ln Z_2=\frac{B\omega}{\hbar}\tag{5-13}$$
with $\beta=1/kT$ and $B$ the moment of inertia of $\sigma_2$. Then
$$\langle m_1\rangle=-\frac{\partial}{\partial\lambda}\ln Z_1(\lambda),\qquad Z_1=\sum_{m=-I}^{I}e^{-\lambda m}\tag{5-14, 5-15}$$
and for $I=\tfrac12$: $\langle m_1\rangle=-\tfrac12\tanh(\tfrac12\lambda)$ (5-16). For small $\omega$, expand $Z_2(\beta,\lambda)=Z_2(\beta,0)[1-\lambda\langle m_2\rangle_0+\tfrac12\lambda^2\langle m_2^2\rangle_0+\cdots]$. With no magnetic field $\langle m_2\rangle_0=0$ and $\hbar^2\langle m_2^2\rangle_0=kTB$, so (5-13) gives
$$\lambda=-\hbar\omega/kT\tag{5-17}$$
The polarization equals that from a magnetic field with Larmor frequency $\omega_L=\omega$. For $|\lambda|\ll1$:
$$\langle m_1\rangle=\frac{\hbar^2 I(I+1)}{3kTB}\langle m_2\rangle\tag{5-18}$$
(p. 629).
- Jaynes sees "every reason to believe" the effect exists. It is related to the Einstein–de Haas effect, and it is predicted without the spin energy or the mechanism. Numerical example: water rotated at 36 000 rpm should polarize protons like a field of about 1/7 gauss (p. 629).

### 6. Conclusion (p. 629–630)
- The von Neumann–Shannon entropy is taken literally as a measure of uncertainty, making entropy more fundamental than energy. Reinterpreting prediction in the subjective sense gives the usual relations without ensembles, ergodicity or equal a priori probabilities (p. 629). Maximizing entropy is not a law of physics but a method of reasoning that avoids unconscious arbitrary assumptions (p. 630).

### Appendix A. Entropy of a probability distribution (p. 630)
- **Three conditions.** (1) $H$ is continuous in the $p_i$. (2) If all $p_i=1/n$, then $A(n)=H(1/n,\dots,1/n)$ is monotonic increasing in $n$. (3) Composition law: grouping events into composite events must not change the total uncertainty:
$$H(p_1\cdots p_n)=H(w_1\cdots w_r)+w_1H(p_1/w_1,\dots,p_k/w_1)+w_2H(p_{k+1}/w_2,\dots,p_{k+m}/w_2)+\cdots\tag{A-1}$$
with $w_1=p_1+\cdots+p_k$, $w_2=p_{k+1}+\cdots+p_{k+m}$, etc. The weight $w_1$ appears because the extra uncertainty arises only with probability $w_1$. Example: $H(\tfrac12,\tfrac13,\tfrac16)=H(\tfrac12,\tfrac12)+\tfrac12H(\tfrac23,\tfrac13)$ (p. 630).
- By (1) it suffices to find $H$ for rational $p_i=n_i/\sum n_i$. By (3), $H$ is then fixed by the $A(n)$: a choice among $n$ alternatives is a first step in a choice among $\sum n_i$ equally likely alternatives, the second step being a choice among $n_i$. Example $(n_1,n_2,n_3)=(3,4,2)$:
$$H(\tfrac39,\tfrac49,\tfrac29)+\tfrac39A(3)+\tfrac49A(4)+\tfrac29A(2)=A(9)$$
In general
$$H(p_1\cdots p_n)+\sum_i p_iA(n_i)=A\Big(\sum_i n_i\Big)\tag{A-2}$$
Taking all $n_i=m$:
$$A(m)+A(n)=A(mn)\tag{A-3}$$
solved by
$$A(n)=K\ln n,\quad K>0\ \text{by condition (2)}\tag{A-4}$$
Jaynes refers to Shannon's paper for the proof that (A-4) is the only solution. Substituting into (A-2) gives
$$H=K\ln\Big(\sum n_i\Big)-K\sum p_i\ln n_i=-K\sum_ip_i\ln p_i\tag{A-5}$$
(p. 630). Step from the first to the second form (added step): $\ln\sum n_i-\sum_i p_i\ln n_i=-\sum_i p_i\ln(n_i/\sum n_j)$ because $\sum_i p_i=1$.

## Toy example (ours, not from the text)
Let $x$ take three values with $f(x_i)=0,1,2$. Suppose we know only $\langle f\rangle=4/7$.
- By (2-4), $p_i\propto z^{f_i}$ with $z=e^{-\mu}$. Try $z=1/2$: weights $1,\tfrac12,\tfrac14$, sum $Z=\tfrac74$, so $p=(\tfrac47,\tfrac27,\tfrac17)$.
- Check with (2-5): $\langle f\rangle=(z+2z^2)/(1+z+z^2)=(\tfrac12+\tfrac12)/\tfrac74=\tfrac47$ ✓.
- Entropy in bits, using $\log_2 7=2.807$: $\tfrac47(0.807)+\tfrac27(1.807)+\tfrac17(2.807)=(3.228+3.614+2.807)/7\approx1.379$.
- Check with (2-13) in nats: $\lambda_0=\ln\tfrac74=0.560$, $\mu\langle f\rangle=0.693\times\tfrac47=0.396$, sum $0.956$ nats $=1.379$ bits ✓.
- Rival distribution with the same mean: $q=(\tfrac37,\tfrac47,0)$, mean $=\tfrac47$. Its entropy is $\tfrac37(1.222)+\tfrac47(0.807)\approx0.985$ bits. It is less noncommittal because it rules out $x_3$, which the data do not exclude (compare p. 623).

## Concepts
- [[maximum-entropy-principle]] — choose the distribution with maximum entropy subject to the known averages; Jaynes calls it the unbiased choice (p. 623)
- [[exponential-family-gibbs-distribution]] — max-entropy solution $p_i=\exp\{-[\lambda_0+\sum\lambda_kf_k(x_i)]\}$ (p. 623)
- [[entropy-hx]] — $-K\sum p_i\ln p_i$, read as the amount of uncertainty in a distribution (p. 622)
- [[partition-function]] (new) — $Z=\sum_i e^{-\sum\lambda_k f_k(x_i)}$; $-\partial\ln Z/\partial\lambda_r=\langle f_r\rangle$ and $\partial^2\ln Z/\partial\lambda_r^2$ is the variance (p. 623)
- [[principle-of-insufficient-reason]] (new) — Laplace's equal-probability rule; max-entropy extends it with a positive criterion (p. 622–623)
- [[subjective-probability]] (new) — probability as a measure of knowledge given the information, in contrast to objective frequency (p. 622)
- [[statistically-conjugate-multiplier]] (new) — $\lambda_k$, the Lagrange multiplier paired with $f_k$; $\lambda=1/T$ for energy (p. 627–628)
- [[macroscopic-uniformity]] (new) — nearly all microstates with appreciable weight give the same macroscopic behavior; the objective content of the predictions (p. 627)
- [[chain-rule]] — Jaynes's composition law (A-1), the grouping property of uncertainty, used to single out the entropy form (p. 630)

## Canonical instances
- [[boltzmann-distribution]] — max-entropy estimate when only $\langle E\rangle$ is known (p. 623–624)
- [[grand-canonical-ensemble]] — max-entropy estimate with $\langle E\rangle$, $\langle n_i\rangle$ given (p. 624)
- [[x-x2-regression-model]] (new) — density $x^n/\epsilon$ model; estimates of $x^2$ from $x$ and vice versa sharpen as $n$ grows (p. 625–626)
- [[pressure-ensemble]] — max-entropy with $\langle E\rangle,\langle V\rangle$ given (p. 629)
- [[nuclear-polarization-effect]] — spin polarization predicted from rotation via an angular-momentum bath (p. 629)

## Bridges (candidates)
- [same-math] Max-entropy solution under expectation constraints ↔ information-theory: exponential family / Gibbs distribution — the same form $p\propto\exp(\sum\lambda_if_i)$.
- [same-math] Composition law (A-1) ↔ information-theory: chain rule $H(X,Y)=H(X)+H(Y|X)$ — the grouping property is the chain rule for a coarse variable and the conditional given it.
- [structural-analogy] $\partial^2\ln Z/\partial\lambda^2$ as variance ↔ Fisher information: curvature of log-likelihood — the same second-derivative-of-log-normalizer structure (relation not stated in the paper).
- [metaphor] Heat bath/thermometer as "bath" for any conserved quantity ↔ information-theory: side information as a single-number constraint on the distribution.

## Questions this raises
- How can "maximal noncommittal" be defined for continuous variables, where the paper restricts itself to the discrete case (p. 622, fn. 6)?
- How do the deferred density-matrix refinements fix the non-rigorous step in the thermal-contact argument (p. 628, fn. 18)?
- Does a failed sharp prediction always localize the error in the state enumeration, or could the error lie elsewhere (p. 627)?
- How large must $n$ be in real systems for the sharpness argument of (3-12)–(3-14) to apply (p. 626)?

## Reading notes
- Page offset: the PDF page labels give no printed number. The page images show printed pages 620–630, so printed = pdf + 619 (pdf 1 = p. 620, the title page, whose number is not printed). All citations use printed numbers.
- Only the first PDF page carries "Reprinted from The Physical Review, Vol. 106, No. 4, 620–630, May 15, 1957".
- The nested exponent in "one out of each $10^{10^{10}}$ of the possible states" (p. 627) is small but readable in the page image, and the digest transcribes it.
- In (5-11) the image has a nested bracket; (5-14)–(5-18) were checked against the image. The sign in (5-17) follows the page and is consistent with expanding $\ln Z_2$ to second order in $\lambda$.
- Jaynes states (2-14) and (2-15) without derivation. He gives only a pointer to Shannon for the uniqueness proof in (A-4). The digest does not supply either.

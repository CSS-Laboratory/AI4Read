---
id: mackay-2003-information/ch31-ising
work: mackay-2003-information
unit: "31 Ising Models"
pages: 399-412
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Ising Models

## L0 — One line
An Ising model (spins ±1 with neighbour couplings) can be studied by Gibbs/Metropolis Monte Carlo or exactly by a transfer matrix whose largest eigenvalue gives the free energy of a long thin strip, with the simulations showing growing energy fluctuations (rather than a heat-capacity peak alone) as the interesting hint of a phase transition.

## L1 — The gist (≤ 120 words)
How can we extract physical properties (energy, heat capacity, entropy, phase transitions) from an Ising model? MacKay shows that heat capacity equals energy variance scaled by temperature, so fluctuations can be measured in simulation. He simulates rectangular and triangular lattices with Gibbs sampling, noting that a heat-capacity peak alone does not prove a phase transition. He then computes the partition function exactly for thin strips with a transfer matrix; the largest eigenvalue gives the free energy per spin. The two methods seem to agree well. The antiferromagnetic triangular model is frustrated and appears to have non-zero entropy at zero temperature. Ising models link to spin glasses, Hopfield networks and constrained channels.

**Prerequisites:** logarithms, mean and variance, partial derivatives, eigenvalues of a symmetric matrix, the Boltzmann distribution, Gibbs sampling. Terms used above: heat capacity = rate of change of mean energy with temperature; partition function $Z$ = sum of Boltzmann weights over all states; free energy $F=-kT\ln Z$; transfer matrix = a matrix that adds one column of spins at a time; frustrated = not all neighbour couplings can be satisfied at once.

## L2 — Key ideas (5–10 bullets)
- The Ising energy and Boltzmann distribution define the model. Generalising couplings and fields gives spin glasses, Hopfield networks and Boltzmann machines (pp. 400–401).
- Differentiating $\ln Z$ gives the mean energy and the energy variance. Hence $C = k_B\beta^2\mathrm{var}(E)$: heat capacity is a fluctuation quantity (pp. 401–402).
- Gibbs sampling or Metropolis can sample the equilibrium distribution. Energy fluctuations that grow at intermediate temperature hint at a phase transition (pp. 402–403).
- A heat-capacity peak occurs in any finite-level system (Schottky anomaly). A peak in the energy fluctuations is the interesting signal (p. 404).
- The $J=\pm1$ rectangular models are expected to be equivalent by a checkerboard flip, except for odd-sized periodic grids. The antiferromagnetic triangular model is always frustrated and shows no energy-fluctuation peak in the $N=4096$ simulation (pp. 406–407).
- The transfer-matrix method writes $Z=\mathrm{Trace}[\mathbf M^C]$ for a strip. For long strips the free energy per spin comes from the largest eigenvalue alone (p. 409).
- Free energy gives entropy, so ground-state degeneracy is visible. The triangular antiferromagnet appears to have about 0.3 entropy per spin at $T\to0$ (pp. 410–411).
- Monte Carlo and transfer-matrix results seem to agree very well (p. 412).

## L3 — Walkthrough

### Chapter introduction (p. 399)
The author says Ising models relate to neural networks, to the exact tree-based computations of Chapter 25, and to crude binary-image models. They also relate to two-dimensional constrained channels. A bar-code where no black dot is surrounded by black and no white dot by white resembles a low-temperature antiferromagnetic Ising model. Evaluating that model's entropy is equivalent to evaluating the channel capacity (p. 399).

### Definition of the model (p. 400)
An Ising model is an array of spins $x_n\in\{-1,+1\}$ that are magnetically coupled. $(m,n)\in\mathcal N$ means $m,n$ are neighbours. $J_{mn}=J$ for neighbours and $0$ otherwise. $H$ is the applied field.
$$E(\mathbf x;J,H) = -\Big[\tfrac12\sum_{m,n}J_{mn}x_mx_n+\sum_n Hx_n\Big]\tag{31.1}$$
The factor $\tfrac12$ is there because each pair is counted twice. $J>0$ is ferromagnetic (neighbours prefer equal spins); $J<0$ is antiferromagnetic (neighbours prefer opposite spins). At temperature $T$, with $\beta=1/k_BT$:
$$P(\mathbf x\mid\beta,J,H)=\frac{1}{Z(\beta,J,H)}\exp[-\beta E(\mathbf x;J,H)]\tag{31.2}$$
$$Z(\beta,J,H)\equiv\sum_{\mathbf x}\exp[-\beta E(\mathbf x;J,H)]\tag{31.3}$$
Three reasons for relevance (pp. 400–401):
1. Ising models are models of magnetic systems with a phase transition. By universality, systems with the same dimension and symmetries have identical scaling laws at their transitions.
2. With non-constant couplings $J_{mn}$ and fields $h_n$ (eq. 31.4, same form as 31.1) we get spin glasses, called Hopfield networks or Boltzmann machines in neural networks. In some of these models all spins are neighbours; physicists then call the system an "infinite-range" spin glass and networkers a "fully connected" network.
3. The Ising model is a statistical model in its own right.

### Remarkable relationships: heat capacity and fluctuations (pp. 401–402)
Heat capacity is $C\equiv\partial\bar E/\partial T$ (31.5), with $\bar E=\frac1Z\sum_{\mathbf x}\exp(-\beta E(\mathbf x))E(\mathbf x)$ (31.6) and $Z=\sum_{\mathbf x}\exp(-\beta E(\mathbf x))$ (31.7). Derivation, step by step:
$$\frac{\partial\ln Z}{\partial\beta}=\frac1Z\sum_{\mathbf x}-E(\mathbf x)\exp(-\beta E(\mathbf x))=-\bar E\tag{31.8}$$
$$\frac{\partial^2\ln Z}{\partial\beta^2}=\frac1Z\sum_{\mathbf x}E(\mathbf x)^2\exp(-\beta E(\mathbf x))-\bar E^2=\langle E^2\rangle-\bar E^2=\mathrm{var}(E)\tag{31.9}$$
$$\frac{\partial\bar E}{\partial T}=-\frac{\partial}{\partial T}\frac{\partial\ln Z}{\partial\beta}=-\frac{\partial^2\ln Z}{\partial\beta^2}\frac{\partial\beta}{\partial T}=-\mathrm{var}(E)(-1/k_BT^2)\tag{31.10}$$
$$C=\frac{\mathrm{var}(E)}{k_BT^2}=k_B\beta^2\mathrm{var}(E)\tag{31.11}$$
So observing energy variance at equilibrium gives the heat capacity.

The author finds this "almost paradoxical". For a system with a finite set of states, at high temperature all states are equiprobable, so $\bar E$ is nearly constant and $C\approx0$, yet energy fluctuates. The resolution is that $C$ only tends to zero, as $\mathrm{var}(E)/k_BT^2$ with $\mathrm{var}(E)$ tending to a constant. The author calls this $1/T^2$ high-temperature behaviour of finite systems "very general" (pp. 401–402). With $\beta$ as the temperature variable, $C^{(\beta)}\equiv\partial\bar E/\partial\beta=\mathrm{var}(E)$ (31.12), so heat capacity and fluctuations would be identical (p. 402).

*Intuition note:* How fast the mean energy changes with temperature is fixed by how much the energy fluctuates at constant temperature ($C=\mathrm{var}(E)/k_BT^2$). That is why one simulation run at one temperature can tell us the heat capacity.

**Exercise 31.1** (p. 402): with $S=\sum p(\mathbf x)\ln\frac1{p(\mathbf x)}$ (31.13), $p(\mathbf x)=\exp[-\beta E(\mathbf x)]/Z(\beta)$ (31.14), and $k_B=1$, show (a) $S=\ln Z(\beta)+\beta\bar E(\beta)$ (31.15); (b) $S=-\partial F/\partial T$ (31.16), with $F=-kT\ln Z$.

### 31.1 Monte Carlo simulation (pp. 402–407)

**Algorithms (p. 402).** Gibbs sampling: pick a spin $n$ at random; set it to $+1$ with probability
$$P(+1\mid b_n)=\frac{1}{1+\exp(-2\beta b_n)}\tag{31.17}$$
where the local field is $b_n=\sum_{m:(m,n)\in\mathcal N}Jx_m+H$ (31.18). The factor 2 appears because states are $\{+1,-1\}$ rather than $\{+1,0\}$. After enough iterations this converges to (31.2). Alternative, Metropolis: the energy change from flipping spin $n$ is $\Delta E=2x_nb_n$ (31.19); accept with probability $1$ if $\Delta E\le0$ and $\exp(-\beta\Delta E)$ if $\Delta E>0$ (31.20). It has roughly double the probability of accepting unfavourable moves, so it may be more efficient. At very low temperatures the relative merits may be subtle (p. 403).

**Rectangular geometry (p. 403).** Periodic boundaries, $H=0$, $J=\pm1$. Temperature started at $T=33$ ($\beta=0.03$), was lowered gradually to $T=0.1$ ($\beta=10$), then raised again. If equilibrium were not reached at some temperature, hysteresis would be expected, so this is a crude check; the two runs also give an idea of reproducibility if they are effectively independent. At each temperature the author recorded mean energy per spin, standard deviation of energy, and mean square magnetization $m=\frac1N\sum_nx_n$ (31.21). Deciding when equilibrium is reached is tricky. His crude rule: iterations per temperature a few hundred times $N$, discarding the first third. With $N=100$ he needed more than 100 000 iterations. Chapter 32 is said to offer a solution (p. 403).

**Results, $J=1$ (p. 403).** Grids $l\times l$, $l=4,\dots,10,40,64$. There are two ground states (all $+1$, all $-1$) with energy $-2$ per spin. At high temperature the spins are independent and the energy fluctuates about 0 with standard deviation $\propto1/\sqrt N$. With $N=16$ the energy rises monotonically. With $N=100$ the high-temperature fluctuations shrink as $1/\sqrt N$, but fluctuations at intermediate temperature become relatively bigger. The author calls this the signature of a collective phenomenon, a phase transition. Only infinite $N$ gives a true transition; $N=100$ gives a hint of critical fluctuations (p. 403; figures 31.3, 31.5).

**Contrast with Schottky anomaly (p. 404).** A peak in heat capacity occurs in any system with a finite number of energy levels, so it is not by itself evidence of a phase transition. Such peaks were viewed as anomalies in classical thermodynamics, since "normal" systems with infinitely many levels (e.g. a particle in a box) have heat capacities that are constant or increasing with temperature. Take a two-level system with energies $0$ and $\epsilon$:
$$\bar E(\beta)=\epsilon\frac{\exp(-\beta\epsilon)}{1+\exp(-\beta\epsilon)}=\epsilon\frac{1}{1+\exp(\beta\epsilon)}\tag{31.22}$$
$$\mathrm dE/\mathrm d\beta=-\epsilon^2\frac{\exp(\beta\epsilon)}{[1+\exp(\beta\epsilon)]^2}\tag{31.23}$$
$$C=\mathrm dE/\mathrm dT=-\frac{\mathrm dE}{\mathrm d\beta}\frac1{k_BT^2}=\frac{\epsilon^2}{k_BT^2}\frac{\exp(\beta\epsilon)}{[1+\exp(\beta\epsilon)]^2}\tag{31.24}$$
and $\mathrm{var}(E)=Ck_BT^2=-\mathrm dE/\mathrm d\beta$. $C$ has a peak, but $\mathrm{var}(E)$ increases monotonically to a value proportional to the number of independent spins (figure 31.6). So a peak in the fluctuations is what is interesting. The Ising model has one (figure 31.5, second row) (p. 404).

*Intuition note:* A system with only finitely many levels can show a bump in heat capacity without anything collective happening, because its energy variance just rises smoothly. In the Ising model, by contrast, the energy fluctuations themselves become relatively bigger at intermediate temperature, which is the hint of a collective transition.

**Rectangular, $J=-1$ (pp. 404–406).** An infinite system's ground states are the two checkerboards, also with energy $-2$ per spin. For an infinite $J=1$ system, flipping all spins on the black squares of a checkerboard and setting $J=-1$ leaves the energy unchanged (magnetization changes). So thermodynamic properties of the two infinite systems are expected to be identical at zero field. Subtlety: if a periodic grid has odd size in any direction, the checkerboard does not match at the boundary. The $J=-1$ ground state then has degeneracy greater than 2 and energy above $-2$ per spin. Boundary frustration grows as the boundary length, $\propto\sqrt N$, so its fractional influence falls as $1/\sqrt N$. Differences are therefore strongest for small systems; for $N=25$ they are striking (figure 31.9) (p. 406).

**Triangular model (pp. 406–407).** $J=1$ presumably resembles the rectangular case. For $J=-1$ there is no unfrustrated ground state, because any three mutually neighbouring spins are frustrated. Of the eight configurations of a triangle, six have energy $-|J|$ and two have $3|J|$ (figure 31.10). The author says we might therefore expect a non-zero entropy at absolute zero, joking "Triangular model violates third law of thermodynamics!" (p. 406). Results for $N=4096$ (figure 31.11): there is no peak at all in the energy standard deviation for $J=-1$. This indicates that the antiferromagnet has no phase transition to a state with long-range order (p. 407).

### 31.2 Direct computation of the partition function (pp. 407–412)

**Setup (p. 407).** $Z(\beta,\mathbf J,\mathbf b)\equiv\sum_{\mathbf x}\exp[-\beta E(\mathbf x;\mathbf J,\mathbf b)]$ (31.25), with $k_B=1$ and $F=-\frac1\beta\ln Z$. There are $2^N$ states, so direct summation is infeasible. As in the sum–product algorithm (Chapter 25), take a strip of width $W$, periodic in both directions. Compute partial partition functions along its length; each step sums over the boundary states, which costs exponentially in $W$. If the system is translation-invariant along its length, one iteration suffices for any length (pp. 407–409).

**Matrix formulation (p. 409).** Label the $C$ columns' states $s_1,\dots,s_C$, each an integer in $0..2^W-1$; bit $r$ of $s_c$ gives the spin in row $r$, column $c$. Then
$$Z=\sum_{\mathbf x}\exp(-\beta E(\mathbf x))\tag{31.26}$$
$$=\sum_{s_1}\sum_{s_2}\cdots\sum_{s_C}\exp\Big(-\beta\sum_{c=1}^C\mathcal E(s_c,s_{c+1})\Big)\tag{31.27}$$
with $s_{C+1}\equiv s_1$ for periodic boundaries, and one possible definition
$$\mathcal E(s_c,s_{c+1})=\sum_{\substack{(m,n)\in\mathcal N:\\ m\in c,\,n\in c+1}}Jx_mx_n+\tfrac14\sum_{\substack{(m,n)\in\mathcal N:\\ m\in c,\,n\in c}}Jx_mx_n+\tfrac14\sum_{\substack{(m,n)\in\mathcal N:\\ m\in c+1,\,n\in c+1}}Jx_mx_n.\tag{31.28}$$
For the rectangular model this makes the matrix symmetric in $s_c,s_{c+1}$. The factors $\tfrac14$ arise because each vertical bond is half inside the rectangle and is visited twice, since $m,n$ both run over the column (figure 31.13 caption). Worked example from figure 31.13: $s_2=(100)_2$, $s_3=(110)_2$, horizontal bonds contribute $+J$, vertical bonds $-J/2$ on each side (periodic top–bottom), so $\mathcal E(s_2,s_3)=0$.

Define $M_{ss'}=\exp(-\beta\mathcal E(s,s'))$ (31.29), a $2^W\times2^W$ matrix. Then
$$Z=\sum_{s_1}\cdots\sum_{s_C}\Big[\prod_{c=1}^CM_{s_c,s_{c+1}}\Big]\tag{31.30}$$
$$=\mathrm{Trace}[\mathbf M^C]\tag{31.31}$$
$$=\sum_a\mu_a^C\tag{31.32}$$
where $\{\mu_a\}_{a=1}^{2^W}$ are the eigenvalues of $\mathbf M$. As $C$ grows, $Z$ is dominated by the largest eigenvalue:
$$Z\to\mu_{\max}^C\tag{31.33}$$
$$f=-kT\ln Z/(WC)=-kTC\ln\mu_{\max}/(WC)=-kT\ln\mu_{\max}/W\tag{31.34}$$
The author finds it "really neat" that all thermodynamic properties of a long thin strip follow from this one eigenvalue (p. 409).

*Intuition note:* Each column interacts only with the next, so the sum over $2^N$ states becomes a product of copies of one matrix $\mathbf M$. For a long strip, the trace of a large power of $\mathbf M$ is dominated by its biggest eigenvalue.

**Computations (pp. 409–411).** Strips of figure 31.14 (rectangular and triangular), $H=0$, $J=\pm1$, free energy per spin for $W=2,\dots,8$. Only $\mu_{\max}$ is needed. Iterative multiplication of the matrix by an initial vector is one way to get it. Because $\mathbf M$ is all positive, its principal eigenvector is all positive (Frobenius–Perron theorem), so $(1,\dots,1)$ is a reasonable start vector. This may be faster than computing all eigenvalues. The author computed all eigenvalues anyway, which also gives finite-length strips via (31.32) (p. 410).

Results (pp. 410–411):
- At high temperature all Ising models should show the same behaviour: entropy per spin is $\ln2$, mean energy per spin goes to 0, and free energy per spin tends to $-\ln(2)/\beta$ (p. 410).
- As $T\to0$ the Boltzmann distribution concentrates on the ground states. A degenerate ground state gives non-zero entropy at $T\to0$, found from $S=-\partial F/\partial T$ (pp. 410–411).
- The triangular antiferromagnet's entropy at absolute zero appears to be about 0.3, about half its high-temperature value (figure 31.16) (p. 411). Mean energy uses $\langle E\rangle=-\partial\ln Z/\partial\beta$ (p. 411).
- Heat capacity (raw derivatives of mean energy) and energy variance are in figures 31.18–31.19. Roughness is due to inaccurate numerics. The graphs seem compatible with the ferromagnet having, and the antiferromagnet not having, a phase transition (p. 411).
- Free-energy picture (p. 411): each ferromagnetic phase has a simple free energy, a sloping straight line through $F=0,T=0$ at high temperature and a horizontal line at low temperature. The slope gives the phase's entropy per spin. The transition occurs roughly where the lines intersect, so the transition temperature is predicted to be linearly related to the ground-state energy. (added step) With lines $F=E_0$ and $F=-T\ln2$ the crossing is at $T=-E_0/\ln2$, which is linear in $E_0$.

**Comparison with Monte Carlo (p. 412).** The author says the agreement between the two sets of results seems very good. The systems are not quite identical (long strip vs periodic square). A more accurate comparison would find all eigenvalues $\lambda$ for width $W$ and compute $\sum\lambda^W$ to get the partition function of a $W\times W$ patch (p. 412).

### 31.3 Exercises (p. 412)
See "Exercises worth doing".

## Toy example (ours, not from the text)
A ring of $C=2$ spins, coupling $J=1$, $\beta=1$, $H=0$. We use a one-row version of the strip (no vertical bonds), so $\mathcal E(s,s')=-Jxx'$ replaces (31.28).

*Transfer matrix.* Rows and columns are states $s\in\{+,-\}$: $\mathbf M=\begin{pmatrix}e&e^{-1}\\e^{-1}&e\end{pmatrix}=\begin{pmatrix}2.71828&0.36788\\0.36788&2.71828\end{pmatrix}$. Its eigenvalues are $e+e^{-1}=3.08616$ and $e-e^{-1}=2.35040$. By (31.32), $Z=3.08616^2+2.35040^2=9.52438+5.52438=15.0488$.

*Direct check.* The ring has two bonds, so $E=-2x_1x_2$. States $++,--$ have $E=-2$ and weight $e^2=7.38906$ each. States $+-,-+$ have $E=+2$ and weight $e^{-2}=0.13534$ each. $Z=2(7.38906)+2(0.13534)=15.0488$ ✓.

*Fluctuation check of (31.11).* $P(E=-2)=14.77811/15.04878=0.98201$ and $P(E=+2)=0.01799$. $\bar E=-2(0.98201)+2(0.01799)=-1.92806$. $\langle E^2\rangle=4$. $\mathrm{var}(E)=4-1.92806^2=4-3.71744=0.28256$. So $C=k_B\beta^2\mathrm{var}(E)\approx0.283$. Cross-check with $Z=4\cosh2\beta$: $\partial^2\ln Z/\partial\beta^2=4\,\mathrm{sech}^2(2)=4(1-0.96403^2)=0.2826$ ✓.

*Large strips.* Using (31.34) with $W=1$, long ring: $f=-\ln3.08616=-1.127$ per spin.

## Concepts
- [[ising-model]] (new) — array of ±1 spins with neighbour couplings $J$ and field $H$; energy (31.1) (p. 400)
- [[exponential-family-gibbs-distribution]] — Boltzmann law $P\propto\exp[-\beta E]$ over spin states (31.2) (p. 400)
- [[partition-function]] (new) — $Z=\sum_{\mathbf x}e^{-\beta E}$; derivatives of $\ln Z$ give mean energy and variance (pp. 400–401)
- [[heat-capacity-fluctuation-relation]] (new) — $C=k_B\beta^2\mathrm{var}(E)$ (31.11) (p. 401)
- [[entropy-h-x]] — here called $S=\sum p\ln(1/p)$ and tied to $\ln Z$ and free energy (Ex. 31.1) (p. 402)
- [[gibbs-sampling]] — update one spin from its conditional (31.17), local field $b_n$ (p. 402)
- [[metropolis-hastings]] — flip spin, accept with (31.20) (p. 402)
- [[schottky-anomaly]] (new) — heat-capacity peak of a finite-level system, with no fluctuation peak (p. 404)
- [[frustration]] (new) — couplings that cannot all be satisfied, e.g. an antiferromagnetic triangle (p. 406)
- [[ground-state-degeneracy]] (new) — several lowest-energy states, so non-zero entropy as $T\to0$ (pp. 410–411)
- [[transfer-matrix-method]] (new) — $Z=\mathrm{Trace}[\mathbf M^C]\to\mu_{\max}^C$ for a strip (p. 409)
- [[phase-transition]] (new) — a 'collective phenomenon'; true phase transitions only for infinite $N$, hinted at by relatively bigger fluctuations at intermediate temperature (p. 403)

## Canonical instances
- [[rectangular-ising-monte-carlo]] — rectangular lattice; for $J=1$ the energy fluctuations peak near the transition (figure 31.5), and $J=-1$ is expected to be equivalent for even sizes (pp. 403–406)
- [[triangular-antiferromagnet]] — frustrated lattice; no fluctuation peak ($N=4096$), entropy appears to be about 0.3 at $T\to0$ (pp. 406–407, 411)
- [[two-level-system]] — simplest Schottky anomaly, eqs. 31.22–31.24 (p. 404)
- [[thin-strip-transfer-matrix]] — widths $W=2$–8, largest eigenvalue gives $f$ (pp. 409–411)

## Bridges (candidates)
- [same-math] $\mathrm{var}(E)=\partial^2\ln Z/\partial\beta^2$ ↔ information-theory: variance of the sufficient statistic as the second derivative of the log-partition function in an exponential family — same derivative identity.
- [same-math] Ising energy (31.4) with free $J_{mn},h_n$ ↔ neural networks: Hopfield/Boltzmann machine energy (named on p. 400).
- [structural-analogy] Transfer-matrix column sweep ↔ bayesian: sum–product message passing on a chain (author says "similar", p. 407).
- [same-math] Gibbs-sampling update (31.17) ↔ bayesian: Gibbs sampling from a full conditional.
- [structural-analogy] Entropy of antiferromagnetic Ising ↔ information-theory: capacity of a 2D constrained channel (author says equivalent, p. 399).

## Questions this raises
- How does one decide that Monte Carlo has reached equilibrium? The author defers this to Chapter 32 (p. 403).
- What is the best way to extract entropy and heat capacity from simulation or from $Z$ (Ex. 31.2)?
- Which couplings $J_{mn}$ make a given list of states into local energy minima (Ex. 31.3)?
- Can we predict a transition temperature quantitatively from the free-energy lines (p. 411)?

## Exercises worth doing
- Ex. 31.1 (p. 402) — derive $S=\ln Z+\beta\bar E$ and $S=-\partial F/\partial T$; links entropy, free energy and $Z$ — difficulty: easy
- Ex. 31.2 (p. 412) — design estimators of entropy (Monte Carlo) and entropy plus heat capacity (partition function) — difficulty: hard
- Ex. 31.3 (p. 412) — choose $J_{mn}$ so that a given list of states are low-energy minima — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 411 = p. 399).
- The text layer is garbled for equations (31.22–31.24, 31.28) and for figure axis labels; I used the page images for them.
- Eq. 31.25 writes $Z(\beta,\mathbf J,\mathbf b)$ and $E(\mathbf x;\mathbf J,\mathbf b)$, with $\mathbf b$ for the field, while earlier sections use $H$ or $h$; $b_n$ also denotes the local field (31.18).
- The main text (p. 409) says the factors $\tfrac14$ are needed because vertical links are "counted four times"; the figure 31.13 caption explains them as half-inside times visited twice.
- Section 31.2 ends with a sentence missing a verb: "One could a more accurate comparison…" (p. 412).
- The extracted text of the sentence about "ΣW λ" is garbled; the intended meaning is $\sum\lambda^W$.
- Figure 31.18 shows small negative heat-capacity values; the author attributes roughness to inaccurate numerics (p. 411).
- The 0.3 entropy value is the author's approximate estimate ("appears to be about 0.3", p. 411, figure 31.16), not an exact number.
- Eq. 31.12 as printed gives $C^{(\beta)}=\partial\bar E/\partial\beta=\mathrm{var}(E)$, whereas (31.8)–(31.9) give $\partial\bar E/\partial\beta=-\mathrm{var}(E)$; the sign is taken as printed (p. 402).

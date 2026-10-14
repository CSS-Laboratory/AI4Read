---
id: betancourt-2017-hmc/main-p3
work: betancourt-2017-hmc
unit: "paper (part 3/3): Sections 5.3–8 and Appendix A"
pages: 41–60
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Tuning, Robustness and Implementation Details of Hamiltonian Monte Carlo (end of the paper)

## L0 — One line
Hamiltonian Monte Carlo can be tuned using the geometry of its integrator, many of its failures show up as measurable diagnostics (divergences: unstable numerical trajectories; low E-BFMI: energy transitions much narrower than the overall energy spread), and a valid sampler needs trajectories chosen reversibly and states drawn with weights proportional to $e^{-H}$.

## L1 — The gist (≤ 120 words)
This part asks how to set the integrator, how far to trust Hamiltonian Monte Carlo (HMC), and how it is implemented exactly. The author links step size to acceptance probability through modified (shadow) energy level sets. He treats the question of for which targets HMC is geometrically ergodic (and gives well-behaved, unbiased estimators) as the robustness question. Heavy tails (flagged, for a poor kinetic energy, by low E-BFMI) and high curvature (flagged by divergences) obstruct it. Both diagnostics are necessary but not sufficient for validity. The appendix proves that, when trajectories are chosen reversibly, sampling a state with weights $\propto e^{-H}$ preserves the target (canonical) distribution. It builds efficient progressive and dynamic samplers and derives the generalized No-U-Turn stopping rule.

**Prerequisites:** Markov chain invariance; Metropolis–Hastings; Hamiltonian $H(q,p)$, energy level sets, symplectic integrators (earlier parts of the paper); indicator functions; basic probability sums.

## L2 — Key ideas
- Symplectic integrators solve a modified Hamiltonian exactly, so their quality can be judged by comparing modified and exact level sets; divergences appear when modified level sets become non-compact (p. 41).
- For simple static HMC, the cost–acceptance relationship is bounded, which motivates tuning step size to an average Metropolis acceptance of 0.6–0.8 (p. 41).
- Heavy tails obstruct geometric ergodicity, and a poorly chosen kinetic energy can make the marginal energy distribution heavy-tailed; this is diagnosed by comparing the energy transition and marginal energy densities, and an E-BFMI (energy mismatch ratio) below 0.3 has empirically proven problematic (p. 44).
- Divergent trajectories flag high-curvature neighborhoods; persistent divergences call for regularizing the target, not just smaller steps (p. 45).
- Both diagnostics are necessary, not sufficient, for estimator validity; the author says HMC is especially robust when they are combined with split $\hat R$ over multiple parallel chains (pp. 45–46).
- Drawing a state with probability $\propto e^{-H}$ from a trajectory, after reversibly chosen trajectories, leaves $\pi\propto e^{-H}$ invariant (pp. 49–50).
- Progressive sampling builds trajectory and sample together with little memory; multiplicative (doubling) expansion makes reversibility checks cheap (pp. 51, 55).
- The No-U-Turn criterion generalizes to Riemannian manifolds via $\rho$ and $p^\sharp$ (p. 58).

## L3 — Walkthrough

### 5.2 (end) and 5.3 Optimal choice of symplectic integrator
**Static scheme, completed (p. 41).** Choose a numerical trajectory $\mathfrak t$ of length $L$ containing the initial point. Then sample a point from it with probability
$$\pi(q,p)=\frac{e^{-H(q,p)}}{\sum_{(q',p')\in\mathfrak t}e^{-H(q',p')}}.$$
Proofs are in Appendix A (p. 41).

**5.3.** An integrator is set by a step size $\epsilon$ and an order $K$, the number of gradient evaluations per step (p. 41).
- Step size sets the number of steps $L=T/\epsilon$, so smaller $\epsilon$ means more accuracy but more cost. Higher order is likewise more accurate and more expensive (p. 41).
- Volume preservation implies numerical trajectories solve exactly a modified (shadow) Hamiltonian $\tilde H$. They stay on its level sets, so performance can be studied by comparing exact and modified level sets (Fig. 32a) (p. 41).
- Divergences occur when modified level sets become non-compact and reach the boundaries of phase space (Fig. 32b) (p. 41).
- When there are no divergences, comparing the level-set shapes bounds the cost against the average Metropolis–Hastings acceptance probability. This is shown for the simple version: integrate for static time $T$, flip momentum, apply an MH correction (Fig. 33) (pp. 41, 43).
- The bounds support automated step-size adaptation during warm-up to an average acceptance between 0.6 and 0.8. The author says more work is needed to formalize this for more sophisticated implementations (pp. 41, 43).
- Most treatments use the first-order leapfrog integrator. Recent work suggests higher-order integrators may be more effective, especially in higher dimensions. Their extra degrees of freedom can, if poorly chosen, completely neutralize the gains over leapfrog, so automated adaptation is needed (p. 43).

*Intuition note:* A symplectic integrator is not exact, but it is exact for a slightly different energy function. If that nearby energy has the same kind of level sets, the trajectory is stable; if not, it blows up. Comparing the exact and nearby level sets lets us quantify integrator performance and tune the step size.

### 6 Robustness
The question is for which targets an HMC implementation is geometrically ergodic and gives well-behaved, unbiased MCMC estimators (pp. 43–44). Analysis is hard. Preliminary results (Livingstone et al., 2016) say even simple HMC is geometrically ergodic over a large class of targets, significantly larger than the class for non-gradient algorithms such as Random Walk Metropolis (p. 44). The analysis also identifies obstructing pathologies, each with an empirical signature that suggests a diagnostic (p. 44).

**6.1 Poorly chosen kinetic energies (p. 44).**
- Heavy tails push the typical set far into parameter space, so a chain needs long sojourns to the tails and back. Dynamic integration times help, but may be insufficient (p. 44).
- If the kinetic energy is poorly chosen, the marginal energy distribution can itself be heavy-tailed. Exploration between level sets is then so slow that after any finite number of transitions it is incomplete (p. 44).
- Diagnosis: plot the marginal energy density $\pi_E$ and the energy transition density $\pi(E\mid q)$ from the chain (Fig. 34). If the transition density is much narrower than the marginal, the tails may not be fully explored (p. 45).
- The mismatch is summarized by the energy Bayesian fraction of missing information:
$$\text{E-BFMI}\equiv\frac{\mathbb E_\pi\!\left[\mathrm{Var}_{\pi_{E|q}}[E\mid q]\right]}{\mathrm{Var}_{\pi_E}[E]}\approx\widehat{\text{E-BFMI}}\equiv\frac{\sum_{n=1}^{N}(E_n-E_{n-1})^2}{\sum_{n=0}^{N}(E_n-\bar E)^2}.$$
- Empirically, values below 0.3 have proven problematic; the exact threshold needs more theory (p. 44).

**6.2 High curvature (pp. 44–45).**
- Neighborhoods of large curvature are hard for most Markov transitions, including HMC. They cause incomplete exploration and bias. They are characteristic of hierarchical models (p. 45).
- Symplectic integrators become unstable and diverge in these neighborhoods (Fig. 35), so divergences are sensitive identifiers (p. 45).
- Any divergent transition should prompt suspicion of the estimators. Mild pathologies can be removed by decreasing the step size (p. 45).
- If divergences persist however small the step, the author says this indicates significant bias. The target then needs regularizing, e.g. stronger priors or another representation, such as alternating centered and non-centered parameterizations in latent Gaussian models (p. 45).

**6.3 Limits (pp. 45–46).** These two diagnostics are "only necessary and not sufficient conditions" for validity (p. 45). Subtler pathologies may exist. Still, the author says these diagnostics make HMC a uniquely robust method, especially when combined with generic diagnostics such as split $\hat R$ over multiple parallel chains (p. 46).

*Intuition note:* The sampler's own warning signs (divergences, energy mismatch) point to real problems (high curvature in the target, an ill-suited kinetic energy). Silence from these checks does not prove the output is right.

### 7 Conclusion; 8 Acknowledgements
HMC exploits the geometry of the typical set, giving coherent exploration of smooth targets, better efficiency than other MCMC algorithms, and stronger validity guarantees. Geometry also supports automatic tuning (p. 46). Future directions: improved ergodicity analysis, refined implementations, non-Gaussian and non-Euclidean kinetic energies. Differential geometry may extend the ideas to other problems, as in Adiabatic Monte Carlo, and possibly to discrete, tree and Hilbert spaces (p. 47). Section 8 lists thanks and funding; not summarized.

### Appendix A: Technical details
**Setting (p. 47).** HMC alternates between exploring an energy level set and resampling momenta (a random walk over energies). Exact trajectories are energy-preserving and typically ergodic: a uniform sample from an ergodic trajectory converges to the microcanonical distribution. Since exact trajectories are rarely available, symplectic integrators are used and their errors are corrected probabilistically (pp. 47–48).

**A.1 Notation (p. 48).** $z=(q,p)$. $z_n$ is the point after $n$ forward steps and $z_{-n}$ after $n$ backward steps. For $L=3$: $\{z_0,z_1,z_2\}$, $\{z_{-1},z_0,z_1\}$, $\{z_{-2},z_{-1},z_0\}$. $\mathfrak T^L_z$ is the set of length-$L$ trajectories containing $z$, and $\mathfrak T^L_{z,z'}=\mathfrak T^L_z\cap\mathfrak T^L_{z'}$.

**A.2 Static implementations.**
- Uniform sampling from a numerical trajectory does not give the canonical distribution; sampling with weights $\propto$ canonical density corrects it exactly (p. 48).
- First sample a trajectory, then a state: $\mathbb T(z'\mid z)=\sum_{\mathfrak t}\mathbb T(z'\mid\mathfrak t)\,\mathbb T(\mathfrak t\mid z)$ (p. 48).
- A.2.1 requires reversibility: $\mathbb T(\mathfrak t\mid z)=\mathbb T(\mathfrak t\mid z')$ for $\mathfrak t\in\mathfrak T^L_{z,z'}$. This implies $\mathbb I(z'\in\mathfrak t)\mathbb T(\mathfrak t\mid z)=\mathbb I(z\in\mathfrak t)\mathbb T(\mathfrak t\mid z')$. It is easily met with $\mathbb T(\mathfrak t\mid z)=U(\mathfrak T^L_z)$, since then $\mathbb T(\mathfrak t\mid z)=L^{-1}$ whenever $\mathfrak T^L_{z,z'}\ne\emptyset$ (p. 49).
- A.2.2: state sampling
$$\mathbb T(z'\mid\mathfrak t)=\frac{\pi(z')}{\sum_{z''\in\mathfrak t}\pi(z'')}\mathbb I(z'\in\mathfrak t)=\frac{e^{-H(z')}}{\sum_{z''\in\mathfrak t}e^{-H(z'')}}\mathbb I(z'\in\mathfrak t).\tag{1}$$
  For an exact integrator this would be uniform; in practice numerical error makes it disfavor higher energies. Options are a slice sampler (auxiliary $u\sim U(0,\pi(z))$, then uniform over states with $\pi(z')>u$) or a direct multinomial draw. The author says Rao–Blackwell implies the multinomial, having no auxiliary variables, performs better (p. 49).
- A.2.3 invariance of $\pi(z)\propto e^{-H(z)}$ (p. 50). Steps:
  1. Expand the transition: $\sum_z\mathbb T(z'|z)\pi(z)=\sum_z\sum_{\mathfrak t}\mathbb T(z'|\mathfrak t)\mathbb T(\mathfrak t|z)\pi(z)$.
  2. Insert (1).
  3. Swap with the reversibility identity: $\mathbb I(z'\in\mathfrak t)\mathbb T(\mathfrak t|z)\to\mathbb I(z\in\mathfrak t)\mathbb T(\mathfrak t|z')$.
  4. Move the sum over $z$ inside: $\sum_z\mathbb I(z\in\mathfrak t)\pi(z)=\sum_{z\in\mathfrak t}\pi(z)$.
  5. This cancels the denominator, leaving $\pi(z')\sum_{\mathfrak t}\mathbb T(\mathfrak t|z')=\pi(z')$.

*Intuition note:* Choosing trajectories "symmetrically" (a window is equally likely seen from any of its points), then picking a point by its density weight, leaves the target distribution unchanged.

**A.3 Efficient static implementations (p. 50).** Storing all $L$ states is costly, so sampling is woven into trajectory construction.

*A.3.1 Uniform progressive sampling (pp. 50–51).* Append $\mathfrak t_{\text{new}}$ (integrating randomly forward or backward) to $\mathfrak t_{\text{old}}$. Given $z_{\text{old}}\sim\mathbb T(z'|\mathfrak t_{\text{old}})$ and $z_{\text{new}}\sim\mathbb T(z'|\mathfrak t_{\text{new}})$, take $z_{\text{old}}$ with probability $p_{\text{old}}=w_{\text{old}}/(w_{\text{old}}+w_{\text{new}})$, where $w=\sum_{z\in\mathfrak t}\pi(z)$ per component (Fig. 36). Then
$$\mathbb T(z'|\mathfrak t)=p_{\text{old}}\mathbb T(z'|\mathfrak t_{\text{old}})+(1-p_{\text{old}})\mathbb T(z'|\mathfrak t_{\text{new}})=\frac{w_{\text{old}}}{w_{\text{old}}+w_{\text{new}}}\mathbb T(z'|\mathfrak t_{\text{old}})+\frac{w_{\text{new}}}{w_{\text{old}}+w_{\text{new}}}\mathbb T(z'|\mathfrak t_{\text{new}}).\tag{2}$$
Proof: insert (1) for each component; the factors $w$ cancel, leaving $\frac{\pi(z')}{\sum_{z''\in\mathfrak t}\pi(z'')}[\mathbb I(z'\in\mathfrak t_{\text{old}})+\mathbb I(z'\in\mathfrak t_{\text{new}})]=\mathbb T(z'|\mathfrak t)$ (p. 51).
- Additive expansion (one step at a time) yields $\mathfrak t\sim U(\mathfrak T^{L+1}_z)$. It coincides with Neal's windowed sampler when the window equals the trajectory length (p. 51).
- Multiplicative (doubling) expansion yields $U(\mathfrak T^{2L}_z)$. Old and new components are leaves of perfect ordered binary trees (Fig. 37), so new components are built recursively, propagating the sample with (2) (Fig. 38; text p. 51).

*A.3.2 Biased progressive sampling (p. 54).* To introduce anti-correlation (which can potentially improve performance), use
$$\mathbb T(z'|\mathfrak t)=\min\!\left(1,\tfrac{w_{\text{new}}}{w_{\text{old}}}\right)\mathbb T(z'|\mathfrak t_{\text{new}})+\left(1-\min\!\left(1,\tfrac{w_{\text{new}}}{w_{\text{old}}}\right)\right)\mathbb T(z'|\mathfrak t_{\text{old}}).$$
This favors the new component, pushing away from the initial state. Averaged over initial states in $\mathfrak t$, the repulsions cancel and $\sum_z\mathbb T(z'|z)\pi(z)\mathbb I(z\in\mathfrak t)=\pi(z')\mathbb I(z'\in\mathfrak t)$. The proof splits $z$ into old and new parts, uses the swapped-role version for starts in the new component, and inserts (1). The $\min$ terms pair up to sum to 1 for each component. *Skip path:* carry forward only that the biased scheme preserves $\pi$ on the trajectory.

**A.4 Dynamic implementations (p. 55).** Different level sets need different integration times, so a termination criterion is used: build an initial trajectory, test, expand and repeat until the criterion is met.

*A.4.1 Maintaining reversibility (pp. 55–56).* A naive dynamic scheme can break $\mathbb T(\mathfrak t|z)=\mathbb T(\mathfrak t|z')$. Starting elsewhere, expansion may terminate prematurely, making $\mathbb T(\mathfrak t|z)=0$ for some starts but not others (Fig. 39). The fix is to reject expansions containing sub-trajectories that satisfy the criterion.
- Additive: check sub-trajectories from every old state to the single new state, which is linear per expansion and quadratic overall (Fig. 40a).
- Multiplicative: check only binary sub-trees of the new trajectory, at logarithmic cost in the old size and total cost quadratic in the log of final length. Checks can run during construction, so a bad new trajectory can be rejected early (Fig. 40b) (p. 55–56).

*A.4.2 Termination criteria (pp. 56–58).* The aim is to avoid integrating too short or too long. The No-U-Turn sampler's heuristic (Hoffman and Gelman, 2014) uses only the boundaries $z_\pm(\mathfrak t)$ (Fig. 41). On Euclidean space it terminates when
$$p_+(\mathfrak t)^T\cdot(q_+(\mathfrak t)-q_-(\mathfrak t))<0\quad\text{AND}\quad p_-(\mathfrak t)^T\cdot(q_-(\mathfrak t)-q_+(\mathfrak t))<0.\tag{3}$$
- It is satisfied only when the end momenta are anti-aligned along the line joining the ends, so further integration would typically bring the ends together. Stopping at that point typically explores about half the level set, which the author says can be too aggressive but works well empirically (Fig. 42, p. 57).
- It needs subtraction of points, so it is defined only on Euclidean manifolds. Generalization: on a Euclidean manifold $q_+-q_-=\int_{t=0}^{T(\mathfrak t)}dt\,M^{-1}p(t)$, so $p_+^T\cdot(q_+-q_-)=p_+^\sharp(\mathfrak t)^T\cdot\rho(\mathfrak t)$ with $p^\sharp\equiv M^{-1}p$ and $\rho\equiv\int_0^{T(\mathfrak t)}dt\,p(t)$. The criterion becomes
$$p_+^\sharp(\mathfrak t)^T\cdot\rho(\mathfrak t)<0\quad\text{AND}\quad p_-^\sharp(\mathfrak t)^T\cdot\rho(\mathfrak t)<0,$$
  as printed (p. 58). The text omits the sign steps for the second term; see Reading notes.
- This form is defined on any Riemannian manifold. In practice $\rho(\mathfrak t)\approx\sum_{z\in\mathfrak t}p(z)$, which gives almost identical results because symplectic integrators are accurate (p. 58).
- Exhaustions use the virial instead and need no Riemannian structure. They add a tuning parameter strongly affecting performance. Hand-tuned, they can beat the No-U-Turn criterion, but they need automated tuning first (p. 58).

**A.5 NUTS and Stan (pp. 58–59).** The original No-U-Turn sampler is a dynamic HMC: No-U-Turn criterion, multiplicative expansion, slice sampling of states. Each new component uses uniform progressive sampling, but the sample update when appending it uses biased progressive sampling. Stan, first built on it, now uses the generalized criterion and multinomial instead of slice sampling, which the author says significantly improves performance (p. 59).

## Toy example (ours, not from the text)
Trajectory of four states with unnormalized densities $\pi(z_0..z_3)=4,2,1,1$ (these are $e^{-H}$ values). Normalizer $=8$, so the target weights are $\tfrac12,\tfrac14,\tfrac18,\tfrac18$.

*Uniform progressive sampling.* Old $=\{z_0,z_1\}$, $w_{\text{old}}=6$. New $=\{z_2,z_3\}$, $w_{\text{new}}=2$. $p_{\text{old}}=6/8=3/4$. Inside old: $z_0$ gets $4/6$ and $z_1$ gets $2/6$. Inside new: $\tfrac12$ each.
- $P(z_0)=\tfrac34\cdot\tfrac46=\tfrac12$
- $P(z_1)=\tfrac34\cdot\tfrac26=\tfrac14$
- $P(z_2)=P(z_3)=\tfrac14\cdot\tfrac12=\tfrac18$

These match the direct weights.

*Biased version.* Start in old (probability mass $6/8$): move to new with $\min(1,2/6)=1/3$, so stay with $2/3$. Start in new (mass $2/8$): move to old with $\min(1,6/2)=1$. Probability of ending at $z_0$: $\tfrac68\cdot\tfrac23\cdot\tfrac46+\tfrac28\cdot1\cdot\tfrac46=\tfrac{24}{72}+\tfrac{8}{48}=\tfrac13+\tfrac16=\tfrac12$ ✓. Probability of $z_2$: $\tfrac68\cdot\tfrac13\cdot\tfrac12=\tfrac18$ ✓. The biased scheme also preserves the target.

## Concepts
- [[hamiltonian-monte-carlo]] — HMC/NUTS: MCMC that follows Hamiltonian trajectories, then corrects with weighted state sampling (pp. 41, 47)
- [[symplectic-integrator]] (new) — volume-preserving numerical integrator that exactly solves a modified Hamiltonian (p. 41)
- [[shadow-hamiltonian]] (new) — modified Hamiltonian $\tilde H$ whose level sets the numerical trajectory stays on (pp. 41–42)
- [[geometric-ergodicity]] (new) — property of target + sampler needed for well-behaved, unbiased MCMC estimators (pp. 43–44)
- [[e-bfmi]] (new) — ratio of mean conditional energy variance to marginal energy variance; values below 0.3 have empirically proven problematic (p. 44)
- [[convergence-diagnostics]] — divergences and E-BFMI as HMC-specific checks, with split $\hat R$ generic (pp. 44–46)
- [[typical-set]] — where mass concentrates; heavy tails push it into extremes (p. 44)
- [[metropolis-hastings]] — correction used in the simple static scheme; target acceptance 0.6–0.8 (p. 41)
- [[progressive-sampling]] (new) — sampling a state while building the trajectory by mixing components with weights $w$ (pp. 50–51)
- [[trajectory-reversibility-condition]] (new) — $\mathbb T(\mathfrak t|z)=\mathbb T(\mathfrak t|z')$ needed for invariance (p. 49)
- [[no-u-turn-criterion]] (new) — stops when boundary momenta anti-align with the end-to-end direction (p. 57)

## Canonical instances
- [[stan]] — implementation using generalized No-U-Turn criterion and multinomial sampling (p. 59)
- [[hierarchical-model-curvature]] — high-curvature neighborhoods characteristic of hierarchical models; centered/non-centered switch (p. 45)
- [[random-walk-metropolis]] — non-gradient method with a smaller geometrically ergodic class than HMC (p. 44)

## Bridges (candidates)
- [same-math] Multinomial draw with weights $\propto e^{-H}$ ↔ Gibbs/Boltzmann sampling: same normalized-exponential weights over a finite set.
- [structural-analogy] Progressive pairwise mixing with $w_{\text{old}}/(w_{\text{old}}+w_{\text{new}})$ ↔ reservoir/weighted streaming sampling: one pass, constant memory.
- [structural-analogy] Divergences as model-geometry warnings ↔ Bayesian workflow: diagnostics prompting reparameterization.

## Questions this raises
- Why do the cost–acceptance bounds yield 0.6–0.8 and how do they change for dynamic trajectories?
- What exactly is the E-BFMI threshold, and how does it depend on the kinetic energy?
- Does the biased progressive scheme improve performance, and by how much?
- Are there pathologies that escape both diagnostics?

## Reading notes
- This part starts mid-way through the section before 5.3 (printed p. 41; the heading of that section is not shown on these pages) and ends with the reference list (p. 60). Printed numbers equal pdf numbers.
- Misprints seen in the images: p. 58 "from the negative boundary, $z_+(\mathfrak t)$" should read $z_-(\mathfrak t)$; $\rho$'s lower limit is printed "$t=0(\mathfrak t)$"; "exhalations" for exhaustions; "effects" for affects (p. 58).
- Sign issue (p. 58): taking the printed relation $q_+-q_-=\int M^{-1}p\,dt$ and $M$ symmetric (added assumption), the second term of (3) becomes $-p_-^{\sharp T}\rho<0$, i.e. $p_-^\sharp\cdot\rho>0$. The page prints "$<0$" for both terms. The text says only "being careful with the signs"; the convention is not explained here.
- In the biased-sampling derivation (p. 54) $\mathbb T(z'|\mathfrak t_{\text{old}})$ and $\mathbb T(z'|\mathfrak t_{\text{new}})$ are overloaded: they denote the transition started from that component, with roles swapped for the new component. Reference list duplicates arXiv number 1410.5110 for two entries.

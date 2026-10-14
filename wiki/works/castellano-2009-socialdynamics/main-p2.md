---
id: castellano-2009-socialdynamics/main-p2
work: castellano-2009-socialdynamics
unit: "paper (part 2/3): end of III.F.2 (Deffuant) through III.G–H, IV, V, VI.A–B and the start of VI.C"
pages: 20–39
fields: [complex-systems]
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
# Castellano, Fortunato & Loreto (2009), part 2: Hegselmann–Krause, other opinion models, cultural, language and crowd dynamics

## L0 — One line
Simple local interaction rules (copy, compromise, align, imitate) produce collective outcomes such as consensus, frozen diversity or ordered motion, and the switch between them is often a phase-transition-like threshold in a control parameter (uncertainty, number of traits, noise).

## L1 — The gist (≤ 120 words)
This part finishes the survey of bounded-confidence opinion models (Hegselmann–Krause) and other opinion models, then reviews cultural dynamics (the Axelrod model and its variants), language dynamics (evolutionary language games, the Naming Game, language competition) and the start of crowd behavior (flocking, pedestrians, panic, applause). The question throughout: how do simple local rules of interaction create global order, fragmentation or transitions? Often the answers are phase-transition-like: thresholds in uncertainty, number of traits or noise separate consensus from diversity. Some of these models are compared with data (elections, language extinction), which makes them testable.

**Prerequisites:** mean-field rate equations; fixed points and their stability; order parameter and phase transition; Ising/XY spin models; basic network types (lattice, small-world, scale-free); log-normal and power-law distributions; matrices as probability tables.

## L2 — Key ideas (5–10 bullets)
- **Hegselmann–Krause (HK)** differs from Deffuant only in the update: an agent averages over *all* its compatible neighbours at once. It gives the same stationary pattern, and its consensus threshold depends on whether the mean degree $\langle k\rangle$ (average number of neighbours) stays finite (ε_c = 1/2) or diverges (ε_c ∼ 0.2) (pp. 20–21).
- **Empirical elections:** the vote share ν of a candidate has a 1/ν central part in several datasets; in open-list proportional elections, P(v,Q,N) collapses onto one log-normal function of vQ/N (a shape whose logarithm is normally distributed) across countries and years (pp. 22–23).
- **Axelrod model:** social influence (interacting people become more similar) plus homophily (similar people interact more) give, on regular lattices, a transition in the number of traits q between consensus and a frozen multicultural state. It is fragile to cultural drift: for any noise rate, large systems end up disordered (pp. 24–26).
- **Evolutionary language game:** payoff = communicative success = fitness. It can be cast as quasispecies equations (evolution equations for self-replicating types, with mutation), and without mutation as the replicator equations of evolutionary game theory (pp. 28–30).
- **Naming Game:** a population with empty inventories spontaneously reaches consensus, a symmetry-breaking transition (one of many equivalent words is spontaneously selected); convergence time scales as $N^{1.5}$ on the complete graph, and the controlled two-word case, Eq. (36), predicts, in the absence of fluctuations, that the larger group wins (pp. 30–32).
- **Language competition:** the Abrams–Strogatz rate equation predicts extinction of one language; bilingualism (or intervention) can allow survival; the Schulze model gives roughly log-normal language sizes in its no-dominant-language phase (pp. 34–35).
- **Vicsek self-propelled particles:** a non-equilibrium ordering transition (moving particles that align with neighbours, plus noise) exists in 2D, where the equilibrium XY model (spins that tend to align) does not order; continuum theories were proposed to explain it (pp. 36–37).
- **Social force model:** a Newtonian equation with personal, repulsive and noise forces reproduces lanes; related models of driven particles and escaping crowds give noise-induced jamming ("freezing by heating") and "faster is slower" (pp. 38–39).

## L3 — Walkthrough

### III.F.2 (end). Deffuant model: clusters, topology, variants
- **Cluster masses.** The masses $m_i$ of the clusters obey $\sum_i m_i = M_0$ and $\sum_i m_i x_i = 0$; the second condition follows from conservation of the average opinion. Numerical solutions of Eq. (29) show only three cluster types: major (mass > 1), minor (mass < $10^{-2}$) and a central cluster at x = 0. They arise from a periodic sequence of bifurcations, in which clusters nucleate and annihilate (p. 20).
- **Any topology.** The stationary state has one or more clusters. Restricting interaction to topological neighbours gives more clusters at low uncertainty. Agents in geometrically separated clusters do not communicate, so even compatible clusters will in general end with different opinions (increased fragmentation) (p. 20).
- **Scale-free networks.** For fixed ε, the number of surviving opinions is proportional to N. Poorly connected nodes have a sizeable probability of being excluded from the dynamics and keeping their opinion forever. This holds for static and evolving networks (p. 20).
- **Discretized Deffuant** (Q integer opinions). Opinions $s_i\neq s_j$ are compatible if $|s_i-s_j|\le L$. The rules are those of Eqs. (27)–(28), with the shift rounded to the nearest integer. For $L\to\infty$, $Q\to\infty$ with $\epsilon=L/Q$ fixed, the continuous results are recovered. For L = 1 on a complete graph: consensus is the only stationary state if Q = 2; for Q > 2 complete consensus is never attained and there are at least two clusters. On scale-free networks the number of surviving opinions is a scaling function of Q and N (p. 20). Footnote 2: for L = 1 the two interacting opinions cannot shift towards each other (only integer values are allowed), so one agent takes the opinion of the other.
- **Variants** (reported, not derived): individual ε values, where agents with large uncertainty dominate; uncertainties that evolve and are coupled to opinions, which can let initially minority extremal positions come to dominate; Deffuant plus spontaneous opinion changes, modelled as diffusion in opinion space, in which large clusters steadily overtake small ones (Ben-Naim); periodic external perturbation as propaganda; coevolving mutual affinity, which determines cluster number and positions endogenously (p. 20).

### III.F.3. Hegselmann–Krause (HK) model
- Opinions are real numbers in, say, [0,1]. Agent i interacts with neighbours whose opinions lie in $[x_i-\epsilon,\,x_i+\epsilon]$. Unlike Deffuant, it interacts with *all* compatible neighbours at once. The authors say Deffuant suits small-group (pair) meetings in large populations, whereas HK suits formal meetings with many people at once (p. 20).
- Update rule on a graph with adjacency matrix $a_{ij}$ (agent i takes the average opinion of its compatible neighbours; ε is the only parameter, with no μ) (p. 20):

$$x_i(t+1)=\frac{\sum_{j:|x_i(t)-x_j(t)|<\epsilon} a_{ij}\,x_j(t)}{\sum_{j:|x_i(t)-x_j(t)|<\epsilon} a_{ij}}\tag{31}$$

- Group averages make simulations lengthy, which "may explain" why few authors have studied HK (p. 20).
- **Results.** Same pattern of stationary states as Deffuant; the number of final clusters decreases as ε increases; above a threshold $\epsilon_c$ there is one cluster. On a complete graph the final configurations are symmetric about 1/2, because the average opinion is conserved. The time to reach the stationary state diverges at the cluster-bifurcation thresholds, because of isolated agents between consecutive clusters (p. 21).
- **Consensus threshold.** $\epsilon_c$ can take only one of two values, depending on how $\langle k\rangle$ behaves as N grows. If $\langle k\rangle$ stays constant (e.g. lattices): $\epsilon_c=\epsilon_1=1/2$. If $\langle k\rangle\to\infty$ (e.g. complete graphs): $\epsilon_c=\epsilon_2\sim0.2$. For Deffuant, $\epsilon_c=1/2$ on any graph (p. 21).
- **Discretized HK** is essentially a voter model with bounded confidence: an agent picks the opinion of a random compatible neighbour. With three opinion values and uncertainty one, it reduces to the constrained voter model. Other developments are listed: alternative averaging, damage spreading, group sizes from 2 to N, Markov-chain reformulation, stability and order-preservation results (p. 21).

*Intuition note.* In HK, an agent averages over its whole compatible group. A single cluster (consensus) appears only above a threshold uncertainty $\epsilon_c$, and that threshold depends on whether each agent's number of neighbours keeps growing with the population.

### III.G. Other opinion models (all as reported by the authors)
- Basic models are essentially deterministic. Most recent models treat randomness as important, since individual attitudes, peer influence and external factors (mass media, propaganda) are hard to predict (p. 21).
- **Jiang et al.**: Ising-like dynamics with the Metropolis flip probability $\exp(-\Delta E/T)$ (T = social temperature). When the majority of neighbours disagrees with an agent, it flips with probability q (this accounts for agents keeping their opinion despite social pressure, "inflexible agents"); q = 1 is usual Ising. For q < 1, detailed balance is violated (non-equilibrium). On the lattice the ferromagnetic transition is continuous for $q>q_c$ and discontinuous for $q<q_c$; the continuous-transition exponents differ from both mean-field and Ising. On small-world lattices with many shortcuts there is no magnetization transition if q is low enough (p. 21).
- **Bartolozzi et al.**: binary opinions, heat-bath dynamics. The field combines, with random weights, the neighbours' mean opinion and the whole-network mean opinion. When noise exceeds a threshold the average opinion shows large intermittent fluctuations; compared with the Dow-Jones series, similarities are "striking" (p. 21).
- **Kuperman–Zanette**: majority-rule imitation, fashion (external modulation) and noise. Stochastic resonance occurs: a suitable amount of noise strongly amplifies the response to the modulation. At fixed noise, an optimal population size does the same (system-size stochastic resonance) (p. 21).
- Others: kinetic models with a diffusion term, reformulated as Fokker–Planck equations (Toscani; de la Lama et al.); internal opinion (a probability) versus external binary action, where agents deep inside a cluster are extremists and those at its boundary are open-minded (Martins); a Kuramoto variant with unbounded real phases showing an anarchy→consensus transition; reformulation in game theory; hub influence overestimated, since the effective coupling between two agents should shrink with their degrees, and with such renormalized couplings the Ising model on scale-free networks always has a ferromagnetic threshold, while uniform couplings give magnetization at any temperature when degree variance is infinite; hierarchy, fashion, taste, surveys; a naming-game variant for opinions (pp. 21–22).

### III.H. Empirical data
- The authors argue that physics should add a quantitative phenomenology of opinion dynamics that constrains models; large datasets and computers now make this possible (p. 22).
- **Elections, distribution of vote fraction ν** (histogram P(ν)). Brazilian 1998 data: central part $\sim 1/\nu$ with an exponential cutoff at large ν; state-deputy datasets are analogous; 2002 data confirm it. Indian data show a similar pattern across states, with discrepancies. Indonesian data are consistent with a power law of exponent near one but too noisy. Mexican claims are not clearly supported (p. 22).
- Interpretation by Costa Filho et al.: a multiplicative process gives a log-normal ν by the Central Limit Theorem. The 1/ν behavior can be reproduced by a log-normal in the limit of large variance (pp. 22–23).
- **Sznajd-based microscopic model** (Bernardes et al.): Barabási–Albert contact graph, candidates are the initial nodes with a definite opinion, and modified Sznajd dynamics spreads their opinions. It reproduces the Brazilian curve, also on other graphs. *Weakness:* the non-trivial distribution is only transient; at long times every voter picks the same candidate (a δ-function), so studies stopped at a chosen time. A simple opinion-spreading model fits on Erdős–Rényi graphs but fails on scale-free ones (p. 23).
- **Universality doubted for the 1/ν region:** the authors say it is unlikely, since candidates' scores depend on party performance; municipal data show a different pattern (p. 23).
- **Open-list proportional elections** (Fortunato–Castellano): v = votes of a candidate, Q = candidates on the party list, N = votes of the list. $P(v,Q,N)$ is a scaling function of the single variable $vQ/N$, log-normal in shape and the same across countries and years (Fig. 7: Italy, Poland, Finland). A word-of-mouth model reproduces it (p. 23).
- **Random Field Ising Model (RFIM) at T = 0** (Michard–Bouchaud) for extreme events (fashions, crashes, panic). Opinions are binary; attitudes are real random fields; public information is a global field F(t) slowly increasing; interaction is a sum of Ising couplings. Order parameter O = average opinion. As F increases, O changes sharply because large groups switch together. The speed $dO/dF$ versus F follows a universal bell-shaped curve with peak height h and width w related by $h\sim w^{-2/3}$. This relation was observed in data on birth-rate drops, mobile-phone diffusion and the end of applause (Fig. 8) (pp. 23–24).

*Intuition note.* When a quantity is a function of a single rescaled variable (here $vQ/N$) for many countries, the details of each country do not matter. That is why a simple microscopic model can be tested against it.

### IV. Cultural dynamics, A. Axelrod model
- By the authors' convention, opinion is a scalar; culture is a vector of variables whose dynamics are coupled. They call this distinction "largely arbitrary" (p. 24).
- **Ingredients:** social influence (interacting individuals become more similar) and homophily (similar individuals interact more). Social scientists expected a convergence to one culture; the model predicts persistence of diversity in some cases (p. 24).
- **Definition.** Each individual has F integer "cultural features" $(\sigma_1,\dots,\sigma_F)$, each taking one of q "traits", $\sigma_f=0,\dots,q-1$. In an elementary step, neighbours i, j are chosen and their overlap is computed (p. 24):

$$\omega_{i,j}=\frac1F\sum_{f=1}^{F}\delta_{\sigma_f(i),\sigma_f(j)}\tag{32}$$

  With probability $\omega_{i,j}$ they interact: one feature with different traits is chosen and the neighbour's trait is set equal to $\sigma_f(i)$. Otherwise nothing happens. A pair is stable if exactly equal or completely different (p. 24).
- **Absorbing states** on any finite system: $q^F$ ordered states (all identical) or more numerous frozen multicultural states. Which class is reached depends on q (Castellano et al., 2000): small q gives quick full consensus; large q gives few interactions and small frozen domains. On regular lattices a phase transition at $q_c$ (dependent on F) separates them (pp. 24–25, Fig. 9).
- **Order parameters:** $\langle S_{max}\rangle/N$ (largest cultural region; finite in the ordered phase, $\sim1/N$ in the disordered one) and $g=\langle N_g\rangle/N$ (number of domains; $g\to0$ ordered, finite disordered) (p. 25).
- **Transition type:** in 2D, continuous for F = 2, discontinuous for F > 2 (footnote 3: "continuous" is a slight abuse because q is discrete). The domain-size distribution at the transition is $P(s)\sim s^{-\tau}$ with $\tau\approx1.6$ (<2) for F = 2 and $\tau\approx2.6$ (>2) for F > 2. In 1D the transition is continuous for all F (p. 25).
- **Competition:** an interaction always raises the overlap of the pair by 1/F, but may make the changed individual more dissimilar to its other neighbours. So with more than two neighbours an interaction can increase overall disorder. This underlies the non-monotonic density of active links (overlap neither 0 nor 1) below but near $q_c$ (Fig. 10; the freezing-time inset has slope 2 in L) (p. 25).
- **Mean field.** Rate equations for the densities $P_m$ of bonds with m equal and F−m different features. Order parameter $n_a=\sum_{m=1}^{F-1}P_m$ (zero in the disordered phase, finite in the ordered phase, as stated). It gives a discontinuous transition for any F. For F = 2 it can be studied analytically: the approach to the steady state has a timescale diverging as $|q-q_c|^{-1/2}$. For F = 2, q = 2 a mapping to the constrained voter model is given (pp. 25–26).

*Intuition note.* Interaction is possible only when two neighbours already share something (and still differ somewhere). With many possible traits, few pairs share anything, so the system freezes before it can agree.

### IV.B. Variants of the Axelrod model
- **Cultural drift** (spontaneous trait change at rate r, i.e. noise). With noise the model shows a noise-induced order–disorder transition, practically independent of q (Fig. 11, effective rate $r'=r(1-1/q)$). For small noise the state is monocultural, because disordered states are unstable to perturbations. For large noise, new domains form as fast as old ones vanish. The threshold satisfies $r_cT(N)=O(1)$, with T(N) the mean relaxation time of a perturbation. Approximately $T=N\ln N$ in d = 2 (agrees with simulations), and $T\sim N^2$ in 1D. Since T diverges with N, for any q the system stays disordered in the thermodynamic limit, however small the drift rate (p. 26).
- Modifications using the local majority trait (Kuperman; Flache–Macy) were proposed to keep a transition under noise; a convincing illustration that they are robust to at least weak noise "is still lacking" (p. 26).
- **Overlap threshold θ** (no interaction below θ): no qualitative change, only a smaller ordered region. **Interaction noise** (below the threshold, interaction occurs with probability δ): favours ordering, no drastic change (p. 26).
- **Topology.** Small-world graphs (Watts–Strogatz, WS): the transition persists, with $q_c$ growing with the rewiring parameter p; this is consistent with mean-field results since p = 1 is a random network. Barabási–Albert (BA) scale-free graphs: for each N there is a smeared transition with bistability (first-order signature), but $q_c\sim N^{0.39}$, so in the thermodynamic limit only ordered states remain. This is similar to the Ising model on scale-free networks (p. 26).
- **Mass media** as fixed external message $M=(\mu_1,\dots,\mu_F)$, with probability B the individual interacts with M as with a neighbour. "Rather unexpectedly", the field favours the multicultural phase: $q_c(B)$ decreases, and for $B>B^*$ with $q_c(B^*)=0$ only the disordered phase exists. A strong field aligns some individuals but decouples those far from it. Global or local non-uniform coupling gives similar conclusions. For $q>q_c(B=0)$ a vanishing field leads to an ordered monocultural state, so the limit B → 0 is discontinuous. Indirect feedback (accepting a trait change not matching the majority only with probability R) behaves the same (pp. 26–27).
- **Metric features:** the overlap contribution of a feature is $[1-\Delta\sigma_f/(q-1)]/F$. This resembles vectorial Deffuant and favours consensus, since only maximal difference forbids interaction (the authors note no systematic investigation was done) (p. 27).

### IV.C. Other multidimensional models
- Deffuant et al. (2000) vectorial binary version: like Axelrod with q = 2, but the interaction probability is a step function of overlap at a bounded-confidence threshold d. Mean field gives consensus for large threshold and fragmentation for small d. Laguna et al.: each differing variable becomes equal with probability μ; a consensus–fragmentation transition exists, with properties depending on μ = 1 versus μ < 1 (p. 27).
- Two-dimensional HK (square opinion space, square or circular confidence ranges, homogeneous mixing): no drastic change; consensus threshold practically the same; positions of coexisting clusters are set by the shape of the opinion space. Lorenz: consensus is easier in a simplex (components sum to one) than in a hypercube (p. 27).

### V. Language dynamics: framing
- Language dynamics covers the emergence, change, evolution, interaction and extinction of languages. Models are roughly sociobiological or sociocultural; the authors compare this to nature versus nurture (p. 27).
- **Sociobiological:** good communicators leave more offspring; communication strategies are innate (nativist spirit) and genetically transmitted, so a better one displaces rivals; "strategy" has a model-dependent meaning (pp. 27–28).
- **Sociocultural:** language is a complex dynamical system continuously reshaped by its users. Good strategies give only better communication, not reproductive success; innovation arises from agents' inventiveness (p. 28).
- **Evolutionary game theory framework (V.A):** under the sociobiological view natural selection is the fundamental driving force. Classical strategies are replaced by inherited traits (genetic or cultural), the search for Nash equilibria becomes the search for evolutionarily stable strategies, and the payoff is interpreted as fitness (p. 28).

### V.A.1. Evolutionary language game (ELG)
- **Setup.** n objects, m words. An individual has a production matrix P ($n\times m$, $p_{ij}$ = probability of using word j for object i) and a comprehension matrix Q ($m\times n$, $q_{ji}$ = probability a hearer associates sound j with object i), with $\sum_{j=1}^m p_{ij}=1$ and $\sum_{i=1}^n q_{ji}=1$. The pair (P, Q) is a language L (p. 28).
- Speaker $I_1$ conveys to hearer $I_2$ with ability $\sum_{i}\sum_{j}p^{(1)}_{ij}q^{(2)}_{ji}$. The symmetrized form is the payoff (p. 28):

$$F(L_1,L_2)=\frac12\sum_{i=1}^{n}\sum_{j=1}^{m}\bigl(p^{(1)}_{ij}q^{(2)}_{ji}+p^{(2)}_{ij}q^{(1)}_{ji}\bigr)\tag{33}$$

- **Maximum payoff.** P and Q need not be correlated a priori. The best payoff is obtained with P binary having at least one 1 in every column (if n ≥ m) or every row (if n ≤ m), and Q binary with $q_{ji}=1$ if $p_{ij}$ is the largest entry of a column of P. For n = m: P has one 1 per row and column, and Q is its transpose. In general $F_{max}=\min\{m,n\}$. Uncorrelated P, Q can lead to pathological situations (Komarova–Niyogi use one matrix) (pp. 28–29).
- **Simulation.** N individuals with random languages $L_1,\dots,L_N$. Individual k gets $F_k=\sum_{l\ne k}F(L_k,L_l)$ and has an offspring with probability $f_k=F_k/\sum_lF_l$ (constant population size). The offspring learns from its parent by building an association matrix A ($a_{ij}$ counts observations of the parent pairing object i with signal j in K samplings) (p. 29):

$$p_{ij}=a_{ij}\Big/\sum_{l=1}^{m}a_{il},\qquad q_{ji}=a_{ji}\Big/\sum_{l=1}^{m}a_{lj}\tag{34}$$

  For $K\to\infty$, $A=P$. For finite K, learning is incomplete, which triggers mutations. What is inherited is a language-specific learning mechanism (nativist spirit), not the language itself (p. 29).
- **Outcome.** The population converges to a common language, not necessarily optimal: it can get stuck in sub-optimal absorbing states with synonymy (several signals for one object) or homonymy (one signal for several objects). Dependence on N and K has not been systematically analysed; the model so far uses a fully connected topology, and exploring other topologies is described as of interest (p. 29).
- **Errors.** With probability $u_{ij}$ of mistaking signal i for j, the maximum payoff falls (**linguistic error limit**): the number of distinguishable signals in a protolanguage, hence of describable objects, is limited, and adding signals does not raise the capacity. Combining signals into words allows unlimited objects; then the fitness can overcome the error limit, increasing exponentially with word length. The authors present this as one possible way evolution selected syntax/grammar (p. 29).

### V.A.2. Quasispecies-like approach
- Take binary $n\times m$ lexical matrices $A_k$, with $M=2^{nm}$ possible. $x_k$ = fraction of individuals with $A_k$, $\sum_{k=1}^M x_k=1$ (p. 29):

$$\dot x_k=\sum_l f_l\,x_l\,Q_{lk}-\phi\,x_k,\qquad l=1,\dots,M=2^{nm}\tag{35}$$

  Here $f_l=\sum_kF(A_l,A_k)x_k$ ($x_k$ = probability of speaking with an individual k), $\phi=\sum_lf_lx_l$ (average fitness), $Q_{lk}$ = probability that a learner from an individual with $A_l$ ends up with $A_k$. The $-\phi x_k$ term keeps the population size constant (p. 30).
- Eq. (35) is a particular case of the quasispecies equations (Eigen). With no mutation ($Q_{ij}=0$ for $i\ne j$) one recovers the replicator equations of evolutionary game theory, equivalent to the Lotka–Volterra equations in $M-1$ dimensions (p. 30).

*Intuition note.* The second term subtracts the average growth rate so that fractions still add up to one. Mutation (off-diagonal Q) is what separates the language game from plain replicator dynamics.

### V.B. Semiotic dynamics; V.B.1. The Naming Game (NG)
- Semiotic dynamics treats language as an evolving system. The NG was conceived to study self-organization in language evolution (Steels). Agents with private random vocabularies are forced to align through conversations, so a shared vocabulary emerges from local adjustments; conversations are special cases of language games (p. 30). Ke et al. studied an imitation model (random or majority-following imitation) and a probabilistic vocabulary representation with production and comprehension matrices that, unlike in the ELG, are dynamically transformed (p. 30).
- **Minimal NG** (Baronchelli et al.): N agents on a fully connected network bootstrap a name for one object. Each has an inventory of known word–object associations, empty at t = 0. At each step two random agents play speaker and hearer. Failure: the hearer lacks the word, so adds it to his inventory. Success: both erase their inventories except the winning word (Fig. 12) (p. 30).
- **Macroscopic analysis.** Quantities: total words $N_w(t)$, different words $N_d(t)$, success rate $S(t)$ (Fig. 13). After a transient, the system spontaneously goes to a global consensus (a word invented during the run takes over). It is a symmetry-breaking, disorder–order transition. In the final absorbing state $N_w=N$, $N_d=1$, $S=1$ (p. 30–31).
- **Scaling** (time = number of binary interactions): $t_{max}\sim N^\alpha$, $t_{conv}\sim N^\beta$, $N_w^{max}\sim N^\gamma$, $t_{diff}=t_{conv}-t_{max}\sim N^\delta$, with $\alpha=\beta=\gamma=\delta=1.5$ (with a subtle feature near the transition, where an additional timescale emerges); simple scaling arguments account for these (p. 31).

### V.B.2. Symmetry breaking: a controlled case
- Two words A, B; fractions $n_A$ (only A), $n_B$ (only B), $n_{AB}$ (both). Mean-field equations (p. 31):

$$\begin{aligned}\dot n_A&=-n_An_B+n_{AB}^2+n_An_{AB}\\ \dot n_B&=-n_An_B+n_{AB}^2+n_Bn_{AB}\\ \dot n_{AB}&=+2n_An_B-2n_{AB}^2-(n_A+n_B)n_{AB}\end{aligned}\tag{36}$$

- Three fixed points. If $n_A(0)>n_B(0)$ the end state is the stable $n_A=1$ (and $n_B=n_{AB}=0$); symmetrically for $n_B(0)>n_A(0)$. From $n_A(0)=n_B(0)$ the text states the equations lead to $n_A=n_B=2n_{AB}=0.4$, which is unstable: any perturbation drives the system to one stable point (see Reading notes on this value) (p. 31).
- Eq. (36) also describes two populations that converged separately to two conventions: the larger imposes its convention, even for a tiny difference (no fluctuations): B dominates if $n_B(0)=0.5+\epsilon$, $n_A(0)=0.5-\epsilon$, $n_{AB}(0)=0$, for any $0<\epsilon\le0.5$. In simulations, the success probability of the minority convention decreases with N, going to zero as $N\to\infty$ (p. 31).
- The same structure describes language competition (Abrams–Strogatz variants with bilinguals; Minett–Wang). The **AB-model** (Castelló et al.), a voter model with bilinguals, is on a complete graph and for infinite N described by equations identical to (36) up to a constant factor in the timescale (p. 32).

*Intuition note.* Without fluctuations, Eq. (36) lets the larger side win however small its lead; in simulations, which include fluctuations, the minority's chance of success decreases with N and goes to zero as $N\to\infty$ (p. 31).

### V.B.3. Role of interaction topology
- On heterogeneous graphs, the order of picking speaker and hearer matters. Variants: *direct* NG (random speaker picks a neighbour as hearer), *reverse* NG (random hearer picks speaker), *neutral* (pick an edge, roles assigned with equal probability) (p. 32).
- **Low-dimensional lattices:** consensus via coarsening (competition among homogeneous clusters driven by interface curvature). A convergence-time scaling $O(N^{1+1/d})$ is conjectured (d ≤ 4). Slower than the fully connected graph but with lower memory use; similar for the AB-model (p. 32).
- **Small-world** (rewiring p): for $t<t_{cross}=O(N/p^2)$, ordinary coarsening while clusters are one-dimensional (typical size < 1/p); later, mean-field-like behaviour. Convergence time is expected to scale as $N^{3/2}$, not $N^3$ (d = 1). Advantage over both extremes: finite memory per node (versus $O(N^{1/2})$ fully connected) and much faster convergence than finite dimensions. For the AB-model on a 2D small world: coarsening, then fast decay to A or B caused by a finite-size fluctuation (Fig. 14: lifetime $\tau\sim p^{-0.76}$) (p. 32).
- **Complex networks:** $t_{conv}\sim N^\beta$, $\beta\simeq1.4\pm0.1$ for both Erdős–Rényi and Barabási–Albert graphs; the scaling laws are described as robust against further topological details (p. 32).

### V.C. Other models
- NG with an "irresolute" parameter β (β = 1 is the NG): in a successful interaction both update their memory with probability β. It has a non-equilibrium transition from absorbing consensus to an *active* (not frozen) stationary state of polarization or fragmentation. The transition persists on heterogeneous networks, unlike Axelrod where it vanishes (p. 33).
- Also mentioned: hybrid vertical/horizontal transmission (Ke et al.), evolutionary NG, utterance selection model, Iterated Learning Model (mappings from meanings to signals passed between generations; compositionality results) (p. 33).

### V.D. Language competition
- About 6,500 languages exist, mostly with few speakers; "up to 90%" might disappear by the end of the 21st century (an estimate cited). The histogram of language sizes (Fig. 15; 6142 languages) resembles a log-normal. The authors stress that it may not be a stable feature of language diversity, and that it may be a consequence of pure demographic growth (Zanette) (p. 33).
- Models are macroscopic (differential equations) or microscopic (simulations) (pp. 33–34).

**V.D.1. Macroscopic models.**
- **Abrams–Strogatz (AS):** languages A, B with speaker fraction x and status s for A (B has $1-x$ and $1-s$); languages do not evolve; attractiveness grows with speakers and status (p. 34):

$$\frac{dx}{dt}=c(1-x)x^{a}s-c\,x(1-x)^{a}(1-s)\tag{37}$$

  The two terms are the rates of switching B→A and A→B (c can be absorbed in the time unit, footnote 6). Stable fixed points are x = 0 and x = 1; a third, at x = 1/2, s = 1/2, is unstable. So the model predicts one language dominates (initial majority and/or higher status) and the other goes extinct. It reproduces the decline of speakers of several endangered languages (Fig. 16). It is minimal and neglects bilingual speakers (p. 34).
- **Mira–Paredes:** bilinguals added; parameter k measures language similarity. For $k>k_{min}(a,s)$ the steady state has monolinguals coexisting with bilinguals; monolinguals of the endangered language disappear, but the language survives via bilingualism if A and B are similar enough (Galician/Castilian data). **Minett–Wang:** adds adult–adult and adult–child transmission; same extinction scenario unless intervention when speakers fall below a threshold (raising status; monolingual education of children) (p. 34).
- **Patriarca–Leppänen:** reaction–diffusion version with two regions: both languages survive, concentrated where favoured. **Pinasco–Romanelli:** with population dynamics of the two communities, generalized Lotka–Volterra equations give a non-trivial fixed point (coexistence) when the endangered speakers' growth rate compensates the conversion rate (pp. 34–35).

**V.D.2. Microscopic models.**
- Language as F features with Q values each (F typically 8–64); Q = 2 gives bit-strings (p. 35).
- **Schulze model:** per individual, with probability p a random feature changes: with probability q to the value of a random individual's feature, otherwise a random value; with probability $(1-x)^2r$ an agent switches to a language spoken by fraction x. Sharp transition between one dominant language (low p) and no dominant language (high p), the latter with roughly log-normal sizes. Languages have no intrinsic fitness, so dominance comes from initial fluctuations. Variants: aging/reproduction, movement on a lattice, bilinguals, a flight-stopping threshold, language families via bit-string similarity (p. 35).
- **de Oliveira et al.:** colonization of a square lattice from the centre; free sites occupied with probability proportional to the population's language size (fitness); mutation probability inversely proportional to fitness; reproduces language-size distribution, better with a fitness upper bound or bit-string languages (p. 35).
- Others: Social Impact Theory (majority pressure, Nettle), language mixing with fitness gain from learning the other's words (Kosmidis), lattice model with aging and bilinguals who forget the locally minority language (Schwämmle) (p. 35).

### VI. Crowd behavior: A. Flocking
- Local interactions determine global collective motion; the authors consider it plausible that an individual has a clear perception only of its neighbourhood, ignoring what most peers do (p. 36).
- **Vicsek model (self-propelled particles, SPP).** N particles with constant speed $v_0$ on a periodic square. Each takes the average direction of the particles in a neighbourhood S(i), plus noise (p. 36):

$$\theta_i(t+\Delta t)=\langle\theta(t)\rangle_{S(i)}+\xi\tag{38}$$

  with ξ uniform in $[-\eta/2,\eta/2]$. It resembles the XY model (velocities as spins, noise as temperature). For $v_0\to0$ it resembles diluted XY ferromagnets; for $v_0\ne0$ it is non-equilibrium with transport (p. 36).
- Order parameter, magnitude of the average velocity, with noise η as control parameter (p. 36):

$$\Phi=\frac1N\Bigl|\sum_j\mathbf v_j\Bigr|\tag{39}$$

$$\Phi(\eta)\sim\begin{cases}\Bigl[\dfrac{\eta_c(\rho)-\eta}{\eta_c(\rho)}\Bigr]^{\beta}&\eta<\eta_c(\rho)\\[2mm]0&\eta>\eta_c(\rho)\end{cases}\tag{40}$$

  This is a continuous kinetic transition breaking rotational symmetry (Fig. 17). Fluctuations of the order parameter diverge at the threshold. Numerically $\beta=0.42\pm0.03$ (mean-field value 1/2) and $\eta_c(\rho)\sim\rho^\kappa$ with $\kappa=0.45\pm0.05$. This differs from diluted ferromagnets, where the critical density tends to the finite percolation threshold as the temperature goes to zero; here it vanishes as η → 0. Results hold for any non-vanishing $v_0$ (p. 36).
- **Surprise in 2D:** the equilibrium XY model does not order (Kosterlitz–Thouless vortices; Mermin–Wagner). In SPP, vortices form early (for $v_0\approx0$) but are unstable and disappear. The kinetic transition is attributed to the non-equilibrium character (pp. 36–37).
- **1D:** the rule is modified (particles change direction after slowing down); same type of transition with $\beta=0.60\pm0.05$, $\kappa\approx1/4$. **3D:** collective motion with mean-field-consistent exponents, for any density, whereas the static model cannot order below the percolation threshold ($\rho_{perc}\approx1$) (p. 37).
- **Continuum theory (Toner–Tu)** for velocity and density fields, built to preserve rotational symmetry (p. 37):

$$\begin{aligned}\partial_t\mathbf v+(\mathbf v\nabla)\mathbf v&=\alpha\mathbf v-\beta|\mathbf v|^2\mathbf v-\nabla P+D_L\nabla(\nabla\mathbf v)+D_1\nabla^2\mathbf v+D_2(\mathbf v\nabla)^2\mathbf v+\boldsymbol\xi\\ \partial_t\rho+\nabla(\rho\mathbf v)&=0\end{aligned}\tag{41}$$

  (P: pressure analogue; α, β symmetry-breaking coefficients, β here is not the exponent; $D_{L,1,2}$ diffusion constants; ξ Gaussian noise). Galilean invariance is broken because momentum is not conserved; the second equation is mass conservation. Dynamic renormalization group: the system orders in 2D, and above four dimensions it behaves as the equilibrium model. It predicts no transition in 1D, contrary to numerics (p. 37).
- **1D continuum theory** from the master equation, with velocity field U(x,t), self-propulsion f(U), noise ζ (p. 37):

$$\partial_tU=f(U)+\mu^2\partial_x^2U+\alpha\frac{(\partial_xU)(\partial_x\rho)}{\rho}+\zeta,\qquad \partial_t\rho=-v_0\partial_x(\rho U)+D\partial_x^2\rho\tag{42}$$

  The non-linear term is crucial. Linear stability analysis shows an ordered phase at sufficiently low noise because domain walls between counter-moving groups are unstable. Numerics show the same universality class as the discrete 1D model (p. 37).

*Intuition note.* The Vicsek model is a non-equilibrium model whose particles keep moving. The authors attribute the order found in 2D to this intrinsic dynamical, non-equilibrium character (p. 37), whereas the equilibrium XY model does not order in 2D.

### VI.B. Pedestrian behavior
- Henderson compared pedestrian flows to gases/fluids (Navier–Stokes). Realistic macroscopic models would need collision avoidance (energy and momentum not conserved) and the "granular" nature of crowds, so microscopic models are favoured: cellular automata (CA) and the social force model (p. 37).
- **CA:** discretized cells, empty or occupied by one agent or an obstacle; motion is a biased random walk with the bias given by a field on cells (like chemotaxis). Efficient, but space discretization constrains flow directions, so continuous-space models are likelier to succeed (p. 37).
- **Social force model** (Helbing): behavioural change is driven by social forces. Equation of motion (p. 38):

$$m_i\frac{d\mathbf v_i}{dt}=\mathbf F_i^{(pers)}+\mathbf F_i^{(soc)}+\xi_i(t)\tag{43}$$

$$\mathbf F_i^{(pers)}=m_i\,\frac{\mathbf v_i^{(0)}-\mathbf v_i}{\tau_i}\tag{44}$$

$$\mathbf F_{ij}^{(rep)}=A_i\exp\!\Bigl(\frac{r_{ij}-d_{ij}}{B_i}\Bigr)\mathbf n_{ij}\tag{45}$$

  Here $\mathbf v^{(0)}$ is the desired velocity, $\tau_i$ the reaction time, $A_i$, $B_i$ strength and range constants, $r_{ij}$ the sum of the disk radii, $d_{ij}$ the distance between centres, $\mathbf n_{ij}$ the unit vector from j to i. $\mathbf F^{(soc)}$ is a sum of interactions with other pedestrians (repulsive, possibly attractive) and with barriers (often the same repulsive form with the distance to the nearest wall point); ξ is unpredictable individual behaviour (p. 38).
- **Emergent phenomena:** ordered lanes (reducing collision risk) and alternating streams through a narrow door, though agents are not told to do this. Counter-moving pedestrians shift aside, small same-direction groups form, are stable, and attract others (p. 38).
- **Freezing by heating** (Helbing et al., 2000b): particles driven in opposite directions in a periodic 2D strip jam into crystallized configurations if noise exceeds a critical threshold. The crystallized state has higher energy than the flowing disordered state, hence is metastable. This may explain jams in great collective excitation such as panic (p. 38).
- **Escape panic** (adapted model): extra forces for body compression and tangential motion. Observed phenomena: intermittent clogging of a narrow exit (bursts of escapees, also seen in mice); "faster is slower" (escape time is minimal at an optimal individual speed); columns near exits can improve the situation. **Smoky room** (exits visible only nearby): with a panic parameter weighing independent action against herding (alignment term as in Vicsek), optimal survival chances come with a mix of personal initiative and herding (pp. 38–39, Fig. 18).
- **Mobility patterns:** bank-note dispersal (Brockmann et al.): travel distances decay algebraically, reproduced by a two-parameter continuous-time random walk; inter-event times also follow a power law. Mobile-phone tracking (González et al.): displacements follow a truncated power law, analysed as truncated Lévy flights (p. 39).

### VI.C. Applause dynamics (part ends mid-section)
- Applause is presented as social self-organization: after an uncoordinated phase, the audience often synchronizes clapping. Synchronization examples cited: fireflies, crickets, chemical oscillators, menstrual cycles (p. 39).
- Néda et al. recorded applause after theatre/opera performances (distant and near-spectator microphones). During rhythmic applause the signal becomes periodic and the average intensity decreases (Fig. 19). Spectators start with a high clapping frequency that reduces to about half in the synchronized phase; the text breaks off here (p. 39).

## Toy example (ours, not from the text)
Aim: see why the larger group wins in Eq. (36), using the exact identity below.

*(added step)* Subtract the first two equations of (36): $\dot n_A-\dot n_B=n_{AB}(n_A-n_B)$. With $d=n_A-n_B$ this is $\dot d=n_{AB}\,d$, so $d(t)=d(0)\exp\!\bigl(\int_0^t n_{AB}\,dt'\bigr)$. The sign of d never changes, and |d| grows whenever $n_{AB}>0$.

Numbers: $n_A=0.6$, $n_B=0.4$, $n_{AB}=0$ (sum 1.0); Euler step $\Delta t=0.1$ (a numerical approximation).
- Step 1: $\dot n_A=-0.24+0+0=-0.24$; $\dot n_B=-0.24$; $\dot n_{AB}=2(0.24)-0-0=0.48$. New values: $n_A=0.576$, $n_B=0.376$, $n_{AB}=0.048$ (sum 1.000). d = 0.200.
- Step 2: $n_An_B=0.216576$, $n_{AB}^2=0.002304$, $n_An_{AB}=0.027648$, $n_Bn_{AB}=0.018048$. $\dot n_A=-0.216576+0.002304+0.027648=-0.186624$; $\dot n_B=-0.216576+0.002304+0.018048=-0.196224$; $\dot n_{AB}=0.433152-0.004608-0.045696=0.382848$ (the three sum to 0). New values: $n_A=0.5573376$, $n_B=0.3563776$, $n_{AB}=0.0862848$. d = 0.2009600, matching $0.2+0.1\times0.048\times0.2=0.20096$.
- Reading: A started ahead and its lead has grown. Mixed agents appear first, then the lead widens. If $n_A(0)=n_B(0)$ then d = 0 forever; the symmetric state is therefore a knife-edge.

## Concepts
- [[voter model / bounded confidence]] — HK: average over all ε-compatible neighbours; discretized HK is a voter model with bounded confidence (pp. 20–21)
- [[mean-field approximation]] — rate equations assuming homogeneous mixing, used for Axelrod bonds and Eq. (36) (pp. 25, 31)
- [[order–disorder transition]] — consensus vs fragmented/frozen states as ε, q, noise or p vary (pp. 21, 24, 33)
- [[homophily and social influence]] — the two Axelrod mechanisms (p. 24)
- [[criticality / phase transition]] — continuous vs discontinuous transitions in Ising-variant, Axelrod and Vicsek models (pp. 21, 25, 36)
- [[universality]] — shared exponents or scaling functions across systems (e.g. $vQ/N$ scaling, $h\sim w^{-2/3}$, SPP universality class) (pp. 23, 37)
- [[small-world network]] — shortcuts give mean-field-like NG and Axelrod behavior (pp. 26, 32)
- [[preferential attachment]] — BA networks as substrate; Axelrod transition disappears at large N there (p. 26)
- [[heavy tail / power law]] — 1/ν vote shares, $P(s)\sim s^{-\tau}$, travel distances (pp. 22, 25, 39)
- [[synchronization]] — Kuramoto-variant consensus; rhythmic applause (pp. 22, 39)
- [[fixed point and stability]] — stable/unstable fixed points in Eqs. (36), (37) (pp. 31, 34)
- [[hysteresis]] — RFIM hysteresis behind the universal $dO/dF$ curve (p. 24)
- [[emergence]] — lanes, collective motion, shared vocabulary arising without being imposed (pp. 30, 36, 38)
- [[agent-based model (ABM)]] — microscopic language and crowd simulations (pp. 35, 37)
- [[axelrod-model]] (new) — vector of F features with q traits; overlap-probability interaction (p. 24)
- [[cultural-drift]] (new) — spontaneous random trait change, noise rate r (p. 26)
- [[absorbing-state]] (new) — state the dynamics cannot leave: ordered or frozen in Axelrod, consensus in the NG (pp. 24, 31)
- [[naming-game]] (new) — agents with word inventories; success keeps only the winning word (p. 30)
- [[symmetry-breaking]] (new) — spontaneous selection of one of equivalent conventions or directions (pp. 30, 36)
- [[quasispecies-replicator-equations]] (new) — Eq. (35); replicator equations when mutation is absent (p. 30)
- [[self-propelled-particles]] (new) — particles with fixed speed aligning to neighbours plus noise (p. 36)
- [[social-force-model]] (new) — Newtonian pedestrian dynamics with personal, repulsive and noise terms (p. 38)
- [[stochastic-resonance]] (new) — optimal noise (or system size) maximizes response to an external modulation (p. 21)
- [[random-field-ising-model]] (new) — T = 0 Ising model with random fields and slowly increasing global field (p. 24)

## Canonical instances
- [[hegselmann-krause-model]] — averaging over all compatible neighbours; $\epsilon_c$ = 1/2 or ∼0.2 (pp. 20–21)
- [[axelrod-model]] — transition in q; fragile to drift (pp. 24–26)
- [[naming-game]] — minimal NG, $N^{1.5}$ scaling, Eq. (36) (pp. 30–32)
- [[abrams-strogatz-model]] — Eq. (37), extinction of one language (p. 34)
- [[schulze-model]] — microscopic language competition, log-normal sizes (p. 35)
- [[vicsek-model]] — SPP, Eqs. (38)–(40) (p. 36)
- [[social-force-model]] — lanes, freezing by heating, faster-is-slower (p. 38)
- [[brazilian-election-vote-distribution]] — 1/ν with cutoff; log-normal $vQ/N$ scaling (pp. 22–23)
- [[evolutionary-language-game]] — payoff Eq. (33), matrices P, Q (p. 28)

## Bridges (candidates)
- [same-math] Eq. (35) with no mutation ↔ evolutionary game theory/ecology: replicator equations, said in the text to be equivalent to Lotka–Volterra in $M-1$ dimensions.
- [same-math] AB-model equations ↔ Naming Game two-word case (Eq. 36): identical up to a time-scale constant (p. 32).
- [structural-analogy] Axelrod freezing at large q ↔ jamming/glassy freezing: both are blocked dynamics with no active moves left.
- [structural-analogy] Naming Game consensus ↔ symmetry breaking in spin systems: one of many equivalent states is selected.
- [structural-analogy] Freezing by heating ↔ noise-induced order in other systems: more noise produces a more ordered (jammed) state.
- [metaphor] Quasispecies equations (RNA/DNA) ↔ language: individuals as replicators of lexical matrices.

## Questions this raises
- Why does the HK consensus threshold depend only on whether $\langle k\rangle$ stays finite, and what happens for slowly growing degree?
- Can an Axelrod-type model be modified so that a multicultural phase survives weak noise in the thermodynamic limit? The text says convincing evidence is lacking.
- Is the log-normal distribution of language sizes a stable structural feature or a demographic by-product, and how could a model be tested against that?
- What kind of non-equilibrium transition are SPP and Naming-Game-with-β, and how do their exponents relate to equilibrium ones?

## Reading notes
- **Part boundaries:** this part starts mid-Sec. III.F.2 (Deffuant model, p. 20, in the middle of the discussion of Eq. 29's cluster masses) and ends in Sec. VI.C (Applause dynamics) at the sentence cut off on p. 39 ("...reduces to approximately a half in the synchro-"). Printed page = pdf page.
- **Fixed point in the text vs Eq. (36) (p. 31):** the text says $n_A=n_B=2n_{AB}=0.4$ at the symmetric point. Check (ours): with $n_A=n_B=a$ and $n_{AB}=c$, $\dot n_A=0$ requires $a^2=c^2+ac$; with a = 0.4, c = 0.2 the right side minus left side gives −0.04 ≠ 0. Solving with $2a+c=1$ gives $c=1/(2+\sqrt5)\approx0.236$, $a\approx0.382$. I report the source's value as printed; it may be a rounding or misprint.
- **Eq. (34) (p. 29):** printed as $q_{ji}=a_{ji}/\sum_{l=1}^m a_{lj}$ with both sums to m, although A is $n\times m$; the index placement and upper limit look inconsistent. I copied it as printed.
- **Jiang et al. variant (p. 21):** the sentence on which agents flip with the Metropolis probability ("surrounded by a majority of neighbors with equal opinion") is ambiguously worded; reported as written.
- **Fig. 8 (p. 23):** the legend lists three fits: birth rate $h\sim w^{-2/3}$, $w^{-0.71}$, and cell phones $w^{-0.62}$; I did not assign them further.
- **Eq. (39):** printed without a $v_0$ normalization; copied as printed. In Eq. (41), β is a coefficient, not the critical exponent β of Eq. (40).
- Footnote 2 (p. 20) and footnotes 3, 4, 6 are reflected above. The text layer was clean; equations were checked against the images. Lengthy lists of citations and the figures' data points are not reproduced.

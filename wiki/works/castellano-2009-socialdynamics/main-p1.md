---
id: castellano-2009-socialdynamics/main-p1
work: castellano-2009-socialdynamics
unit: "paper (part 1/3): Sections I–II and III.A–III.F.2 (through the Deffuant rate equation, Eq. 30)"
pages: 1–19
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Statistical physics of social dynamics (part 1/3): framework, voter, majority-rule, social impact, Sznajd, start of bounded confidence

## L0 — One line
Social dynamics can be studied as order–disorder transitions (consensus vs. fragmentation) produced by simple interacting agents, using Ising-style tools, and the voter, majority-rule, social impact, Sznajd and bounded-confidence models are the first models examined.

## L1 — The gist (≤ 120 words)
How do interactions between simple agents turn initial disagreement into shared opinions, cultures or languages? The review answers by treating "order" as consensus and "disorder" as fragmentation, then borrowing tools from statistical physics: Ising/Potts analogies, coarsening, finite-size effects, network topology, master equations, agent-based simulation. This part introduces these tools and the first opinion models. Voter model (an agent copies a neighbor): in an infinite system, consensus only for d ≤ 2. Majority rule (groups adopt their majority opinion): a threshold decides the winner. Social impact and Sznajd models add group effects. Deffuant adds bounded confidence (agents interact only if opinions are close) with continuous opinions. The authors stress that theory far outweighs empirical validation.

**Prerequisites:** Ising model and temperature; probability and expected values; master equation (gain–loss equation); basic graph theory (degree, clustering); fixed points of one-variable ODEs.

## L2 — Key ideas (5–10 bullets)
- Scope and stance: individuals are treated as adaptive, not rational; communication, not strategy, is the focus. The authors say that in most situations large-scale properties do not depend on microscopic details; only symmetries, dimensionality and conservation laws are relevant (universality), so models may include only the simplest properties of individuals (p. 2–3).
- Order means consensus, polarization means two surviving states, fragmentation means more than two. Social influence (agents becoming more alike) can be seen as a counterpart of ferromagnetic coupling (aligning spins); noise and network topology are raised as factors that may affect the ordering (p. 4).
- Ising paradigm: ordering is tracked with the correlation function $C(r,t)$ and the interface density $n_a$ (fraction of neighbor pairs that disagree); the magnetization (average of the $\pm1$ states) is not a suitable monitor of ordering. Coarsening is the growth of ordered domains; surface tension is the energy cost of interfaces between domains. Finite $N$ matters because social systems are much smaller than physical ones (p. 5).
- Network topology (ER random graph, small-world, Barabási–Albert growth by preferential attachment) changes dynamics. In heterogeneous networks a neighbor is likely to have higher degree, so the order of selecting agents can matter (p. 6–7).
- Voter model: exactly solvable, no surface tension, magnetization conserved on regular lattices; infinite systems reach consensus only for $d\le 2$. Its behavior on networks depends on how the update is defined (p. 9–12).
- Majority rule (mean field, group size 3) has fixed points $0,\tfrac12,1$ and consensus time $\sim\log N$. On lattices in $d>1$ with zero initial magnetization the system may be trapped in metastable (long-lived, non-final) states (p. 13–14).
- Social impact and Sznajd models add group pressure. Sznajd B on a chain is equivalent to a voter dynamics, so it does not respect the social-validation principle that motivated it (p. 14–16).
- Bounded confidence (Deffuant) gives opinion clusters; the cluster number is roughly $1/(2\epsilon)$ and $\epsilon_c=1/2$ for consensus in the cases listed (p. 18–19).

## L3 — Walkthrough

### Abstract and Contents (p. 1)
The review covers opinion, cultural and language dynamics, crowd behavior, hierarchy formation, human dynamics and social spreading. It stresses links to traditional statistical physics and comparison with empirical data (p. 1).

### I. Introduction (p. 2–3)
- **Motivation.** Humans interact with few peers, yet societies show global regularities: disorder-to-order transitions (common language, consensus), scaling and universality. This calls for explaining large-scale regularities as collective effects of relatively simple individuals (p. 2).
- **History.** The authors say that physical modeling of society is in some sense older than statistical modeling of physical phenomena. They cite birth/death rates and crime statistics as spurs to statistics. They list Hobbes, Laplace, Comte, Stuart Mill; they say Maxwell and Boltzmann knew this view and that it probably played a role in their statistical description of gases (p. 2).
- **Main question.** How do interactions between agents create order from initial disorder? Order is consensus, agreement or uniformity; disorder is fragmentation. Without interactions heterogeneity would dominate. Interaction generally (not always) makes people more similar (p. 2).
- **Two levels of difficulty.** Humans are not simple like atoms, so models involve a huge, unwarranted simplification. One difficulty is defining sensible microscopic models; the other is inferring macroscopic behavior from them. The authors say the critique that physicists' models are too simple is most of the time very well grounded, and that it also applies to Schelling's and Axelrod's models (p. 2).
- **Added value of statistical physics.** In most situations, qualitative (even some quantitative) large-scale properties do not depend on microscopic details; only higher-level features such as symmetries, dimensionality or conservation laws are relevant (universality). Comparison with data should test whether real trends are compatible with plausible microscopic models, self-consistent, or in need of extra ingredients (p. 3).
- **Scope.** Individuals are adaptive rather than rational; emphasis on communication rather than strategy. Topics: opinion (III), culture (IV), language (V), crowds (VI), hierarchies (VII), human dynamics (VIII), social spreading (IX), coevolution of states and topology (X). Left out: econophysics, evolutionary theory and evolutionary game theory (except language formation), vehicular traffic, a full treatment of complex networks (networks are only substrates), and epidemics on networks (p. 3).
- **Imbalance.** With the exception of some specific sections, theory greatly exceeds empirical evidence; the authors call this a reflection of the literature, not their choice. Unlike complex networks or econophysics, where data came first, in some of the fields reviewed a profusion of models was justified mainly by vague plausibility arguments. Physicists' contribution to grounding the field in data has been so far "insufficient". The Social Web hints at a change (p. 3).

### II. General framework (p. 3–8)
Opinions, traits, social status and kinematic features are modeled by a small set of variables whose dynamics come from social interactions. The dynamics tends to reduce the variability of the initial state, and this may lead to an ordered state (all share a feature) or to a fragmented one (p. 4).

**Terminology fixed by the authors (p. 4).** *Consensus*: all agents share the same state. *Polarization*: many states possible but only two survive. *Fragmentation*: more than two surviving states.

- **Drive to order.** "Social influence" can be seen as a counterpart of ferromagnetic interaction. Anti-ferromagnetic couplings (pushing toward a different state) also matter in some cases (p. 4).
- **Noise.** Time-independent noise in parameters represents differences between individuals. Time-dependent noise can cause spontaneous transitions. Key question: do fluctuations slow or stop ordering? (p. 4).
- **Topology.** Traditional physics uses lattices or all-to-all interaction (which guarantees that the mean-field approximation is correct; also called homogeneous mixing). The latter is hardly realistic socially (p. 4).
- **Bounded confidence.** Two individuals interact only if not too different. It parallels somewhat the range of interaction, but the distance is in an opinion space, not physical space (p. 4).

#### A. Order and disorder: the Ising paradigm (p. 4–5)
- $N$ spins $s_i=\pm1$ with energy
$$H=-\frac12\sum_{\langle i,j\rangle}s_is_j \tag{1}$$
 (sum over nearest-neighbor pairs). Metropolis dynamics: a single spin flip is accepted with probability $\exp(-\Delta E/k_BT)$ (p. 4).
- Ferromagnetic coupling drives toward all $+$ or all $-$; thermal noise opposes. For $T<T_c$ long-range order; for $T>T_c$ macroscopic disorder. The order parameter is $m=\frac1N\sum_i\langle s_i\rangle$: 0 for $T>T_c$, $m(T)>0$ for $T<T_c$ (p. 5). Above $T_c$ spins are still correlated in finite domains (Fig. 1) (p. 5).
- **Potts model**: each spin takes one of $q$ values, equal neighbors favored; $q=2$ is Ising (p. 5).
- **Ordering dynamics** from a disordered start at $T<T_c$: small domains form, then *coarsening* (domains grow, statistics unchanged when rescaled). This is *dynamic scaling*; the typical domain size $L(t)$ is the only relevant length (p. 5).
- The driving force is *surface tension*: interfaces cost energy and are minimized by straightening them (curvature-driven ordering). Its presence is a consequence of each spin's tendency to align with the majority of its neighbors. When the majority plays no role, ordering changes qualitatively (p. 5).
- **Monitoring order.** Magnetization is unsuitable (insensitive to domain size). Use
$$C(r,t)=\langle s_i(t)s_{i+r}(t)\rangle-\langle s_i(t)\rangle^2,$$
 with an implicit average over $i$; $t$ counts attempted updates per spin. Dynamic scaling: $C(r,t)=L(t)^dF[r/L(t)]$, with $L(t)\sim t^{1/z}$. The exponent $z$ is universal, possibly depending only on qualitative features such as conservation of magnetization or dimensionality; for Glauber/Metropolis $z=2$ in any dimension (p. 5).
- **Interface density** $n_a(t)=N_a(t)/N_p$ ($N_p$ = nearest-neighbor pairs, $N_a$ = pairs in different states): $n_a=1/2$ complete disorder, $n_a=0$ full consensus (p. 5).
- **Finite size.** Phase transitions are rigorously defined only as $N\to\infty$. Social systems are much smaller than physical ones, so finiteness of $N$ must play a crucial role. Studying $N$-dependence still helps find robust features (p. 5).

*Intuition note:* Coarsening is like patches of agreement growing and merging. A rule that follows the majority gives interfaces an energy cost (surface tension), and this cost drives the boundaries to become smooth. Counting disagreeing neighbor pairs ($n_a$) shows progress when total magnetization does not.

#### B. Role of topology (p. 5–7)
- **ER graph**: each pair of the $N$ vertices linked with probability $p$. Degree distribution is binomial (Poisson for large $N$), $\langle k\rangle\simeq Np$. For $p$ of order $1/N$ the graph is sparse and locally tree-like (p. 6).
- **Small-world** (Watts–Strogatz): average distance grows only logarithmically with size, yet many triangles exist. The model introduces a fraction $p$ of random long-range links into an initially regular lattice. Two quantities: path length $L(p)$ (average shortest path) and clustering coefficient $C(p)$ (fraction of the $k(k-1)/2$ possible links between a node's neighbors that exist, averaged over nodes). Small-world networks have high $C(p)$ and low $L(p)$ (p. 6).
- **Barabási–Albert (BA)**: start with $m$ fully connected nodes; each new node links to $m$ older nodes with probability proportional to degree (preferential attachment). Result: $\langle k\rangle=2m$, clustering of order $1/N$, $P(k)\sim k^{-\gamma}$ with $\gamma=3$. Power-law degree distributions with $\gamma\le3$ are called scale-free (p. 6).
- **Real social networks** differ from artificial ones, and from technological/biological networks, in two ways (Newman and Park): positive degree correlation (assortativity; most non-social networks are disassortative) and clustering well above random models (p. 6).
- **Neighbor's degree.** If one picks a random node and then one of its neighbors, the second node is likely to have higher degree; the neighbor's degree distribution is $kP(k)/\langle k\rangle$. For models with binary asymmetric rules (the two chosen agents have different roles) on strongly heterogeneous networks, the order of selection may affect the dynamics. For scale-free degree distributions this may have strong effects, as in the voter model and the Naming Game (p. 6–7).

#### C. Dynamical systems approach (sociodynamics) (p. 7)
- Sociodynamics (Weidlich, Helbing) is a branch of synergetics for social systems. In synergetics one starts from microscopic equations and reduces degrees of freedom. For society microscopic equations are not available, so one identifies macro-variables and builds equations directly from social hypotheses (p. 7).
- One defines transition rates per unit time between configurations. The master equation for $P(m,t)$ over discrete states $m$:
$$\frac{dP(m,t)}{dt}=\sum_{m'}\big[W_{m',m}P(m',t)-W_{m,m'}P(m,t)\big], \tag{2}$$
 where $W_{m,m'}$ is the rate from $m$ to $m'$. First term = gain, second = loss (p. 7).
- Master equations are easy to write but hard to solve: usually highly nonlinear, in general only numerical solutions, and they contain too much information relative to data. Take averages of macro-variables:
$$m_k(t)=\sum_m m_kP(m,t). \tag{3}$$
 Their exact equations need the full $P$. If the distribution stays unimodal and sharply peaked,
$$P(m,t)\simeq P(m(t)), \tag{4}$$
 which gives a closed (approximate) set of coupled differential equations (p. 7).

#### D. Agent-based modeling (p. 7–8)
- Agent-based modeling: build computational agents with properties and simulate them in parallel. It aims at the emergence of macro from micro. Roots: molecular dynamics, Monte Carlo, and von Neumann–Ulam cellular automata (e.g., Conway's Game of Life) (p. 7).
- Lineage: Artificial Intelligence ("actors", then "agents"), Reynolds' individual-based models and artificial life, Epstein–Axtell's Sugarscape (first large-scale agent model). *Brownian agents* (Schweitzer) generalize Brownian particles: active particles with internal states, energy and information, interacting through the environment. Interactions are usually asymmetrical, unlike in physical systems (p. 8).

### III. Opinion dynamics (p. 8–19)

#### A. Introduction (p. 8–9)
- In any mathematical model opinion has to be a variable, or a set of variables (a collection of numbers). Many real issues have few positions, often two. The challenge is to find rules for how these numbers change (p. 8).
- Development has been uncoordinated, with plausible mechanisms turned into rules, often without sociological references. First opinion dynamics by a physicist: Weidlich (1971, sociodynamics). The Ising model entered later (Galam et al.): spin coupling = pairwise interaction, field = cultural majority or propaganda, individual fields = personal preferences. Depending on their strength, consensus or coexistence of the two opinions may result (p. 8–9).
- Models reviewed: voter, majority rule, social impact, Sznajd, bounded confidence, others, empirical data (p. 9).

#### B. Voter model (p. 9–13)

**1. Regular lattices.**
- Rule: each agent has $s=\pm1$; at each step agent $i$ and a neighbor $j$ are picked, and $s_i=s_j$ (imitation). The majority state does not act directly (pressure only in an average sense), so more fluctuations than in zero-temperature Glauber dynamics may be expected. No bulk noise, so full consensus states are absorbing. In $d=1$ it equals zero-temperature Glauber. In $d=2$ (Fig. 2) domains grow but interfaces are very rough, unlike usual coarsening (p. 9).
- Origin and uses: Clifford–Sudbury, named by Holley–Liggett. It is one of the very few non-equilibrium stochastic processes exactly solvable in any dimension. Probabilists used duality with coalescing random walkers. The authors follow Frachebourg–Krapivsky (p. 9).
- On a $d$-dimensional hypercubic lattice the flip rate of spin $k$ is
$$W_k(S)\equiv W(s_k\to-s_k)=\frac d4\Big(1-\frac1{2d}s_k\sum_js_j\Big), \tag{5}$$
 over the $2d$ nearest neighbors ($d/4$ sets the time scale). Master equation:
$$\frac{d}{dt}P(S,t)=\sum_k\big[W_k(S^k)P(S^k,t)-W_k(S)P(S,t)\big], \tag{6}$$
 where $S^k$ equals $S$ except spin $k$ flipped (p. 9).
- The rates are linear, so the equations for correlation functions $\langle s_k\cdots s_l\rangle\equiv\sum_SP(S,t)s_k\cdots s_l$ of any order close (do not depend on higher-order functions) and can be solved (p. 9).
- One-body:
$$\frac{d}{dt}\langle s_k\rangle=\Delta_k\langle s_k\rangle, \tag{7}$$
 with $\Delta_k$ the discrete Laplace operator. Summing over $k$, the global magnetization $\langle s\rangle=\frac1N\sum_k\langle s_k\rangle$ is conserved. This gives the exit probability (probability of ending all up) in a finite system: with $\rho(0)=(\langle s\rangle+1)/2$, $P_{up}(\rho(0))=\rho(0)$ in any dimension (p. 9–10).
- Two-body:
$$\frac d{dt}\langle s_ks_l\rangle=(\Delta_k+\Delta_l)\langle s_ks_l\rangle. \tag{8}$$
 Same structure as the 1D zero-temperature Glauber Ising correlators; solved by Laplace transform. The density of active interfaces $n_a(t)=(1-\langle s_ks_{k+1}\rangle)/2$ behaves as
$$n_a(t)\sim\begin{cases}t^{-(2-d)/2}&d<2\\1/\ln t&d=2\\a-bt^{-d/2}&d>2.\end{cases}\tag{9}$$
 For $d\le2$ coarsening leads to complete consensus. For $d>2$ a finite density of interfaces remains: no consensus in an infinite system; opposite domains coexist indefinitely. In terms of duality the authors attribute this to the transient nature of random walks in $d>2$; the sentence as printed continues "diffusing active interfaces have a finite probability to meet and annihilate" (p. 10).
- For $d=2$ at large times:
$$n_a(t)=\frac{\pi}{2\ln t+\ln 256}+O\!\Big(\frac{\ln t}{t}\Big). \tag{10}$$
 The large constant makes the approach to the logarithmic decay very slow, explaining why different laws were hypothesized from numerical evidence (p. 10).
- In $d=2$ the scaling form of $C(r,t)$ is violated logarithmically: there is no single domain length. Domains of all sizes $t^\alpha$, $0<\alpha\le1/2$, coexist (p. 10).
- **Finite systems:** consensus is invariably reached. Time $T_N\sim N^2$ ($d=1$), $N\ln N$ ($d=2$), $N$ ($d>2$). For $d\le2$ consensus arrives by coherent coarsening, for $d>2$ only through a large random fluctuation (p. 10).
- **Generalized rates** $W_k(S)=\frac12[1-s_kf_k(S)]$, $|f_k|\le1$. Local, spatially symmetric, up-down-symmetric dynamics needs $f_k$ to be an odd function of the neighbor sum. On a square lattice $f(2)=-f(-2)=x$ and $f(4)=-f(-4)=y$. Special cases: voter $x=1/2,y=1$; majority-vote $x=y$; Glauber $y=2x/(1+x^2)$; noisy voter $y=2x$. $y$ gauges bulk noise ($y=1$: none); $x$ gauges interfacial noise (p. 10).
- Simulations and pair approximation: a ferromagnetic region around $x=y=1$ (zero-T Glauber) and a paramagnetic phase, separated by a line of continuous transitions ending at the voter point. Changing $x$ while keeping $y=1$ gives a jump of the order parameter (first order). Hence the voter point is critical, at the transition between order and disorder driven by purely interfacial noise (p. 10).
- **Droplet test.** A droplet of up spins in a down background: Cahn–Allen theory (curvature-driven) predicts linear decay of droplet area in $d=2$, at a rate proportional to surface tension. In the voter model the interface roughens but the radius stays statistically unchanged: no surface tension (Fig. 2) (p. 10).
- **Voter-like behavior is more general.** Dornic et al. argue it is generically observed at order–disorder non-equilibrium transitions driven by interfacial noise between dynamically symmetric absorbing states. The symmetry may come from up-down symmetry of rules or from conservation of magnetization. Exponents: $\beta=0$, $\nu=1/2$ in all dimensions; $\gamma=1/2$ for $d=1$ and $\gamma=1$ for $d>2$ with logarithmic corrections at the upper critical dimension $d=2$ (as printed) (p. 11).
- **Noisy voter model** (linear Glauber): spontaneous flips added, still exactly solvable. Bulk noise destroys long-range order; it is always in the paramagnetic phase of the generalized model, so domains form only up to a finite correlation length, which grows as noise decreases; the voter first-order transition occurs at zero noise (p. 11). The generalized voter universality class and its links to other non-equilibrium transitions are called a complicated, open issue (p. 11).

*Intuition note:* Copying a random neighbor gives interfaces no restoring tendency (no surface tension), and the voter model maps onto random walkers that coalesce when they meet (duality). In $d\le2$ coarsening leads to consensus; in $d>2$ random walks are transient and a finite density of interfaces survives, so opinions stay mixed in an infinite system. Because the average opinion (magnetization) is conserved, the chance of ending all up equals the initial fraction of up.

**2. Modifications and applications (p. 11).**
- Multitype (Potts) voter; a single *zealot* (never changes opinion; Mobilia): breaks magnetization conservation; for $d\le2$ the zealot induces general consensus on its opinion; for higher $d$ consensus is not reached but the stationary state near the zealot is biased. Many-zealot cases were also studied (p. 11).
- *Constrained voter model*: three states (left, right, centre); only centrists interact with others, extremists do not talk to each other (a discrete analogue of bounded confidence). Probabilities of ending in one of three consensus states or in a mixture of extremists were derived, with little change between $d=1$ and mean field (p. 11).
- *AB-model*: states A, B and intermediate AB. With $\sigma_l$ the local density of state $l$ ($l$=A,B,AB) around the chosen agent $i$:
$$p_{A\to AB}=\tfrac12\sigma_B,\quad p_{B\to AB}=\tfrac12\sigma_A, \tag{11}$$
$$p_{AB\to B}=\tfrac12(1-\sigma_A),\quad p_{AB\to A}=\tfrac12(1-\sigma_B). \tag{12}$$
 Extremes here do interact; the only absorbing states are consensus A and consensus B (p. 11).
- *Vacillating voter* (checks two neighbors; flips if either differs): bias toward zero magnetization, anti-coarsening, consensus time exponential in $N$. *Memory/noise reduction* (counters; flip when a counter reaches threshold $r$): induces effective surface tension, curvature-driven coarsening. *Inertia* (Stark et al.): rate decreases linearly with time since last flip, up to a saturation; a sufficiently weak inertia makes consensus faster on 2D lattices, Watts–Strogatz and fully connected networks. Ecology variants: speciation, biased voter (p. 11).

**3. The voter model on networks (p. 12).**
- **Complete graph:** Fokker–Planck equation for the magnetization density is a diffusion equation with position-dependent diffusion constant and no drift (no surface tension); solvable. Mean consensus time scales as $N$; tail $\exp(-t/N)$ (p. 12).
- **Definitions diverge on heterogeneous graphs.** *Direct voter*: pick a site, copy a random neighbor; magnetization is not conserved. *Link-update*: pick a link, one randomly chosen end copies the other; conservation restored. *Reverse (invasion) voter*: pick a node and copy its variable to a random neighbor (p. 12).
- For direct voter dynamics on a generic graph a degree-weighted density $\omega$ of up spins is conserved, and
$$T_N(\omega)=-N\frac{\mu_1^2}{\mu_2}\big[(1-\omega)\ln(1-\omega)+\omega\ln\omega\big], \tag{13}$$
 with $\mu_k$ the $k$-th moment of the degree distribution. For scale-free graphs (exponent $\gamma$): $T_N\sim N$ for $\gamma>3$, sublinear for $\gamma\le3$ (agrees with simulations). Link-update: linear in $N$ independent of degree distribution. Reverse voter: $T_N\sim N$ for any $\gamma>2$ (p. 12).
- **Small-world networks:** after an initial 1D-like regime, $n_a$ forms a plateau (Fig. 3) because shortcuts hinder interface diffusion. The system sits in a metastable state with domains of typical length $\sim1/p$. Its lifetime scales with linear size $L$, so finite systems reach consensus faster than on a 1D lattice ($L^2$). In infinite systems the coexisting state is stable, so long-range links prevent complete ordering (p. 12).

#### C. Majority rule model (p. 13–14)
- Setup: $N$ agents with binary opinions, fractions $p_+$ and $p_-=1-p_+$; complete graph. At each step a random group of $r$ agents (group size drawn from a distribution) adopts the group's majority opinion (Fig. 4). For even $r$, ties are resolved in favor of one opinion (say $+1$), motivated by social inertia (p. 13).
- With initial fraction $p_+^0$ there is a threshold $p_c$: above it all end $+1$, below it all end $-1$. Consensus time $\sim\log N$. For odd group sizes $p_c=1/2$; if even groups exist, $p_c<1/2$ (the favored opinion can win from a minority) (p. 13).
- **Mean-field derivation (fixed group size 3, continuum limit, Chen–Redner).** Let $m=\frac1N\sum_ks_k=p_+-p_-$. $N_+$ rises by one if the group is $++-$ and falls by one if it is $+--$:
$$dN_+=3(p_+^2p_--p_+p_-^2)=-6p_+\big(p_+-\tfrac12\big)(p_+-1), \tag{14}$$
 (factor 3 from permutations of the configurations). With $dt=3/N$ (each agent updated once per unit time):
$$\frac{dN_+}{N}\frac N3=\dot p_+=-2p_+\big(p_+-\tfrac12\big)(p_+-1). \tag{15}$$
 Fixed points: $p_+=0,\tfrac12,1$; $\tfrac12$ unstable, the others stable. From any $p_+\ne1/2$ all agents converge to the initial majority state; integration gives consensus time $\sim\log N$ (p. 13).
- **Lattices.** Not analytically solvable in $d=1$. Magnetization not conserved, so the exit probability depends nontrivially on the initial magnetization in the thermodynamic limit and a minority can win; consensus time $\sim N^2$. In higher $d$: diffusive coarsening; for zero initial magnetization the system may get trapped in metastable stripes (2d) or slabs (3d), giving two time scales; average consensus time grows as a power of $N$ with dimension-dependent exponent. For non-zero initial magnetization the metastable states quickly disappear. In $d=4$ simulations do not reproduce mean field, so the upper critical dimension is larger than four. Other topologies studied: heterogeneous networks, community-structured graphs, small-world lattices (p. 13–14).
- **Multi-state and plurality rule** (Chen–Redner; $s$ states, group size $G$): mean-field consensus for any $s,G$, time $\sim\log N$. On the square lattice, if $s$ is too large no group has a majority and the system does not evolve. Plurality rule: the group adopts the opinion with the most representatives; consensus for any $s,G$ (a relative majority always exists); once only two opinions remain, 2-state MR behavior with metastable states (p. 14).
- **Variants listed** (brief): moving agents, variable neighbor numbers, three opinions, opinion-favoring probabilities, contrarians, inflexible agents (p. 14).
- **Majority–minority (MM) model:** the majority prevails with probability $p$, the minority with $1-p$. For groups of three, $m$ changes by $2p-4(1-p)$ per interaction, so at $p=p_c=2/3$ $m$ does not change on average, like the voter model. Mean field: exit probability is a step function for $p>p_c$ and equals $1/2$ for $p<p_c$ (driven toward zero magnetization) (p. 14).
- **Majority-vote model** (Liggett): with probability $1-q$ a spin takes its neighbors' majority sign, with probability $q$ the minority; ties flip with probability 1/2; one spin updated per step. $q=0$ is zero-temperature Glauber. Order–disorder transition at critical $q_c$ on regular lattices with Ising-class exponents; also on small-world lattices and random graphs (p. 14).
- **Klimek et al. model:** an agent is convinced if at least a fraction $p$ of neighbors share an opinion; interpolates between majority ($p=1/2$) and unanimity ($p=1$) (p. 14).

*Intuition note:* Locally taking the majority amplifies any initial advantage, so in the mean field the initial majority wins. The rule that favors one side in ties shifts the threshold below 1/2. On lattices in 2D and 3D with zero initial magnetization, metastable stripes or slabs evolve very slowly and can delay consensus.

#### D. Social impact theory (p. 14–15)
- Latané's theory: the impact of a group on a subject depends on group size, members' convincing power and distance (spatial or in an abstract space of relationships). Its cellular-automaton versions are exactly solvable in mean field (p. 14).
- Each individual $i$ has opinion $\sigma_i=\pm1$, persuasiveness $p_i$ and supportiveness $s_i$ (random numbers, a source of disorder). Total impact:
$$I_i=\Big[\sum_{j=1}^N\frac{p_j}{d_{ij}^\alpha}(1-\sigma_i\sigma_j)\Big]-\Big[\sum_{j=1}^N\frac{s_j}{d_{ij}^\alpha}(1+\sigma_i\sigma_j)\Big], \tag{16}$$
 with $\alpha>2$ giving how fast impact decays with distance. First term: persuasive impact (from agents with opposite opinion); second: supportive impact (from agents with the same opinion, favoring status quo) (p. 15).
- Update rule:
$$\sigma_i(t+1)=-\mathrm{sgn}\,[\sigma_i(t)I_i(t)+h_i], \tag{17}$$
 with $h_i$ a random field for other sources (e.g., mass media). A spin flips if the pressure to change beats the pressure to keep ($I_i>0$ when $h_i$ vanishes) (p. 15).
- Results: for fully connected agents without individual fields, infinitely many stationary states (order parameter a complex function of one variable, as in spin glasses). In general, in the absence of individual fields, the dynamics leads to dominance of one opinion but not complete consensus; if the initial magnetization is about zero, the system converges to a large majority in one opinion plus stable minority domains. With individual fields these minority domains become metastable ("staircase dynamics") (p. 15).
- Social impact theory neglects memory, finite information speed and physical space. **Extension with active Brownian particles:** agents with opinion $\sigma_i=\pm1$ and strength $s_i$ act as sources of a scalar opinion field $h_\sigma(\mathbf r,t)$. Opinion-change rates, with $T$ a social temperature:
$$w(\sigma'|\sigma)=\eta\exp\{[h_{\sigma'}(\mathbf r,t)-h_\sigma(\mathbf r,t)]/T\}. \tag{18}$$
 Field equation:
$$\frac{\partial}{\partial t}h_\sigma(\mathbf r,t)=\sum_{i=1}^Ns_i\delta_{\sigma,\sigma_i}\delta(\mathbf r-\mathbf r_i)-\gamma h_\sigma(\mathbf r,t)+D_h\Delta h_\sigma(\mathbf r,t). \tag{19}$$
 Density $n_\sigma$ of individuals with opinion $\sigma$:
$$\frac{\partial}{\partial t}n_\sigma=-\nabla[n_\sigma\,\alpha\nabla h_\sigma]+D_n\Delta n_\sigma-\sum_{\sigma'\ne\sigma}[w(\sigma'|\sigma)n_\sigma-w(\sigma|\sigma')n_{\sigma'}]. \tag{20}$$
 Here $N$ is the number of agents, $1/\gamma$ the average lifetime of the field, $D_h$ the diffusion constant for information exchange, $D_n$ the spatial diffusion coefficient of individuals, $\alpha$ the agents' response to the field. The equations are coupled with nonlinear feedback. Three phases: paramagnetic (high temperature, high diffusion), ferromagnetic (low temperature, low diffusion), and segregation (opinions prevail in spatially separated domains) (p. 15).

#### E. Sznajd model (p. 16–18)
- Principle: convincing is easier for two or more people than for one; the authors later call this "social validation". Original version (Sznajd B), on a linear chain: a pair $i,i+1$ fixes its neighbors $i-1$, $i+2$:
$$\text{if } s_i=s_{i+1}\text{ then }s_{i-1}=s_i=s_{i+1}=s_{i+2}; \tag{21}$$
$$\text{if } s_i\ne s_{i+1}\text{ then }s_{i-1}=s_{i+1}\text{ and }s_{i+2}=s_i. \tag{22}$$
 Random sequential updating (p. 16).
- From a random start with equal opinions: consensus all up or all down (probability 1/4 each), or a stalemate in antiferromagnetic order ($m=0$, probability 1/2; due to rule 22). These values are deduced from the up-down symmetry. Relaxation time is log-normal (Behera–Schweitzer). The number of agents never changing opinion first decays as a power law and then reaches a constant finite value, unlike the Ising model (p. 16).
- *Information flow:* the Sznajd model was supposed to describe how opinions spread (flow from the pair outward). Behera and Schweitzer showed that in 1D the direction of flow is irrelevant: Sznajd B is equivalent to a voter dynamics with influence from next-to-nearest neighbors. Updating a pair introduces a factor of two in the relaxation time; all else is the same (hitting probabilities, time distributions). The dynamics reduce to "just follow your next-to-nearest neighbor" (p. 16). So Sznajd B does not respect the social validation principle that motivated it (p. 16).
- **Sznajd A:** only the ferromagnetic rule (21); neighbors of a disagreeing pair keep their opinions. On the square lattice a pair influences its six neighbors only if the pair agrees (Fig. 5). Exit probability is a step function at $m=0$: initial $m<0$ gives consensus $m=-1$; $m>0$ gives $m=1$. Consensus-time distribution is broad but not log-normal. Sznajd B in 1D has no transition in exit probability (coexistence of ferro/antiferro states). Fixed points of Sznajd A persist if the size of the pool of persuaders is changed; the exception is Ochrombel's simplification, where a single agent imposes its opinion on all neighbors (p. 16–17).
- **Complete graph** (Slanina–Lavička): two random agents $i,j$ and a random third $k$; if $s_i=s_j$ then $s_k=s_i$, otherwise nothing. In the thermodynamic limit:
$$\frac{\partial}{\partial t}P(m,t)=-\frac{\partial}{\partial m}\big[(1-m^2)mP(m,t)\big], \tag{23}$$
 a pure drift of the magnetization, with general solution
$$P(m,t)=[(1-m^2)m]^{-1}f\!\Big(e^{-t}\frac{m}{\sqrt{1-m^2}}\Big), \tag{24}$$
 $f$ depending on initial conditions. For $P(m,0)=\delta(m-m_0)$, $P$ stays a $\delta$-function, pushed toward $+1$ if $m_0>0$ or $-1$ if $m_0<0$, reached asymptotically. So $m_0$ determines the final consensus, with a transition when $m_0$ changes sign. The tail of the time distribution is exponential (p. 17).
- **Hamiltonian attempts.** Sznajd rules equal minimization of a local disagreement function
$$E_i=-J_1s_is_{i+1}-J_2s_is_{i+2}, \tag{25}$$
 with $s_i$ taking the value minimizing $E_i$ (two-component, TC, model). If $J_1J_2>0$ the two terms are equivalent. Sznajd B is recovered for $-J_2<J_1<J_2$, $J_2>0$. Four phases, delimited by the bisectors $J_1\pm J_2=0$, with a new attractor of aligned pairs with alternating signs ($\ldots++--++--\ldots$). The model is not equivalent to a zero-temperature Hamiltonian model: $\sum_iE_i$ is not an energy because local minimization can raise its global value (p. 17).
- **General sequential probabilistic model (GPM)** (Galam): in mean field a random group of $k$ agents, $j$ with $+$, is selected; the group adopts $+$ with probability $m_{k,j}$ and $-$ with $1-m_{k,j}$. With $p(t)$ the fraction of $+$:
$$p(t+1)=\sum_{j=0}^km_{k,j}\,p(t)^j[1-p(t)]^{k-j}\frac{k!}{j!(k-j)!}. \tag{26}$$
 Two phases: consensus and coexistence of both opinions in equal proportions. The transition occurs where magnetization is on average conserved (voter dynamics). With suitable $\{m_{k,j}\}$ it reproduces mean-field behavior of all known models with binary opinions: voter, majority rule, Sznajd, MM, etc. (p. 17).
- **Modifications.** Studied on regular lattices, complete, random, small-world and scale-free graphs. On any graph with only rule (21), a sharp dynamic transition from all down to all up; on growing networks, a smooth crossover. The transition persists with dilution, more than two states, and an influence of the pair extending beyond its neighborhood; it disappears with noise or antiferromagnetic rules (p. 17–18). Synchronous updating can produce "frustrated" agents who keep their opinion, hindering consensus (stable mixed clusters); noise or memory limits this (p. 18).
- **Bounded confidence in Sznajd** for $q>2$ states: if opinions are similar when they differ by at most one unit, and a pair of agents with the same opinion can convince only neighbors of similar opinions, the dynamics always give consensus for $q=3$, while for $q>3$ it is very likely that at least two opinions survive (Stauffer). A real-valued extension exists (p. 18). Applications: voting behavior, economic attitudes, product competition, spread of opinions among traders (p. 18).

*Intuition note:* In 1D, the Sznajd B pair rule turns out to be equivalent to a voter dynamics in which each agent follows its next-to-nearest neighbor; updating a pair only adds a factor of two to the relaxation time. The authors conclude that Sznajd B does not realize the social-validation idea.

#### F. Bounded confidence models (p. 18–19; the section continues past this unit)

**1. Continuous opinions (p. 18).**
- Opinions may vary smoothly (e.g., political orientation). Majority and equality of opinion lose meaning, so a different framework is needed. Early studies came from applied mathematicians, on conditions for a panel of experts to reach a common decision (p. 18).
- Start: $N$ agents with random real opinions; here all agents usually start with different opinions. Final clusters: one (consensus), two (polarization) or more (fragmentation). Bounded confidence (BC): an agent with opinion $x$ interacts only with peers whose opinion lies in $]x-\epsilon,x+\epsilon[$; $\epsilon$ is the uncertainty or tolerance (p. 18).

**2. Deffuant model (p. 18–19).**
- Agents on graph nodes, opinions $x_i\in[0,1]$ at random. At each step a random agent and a random neighbor meet. If the difference of opinions exceeds $\epsilon$, nothing happens. If $|x_i(t)-x_j(t)|<\epsilon$:
$$x_i(t+1)=x_i(t)+\mu[x_j(t)-x_i(t)], \tag{27}$$
$$x_j(t+1)=x_j(t)+\mu[x_i(t)-x_j(t)]. \tag{28}$$
 $\mu\in[0,1/2]$ is the convergence parameter; $\mu=1/2$ puts both at the pair's earlier average. The pair average is unchanged, so the global average (1/2) is invariant (p. 19).
- Evolution: the uniform state is unstable near the edges of opinion space; the instability propagates toward the middle, forming dense patches that become final clusters. Once clusters are further apart than $\epsilon$, only same-cluster agents interact and converge to one value; the final state is a sequence of Dirac deltas. Cluster number and size depend on $\epsilon$; $\mu$ affects convergence time, but for small $\mu$ the final configuration also depends on $\mu$ (p. 19).
- On complete graphs, regular lattices, random graphs and scale-free networks: for $\epsilon>\epsilon_c=1/2$ all share opinion 1/2 (complete consensus). This may be a general property independent of the social graph. For small $\epsilon$ more clusters emerge (Fig. 6, $\epsilon=0.25$, two factions) (p. 19).
- Monte Carlo: number of clusters $n_c\approx1/(2\epsilon)$. Reason: clusters must differ by at least $\epsilon$, so no other cluster lies within a length-$2\epsilon$ interval centered at a cluster; $1/(2\epsilon)$ is a fair estimate (p. 19).
- **Rate equation (fully mixed, $\mu=1/2$; Ben-Naim et al.).** $P(x,t)dx$ = probability an agent has opinion in $[x,x+dx]$; threshold $\epsilon=1$, opinion range $[-\Delta,\Delta]$ (equivalent to the usual setting if $\epsilon=1/2\Delta$, as printed):
$$\frac{\partial}{\partial t}P(x,t)=\int_{|x_1-x_2|<1}dx_1dx_2\,P(x_1,t)P(x_2,t)\Big[\delta\Big(x-\frac{x_1+x_2}2\Big)-\delta(x-x_1)\Big]. \tag{29}$$
 It conserves the norm $M_0=\int_{-\Delta}^{+\Delta}P\,dx$ and the average opinion. Start from the flat $P(x,0)=1$, find $P_\infty(x)=P(x,t\to\infty)$. If $\Delta<1/2$ all agents interact, (29) is integrable, all approach opinion 0: $P_\infty(x)=M_0\delta(x)$. If $\Delta>1/2$ it is not analytically solvable; the asymptotic distribution is a sum of deltas:
$$P_\infty(x)=\sum_{i=1}^pm_i\delta(x-x_i). \tag{30}$$
 (Part 1 ends here; Hegselmann–Krause, Sec. III.F.3, comes next, listed in the Contents on p. 20.)

*Intuition note:* Compromise in small steps plus talking only to similar agents lets agents merge into clusters that then no longer interact with each other. A smaller tolerance $\epsilon$ leaves more clusters.

## Toy example (ours)
Voter model on a complete graph of $N=3$ agents (a regular graph, so magnetization is conserved), initial state $(+,+,-)$. Each step: pick an agent uniformly, then one of the other two uniformly; the agent copies it. Let $k$ = number of $+$ agents. Claim from conservation of magnetization: exit probability $=\rho(0)=2/3$ (cf. $P_{up}=\rho(0)$, p. 10).

Check directly. $k=2$: $k\to3$ if the $-$ agent is picked (prob. 1/3) and copies a $+$ (prob. 1): $1/3$. $k\to1$ if a $+$ agent is picked (2/3) and copies the $-$ (1/2): $1/3$. Stay with prob. 1/3. By symmetry, $k=1$: $\to2$ with prob. $(2/3)(1/2)=1/3$, $\to0$ with prob. $1/3$, stay $1/3$.
Let $h_k$ = probability to end at $k=3$; $h_3=1$, $h_0=0$.
- $h_2=\tfrac13\cdot1+\tfrac13h_1+\tfrac13h_2\Rightarrow2h_2=1+h_1$.
- $h_1=\tfrac13h_2+\tfrac13\cdot0+\tfrac13h_1\Rightarrow2h_1=h_2$.
- So $2h_2=1+h_2/2\Rightarrow h_2=2/3$, $h_1=1/3$. ✓ equals $k/3$.

Expected change of $k$ at $k=2$: $(+1)(1/3)+(-1)(1/3)=0$, so the magnetization has no drift.

## Concepts
- [[order-disorder-transition]] — consensus (order) vs. fragmentation (disorder); the review's central theme (p. 2, 4)
- [[universality]] — in most situations large-scale behavior depends only on symmetries, dimension, conservation laws, not microscopic details (p. 3)
- [[mean-field-approximation]] — all-to-all interaction ("homogeneous mixing"), which guarantees that the mean-field approximation is correct (p. 4)
- [[voter-model-bounded-confidence]] — voter rule (copy a neighbor) and bounded confidence (interact only if opinions close; distance in opinion space) (p. 4, 9, 18)
- [[agent-based-model-abm]] — simulate computational agents in parallel to study micro-to-macro emergence (p. 7)
- [[small-world-network]] — high clustering, short paths (Watts–Strogatz) (p. 6)
- [[preferential-attachment]] — BA rule: new links with probability proportional to degree (p. 6)
- [[heavy-tail-power-law]] — $P(k)\sim k^{-\gamma}$; scale-free if $\gamma\le3$ (p. 6)
- [[homophily-and-social-influence]] — "social influence": interaction makes agents more alike; ferromagnetic analogue (p. 4)
- [[criticality-phase-transition]] — voter point is critical between order and disorder driven by interfacial noise (p. 10)
- [[emergence]] — micro-to-macro emergence is the stated aim of ABM (p. 7)
- [[fixed-point-and-stability]] — majority-rule fixed points $0,\tfrac12,1$ ($\tfrac12$ unstable) (p. 13)
- [[master-equation]] (new) — gain–loss equation for the probability of macro-states (p. 7)
- [[coarsening-dynamic-scaling]] (new) — domain growth $L(t)\sim t^{1/z}$ with rescaled statistical morphology (p. 5)
- [[surface-tension-curvature-driven]] (new) — tendency to align with majority makes interfaces cost energy; absent in the voter model (p. 5, 10)
- [[exit-probability-and-consensus-time]] (new) — probability of ending in a given consensus; time $T_N$ to reach it (p. 9–10, 13)
- [[absorbing-state]] (new) — state where dynamics stop, e.g., consensus without bulk noise (p. 9)
- [[sociodynamics]] (new) — macro-variable transition-rate approach to social modeling (p. 7)
- [[social-impact-theory]] (new) — impact of a group depends on number, convincing power and distance of its members (p. 14–15)
- [[disagreement-function]] (new) — local function $E_i$ minimized in the Sznajd TC model; not a global energy (p. 17)
- [[finite-size-effects]] (new) — social systems are small, so finite $N$ matters (p. 5)

## Canonical instances
- [[ising-model]] — paradigm of order–disorder transition and ordering dynamics (p. 4–5)
- [[voter-model]] — exactly solvable; in an infinite system consensus only for $d\le2$; no surface tension (p. 9–12)
- [[majority-rule-model]] — mean-field threshold dynamics; for group size 3, $\dot p_+=-2p_+(p_+-\tfrac12)(p_+-1)$ (p. 13)
- [[majority-vote-model]] — noisy majority with Ising-class transition on regular lattices (p. 14)
- [[sznajd-model]] — pair influence; Sznajd B on a chain is equivalent to voter dynamics (p. 16)
- [[social-impact-model]] — Latané/Nowak persuasion–support dynamics (p. 14–15)
- [[deffuant-model]] — pairwise compromise with confidence bound $\epsilon$ (p. 18–19)
- [[erdos-renyi-model]], [[watts-strogatz-model]], [[barabasi-albert-model]] — network substrates (p. 6)
- [[ab-model]] — three-state voter variant with intermediate state (p. 11)

## Bridges (candidates)
- [same-math] Voter-model duality ↔ probability: exact mapping to coalescing random walkers; transience of random walks in $d>2$ is linked to the lack of consensus there (p. 9–10).
- [structural-analogy] Voter/Glauber correlation equations ↔ statistical physics: same structure as the 1D zero-temperature Glauber Ising equations; in $d=1$ the dynamics coincide (p. 9–10).
- [structural-analogy] Social influence ↔ ferromagnetism: alignment with neighbors vs. spin alignment (p. 4).
- [structural-analogy] Deffuant rate equation (29) ↔ gain–loss equations for distributions under pairwise encounters (p. 19).
- [structural-analogy] Bounded confidence ↔ finite interaction range in physics, with distance in opinion space (p. 4).
- [metaphor] Majority-rule fixed points ↔ tipping point / bistable system: unstable $1/2$ separates two stable consensus states (p. 13).

## Questions this raises
- If the voter model has no surface tension, what other features of real opinion change (zealots, memory, inertia) generate effective surface tension, and which ones does data support?
- How robust are the voter results on networks to the choice of update (direct, link-update, reverse), and which fits real communication?
- The review notes that theory far outweighs data validation; what empirical observable (e.g., Section III.H, not in this part) could discriminate voter from majority-rule or Sznajd models?
- Is the property that $\epsilon>1/2$ gives consensus in the Deffuant model independent of the social graph, as the authors suggest it may be?

## Reading notes
- Part 1 of 3: covers printed pp. 1–19 (title page/Contents through the Deffuant rate equation, Eq. 30). It starts at the title and abstract and ends within Section III.F.2 (Deffuant). Section III.F.3 (Hegselmann–Krause) and everything after belong to later parts.
- Printed page numbers equal pdf page numbers (offset 0).
- The edition seen is the arXiv version 0710.3256v2 (11 May 2009), as stamped on page 1.
- Equations were transcribed from the page images where available. In Eq. (3) on p. 7 the text layer does not mark where the index $k$ sits; it is read here as the component $m_k$, in line with the text's "equations of motion for $m_k(t)$".
- Page 11 states the exponents with $\gamma=1$ for $d>2$ together with logarithmic corrections at the upper critical dimension $d=2$; I report it as printed.
- Page 10 attributes the lack of order for $d>2$ to the transience of random walks and then says the diffusing interfaces have a finite probability to meet and annihilate; I report the sentence as printed.
- Page 19 prints the equivalence in-line as $\epsilon=1/2\Delta$, and the case $\Delta<1/2$ as "all agents interact"; both are copied as printed.
- Page 11: the printed sentence introducing a related one-dimensional model (Lambiotte and Redner, 2007) ends without describing it. Page 17: the sentence about Sznajd's sharp transition contains a printed typo ("will" for "with").
- No exercises in this unit.

---
id: castellano-2009-socialdynamics/main-p3
work: castellano-2009-socialdynamics
unit: paper (part 3/3) — end of Sec. VI (applause, Mexican wave), Secs. VII–XI (hierarchies, human dynamics, spreading, coevolution, outlook)
pages: 40–50 (pp. 51–58 are the reference list, not digested)
fields: [complex-systems]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Statistical physics of social dynamics — part 3: applause, hierarchies, human dynamics, spreading, coevolution, outlook

## L0 — One line
Simple statistical-physics models (Kuramoto synchronization, Bonabeau and advancement–decline hierarchy models, queuing models, rumor models, coevolving networks) reproduce social phenomena, but the authors say that identifying which phenomena the models actually describe, using empirical data, must become a priority.

## L1 — The gist (≤ 120 words)
This part covers how simple interacting-agent models explain collective social phenomena. Rhythmic applause is treated as Kuramoto synchronization. In the Bonabeau model, hierarchies arise from fights plus memory (relaxation). Priority-queue models have been proposed to explain bursty human activity. Rumor models are epidemic-like; the Daley–Kendall model has no spreading threshold under homogeneous mixing. Opinions and network links can coevolve and produce topological phase transitions. The review's outlook stresses simplicity, universality, phase transitions and scales as physics' contributions. It says models need empirical data and concrete applications, or they risk being "only a conceptual exercise". It names the web, language dynamics and evolving social networks as promising directions.

**Prerequisites:** ordinary differential equations; Jacobian eigenvalues and linear stability; mean-field approximation; power laws; basic network ideas (degree, giant component, rewiring); SIR epidemics.

## L2 — Key ideas (5–10 bullets)
- Rhythmic applause is modeled with Kuramoto oscillators. For $N\to\infty$ a synchronized phase appears for $K>K_c$, and for a Gaussian frequency distribution $K_c$ is proportional to the spread of natural frequencies. The much higher dispersion of frequencies in enthusiastic clapping hinders synchronization (p. 40).
- The hypothesis that hierarchy formation is self-organization due to social dynamics is, per the review, now the most widespread. In the Bonabeau model (winner/loser feedback plus relaxation) the mean-field egalitarian state loses linear stability above $\rho_c=2\mu/\eta$. The transition is discontinuous for $\eta<2$ and continuous for $\eta\ge2$ (pp. 40–41).
- Advancement–decline model (mean field): for decline rate $r<1$ a fraction $r$ stays at finite strength and a fraction $1-r$ has strength growing linearly in time. For $r\ge1$ all strengths stay finite (p. 42).
- Human activity is bursty and heavy-tailed. Priority-queue models give waiting-time power laws with exponent $1$, $3/2$ or (exact result at $p=1$) $2$, depending on the model, the protocol and the regime (stationary or critical). Collaborative tagging and Digg add Zipf-like and log-normal statistics (pp. 43–45).
- Rumor models (Daley–Kendall) have no spreading threshold under homogeneous mixing, because of the nonlinear stifling term; a threshold returns if linear self-recovery is also present. On scale-free networks they reach fewer people but are more efficient. On small-world networks the transition is dynamic, not geometric (p. 46).
- Coevolution of states and links gives topological phase transitions, with cluster-size power laws, critical slowing down, and shifted opinion thresholds. Adaptive links can favor consensus (Axelrod) or remove fragmentation (Deffuant) (pp. 47–48).
- Outlook: physics contributed modeling, simplicity, universality and attention to scales and topology. The review says that identifying which phenomena the models actually describe must become a priority; for instance, the Axelrod model has not yet been shown to describe at least semi-quantitatively any concrete situation (p. 49).

## L3 — Walkthrough

### End of the rhythmic-applause subsection of Sec. VI (continued from earlier pages)
- An order parameter for synchronization is the maximum, over period $T\in[T_{min},T_{max}]$ and phase $\Phi$, of the normalized correlation between the sound signal $s(t)$ and a harmonic function (p. 40):
$$r(t)=\max_{\{T,\Phi\}}\left[\frac{\int_{t-T}^{t+T}s(t)\sin(2\pi/T+\Phi)\,dt}{\int_{t-T}^{t+T}s(t)}\right]\tag{46}$$
- The text says its time evolution (called $q(t)$ there) shows synchronization emerging (p. 40).
- Kuramoto description: $N$ non-identical rotators, each with phase $\phi_i$ and natural frequency $\omega_i$ drawn from $g(\omega)$ (p. 40):
$$\frac{d\phi_i}{dt}=\omega_i+\frac{K}{N}\sum_{j=1}^{N}\sin(\phi_i-\phi_j)\tag{47}$$
- $K$ is the coupling. Each rotator interacts with all others, trying to minimize phase differences (p. 40).
- For $N\to\infty$ there is a critical $K_c$: for $K>K_c$ the rotators are partially aligned (synchronized phase). For Gaussian $g(\omega)$ with dispersion $D$, $K_c=D\sqrt{2/\pi^3}$, so $K_c$ is proportional to $D$ (p. 40).
- Small $D$ makes synchronization likely. The frequency of rhythmic applause, and its dispersion, are small (experiments on individual spectators). The enthusiastic clapping at the start has much higher dispersion, which hinders synchronization (p. 40).
- Synchronized applause is not stable. Noise intensity drops because clapping slows. Spectators may find the reduced sound too weak and decide to speed up to make more noise; this brings back the enthusiastic phase and synchronization is lost. It may be reached again later (p. 40).
- A more realistic model uses two-mode stochastic oscillators driven only by the goal of a desired global noise level, with or without synchronization (p. 40).

*Intuition note:* Synchronization is easy when everyone's natural rhythm is similar, because then weak coupling suffices. Spectators may decide to clap faster to be louder; this can bring back the enthusiastic phase and destroy the synchronization.

### D. Mexican wave
- Models are inspired by excitable media. A unit switches from inactive to active if the density of active units in its neighborhood exceeds a critical threshold (p. 40).
- The influence of a neighbor decreases with distance and is higher if the neighbor is on the side the wave comes from. The summed influence is compared with the spectator's threshold, which is uniformly distributed in some range (p. 40).
- A group of spectators must exceed a critical mass to start the wave. The models reproduce size, form, velocity and stability of real waves (p. 40).

### VII. Formation of hierarchies
- Many species, including humans, have rank structure. Rank determines roles and access to resources, and hierarchy allows task specialization (p. 40).
- Question: how do inequalities arise from individuals of initially identical status? Intrinsic attributes (size, talent) are one explanation. Landau (1951) pointed out that intrinsic factors alone cannot explain hierarchies in animal communities and that interactions are crucial. Hierarchy as a self-organization phenomenon due to social dynamics is now the most widespread hypothesis (pp. 40–41).

#### A. The Bonabeau model
- Empirical motivation: laboratory experiments hint at a positive feedback mechanism (winner/loser effects), where winning raises the chance of winning later. Memory also matters: cockroaches removed and reinserted do not regain their rank immediately (p. 41).
- Setup: agents on an $L\times L$ square lattice, one per site, density $\rho$ (the control parameter). Each agent random-walks to a neighboring site. If the site is free it moves in. If occupied, a fight occurs and the winner gets the site. If the attacker wins, the two swap positions (p. 41).
- Strength $F$ grows with fights won. The probability that $i$ beats $j$ is a Fermi function (p. 41):
$$Q_{ij}=\frac{1}{1+\exp\{-\eta[F_i-F_j]\}}\tag{48}$$
- $\eta$ is a sort of inverse temperature. For $\eta\to\infty$ the stronger agent always wins. For $\eta\to0$ both win with probability $1/2$ (p. 41).
- A win/loss changes strength by $\pm1$. Memory is a relaxation: all strengths decrease by a constant fraction $\mu$ per time step (p. 41).
- Order parameter: the variance of the winning probabilities in the stationary state (p. 41):
$$\sigma=\langle Q_{ij}^2\rangle-\langle Q_{ij}\rangle^2\tag{49}$$
- $\sigma=0$ for an egalitarian society and $\sigma>0$ for a hierarchical one (p. 41).
- Simulations usually start with all strengths zero. One iteration is a sweep over all agents. Main result: there is a critical density $\rho_c(\eta,\mu)$. For $\rho<\rho_c$ society is egalitarian; for $\rho>\rho_c$ a hierarchy forms (p. 41).
- Mechanism: at low density fights are rare and relaxation keeps strengths near zero. At high density the strength growth of some agents is not counterbalanced by relaxation (p. 41).

**1. Mean field solution.** Mean field means no spatial correlations; $\rho$ is the probability that two agents meet and fight (p. 41).
$$\frac{dF_i}{dt}=H_i(\{F_j\})=-\mu F_i+\frac{\rho}{N}\sum_{j=1}^{N}\frac{\sinh\eta(F_i-F_j)}{1+\cosh\eta(F_i-F_j)}\tag{50}$$
- The mean strength $\langle F\rangle$ decays exponentially to zero, so all stationary states have $\langle F\rangle=0$ (p. 41). *(added step: summing (50) over $i$, the fight term is antisymmetric in $i,j$ and cancels, so $d\langle F\rangle/dt=-\mu\langle F\rangle$.)*
- Stability of the egalitarian solution $F_i=0\ \forall i$ comes from the $N\times N$ Jacobian (p. 41):
$$H_{ij}=\frac{\partial}{\partial F_j}R_i(0,0,\dots,0)=\left(-\mu+\frac{\rho\eta}{2}\right)\delta_{ij}-\frac{\rho\eta}{2N}\tag{51}$$
- There are only two distinct eigenvalues: $-\mu<0$ and $\rho\eta/2-\mu$ (large $N$). The second is negative only for $\rho<\rho_c(\eta,\mu)=2\mu/\eta$ (p. 41).
- *(added step: $\sinh x/(1+\cosh x)=\tanh(x/2)$, whose slope at 0 is $1/2$. This gives the $\rho\eta/2$ terms. The matrix is $aI-bJ$ with $J$ the all-ones matrix. The all-ones vector has eigenvalue $a-bN=-\mu$. Vectors orthogonal to it have eigenvalue $a=-\mu+\rho\eta/2$.)*
- For $\rho>\rho_c$ the egalitarian solution is linearly unstable and a hierarchy emerges (p. 41).
- For $\eta<2$ the transition is discontinuous (subcritical bifurcation at $\rho_c$). There are metastable states besides the egalitarian one, so hierarchy can appear even for $\rho<\rho_c$, and simulations depend strongly on initial conditions (p. 41).
- For $\eta\ge2$ the bifurcation is critical: continuous transition, critical exponents and critical slowing down (p. 41).

*Intuition note:* Each fight pushes the winner up, and relaxation pulls everyone back to zero. When fights are frequent enough ($\rho>2\mu/\eta$) the push beats the pull, and small differences grow.

**2. Modifications of the Bonabeau model (p. 42).**
- Most popular modification (Stauffer 2003b): replace $\eta$ in (48) with the standard deviation $\sigma$ of (49). This gives a feedback between the current hierarchy and the dominance relations (p. 42).
- Mean-field analysis (Lacasa and Luque 2006) shows the egalitarian fixed point is stable at all densities. This is at odds with simulations, which support a transition to hierarchy (Malarz et al. 2006) (p. 42).
- The discrepancy is explained by a saddle-node bifurcation above a critical density: egalitarian and hierarchical fixed points are both stable, and the endpoint depends on initial conditions (p. 42).
- The model was simulated on regular lattices, complete graphs and scale-free networks. The transition holds in every case. On scale-free networks the critical density may tend to zero for infinitely many agents (p. 42).
- On the lattice, the society is equally divided into leaders and followers, which is not realistic. If a loser's strength changes more than a winner's, the fraction of leaders drops rapidly with the asymmetry (p. 42).
- Moving-rule variants (Odagaki and Tsujiguchi): *Timid* agents avoid fights, move to a free site if any, else fight the weakest neighbor. Two transitions occur with density: a continuous one (middle class) and a discontinuous one (class of winners). *Challenging* agents pick the strongest neighbor. Hierarchies emerge at low density, and spatial domains form at low and intermediate densities (p. 42).

#### B. The Advancement–Decline model (Ben-Naim and Redner 2005)
- Integer strengths, pairwise interactions. Advancement is deterministic: the stronger agent gains one unit, and both advance if equal. Decline: each strength drops by one unit at rate $r$ while positive. $r$ sets the balance (p. 42).
- Mean field: $f_j(t)$ is the fraction of agents with strength $j$, and $F_k=\sum_{j=0}^k f_j$. The cumulative distribution obeys a non-linear master equation (p. 42):
$$\frac{dF_k}{dt}=r(F_{k+1}-F_k)+F_k(F_{k-1}-F_k)\tag{52}$$
- The first two terms are decline and the other two advancement. Initially $f_0(0)=1$, i.e. $F_k(0)=1\ \forall k\ge0$. The reflecting wall at $k=0$ is imposed by $F_{-1}(t)=0$ (p. 42).
- Continuous strength limit (p. 42):
$$\frac{\partial F(k,t)}{\partial t}=[r-F(k,t)]\frac{\partial F(k,t)}{\partial k}\tag{53}$$
- *(added step: use $F_{k\pm1}-F_k\approx\pm\partial_kF$.)*
- For $t\to\infty$ at finite strength, with $F(k,\infty)\le1$, Eq. (53) leaves two possibilities (p. 42):
$$F(k,\infty)=r\ \ (r<1);\qquad \partial F(k,\infty)/\partial k=0\ \ (r\ge1)\tag{54}$$
- For $r\ge1$ all agents have finite strength in the stationary state. For $r<1$ there is a hierarchy: a fraction $r$ with finite strength (lower class) and a fraction $1-r$ whose strength diverges with $t$ (middle class) (p. 42).
- Dimensional analysis shows the middle-class strength grows linearly in $t$. Try $F_k\sim\Phi(x)$, $x=k/t$, $\Phi(\infty)=1$. Eq. (53) becomes (p. 42):
$$x\Phi'(x)=(\Phi(x)-r)\Phi'(x)\tag{55}$$
- Its solution is (p. 42):
$$\Phi(x)\sim\begin{cases}x+r,&x<1-r\\1,&x\ge1-r\end{cases}\tag{56}$$
- *(added step: $\partial_tF=-(x/t)\Phi'$ and $\partial_kF=\Phi'/t$. Then $\Phi'=0$ or $x=\Phi-r$.)*
- Hence the maximum strength is $(1-r)t$, growing linearly. At $x\to0$, $\Phi(0)=r$ recovers the lower-class fraction (p. 42).
- Later generalization (Ben-Naim et al. 2006b): the stronger agent wins with probability $p$. This gives a richer phase diagram. In some region a new egalitarian class appears whose strength distribution is peaked and moves at constant velocity, like a traveling wave. The model has been applied to sport competitions and generalized to games with more than two players (pp. 42–43).

*Intuition note:* Advancement pushes strength up and decline pulls it down. The parameter $r$ sets the balance. In the mean-field solution, for $r<1$ a fraction $r$ (the "lower class") keeps finite strength while the rest grows linearly in time; for $r\ge1$ all strengths stay finite.

### VIII. Human dynamics

#### A. Empirical data
- Email logs were a first data source. The response time $\tau$ until a message is answered has a broad distribution, roughly $1/\tau$ (Fig. 20, Eckmann et al. 2004). Eckmann et al. also report coherent self-organized structures from synchronized users. Johansen (2004) suggests $\sim1/\tau$ for human behavior without deadlines (p. 43).
- Mail correspondence (Einstein, Darwin, Freud) gives a different scaling: probability of reply in $\tau$ days is $\approx\tau^{-\alpha}$ with $\alpha=3/2$ (p. 43).
- Picture: human dynamics comes in bursts of events with short interevent times, followed by long inactivity. Interevent times typically show heavy-tailed, non-Poissonian statistics. (Alfi et al. 2007 studied reactions to conference registration deadlines; the result is not stated on these pages.) (p. 43)

#### B. Queuing models
- Barabási model (decision-based queue): each agent has a list of $L$ tasks with priorities $x_i$ from $\rho(x)$. At each step, with probability $p$ it executes the highest-priority task; with $1-p$ a random one. The executed task is replaced by a new one with priority drawn from $\rho(x)$. Simulations for $p\to1$ give a power-law tail of task waiting times with exponent $\alpha=1$ (p. 43).
- Exact solution for $L=2$ (Vázquez 2005): $1/\tau$ with an exponential cutoff at characteristic time $(\ln(2/(1+p)))^{-1}$, which diverges as $p\to1$. The limit $p\to1$ is subtle because the prefactor vanishes (p. 43).
- Gabrielli and Caldarelli: for $L=2$ at $p=1$ the model maps exactly onto invasion percolation in $d=1$. Run time statistics gives an exact waiting-time distribution $\tau^{-2}$, unlike the $1/\tau$ valid for the stationary state at $0<p<1$. The $\tau^{-2}$ behavior disappears as $p\to1$ because the prefactor vanishes (pp. 43–44).
- Summary: for $0<p<1$ deviations from stationarity relax exponentially fast. For $p\to1$ the stationary state is trivial and deviations relax so slowly that the dynamics is intrinsically nonstationary (p. 44).
- Cobham-type queue (Vázquez et al. 2006): letters arrive as a Poisson process at rate $\lambda$, responses at rate $\mu$. Priorities are $x=1,\dots,r$ and the highest is always answered. Prediction: power-law waiting times with exponent $3/2$ and cutoff time $\tau_0=1/(\mu(1-\sqrt\rho)^2)$, with traffic intensity $\rho=\lambda/\mu$ (the control parameter) (p. 44).
- At $\rho=1$ (critical) the queue length is a 1-d random walk with a lower bound at zero. The exponent $3/2$ is the return-time exponent of a random walker (p. 44).
- Other work (p. 44):
  - Hidalgo: conditions for scaling.
  - Blanchard and Hongler: time-dependent priority (aging).
  - Grinstein and Linsker: continuous priorities $x\in[0,1]$; a task is added with probability $\lambda$, and the top task is executed with probability $\mu$.
- Grinstein–Linsker results: for $\lambda=\mu<1$, a power law with exponent $3/2$. For $\lambda<\mu<1$, $\tau_0=(\mu-\lambda)^2/(4\mu(1-\lambda))$ and, as printed for $\tau\ll\tau_0$ (see Reading notes), $P(\tau)\sim e^{-\tau/\tau_0}\tau^{-5/2}$, while for $1\ll\tau\ll\tau_0$, $P(\tau)\sim\tau^{-3/2}$. A cost for switching task classes changes the asymptotics (p. 44).
- Bedogne and Rodgers: infinite list with real non-negative priorities from $\rho(x)$. A task is selected with probability increasing in priority (p. 44):
$$\Pi(x,t)=\frac{x^{\gamma}P(x,t)}{\int_0^\infty x^{\gamma}P(x,t)\,dx}\tag{57}$$
- $\gamma\ge0$ and $P(x,t)$ is the "waiting room" priority distribution. $P(\tau)$ can be found analytically and depends on $\rho(x)$. $P(\tau)\sim1/\tau$ is recovered when $\rho(x)$ is exponential (p. 44).

*Intuition note:* If you almost always do the most urgent task, low-priority tasks wait very long. This creates a heavy tail; the characteristic cutoff time diverges as $p\to1$. Which exponent you get depends on details of the protocol and whether the system is critical.

#### C. The social web
- Collaborative tagging (del.icio.us, Flickr, CiteULike): users attach free text tags to resources. Frequency–rank plots of tags co-occurring with a given tag (Fig. 21) have a power-law tail at high rank, a generalized Zipf's law with exponent between 1 and 2, a signature of emergent hierarchical structure (p. 44).
- The exponent deserves study, because mechanisms usually invoked for Zipf's law "do not look very realistic" here. The low-rank part is flatter than strict Zipf. Possible causes: semantically equivalent competing tags (e.g. blog/blogs), and hierarchical organization, since more general tags co-occur with more tags (pp. 44–45).
- Globally, a loose categorization system emerges without coordination. The temporal autocorrelation of the tag sequence follows $1/(t+\tau)$, which suggests a heavy-tailed memory kernel for user access to the past (p. 45).
- Stochastic model of Cattuto et al. 2007: (i) a frequency-bias mechanism (users exposed to each other's tags), (ii) memory/aging with heavy-tailed access to the past. It accounts quantitatively for the data. This suggests a universal behavior of users, who appear to follow simple activity patterns (p. 45).
- Web information access (p. 45):
  - Johansen and Sornette: response to a point-like perturbation.
  - Chessa and Murre: a cognitive point-process model.
  - Dezsö et al.: visits to news documents.
  - Wu and Huberman: collective attention on Digg.
- Digg: the distribution of diggs per story is approximately log-normal. It is explained by a stochastic model (p. 45):
$$N_t=(1+r_tX_t)N_{t-1}\tag{58}$$
- $X_t$ are positive i.i.d. variables with given mean and variance. $r_t$ is a decreasing "novelty factor" with $r_1=1$, $r_t\to0$. Experimentally $r_t$ is a stretched exponential with characteristic time about one hour (p. 45).

### IX. Social spreading phenomena
- Opinion dynamics: alternatives are comparably plausible, so influence can go both ways. Rumors and news are intrinsically asymmetric: the flow is only from those who know to those who do not (pp. 45–46).
- Rumor spreading is modeled without a threshold: hearing it from one neighbor is generally enough. It resembles an epidemic (informed = infected, uninformed = susceptible). Differences (intentional spreading, perceived advantage) mostly lie in the interpretation of parameters. The field is seen as closer to epidemiology than to opinion dynamics (p. 46).
- Typical questions: how many people are reached, is there an epidemic threshold, what is the time evolution, cost and efficiency (p. 46).
- Daley–Kendall (DK) model: ignorants, spreaders, stiflers (roles as S, I, R in SIR). In SIR, infected recover spontaneously, so the transition to R is proportional to the spreader density $s(t)$. In DK, spreaders stop when they meet informed people, so the transition is proportional to $s(t)[s(t)+r(t)]$, with $r(t)$ the density of stiflers (p. 46).
- Homogeneous mixing (Sudbury): there is no threshold. For any spreading rate $\lambda$ a finite fraction $r_\infty$ is informed, given by (p. 46):
$$r_\infty=1-e^{-(1+\lambda/\alpha)r_\infty}\tag{59}$$
- $\alpha$ is the proportionality constant of the transition to R. The Maki–Thompson model gives the same result. So the nonlinear rate removes the SIR threshold. With both self-recovery and the nonlinear DK mechanism, a threshold returns, since the linear term prevails for small $s$ (p. 46).
- Complex networks: on scale-free networks $r_\infty$ is lower than on homogeneous ones, because hubs become stiflers early. But efficiency $E=r_\infty/L$ ($L$ = total traffic) is higher for scale-free networks for any parameters. In a broad parameter range they beat trivial broadcast (p. 46).
- Small-world Watts–Strogatz network (Zanette): an epidemic transition at rewiring probability $p_c$. For $p>p_c$ the rumor reaches a finite fraction. For $p<p_c$ it stays localized and $r_\infty\to0$ in the thermodynamic limit. $p_c$ stays finite for $N\to\infty$, unlike the geometric small-world threshold, which vanishes. So the transition is dynamic in nature (p. 46).
- Corruption: modeled as an epidemic with a strongly nonlinear dependence on the number of corrupt neighbors. Global coupling terms add society's response, proportional to the fraction of non-corrupt people. The phenomenology is rich (pp. 46–47).
- Dodds–Watts social contagion adds memory (repeated exposure) to SIR. Information spreading among diffusing agents has also been studied (p. 47).
- Gossip is a rumor about a person, so it is local. If only nearest neighbors of the subject can spread it, the fraction reached has a minimum as a function of degree $k$ for some empirical and model social networks. So there is an ideal number of connections to minimize gossip propagation (p. 47).

*Intuition note:* In SIR, spreaders quit spontaneously at a rate proportional to their density $s$. In the pure DK model the quitting rate is proportional to $s(s+r)$, and under homogeneous mixing the text finds no threshold: any spreading rate informs a finite fraction. If both mechanisms are present, a threshold returns because the linear term prevails for small $s$ (p. 46).

### X. Coevolution of states and topology
- Earlier sections used static networks. Real systems have node states and links changing on comparable time scales and explicitly coupled. A dissimilar contact may be cut and replaced (p. 47).
- Three ingredients: node dynamics (voter-like, majority, continuous opinion), link dynamics (deletion, addition, or rewiring, which conserves $\langle k\rangle$), and relative rate $\phi$. A random node is chosen. If it equals its neighbor(s) nothing happens. Otherwise, with probability $\phi$ it rewires a link, and with $1-\phi$ it updates its state (p. 47).
- If node dynamics leads toward consensus, it is reasonable to expect that small $\phi$ gives asymptotically a single network in one state. $\phi\to1$ splits the network into components with different consensus states. A topological phase transition separates them at $\phi_c$ (p. 47).
- Holme–Newman: Potts variables with $G$ values on nodes, $\gamma=G/N$ constant. With probability $1-\phi$ the node copies the neighbor. With $\phi$ it rewires the link to a random vertex with its own opinion. Dynamics runs until components are in full consensus (p. 47).
- Large $\phi$: clusters coincide with initial opinion holders, and the size distribution is multinomial. Small $\phi$: clusters are components of the initial graph (p. 47).
- At $\phi_c$: a power-law cluster-size distribution with exponent about $-3.5$ (Fig. 22), different from the mean-field percolation class. Finite-size scaling exponents are universal (independent of $\langle k\rangle$ and $\gamma$) and different from percolation. Critical slowing down is observed (p. 47).
- Binary variant (Vazquez et al. 2008): master equation gives an absorbing transition between an active phase for $\phi<\phi_c=(\langle k\rangle-2)/(\langle k\rangle-1)$ and a frozen phase (no active links) for $\phi>\phi_c$. In finite systems, numerical simulations show that the absorbing phase is two disconnected components (all up, all down). The active phase is one giant component (pp. 47–48).
- Nardini et al.: links rewired to completely random nodes, small rewiring rate. If the node picks the neighbor's opinion (direct voter), consensus time is logarithmic in $N$. If the neighbor is convinced by the node (reverse voter), it diverges exponentially with $N$. Mean field clarifies why, and why the consensus time stays proportional to $N$ for the "AB-model", independent of update direction (p. 48).
- Gil–Zanette (links only deleted): binary opinions on a fully connected network. Disagreeing neighbors: one copies the other with probability $p_1$; with probability $(1-p_1)p_2$ they disconnect. The stationary state depends only on $q=p_1/[p_1+(1-p_1)p_2]$ (p. 48).
  - Small $q$: two communities of similar size and opposite opinions, mostly internal links.
  - Large $q$: one single-opinion community, or one well-connected community plus poorly connected smaller ones.
  - At intermediate $q_c$ the link density has a minimum $r_c(q_c)$. Both $r_c$ and $q_c$ vanish for large systems.
- Axelrod model with coevolution (Centola et al. 2007): if overlap $\omega$ between two nodes is exactly zero, the link is cut and one agent reconnects randomly. The monocultural–fragmentation transition $q_c$ moves to much larger values: coevolution favors consensus. At $q_c$ there are cultural groups that are also disconnected subnetworks (p. 48).
- For $q=q^*>q_c$ a topological transition occurs. For $q>q^*$ the system is culturally disordered but a giant component forms again, because each vertex keeps breaking links and searching in vain for similar partners. The $q_c$ transition is explained by competing time scales of cultural and topological evolution (Vazquez et al. 2007). $q^*$ is where the time to reach a topologically stationary state is maximum (p. 48).
- Deffuant model with rewiring (Kozma and Barrat): with probability $1-w$ an opinion step with confidence bound $d$, otherwise a random rewiring. Coevolution acts oppositely on the two transitions of the static ER case. The consensus threshold $d_1$ grows with $w$. The polarized-to-fragmented threshold goes to zero: $d_2(w>0)=0$. The fragmented state vanishes because nodes can rewire and find agreeing partners (p. 48).
- Benczik et al.: Glauber zero-temperature spins. Equal-spin nodes are connected with probability $p$ and opposite-spin ones with $1-p$. There is no fragmentation. Consensus is always reached in finite systems, but exceedingly long disordered metastable states exist (p. 48).

*Intuition note:* When links follow opinions and opinions follow links, whether the network splits depends on which process is faster. Tuning that ratio gives a sharp transition with critical-like cluster sizes.

### XI. Outlook (pp. 49–50)
- The review emphasizes the statistical physics approach. Physics' role has been mainly modeling (new models, or analysis of existing models for phase transitions, universality, etc.), guided by simplicity. Simplicity helps to find universalities and mappings to known models, and physicists stress the role of scales and topology (p. 49).
- Data analysis, on synthetic and empirical data, serves to identify new phenomenology and to validate models, creating a feedback between theory and experiment (p. 49).
- Methodological wishes: interdisciplinary exchange; general classes of behavior defined by large-scale universal features, not microscopic definitions; identifying which phenomena the models actually describe. For instance, the Axelrod model has not yet been shown to describe at least semi-quantitatively any concrete situation. Without applications, modeling risks being "only a conceptual exercise" (p. 49).
- Empirical data are crucial. Research so far rarely used datasets, often insufficient to discriminate between model schemes. The web can host controlled experiments and data repositories. Traffic and pedestrian studies are cited as a successful example of reliable quantitative prediction (Helbing et al. 2007) (p. 49).
- Direction 1 — Information dynamics and the Social Web: in Web 2.0 users shape the structure of knowledge. Web games where pairs coordinate labels for pictures yield image categorization as a side effect. Tools are needed for noisy data, user interaction and the flow of data. The web could become a laboratory for opinion formation, cultural trends, consumer behavior and marketing (pp. 49–50).
- Direction 2 — Language and communication systems: language dynamics covers more than the vocabulary emergence of Sec. V. Communication systems emerge spontaneously from agent interactions. Questions include how conventions arise and the emergence of higher forms (compositionality, categories, syntax, grammar) (p. 50).
- Direction 3 — Evolution of social networks: community discovery is a major challenge. Social-network-analysis communities are based on communication relationships. For recommendation, communities of homogeneous interests matter, independent of contacts, though the two often partly overlap. Two research areas: which observable features best infer relationships (this affects the detection method), and coevolution of dynamics and substrate. Empirical data on the latter are becoming available (p. 50).
- Acknowledgments and funding (EU projects ECAgents, TAGora) follow (p. 50).

## Toy example (ours, not from the text)
Check the Bonabeau instability with $N=2$ agents, mean-field Eq. (50), $\mu=0.1$, $\eta=1$, so $\rho_c=2\mu/\eta=0.2$.
- Perturb $F_1=\varepsilon$, $F_2=-\varepsilon$. Then $F_1-F_2=2\varepsilon$ and $\sinh x/(1+\cosh x)=\tanh(x/2)$.
- $dF_1/dt=-\mu\varepsilon+\frac{\rho}{2}\left[\tanh(0)+\tanh(\eta\varepsilon)\right]\approx(-\mu+\rho\eta/2)\varepsilon$ for small $\varepsilon$.
- $\rho=0.1$: rate $=-0.1+0.05=-0.05<0$. The difference decays, so the society stays egalitarian.
- $\rho=0.4$: rate $=-0.1+0.2=+0.1>0$. The difference grows like $e^{0.1t}$; for example, after $t=10$ it is multiplied by $e^{1}\approx2.72$. So a hierarchy emerges.
- The mean $F_1+F_2$ obeys $d(F_1+F_2)/dt=-\mu(F_1+F_2)$, which stays zero.

Advancement–decline check: $r=0.3<1$. A fraction $0.3$ stays at finite strength and $0.7$ has strength growing linearly. At $t=100$ the maximum strength is $(1-r)t=0.7\times100=70$.

## Concepts
- [[linear-stability-analysis]] — Jacobian eigenvalues of the egalitarian state decide hierarchy onset in the Bonabeau model (p. 41)
- [[bifurcation]] — change of dynamics at $\rho_c$; subcritical for $\eta<2$, critical for $\eta\ge2$ (p. 41)
- [[saddle-node-bifurcation]] — in the $\sigma$-modified model, two stable fixed points coexist above a critical density (p. 42)
- [[mean-field-approximation]] — spatial correlations ignored, density is the meeting probability (p. 41)
- [[synchronization]] — Kuramoto oscillators are partially aligned for $K>K_c\propto D$ (Gaussian $g(\omega)$, $N\to\infty$) (p. 40)
- [[feedback]] — winner/loser effect and the $\sigma$-feedback in the modified Bonabeau model (pp. 41–42)
- [[order-disorder-transition]] — egalitarian/hierarchical, and consensus/fragmented network transitions (pp. 41, 47)
- [[criticality-phase-transition]] — power-law cluster sizes at $\phi_c$ with critical slowing down (p. 47)
- [[critical-slowing-down]] — stated to characterize the continuous ($\eta\ge2$) mean-field hierarchy transition, and observed at $\phi_c$ (pp. 41, 47)
- [[heavy-tail-power-law]] — $1/\tau$, $\tau^{-3/2}$ waiting times; Zipf tags (pp. 43–45)
- [[voter-model-bounded-confidence]] — voter and Deffuant dynamics used as node dynamics in coevolution (pp. 47–48)
- [[small-world-network]] — rumor transition at finite $p_c$ (p. 46)
- [[threshold-model]] — units activate above a critical neighbor density (Mexican wave); rumor models have none (pp. 40, 46)
- [[universality]] — invoked as an advantage of simple models; finite-size exponents independent of $\langle k\rangle,\gamma$ (pp. 47, 49)
- [[bonabeau-model]] (new) — lattice fighting model with Fermi win probability and relaxation (p. 41)
- [[advancement-decline-model]] (new) — integer strengths, deterministic advancement, decline at rate $r$ (p. 42)
- [[burstiness]] (new) — bursts of events separated by long inactivity, heavy-tailed interevent times (p. 43)
- [[priority-queue-model]] (new) — task execution by priority; waiting-time power laws (pp. 43–44)
- [[daley-kendall-rumor-model]] (new) — ignorants/spreaders/stiflers with nonlinear stifling (p. 46)
- [[coevolution-adaptive-network]] (new) — node states and links evolve together, with relative rate $\phi$ (p. 47)

## Canonical instances
- [[rhythmic-applause]] — Kuramoto synchronization appears and is lost in audiences (p. 40)
- [[mexican-wave]] — excitable-medium threshold model with a critical mass (p. 40)
- [[email-response-time]] — $1/\tau$ distribution; letters follow $\tau^{-3/2}$ (p. 43)
- [[collaborative-tagging]] — generalized Zipf law, heavy-tailed memory kernel (pp. 44–45)
- [[digg-collective-attention]] — log-normal diggs via a multiplicative process (p. 45)
- [[holme-newman-potts-coevolution]] — power-law cluster sizes with exponent about $-3.5$ at $\phi_c$ (pp. 47–48)
- [[axelrod-coevolution]] — link cutting at zero overlap favors consensus (p. 48)

## Bridges (candidates)
- [structural-analogy] Bonabeau/$\sigma$-model coexisting stable states above a critical density ↔ saddle-node bifurcation and hysteresis — dependence on initial conditions resembles hysteresis in tipping points.
- [same-math] Exponent $3/2$ of queue waiting time at $\rho=1$ ↔ random-walk return-time exponent — the text derives it from the walker's return-time probability.
- [structural-analogy] DK rumor threshold removal ↔ SIR epidemic threshold — only the recovery term differs.
- [structural-analogy] Holme–Newman transition at $\phi_c$ ↔ criticality/universality — power-law clusters and critical slowing down, but with exponents different from percolation.
- [structural-analogy] Digg multiplicative growth with decaying novelty ↔ heavy tails — a multiplicative process gives a skewed (log-normal) distribution.

## Questions this raises
- Why does the stationary $1/\tau$ result (for $0<p<1$) differ from the $\tau^{-2}$ obtained at $p=1$? What does "intrinsically nonstationary" mean for fitting real data?
- Which real data could discriminate between the Axelrod coevolution variants, given that the review says datasets are often insufficient to discriminate among models?
- How are the time-scale arguments for $q_c$ and $q^*$ (Vazquez et al.) made quantitative? These pages only state them.
- What sets the Zipf exponent in tagging, given that the review calls the usual mechanisms unrealistic here?

## Reading notes
- This part starts at p. 40, in the middle of the rhythmic-applause discussion (end of Sec. VI; the heading of that subsection is on an earlier page). It ends with the Outlook and acknowledgments on p. 50. Pp. 51–58 are only the bibliography and are not digested. Printed page = pdf page.
- Eq. (46): the image shows $\sin(2\pi/T+\Phi)$ (probably meant $2\pi t/T$; copied as printed). The text calls the order parameter $r(t)$ in (46) but $q(t)$ in the next sentence.
- Eq. (47): as printed, the coupling is $+\frac KN\sin(\phi_i-\phi_j)$. For this sign two equal-frequency oscillators repel, whereas the text says rotators minimize phase differences. This is probably a sign misprint in the source; copied as printed.
- Eq. (51) uses $R_i$ where Eq. (50) uses $H_i$ for the same function.
- Grinstein–Linsker paragraph (p. 44): "for $\tau\ll\tau_0$, $P\sim e^{-\tau/\tau_0}\tau^{-5/2}$" conflicts with the next range $1\ll\tau\ll\tau_0$ and is probably meant as $\tau\gg\tau_0$. There is also a stray ">" after the formula for $\tau_0$.
- Fig. 22 caption says panels (a), (b), (c) show $\phi$ above, at and below critical, but the panel labels are $\phi=0.04,\ 0.458,\ 0.96$, increasing. The caption order looks reversed.
- The "AB-model" (p. 48) is not defined on these pages. The Alfi et al. result on deadlines (p. 43) is not stated on these pages.
- The symbol $\rho$ is used for lattice density (Bonabeau), for the priority distribution, and for traffic intensity. $r$ is used for decline rate, number of priorities, and stifler density.

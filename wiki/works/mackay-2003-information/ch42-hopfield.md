---
id: mackay-2003-information/ch42-hopfield
work: mackay-2003-information
unit: "42 Hopfield Networks"
pages: 505–521
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Hopfield Networks

## L0 — One line
A fully connected network with symmetric weights and Hebbian (outer-product) learning has an energy-like Lyapunov function when its neurons are updated one at a time, so its dynamics settle into stable states that act as an associative memory, with a measurable capacity of about 0.138 I random patterns for I neurons.

## L1 — The gist (≤ 120 words)
How can a network of neurons with symmetric connections store memories and recall them from corrupted cues? Hebbian learning sets each weight to a sum of products of pattern bits. Under asynchronous updating, a Lyapunov (energy-like) function guarantees convergence to a stable state. With I neurons, the Hebb rule stores about 0.138 I random patterns, each recalled with about 1.6% of bits flipped (0.24 bits per weight); beyond that, recall fails abruptly. Optimizing the weights, as for a single neuron, does better. The energy view also lets Hopfield networks attack optimization problems such as travelling salesman, but weight scaling is delicate.

**Prerequisites:** sums and matrix–vector products; tanh and sigmoid; Gaussian tail probability Φ; binary entropy $H_2$; the single-neuron classifier of Ch. 39–40; binary symbol codes and the Kraft equality (only for the last puzzle).

## L2 — Key ideas
- A local, unsupervised Hebb rule (strengthen weights between co-active neurons) lets a partial cue trigger "pattern completion" (pp. 505–506).
- The binary Hopfield network has symmetric weights, no self-weights, threshold units, and weights $w_{ij}=\eta\sum_n x_i^{(n)}x_j^{(n)}$ (pp. 506–507).
- The activity rule equals the mean-field equations of a spin system. So an asynchronous, symmetric network has a Lyapunov function and must settle to a fixed point (p. 508).
- In simulation the memory tolerates deleted weights and corrects several flipped bits. It also has spurious states (inverses, mixtures), and overloading breaks it catastrophically (p. 510).
- The signal-versus-noise calculation gives $P(\text{unstable})=\Phi(-1/\sqrt{N/I})$. The statistical-physics capacity is $N_{\rm crit}=0.138I$, about 0.24 bits per weight (pp. 513–515).
- Training each neuron as a single-neuron classifier, with symmetrization, beats the Hebb rule (pp. 515–516).
- Hopfield–Tank map travelling salesman onto a network; weight scaling is the difficulty, and Aiyer's deterministic annealing addresses it (pp. 517–518).
- The southeast puzzle is solved by a conserved weight $2^{-l}$, as in the Kraft equality (p. 521).

## L3 — Walkthrough

### Introduction (p. 505)
- A *feedforward* network has connections forming a directed acyclic graph. Any other network is a *feedback* network (p. 505).
- The Hopfield network is fully connected, with symmetric weights: the weight from $i$ to $j$ equals that from $j$ to $i$ (p. 505).
- Two applications: associative (content-addressable) memory and optimization (p. 505).

### 42.1 Hebbian learning (pp. 505–506)
- Hebb's model: weights between positively correlated neurons increase,
$$\frac{dw_{ij}}{dt}\sim \text{Correlation}(x_i,x_j)\tag{42.1}$$
- Example: stimulus $m$ (banana smell) activates neuron $m$; stimulus $n$ (yellow sight) activates neuron $n$. If both co-occur, $w_{nm}$ and $w_{mn}$ increase. Later, stimulus $n$ alone makes $x_n$ large, and the positive weight activates $m$. This is "pattern completion" (p. 506).
- No teacher or signal is needed. The unsupervised, local learning rule and local activity rule spontaneously produce associative memory (p. 506).

*Intuition note:* weights grow between neurons whose activities are positively correlated, so part of a memory can pull up the rest. No teacher or signal is needed to say that an association should be made.

### 42.2 Definition of the binary Hopfield network (pp. 506–507)
- **Convention:** $w_{ij}$ is the connection *from* neuron $j$ *to* neuron $i$ (p. 506).
- **Architecture:** $I$ neurons; $w_{ij}=w_{ji}$; $w_{ii}=0$. Biases $w_{i0}$ are weights from a neuron 0 fixed at $x_0=1$. Activities $x_i\in\{-1,1\}$ (p. 506).
- **Activity rule:** each neuron acts like a single threshold neuron (p. 506):
$$x(a)=\Theta(a)=\begin{cases}1 & a\ge 0\\ -1 & a<0\end{cases}\tag{42.2}$$
- **Synchronous** updates: all neurons compute $a_i=\sum_j w_{ij}x_j$ (42.3), then simultaneously set $x_i=\Theta(a_i)$ (42.4). **Asynchronous** updates: one neuron at a time, in a fixed or random order. Properties may be sensitive to this choice (p. 506).
- **Learning rule:** memories $\{\mathbf x^{(n)}\}$, binary with $x_i\in\{-1,1\}$, should be stable states. Weights use the sum of outer products (Hebb rule) (p. 507):
$$w_{ij}=\eta\sum_n x_i^{(n)}x_j^{(n)}\tag{42.5}$$
$\eta$ is "unimportant" (Ex. 42.1 asks why); $\eta=1/N$ keeps the largest weight from growing with $N$ (p. 507).
- Fig. 42.2: memories as city–country strings. Pattern completion restores a partial string; error correction restores a misspelt one (p. 507).

### 42.3 Continuous Hopfield network (p. 507)
- Same architecture and learning rule, with real activities in $(-1,1)$ and a sigmoid unit (p. 507):
$$a_i=\sum_j w_{ij}x_j\tag{42.6}$$
$$x_i=\tanh(a_i)\tag{42.7}$$
- Now $\eta$ matters. Alternatively fix $\eta$ and use a gain $\beta\in(0,\infty)$: $x_i=\tanh(\beta a_i)$ (42.8) (p. 507).
- Ex. 42.2 asks where equations 42.6–42.8 have been met before (p. 507).

### 42.4 Convergence (pp. 507–508)
- Question: why should any pattern, let alone a desired memory, be stable? The text treats the continuous network, of which the binary one is a special case (p. 507).
- Equations 42.6 and 42.8 appeared in section 33.2 (variational methods). There a spin system with energy
$$E(\mathbf x;\mathbf J)=-\tfrac12\sum_{m,n}J_{mn}x_mx_n-\sum_n h_nx_n\tag{42.9}$$
was approximated by a separable distribution
$$Q(\mathbf x;\mathbf a)=\frac1{Z_Q}\exp\Big(\sum_n a_nx_n\Big)\tag{42.10}$$
and $Q$ was optimized to minimize the variational free energy (p. 508)
$$\beta\tilde F(\mathbf a)=\beta\sum_{\mathbf x}Q(\mathbf x;\mathbf a)E(\mathbf x;\mathbf J)-\sum_{\mathbf x}Q(\mathbf x;\mathbf a)\ln\frac1{Q(\mathbf x;\mathbf a)}\tag{42.11}$$
- The iterative pair
$$a_m=\beta\Big(\sum_nJ_{mn}\bar x_n+h_m\Big)\tag{42.12}$$
$$\bar x_n=\tanh(a_n)\tag{42.13}$$
was guaranteed to decrease
$$\beta\tilde F(\mathbf a)=\beta\Big(-\tfrac12\sum_{m,n}J_{mn}\bar x_m\bar x_n-\sum_nh_n\bar x_n\Big)-\sum_nH_2^{(e)}(q_n)\tag{42.14}$$
Here $H_2^{(e)}$ is, by context, a binary entropy (not defined on these pages); by comparison with 42.15 below, $q_n=(1+\bar x_n)/2$ (added step).
- Replace $J\to w$, $\bar x\to x$, $h_n\to w_{i0}$. The Hopfield equations are then identical to mean-field equations minimizing (p. 508)
$$\beta\tilde F(\mathbf x)=-\beta\,\tfrac12\mathbf x^{\mathsf T}\mathbf W\mathbf x-\sum_iH_2^{(e)}[(1+x_i)/2]\tag{42.15}$$
- **Lyapunov function:** a function that decreases under the system's dynamics and is bounded below. If a system has one, its dynamics settle to a fixed point (a local minimum of the function) or a limit cycle (along which the function is constant). Chaos is not possible, and state space divides into basins of attraction, one per attractor (p. 508).
- Conclusion: the continuous Hopfield activity rules, if implemented asynchronously, have a Lyapunov function. It is convex in each $a_i$, so the dynamics always converge to a stable fixed point (p. 508).
- This proof depends crucially on symmetric connections and on asynchronous updates (p. 508).
- Exercises 42.3 and 42.4 ask for counterexamples. Printed results (p. 520–521): with 2 neurons and $w_{12}=1$, $w_{21}=-1$, there is no stable state. With $w_{12}=w_{21}=1$, synchronous updates from $x_1=1,x_2=-1$ make both neurons flip every iteration.

*Intuition note:* the update rule is a way of sliding downhill on an energy landscape. A function that decreases and is bounded below forces the dynamics to settle. The text says the proof depends on symmetric weights and on asynchronous updates.

### 42.5 The associative memory in action (p. 510)
- Fig. 42.3: a 25-unit binary network, four 5×5 patterns (letters D, J, C, M), Hebbian learning, asynchronous updating. Starting states differing by one to five bits from a memory are restored in one or two iterations (figure caption, p. 509). A randomly perturbed memory often needs just one iteration (p. 510).
- Extra stable states: the inverse of any stable state is stable, and there are mixtures of memories. Far-away starts reach, e.g., a D–J mixture, a J–C mixture, corrupted M (2 bits off) or J (4 bits off), and the inverse of the latter (p. 509 caption, p. 510).
- **Brain damage:** setting 50 or 100 of the 300 weights to zero at random still leaves the memories as attracting stable states (p. 510).
- **More memories:** five patterns are all stable even with 26 weights deleted, but basins are smaller. From 3-bit-flipped starts only three of five memories are recovered (p. 510).
- With six patterns (Fig. 42.5) only one is stable; the others flow into one of two spurious stable states. Overloading fails catastrophically (p. 510).

### 42.6 Continuous-time continuous network (pp. 510–512)
- Motivation: the sensitivity to asynchronous versus synchronous updates might be a cause for concern for biological relevance. In continuous time the issue "melts away" (p. 510).
- Activations are instantaneous, $a_i(t)=\sum_jw_{ij}x_j(t)$ (42.16). Activities obey
$$\frac{d}{dt}x_i(t)=-\frac1\tau\big(x_i(t)-f(a_i)\big)\tag{42.17}$$
with e.g. $f=\tanh$. For steady $a_i$, $x_i$ relaxes exponentially to $f(a_i)$ with time-constant $\tau$ (pp. 510, 512).
- Result: as long as $\mathbf W$ is symmetric, the free energy (42.15) is a Lyapunov function (p. 512). Ex. 42.6: prove it by computing $d\tilde F/dt$ (p. 512).
- Remark: proof is easy if the dynamics are steepest descent on $L$. Here, "every component" of $dx_i/dt$ has a definite sign relation to $\partial\tilde F/\partial x_i$. So with an appropriately defined metric the dynamics do perform steepest descent (p. 512; sign wording: see Reading notes).

### 42.7 Capacity (pp. 512–515)
- View the memory as a communication channel (Fig. 42.6): memories are encoded into $\mathbf W$ by the Hebb rule (or another rule); the receiver sees only $\mathbf W$ and reads the stable states as the memories. Earlier, a linear threshold neuron's capacity was 2 bits per weight (p. 512).
- **Four failure modes** (p. 512): (1) corrupted bits in a memory; (2) memories absent as attractors, or with basins too small to be useful; (3) spurious memories unrelated to the desired ones; (4) spurious memories derived by mixing or inversion.
- Modes 1 and 2 are clearly undesirable, mode 2 especially. Mode 3 matters less if desired memories have large basins. Mode 4 may sometimes be beneficial: "John loves cake" stable after storing "John loves Mary" and "John gets cake" could be called generalization (p. 513).
- Capacity may be defined as the number of random patterns $N$ storable without failure mode 2 having substantial probability. Also requiring mode 1 to have tiny probability gives a much smaller capacity (p. 513).

**Stringent definition (p. 513).** Put the network in $\mathbf x^{(n)}$ (random binary patterns). The activation of neuron $i$ is $a_i=\sum_jw_{ij}x_j^{(n)}$ (42.18), with, for $i\ne j$, a signal term plus a noise term:
$$w_{ij}=x_i^{(n)}x_j^{(n)}+\sum_{m\ne n}x_i^{(m)}x_j^{(m)}\tag{42.19}$$
Substituting:
$$a_i=\sum_{j\ne i}x_i^{(n)}x_j^{(n)}x_j^{(n)}+\sum_{j\ne i}\sum_{m\ne n}x_i^{(m)}x_j^{(m)}x_j^{(n)}\tag{42.20}$$
$$\phantom{a_i}=(I-1)x_i^{(n)}+\sum_{j\ne i}\sum_{m\ne n}x_i^{(m)}x_j^{(m)}x_j^{(n)}\tag{42.21}$$
- The first term uses $(x_j^{(n)})^2=1$ (added step). The second is a sum of $(I-1)(N-1)$ independent binary quantities with mean 0 and variance 1. So $a_i$ has mean $(I-1)x_i^{(n)}$ and variance $(I-1)(N-1)$ (p. 513).
- For large $I,N$: $a_i$ is Gaussian with mean $Ix_i^{(n)}$ and variance $IN$ (Fig. 42.7). The probability that bit $i$ flips on the first iteration is the tail area:
$$P(i\text{ unstable})=\Phi\!\Big(-\frac{I}{\sqrt{IN}}\Big)=\Phi\!\Big(-\frac1{\sqrt{N/I}}\Big)\tag{42.22}$$
$$\Phi(z)\equiv\int_{-\infty}^z dz\,\frac1{\sqrt{2\pi}}e^{-z^2/2}\tag{42.23}$$
- Example: for $N\simeq0.18I$, a specified bit of a specified pattern has a 1% chance of being unstable on the first iteration (p. 514).
- **Ex. 42.7** (p. 514): require total error probability below $\epsilon$ and use $\Phi(-z)\simeq\frac1{\sqrt{2\pi}}\frac{e^{-z^2/2}}{z}$ (42.24). The exercise states the target result
$$N_{\max}\simeq\frac{I}{4\ln I+2\ln(1/\epsilon)}\tag{42.25}$$

*Intuition note:* each neuron sees a clear signal of size $I$ plus random "crosstalk" from the other memories of typical size $\sqrt{IN}$. Crosstalk grows with the number of stored patterns, so bits flip more often as $N/I$ grows.

**The statistical physicists' capacity (pp. 514–515).**
- Equation 42.22 says nothing about later iterations. Flipped bits might destabilize others, causing an avalanche that ends far from the memory (p. 514).
- For large $N/I$ avalanches happen; for small $N/I$ they tend not to. For large $I$, Amit et al. (1985) used statistical-physics methods to find numerically a sharp discontinuity at
$$N_{\rm crit}=0.138I\tag{42.26}$$
- Below it there is likely a stable state near every desired memory, with a small fraction of bits flipped. Above it only spurious "spin glass" states exist, none correlated with the memories. Just below $N_{\rm crit}$, 1.6% of bits are flipped (p. 515).
- Fig. 42.8: overlap $\sum_ix_ix_i^{(n)}/I$ is 1 for perfect recall and 0 at 50% bits flipped. It drops abruptly from 0.97 to zero at $N/I=0.138$ (p. 514).
- Other transitions (p. 515): spin glass states exist for all $N/I$. For $N/I\in(0,0.138)$ there are stable states near the memories. For $(0,0.05)$ those have lower energy than the spin glass states; for $(0.05,0.138)$ spin glass states dominate. For $(0,0.03)$ there are also mixture states, with higher energy than the memory states.
- **Capacity in bits:** $0.138I$ patterns of length $I$, each received with 1.6% of bits flipped:
$$0.138I^2\times(1-H_2(0.016))=0.122\,I^2\text{ bits}\tag{42.27}$$
With $I^2/2$ weights, this is 0.24 bits per weight. The expression omits a smaller negative term of order $N\log_2N$ bits, linked to the arbitrary order of the memories (p. 515).

*Intuition note:* the network is likely to keep a stored pattern with only small errors up to about 14 patterns per 100 neurons (for large $I$). Past that, recall collapses at once, not gradually.

### 42.8 Improving on the Hebb rule (pp. 515–516)
- Idea: define an objective measuring how well all memories are stored, then minimize it. For every neuron $i$ and pattern $n$: if the other neurons are set to $x_j=x_j^{(n)}$, then neuron $i$'s preferred output should be $x_i^{(n)}$. This is exactly the single-neuron problem of Ch. 39, with each pattern giving an input–target pair for each neuron (p. 515).
$$G(\mathbf W)=-\sum_i\sum_n\Big[t_i^{(n)}\ln y_i^{(n)}+(1-t_i^{(n)})\ln(1-y_i^{(n)})\Big]\tag{42.28}$$
$$t_i^{(n)}=\begin{cases}1&x_i^{(n)}=1\\0&x_i^{(n)}=-1\end{cases}\tag{42.29}$$
$$y_i^{(n)}=\frac1{1+\exp(-a_i^{(n)})},\;\; a_i^{(n)}=\sum_jw_{ij}x_j^{(n)}\tag{42.30}$$
(Brackets in 42.28 added for readability; the page prints no bracket.)
- **Algorithm 42.9** (Octave; p. 516). Shapes: data $\mathtt x$ is $N\times I$; $\mathtt t$ is $\mathtt x$ with $-1\to0$; $\mathtt w$ is $I\times I$.
  1. `w = x'*x` (Hebb initialization).
  2. Loop $L$ times: set the diagonal of `w` to zero; `a = x*w` ($N\times I$); `y = sigmoid(a)`; `e = t - y`; `gw = x'*e` ($I\times I$); `gw = gw + gw'` (symmetrize).
  3. Step: `w = w + eta*(gw - alpha*w)`.
- It does better than one-shot Hebb. The six patterns of Fig. 42.5, unstorable by the Hebb rule, all become stable (p. 516). Ex. 42.8 asks for empirical capacity and avalanche study (p. 516).

### 42.9 Optimization: travelling salesman (pp. 516–518)
- Hopfield networks minimize an energy, so one may map constraint-satisfaction problems onto them. Hopfield and Tank (1985) suggested designing weights so that settling minimizes the problem's objective (pp. 516–517).
- **TSP:** $K$ cities, $K(K-1)/2$ distances; find the shortest closed tour visiting each city once. It is equivalent in difficulty to an NP-complete problem (p. 517).
- **Encoding:** $I=K^2$ neurons in a square; neuron (city, place) means "this city comes at this point in the tour". States are taken in $\{0,1\}$ (p. 517).
- **Weights, role 1 (validity):** a valid state is a permutation matrix (one 1 per row and column). Enforce by large negative weights between neurons in the same row or column, plus a positive bias so that $K$ neurons turn on (Fig. 42.10b) (p. 517).
- **Weights, role 2 (objective):** negative weights proportional to distances between nodes in adjacent columns, e.g. $-d_{BD}$. In a valid state, energy = total tour distance plus a constant from the biases (pp. 517–518).
- **Difficulty:** this fails for large problems without modification. With "large" validity weights the network reaches a valid state with little regard for distances. With "small" ones, an invalid state may have lower energy than any valid one (p. 518).
- **Aiyer (1991):** modified the distance weights so they do not interfere with validity, and defined a continuous network confined to a "valid subspace". He used graduated non-convexity / deterministic annealing, increasing the gain $\beta$ from 0 to $\infty$, at which point the state is a valid tour. Fig. 42.11a: 30-city trajectories. Fig. 42.11b: a "travelling scholar" tour of 27 Cambridge Colleges, the Engineering Department, the University Library and Aiyer's house (p. 518).

### 42.10 Further exercises (pp. 519–520)
- Ex. 42.9: two memories $\mathbf m,\mathbf n$ stored with $w_{ij}=m_im_j+n_in_j$ ($i\ne j$) (42.31). Show $a_i=\mu m_i+\nu n_i$ (42.32), that $\mathbf x=\mathbf m$ is stable, and that for $\mathbf x=\mathbf m+2\mathbf d$ (42.33), with overlap $o_{\mathbf{mn}}=\sum_im_in_i$ (42.34), $\mathbf m$ is restored if $D<\tfrac14(I-|o_{\mathbf{mn}}|-2)$ (42.35) (p. 519).
- Ex. 42.10: viewing each neuron as a binary classifier, show it is almost certainly impossible to store more than $2I$ random memories in $I$ neurons (p. 519).
- Ex. 42.11 (Erik's puzzle, p. 520): live cells never die; a dead cell comes alive if two or more of its N/S/E/W neighbours are alive. Smallest number of live cells that makes an $N\times N$ square fully alive? Also the $d$-dimensional version.
- Ex. 42.12 (southeast puzzle, p. 520): pieces on a semi-infinite board start with one piece at the northwest corner. Each move replaces one piece by two, one square east and one square south, never two on a square. Can the ten squares nearest the corner all be empty? Hint: data compression.

### 42.11 Solution to the southeast puzzle (p. 521)
- Analogy with binary symbol codes: splitting a codeword in two gives two codewords, each of implicit probability $2^{-l}$ with $l$ the new depth; for a complete code the Kraft equality says these sum to 1 (p. 521).
- Give a piece weight $2^{-l}$ with $l$ the city-block distance from the top-left square. Every legal move leaves the total weight unchanged. The start weight is 1 (p. 521).
- If the ten nearest squares (distances 0–3) were empty and all other squares full, the total would be $\sum_{l=4}^\infty(l+1)2^{-l}=3/4$. Hence emptying all ten is impossible (p. 521). (Added step: $3/4$ is the maximum possible weight with those squares empty, which is below 1.)
- The text calls the total weight a Lyapunov function "of the second type", yet also calls it conserved (see Reading notes) (p. 521).

## Toy example (ours, not from the text)
Four neurons, binary, $\eta=1$, two memories $\mathbf x^{(1)}=(+1,+1,-1,-1)$, $\mathbf x^{(2)}=(+1,-1,+1,-1)$.

**Weights** $w_{ij}=x^{(1)}_ix^{(1)}_j+x^{(2)}_ix^{(2)}_j$ for $i\ne j$, with $w_{ii}=0$:
- $w_{12}=(1)(1)+(1)(-1)=0$; $w_{13}=(1)(-1)+(1)(1)=0$; $w_{14}=(1)(-1)+(1)(-1)=-2$.
- $w_{23}=(1)(-1)+(-1)(1)=-2$; $w_{24}=(1)(-1)+(-1)(-1)=0$; $w_{34}=(-1)(-1)+(1)(-1)=0$.
- So the only non-zero weights are $w_{14}=w_{41}=-2$ and $w_{23}=w_{32}=-2$.

**Stability of memory 1:** $a_1=w_{14}x_4=(-2)(-1)=2\to+1$; $a_2=w_{23}x_3=(-2)(-1)=2\to+1$; $a_3=w_{32}x_2=-2\to-1$; $a_4=w_{41}x_1=-2\to-1$. All four match $\mathbf x^{(1)}$. Memory 2 checks the same way. The stable states are exactly those with $x_4=-x_1$ and $x_3=-x_2$. These are $\pm\mathbf x^{(1)}$ and $\pm\mathbf x^{(2)}$, so inverses are stable, as the text observes for its network (p. 510).

**Error correction:** start at $(-1,1,-1,-1)$ (bit 1 flipped). Update neuron 1: $a_1=w_{14}x_4=(-2)(-1)=2\to+1$. State restored to $\mathbf x^{(1)}$ in one update.

**Energy** (term $-\tfrac12\mathbf x^{\mathsf T}\mathbf Wx=2(x_1x_4+x_2x_3)$ here, since the sum counts each pair twice): at $(-1,1,-1,-1)$: $2(1-1)=0$; at $\mathbf x^{(1)}$: $2(-1-1)=-4$. It decreased.

**Synchronous failure:** from $(1,1,1,1)$, all $a_i=-2$, so the state becomes $(-1,-1,-1,-1)$; then all $a_i=+2$ and it returns. A 2-cycle. Asynchronously, update neuron 1: $(−1,1,1,1)$ (energy 4 → 0). Update neuron 2: $a_2=-2x_3=-2\to-1$, giving $(-1,-1,1,1)=-\mathbf x^{(1)}$ (energy $-4$), a fixed point.

## Concepts
- [[hopfield-network]] (new) — fully connected, symmetric, no self-weights; stable states act as memories (p. 505, 506)
- [[hebb-rule]] (new) — $w_{ij}=\eta\sum_nx_i^{(n)}x_j^{(n)}$: local, unsupervised outer-product learning (p. 505, 507)
- [[associative-memory]] (new) — content-addressable memory that does pattern completion and error correction (p. 505, 507)
- [[lyapunov-function]] (new) — function that decreases along the dynamics and is bounded below; implies settling to a fixed point or limit cycle, no chaos (p. 508)
- [[basin-of-attraction]] (new) — set of initial states flowing to a given attractor (p. 508)
- [[spurious-stable-state]] (new) — stable state not a desired memory: inverses, mixtures, spin glass states (pp. 510, 512, 515)
- [[hopfield-capacity]] (new) — number of random patterns storable, here $0.138I$ with 1.6% flipped bits, 0.24 bits/weight (pp. 513–515)
- [[variational-inference-elbo]] — here the Hopfield activity rule equals mean-field minimization of variational free energy (p. 508)
- [[noisy-channel]] / [[channel-capacity]] — memory viewed as a channel from memories to weights to stable states; capacity counted in bits (p. 512, 515)
- [[prefix-code-kraft-inequality]] — the conserved weight $2^{-l}$ in the southeast puzzle (p. 521)
- [[deterministic-annealing]] (new) — raise gain $\beta$ from 0 to $\infty$ to reach a valid TSP tour (p. 518)

## Canonical instances
- [[hopfield-letter-memory]] — 25-unit network storing D, J, C, M; robust to errors and damage (pp. 509–510)
- [[hopfield-overload]] — six patterns: one stable, rest flow to spurious states (pp. 510–511)
- [[hopfield-tsp]] — $K^2$ neurons encode city-at-place; Aiyer's annealed solution (pp. 517–518)
- [[southeast-puzzle]] — conserved weight shows ten squares cannot be emptied (pp. 520–521)
- [[two-neuron-nonconvergence]] — asymmetric or synchronous examples with no fixed point (pp. 520–521)

## Bridges (candidates)
- [same-math] Hopfield activity rule ↔ bayesian: mean-field variational inference with a factorised $Q$ — the unit states the equations are identical (p. 508).
- [same-math] Per-neuron objective $G(\mathbf W)$ ↔ information-theory: cross-entropy loss of logistic regression — (42.28) is the single-neuron objective of Ch. 39.
- [structural-analogy] Capacity in bits per weight ↔ information-theory: channel capacity — memories pass through weights and attractors as through a noisy channel.
- [structural-analogy] Southeast conserved weight $2^{-l}$ ↔ information-theory: Kraft equality for complete binary codes — splitting preserves the sum.

## Questions this raises
- The Hebb rule gives 0.24 bits per weight, while a single neuron reaches 2 bits per weight. How close can any learning rule come (cf. Ex. 42.10, the $2I$ bound)?
- How does the optimized rule of Algorithm 42.9 compare in capacity and avalanche behaviour (Ex. 42.8)?
- Can mixture-state "generalization" (mode 4) be made useful on purpose, or controlled?
- How should validity and distance weights in TSP be scaled, other than by Aiyer's modification?

## Exercises worth doing
- Ex. 42.1 (p. 507) — why $\eta$ does not matter for the binary network — difficulty: easy
- Ex. 42.5 (p. 510) — simulate a network; test robustness to deleted weights — difficulty: medium
- Ex. 42.6 (p. 512) — prove $\tilde F$ is a Lyapunov function in continuous time — difficulty: easy
- Ex. 42.7 (p. 514) — derive $N_{\max}$ from the Gaussian tail — difficulty: medium
- Ex. 42.9 (p. 519) — two-memory analysis; correctable bit flips — difficulty: medium
- Ex. 42.10 (p. 519) — Hopfield network as per-neuron classifiers; $2I$ bound — difficulty: medium

## Reading notes
- Printed page = pdf − 12 (pdf 517 = printed 505). Running headers show "42 — Hopfield Networks".
- The weight matrices in Figs. 42.3 and 42.4 and the figure panels are images; they are not transcribed here.
- p. 512: the steepest-descent remark prints $\frac{d}{dt}x_i\propto\frac{\partial}{\partial x_i}L$ and says components of $dx_i/dt$ have "the same sign as" $\partial\tilde F/\partial x_i$. Descent needs the opposite sign. Equation 42.17 has a minus sign, so I read this as a misprint or loose wording.
- p. 521: the weight is called a Lyapunov function "of the second type" (bounded below, decreasing or constant), yet it is said to be conserved. A conserved quantity fits the first type as listed on that page.
- p. 510: "20% of its components are destroyed" is loose. Deleting 50 or 100 of 300 weights is about 17% or 33%.
- The text uses both $N\simeq0.18I$ (1% first-step bit error) and $N_{\rm crit}=0.138I$ (avalanche threshold). They are different quantities.
- $q_n$ in 42.14 and the notation $H_2^{(e)}$ are not defined in this unit; the text points to section 33.2 for the variational derivation, presumably where they were introduced.
- Solutions are printed only for Exercises 42.3, 42.4 and 42.12; Ex. 42.11's answer is not in this unit.

---
id: mackay-2003-information/ch16-message
work: mackay-2003-information
unit: 16 Message Passing
pages: 241-247
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Message Passing

## L0 — One line
A global quantity that splits into separately computable parts can be computed by simple local messages passed between neighbouring nodes, without listing all the possibilities.

## L1 — The gist (≤ 120 words)
How can a global quantity be computed using only simple, local operations? MacKay shows that if the quantity is separable, neighbours can pass small messages. He demonstrates this with soldiers counting themselves (in a line, then in a tree), with counting the paths through a grid (sum–product, forward and backward passes, uniform path sampling), and with the lowest-cost route through a graph (min–sum, or Viterbi). Cycles break the simple counting rules. Some global functions are not separable; finding low-cost solutions for them is called a challenge. The min–sum algorithm is later used to decode error-correcting codes.

**Prerequisites:** basic graphs (nodes, edges, directed edges, cycles); addition and minimum; simple probability.

## L2 — Key ideas
- Message passing means simple processors exchange simple messages locally, and a global problem gets solved (p. 241).
- Counting soldiers in a line works because the total is the number in front plus the number behind plus one, and the two parts are separated by the commander (p. 242).
- With cycles, "in front" and "behind" are unclear, so rule-set A fails. On a cycle-free graph (a tree), rule-set B lets any node deduce the total (pp. 242–243).
- The number of paths to a grid node is the sum of the path counts of its upstream neighbours, so no path is ever enumerated (p. 244).
- A backward pass plus the forward pass gives the paths through each node. Multiplying the two messages, then dividing by the total, gives the probability that a random path uses that node (p. 244).
- A uniform random path needs biased coin flips, with biases proportional to the backward messages. In the five-path grid of Figure 16.8, fair coins at each junction cannot give a uniform sample (p. 247).
- In min–sum (Viterbi), each node adds edge costs to incoming messages and keeps the minimum; it finds the lowest-cost path and the critical path (pp. 245–246).
- Not every global function is separable; birthdays, largest equal-height group and the travelling salesman tour are examples (p. 246).

## L3 — Walkthrough

### 16.1 Counting
**Idea.** Simple distributed hardware, with local messages, can solve a global problem (p. 241).

**Expensive solution.** The commander shouts and every soldier shouts back. This needs a reliable channel to every soldier, a commander who can listen to all of them and count, and well-fed soldiers (p. 241).

**Cheap solution: rule-set A (Algorithm 16.1).** Each soldier can say single integers to the two adjacent soldiers and can add one (p. 241).
1. The front soldier says "one" to the soldier behind.
2. The rearmost soldier says "one" to the soldier in front.
3. A soldier who hears a number from one side adds one and says the new number to the other side (p. 241).

The commander adds the number from the soldier in front, the number from the soldier behind, and one for himself. In Figure 16.2 this is 3 + 1 + 1 = 5 soldiers (p. 242). Only local communication, storage and integer addition are needed (p. 242).

**Separation.** The total equals (number in front of a point) + (number behind it). The two parts can be computed separately because the commander separates the groups (p. 242).

**Cycles.** For a swarm of guerillas (Figure 16.3), rule-set A fails. It is unclear who is in front or behind. Also, if the connection graph has cycles, a guerilla in a cycle (such as "Jim") cannot split the group in two (p. 242).

**Rule-set B (Algorithm 16.5)** works if the connections form a cycle-free graph, called a tree (pp. 242–243). Each guerilla follows four rules:
1. Count your neighbours, $N$.
2. Count the messages received, $m$, with values $v_1,\dots,v_N$. Let $V$ be their running total.
3. If $m=N-1$, tell the one neighbour who has not yet sent a message the number $V+1$.
4. If $m=N$, then (a) $V+1$ is the required total, and (b) say to each neighbour $n$ the number $V+1-v_n$ (p. 243).

*Intuition note.* A message to a neighbour says how many nodes lie on your side of the link. A node that has heard from everyone knows the total. Each neighbour is then told the total minus what that neighbour already contributed.

### 16.2 Path-counting
**Problem.** Valid paths run from A to B by rightward and downward moves on a grid (Figure 16.6). The questions are (1) how many paths there are, (2) the probability that a random path passes through a given node, and (3) how to select a random path. "Random" means all paths are equally likely (p. 244).

**Why it is hard.** The number of paths is expected to be large. Even a diagonal strip three nodes wide gives about $2^{N/2}$ paths (p. 244).

**Forward pass.** Every path to P enters through an upstream neighbour (above or to the left), M or N (Figure 16.7). So the number of paths from A to P is the number from A to M plus the number from A to N (p. 244). A node sends the sum of its incoming messages downstream once it has all of them. In the example (ten vertices, twelve directed edges), the number 5 emerges at B. Figure 16.9 shows the five paths as a check (p. 244).

**Probability of passing through a node.** A backward pass is added. At each vertex, the forward message times the backward message is the number of paths through that vertex. Dividing by the total number of paths gives the probability. In Figure 16.10 four paths pass through the central vertex, so the probability is 4/5 (p. 244; division by 5 is an added step). Figure 16.11 shows the result for the triangular $41\times 41$ grid, with blob area proportional to probability (p. 244).

**Random path sampling.** Exercises 16.1 and 16.2 ask about this (pp. 244–245). The solutions are:
- Fair coin flips at each junction give path probabilities that are powers of 1/2. The grid of Figure 16.8 has five paths, which must each have probability 1/5, so coin flips cannot sample uniformly (p. 247).
- A uniform sample uses a different biased coin at each junction, with biases proportional to the backward messages of the two options. For example, at the first choice after leaving A, a "3" message comes from the East and a "2" from the South, so go East with probability 3/5 and South with probability 2/5 (p. 247).

*Intuition note.* The backward message of an option says how many complete paths continue through it. Choosing in proportion to those counts gives every full path the same chance.

**Sum–product.** This is the name of the algorithm used for counting. The "sum" is the addition of incoming messages. The "product" can be seen by treating the sum as a weighted sum in which all weights are 1 (p. 245).

### 16.3 Finding the lowest-cost path
**Setup.** Travel from Ambridge (A) to Bognor (B) in the graph of Figure 16.12, with edge costs in hours. For example, A–I–L–N–B costs 8 hours. The goal is to avoid evaluating every path, by finding for each node the cost of the cheapest path to it from A ("the cost of $x$") (p. 245).

**Min–sum (Viterbi) algorithm.** A node broadcasts its cost to its descendants once it knows the costs of all its predecessors. Each edge adds its cost to the message (p. 245).
- A has cost 0. H has cost 4 and I has cost 1. J has cost 6 and L has cost 2 (p. 245).
- K receives 5 (via H) and 3 (via I). It takes the minimum, 3, and keeps only edge I–K, pruning the other edge into K (p. 245).
- Two more iterations (Figure 16.13d, e) show a path A to B of cost 6. Figure 16.13 shows M with cost 5 and N with cost 4 (pp. 245–246).
- If there is a tie, any minimum route may be picked at random (pp. 245–246).
- Backtracking from B along surviving edges gives the lowest-cost path A–I–K–M–B (p. 246).

**Other applications.** The min–sum algorithm finds the critical path of a production process, meaning the operations whose speed-up would shorten the time from raw materials to product. In Chapter 25 it is used to decode error-correcting codes (p. 246).

*Intuition note.* In path counting a node adds its incoming messages; in min–sum a node adds the edge cost to each incoming message and keeps the smallest (our comparison). Remembering the winning edge lets you trace the best path back.

### 16.4 Summary and related ideas
Some global functions are separable. The number of paths from A to P splits into the number to M plus the number to N, and such functions can be computed efficiently by message passing (p. 246). Examples that lack such separability are (1) the number of pairs of soldiers sharing a birthday, (2) the size of the largest group sharing a height (to the nearest centimetre), and (3) the length of the shortest tour visiting every soldier (p. 246). Finding low-cost solutions to such problems is described as a challenge of machine learning. A neural approach (Hopfield and Brody) can find a large subset of approximately equal variables. A neural approach to the travelling salesman problem is deferred to section 42.9 (p. 246).

### 16.5–16.6
Further exercises: 16.3 (asymptotics of Figure 16.11a) and 16.4 (the integral image, equation 16.1) (p. 246). The solutions printed in this unit are those to Exercises 16.1 and 16.2, given above (p. 247).

## Toy example (ours)
A star-shaped tree: centre $c$ joined to leaves $x$, $y$, $z$ (4 nodes). Apply rule-set B.
- Each leaf has $N=1$, $m=0=N-1$, $V=0$. So each tells $c$ the number $V+1=1$.
- $c$ has $N=3$ and receives $v_x=v_y=v_z=1$, so $V=3$. Since $m=N$, the total is $V+1=4$ ✓.
- $c$ tells $x$ the number $V+1-v_x=4-1=3$, and likewise 3 to $y$ and $z$.
- Leaf $x$ now has $m=N=1$, $V=3$, so its total is $V+1=4$ ✓. Every node agrees.

## Concepts
- [[message-passing]] (new) — local nodes exchange simple messages to compute a global quantity (p. 241)
- [[separability]] (new) — a global function splits into parts computable separately, e.g. in front plus behind (p. 242)
- [[tree-cycle-free-graph]] (new) — graph without cycles; rule-set B is designed for such graphs (p. 242)
- [[sum-product-algorithm]] (new) — nodes sum incoming messages; used here to count paths, a weighted sum with weights 1 (p. 245)
- [[min-sum-viterbi-algorithm]] (new) — nodes add edge costs and keep the minimum incoming cost; finds the cheapest path (p. 245)
- [[forward-backward-passes]] (new) — forward times backward messages give paths through a node (p. 244)

## Canonical instances
- [[soldiers-counting]] — local counting of soldiers in a line and of guerillas in a tree (pp. 241–243)
- [[grid-path-counting]] — counting and sampling paths through a grid (p. 244)
- [[ambridge-bognor-route]] — min–sum on a route graph, lowest cost 6 hours (pp. 245–246)
- [[critical-path-production]] — critical path of a production process by min–sum (p. 246)

## Bridges (candidates)
- [structural-analogy] sum–product message passing ↔ bayesian: computing marginal probabilities by local sums over a graph — the text itself calls path counting a sum–product example.
- [same-math] min–sum on a graph ↔ information-theory: decoding of error-correcting codes — the text says Chapter 25 uses min–sum for decoding.
- [structural-analogy] sampling a path with probabilities from backward messages ↔ bayesian: sampling from a posterior using conditional probabilities.

## Questions this raises
- What can be done when the graph has cycles and the simple rules fail?
- How do real-valued weights in the "product" part change the sum–product rule?
- Which separable and non-separable functions arise in inference problems?
- Why does min–sum decode codes (Chapter 25)?

## Exercises worth doing
- Ex. 16.1 (p. 244) — why fair coin flips fail to give uniform paths — difficulty: easy
- Ex. 16.2 (p. 245) — how to sample uniformly using the forward and backward messages — difficulty: medium
- Ex. 16.3 (p. 246) — asymptotic properties of the probabilities in Figure 16.11a — difficulty: medium
- Ex. 16.4 (p. 246) — computing the integral image by message passing, and rectangle sums — difficulty: medium

## Reading notes
- Printed page = pdf page − 12.
- The text layer of Figures 16.10 and 16.13 is garbled. I checked the figure images for the numbers used (the central vertex, and costs of M and N).
- Algorithm 16.1 and Algorithm 16.5 are called rule-set A and rule-set B in the text.

---
id: rosvall-2008-maps/main-p1
work: rosvall-2008-maps
unit: paper (part 1/3)
pages: pdf 1–21
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Maps of random walks on complex networks reveal community structure (part 1/3)

## L0 — One line
Finding modules in a directed, weighted network is the same problem as finding the shortest two-level code for a random walk on it, and the expected per-step length of that code (a Shannon limit) is the "map equation".

## L1 — The gist (≤ 120 words)
Question: how can we split a network into modules while keeping link direction and weight? The authors use a random walk as a stand-in for information flow. They give modules unique names and reuse node names inside modules, like street names across cities. The average code length per step, L(M), is the map equation. The best partition minimizes L(M); it is found by greedy merging plus simulated annealing. Unlike modularity, this approach follows flow. It gives different partitions on two small test networks. Applied to citations among 6,128 journals, it yields an 88-module map of science with a directional applied-to-basic citation pattern.

**Prerequisites:** entropy, Huffman code, Shannon's source coding bound; Markov chain steady state; basic graph terms (directed, weighted links).

## L2 — Key ideas
- A good map is a good compression. A code that exploits regularities of the flow measures how well a map simplifies without losing structure (pdf 1).
- A random walk is the proxy for flow because it uses only the information in the network diagram (pdf 1).
- Two-level code: modules get unique names, node names inside modules are reused, and an exit codeword marks leaving a module. In Fig. 1 this lowers the limit L from 4.50 to 3.05 bits/step (pdf 3).
- Map equation: $L(\mathsf M)=q_{\curvearrowright}H(\mathcal Q)+\sum_i p^i_{\circlearrowright}H(\mathcal P^i)$. Here $q_{\curvearrowright}$ is the chance per step of switching modules, $H(\mathcal Q)$ the entropy of module names, $H(\mathcal P^i)$ the entropy of moves inside module $i$ (exit included), and $p^i_{\circlearrowright}$ the weight of module $i$. Community detection is to minimize it over partitions (pdf 3, 8).
- Teleportation (with probability τ = 0.15 the walker jumps to a random node) makes directed walks ergodic (a unique long-run visit distribution) and turns the walker into the "random surfer" of Google's PageRank (pdf 3, 9).
- Map equation and modularity (a score comparing in-module link weight with its expected value) can disagree. In Fig. 2, modularity prefers heavy links inside modules, while the map equation prefers long persistence of flow. Where links induce no flow, the map equation returns one module (pdf 4).
- Search: greedy merging of modules, then a refinement step by simulated annealing (the heat-bath algorithm is used). Greedy search has partitioned networks of 2.6 million nodes and 29 million links (pdf 9).
- Science map: 6,128 journals, 88 modules. It shows a structure more like a U than a ring, joined mainly by a backbone of medicine, molecular biology, chemistry and physics, and citations flowing from applied to basic fields. Mapping a subset of the nodes is expected to give finer modules, as Fig. 4 illustrates (pdf 7).

## L3 — Walkthrough

### Abstract and Introduction (pdf 1)
- The method decomposes a network into modules by optimally compressing a description of information flow. The result is a "map" that simplifies the network and highlights regularities (pdf 1).
- A good map balances two errors: omitting important structure through oversimplification, and burying relationships in detail. Information theory lets the authors measure map efficiency and the detail lost (pdf 1).
- Links in complex systems are weighted, directional, interdependent and conductive. So modules should be found from flow: a group among which information flows quickly is described as one module (pdf 1).
- Why a random walk: it uses all the information in the network representation and nothing more. It is a default dynamics derived from the diagram alone (pdf 1).
- The authors say they thereby show that finding community structure is equivalent to solving a coding problem (pdf 1).

*Intuition note:* If a walker stays inside a cluster for a long time, the cluster can be named once. Then the walk can be described in fewer bits (as in Fig. 1C).

### Describing a path on a network (pdf 1–2)
- Communication game: both parties know a weighted directed network. They want a code for random-walk paths whose words refer to network structure (pdf 1).
- Pure compression would encode at the entropy rate of the Markov process, with a separate dictionary per node (pdf 1–2). The authors reject this because a codeword then changes meaning with location. A map needs names that stay unique for important structures (pdf 2).
- Fig. 1A: a weighted network with n = 25 nodes and one 71-step walk (pdf 2).

### Huffman coding (pdf 2)
- A Huffman code gives short words to common nodes and long words to rare ones. Codeword lengths come from the ergodic visit frequencies (pdf 2).
- Fig. 1B: the 71-step walk costs 314 bits. A uniform code needs $\lceil\log 25\rceil=5$ bits per node, so $71\cdot5=355$ bits (pdf 2).
- Source coding theorem (as used here): for a random variable with state frequencies $p_i$, the average codeword length is no less than $H(X)=-\sum_1^n p_i\log p_i$ (pdf 2). The authors write $L$ for this lower bound. Fig. 1B has $L=4.50$ bits/step (pdf 2).

### Highlighting important objects (pdf 2–3)
- One-level naming gives efficient names but no map. The two-level description keeps unique names for modules and reuses names for nodes within modules (pdf 3).
- City analogy: cities have unique names, street names are reused. This causes little confusion because most routes stay within one city (pdf 3).
- Each module has its own Huffman code. A special exit codeword is part of that code. It is always followed by the module code of the new module (pdf 3).
- Fig. 1C: the two-level code describes the walk in 243 bits, on average 32% shorter. The limit is $L=3.05$ vs 4.50 bits/step (pdf 2–3).
- Fig. 1D shows only module names: the map (pdf 2–3).

**Map equation** (pdf 3):
$$L(\mathsf M)=q_{\curvearrowright}H(\mathcal Q)+\sum_{i=1}^{m}p^{i}_{\circlearrowright}H(\mathcal P^{i}).\tag{1}$$
- $q_{\curvearrowright}$ is the probability that the walk switches modules on a step. $H(\mathcal Q)$ is the entropy of module names. $H(\mathcal P^i)$ is the entropy of movements within module $i$, exit included. $p^i_{\circlearrowright}$ is the fraction of within-module movements in $i$ plus the exit probability of $i$, so $\sum_i p^i_{\circlearrowright}=1+q_{\curvearrowright}$ (pdf 3).
- The best code corresponds to the partition $\mathsf M$ of $n$ nodes into $m$ modules that minimizes (1) (pdf 3).

*Intuition note:* Eq. 1 is the cost of "which city" (weighted by how often we change city) plus the cost of "which street, or leave" (weighted by time spent in each city).

- Search: ergodic visit frequencies come from the power method. Partitions are explored by deterministic greedy search, refined by simulated annealing with the heat-bath algorithm (pdf 3).

### Directed networks and teleportation (pdf 3)
- Fig. 1 is undirected for simplicity, but the method handles directed weighted links. The map equation is unchanged. The walk is modified for ergodicity, meaning a unique long-run visit distribution (pdf 3).
- With probability τ the walker jumps to a random node anywhere. This is the "random surfer" of PageRank (pdf 3).
- Results are robust to τ. For the network in Fig. 1, the optimal partition is unchanged as long as τ < 0.45. The stronger the regularities, the higher τ may be before teleportation swamps structure. The authors use τ = 0.15 (damping d = 0.85) (pdf 3).

### Mapping flow compared to maximizing modularity (pdf 3–4)
- Traditional methods ignore link direction and weight. Modularity optimization does use them (pdf 3).
- Modularity for $m$ modules (sum of in-module link weight minus its expected value):
$$Q=\sum_{i=1}^{m}\left(\frac{w_{ii}}{w}-\frac{w_i^{\mathrm{in}}w_i^{\mathrm{out}}}{w^{2}}\right).\tag{2}$$
$w_{ii}$ is the weight of links inside module $i$. $w_i^{\rm in}, w_i^{\rm out}$ are its total in- and out-weights. $w$ is the total weight. $Q$ is maximized over all assignments (pdf 3).
- Conceptual difference: Eq. 1 finds the essence of a network in the flow patterns its structure induces. Eq. 2 finds it in combinatoric properties of links (pdf 3).
- **Fig. 2A:** the left partition (four clusters with long persistence) has $L=2.67$ bits/step and $Q=0.25$. The right partition has $L=4.13$ and $Q=0.50$ (pdf 4).
  - In the left clusters, with bold links at twice the weight of others and no teleportation, a walker takes on average 3 steps in a module before exiting. In the right clusters it takes only 12/5 steps (pdf 4).
  - Modularity is blind to flow interdependence and prefers the right partition, which puts heavy links inside modules (pdf 4).
- **Fig. 2B:** every node is a source or a sink, so no walk exceeds one step. Teleportation dominates and any multi-module partition has high between-module flow. The map equation then always returns one module ($L=2.73$, $Q=0.00$). Modularity prefers the right partition ($L=4.68$, $Q=0.56$) (pdf 4).
- Guidance: for links that represent movement, flow-based methods such as the map equation are likely to find the most important structure. For links that are pairwise relationships, not flows, combinatoric methods (modularity, cluster-based compression) may be preferable (pdf 4).

*Intuition note:* The map equation asks "where does a walker stay?", modularity asks "where are the heavy links?". These are different questions and can have different answers.

### Mapping scientific communication (pdf 4–6)
- Data: 6,128 journals, 6,434,916 citations. They count citations in 2004 articles to articles of the previous five years (pdf 4).
- Exclusions: journals with fewer than 12 articles per year; journals that cite no other journal in the set; Science, Nature and PNAS (their breadth would suggest false links between disciplines); and self-citations (pdf 4–5).
- Fields come from the citation data. The authors' only subjective step is naming the clusters (pdf 5).
- Fig. 3: 88 modules, 3,024 directed weighted links. Only links traversed by the surfer more than 1/5000 of the time are drawn, covering 98% of node weight and 94% of flow (pdf 5).
- Module size equals the surfer's time share. Molecular biology has 723 journals and 26% of the time. Tribology has 7 journals and 0.064% (pdf 5–6).
- Arrows point from citing to cited ($A\to B$: A cites B). Applied fields cite basic fields extensively but not the reverse, e.g. geotechnology → geosciences, plastic surgery → general medicine, power systems → general physics (pdf 6).
- Border thickness shows outflow probability: 30% for general medicine, 12% for economics (pdf 6).
- Structure: a ring-like structure in which all major disciplines are connected by chains of citations, though not always directly. Considering link weights, it is more like the letter U, with social sciences at one end and engineering at the other. The backbone is medicine, molecular biology, chemistry and physics (pdf 6).
- Because the map covers a five-year window, it represents what de Solla Price called the "research frontier", rather than long-term interdependencies among fields. Mathematics is not central on the map, even though it is essential to the natural sciences, because only certain subfields (e.g. areas of physics and statistics) rely heavily on its most recent developments and contribute in return to its research agenda (pdf 6).

### Scale of the map (pdf 6–7)
- Module resolution depends on the universe of included nodes. Mapping a subset should reveal finer divisions (pdf 7).
- Fig. 4: 1,431 social-science journals, 217,287 citations. The 10 social-science modules split into 54. Links shown are those visited at least 1/2000 of the time, capturing 97% of node weight and 90% of flow (pdf 6).
- The basic structure is unchanged. Anthropology splits into physical and cultural, sociology into behavioral and institutional, marketing separates from management, and psychology and psychiatry reveal applied subfields (pdf 7).
- The authors conclude that this extra detail would have been clutter on the full map, and that they have shown how to formalize the cartographer's balance with information theory (pdf 7).

### Supporting material: the map equation (pdf 8)
- A module partition $\mathsf M$ is a hard partition: each node belongs to exactly one of $m$ modules. $L(\mathsf M)$ is the average bits per step for an infinite random walk. The same expression (Eq. 1) is restated as
$$L(\mathsf M)=q_{\curvearrowright}H(\mathcal Q)+\sum_{i=1}^{m}p^{i}_{\circlearrowright}H(\mathcal P^{i}).\tag{3}$$
- Switching probability, with $q_{i\curvearrowright}$ the per-step exit probability of module $i$ (derived in Eq. 9):
$$q_{\curvearrowright}=\sum_{i=1}^{m}q_{i\curvearrowright}.\tag{4}$$
- Between-module entropy: modules are treated as states with frequencies $q_{i\curvearrowright}/\sum_j q_{j\curvearrowright}$ in Shannon's bound (pdf 8):
$$H(\mathcal Q)=\sum_{i=1}^{m}\frac{q_{i\curvearrowright}}{\sum_{j}q_{j\curvearrowright}}\log\!\left(\frac{q_{i\curvearrowright}}{\sum_{j}q_{j\curvearrowright}}\right)\ \text{(sign: see Reading notes)}\tag{5}$$
- Weight of module $i$ (ergodic node frequencies $p_\alpha$, from the power method). Exit probability is included because exit codewords are coded together with node codewords, so their length matches their frequency of use (pdf 8):
$$p^{i}_{\circlearrowright}=q_{i\curvearrowright}+\sum_{\alpha\in i}p_\alpha.\tag{6}$$
- Within-module entropy of module $i$ (exit term plus node terms; sign: see Reading notes):
$$H(\mathcal P^i)=\frac{q_{i\curvearrowright}}{q_{i\curvearrowright}+\sum_{\beta\in i}p_\beta}\log\!\left(\frac{q_{i\curvearrowright}}{q_{i\curvearrowright}+\sum_{\beta\in i}p_\beta}\right)\tag{7a}$$
$$\qquad+\sum_{\alpha\in i}\frac{p_\alpha}{q_{i\curvearrowright}+\sum_{\beta\in i}p_\beta}\log\!\left(\frac{p_\alpha}{q_{i\curvearrowright}+\sum_{\beta\in i}p_\beta}\right)\tag{7b}$$
- Collecting terms gives the final form (pdf 8), where $\log$ and sign conventions are as printed:
$$L(\mathsf M)=\Big(\sum_{i}q_{i\curvearrowright}\Big)\log\Big(\sum_{i}q_{i\curvearrowright}\Big)\tag{8a}$$
$$-(1+1)\sum_{i}q_{i\curvearrowright}\log q_{i\curvearrowright}-\sum_{\alpha=1}^{n}p_\alpha\log p_\alpha\tag{8b}$$
$$+\sum_{i}\Big(q_{i\curvearrowright}+\sum_{\alpha\in i}p_\alpha\Big)\log\Big(q_{i\curvearrowright}+\sum_{\alpha\in i}p_\alpha\Big).\tag{8c}$$
- (added step) With the minus signs of entropy: $q_\curvearrowright H(\mathcal Q)=-\sum_i q_{i\curvearrowright}\log q_{i\curvearrowright}+q_\curvearrowright\log q_\curvearrowright$, and $p^i_\circlearrowright H(\mathcal P^i)=-q_{i\curvearrowright}\log q_{i\curvearrowright}-\sum_{\alpha\in i}p_\alpha\log p_\alpha+p^i_\circlearrowright\log p^i_\circlearrowright$. Summing over $i$ gives (8a)–(8c).
- Key point: $L$ depends only on $p_\alpha$ and $q_{i\curvearrowright}$. The term $\sum_\alpha p_\alpha\log p_\alpha$ is independent of the partition, and $p_\alpha$ otherwise appears only summed within modules. So it is sufficient for the optimizer to track changes in $q_{i\curvearrowright}$ and $\sum_{\alpha\in i}p_\alpha$ (pdf 9).

*Intuition note:* Everything needed is "how often is each module visited" and "how often is it left". The node-level detail drops out of the comparison between partitions.

### Implementation (pdf 9)
- **Ergodic frequencies:** teleportation links every node to every other with positive probability. The chain is then irreducible and aperiodic and has a unique steady state (Perron–Frobenius). Start with $p_\alpha=1/n$. At each step, with probability $1-\tau$ follow an outlink with probability proportional to $w_{\alpha\beta}$ (normalized so $\sum_\beta w_{\alpha\beta}=1$). With probability $\tau$, or 1 if the node has no outlinks, teleport uniformly. $\tau=0.15$ (pdf 9).
- **Exit probability** with teleportation, $n_i$ the number of nodes in module $i$ (pdf 9):
$$q_{i\curvearrowright}=\tau\,\frac{n-n_i}{n-1}\sum_{\alpha\in i}p_\alpha+(1-\tau)\sum_{\alpha\in i}\sum_{\beta\notin i}p_\alpha w_{\alpha\beta}.\tag{9}$$
The first term follows because each node teleports a fraction $\tau(n-n_i)/(n-1)$ out of the module. The second is the weight sent outside by links.
- **Greedy search:** start with each node in its own module. Repeatedly merge the pair of modules giving the largest decrease in $L$, until merging lengthens the description. This worked for 2.6 million nodes and 29 million links (pdf 9).
- **Simulated annealing:** start from the greedy result, run the heat-bath algorithm at several temperatures, and keep the run with minimal $L$. It can improve $L$ by up to several percent (pdf 9).
- **Visualization:** module area ∝ time share, border ring ∝ exit probability, link width ∝ transition probability between modules (teleportation excluded) (pdf 9).

### Fig. S1: greedy search on the Fig. 1 network (pdf 10–21)
- Each slide shows the partition and two stacks of boxes. The left stack (heights $q_{i\curvearrowright}$) is the module code, with Huffman codes from $q_{i\curvearrowright}/q_\curvearrowright$. The right stack (heights $p_\alpha$ and $q_{i\curvearrowright}$ per module) is the within-module codes, with Huffman codes from $p_\alpha/p^i_\circlearrowright$ and $q_{i\curvearrowright}/p^i_\circlearrowright$ (pdf 10).
- Codeword lengths are approximately $-\log$ of those ratios, so the Shannon limits in Eq. 1 are lower bounds on Huffman lengths (pdf 10).
- Start: every node its own module, $L=4.53+2.00=6.53$ bits (pdf 10). Next slides (between-module term + within-module term = total): 6.53 (pdf 11); 4.31+2.05=6.37 (pdf 12); 3.98+2.15=6.13 (pdf 13); 3.77+2.20=5.97 (pdf 14); 3.47+2.22=5.69 (pdf 15); 3.19+2.20=5.39 (pdf 16); 2.99+2.26=5.24 (pdf 17); 2.72+2.30=5.03 (pdf 18); 2.42+2.36=4.78 (pdf 19); 2.13+2.35=4.48 (pdf 20); 1.97+2.38=4.35 (pdf 21).
- The caption says the minimum is reached on the last slide, with four modules (pdf 10). That slide is not in this part.

## Toy example (ours, not from the text)
Two triangles {1,2,3} and {4,5,6} joined by link 3–4. Undirected, unweighted, no teleportation (a simplification). Degrees: 2,2,3,3,2,2, total 14. Visit frequencies $p=\deg/14$: four nodes at 1/7, two nodes (3 and 4) at 3/14.
- One level: $H(P)=4\cdot\frac17\log_2 7+2\cdot\frac{3}{14}\log_2\frac{14}{3}=\frac47(2.8074)+\frac37(2.2224)=1.6042+0.9525=2.557$ bits/step.
- Two levels: node 3 leaves its triangle with probability 1/3 and is visited 3/14 of the time, so $q_1=q_2=1/14$ and $q_\curvearrowright=1/7$.
  - $H(\mathcal Q)=1$ bit, so first term $=1/7=0.143$.
  - $p^1_\circlearrowright=1/14+7/14=4/7$. Within-module probabilities: exit 1/8, nodes 1/4, 1/4, 3/8. $H(\mathcal P^1)=\frac18\cdot3+2\cdot\frac14\cdot2+\frac38\log_2\frac83=0.375+1.0+0.531=1.906$.
  - Second term $=2\cdot\frac47\cdot1.906=2.178$. So $L=0.143+2.178=2.321$ bits/step.
- Check with Eq. 8: $-0.401+1.088+2.557-0.923=2.321$ ✓. The partition into two triangles is shorter (2.32 < 2.56).

## Concepts
- [[entropy]] — average surprisal; here it bounds codeword length per step of a walk (pdf 2).
- [[source-coding-theorem]] — average codeword length cannot be below $H(X)$ (pdf 2).
- [[huffman-arithmetic-coding]] — Huffman code gives short words to frequent nodes; used to illustrate codes (pdf 2).
- [[prefix-code-kraft]] — the Huffman code is prefix-free (pdf 2).
- [[entropy-rate]] — rate at which a Markov process can be encoded at best; the authors choose not to use it as the aim (pdf 1–2).
- [[map-equation]] (new) — expected per-step description length $L(\mathsf M)$ of a random walk under a two-level code for partition $\mathsf M$ (pdf 3, 8).
- [[two-level-code]] (new) — unique module names, reused within-module node names, plus exit codeword (pdf 3).
- [[random-surfer-teleportation]] (new) — walker that jumps uniformly with probability τ, making the chain ergodic (pdf 3, 9).
- [[modularity]] (new) — $Q$ of Eq. 2: in-module link weight minus its expected value (pdf 3).
- [[ergodic-visit-frequency]] (new) — steady-state share of time at each node, computed by the power method (pdf 8–9).
- [[community-detection]] (new) — here, equivalent to minimizing description length of flow (pdf 1, 3).

## Canonical instances
- [[fig1-huffman-25-node]] — 25-node network: 314 vs 355 bits; $L$ 4.50 → 3.05 bits/step (pdf 2–3).
- [[city-street-names]] — analogy for reusing node names across modules (pdf 3).
- [[fig2-flow-vs-modularity]] — two networks where map equation and modularity partitions differ (pdf 4).
- [[citation-map-of-science]] — 6,128 journals, 88 modules, U-like structure with a backbone (pdf 5–6).
- [[social-science-submap]] — 54 modules for 1,431 journals; finer resolution for a subset (pdf 6–7).

## Bridges (candidates)
- [structural-analogy] Map equation ↔ information-theory: Minimum Description Length — pick the model giving the shortest total code (the paper cites refs 14–16 for the equivalence between community finding and coding; ref. 15 is titled "Advances in minimum description length").
- [structural-analogy] Eq. 1 ↔ information-theory: weighted sum of entropies — resembles the chain-rule split (the weights sum to $1+q_\curvearrowright$, not 1, so it is not literally the chain rule) of a path into "which module" and "which node given module".
- [same-math] Random surfer with teleportation ↔ web search: PageRank steady-state distribution.
- [structural-analogy] Two-level naming ↔ linguistics: reuse of short names within a context, as in efficient communication.

## Questions this raises
- When partitions differ, how much of the difference is due to teleportation rather than the walk's persistence?
- Is the greedy-plus-annealing result a global minimum of $L$, or only a good local one?
- How does the optimal number of modules change if the code has three or more levels?
- How would the science map change with a longer citation window than five years?

## Reading notes
- This part covers the main paper text, references, and supporting material: pdf 1–21. It starts at the title and abstract (pdf 1). It ends at the 12th page of Fig. S1 (pdf 21, $L=4.35$). The remaining greedy-search slides are in the next part.
- Page references use (pdf N), as instructed. The labels give printed numbers 1–17 for pdf 1–17, but pdf 18–21 are labelled printed 10–13, repeating earlier numbers. Printed number = pdf number for pdf 1–17 only.
- Eqs. 5, 7a and 7b are printed in the images without the leading minus sign of entropy. The text calls them lower limits of codeword length, so a minus sign is evidently intended. Eq. 8 is consistent with the minus signs, as checked above. I copied the printed forms.
- Eq. 8b contains "(1+1)" as printed (equals 2).
- Typos in the source: "illustratess", "visa versa", "Perron-Frobineous", "that that". The SI reference list restarts at 1 and differs from the main-text numbering.
- The slide at pdf 11 shows the same $L=6.53$ as pdf 10; the text layer does not make clear what differs.
- Table-like slide text (codeword lists, stack labels) is garbled in the text layer; I used the images for the $L$ values.

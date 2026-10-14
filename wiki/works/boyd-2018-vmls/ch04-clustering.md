---
id: boyd-2018-vmls/ch04-clustering
work: boyd-2018-vmls
unit: "Chapter 4 — Clustering"
pages: 69–88
fields: [linear-algebra]
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
# Clustering (k-means)

## L0 — One line
Clustering splits $N$ vectors into $k$ groups by minimising the mean squared distance to group representatives, and the k-means algorithm does this heuristically by alternating "assign to nearest representative" and "replace each representative by its group mean".

## L1 — The gist (≤ 120 words)
The chapter asks how to group many vectors so that vectors in a group are close together. It defines a quality score, $J^{\text{clust}}$, the mean squared distance from each vector to its group's representative (a typical vector chosen for that group). Finding the best clustering is practically impossible for all but tiny problems. But each half of the problem is easy when the other half is fixed: assign each vector to the nearest representative, and set each representative to its group mean. Alternating the two steps is the k-means algorithm. It always converges but may stop at a suboptimal answer. It is cheap and useful for topic discovery, digit images, classification, recommendation and filling in missing entries.

**Prerequisites:** vector norm and distance, the mean of a list of vectors, set notation ($i\in G_j$, $|G_j|$), counting flops, and the idea of a word-count histogram vector.

## L2 — Key ideas (5–10 bullets)
- Clustering partitions $N$ vectors into $k$ groups of mutually close vectors. It is typically used when the vectors are feature vectors, and $k$ is normally much smaller than $N$ (p. 69).
- A clustering is an assignment vector $c$ plus representatives $z_1,\dots,z_k$. Its quality is $J^{\text{clust}}$, the mean squared distance of each vector to its representative; smaller is better (p. 72).
- Optimal clustering is practically impossible to find for all but the smallest problems. But with representatives fixed, the best assignment is "nearest representative", and with assignments fixed, the best representative is the group mean (pp. 73–74).
- The k-means algorithm alternates these two exact steps. $J^{\text{clust}}$ decreases, so it converges in finitely many steps, but only to a possibly suboptimal partition that depends on the start. It is common to run it several times from different starts and keep the run with the smallest final $J^{\text{clust}}$ (p. 76).
- Cost is about $(3k+1)Nn$ flops (arithmetic operations) per iteration (p. 79); the author says it needs far less computation than exact search and can be run with $N$ in the billions (p. 73).
- Representatives are interpretable: each entry is an average over the group, and the data points closest to a representative can be thought of as archetypes (p. 76).
- On MNIST (a data set of handwritten-digit images) and Wikipedia word histograms, k-means "discovers" digits and topics using only distances between vectors (pp. 79, 82–85).
- Applications: exploratory analysis, classification by nearest representative, recommendation, and imputing (guessing) missing entries from the nearest representative (pp. 85–86).

## L3 — Walkthrough

### Chapter introduction (p. 69)
The chapter treats clustering of vectors by pairwise distance and presents the k-means algorithm. It says the material is not used later in the book. It relies only on the previous three chapters (p. 69).

### 4.1 Clustering (pp. 69–71)
- **Goal.** Given $N$ $n$-vectors $x_1,\dots,x_N$, partition them (if possible) into $k$ groups with the vectors in each group close to each other. Normally $k \ll N$. Typical $k$ runs from a handful to a few hundred or more, and $N$ from hundreds to billions (p. 69).
- Part of the task is to decide whether the vectors can be divided into $k$ such groups at all. That depends on $k$ and on the data (p. 69).
- **Figure 4.1** has $N=300$ 2-vectors that fall clearly into $k=3$ clusters (p. 69). The author says this is atypical in three ways (p. 70):
  1. For $n=2$ one can just scatter-plot and look. In almost all applications $n$ is larger, so this visual method is not available.
  2. These points are very well clustered. In most applications many points lie between clusters.
  3. The best $k$ is clear here but is often unclear in real data.
- Even so, clustering can be useful when the clustering is not clean and the best $k$ is unclear (p. 70).
- **Example applications listed (pp. 70–71):**
  - Topic discovery: word histograms of $N$ documents are clustered, with no knowledge of word meanings.
  - Patient clustering and customer market segmentation (purchase vectors).
  - ZIP-code clustering: $N\approx 40000$, e.g. $k=100$.
  - Student clustering: grading records, e.g. $k=10$.
  - Survey response clustering: Likert answers coded $-2,\dots,+2$.
  - Weather zones: a 24-vector per county, 12 monthly temperatures plus 12 monthly rainfalls, standardised.
  - Daily energy-use patterns: 24 hourly values per customer. The author suggests a clustering algorithm might "discover" customers with a swimming pool, electric water heater or solar panels.
  - Financial sectors: attributes scaled to similar ranges.
- Knowing the vectors cluster well into, say, $k=5$ or $k=37$ groups gives insight into the data. Examining the clusters often lets one label them (p. 71).

### 4.2 A clustering objective (pp. 72–74)
**Assignments.** Label the groups $1,\dots,k$. The $N$-vector $c$ gives $c_i$, the group of $x_i$. Example: $N=5$, $k=3$, $c=(3,1,1,1,2)$ gives $G_1=\{2,3,4\}$, $G_2=\{5\}$, $G_3=\{1\}$. Formally
$$G_j=\{i \mid c_i=j\}.$$
(p. 72)

**Representatives.** Each group has a representative $n$-vector $z_j$. It can be any $n$-vector, not necessarily one of the data vectors. We want $\|x_i-z_{c_i}\|$ small for every $i$ (p. 72).

**Objective.**
$$J^{\text{clust}}=\big(\|x_1-z_{c_1}\|^2+\cdots+\|x_N-z_{c_N}\|^2\big)/N \tag{4.1}$$
This is the mean squared distance from the vectors to their representatives. It depends on both $c$ and $z_1,\dots,z_k$, and smaller is better. $J^{\text{clust}}=0$ happens only when the data take only $k$ different values and each vector is assigned to the representative equal to it. The author says this would probably not occur in practice (p. 72). Other objectives are possible, for example ones encouraging more balanced groups, but the book uses this common one (pp. 72–73).

**Optimal vs suboptimal.** An *optimal* clustering minimises $J^{\text{clust}}$ over $c_1,\dots,c_N$ and $z_1,\dots,z_k$. For all but the very smallest problems it is practically impossible to find. It can be done in principle, but the computation grows extremely rapidly with $N$ (p. 73). The k-means algorithm needs far less computation, can be run with $N$ in the billions, and often finds a very good, though not necessarily the best, clustering. Its results are called *suboptimal*, meaning they might not give the lowest possible $J^{\text{clust}}$ (p. 73).

**Fixed representatives, choose assignments.**
- $J^{\text{clust}}$ is a sum of $N$ terms, and $c_i$ affects only the $i$th term $(1/N)\|x_i-z_{c_i}\|^2$ (p. 73).
- So each $c_i$ can be chosen separately: the $j$ minimising $\|x_i-z_j\|$. In words, assign each vector to its nearest representative. This solves the problem exactly (p. 73).
- Then $\|x_i-z_{c_i}\|=\min_{j=1,\dots,k}\|x_i-z_j\|$, and
$$J^{\text{clust}}=\Big(\min_{j}\|x_1-z_j\|^2+\cdots+\min_{j}\|x_N-z_j\|^2\Big)/N,$$
the mean squared distance from the data to their closest representative (p. 73).

**Fixed assignments, choose representatives.**
- Rearrange the sum into group sums: $J^{\text{clust}}=J_1+\cdots+J_k$ with
$$J_j=(1/N)\sum_{i\in G_j}\|x_i-z_j\|^2 .$$
- $z_j$ affects only $J_j$, so each $z_j$ is chosen to minimise the mean squared distance to its group. The solution is the group mean (centroid):
$$z_j=(1/|G_j|)\sum_{i\in G_j}x_i ,$$
where $|G_j|$ is the number of elements of $G_j$. The author refers to exercise 4.1 for the justification (p. 74).

*Intuition note.* The full problem is hard because assignments and representatives depend on each other. Fix one, and the other is easy because the objective splits into independent small pieces: one per vector, or one per group.

### 4.3 The k-means algorithm (pp. 74–79)
Since the two choices are circular, iterate: alternately update assignments, then representatives. Each step lowers $J^{\text{clust}}$ unless the step changes nothing (p. 74). The method was first proposed by Stuart Lloyd in 1957, independently by Hugo Steinhaus. It is sometimes called the Lloyd algorithm, and the name "k-means" has been used since the 1960s (p. 74).

**Algorithm 4.1 (k-means).** Given $x_1,\dots,x_N$ and initial representatives $z_1,\dots,z_k$, repeat until convergence (p. 75):
1. *Partition.* Assign each $x_i$ to the group of its nearest representative.
2. *Update.* Set each $z_j$ to the mean of the vectors in group $j$.

Figure 4.2 shows one iteration on 30 2-vectors with 3 representatives (p. 75).

**Comments and clarifications (pp. 75–76).**
- Ties in step 1 can be broken by choosing, among the closest representatives, the one with the smallest $j$.
- A group may become empty in step 1. Then drop that group and its representative, ending with fewer than $k$ groups.
- If the assignments in step 1 are the same in two successive iterations, the representatives are also the same. Nothing changes afterwards, so stop; this is what "until convergence" means. In practice one often stops earlier, when the improvement in $J^{\text{clust}}$ becomes very small.
- Initial representatives: pick them randomly from the data vectors, or start from a random assignment to $k$ groups and use the group means. Better initialisations exist but are beyond the book.

**Convergence (p. 76).**
- Because $J^{\text{clust}}$ decreases at each step, k-means converges in a finite number of steps.
- Depending on the starting representatives, it can and does converge to different partitions with different objective values.
- It is a *heuristic*: it cannot guarantee that the final partition minimises $J^{\text{clust}}$.
- Hence it is common to run it several times from different starts and keep the run with the smallest final $J^{\text{clust}}$. It is still very useful and widely used.
- Figures 4.3–4.5 show iterations 1, 2 and 10 on the data of figure 4.1 with $k=3$ and random initial representatives, the final clustering, and the decreasing $J^{\text{clust}}$. The objective is measured after step 1 of each iteration (pp. 77–78).

*Intuition note.* Each step can only help or leave things unchanged, so the objective goes down until a step changes nothing. The author says this implies the algorithm converges in a finite number of steps (p. 76). Where it ends depends on the starting representatives, and it is not guaranteed to be the best partition.

**Interpreting representatives (p. 76).** Representatives are interpretable. Example: if voters are clustered into 7 groups and component 4 is age, then $(z_3)_4=37.8$ means the average age in group 3 is 37.8. Another way is to find the data points closest to each representative and treat them as archetypes of the group.

**Choosing $k$ (p. 76).** Run k-means for several $k$ and compare. The choice depends on how the clustering will be used (§4.5). As a general statement: if $J^{\text{clust}}$ at $k=7$ is quite a bit smaller than for $k=2,\dots,6$ and not much larger than for $k=8,9,\dots$, one could reasonably choose $k=7$.

**Complexity (p. 79).**
- Step 1: nearest-representative search for $N$ vectors among $k$ centroids takes about $3Nkn$ flops.
- Step 2: a cluster with $p$ vectors takes $n(p-1)\approx np$ flops. Over all clusters the total is $Nn$ flops, less than step 1.
- So about $(3k+1)Nn$ flops per iteration, which is of order $Nkn$.
- A run typically takes fewer than a few tens of iterations, and one runs it a modest number of times, such as 10. A very rough guess for 10 runs is $1000Nkn$ flops.
- Example: $N=100000$, $n=100$, $k=10$ on a 1 Gflop/s computer. The author's estimate is about 100 seconds, which he calls crude. (added step) Check: $1000\cdot10^5\cdot100\cdot10=10^{11}$ flops, divided by $10^9$ flops/s, is $100$ s.

*Intuition note.* The cost grows in direct proportion to the number of vectors, their length and the number of groups. That linear growth helps explain why k-means can be run on very large data sets (the author mentions $N$ in the billions, p. 73).

### 4.4 Examples (pp. 79–85)

**4.4.1 Image clustering (pp. 79–81).**
- MNIST: $N=60000$ grayscale handwritten-digit images of size $28\times28$, each a vector with $n=784$ (p. 79).
- k-means with $k=20$, starting from a random assignment, repeated 20 times. Figure 4.7 shows $J^{\text{clust}}$ per iteration for three starts, including those with the lowest and highest final values. The plotted values lie roughly between 35 and 42 (pp. 79–80).
- Figures 4.8 and 4.9 show the representatives for the lowest and highest final objective. Most representatives are recognisable digits, with some reasonable confusion such as 4 vs 9 or 3 vs 8 (pp. 79, 81).
- The algorithm knows nothing about digits, handwriting or that the vectors are images; it uses only distances between 784-vectors. One interpretation is that it has "discovered" the digits (p. 79).

**4.4.2 Document topic discovery (pp. 82–85).**
- Corpus: $N=500$ popular Wikipedia articles (September 6, 2015 – June 11, 2016). Section titles and reference sections are removed. Numbers and stop words are removed and a stemming algorithm is applied to nouns and verbs. The dictionary holds the words appearing in at least 20 documents: 4423 words. Each document is a word-histogram vector of length 4423 (p. 82).
- k-means with $k=9$ and 20 random initial partitions gave similar but slightly different clusterings. Figure 4.10 shows $J^{\text{clust}}$ for three of them (values roughly between $7\times10^{-3}$ and $8.3\times10^{-3}$). The run with the lowest final value is used below (p. 82).
- Table 4.1 lists the 10 largest histogram coefficients of each representative. Table 4.2 lists cluster sizes and the 10 titles closest to each representative (pp. 83–84):

| Cluster | Size | Theme (from the titles) |
|---|---|---|
| 1 | 21 | boxers and fighters |
| 2 | 43 | holidays |
| 3 | 189 | historical and political figures |
| 4 | 46 | musicians and albums |
| 5 | 49 | sports figures and teams |
| 6 | 39 | TV series |
| 7 | 16 | wrestling events |
| 8 | 58 | film actors |
| 9 | 39 | films |

  (The themes are my reading of the printed titles. The sizes sum to 500.)
- The author says each cluster makes sense and mostly contains documents on similar topics or themes, and that the top words also make sense. Movies and TV series (mostly) fall in different clusters (9 and 6). Clusters 8 and 9 share several top words but cover different topics, actors and movies (p. 82).
- The algorithm does not know word meanings or word order. It uses only the distance between word-count histogram vectors (p. 85).

### 4.5 Applications (pp. 85–86)
- **Exploratory analysis.** k-means can be used to get an idea of what a large collection of vectors 'looks like'. For $k$ below a few tens, one examines representatives and some group members to label the groups (p. 85).
- **Classification.** Cluster, label the groups by hand, then classify a new vector by its nearest representative. This gives a rudimentary digit classifier or topic classifier. The author says better methods come in chapter 14 (p. 85).
- **Recommendation engine.** Vectors count how often each user streamed each of $n$ songs; they are typically sparse. Clustering finds groups with similar taste. $(z_j)_i$ is the average number of plays of song $i$ by users in group $j$. To recommend 5 songs to a user whose vector $x_i$ is in cluster $j$, find the indices $l$ with $(x_i)_l=0$ that have the 5 largest values of $(z_j)_l$ (p. 85).
- **Guessing (imputing) missing entries (pp. 85–86).**
  - First run k-means on only the complete vectors.
  - For a vector $x$ with known-entry index set $K$, choose the $j$ that minimises
$$\sum_{i\in K}\big(x_i-(z_j)_i\big)^2 .$$
  - Fill each missing entry with the corresponding entry of $z_j$. For a missing age this is the average age of that cluster.

## Toy example (ours, not from the text)
Take $n=1$, $N=4$ scalars $x=(1,2,9,10)$, $k=2$, start $z_1=1$, $z_2=2$.

**Iteration 1, step 1.** Distances:
- $x_1=1$: $0$ to $z_1$, $1$ to $z_2$, so group 1.
- $x_2=2$: $1$ and $0$, so group 2.
- $x_3=9$: $8$ and $7$, so group 2.
- $x_4=10$: $9$ and $8$, so group 2.

So $c=(1,2,2,2)$ and $J^{\text{clust}}=(0^2+0^2+7^2+8^2)/4=113/4=28.25$.

**Step 2.** $z_1=1$ and $z_2=(2+9+10)/3=7$. Now $J^{\text{clust}}=(0+5^2+2^2+3^2)/4=38/4=9.5$, lower than 28.25.

**Iteration 2, step 1.** With $z=(1,7)$:
- $x_1=1$: $0$ vs $6$, so group 1.
- $x_2=2$: $1$ vs $5$, so group 1.
- $x_3=9$: $8$ vs $2$, so group 2.
- $x_4=10$: $9$ vs $3$, so group 2.

So $c=(1,1,2,2)$ and $J^{\text{clust}}=(0+1+4+9)/4=3.5$.

**Step 2.** $z_1=(1+2)/2=1.5$ and $z_2=(9+10)/2=9.5$. Then $J^{\text{clust}}=(0.25\cdot4)/4=0.25$.

**Iteration 3, step 1.** Nearest representatives give the same $c=(1,1,2,2)$, so the algorithm has converged. $J^{\text{clust}}$ went $28.25\to9.5\to3.5\to0.25$, never increasing.

## Concepts
- [[clustering]] (new) — partition $N$ vectors into $k$ groups of mutually close vectors (p. 69)
- [[cluster-assignment-vector]] (new) — the $N$-vector $c$ with $c_i$ the group of $x_i$; index sets $G_j=\{i\mid c_i=j\}$ (p. 72)
- [[group-representative-centroid]] (new) — an $n$-vector $z_j$ per group; the best choice for fixed groups is the group mean (pp. 72, 74)
- [[clustering-objective-jclust]] (new) — $J^{\text{clust}}$, the mean squared distance from vectors to their representatives, eq. (4.1) (p. 72)
- [[k-means-algorithm]] (new) — alternate nearest-representative assignment and group-mean update (p. 75)
- [[heuristic-algorithm]] (new) — a method with no guarantee of finding the minimiser of its objective (p. 76)
- [[imputation-missing-entries]] (new) — guessing missing vector entries from the nearest representative using the known entries (pp. 85–86)
- [[norm]] — Euclidean length; distances $\|x_i-z_j\|$ drive all steps (p. 72)

## Canonical instances
- [[mnist-digit-clustering]] — k-means with $k=20$ on 60000 vectors of length 784; most representatives are recognisable digits (p. 79)
- [[wikipedia-topic-discovery]] — 500 articles, 4423-word histograms, $k=9$; clusters mostly contain documents on similar topics or themes (p. 82)
- [[song-recommendation-by-clusters]] — recommend songs with high representative values that the user has not played (p. 85)
- [[kmeans-worked-iteration-fig-4-2]] — one assignment-plus-update iteration on 30 2-vectors (p. 75)

## Bridges (candidates)
- [structural-analogy] k-means centroid update (mean minimises sum of squared distances) ↔ least squares: both minimise a sum of squared distances, and the mean is the best single constant fit (exercise 4.1 shows the minimiser).
- [structural-analogy] alternating "fix representatives, solve for assignments / fix assignments, solve for representatives" ↔ numerical optimisation: alternating exact minimisation over two blocks of variables, each step never increasing the objective.
- [structural-analogy] word-histogram vectors and distance ↔ cosine similarity / embeddings: documents as vectors compared by geometry, though this chapter uses Euclidean distance, not cosine.
- [metaphor] representatives as archetypes ↔ principal component analysis: both summarise data by a few prototype vectors, but via different constructions.

## Questions this raises
- Since k-means can converge to different partitions, how many random restarts are enough, and are there better initialisations (the author says they exist but skips them, p. 76)?
- How should $k$ be chosen? (The author says it depends on how the clustering will be used; his example rule on p. 76 looks for a clear drop before and a small gain after.)
- How much do results depend on scaling the features? (The examples standardise weather and financial data, p. 71.)
- How does the nearest-representative classifier compare with the better classification methods promised in chapter 14 (p. 85)?

## Exercises worth doing
- Ex. 4.1 (p. 87) — prove the mean minimises the sum of squared distances via $J(z)=\sum\|x_i-\bar x\|^2+L\|z-\bar x\|^2$; justifies the update step — difficulty: medium
- Ex. 4.2 (p. 87) — show that representatives of nonnegative or proportion vectors keep those properties, and interpret $(z_j)_i$ for Boolean data — difficulty: easy
- Ex. 4.3 (p. 87) — show 2-means groups are separated by an affine function $w^Tx+v$ (hint: $\|x-z_1\|^2-\|x-z_2\|^2$) — difficulty: medium
- Ex. 4.4 (p. 87) — modify k-means to respect pre-assigned vectors, and give a medical example — difficulty: easy

## Reading notes
- Printed page = pdf page − 10 (pdf 79 = printed 69). The unit ends at printed 87; printed 88 (pdf 98) is blank.
- The text says the chapter is not used in the rest of the book (p. 69).
- Figures 4.1–4.5 and 4.7–4.10 were checked in the page images. Numbers in the L3 descriptions of figures are approximate readings of the axes, not values printed in the text.
- Misprints seen in the image: "an initial representatives" (p. 76; presumably "initial representatives" was meant) and "representive" (p. 76).
- Exercise 4.1(a)–(c) equations were read in the image: the key identity is $J(z)=\sum_{i=1}^L\|x_i-\bar x\|^2+L\|z-\bar x\|^2$. No solutions are printed in this unit, and none are given here.

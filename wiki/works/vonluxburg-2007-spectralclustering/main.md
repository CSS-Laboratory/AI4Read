---
id: vonluxburg-2007-spectralclustering/main
work: vonluxburg-2007-spectralclustering
unit: paper
pages: 1-32
fields: [linear-algebra]
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
# A Tutorial on Spectral Clustering (von Luxburg, 2007)

## L0 — One line
Spectral clustering re-represents data by the first k eigenvectors of a graph Laplacian and runs k-means there. It is explained in three ways: as a relaxed graph cut, as a random-walk statement, and as a perturbation of the ideal block-diagonal case.

## L1 — The gist (≤ 120 words)
How can data with pairwise similarities be clustered, and why does an eigenvector-based method work? The tutorial builds a similarity graph, defines three graph Laplacians, and states three algorithms (unnormalized, Shi–Malik, Ng–Jordan–Weiss). It explains them in three ways: as relaxations of RatioCut and Ncut, as random walks that rarely switch clusters, and as perturbations of the ideal case with k connected components (Davis–Kahan). It then discusses practical choices. The author recommends the k-nearest-neighbour graph and the normalized $L_{\rm rw}$. The graph-cut relaxation carries no quality guarantee. The author says the method can be quite sensitive to graph parameters.

**Prerequisites:** eigenvalues/eigenvectors of symmetric matrices; positive semi-definiteness; Rayleigh quotient / trace minimization; basic probability (Markov chains); k-means.

## L2 — Key ideas (5–10 bullets)
- The Laplacian $L=D-W$ has quadratic form $f'Lf=\tfrac12\sum w_{ij}(f_i-f_j)^2$. The multiplicity of eigenvalue 0 equals the number of connected components, with indicator-vector eigenvectors. This is important for spectral clustering (pp. 4–5).
- Algorithm template: build a graph, take the first k (generalized) eigenvectors, treat the rows as points in $\mathbb R^k$, run k-means. The three variants differ in the Laplacian used. Ng et al. add a row normalization (pp. 6–7).
- Graph-cut view: relaxing the discrete RatioCut problem gives $L$-eigenvectors. Relaxing Ncut gives $L_{\rm rw}$ eigenvectors, via a trace minimization (Rayleigh–Ritz). The relaxation has no guarantee on solution quality (pp. 10–13).
- Random-walk view: $\mathrm{Ncut}(A,\bar A)=P(\bar A|A)+P(A|\bar A)$ for a stationary walk. Without further assumptions, the commute distance is only loosely related to the spectral embedding (pp. 14–16).
- Perturbation view: by Davis–Kahan, the eigenspace moves by at most $\|H\|/\delta$, so a large eigengap helps. The author finds $L$ and $L_{\rm rw}$ well justified by this argument, and $L_{\rm sym}$ also justifiable but needing more care for low-degree vertices (pp. 17–19).
- Practice: use a k-nearest-neighbour graph first. Graph parameters are chosen by rules of thumb with no firm theory. The eigengap heuristic helps choose k when clusters are clear (pp. 19–24).
- Author's recommendation: normalized over unnormalized (Ncut also serves the within-cluster objective; for normalized versions convergence is proved, while unnormalized clustering can fail to converge), and $L_{\rm rw}$ over $L_{\rm sym}$ (pp. 24–27).

## L3 — Walkthrough

### 1 Introduction (p. 1)
Spectral clustering is presented as simple, solvable with standard linear algebra, and often better than k-means or single linkage. Plan: similarity graphs (§2), Laplacians (§3), algorithms (§4), three explanations (§5 graph cuts, §6 random walks, §7 perturbation), practice (§8), literature (§9) (p. 1).

### 2 Similarity graphs (pp. 2–3)
Given similarities $s_{ij}\ge0$, the similarity graph $G=(V,E)$ has one vertex per data point. Clustering becomes: partition so that between-group edges have low weight and within-group edges high weight (p. 2).

**2.1 Notation (p. 2).** $W=(w_{ij})$ is the weighted adjacency matrix, $w_{ij}=w_{ji}\ge0$. Degree $d_i=\sum_j w_{ij}$; $D$ is the diagonal degree matrix. Complement $\bar A=V\setminus A$. Indicator vector $\mathbb 1_A$. $W(A,B):=\sum_{i\in A,j\in B}w_{ij}$. Two sizes: $|A|$ = number of vertices, $\mathrm{vol}(A):=\sum_{i\in A}d_i$. A connected component is a connected set with no edges to its complement. A partition is a set of non-empty, disjoint sets whose union is $V$.

**2.2 Graph constructions (p. 3).** The goal is to model local neighbourhoods.
- *ε-neighbourhood:* connect points with distance $<\varepsilon$; usually unweighted.
- *k-nearest-neighbour:* the relation is directed. Either connect $i,j$ if $i$ is among the k-NN of $j$ *or* vice versa (the "k-NN graph"), or if *both* hold (the "mutual k-NN graph"). Edges are weighted by similarity.
- *Fully connected:* all positive similarities, weighted by $s_{ij}$. It is useful only if $s$ itself is local, e.g. $s(x_i,x_j)=\exp(-\|x_i-x_j\|^2/(2\sigma^2))$; $\sigma$ plays the role of $\varepsilon$.

The author knows of no theory on how the graph choice affects the result (p. 3).

### 3 Graph Laplacians (pp. 3–6)
Conventions: eigenvectors need not be normalized ($\mathbb 1$ and $a\mathbb 1$ count as the same); eigenvalues are ordered increasingly; "first k eigenvectors" means the k smallest eigenvalues. The literature has no unique "graph Laplacian" (p. 3).

**3.1 Unnormalized Laplacian,** $L=D-W$ (p. 4).

**Proposition 1.** (1) For all $f\in\mathbb R^n$: $f'Lf=\tfrac12\sum_{i,j}w_{ij}(f_i-f_j)^2$. (2) $L$ is symmetric and positive semi-definite. (3) The smallest eigenvalue is 0 with eigenvector $\mathbb 1$. (4) $L$ has $n$ non-negative real eigenvalues $0=\lambda_1\le\dots\le\lambda_n$ (p. 4).

Proof of (1), step by step:
$$f'Lf=f'Df-f'Wf=\sum_i d_if_i^2-\sum_{i,j}f_if_jw_{ij}=\tfrac12\Big(\sum_i d_if_i^2-2\sum_{i,j}f_if_jw_{ij}+\sum_j d_jf_j^2\Big)=\tfrac12\sum_{i,j}w_{ij}(f_i-f_j)^2.$$
(2) follows from symmetry of $W,D$ and from (1), which gives $f'Lf\ge0$. (3) is "obvious". (4) follows from (1)–(3) (p. 4). $L$ ignores the diagonal of $W$, so self-edges do not change it (p. 4).

**Proposition 2.** For an undirected graph with non-negative weights, the multiplicity $k$ of eigenvalue 0 of $L$ equals the number of connected components $A_1,\dots,A_k$. The eigenspace of 0 is spanned by $\mathbb 1_{A_1},\dots,\mathbb 1_{A_k}$ (p. 4).

Proof, key steps. Case $k=1$: if $Lf=0$ then $0=f'Lf=\sum w_{ij}(f_i-f_j)^2$. All terms are non-negative, so each vanishes: $f_i=f_j$ whenever $w_{ij}>0$. Hence $f$ is constant along paths, so on the whole component (p. 5). Case $k$ components: order vertices by component; $L$ is block diagonal with blocks $L_i$, each a graph Laplacian of its component. The spectrum of $L$ is the union of the spectra of the $L_i$. Each $L_i$ has eigenvalue 0 with multiplicity 1 and the constant eigenvector. Padding it with zeros gives the indicator vector (p. 5).

*Intuition note.* The quadratic form is zero only for vectors that do not change across any edge. So the zero-eigenspace records which vertices are connected.

**3.2 Normalized Laplacians (p. 5).**
$$L_{\rm sym}:=D^{-1/2}LD^{-1/2}=I-D^{-1/2}WD^{-1/2},\qquad L_{\rm rw}:=D^{-1}L=I-D^{-1}W.$$

**Proposition 3 (pp. 5–6).** (1) $f'L_{\rm sym}f=\tfrac12\sum w_{ij}\big(f_i/\sqrt{d_i}-f_j/\sqrt{d_j}\big)^2$. (2) $\lambda$ is an eigenvalue of $L_{\rm rw}$ with eigenvector $u$ iff $\lambda$ is an eigenvalue of $L_{\rm sym}$ with eigenvector $w=D^{1/2}u$. (3) $\lambda,u$ is an eigenpair of $L_{\rm rw}$ iff they solve $Lu=\lambda Du$. (4) 0 is an eigenvalue of $L_{\rm rw}$ with eigenvector $\mathbb 1$, and of $L_{\rm sym}$ with eigenvector $D^{1/2}\mathbb 1$. (5) Both are positive semi-definite with $n$ non-negative real eigenvalues $0=\lambda_1\le\dots\le\lambda_n$.
Proofs: (1) as in Prop. 1. (2) multiply $L_{\rm sym}w=\lambda w$ by $D^{-1/2}$ and set $u=D^{-1/2}w$. (3) multiply $L_{\rm rw}u=\lambda u$ by $D$. (4) $L_{\rm rw}\mathbb 1=0$; the rest from (2). (5) from (1), then (2) (p. 6).

**Proposition 4.** The multiplicity of eigenvalue 0 of both $L_{\rm rw}$ and $L_{\rm sym}$ equals the number $k$ of connected components. For $L_{\rm rw}$ the eigenspace is spanned by $\mathbb 1_{A_i}$; for $L_{\rm sym}$ by $D^{1/2}\mathbb 1_{A_i}$. The proof is analogous to Prop. 2 (p. 6).

### 4 Algorithms (pp. 6–9)
Input: similarity matrix $S\in\mathbb R^{n\times n}$ (symmetric, non-negative) and the number of clusters $k$. All three algorithms first build a similarity graph with weight matrix $W$ (§2). The steps then differ (pp. 6–7):

| Variant | Laplacian | Eigenproblem | Extra step |
|---|---|---|---|
| Unnormalized | $L$ | first $k$ eigenvectors of $L$ | none |
| Shi–Malik (2000) | $L$ | first $k$ generalized eigenvectors of $Lu=\lambda Du$ (= eigenvectors of $L_{\rm rw}$, Prop. 3) | none |
| Ng–Jordan–Weiss (2002) | $L_{\rm sym}$ | first $k$ eigenvectors of $L_{\rm sym}$ | rows of $U$ normalized to norm 1: $t_{ij}=u_{ij}/(\sum_k u_{ik}^2)^{1/2}$ |

In every case $U\in\mathbb R^{n\times k}$ has the eigenvectors as columns, $y_i\in\mathbb R^k$ is the $i$-th row of $U$ (of $T$ for Ng et al.), and the $y_i$ are clustered by k-means into $C_1,\dots,C_k$. Output: $A_i=\{j\mid y_j\in C_i\}$. The main trick is the change of representation from $x_i$ to $y_i\in\mathbb R^k$ (p. 7). The reason for the row normalization is given in §7 (p. 7).

**Toy data of Figure 1 (pp. 8–9).** 200 points in $\mathbb R$ from a mixture of four Gaussians; Gaussian similarity with $\sigma=1$; the 10-NN graph and the fully connected graph are compared.
- In the 10-NN graph the four clusters are disconnected. The first four eigenvalues are 0 and the eigenvectors are cluster indicators (Props. 2, 4) (pp. 8–9).
- In the fully connected graph there is one component, so eigenvalue 0 has multiplicity 1 and the first eigenvector is constant. For the unnormalized case, thresholding eigenvector 2 at 0 separates clusters {1,2} from {3,4}; eigenvector 3 gives {1,4} vs {2,3}; eigenvector 4 gives {1,3} vs {2,4} (p. 9).
- In all illustrated cases k-means on the first four eigenvectors finds the four clusters (p. 9).

### 5 Graph cut point of view (pp. 9–14)
For $k$ sets, mincut minimizes $\mathrm{cut}(A_1,\dots,A_k):=\tfrac12\sum_i W(A_i,\bar A_i)$. For $k=2$ it is efficiently solvable but often separates a single vertex. Two balanced objectives (p. 9):
$$\mathrm{RatioCut}(A_1,\dots,A_k):=\tfrac12\sum_i\frac{W(A_i,\bar A_i)}{|A_i|}=\sum_i\frac{\mathrm{cut}(A_i,\bar A_i)}{|A_i|},\qquad \mathrm{Ncut}(A_1,\dots,A_k):=\tfrac12\sum_i\frac{W(A_i,\bar A_i)}{\mathrm{vol}(A_i)}=\sum_i\frac{\mathrm{cut}(A_i,\bar A_i)}{\mathrm{vol}(A_i)}.$$
$\sum 1/|A_i|$ is smallest when all $|A_i|$ coincide, and $\sum1/\mathrm{vol}(A_i)$ when all volumes coincide. So both favour balanced clusters. Balancing makes the problem NP hard. Spectral clustering solves relaxed versions: relaxing Ncut gives normalized, relaxing RatioCut gives unnormalized spectral clustering (pp. 9–10).

**5.1 RatioCut, $k=2$ (pp. 10–11).** Problem (1): $\min_{A\subset V}\mathrm{RatioCut}(A,\bar A)$. Define
$$f_i=\begin{cases}\sqrt{|\bar A|/|A|}&v_i\in A\\-\sqrt{|A|/|\bar A|}&v_i\in\bar A.\end{cases}\tag{2}$$
Then, using Prop. 1 (the edges within $A$ or within $\bar A$ contribute zero):
$$f'Lf=\tfrac12\sum_{i,j}w_{ij}(f_i-f_j)^2=\mathrm{cut}(A,\bar A)\Big(\tfrac{|\bar A|}{|A|}+\tfrac{|A|}{|\bar A|}+2\Big)=\mathrm{cut}(A,\bar A)\Big(\tfrac{|A|+|\bar A|}{|A|}+\tfrac{|A|+|\bar A|}{|\bar A|}\Big)=|V|\cdot\mathrm{RatioCut}(A,\bar A).$$
Also $\sum_if_i=|A|\sqrt{|\bar A|/|A|}-|\bar A|\sqrt{|A|/|\bar A|}=0$, so $f\perp\mathbb 1$, and $\|f\|^2=|\bar A|+|A|=n$. Hence (3): $\min_{A}f'Lf$ subject to $f\perp\mathbb 1$, $f_i$ as in (2), $\|f\|=\sqrt n$. This discrete problem is still NP hard. Relax by letting $f\in\mathbb R^n$:
$$\min_{f\in\mathbb R^n}f'Lf\ \text{ s.t. } f\perp\mathbb 1,\ \|f\|=\sqrt n.\tag{4}$$
By the Rayleigh–Ritz theorem the solution is the eigenvector of the second smallest eigenvalue of $L$. To get a partition one may use the sign of $f_i$ (too simple, especially for $k>2$). Most algorithms cluster the coordinates $f_i$ with k-means into $C,\bar C$. This is exactly unnormalized spectral clustering for $k=2$ (p. 11).

**5.2 RatioCut, general $k$ (pp. 11–12).** Define $h_{i,j}=1/\sqrt{|A_j|}$ if $v_i\in A_j$, else 0 (5); $H\in\mathbb R^{n\times k}$ has these columns, so $H'H=I$. One finds $h_i'Lh_i=\mathrm{cut}(A_i,\bar A_i)/|A_i|=(H'LH)_{ii}$, hence
$$\mathrm{RatioCut}(A_1,\dots,A_k)=\sum_i h_i'Lh_i=\mathrm{Tr}(H'LH).$$
So the problem is $\min\mathrm{Tr}(H'LH)$ s.t. $H'H=I$, $H$ as in (5). Relaxing $H\in\mathbb R^{n\times k}$ gives the standard trace-minimization problem. By a version of Rayleigh–Ritz, $H$ = the first $k$ eigenvectors of $L$, i.e. the matrix $U$ of the algorithm. k-means on the rows of $U$ converts it back to a partition (p. 12).

**5.3 Ncut (pp. 12–13).** For $k=2$, define $f_i=\sqrt{\mathrm{vol}(\bar A)/\mathrm{vol}(A)}$ on $A$ and $-\sqrt{\mathrm{vol}(A)/\mathrm{vol}(\bar A)}$ on $\bar A$ (6). One checks $(Df)'\mathbb 1=0$, $f'Df=\mathrm{vol}(V)$, $f'Lf=\mathrm{vol}(V)\,\mathrm{Ncut}(A,\bar A)$. So the problem is (7): $\min_A f'Lf$ s.t. $f$ as in (6), $Df\perp\mathbb 1$, $f'Df=\mathrm{vol}(V)$. Relaxed (8): same with $f\in\mathbb R^n$. Substituting $g=D^{1/2}f$:
$$\min_{g\in\mathbb R^n}g'D^{-1/2}LD^{-1/2}g\ \text{ s.t. } g\perp D^{1/2}\mathbb 1,\ \|g\|^2=\mathrm{vol}(V).\tag{9}$$
Here $D^{-1/2}LD^{-1/2}=L_{\rm sym}$ and $D^{1/2}\mathbb 1$ is its first eigenvector. By Rayleigh–Ritz, $g$ is the second eigenvector of $L_{\rm sym}$. Re-substituting $f=D^{-1/2}g$ and using Prop. 3, $f$ is the second eigenvector of $L_{\rm rw}$, equivalently the generalized eigenvector of $Lu=\lambda Du$ (p. 12).

For $k>2$: $h_{i,j}=1/\sqrt{\mathrm{vol}(A_j)}$ if $v_i\in A_j$, else 0 (10). Then $H'H=I$, $h_i'Dh_i=1$, $h_i'Lh_i=\mathrm{cut}(A_i,\bar A_i)/\mathrm{vol}(A_i)$, so the problem is $\min\mathrm{Tr}(H'LH)$ s.t. $H'DH=I$, $H$ as in (10). With $T=D^{1/2}H$ and the discreteness dropped:
$$\min_{T\in\mathbb R^{n\times k}}\mathrm{Tr}(T'D^{-1/2}LD^{-1/2}T)\ \text{ s.t. } T'T=I.\tag{11}$$
The solution is the first $k$ eigenvectors of $L_{\rm sym}$. Then $H=D^{-1/2}T$ consists of the first $k$ eigenvectors of $L_{\rm rw}$, i.e. the generalized eigenvectors of $Lu=\lambda Du$. This is Shi–Malik (p. 13).

*Intuition note.* "Good partition" is encoded as a special indicator vector, so the cut value is a quadratic form in that vector. Dropping "takes only two values" turns an NP-hard search into an eigenvector problem. The price is that the real answer must be rounded back to clusters.

**5.4 Comments (pp. 13–14).** There is *no guarantee* on the relaxed solution's quality: $\mathrm{RatioCut}(B_1..B_k)-\mathrm{RatioCut}(A_1..A_k)$ can be arbitrarily large (p. 13).
- *Cockroach graph* (Guattery and Miller; Figure 2, a ladder of $4k$ vertices with some rungs removed). The best cut for $k=2$ is vertical, $A=\{v_1..v_k,v_{2k+1}..v_{3k}\}$: $|A|=|\bar A|=2k$, $\mathrm{cut}=2$, so $\mathrm{RatioCut}=2/k$. The authors prove that unnormalized spectral clustering always cuts horizontally, $B=\{v_1..v_{2k}\}$: $k$ edges cut, $\mathrm{RatioCut}(B,\bar B)=1$. This is $k/2$ times worse, a factor of order $n$ (p. 13).
- Efficient constant-factor approximation of balanced cuts is known not to exist in general; the approximation problem can itself be NP hard (p. 13).
- Other relaxations exist, e.g. a semi-definite program (p. 14). Spectral relaxation is popular because it gives a standard, simple linear-algebra problem, not because the solutions are particularly good (p. 14).

### 6 Random walks point of view (pp. 14–16)
Transition probability $p_{ij}=w_{ij}/d_i$; transition matrix $P=D^{-1}W$. If the graph is connected and non-bipartite, a unique stationary distribution exists: $\pi_i=d_i/\mathrm{vol}(V)$. Also $L_{\rm rw}=I-P$, so $\lambda$ is an eigenvalue of $L_{\rm rw}$ with eigenvector $u$ iff $1-\lambda$ is an eigenvalue of $P$ with eigenvector $u$. So it is no surprise that the largest eigenvectors of $P$ and the smallest of $L_{\rm rw}$ can describe cluster properties (p. 14).

**Proposition 5 (Meila and Shi).** Let $G$ be connected and non-bipartite, with $X_0\sim\pi$. For disjoint $A,B$ let $P(B|A):=P(X_1\in B\mid X_0\in A)$. Then $\mathrm{Ncut}(A,\bar A)=P(\bar A|A)+P(A|\bar A)$ (p. 14).
Proof: $P(X_0\in A,X_1\in B)=\sum_{i\in A,j\in B}\pi_ip_{ij}=\sum\frac{d_i}{\mathrm{vol}(V)}\frac{w_{ij}}{d_i}=\frac1{\mathrm{vol}(V)}\sum_{i\in A,j\in B}w_{ij}$. Dividing by $P(X_0\in A)=\mathrm{vol}(A)/\mathrm{vol}(V)$ gives $P(X_1\in B|X_0\in A)=\sum_{i\in A,j\in B}w_{ij}/\mathrm{vol}(A)$; the definition of Ncut finishes it (p. 15). So minimizing Ncut seeks a cut the walk seldom crosses (p. 15).

**Commute distance (pp. 15–16).** $c_{ij}$ is the expected time of the walk to go from $v_i$ to $v_j$ and back. Unlike the shortest-path distance, it shrinks when many short paths exist (p. 15). The generalized inverse is $L^\dagger:=U\Lambda^\dagger U'$, with $\Lambda^\dagger$ having entries $1/\lambda_i$ for $\lambda_i\ne0$ and 0 otherwise. Entries: $l^\dagger_{ij}=\sum_{k=2}^n\frac1{\lambda_k}u_{ik}u_{jk}$ (the sum starts at $k=2$, as printed, p. 15).

**Proposition 6.** For a connected undirected graph,
$$c_{ij}=\mathrm{vol}(V)\,(l^\dagger_{ii}-2l^\dagger_{ij}+l^\dagger_{jj})=\mathrm{vol}(V)\,(e_i-e_j)'L^\dagger(e_i-e_j).$$
It is cited from Klein and Randic (electrical-network proof); a first-step-analysis proof is in Fouss et al. (p. 15). So $\sqrt{c_{ij}}$ is a Euclidean distance. Take $z_i$ = the $i$-th row of $U(\Lambda^\dagger)^{1/2}$; then $\langle z_i,z_j\rangle=e_i'L^\dagger e_j$ and $c_{ij}=\mathrm{vol}(V)\|z_i-z_j\|^2$ (p. 16).

*Comparison with the spectral embedding (p. 16).* Spectral clustering uses the first $k$ columns of $U$; the commute embedding uses all columns, each scaled by $1/\sqrt{\lambda}$. With $k$ disconnected components the two differ strongly: the first $k$ columns of the scaled matrix are all zero, since $\lambda^\dagger=0$ there. For a connected graph the small-eigenvalue eigenvectors are emphasized, and the two embeddings "might" behave similarly. The author's view: it seems the commute distance can be a helpful intuition, but without further assumptions there is only a rather loose relation; the author has not yet seen a precise mathematical statement, and says the relation might be tightened (e.g. for strictly positive definite similarity functions); some authors claim the link in a "hand-waving" way (p. 16).

*Intuition note.* Ncut counts how often the walk jumps between the two sides. A balanced cut with few edges gives few jumps. The commute distance is a nice picture but not a proven equivalent of the spectral embedding.

### 7 Perturbation theory point of view (pp. 16–19)
*Ideal case:* between-cluster similarity is exactly 0. Then the first $k$ eigenvectors of $L$ or $L_{\rm rw}$ are indicators, and every $y_i$ equals a unit vector $(0,..,1,..,0)'$ that marks its component. k-means trivially recovers the clusters. *Nearly ideal case:* the Laplacian is a perturbed version of the ideal one, the eigenvectors stay close to the indicators, and k-means still separates the groups if the perturbation is not too large (pp. 16–17).

**7.1 Davis–Kahan (p. 17).** Principal angles: for $p$-dimensional subspaces with orthonormal bases $V_1,V_2$ (matrices), $\cos\Theta_i$ are the singular values of $V_1'V_2$. $\sin\Theta$ is the diagonal matrix of the sines.

**Theorem 7 (Davis–Kahan).** Let $A,H\in\mathbb R^{n\times n}$ be symmetric; $\|\cdot\|$ is the Frobenius or two-norm. Let $\tilde A=A+H$. Let $S_1\subset\mathbb R$ be an interval, $V_1$ the eigenspace for the eigenvalues of $A$ in $S_1$, $\tilde V_1$ the analogue for $\tilde A$. Let $\delta=\min\{|\lambda-s|:\lambda$ an eigenvalue of $A$, $\lambda\notin S_1$, $s\in S_1\}$. Then
$$d(V_1,\tilde V_1):=\|\sin\Theta(V_1,\tilde V_1)\|\le\frac{\|H\|}{\delta}.$$

Reading it for $L$ (p. 17): $A$ is the ideal $L$ with $k$ components, $\tilde A=\tilde L$ is the noisy version. We want $S_1$ to contain the first $k$ eigenvalues of both. This is easier the smaller $\|H\|$ and the larger the eigengap $|\lambda_k-\lambda_{k+1}|$. Then the perturbed eigenvectors are approximately piecewise constant. If $S_1=[0,\lambda_k]$, $\delta$ is the gap $|\lambda_{k+1}-\lambda_k|$ (as the author states). If no such $S_1$ exists, one compromises: compare the first $k$ eigenvectors of $L$ with the first $\tilde k$ of $\tilde L$, or the bound becomes useless as $\delta\to0$ (p. 18).

**7.2 Comments (p. 18).** Being block diagonal in the ideal case can be considered a *necessary but not sufficient* condition for eigenvectors to work. Two more properties are needed.
1. *Meaningful order of eigenvalues.* For Laplacians each component has exactly one 0-eigenvector, so the first $k$ eigenvectors give one per component. For $S$ or $W$ the two largest eigenvalues may come from the same block, so some blocks are represented twice and others missed. Hence eigenvectors of $S$ or $W$ are discouraged for clustering (p. 18).
2. *Entries safely away from 0.* After perturbation, tiny entries are ambiguous. For $L,L_{\rm rw}$ the ideal eigenvectors are indicators, so this does not occur. For $L_{\rm sym}$ the ideal eigenvectors are $D^{1/2}\mathbb 1_{A_i}$, so low-degree vertices give tiny entries (p. 18). Row normalization in Ng et al. addresses this in the ideal case (one non-zero entry per row, so $T$ holds indicators). In practice, a row $(\varepsilon_1,\varepsilon_2)$ is multiplied by $1/\sqrt{\varepsilon_1^2+\varepsilon_2^2}$, so points of different clusters may end up together. One could argue that such low-degree points are outliers anyway (p. 19).

**Conclusion (p. 19):** $L$ and $L_{\rm rw}$ are well justified by perturbation theory. $L_{\rm sym}$ can be justified but needs more care with very low degrees.

### 8 Practical details (pp. 19–27)
**8.1 Similarity graph (pp. 19–22).** Local behaviour of $s$ matters; the long-range value (0.01 vs 0.001) does not. For $\mathbb R^d$ a default is the Gaussian; no general advice otherwise (p. 19).
Figure 3 (two "moons" of different density plus a Gaussian, in $\mathbb R^2$) shows (pp. 19–20):
- *ε-graph:* hard to choose ε for data "on different scales". At $\varepsilon=0.3$ the middle moon is tightly connected while the Gaussian is barely connected.
- *k-NN graph:* connects points on different scales (low-density Gaussian to high-density moon). It can break into components where high-density regions are far apart (the two moons).
- *Mutual k-NN:* connects points within regions of constant density, not across different densities. It seems suited to clusters of different densities.
- *Fully connected* with Gaussian: $\sigma$ plays the role of ε, but the matrix is not sparse (pp. 20–21).

The author recommends the k-NN graph as first choice (sparse $W$, in the author's experience less sensitive to parameters) (p. 21).
Parameters (pp. 21–22): if the graph has more components than the requested $k$, spectral clustering trivially returns components. So make the graph connected or nearly so, with few or no isolated vertices. Asymptotic results: k-NN and mutual k-NN graphs are connected for $k$ of order $\log n$; for the ε-graph the cited result requires ε of order $(\log n/n)^d$ (as printed); these do not help on finite samples (p. 21). Rules of thumb:
- k-NN: connected, or at least significantly fewer components than clusters wanted; for very large graphs $k\sim\log n$.
- Mutual k-NN: "a bit lost"; it has far fewer edges, so choose larger $k$; no heuristic exists for allowing meaningful disconnected parts.
- ε-graph: ε = length of the longest edge of a minimal spanning tree (it is broken by outliers or far-apart tight clusters, which make ε too large).
- Gaussian $\sigma$: of the order of the mean distance to the $k$-th neighbour ($k\sim\log n+1$), or $\sigma=\varepsilon$ from the MST. These are "ad-hoc" (p. 22).

Spectral clustering "can be quite sensitive" to graph and parameters. No systematic study or firm theory exists (p. 22).

**8.2 Computing eigenvectors (p. 22).** For k-NN or ε graphs the Laplacians are sparse. Power method or Krylov methods such as Lanczos are used; convergence is faster for a larger eigengap $\gamma_k=|\lambda_k-\lambda_{k+1}|$. If an eigenvalue has multiplicity $>1$ (e.g. 0 with multiplicity $k$ in the ideal case), solvers return some orthonormal basis of the eigenspace. Every vector $u=\sum_{i}a_i\mathbb 1_{A_i}$ is piecewise constant on the clusters, so the information is still encoded.

**8.3 Number of clusters (pp. 22–24).** Generic tools exist: model-based criteria, gap statistic, stability, etc. (pp. 22–23). The *eigengap heuristic*: choose $k$ so that $\lambda_1..\lambda_k$ are very small but $\lambda_{k+1}$ is relatively large. Justifications: perturbation theory (ideal case, 0 has multiplicity $k$, then a gap), and spectral graph theory (cut sizes relate to the first eigenvalues) (p. 23). Figure 4: three samples with increasing Gaussian variance, eigenvalues of $L_{\rm rw}$ on the 10-NN graph. Four well-separated clusters show four near-zero eigenvalues and a clear gap. For blurrier clusters the gap between $\lambda_4$ and $\lambda_5$ is less clear. In the last set there is no gap (p. 23). The heuristic works well for pronounced clusters; ambiguous data give ambiguous results (p. 23). The choice of $k$ and of graph connectivity interact; if the graph has $k_0$ components, $k_0$ is a valid choice, but nothing non-trivial is known beyond that (p. 24).

**8.4 The k-means step (p. 24).** Using k-means is "nothing principled"; in the ideal case all points of cluster $C_s$ map to the same point $e_s$ and any algorithm works. One can argue that at least the Euclidean distance between the $y_i$ is meaningful: it is related to the commute distance, to a "diffusion distance" (Nadler et al.), and to other spectral embeddings. Alternatives: hyperplanes (Lang), or approximating the eigenvector subspace by piecewise constant vectors with weighted k-means (Bach and Jordan).

**8.5 Which Laplacian? (pp. 24–27).** If degrees are nearly equal, all Laplacians are similar; if broadly distributed they differ considerably (p. 24). The author's opinion: use normalized rather than unnormalized, and $L_{\rm rw}$ rather than $L_{\rm sym}$.
- *Objectives (pp. 24–25).* Objective 1: minimize between-cluster similarity $\mathrm{cut}(A,\bar A)$. Objective 2: maximize within-cluster similarity $W(A,A)$ and $W(\bar A,\bar A)$. Since $W(A,A)=W(A,V)-W(A,\bar A)=\mathrm{vol}(A)-\mathrm{cut}(A,\bar A)$, Ncut (small cut, large volume) serves both. The MinMaxCut criterion $\sum_i\mathrm{cut}(A_i,\bar A_i)/W(A_i,A_i)$ has the same relaxation as Ncut ($L_{\rm rw}$ eigenvectors). RatioCut balances vertex counts, which need not relate to within-cluster similarity (a large set with very weak internal edges). So unnormalized spectral clustering implements only objective 1 (p. 25).
- *Consistency (pp. 25–26).* With i.i.d. samples, both normalized algorithms are proved to converge: $L_{\rm sym}$ converges to an operator $U$ on $C(\mathcal X)$, under "very mild conditions" (cited). The induced partition has a diffusion interpretation. For unnormalized clustering, $(1/n)L$ converges to a limit operator $T$, but spectral clustering can fail to converge or converge to one-point clusters, even for small samples. The author states that $\lambda_i\ll\min_j d_j$ should hold for all $i=1..k$ used, to avoid these problems. Eigenvectors with eigenvalues above $\min d_j$ approximate Dirac functions (nearly 0 except in one coordinate). Figure 5 (toy data, $\sigma=2$ and $5$): as $\sigma$ grows the eigenvalues approach $\min d_j$ (for $\sigma=1$, eigenvalues 2, 3, 4 are significantly below; for $\sigma=2$ only the first three are below; for $\sigma=5$ only the first two), and the eigenvectors become Dirac-like. This affects only $L$, not $L_{\rm rw}$ or $L_{\rm sym}$ (pp. 26–27).
- *$L_{\rm rw}$ vs $L_{\rm sym}$ (p. 27).* All three explanations favour $L_{\rm rw}$: its eigenvectors are indicators, while those of $L_{\rm sym}$ carry the factor $D^{1/2}$ ("undesired artifacts"), with no computational advantage.

### 9 Outlook and further reading (pp. 27–29)
History: Donath and Hoffman (1973) used eigenvectors of the adjacency matrix; Fiedler (1973) linked bipartitions to the second Laplacian eigenvector; rediscovered in several communities (p. 27). Extensions: co-clustering, side information, weighted kernel k-means, learning similarity functions, distributed settings. Relations to kernel PCA rest on the smallest eigenvectors of Laplacians being the largest eigenvectors of kernel (Gram) matrices; two versions are given: $D^{-1/2}WD^{-1/2}$ (Bengio et al.) or Moore–Penrose inverses of $L$ or $L_{\rm sym}$ (Saerens et al.) (pp. 27–28). Strengths: few assumptions on cluster shape (unlike k-means, clusters need not be convex, e.g. intertwined spirals); efficient for sparse graphs; no local minima once the graph is chosen. Weakness: graph choice is non-trivial and the method can be unstable, so it is no "black box" (p. 28).

Other uses of Laplacians: $f'Lf$ small means $f$ varies little where data are dense, so it can regularize semi-supervised learning (the "cluster assumption"). The name comes from the analogy $w_{ij}=1/d_{ij}^2$ gives $w_{ij}(f_i-f_j)^2\approx((f_i-f_j)/d_{ij})^2$, a difference quotient, resembling $\langle g,Lg\rangle=\int|\nabla g|^2dx$. Convergence of graph Laplacians to Laplace(–Beltrami) operators is proved in several cited works (pp. 28–29).

## Toy example (ours, not from the text)
Graph on 4 vertices; edges 1–2 and 3–4 with weight 1, edge 2–3 with weight 0.1. Degrees: $d=(1,1.1,1.1,1)$.

$$L=\begin{pmatrix}1&-1&0&0\\-1&1.1&-0.1&0\\0&-0.1&1.1&-1\\0&0&-1&1\end{pmatrix}.$$

1. *Ideal case.* If the weight 0.1 were 0, the graph would have two components {1,2},{3,4}; eigenvalue 0 would have multiplicity 2 with eigenvectors $\mathbb 1_{\{1,2\}},\mathbb 1_{\{3,4\}}$ (Prop. 2).
2. *RatioCut identity.* Take $A=\{1,2\}$. Then $|A|=|\bar A|=2$, so $f=(1,1,-1,-1)$ by Eq. (2). $\mathrm{cut}(A,\bar A)=0.1$, so $\mathrm{RatioCut}=0.1/2+0.1/2=0.1$. Direct: $f'Lf=\tfrac12\cdot2\cdot0.1\cdot(1-(-1))^2=0.4$ (only edge 2–3 contributes, in both orders). And $|V|\cdot\mathrm{RatioCut}=4\cdot0.1=0.4$ ✓. Also $\sum f_i=0$ and $\|f\|^2=4=n$ ✓.
3. *Relaxation.* Try an antisymmetric eigenvector $(a,b,-b,-a)$. Row 1: $a-b=\lambda a$. Row 2: $-a+1.1b+0.1b=\lambda b$, i.e. $-a+1.2b=\lambda b$. The determinant condition is $(1-\lambda)(1.2-\lambda)-1=0$, i.e. $\lambda^2-2.2\lambda+0.2=0$. The smaller root is $\lambda=(2.2-\sqrt{4.04})/2\approx0.095$. Then $b=(1-\lambda)a\approx0.905a$, so $f_2\propto(1,0.905,-0.905,-1)$. It is $\le0.1$, the Rayleigh quotient of the discrete $f$ ($0.4/4$), as it must be since $f\perp\mathbb 1$.
4. *Rounding.* Signs of $f_2$ give $\{1,2\}$ vs $\{3,4\}$, the best cut. Here the relaxed solution recovers the discrete one (unlike the cockroach graph, p. 13).

## Concepts
- [[graph-laplacian]] — $L=D-W$; $f'Lf=\tfrac12\sum w_{ij}(f_i-f_j)^2$; author also uses the normalized $L_{\rm sym},L_{\rm rw}$ (pp. 4–5)
- [[adjacency-matrix]] — here a weighted symmetric $W$ with $w_{ij}\ge0$ (p. 2)
- [[positive-semidefinite-matrix]] — $L,L_{\rm sym},L_{\rm rw}$ all PSD, from the quadratic forms (pp. 4–6)
- [[eigenvector-eigenvalue]] — used with eigenvalues ordered increasingly; "first k" means smallest (p. 3)
- [[rayleigh-quotient]] — Rayleigh–Ritz theorem gives solutions of relaxed cut problems as bottom eigenvectors (pp. 11–12)
- [[pseudoinverse]] — $L^\dagger=U\Lambda^\dagger U'$ computes commute distance (p. 15)
- [[markov-stochastic-matrix]] — $P=D^{-1}W$, $L_{\rm rw}=I-P$; stationary $\pi_i=d_i/\mathrm{vol}(V)$ (p. 14)
- [[power-iteration]] — power method mentioned for eigenvectors of sparse Laplacians (p. 22)
- [[krylov-subspace-methods]] — Lanczos method, speed depends on eigengap (p. 22)
- [[fiedler-vector]] — second Laplacian eigenvector; Fiedler (1973) proposed it for bipartition; the author's own derivation is the $k=2$ relaxations (pp. 11, 27)
- [[principal-component-analysis]] — only mentioned as related via kernel matrices (p. 27)
- [[spectral-clustering]] (new) — cluster the rows of the first $k$ Laplacian eigenvectors with k-means (p. 6)
- [[ratiocut]] (new) — balanced cut objective using $|A_i|$; relaxation gives unnormalized clustering (p. 9)
- [[ncut]] (new) — balanced cut using $\mathrm{vol}(A_i)$; relaxation gives $L_{\rm rw}$ clustering (p. 9)
- [[relaxation-of-discrete-optimization]] (new) — dropping the two-valued constraint on indicators (pp. 10–12)
- [[commute-distance]] (new) — expected round-trip time; $c_{ij}=\mathrm{vol}(V)(e_i-e_j)'L^\dagger(e_i-e_j)$ (pp. 15–16)
- [[davis-kahan-theorem]] (new) — bounds eigenspace distance by $\|H\|/\delta$ (p. 17)
- [[eigengap-heuristic]] (new) — choose $k$ with $\lambda_1..\lambda_k$ small and $\lambda_{k+1}$ large (p. 23)
- [[similarity-graph-constructions]] (new) — ε-neighbourhood, k-NN, mutual k-NN, fully connected (p. 3)
- [[generalized-eigenproblem]] (new) — $Lu=\lambda Du$, equivalent to $L_{\rm rw}u=\lambda u$ (p. 5)

## Canonical instances
- [[four-gaussians-toy]] — 200 points, four Gaussians in $\mathbb R$; eigenvectors as indicators in kNN and thresholds in fully connected case (pp. 8–9)
- [[cockroach-graph]] — ladder graph where unnormalized spectral clustering is $k/2$ times worse in RatioCut (p. 13)
- [[two-moons-plus-gaussian]] — behaviour of ε, kNN, mutual kNN graphs on data of different densities (pp. 19–20)
- [[eigengap-three-datasets]] — eigengap fades as clusters blur (p. 23)
- [[dirac-eigenvectors-unnormalized]] — $L$ eigenvectors become Dirac-like when eigenvalues approach $\min d_j$ (pp. 26–27)

## Bridges (candidates)
- [same-math] Trace minimization $\min\mathrm{Tr}(H'LH)$ s.t. $H'H=I$ ↔ linear-algebra spine: Rayleigh quotient / Courant–Fischer extreme eigenvalues — same optimization, bottom-$k$ eigenvectors.
- [same-math] $L^\dagger$ and commute distance ↔ pseudoinverse: $A^+=V\Sigma^+U^T$ restricted to non-zero eigenvalues.
- [structural-analogy] $P=D^{-1}W$ and stationary $\pi$ ↔ PageRank / Markov steady state: a similar random-walk transition matrix and stationary distribution.
- [structural-analogy] Smoothness regularizer $f'Lf$ ↔ network science: signals smooth on a network (neighbours have similar values).
- [metaphor] Eigengap as "how well-separated the communities are" ↔ condition number: both measure spectral separation affecting stability.

## Questions this raises
- The author says the relation between the commute-time embedding and the spectral embedding is loose. Can it be made precise, e.g. for strictly positive definite similarity functions (p. 16)?
- Can the sensitivity to graph type and parameters (§8.1) be turned into theory-based rules (p. 22)?
- How do $k$ and the connectivity parameter interact once the graph is connected (p. 24)?
- Which conditions on $L_{\rm sym}$ and degree distributions make row normalization safe in practice (p. 19)?

## Reading notes
- Printed page = pdf page (offset 0). The paper is the arXiv version (arXiv:0711.0189v1), noted as appearing in *Statistics and Computing* 17(4), 2007 (p. 1).
- Text layer lost overbars (e.g. $\bar A$ shows as $A$) and some symbols; I checked against the images.
- Page 16 writes the embedding matrix as $U(\Lambda^\dagger)^{1/2}$ in one paragraph and $(\Lambda^\dagger)^{1/2}U$ in the next. Rows of $U(\Lambda^\dagger)^{1/2}$ are meant (as the text's $z_i$ definition).
- Page 17 writes $H=L-\tilde L$ although Theorem 7 defines $\tilde A=A+H$; the sign does not matter for $\|H\|$.
- Page 21: the exponent in $(\log(n)/n)^d$ for ε is printed as shown; I did not verify it.
- Page 24 has "sample point" where "same point" is evidently meant, and "$\mathbb R^d$" for the embedding space where $\mathbb R^k$ is meant.
- Page 13 prints "rimes", evidently a misprint for rungs.
- Page 13 (Ncut, $k>2$) states $H'H=I$ together with $h_i'Dh_i=1$; the constraint used in the problem is $H'DH=I$. The digest follows the printed text.
- Page 27 says $\sigma=1$ has eigenvalues 2–4 below $\min d_j$ (consistent with Fig. 1).
- The reference list (pp. 29–32) was not digested.

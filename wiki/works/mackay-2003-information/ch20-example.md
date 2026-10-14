---
id: mackay-2003-information/ch20-example
work: mackay-2003-information
unit: "20 An Example Inference Task: Clustering"
pages: 284-292
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# An Example Inference Task: Clustering

## L0 — One line
K-means groups data by hard assignment to the nearest mean; softening the assignment with a stiffness parameter β may fix some of its faults but is not going to fix all of them, which leads the author to a mixture-density-modelling view of clustering.

## L1 — The gist (≤ 120 words)
How can N data points be grouped into K clusters, and why? MacKay gives four motivations: prediction, lossy compression, spotting misfits, and models of neural learning. He presents K-means (assign each point to its nearest mean, then move each mean to the average of its points) and shows it always converges. It has ad hoc features and can be viewed as failing on clusters of unequal weight, unequal width or elongated shape. Soft K-means replaces "nearest" by a soft-min with stiffness β. The solutions section shows that for a single Gaussian with K = 2 and fixed β, a mean pair at 0 becomes unstable once the data variance exceeds 1/β. One parameter cannot fix everything.

**Prerequisites:** vectors and means; exponentials and the softmax form; Taylor series; Gaussian variance and fourth moment; fixed points of a map.

## L2 — Key ideas (5–10 bullets)
- Clustering has several purposes: prediction ("mixture density modelling"), lossy compression ("vector quantization"), flagging misfits, and modelling neural learning (pp. 284–285).
- K-means alternates an assignment step (nearest mean) and an update step (mean of assigned points) (p. 286).
- The outcome depends on the initialization: two runs with K = 4 reach different solutions (p. 287).
- K-means has no representation of cluster weight, breadth or shape, and it is "hard" (pp. 288–289).
- Soft K-means uses responsibilities from a soft-min with stiffness β; the update step is unchanged (p. 289).
- Energy argument: the total spring energy is a Lyapunov function, so K-means converges (p. 291).
- For a single Gaussian with K = 2, the mean at 0 is stable if $\sigma_1^2 \le 1/\beta$ and unstable otherwise; above that value there is a pitchfork bifurcation (p. 291).
- A "cheap theory" (a series continuation the author calls "rather suspect" but which fits well) gives the post-bifurcation means, $m=\pm\beta^{-1/2}(\sigma_1^2\beta-1)^{1/2}/(\sigma_1^2\beta)$ (p. 292).

## L3 — Walkthrough

### 20 Introduction: why cluster? (pp. 284–285)
Clustering = grouping N objects into K clusters (the author says hierarchical clustering is not discussed yet) (p. 284). Four motivations:
1. **Predictive power.** A good clustering lets us predict attributes of new objects; we believe the labels are meaningful and give a more efficient description. This type of clustering is sometimes called *mixture density modelling*. Its objective is the information content of the data, $\log 1/P(\{x\})$ (p. 284).
2. **Lossy compression.** Cluster names communicate briefly. In image compression, split an image into N patches, match each to one of K templates, and send the labels $k_1,\dots,k_N$. Building the template library is the same task as finding cluster centres. This type of clustering is sometimes called *vector quantization* (p. 284).
   - A vector quantizer has an assignment rule $x\to k(x)$ and a reconstruction rule $k\to m^{(k)}$. They are chosen to minimize the expected distortion
   $$D=\sum_x P(x)\,\tfrac12\left[m^{(k(x))}-x\right]^2 \tag{20.1}$$
   - The templates need not have natural meaning. The encoder resembles decoding an error-correcting code (p. 285).
3. **Misfits flag interesting objects.** Patches that a quantizer compresses badly may contain ships (p. 285).
4. **Models of neural learning.** K-means is a *competitive learning* algorithm: clusters compete to own data points (p. 285).

### 20.1 K-means clustering (pp. 285–288)
Setup: N points $\mathbf x^{(n)}$ in I-dimensional real space, K means $\mathbf m^{(k)}$, and a metric
$$d(\mathbf x,\mathbf y)=\tfrac12\sum_i (x_i-y_i)^2 \tag{20.2}$$
(p. 285). "K" is just the chosen number of clusters (p. 285).

**Algorithm 20.2** (p. 286). Initialize the means, e.g. at random values, then repeat the two steps until the assignments do not change.
- *Assignment:* $\hat k^{(n)}=\operatorname{argmin}_k\, d(\mathbf m^{(k)},\mathbf x^{(n)})$ (20.3). Equivalently, use responsibilities $r_k^{(n)}=1$ if $\hat k^{(n)}=k$, else 0 (20.4). Ties go to the smallest winning k.
- *Update:*
$$\mathbf m^{(k)}=\frac{\sum_n r_k^{(n)}\mathbf x^{(n)}}{R^{(k)}},\qquad R^{(k)}=\sum_n r_k^{(n)} \tag{20.5, 20.6}$$
If $R^{(k)}=0$, the mean stays where it is.

**Demonstrations.** With K = 2 on 40 points, the algorithm converges after three iterations, when assignments stop changing. The book states that K-means always converges to a fixed point (p. 285). Exercise 20.1 asks for a proof, with the hint of a physical analogy and a Lyapunov function: a function of the state that decreases whenever the state changes and is bounded below (p. 287).

With K = 4, the result depends on the initial condition (Fig. 20.4). Run 1 settles after five iterations with points fairly evenly split. Run 2 settles after six iterations with half the points in one cluster (p. 287).

*Intuition note:* K-means loops until the assignments stop changing, and different starting means can end in different solutions (Fig. 20.4). The Lyapunov argument below (p. 291) explains why the loop settles, but it does not single out one solution.

**Questions about the algorithm** (pp. 287–288). Why set the mean to the mean of assigned points? Where does d come from, and how could the "best" distance be chosen? (In vector quantization d is part of the problem definition; MacKay assumes data modelling.) How to choose K? How to choose among alternative clusterings for a given K?

**Where K-means may be viewed as failing** (p. 288):
- *Unequal clusters (Fig. 20.5).* 75 points come from a mixture of two Gaussians; the right one has one fifth of the points and is narrower. With K = 2, four points of the broad cluster are assigned to the narrow one, and both means lie left of the true centres. K-means uses only distances, with no representation of weight or breadth.
- *Elongated clusters (Fig. 20.6).* The only stable state slices both elongated clusters in half. K-means cannot represent cluster size or shape. MacKay concludes that "there is something wrong with the distance d" (p. 288).
- *Hard assignment.* Each point is assigned to exactly one cluster, has an equal vote with the other points there, and no vote in other clusters. Borderline points arguably should have a partial role in several clusters (pp. 288–289).

### 20.2 Soft K-means (p. 289)
**Algorithm 20.7** has one parameter, the stiffness β.
- *Assignment:*
$$r_k^{(n)}=\frac{\exp\!\big(-\beta\, d(\mathbf m^{(k)},\mathbf x^{(n)})\big)}{\sum_{k'}\exp\!\big(-\beta\, d(\mathbf m^{(k')},\mathbf x^{(n)})\big)} \tag{20.7}$$
The K responsibilities of a point sum to 1.
- *Update:* identical to (20.5)–(20.6), written (20.8), (20.9).

The only difference from hard K-means is that responsibilities can take values between 0 and 1: a "soft-min" replaces the "min". Exercise 20.2 asks to show that as $\beta\to\infty$ the algorithm becomes hard K-means, except for means with no assigned points, and to say what those means do instead of sitting still.

β has dimension inverse-length-squared. So $\sigma\equiv1/\sqrt\beta$ is a lengthscale. In Fig. 20.8 (K = 4, 40 points), σ is the circle radius. At the largest σ all four means converge exactly to the data mean. They then separate into two groups of two, and at shorter σ each pair bifurcates again (pp. 289–290).

*Intuition note:* β sets how sharply a point favours its nearest mean. Reading (20.7), small β makes a point's responsibilities more nearly equal across the means (our reading, not stated in the text). Ex. 20.2 asks the reader to show that as β→∞ the algorithm becomes hard K-means.

### 20.3 Conclusion (pp. 289–290)
Adding β may fix some problems, but "adding one stiffness parameter β is not going to make all these problems go away" (p. 290). Open: how to set β, elongated clusters, unequal weight and width. These return in a later chapter on mixture density modelling. Further reading: Luttrell 1989, 1990 (vector quantization) (p. 290).

### 20.4 Exercises (p. 290)
Ex. 20.3: study soft K-means fixed points for a single separable 2-D Gaussian with variances $\sigma_1^2>\sigma_2^2$, K = 2, N large, as β varies; hint $\mathbf m^{(1)}=(m,0)$, $\mathbf m^{(2)}=(-m,0)$. Ex. 20.4: data from two equal-weight 1-D Gaussians with means ±1 and standard deviation $\sigma_P$; the exercise asks to show that hard K-means (K = 2) puts the means further apart than ±1; find β that places the soft means correctly.

### 20.5 Solutions (pp. 291–292)
**Ex. 20.1 (p. 291).** Join each point to its responsible mean by a spring with energy proportional to squared length, $\beta d(\mathbf x^{(n)},\mathbf m^{(k)})$. The total energy is a Lyapunov function, because (a) the assignment step can only decrease it, since a point switches only if its spring shortens; (b) the update step can only decrease it, since the mean minimizes its springs' energy; (c) it is bounded below. Hence the algorithm converges.

**Ex. 20.3 setup (p. 291).** With $\mathbf m^{(1)}=(m,0)$ and $\mathbf m^{(2)}=(-m,0)$ (the page prints $\mathbf m^{(1)}$ twice; see Reading notes):
$$r_1(\mathbf x)=\frac{\exp(-\beta(x_1-m)^2/2)}{\exp(-\beta(x_1-m)^2/2)+\exp(-\beta(x_1+m)^2/2)}\tag{20.10}$$
$$=\frac1{1+\exp(-2\beta m x_1)}\tag{20.11}$$
The updated mean:
$$m'=\frac{\int dx_1\,P(x_1)\,x_1\,r_1(\mathbf x)}{\int dx_1\,P(x_1)\,r_1(\mathbf x)}\tag{20.12}$$
$$=2\int dx_1\,P(x_1)\,x_1\,\frac1{1+\exp(-2\beta m x_1)}\tag{20.13}$$
(The factor 2 comes from the denominator being $1/2$ when $P(x_1)$ is symmetric about 0, since $r_1(x_1)+r_1(-x_1)=1$; added step.)

**Stability of m = 0.** For tiny m ($\beta\sigma_1 m\ll1$):
$$\frac1{1+\exp(-2\beta m x_1)}\simeq\tfrac12(1+\beta m x_1)+\cdots\tag{20.14}$$
$$m'\simeq\int dx_1\,P(x_1)\,x_1(1+\beta m x_1)\tag{20.15}$$
$$=\sigma_1^2\beta m\tag{20.16}$$
So m grows or decays exponentially depending on whether $\sigma_1^2\beta$ is above or below 1. The fixed point m = 0 is stable if
$$\sigma_1^2\le1/\beta\tag{20.17}$$
and unstable otherwise. The derivation holds for any $P(x_1)$ with variance $\sigma_1^2$, not just a Gaussian. If $\sigma_1^2>1/\beta$ there is a bifurcation: two stable fixed points surround the unstable one at 0 (Fig. 20.9). Fig. 20.10 (β = 1, varying $\sigma_1$) and Fig. 20.11 (fixed $\sigma_1$, varying $1/\beta^{1/2}$) show this pitchfork (p. 291).

**Beyond the bifurcation (p. 292).** The author calls this a "cheap theory". The series continuation is "rather suspect", because the series need not converge beyond the bifurcation, but it fits well. One more term:
$$\frac1{1+\exp(-2\beta m x_1)}\simeq\tfrac12\big(1+\beta m x_1-\tfrac13(\beta m x_1)^3\big)+\cdots\tag{20.18}$$
$$m'\simeq\int dx_1\,P(x_1)x_1\big(1+\beta m x_1-\tfrac13(\beta m x_1)^3\big)\tag{20.19}$$
$$=\sigma_1^2\beta m-\tfrac13(\beta m)^3\,3\sigma_1^4\tag{20.20}$$
using the Gaussian fourth moment $3\sigma_1^4$. The approximate map has a fixed point at $m$ such that
$$\sigma_1^2\beta\big(1-(\beta m)^2\sigma_1^2\big)=1\tag{20.21}$$
$$m=\pm\beta^{-1/2}\frac{(\sigma_1^2\beta-1)^{1/2}}{\sigma_1^2\beta}\tag{20.22}$$
Figure 20.10's thin line shows this approximation.

*Intuition note:* When the data are spread out enough compared with the lengthscale σ, the symmetric pair of means at the centre (m = 0) is an unstable fixed point, and two stable fixed points appear on either side. The split starts at $\sigma_1^2=1/\beta$.

**Ex. 20.5 (p. 292).** As $1/\beta^{1/2}\to0$ the means tend to about ±0.8. The asymptote is the mean of the rectified Gaussian:
$$\frac{\int_0^\infty \mathrm{Normal}(x,1)\,x\,dx}{1/2}=\sqrt{2/\pi}\simeq0.798\tag{20.23}$$

## Toy example (ours)
1-D points $\{0,1,5,6\}$, K = 2, initial means $m_1=0,\ m_2=3$, $d=\tfrac12(x-m)^2$.

*Hard K-means.* Distances $(d_1,d_2)$: point 0: (0, 4.5), so cluster 1. Point 1: (0.5, 2), so cluster 1. Point 5: (12.5, 2), so cluster 2. Point 6: (18, 4.5), so cluster 2. Update: $m_1=(0+1)/2=0.5$, $m_2=(5+6)/2=5.5$. Reassigning gives the same assignments, so it has converged.

*Soft responsibilities for the point x = 2 with means 0 and 3:* $d_1=\tfrac12\cdot4=2$, $d_2=\tfrac12\cdot1=0.5$.
- β = 1: $r_1=e^{-2}/(e^{-2}+e^{-0.5})=0.1353/(0.1353+0.6065)=0.182$, so $r_2=0.818$.
- β = 4: $r_1=1/(1+e^{4(2-0.5)})=1/(1+e^{6})=1/404.4\approx0.0025$. This is nearly the hard answer (0, 1).

## Concepts
- [[k-means]] (new) — alternate nearest-mean assignment and mean update; a hard-assignment clustering algorithm (p. 286)
- [[clustering]] (new) — grouping N objects into K clusters (p. 284)
- [[mixture-density-modelling]] (new) — clustering judged by predictive information content $\log 1/P(\{x\})$ of the data (p. 284)
- [[vector-quantization]] (new) — clustering for lossy compression, with assignment rule $k(x)$ and reconstruction rule $m(k)$ minimizing distortion (pp. 284–285)
- [[responsibility]] (new) — degree $r_k^{(n)}$ to which cluster k owns point n; 0/1 in hard, in [0,1] in soft K-means (pp. 286, 289)
- [[soft-k-means]] (new) — K-means with soft-min responsibilities and stiffness β (p. 289)
- [[lyapunov-function]] (new) — a bounded-below function of the state that decreases at every change; guarantees convergence (p. 287)
- [[pitchfork-bifurcation]] (new) — as a parameter crosses a threshold, a stable fixed point becomes unstable and two stable fixed points appear on either side of it; here at $\sigma_1^2=1/\beta$ (p. 291)
- [[self-information]] — here only the objective $\log 1/P(\{x\})$ appears (p. 284)

## Canonical instances
- [[little-n-large-clusters]] (new) — in the Fig. 20.5 example, K-means assigns points of the broad cluster to the narrow one; the clusters differ in weight and breadth (p. 288)
- [[elongated-clusters-sliced]] (new) — K-means cuts two elongated clusters in half (p. 288)
- [[soft-kmeans-lengthscale-sweep]] (new) — Fig. 20.8: means merge at large σ and split at smaller σ (p. 290)

## Bridges (candidates)
- [structural-analogy] K-means two-step loop ↔ bayesian: assigning data to hidden causes, then re-fitting parameters, as in mixture-model inference — the book says it returns to this view later (p. 290)
- [same-math] soft-min responsibilities (20.7) ↔ softmax / Gibbs distribution $p\propto\exp(-\beta\,\text{energy})$ — same exponential-normalized form
- [structural-analogy] vector quantization ↔ information-theory: lossy compression with distortion (rate–distortion) — the chapter gives distortion (20.1) but no rate analysis
- [metaphor] encoder of a vector quantizer ↔ decoding of an error-correcting code (noted in passing, p. 285)

## Questions this raises
- How should β (or K) be chosen from data rather than by hand?
- Which probabilistic model has soft K-means as a special case, and how do cluster weight and shape enter it?
- Does the Lyapunov argument show convergence to a good solution, or only to some fixed point?
- How accurate is the post-bifurcation formula (20.22) far from the threshold?

## Exercises worth doing
- Ex. 20.2 (p. 289) — hard K-means as the $\beta\to\infty$ limit; what happens to empty means — difficulty: easy
- Ex. 20.4 (p. 290) — why hard K-means exaggerates the separation of two overlapping Gaussians, and the β that corrects it — difficulty: medium

(Ex. 20.1, 20.3 and 20.5 have printed solutions, covered in L3.)

## Reading notes
- Printed page = pdf − 12. Text layer was garbled in places; equations were checked against the images.
- Misprint on p. 291: the solution to Ex. 20.3 initializes "$\mathbf m^{(1)}=(m,0)$ and $\mathbf m^{(1)}=(-m,0)$"; the second should be $\mathbf m^{(2)}$ (matches the hint on p. 290).
- The printed solution to Ex. 20.3 covers only the stability and bifurcation of m = 0, plus the series approximation.
- The "stable if $\sigma_1^2\le1/\beta$" statement (20.17) is as printed; the text says m grows or decays according to whether $\sigma_1^2\beta$ is greater or less than 1 and does not discuss the equal case.
- Ex. 20.5's solution uses a unit-variance Normal; the pages do not say $\sigma_1=1$ in Fig. 20.11.

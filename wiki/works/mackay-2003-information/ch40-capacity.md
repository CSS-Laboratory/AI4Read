---
id: mackay-2003-information/ch40-capacity
work: mackay-2003-information
unit: "40 Capacity of a Single Neuron"
pages: 483-491
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Capacity of a Single Neuron

## L0 — One line
For large K, a binary threshold neuron (it outputs 1 if its weighted input sum is positive, otherwise 0) with K weights can almost certainly memorize up to N = 2K random binary labels, but will almost certainly fail to memorize more; its capacity is two bits per weight.

## L1 — The gist (≤ 120 words)
How much information can be stored by training a neural network? The chapter treats the trained weights as a communication channel. The receiver may only see the neuron's output on the N training inputs, so what counts is how many binary labellings of N points a threshold neuron can produce. For points in general position (roughly, like random points) this number is T(N,K) = 2 Σ_{k<K} C(N−1,k), found with a hyperplane-counting argument in weight space and a Pascal-triangle recurrence. For large K, the fraction T/2^N stays near 1 until N ≈ 2K, then collapses. Hence, for large K, the capacity is 2 bits per weight, and a neuron with K inputs stores 2K bits.

**Prerequisites:** binary labelling, dot product and hyperplanes (a plane through the origin), binomial coefficients and Pascal's triangle, Gaussian cumulative distribution, the idea of channel capacity.

## L2 — Key ideas (5–10 bullets)
- Learning is viewed as communication: the sender turns data D_N into weights w, and the receiver uses w, for example to reconstruct the targets (p. 483). This makes "capacity" a meaningful question for a network.
- The infinite-capacity answer (real-valued weights carry infinitely many bits) is excluded by letting the receiver observe only the neuron's outputs at the same N training points (pp. 483–484).
- Capacity is redefined as the largest N such that all N labels are reproduced with very small error probability; the author notes this departs a little from Chapter 9 (p. 484).
- The number of threshold functions T(N,K) is found by counting regions of weight space cut by hyperplanes (planes through the origin) x⁽ⁿ⁾·w = 0, one per data point (pp. 485–488).
- Adding the Nth hyperplane gives T(N,K) = T(N−1,K) + T(N−1,K−1), the Pascal recurrence. With the boundary conditions it gives T(N,K) = 2 Σ_{k=0}^{K−1} C(N−1,k) (pp. 488–489).
- T = 2^N for N ≤ K. The line N = K marks the largest number of points for which every labelling can be realized; this number, K, is the VC dimension of the class (p. 489).
- For large K, T/2^N is only negligibly below 1 up to N = 2K, then drops catastrophically (error-function approximation). Capacity is 2 bits per weight (p. 490).

## L3 — Walkthrough

### 40.1 Neural network learning as communication (p. 483)
- Setting: weights w are adapted to data D_N = {t_n} at given locations {x_n}. The sender sees D_N and produces a message w; the receiver uses w, for example to reconstruct D_N (Fig. 40.1) (p. 483).
- This is "memory" use of the neuron, not "generalization" (extrapolating to t_{N+1} at x_{N+1}) (p. 483).
- Weights play the role of a channel, like a disk drive. Question: how much information can be stored by training a network? (p. 483)
- Baseline: a learning algorithm that produces either a network answering +1 to all inputs or one answering 0 to all inputs, depending on the data, distinguishes only two sorts of data set. It conveys at most 1 bit, reached when the two kinds are equiprobable (p. 483).

### 40.2 The capacity of a single neuron (pp. 483–484)
- Claim to be shown: a single binary threshold neuron has capacity two bits per weight, so K inputs store 2K bits (p. 483).
- **Rules.** The receiver cannot examine the weights, and cannot probe the neuron at arbitrary inputs. It sees the output only at the fixed training points {x_n} (p. 484).
- So what matters is how many binary labellings of N points a linear threshold function can produce, compared with the maximum 2^N (p. 484).
- **Capacity** is defined as the largest N for which the error probability is very small (departing a little from Chapter 9) (p. 484).
- **Scenario.** The sender gets a neuron with K inputs and a labelling of N points, and uses an adaptive algorithm. We assume it finds a w reproducing the labelling exactly if one exists. The receiver evaluates the threshold function at the N inputs (p. 484).

**General position (Def. 40.1).** Points {x_n} in K-dimensional space are in general position if any subset of size ≤ K is linearly independent, and no K+1 of them lie in a (K−1)-dimensional plane (p. 484). In K = 3 this means no three collinear and no four coplanar. Such points behave like random points as far as linear dependences go (p. 484).

**The neuron.**
$$y = f\Big(\sum_{k=1}^{K} w_k x_k\Big)\tag{40.1}$$
$$f(a)=\begin{cases}1 & a>0\\ 0 & a\le 0\end{cases}\tag{40.2}$$
There is no bias. For a neuron with a bias, replace K by K+1 in the final result (one input fixed to 1). Those inputs are then not in general position, but the derivation still works (p. 484).

### 40.3 Counting threshold functions (pp. 485–490)
T(N,K) is the number of distinct threshold functions on N points in general position in K dimensions (p. 485).

**Cases by hand (p. 485).**
- K = 1: flipping the sign of w₁ labels the right of the origin 1 and the rest 0, or vice versa. So T(N,1) = 2.
- N = 1: w = ±x⁽¹⁾ gives both labellings. So T(1,K) = 2.
- K = 2: spin the separating line around the origin. Each time it passes a point we get a new function; in one revolution each point is passed twice, and general position means one point at a time. So T(N,2) = 2N.
- For K = 2 and N ≥ 3, not all 2^N functions are realizable. Example: XOR on x = (±1, ±1), N = 4, K = 2. These points are not in general position, but the author invites the reader to confirm that XOR stays unrealizable if they are perturbed into general position.

**Weight-space view, K = 2 (pp. 485–486).** Colour regions of weight space by the labelling they give. The weight vectors that label x⁽ⁿ⁾ as 1 form the half-space
$$\mathbf{x}^{(n)}\cdot\mathbf{w}>0\tag{40.3}$$
and the others occupy x⁽ⁿ⁾·w < 0 (Fig. 40.2). Two points give two lines and 4 regions (Fig. 40.3). Three points give three lines and 6 regions (Fig. 40.4); labellings (0,0,0) and (1,1,1) cannot be realized. So T(3,2) = 6 (p. 486). The caption says that for any three points in general position, two labellings are unrealizable.

**K = 3 (p. 486).** Add one point (one plane) at a time:
- N = 2: two planes, 4 regions, T(2,3) = 4.
- N = 3: three planes, 8 regions, T(3,3) = 8 (Fig. 40.5a).
- N = 4: the fourth plane cannot cut all 8 regions. Six regions are cut in two and two are unaffected, so T(4,3) = 14 (Fig. 40.5b). Two of the binary functions on 4 points in 3 dimensions are therefore not realizable (pp. 486, 488).

Table 40.6 (hand-found values, p. 487): row N=1 is 2 for every K; N=2: 2, 4, 4; N=3: 2, 6, 8; N=4: 2, 8, 14; N=5: 2, 10; N=6: 2, 12 (for K = 1, 2, 3).

**Why T(4,3) = T(3,3) + 6 (p. 488).** Six is the number of regions the new plane bisected. Equivalently, the new plane is itself a (K−1)-dimensional space cut into six regions by the N−1 earlier planes (Fig. 40.7c). The author asks how many regions N−1 hyperplanes create in K−1 dimensions, and answers T(N−1,K−1). Here that is T(3,2) = 6, so
$$T(4,3)=T(3,3)+T(3,2).\tag{40.4}$$

**Recurrence (p. 488).** When the Nth hyperplane is added in K dimensions, it bisects T(N−1,K−1) of the T(N−1,K) existing regions. The total is 2T(N−1,K−1) from the split regions, plus the T(N−1,K) − T(N−1,K−1) regions not split:
$$T(N,K)=T(N-1,K)+T(N-1,K-1).\tag{40.5}$$
Boundary conditions: T(N,1) = 2 and T(1,K) = 2.

> *Intuition note:* each new data point adds one plane through the origin in weight space. The plane only creates new regions where it crosses old ones, and the crossing pattern is itself a smaller counting problem one dimension down.

**Solving it (pp. 488–489).** Pascal's triangle (Table 40.8) has entries
$$C(N,K)\equiv\binom{N}{K}\equiv\frac{N!}{(N-K)!\,K!}\tag{40.6}$$
which satisfy
$$C(N,K)=C(N-1,K-1)+C(N-1,K),\ \text{for all }N>0\tag{40.7}$$
with the convention C(N,K) ≡ 0 if K > N or K < 0. So C(N,K) satisfies recurrence (40.5). That alone does not give T = C, since many functions satisfy one recurrence (p. 488).

The author seeks T as a linear superposition of shifted combinations C_{α,β}(N,K) ≡ C(N+α, K+β). Comparing Tables 40.8 and 40.6: translate Pascal's triangle right by 1, 2, 3, …; superpose; add; multiply by two; drop the table by one line. The result is
$$T(N,K)=2\sum_{k=0}^{K-1}\binom{N-1}{k}.\tag{40.8}$$
Since $\sum_{k=0}^{N-1}\binom{N-1}{k}=2^{N-1}$, the case K−1 ≥ N−1 simplifies:
$$T(N,K)=\begin{cases}2^{N} & K\ge N\\[2pt] 2\sum_{k=0}^{K-1}\binom{N-1}{k} & K<N.\end{cases}\tag{40.9}$$

**Interpretation (p. 489).** The ratio T(N,K)/2^N is the probability that an arbitrary labelling {t_n} can be memorized by the neuron. It equals 1 for all N ≤ K. The line N = K is the maximum number of points on which any arbitrary labelling can be realized. This number is the Vapnik–Chervonenkis (VC) dimension of the function class. The VC dimension of a binary threshold function on K dimensions is K.

**Large K (p. 490).** For N < 2K the ratio is still greater than 1/2, and for large K it is very close to 1. The sum is well approximated by an error function:
$$\sum_{0}^{K}\binom{N}{k}\simeq 2^{N}\,\Phi\!\left(\frac{K-(N/2)}{\sqrt{N}/2}\right)\tag{40.10}$$
with Φ(z) the Gaussian cumulative distribution (the printed integrand is $\exp(-z^2/2)/\sqrt{2\pi}$, integrated from $-\infty$ to z).

Figure 40.9 (p. 489) shows T/2^N from several viewpoints:
- It is approximately an error function in K, passing through 0.5 at K = N/2 and reaching 1 at K = N.
- It is 1 up to N = K and drops sharply at N = 2K.
- For K = 1000 there is a sudden drop at N = 2K.
- Panel (d) plots log₂T(N,K) and log₂2^N against N for K = 1000; in the image the two curves nearly coincide until about N = 2K (read from the plot, not stated in the caption).

Take-home (Fig. 40.9c, p. 490): for N > K the fraction is below 1, but only negligibly below 1 up to N = 2K. Then it falls catastrophically, and for N > 2K only a tiny fraction of labellings is realizable.

**Conclusion (p. 490).** For large K the capacity of a linear threshold neuron is 2 bits per weight. A single neuron can almost certainly memorize up to N = 2K random binary labels perfectly, but will almost certainly fail to memorize more.

> *Intuition note:* below N = K any labelling works. Between K and 2K, for large K, almost any labelling can still be realized: the fraction T/2^N is only negligibly below 1. Beyond 2K it drops catastrophically to a tiny fraction (p. 490).

### 40.4 Further exercises (p. 490)
Exercises 40.4–40.9 (see "Exercises worth doing"). Exercise 40.7 uses Fig. 40.10: three lines in a plane create seven regions. Exercise 40.8 uses 10¹¹ neurons with 1000 connections each and two bits per connection.

### 40.5 Solutions (p. 491)
For Exercise 40.5 the printed result is T(4,3)/2⁴ = 14/16 = 7/8 (eq. 40.11) (p. 491).

## Toy example (ours, not from the text)
Take K = 2, so T(N,2) = 2Σ_{k=0}^{1} C(N−1,k) = 2(1 + (N−1)) = 2N.

| N | T(N,2) | 2^N | T/2^N |
|---|---|---|---|
| 2 | 4 | 4 | 1 |
| 3 | 6 | 8 | 0.75 |
| 4 | 8 | 16 | 0.5 |
| 5 | 10 | 32 | 0.3125 |

This matches Table 40.6 (T(3,2) = 6) and shows 100% memorization up to N = K = 2, then a fall. At N = 2K = 4 the fraction is exactly 1/2.

Recurrence check (added step): T(5,3) = T(4,3) + T(4,2) = 14 + 8 = 22. Formula (40.8): 2(C(4,0)+C(4,1)+C(4,2)) = 2(1+4+6) = 22 ✓.

For K = 3, N = 6: T = 2(1+5+10) = 32, and 32/64 = 1/2, again 1/2 at N = 2K.

## Concepts
- [[channel-capacity]] — here, the largest N for which all N target bits are reproduced with very small error through the weights; the author says this departs a little from Chapter 9 (p. 484)
- [[noisy-channel]] — the trained weights are treated as a channel from training data to a future user (p. 483)
- [[general-position]] (new) — points where any ≤ K are linearly independent and no K+1 lie in a (K−1)-plane (p. 484)
- [[binary-threshold-neuron]] (new) — y = f(Σ w_k x_k), with f = 1 if a > 0 and 0 otherwise; no bias (p. 484)
- [[threshold-function-count]] (new) — T(N,K), the number of distinct labellings of N general-position points in K dimensions by a neuron (p. 485)
- [[weight-space-counting]] (new) — counting labellings as regions of w-space cut by the planes x⁽ⁿ⁾·w = 0 (p. 485)
- [[vc-dimension]] (new) — the largest number of points on which any labelling can be realized; K for threshold functions (p. 489)
- [[memorization-capacity]] (new) — for large K, about 2 bits per weight; almost certainly memorizes up to N = 2K random labels and almost certainly fails beyond (p. 490)

## Canonical instances
- [[xor-unrealizable]] — XOR on (±1,±1) cannot be realized by a linear threshold function (p. 485)
- [[t43-fourteen-regions]] — four planes divide 3-space into 14 regions, so T(4,3) = 14 (p. 486)
- [[pascal-recurrence-for-regions]] — T(N,K) = T(N−1,K) + T(N−1,K−1) solved by binomial sums (pp. 488–489)
- [[capacity-cliff-n-2k]] — the realizable fraction drops sharply at N = 2K (Fig. 40.9) (p. 489)

## Bridges (candidates)
- [structural-analogy] sharp drop of T/2^N at N = 2K ↔ information-theory: reliable communication below capacity and failure above — both show a threshold in the rate.
- [same-math] error-function approximation to a partial binomial sum (40.10) ↔ probability: normal approximation to the binomial cumulative distribution — the same calculation.
- [structural-analogy] counting labellings realizable by a model class (VC dimension) ↔ bayesian: how many datasets a model can fit, as in the marginal likelihood — both measure the flexibility of a model class.

## Questions this raises
- Does the 2-bits-per-weight result change for networks with many neurons or hidden layers, where weights act through several layers?
- What happens if the points are not in general position, or the labels are not random (for example, structured data)?
- What is the effect of a learning algorithm that does not always find an exact solution when one exists?
- How does memory capacity (this chapter) relate to generalization to the new point x_{N+1}?

## Exercises worth doing
- Ex. 40.4 (p. 490) — whether 2N points can be halved by a line or hyperplane, with and without general position — difficulty: medium
- Ex. 40.5 (p. 490) — four random points on a sphere lying in one hemisphere, and its link to T(N,K); a solution is printed on p. 491 — difficulty: medium
- Ex. 40.6 (p. 490) — find weight vectors for given labellings in K = 3, and an unrealizable labelling — difficulty: medium
- Ex. 40.7 (p. 490) — remove the through-the-origin constraint; count regions made by N lines in general position (Fig. 40.10) — difficulty: hard
- Ex. 40.8 (p. 490) — Fermi estimate of life's sensory input versus brain capacity (10¹¹ neurons × 1000 synapses × 2 bits) — difficulty: medium
- Ex. 40.9 (p. 491) — capacity of a spiking axon in bits per second — difficulty: hard

## Reading notes
- Printed page = pdf − 12 (pdf 495–503 ↔ printed 483–491).
- The text layer for Figs. 40.5, 40.7 and 40.9 is garbled. I used the images for the 3D illustrations and captions, and the table 40.6 values are read from the image.
- In eq. (40.10) the sum is written from 0 to K with C(N,k), while the exact formula (40.9) uses C(N−1,k) up to K−1. The author says that, for our purposes, the sum in (40.9) is well approximated by the error function (40.10); the Fig. 40.9 caption says the figures were plotted using that approximation.
- The printed definition of Φ(z) (p. 490) has an integrand with no dz and reuses z inside the integral. The meaning is clearly the Gaussian cumulative distribution.
- No other misprints noticed.
- The unit ends at the solution of Exercise 40.5 on p. 491; solutions for the other exercises are not printed in these pages.

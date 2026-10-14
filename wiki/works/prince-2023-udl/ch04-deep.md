---
id: prince-2023-udl/ch04-deep
work: prince-2023-udl
unit: "Chapter 4 — Deep neural networks"
pages: 41-55
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Deep neural networks

## L0 — One line
A deep network (more than one hidden layer) is a ReLU-based piecewise linear function that can produce many more linear regions for a given number of parameters than a shallow one; two ways to picture this are that layers "fold" the input space or clip what the previous layer produced.

## L1 — The gist (≤ 120 words)
Shallow networks can already approximate any continuous function, but for some functions they would need impractically many hidden units. The chapter asks what extra hidden layers buy. Composing two shallow networks is shown to be a special case of a two-hidden-layer network. The first network folds the input space and the second network's function is repeated over the folds. Matrix notation then gives the general formula for K layers. Deep networks create many more linear regions per parameter, can be much more efficient for some functions, suit large structured inputs, and give the best results for most tasks. The author notes it is unclear that real-world functions exploit this, and that training and generalization are not well understood.

**Prerequisites:** ReLU and shallow networks (chapter 3: hidden units, piecewise linear functions); matrix–vector multiplication and matrix shapes; the binomial coefficient.

## L2 — Key ideas
- Composing two shallow networks (three hidden units each) gives a function whose number of linear regions is potentially greater than for one shallow network with six hidden units. With three alternating regions in the first network, the second network's function is duplicated three times, giving nine regions (p. 43).
- Composition is a special case of a two-hidden-layer network. The deep network has nine free slope parameters ψ, whereas the composition constrains them to an outer product (p. 45).
- Two views of a deep network: layers "fold" the input space, or layers clip functions with ReLU and recombine them. Each view gives only partial insight, and the network is still just one equation from x to y′ (p. 46).
- General K-layer network in matrix form: y = β_K + Ω_K a[β_{K−1} + Ω_{K−1}(…)], with specified shapes for every Ω_k and β_k (pp. 49, 48).
- Depth and width are hyperparameters, chosen before the model parameters are learned (p. 46).
- For one input and one output, a deep network can have up to (D+1)^K regions with 3D+1+(K−1)D(D+1) parameters. A shallow one can have up to D+1 regions with 3D+1 parameters (both for D > 2) (p. 50).
- A larger region count is not clearly an advantage: the regions have complex dependencies and symmetries. It is not clear that it helps unless real-world functions have similar symmetries or the mapping really is a composition of simpler functions (p. 50).
- Other possible advantages of depth: depth efficiency (not clear it applies to real-world functions), local-to-global processing of images, and (it seems) easier training and better generalization. Training and generalization are not well understood (pp. 50–51).

## L3 — Walkthrough

### Intro (p. 41)
With ReLU, both shallow and deep networks give piecewise linear maps. Shallow networks with enough hidden units can describe arbitrarily complex functions. For some functions, though, the number of units needed is impractically large. Deep networks make many more linear regions for a given parameter count (p. 41).

### 4.1 Composing neural networks (pp. 41–43)
First network (input x, output y), with $a[\cdot]$ the activation function:
$$h_d = a[\theta_{d0}+\theta_{d1}x],\ d=1,2,3 \tag{4.1}$$
$$y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3 \tag{4.2}$$
Second network takes y as input:
$$h'_d=a[\theta'_{d0}+\theta'_{d1}y],\ d=1,2,3 \tag{4.3}$$
$$y'=\phi'_0+\phi'_1h'_1+\phi'_2h'_2+\phi'_3h'_3 \tag{4.4}$$
(pp. 41, 43). With ReLU, this is again piecewise linear, but the number of regions is potentially greater than for a shallow network with six hidden units (p. 43).

Worked case (fig. 4.1): let the first network produce three regions with alternating slope sign. Three input ranges then map to the same y range [−1, 1]. The second mapping is applied three times, so its function is duplicated three times, giving nine linear regions (p. 43). Fig. 4.2 shows a 2D example: the first network has 7 regions (one flat); the second splits each of the 6 non-flat regions in two, giving 13 regions (p. 44).

Folding view: the first network "folds" the input space onto itself, and the second network's function is replicated wherever points were folded together (p. 43, fig. 4.3).

*Intuition note:* If the first network is chosen so that several different inputs land on the same intermediate value, whatever the second network does to that value is repeated for each of those inputs (p. 43). In the example this gives 3 × 3 = 9 regions.

### 4.2 From composing networks to deep networks (pp. 43–45)
y is linear in h₁, h₂, h₃. The second network's first step is linear in y. A linear function of a linear function is linear, so substituting (4.2) into (4.3) gives
$$h'_1=a[\theta'_{10}+\theta'_{11}\phi_0+\theta'_{11}\phi_1h_1+\theta'_{11}\phi_2h_2+\theta'_{11}\phi_3h_3]\tag{4.5}$$
and similarly for $h'_2,h'_3$ (p. 43). This is rewritten as
$$h'_d=a[\psi_{d0}+\psi_{d1}h_1+\psi_{d2}h_2+\psi_{d3}h_3],\ d=1,2,3\tag{4.6}$$
with $\psi_{10}=\theta'_{10}+\theta'_{11}\phi_0$, $\psi_{11}=\theta'_{11}\phi_1$, $\psi_{12}=\theta'_{11}\phi_2$, and so on (p. 45). This is a network with two hidden layers (fig. 4.4). It represents a broader family than composition: in (4.6) the nine slopes $\psi_{11},\dots,\psi_{33}$ are arbitrary. In (4.5) they are constrained to the outer product $[\theta'_{11},\theta'_{21},\theta'_{31}]^T[\phi_1,\phi_2,\phi_3]$ (p. 45).

### 4.3 Deep neural networks (pp. 45–47)
General two-layer, three-unit network: first layer (4.7), second layer (4.8), output (4.9):
$$h_d=a[\theta_{d0}+\theta_{d1}x]\tag{4.7}$$
$$h'_d=a[\psi_{d0}+\psi_{d1}h_1+\psi_{d2}h_2+\psi_{d3}h_3]\tag{4.8}$$
$$y'=\phi'_0+\phi'_1h'_1+\phi'_2h'_2+\phi'_3h'_3\tag{4.9}$$
Second view, "clip and recombine" (fig. 4.5), in four steps (p. 46):
1. First-layer hidden units are computed as usual.
2. Second-layer pre-activations are three new linear functions of them, so we have effectively a shallow network with three outputs. Their joints (points where slope changes) are in the same places.
3. The second ReLU clips each function and adds new joints.
4. The output is a linear combination of the results.

The folding view stresses dependencies in the output function but not how clipping creates joints. The clipping view stresses the opposite. Both give only partial insight. The whole network is a single equation (4.10), "admittedly rather difficult to understand": $y'$ is $\phi'_0$ plus $\phi'_d\,a[\psi_{d0}+\sum_j\psi_{dj}\,a[\theta_{j0}+\theta_{j1}x]]$ summed over d = 1, 2, 3 (p. 46).

*Intuition note:* Each ReLU in the second layer clips its input function and adds new joints (bend points) to it (p. 46). This is one way to see how a deeper network can have more regions.

**4.3.1 Hyperparameters (p. 46).** Width = hidden units per layer; depth = number of hidden layers; total hidden units = capacity. K layers with sizes $D_1,\dots,D_K$ are hyperparameters, chosen before learning the slopes and intercepts. A network is therefore a "family of families" of functions (p. 46).

### 4.4 Matrix notation (pp. 48–49)
Equations 4.11–4.13 write 4.7–4.9 with vectors and matrices (p. 48). Compactly:
$$\mathbf h=\mathbf a[\boldsymbol\theta_0+\boldsymbol\theta x],\quad \mathbf h'=\mathbf a[\boldsymbol\psi_0+\boldsymbol\Psi\mathbf h],\quad y'=\phi'_0+\boldsymbol\phi'\mathbf h'\tag{4.14}$$
where $\mathbf a[\cdot]$ applies the activation to every element separately (p. 49).

**4.4.1 General formulation.** With $\mathbf h_k$ the hidden units of layer k, $\boldsymbol\beta_k$ the biases feeding layer k+1, and $\boldsymbol\Omega_k$ the weights from layer k to k+1:
$$\mathbf h_1=\mathbf a[\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x],\ \ \mathbf h_{k+1}=\mathbf a[\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf h_k],\ \ \mathbf y=\boldsymbol\beta_K+\boldsymbol\Omega_K\mathbf h_K\tag{4.15}$$
Here $k=1,\dots,K-1$ in the middle rule; the author lists the layers $\mathbf h_2,\mathbf h_3,\dots,\mathbf h_K$ explicitly (p. 49). Parameters: $\boldsymbol\phi=\{\boldsymbol\beta_k,\boldsymbol\Omega_k\}_{k=0}^K$.

Shapes (p. 49): $\boldsymbol\beta_{k-1}$ has size $D_k$; $\boldsymbol\beta_K$ has size $D_o$ (output). $\boldsymbol\Omega_0$ is $D_1\times D_i$; $\boldsymbol\Omega_K$ is $D_o\times D_K$; the others $\boldsymbol\Omega_k$ are $D_{k+1}\times D_k$. Fig. 4.6 example: $D_i=3$, $D_1=4$, $D_2=2$, $D_3=3$, $D_o=2$, so $\boldsymbol\Omega_0\in\mathbb R^{4\times3}$, $\boldsymbol\Omega_1\in\mathbb R^{2\times4}$, $\boldsymbol\Omega_2\in\mathbb R^{3\times2}$, $\boldsymbol\Omega_3\in\mathbb R^{2\times3}$; $\boldsymbol\beta_0\in\mathbb R^4$, $\boldsymbol\beta_1\in\mathbb R^2$, $\boldsymbol\beta_2\in\mathbb R^3$, $\boldsymbol\beta_3\in\mathbb R^2$ (p. 48).

As one function:
$$\mathbf y=\boldsymbol\beta_K+\boldsymbol\Omega_K\mathbf a\big[\boldsymbol\beta_{K-1}+\boldsymbol\Omega_{K-1}\mathbf a[\dots\boldsymbol\beta_2+\boldsymbol\Omega_2\mathbf a[\boldsymbol\beta_1+\boldsymbol\Omega_1\mathbf a[\boldsymbol\beta_0+\boldsymbol\Omega_0\mathbf x]]\dots]\big]\tag{4.16}$$
(p. 49).

### 4.5 Shallow vs. deep (pp. 49–51)
**4.5.1 Approximation.** A two-hidden-layer network can represent the composition of two shallow networks. If the second computes the identity, it replicates one shallow network. Hence it can approximate any continuous function arbitrarily closely given sufficient capacity (p. 50).

**4.5.2 Regions per parameter.** For one input, one output and D > 2 hidden units (p. 50):
- Shallow: up to D+1 regions, 3D+1 parameters.
- Deep, K layers of D units: up to $(D+1)^K$ regions, $3D+1+(K-1)D(D+1)$ parameters.

Fig. 4.7a: with K = 5, D = 10, there are 471 parameters and 161,051 regions. Fig. 4.7b ($D_i=10$): K = 5, D = 50 gives 10,801 parameters and more than $10^{40}$ regions (p. 51). The effect grows with input dimension (p. 50).

Caveat: flexibility is still limited by parameters. The regions have complex dependencies and symmetries (as in folding). It is not clear that the greater number of regions is an advantage unless (i) there are similar symmetries in the real-world functions we wish to approximate or (ii) we have reason to believe the mapping really does involve a composition of simpler functions (p. 50).

**4.5.3 Depth efficiency.** Functions exist that need exponentially more hidden units in a shallow network to match a deep one. It is not clear that real-world functions are of this kind (p. 50).

**4.5.4 Large structured inputs.** Fully connected networks are impractical for inputs like images of ~10⁶ pixels: too many parameters, and the same object should be recognized at any position. The solution is to process local regions in parallel and integrate gradually, which is hard to specify without multiple layers (chapter 10) (pp. 50–51).

**4.5.5 Training and generalization.** Moderately deep networks are usually easier to train than shallow ones. The author says over-parameterized deep models *may* have many roughly equivalent solutions that are easy to find. Training gets harder again with many more layers. Deep networks also seem to generalize better, and the best results for most tasks use tens or hundreds of layers. Neither phenomenon is well understood (p. 51).

### 4.6 Summary (p. 52)
Five points: (i) both can approximate any function given enough capacity; (ii) deep networks give many more regions per parameter; (iii) some functions are much more efficiently approximated by deep networks; (iv) large structured inputs are best processed in stages; (v) in practice deep networks give the best results for most tasks. Next: loss functions (p. 52).

### Notes (pp. 52–53)
- History: "deep learning" first used by Dechter (1986). The modern era was kick-started by Krizhevsky et al. (2012). The author says it was *arguably* due to four factors: bigger datasets, more compute, ReLU, and stochastic gradient descent (p. 52).
- Regions: with D hidden units in total, the upper bound is $2^D$ (Montúfar et al., 2014). For $D_i$ inputs and K layers of $D\ge D_i$ units, the count is $O\big((D/D_i)^{(K-1)D_i}D^{D_i}\big)$ (p. 52). If every one of the K layers has the same number D of hidden units and D is an integer multiple of $D_i$, the maximum is exactly
$$N_r=\Big(\tfrac{D}{D_i}+1\Big)^{D_i(K-1)}\cdot\sum_{j=0}^{D_i}\binom{D}{j}\tag{4.17}$$
The first factor comes from the first K−1 layers (repeated folding, using D/D_i units per input dimension). The sum is the shallow-network region count from the last layer (p. 53).
- Universal approximation: if the layers of a deep network have enough hidden units, the "width version" of the theorem applies (p. 53). Lu et al. (2017) proved a "depth version": with enough layers, ReLU networks with at least $D_i+4$ units per layer can approximate any Lebesgue integrable function to any given accuracy (p. 53).
- Depth efficiency results: Telgarsky (2016) shows networks with one input and output and O[k³] layers of constant width that cannot be realized with O[k] layers and width below 2^k. Eldan & Shamir (2016) show a three-layer network with multivariate input that no two-layer network can realize if the capacity is sub-exponential in the input dimension. Liang & Srikant (2016) cover a broad class (p. 53).
- Width efficiency (Lu et al.): some wide shallow networks need narrow networks of polynomial depth. This bound is less restrictive than the exponential one, suggesting depth is more important. Vardi et al. (2022): for ReLU networks, the price of making the width small is only a linear increase in depth (p. 53).

## Toy example (ours, not from the text)
Take x ∈ [0, 1], ReLU activations.
- Network 1: $h_1=\mathrm{ReLU}(2x)$, $h_2=\mathrm{ReLU}(4x-2)$, $y=h_1-h_2$. For x ≤ 0.5, y = 2x. For x ≥ 0.5, y = 2x − (4x−2) = 2 − 2x. So y rises 0→1, then falls 1→0.
- Network 2: $g(y)=\mathrm{ReLU}(y)-2\,\mathrm{ReLU}(y-0.5)$. For y ≤ 0.5, g = y. For y ≥ 0.5, g = y − 2y + 1 = 1 − y.

| x | y | y′ = g(y) |
|---|---|---|
| 0 | 0 | 0 |
| 0.125 | 0.25 | 0.25 |
| 0.25 | 0.5 | 0.5 |
| 0.375 | 0.75 | 0.25 |
| 0.5 | 1 | 0 |
| 0.625 | 0.75 | 0.25 |
| 0.75 | 0.5 | 0.5 |
| 0.875 | 0.25 | 0.25 |
| 1 | 0 | 0 |

The composite has peaks at x = 0.25 and x = 0.75 and zeros at 0, 0.5, 1. It has 4 linear regions. The second network alone has 2 regions on [0, 1]. The first network folds [0, 1] onto [0, 1] twice (once forward, once reversed), so g's shape appears twice, the second copy flipped, giving 2 × 2 = 4 regions.

## Concepts
- [[deep-neural-network]] (new) — network with more than one hidden layer (p. 41)
- [[width-depth-capacity]] (new) — width = units per layer, depth = number of hidden layers, total hidden units = capacity (p. 46)
- [[hyperparameter]] (new) — quantity such as K or D_k chosen before learning the parameters (p. 46)
- [[linear-region-counting]] (new) — counting pieces of a ReLU network's piecewise linear function; deep networks give more per parameter (p. 50)
- [[folding-view]] (new) — a layer folds input space so a later function is repeated over folded points (p. 43)
- [[depth-efficiency]] (new) — some functions need exponentially more units in a shallow network than a deep one (p. 50)
- [[universal-approximation]] (new) — enough hidden units per layer (width version, continuous functions) or enough layers (depth version, Lebesgue-integrable functions, Lu et al.) allow arbitrarily close approximation (pp. 50, 53)
- [[feed-forward (MLP) block]] — here, the fully connected layer stack of eq. 4.15 (p. 49)

## Canonical instances
- [[folding-two-networks]] (new) — fig. 4.1: the second network's function is duplicated three times, giving nine regions (p. 43)
- [[regions-per-parameter]] (new) — K = 5, D = 10: 471 parameters, 161,051 regions (p. 51)
- [[fully-connected-vs-image]] (new) — why 10⁶-pixel images need local processing (p. 51)

## Bridges (candidates)
- [structural-analogy] repeated folding/composition multiplies regions ↔ function composition generally: depth multiplies what width only adds — both build complexity by composing simple pieces.
- [same-math] $\mathbf h_{k+1}=\mathbf a[\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf h_k]$ ↔ llm: the per-token feed-forward (MLP) block of a Transformer, which has the same linear-then-activation form (canon link; not stated in this unit).
- [metaphor] hyperparameters as a "family of families" ↔ model selection: choosing K and D picks a function class before fitting.

## Questions this raises
- Do real-world functions have the symmetries or compositional structure that would make extra linear regions useful (p. 50)?
- Why are moderately deep networks easier to train than shallow ones, and why does training get harder again with many more layers (p. 51)?
- Why do deep networks seem to generalize better (p. 51)?
- How are loss functions defined and parameters found (chapters 5–7, p. 52)?

## Exercises worth doing
- Ex. 4.1 (p. 53) — draw the composition of two given networks (fig. 4.8); builds the folding intuition — easy
- Ex. 4.3 (p. 54) — ReLU non-negative homogeneity: rescaling weights and biases leaves the function unchanged — medium
- Ex. 4.4 (p. 54) — write out a network and give the shapes of all Ω and β — easy
- Ex. 4.8 (p. 55) — build an oscillating function and count regions under repeated composition — hard
- Ex. 4.10 (p. 55) — derive the parameter count $3D+1+(K-1)D(D+1)$ — medium
- Ex. 4.11 (p. 55) — compare a shallow and a deep network using eq. 4.17 — medium

## Reading notes
- Printed page = pdf − 14 (pdf 55–69 = printed 41–55). Page footers read "Draft: please send errata…", so this is a draft edition.
- No page images were provided for pdf 66–67 (printed 52–53). Eq. 4.17 and the "2^D" bound come from the text layer, where superscripts are flattened (the text layer prints "2D" for the bound; reading it as 2^D is my inference). I read 4.17 from the layout. Check: with $D_i=1$ it gives $(D+1)^{K-1}(1+D)=(D+1)^K$, matching p. 50. The $O(\cdot)$ bound is also from text only.
- The text calls problems 4.1, 4.8, 4.9 and 4.11 starred (∗); the source does not explain the star in these pages.
- In figure 4.5 (printed p. 47, pdf 61) the axes run x from 0 to 2, unlike the earlier figures. This does not affect the argument.

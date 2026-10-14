---
id: prince-2023-udl/ch03-shallow
work: prince-2023-udl
unit: "Chapter 3 — Shallow neural networks"
pages: 25-40
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Shallow neural networks

## L0 — One line
A shallow network computes several linear functions of the input, clips each with an activation function, and sums them with weights. With ReLU activations this gives a piecewise linear function that, with enough hidden units, can approximate any continuous function.

## L1 — The gist (≤ 120 words)
One-input linear regression can only draw a line. The chapter asks which models can describe richer input/output relations. The answer is the shallow neural network, with one hidden layer. Each hidden unit (a clipped linear function of the input) makes one "joint", a bend. With ReLU activations (clipping negatives to zero), the network is a continuous piecewise linear function. With one input and D hidden units it has at most D + 1 linear regions. With more inputs, the regions are convex polytopes (flat-sided cells), and their number grows rapidly with input dimension. With enough hidden units, such a network can approximate any continuous function to any precision. The chapter also fixes terminology (layers, weights, biases, MLP) for later chapters.

**Prerequisites:** the supervised-learning setup of Chapter 2 (model, parameters, least-squares loss); lines $y=a+bx$; sums; vectors in $\mathbb{R}^n$.

## L2 — Key ideas
- The basic building block is a linear function of the input followed by a ReLU, which clips negative values to zero. The output is a weighted sum of such blocks plus an offset (pp. 25–27).
- Each hidden unit contributes one joint. Each linear region has its own activation pattern (which units are active), and its slope comes from the active units (p. 27).
- The number of hidden units is a measure of network capacity. A one-input network with $D$ ReLU units has at most $D$ joints and $D+1$ regions (p. 29).
- Universal approximation: with enough hidden units, some shallow network approximates any continuous function on a compact set to any chosen precision (p. 29, p. 38).
- Multiple outputs share hidden units, so their joints sit in the same places. Slopes and heights can differ (p. 31).
- Multiple inputs give oriented planes clipped along hyperplanes. The regions become convex polytopes, and their number grows rapidly with input dimension (pp. 32–34).
- The activation must be nonlinear. A linear activation would make the whole mapping linear (p. 35).
- Terminology: layers, weights, biases, pre-activations and activations, MLP, feed-forward, fully connected (pp. 35–36).

## L3 — Walkthrough

### 3.1 Neural network example (pp. 25–29)
A shallow network is a function $\mathbf y=\mathbf f[\mathbf x,\boldsymbol\phi]$ mapping multivariate inputs to multivariate outputs (p. 25). The chapter starts with a scalar-to-scalar network with ten parameters $\boldsymbol\phi=\{\phi_0,\dots,\phi_3,\theta_{10},\theta_{11},\theta_{20},\theta_{21},\theta_{30},\theta_{31}\}$ (p. 25):

$$y=f[x,\boldsymbol\phi]=\phi_0+\phi_1 a[\theta_{10}+\theta_{11}x]+\phi_2 a[\theta_{20}+\theta_{21}x]+\phi_3 a[\theta_{30}+\theta_{31}x]\tag{3.1}$$

Three steps: compute three linear functions of the input; pass each through an activation function $a[\bullet]$; weight the results by $\phi_1,\phi_2,\phi_3$, sum them and add the offset $\phi_0$ (p. 25). The usual activation is the rectified linear unit (p. 25):

$$a[z]=\mathrm{ReLU}[z]=\begin{cases}0 & z<0\\ z & z\ge 0\end{cases}\tag{3.2}$$

Equation 3.1 is a family of functions. Inference means evaluating it for a given $x$. Training means minimizing a least-squares loss $L[\boldsymbol\phi]$ over a dataset $\{x_i,y_i\}_{i=1}^I$ to find $\hat{\boldsymbol\phi}$ (p. 26).

**3.1.1 Intuition.** The family is continuous piecewise linear with up to four linear regions (Fig. 3.2, p. 26). Define the *hidden units* (p. 27):

$$h_1=a[\theta_{10}+\theta_{11}x],\quad h_2=a[\theta_{20}+\theta_{21}x],\quad h_3=a[\theta_{30}+\theta_{31}x]\tag{3.3}$$
$$y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3\tag{3.4}$$

- Each hidden unit holds a line that ReLU clips below zero. The three points where the lines cross zero become the three joints. The clipped lines are weighted by $\phi_1,\phi_2,\phi_3$, and $\phi_0$ sets the overall height (Fig. 3.3, p. 27).
- A clipped unit is *inactive*. An unclipped unit is *active*. Each linear region is a different *activation pattern*. In the shaded region of Fig. 3.3j, $h_1$ and $h_3$ are active and $h_2$ is inactive (p. 27).
- The slope of a region comes from the slopes $\theta_{\bullet1}$ of the active units and the weights $\phi_\bullet$. In the shaded region it is $\theta_{11}\phi_1+\theta_{31}\phi_3$ (p. 27).
- Three hidden units can give four regions. Only three of the four slopes are independent. The fourth is either zero (all units inactive there) or a sum of slopes from the other regions (p. 27).

*Intuition note:* Each hidden unit is a bent line, flat on one side of its joint. Adding bent lines gives a function with a kink at every joint. The slopes and weights set how steep each kink is.

**3.1.2 Depicting networks.** Fig. 3.4a draws the input on the left, hidden units in the middle and the output on the right. Each arrow is one of the ten parameters. Extra nodes holding the number one carry the offsets. Fig. 3.4b omits the intercepts and parameter names (pp. 27, 29). Footnote 1: here "linear" means $z'=\phi_0+\sum_i\phi_iz_i$. Any other function is nonlinear (p. 27).

### 3.2 Universal approximation theorem (pp. 29–30)
With $D$ hidden units (p. 29):
$$h_d=a[\theta_{d0}+\theta_{d1}x]\tag{3.5}$$
$$y=\phi_0+\sum_{d=1}^D\phi_dh_d\tag{3.6}$$

The number of hidden units measures the *network capacity*. With ReLU the output has at most $D$ joints and at most $D+1$ linear regions (p. 29). The author argues that each added hidden unit adds a linear region. Smaller regions are better approximated by a line (Fig. 3.5, p. 30). The theorem states that for any continuous function there exists a shallow network approximating it to any specified precision. This holds for 1D functions on a compact subset of the real line (p. 29), and the figure caption extends it to compact subsets of $\mathbb R^{D_i}$ (p. 30).

*Intuition note:* More joints mean shorter straight pieces. Short enough pieces follow any smooth curve closely.

### 3.3 Multivariate inputs and outputs (pp. 30–33)
The theorem also holds for $\mathbf x=[x_1,\dots,x_{D_i}]^T$ and $\mathbf y=[y_1,\dots,y_{D_o}]^T$ (p. 30).

**3.3.1 Outputs.** Use a different linear function of the hidden units for each output. Example: one input, four hidden units (3.7) and two outputs (p. 31):
$$y_1=\phi_{10}+\phi_{11}h_1+\phi_{12}h_2+\phi_{13}h_3+\phi_{14}h_4$$
$$y_2=\phi_{20}+\phi_{21}h_1+\phi_{22}h_2+\phi_{23}h_3+\phi_{24}h_4\tag{3.8}$$
Both outputs use the same hidden units, so their four joints are in the same places. Slopes and vertical offset can differ (Fig. 3.6, p. 31).

**3.3.2 Inputs.** For two inputs and three hidden units, each unit gets one slope per input (pp. 31, 33):
$$h_d=a[\theta_{d0}+\theta_{d1}x_1+\theta_{d2}x_2],\ d=1,2,3\tag{3.9}$$
$$y=\phi_0+\phi_1h_1+\phi_2h_2+\phi_3h_3\tag{3.10}$$
Each hidden unit's input is an oriented plane. ReLU clips the negative part, and the clipped planes are recombined into a continuous piecewise linear surface of convex polygonal regions (Fig. 3.8, p. 32). Each region has its own activation pattern. In the central triangular region, units 1 and 3 are active and unit 2 is inactive (p. 33). For more than two inputs the regions are convex polytopes (p. 33).

**Number of regions.** Each hidden unit defines a hyperplane separating where it is active from where it is not. With $D_i$ hidden units aligned to the coordinate axes, the space divides into $2^{D_i}$ orthants: four quadrants for two inputs, eight octants for three (Fig. 3.10, p. 34). Shallow networks usually have more hidden units than input dimensions, so they typically create more than $2^{D_i}$ regions (p. 33). Fig. 3.9: with $D=500$ units and $D_i=100$ there can be greater than $10^{107}$ regions, with 51,001 parameters (p. 34).

*Intuition note:* Every hidden unit cuts the input space once with a flat boundary. Many cuts in high dimension can make an enormous number of cells, each with its own linear rule.

### 3.4 General case (pp. 33–35)
For $\mathbf x\in\mathbb R^{D_i}$, $\mathbf y\in\mathbb R^{D_o}$ and $D$ hidden units (pp. 33, 35):
$$h_d=a\Big[\theta_{d0}+\sum_{i=1}^{D_i}\theta_{di}x_i\Big]\tag{3.11}$$
$$y_j=\phi_{j0}+\sum_{d=1}^D\phi_{jd}h_d\tag{3.12}$$
Fig. 3.11 (three inputs, three hidden units, two outputs) has twenty parameters: fifteen slopes and five offsets (p. 35).

The activation must be nonlinear. With no activation, or a linear one, the overall mapping would be linear (p. 35). With ReLU the input space is divided into convex polytopes by the hyperplanes at the joints. Each polytope holds a different linear function. The polytopes are the same for every output, but the linear functions can differ (p. 35).

### 3.5 Terminology (pp. 35–36)
- Layers: input, hidden and output. Hidden units are sometimes called neurons (p. 35).
- Pre-activations are the values entering the hidden layer, before ReLU. Activations are the values after ReLU (p. 35).
- Any network with at least one hidden layer is called a multi-layer perceptron (MLP), "for historical reasons". Networks with one hidden layer are sometimes called shallow; those with several hidden layers are called deep (p. 35).
- Feed-forward: the connections form an acyclic graph. Fully connected: every element of one layer connects to every element of the next (p. 35).
- Connections carry slope parameters, called weights. Offsets are called biases (p. 36).

### 3.6 Summary (p. 36)
A shallow network (i) computes several linear functions of the input, (ii) passes each through an activation, and (iii) linearly combines the activations. It divides the input space into a continuous surface of piecewise linear regions. Chapter 4 adds more hidden layers, and Chapters 5–7 cover training.

### Notes (pp. 36–39)
- **"Neural":** The connection to brains is "tenuous". There is scant evidence that brain computation works like these networks, and the author finds it unhelpful to think about biology going forward (p. 36).
- **History (p. 37):** McCulloch & Pitts (1943) proposed an artificial neuron, without a practical learning algorithm. Rosenblatt (1958) gave the perceptron and a weight-learning algorithm. Minsky & Papert (1969) argued that hidden layers with nonlinear activations could allow more general relations, but concluded that Rosenblatt's algorithm could not learn them. Backpropagation (Chapter 7) arrived in the 1980s.
- **Activations (pp. 37–38):** ReLU has a derivative of one for positive inputs, which contributes to stable and efficient training. Sigmoid derivatives saturate. ReLU's derivative is zero for negative inputs. If all training examples give negative input to a unit, its incoming weights cannot improve (the "dying ReLU" problem). Variants include leaky, parametric and concatenated ReLU, and smooth functions such as softplus, GeLU, SiLU and ELU. Swish is $a[x]=x/(1+\exp[-\beta x])$ with learned $\beta$. HardSwish is a faster approximation:
$$\mathrm{HardSwish}[z]=\begin{cases}0&z<-3\\ z(z+3)/6&-3\le z\le3\\ z&z>3\end{cases}\tag{3.13}$$
There is no definitive answer on which is empirically superior. The book keeps basic ReLU because the functions it creates are easy to characterize by number of linear regions (p. 38).
- **Universal approximation (p. 38):** The "width version" says one hidden layer with finitely many units suffices. Cybenko (1989) proved it for a class of sigmoid activations. Hornik (1991) showed it for a larger class of nonlinear activations.
- **Number of regions (p. 38):** For $D_i\le D$, Zaslavsky (1975) showed that $D$ hyperplanes create at most $\sum_{j=0}^{D_i}\binom{D}{j}$ regions. As a rule of thumb, shallow networks create between $2^{D_i}$ and $2^D$ regions.
- **Linear vs affine (p. 39):** A linear function satisfies $f[a+b]=f[a]+f[b]$, hence $f[2a]=2f[a]$. Adding the bias $\phi_0$ breaks this, so the function is affine. The book still calls both "linear".

## Toy example (ours)
One input, $D=2$ hidden units, ReLU. Parameters: $\phi_0=0.5$, $\phi_1=2$, $\phi_2=-1$; $h_1=a[-1+x]$, $h_2=a[3-x]$. So $y=0.5+2h_1-h_2$.
- Joints: $h_1$ crosses zero at $x=1$ and $h_2$ at $x=3$. That gives $D+1=3$ regions.
- $x<1$: $h_1=0$, $h_2=3-x$, so $y=0.5-(3-x)=x-2.5$. Slope 1 $=\theta_{21}\phi_2=(-1)(-1)$.
- $1\le x<3$: $y=0.5+2(x-1)-(3-x)=3x-4.5$. Slope 3 $=\theta_{11}\phi_1+\theta_{21}\phi_2=2+1$.
- $x\ge3$: $h_2=0$, so $y=0.5+2(x-1)=2x-1.5$. Slope 2.
- Checks: at $x=1$, $-1.5$ and $3-4.5=-1.5$. At $x=3$, $9-4.5=4.5$ and $6-1.5=4.5$. At $x=2$ directly: $h_1=1$, $h_2=1$, $y=0.5+2-1=1.5=3(2)-4.5$.
- The middle slope equals the sum of the other two, $1+2=3$, as in the pattern noted on p. 27.

## Concepts
- [[shallow-neural-network]] (new) — network with one hidden layer: linear functions, activation, linear combination (p. 36)
- [[hidden-unit]] (new) — activation $h_d=a[\theta_{d0}+\sum_i\theta_{di}x_i]$; also called neuron (pp. 27, 35)
- [[relu]] (new) — $a[z]=\max(0,z)$; clips negatives to zero (p. 25)
- [[activation-function]] (new) — nonlinearity applied to each hidden unit; must be nonlinear for non-linear mappings (p. 35)
- [[activation-pattern]] (new) — which hidden units are active or inactive; differs per linear region (p. 27)
- [[linear-region]] (new) — piece of input space where the network is one linear function; a convex polytope in many dimensions (p. 33)
- [[network-capacity]] (new) — the number of hidden units in a shallow network is a measure of its capacity (p. 29)
- [[universal-approximation-theorem]] (new) — enough hidden units approximate any continuous function on a compact set (p. 29)
- [[feed-forward-mlp-block]] — here the whole MLP: at least one hidden layer; the book's term is feed-forward when connections are acyclic (p. 35)

## Canonical instances
- [[ten-parameter-relu-network]] (new) — three-unit scalar network of Eq. 3.1 and Fig. 3.3 (pp. 25–28)
- [[axis-aligned-orthants]] (new) — $D_i$ hyperplanes give $2^{D_i}$ regions (p. 33, Fig. 3.10)
- [[dying-relu]] (new) — if all training examples give a unit negative input, its zero derivative means its incoming weights cannot be improved (p. 38)

## Bridges (candidates)
- [structural-analogy] Hidden-layer ReLU network ↔ llm: the per-token feed-forward block of a Transformer — same layer shape (linear, nonlinearity, linear), but the book here covers only the shallow case.
- [metaphor] "Neurons" and hidden units ↔ neuroscience: the author calls the link "tenuous" (p. 36).
- [same-math] Counting regions cut by $D$ hyperplanes ↔ combinatorial geometry: Zaslavsky's bound (p. 38).

## Questions this raises
- How do deep networks (several hidden layers) change the number and shape of linear regions?
- The theorem says an approximating network exists. How many hidden units are needed, and can training find it (Chapters 5–7)?
- Which activation functions matter in practice, given that ReLU is kept for its easy characterization only?
- Why do a network's joints stay shared across outputs, and what does this constrain?

## Exercises worth doing
- Ex. 3.2 (p. 39) — read off activation patterns of the four regions in Fig. 3.3j — easy
- Ex. 3.3 (p. 39) — derive joint positions and slopes from the ten parameters — medium
- Ex. 3.6 (p. 40) — rescaling a hidden unit by a constant, using ReLU's non-negative homogeneity (3.14) — medium
- Ex. 3.10 (p. 40) — when can three hidden units give fewer than four regions? — medium
- Ex. 3.17 (p. 40) — parameter count in terms of $D_i,D,D_o$ — medium
- Ex. 3.18 (p. 40) — use Zaslavsky's bound to count regions for $D=3$ and $D=5$ — hard

## Reading notes
- Printed page = pdf − 14. Source is a draft ("please send errata") with a CC-BY-NC-ND notice.
- The Fig. 3.9 caption's "10107" is $10^{107}$ (superscript lost in the text layer).
- Page 37 Notes mention Kurenkov (2020), Sejnowski (2018) and Schmidhuber (2022) as histories; I did not use them.
- The chapter's problems (pp. 39–40) are not solved here; only six are listed in the exercises section.
- Fig. 3.13 shows several activations (p. 37). In the Notes, only HardSwish has a numbered equation (3.13); Swish is given inline (p. 38).

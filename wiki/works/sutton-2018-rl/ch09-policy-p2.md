---
id: sutton-2018-rl/ch09-policy-p2
work: sutton-2018-rl
unit: "Chapter 9, part 2/2: §9.5.5 (end) – §9.12, exercises 9.5–9.8, bibliographical remarks"
pages: 222-242
fields: [control-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# On-policy Prediction with Approximation (part 2/2)

## L0 — One line
Beyond hand-set linear SGD, on-policy value prediction can use step-size rules of thumb, neural networks, least-squares TD, stored-example (memory and kernel) methods, and interest/emphasis weighting to focus learning on the states that matter.

## L1 — The gist (≤ 120 words)
This part asks how to go beyond basic linear semi-gradient prediction. It gives a rule of thumb for the step size and presents neural networks as nonlinear approximators, trained by backpropagation with several tricks for deep nets. It then covers least-squares TD (LSTD), which is data-efficient but costs O(d²) per step, and memory-based and kernel methods, which store examples instead of learning weights. Finally it introduces "interest" and "emphasis" for focusing learning on important states, and closes with a chapter summary. This matters because the impressive RL applications use nonlinear approximation, while current theory covers mostly tabular and linear methods.

**Prerequisites:** semi-gradient TD and SGD update (9.7); linear approximation $\hat v=\mathbf w^\top\mathbf x$; TD fixed point $\mathbf A^{-1}\mathbf b$; matrix inverse and outer product; big-O cost.

## L2 — Key ideas
- **RBF networks** (radial basis function networks) are linear approximators with smoothly varying features. The authors say this smoothness has no practical significance in most cases, and graded-response methods like RBFs add computation over tile coding. (p. 222)
- **Step size by rule of thumb:** the classical $1/t$ is unsuitable here. For linear SGD, $\alpha=(\tau\,\mathbb E[\mathbf x^\top\mathbf x])^{-1}$ is a good rule of thumb for learning in about $\tau$ experiences with substantially the same feature vector; it works best if feature-vector length varies little. (pp. 222–223)
- **Neural networks** are widely used nonlinear approximators. Training hidden layers builds features automatically, but deep nets bring overfitting and backward-pass derivatives that decay (slow learning) or grow (instability). Dropout, layer-wise pretraining, batch normalization, residual connections and convolution are techniques presented for training deep nets. (pp. 223–228)
- **LSTD** computes the TD fixed point directly from running estimates of $\mathbf A$ and $\mathbf b$. It is the most data-efficient linear TD(0), but needs O(d²) memory and per-step computation. (pp. 228–230)
- **Memory-based methods** store examples and compute values only at query time. They are nonparametric and local, and avoid exponential memory in the state dimension. (pp. 230–232)
- **Kernel regression** weights stored targets by a similarity kernel. Any linear parametric method can be recast as kernel regression with $k(s,s')=\mathbf x(s)^\top\mathbf x(s')$. (pp. 232–233)
- **Interest and emphasis** generalise the on-policy distribution so that limited approximation resources can be used in a more targeted way, on states we care about. (pp. 234–235)

## L3 — Walkthrough

### 9.5.5 Radial basis functions (end of section) (pp. 222)
- RBFs' main advantage over binary features is that the approximate functions vary smoothly and are differentiable. The authors say this has no practical significance in most cases. (p. 222)
- Graded-response methods in tile coding need substantial extra computation and often lose performance beyond two state dimensions. In high dimensions tile edges matter more, and well-controlled graded activations near edges are hard to get. (p. 222)
- An **RBF network** is a linear approximator with RBF features, learned by (9.7)–(9.8). Some methods also adapt centers and widths, which makes it nonlinear. That may fit targets more precisely, but costs more computation and manual tuning. (p. 222)

### 9.6 Selecting step-size parameters manually (pp. 222–223)
- Theory helps little. The stochastic-approximation conditions (2.7) are sufficient to guarantee convergence but tend to give learning that is too slow. $\alpha_t=1/t$ is not appropriate for TD, nonstationary problems, or any function-approximation method. (p. 222)
- Recursive least-squares methods set an optimal *matrix* step size, and LSTD is one such extension. They need $O(d^2)$ step-size parameters, $d$ times more than the parameters learned, so they are ruled out for large problems. (p. 222)
- Tabular intuition: $\alpha=1$ removes the sample error after one target. If $\alpha=1/\tau$, the estimate approaches the mean of its targets after about $\tau$ experiences, with recent targets weighted most. (p. 222)
- With general approximation, "number of experiences with a state" is unclear. For linear SGD the authors give this rule of thumb, for learning in about $\tau$ experiences with substantially the same feature vector: (p. 223)

$$\alpha \doteq \left(\tau\,\mathbb E\!\left[\mathbf x^\top\mathbf x\right]\right)^{-1}\tag{9.19}$$

 Here $\mathbf x$ is drawn from the distribution of SGD inputs. It works best if feature vectors do not vary much in length, ideally $\mathbf x^\top\mathbf x$ constant. (p. 223)

**Intuition note.** $\mathbf x^\top\mathbf x$ is the squared length of the feature vector, and it scales how much one update changes the estimate. Dividing by it turns "$1/\tau$" from the tabular case into a per-feature-vector step size.

- Exercises 9.5 (tile-coding step size) and 9.6 (error reduced to zero in one update when $\tau=1$) follow here. (p. 223)

### 9.7 Nonlinear approximation: artificial neural networks (pp. 223–228)
**Structure.**
- An ANN is a network of interconnected neuron-like units. A **feedforward** ANN has no loops. Figure 9.14 shows 4 input units, two hidden layers (neither input nor output) and 2 output units, with a real-valued weight on each link. A network with at least one loop is **recurrent**. Only the feedforward case is treated. (pp. 223–224)
- Units are typically *semi-linear*: a weighted sum of inputs passed through a nonlinear **activation function**. Typical choices are sigmoid functions such as the logistic $f(x)=1/(1+e^{-x})$, sometimes the rectifier $f(x)=\max(0,x)$. A step function ($1$ if $x\ge\theta$, else $0$) gives a binary threshold unit. Input units have externally set activations. (p. 224)
- Each output is a nonlinear function of the input activations, parameterised by the weights. An ANN with no hidden layers can represent only a very small fraction of input–output functions. (p. 224)
- With one hidden layer of enough sigmoid units, any continuous function on a compact input region can be approximated to any accuracy (Cybenko, 1989). This also holds for other activations satisfying mild conditions. Nonlinearity is essential: if all units are linear, the whole network equals one with no hidden layers. (p. 224)
- Despite this, complex AI functions are made easier, and indeed may require, hierarchical compositions of many layers. Successive layers of a deep ANN compute increasingly abstract representations. (pp. 224–225)

**Training.**
- Training hidden layers creates features automatically, without relying only on hand-crafted ones. ANNs usually learn by a stochastic gradient method. The objective is expected loss over labelled examples (supervised case), or TD errors for value learning, or expected reward as in gradient bandits or policy gradients. (p. 225)
- All of these need the partial derivative of the objective with respect to each weight. The gradient is the vector of these. (p. 225)
- **Backpropagation** (for differentiable activations) alternates a forward pass, which computes unit activations, with a backward pass, which efficiently computes a partial derivative for each weight. As in other stochastic methods, the vector is an *estimate* of the gradient. (p. 225)
- It works well for shallow nets (1–2 hidden layers) but may not for deeper ones. Training $k+1$ hidden layers can do worse than $k$, though the deeper net can represent everything the shallower one can. (p. 225)
- Two of several important factors: first, many weights make overfitting hard to avoid. Second, backward-pass derivatives either decay rapidly toward the input side, making deep-layer learning very slow, or grow rapidly, making it unstable. (p. 225)

**Remedies.** (pp. 226–228)
- *Overfitting* means failing to generalise to unseen cases. It is less of a problem for online RL without limited training sets, but generalising effectively still matters. Remedies: cross validation (stop when validation performance drops), regularization (penalise complexity), and weight sharing. (p. 226)
- *Dropout* (Srivastava et al., 2014) randomly removes units during training, like training many "thinned" networks. At test time it approximates their combination by multiplying each outgoing weight by the probability that the unit was retained. It encourages hidden units to learn features that work with random collections of other features. (p. 226)
- *Deep belief networks* (Hinton, Osindero, Teh, 2006): the deepest layers are trained one at a time by unsupervised learning, then the network is fine-tuned by backpropagation. This generally works much better than random initial weights. One idea is that it starts the network in a region of weight space where gradient methods make good progress. (p. 226)
- *Batch normalization* (Ioffe, Szegedy, 2015) normalises the outputs of deep layers using statistics from mini-batches, which improves the learning rate. (p. 226)
- *Deep residual learning* (He et al., 2016): a block learns a residual function (its difference from the identity) when skip connections add the block's input to its output. This needs no extra weights. It gave substantial improvements on image-classification benchmarks, and with batch normalization was used in the Go application of Chapter 16. (p. 227)
- *Deep convolutional networks* suit data in spatial arrays such as images, and were inspired by early visual processing in the brain. Because of their architecture they can be trained by backpropagation without the methods above. (p. 227)
 - A *feature map* is a pattern of activity over units that all do the same operation on their **receptive field**. The fields are the same size and are shifted across the input. Units in a map share weights, so the map detects its feature wherever it appears. (p. 227)
 - Figure 9.15 (LeCun et al., 1998, handwritten characters): alternating convolutional and subsampling layers, then fully connected layers. The first convolutional layer has 6 maps of $28\times28$ units with $5\times5$ overlapping fields (overlap four rows and columns), so each map has just 25 adjustable weights. (pp. 227–228)
 - *Subsampling* layers average over receptive fields. In the first one, each unit averages a non-overlapping $2\times2$ field, giving six $14\times14$ maps. This makes responses spatially invariant, which helps because a feature useful in one place is likely useful elsewhere. (p. 228)
- Current RL theory is mostly limited to tabular and linear methods, but notable applications owe much to multi-layer ANNs (Chapter 16). (p. 228)

**Intuition note.** A hidden layer lets the network invent its own features instead of using hand-made ones. The price is a harder training problem: many weights and gradients that shrink or blow up across layers.

### 9.8 Least-squares TD (pp. 228–230)
- Methods so far cost computation per step proportional to the number of parameters. LSTD is, arguably, the best that can be done for linear approximation with more computation. (p. 228)
- Linear TD(0) converges asymptotically (with suitably decreasing step sizes) to the TD fixed point (Section 9.4): (p. 228)

$$\mathbf w_{TD}=\mathbf A^{-1}\mathbf b,\qquad \mathbf A\doteq\mathbb E\!\left[\mathbf x_t(\mathbf x_t-\gamma\mathbf x_{t+1})^\top\right],\quad \mathbf b\doteq\mathbb E[R_{t+1}\mathbf x_t].$$

- Iterating is wasteful of data. LSTD instead forms the natural estimates ($\mathbf x$, $\mathbf b$: $d$-vectors; $\mathbf A$: $d\times d$): (p. 228)

$$\widehat{\mathbf A}_t\doteq\sum_{k=0}^{t-1}\mathbf x_k(\mathbf x_k-\gamma\mathbf x_{k+1})^\top+\varepsilon\mathbf I,\qquad \widehat{\mathbf b}_t\doteq\sum_{k=0}^{t-1}R_{k+1}\mathbf x_k,\tag{9.20}$$

 where $\varepsilon\mathbf I$, for some small $\varepsilon>0$, makes $\widehat{\mathbf A}_t$ always invertible. (p. 229)
- These estimate $t$ times $\mathbf A$ and $t$ times $\mathbf b$. The factors of $t$ cancel in the estimate of the fixed point: (p. 229)

$$\mathbf w_t\doteq\widehat{\mathbf A}_t^{-1}\widehat{\mathbf b}_t.\tag{9.21}$$

- This is the most data-efficient form of linear TD(0) but costs more. Semi-gradient TD(0) needs only $O(d)$ memory and per-step computation. (p. 229)
- Cost: the sums in (9.20) can be updated incrementally in constant time per step, but the $\widehat{\mathbf A}_t$ update is an outer product, so $O(d^2)$ time and memory. A general inverse is $O(d^3)$. Because $\widehat{\mathbf A}_t$ is a sum of outer products, its inverse can be updated in $O(d^2)$ by the Sherman–Morrison formula (for $t>0$, $\widehat{\mathbf A}_0\doteq\varepsilon\mathbf I$): (p. 229)

$$\widehat{\mathbf A}_t^{-1}=\left(\widehat{\mathbf A}_{t-1}+\mathbf x_{t-1}(\mathbf x_{t-1}-\gamma\mathbf x_t)^\top\right)^{-1}=\widehat{\mathbf A}_{t-1}^{-1}-\frac{\widehat{\mathbf A}_{t-1}^{-1}\mathbf x_{t-1}(\mathbf x_{t-1}-\gamma\mathbf x_t)^\top\widehat{\mathbf A}_{t-1}^{-1}}{1+(\mathbf x_{t-1}-\gamma\mathbf x_t)^\top\widehat{\mathbf A}_{t-1}^{-1}\mathbf x_{t-1}}\tag{9.22}$$

 It uses only vector–matrix and vector–vector products, so storing and maintaining $\widehat{\mathbf A}_t^{-1}$ and applying (9.21) costs $O(d^2)$ memory and per-step computation. (p. 229)
- **Algorithm box (p. 230).** Input: features with $\mathbf x(terminal)=\mathbf 0$; small $\varepsilon>0$. Initialise $\widehat{\mathbf A^{-1}}\leftarrow\varepsilon^{-1}\mathbf I$, $\widehat{\mathbf b}\leftarrow\mathbf 0$. Each step, after taking $A\sim\pi(\cdot|S)$ and observing $R,S'$, $\mathbf x'\leftarrow\mathbf x(S')$:
 - $\mathbf v\leftarrow\widehat{\mathbf A^{-1}}^{\!\top}(\mathbf x-\gamma\mathbf x')$
 - $\widehat{\mathbf A^{-1}}\leftarrow\widehat{\mathbf A^{-1}}-(\widehat{\mathbf A^{-1}}\mathbf x)\mathbf v^\top/(1+\mathbf v^\top\mathbf x)$
 - $\widehat{\mathbf b}\leftarrow\widehat{\mathbf b}+R\mathbf x$
 - $\mathbf w\leftarrow\widehat{\mathbf A^{-1}}\widehat{\mathbf b}$
 - $S\leftarrow S'$, $\mathbf x\leftarrow\mathbf x'$
- Is it worth it? That depends on $d$, how important fast learning is, and the cost of other system parts. The "no step size" advantage is probably overstated. LSTD needs $\varepsilon$: too small and the inverses can vary wildly, too large and learning slows. (p. 229)
- Having no step size also means LSTD never forgets. That is problematic if the target policy changes, as in GPI. Control applications then typically need another forgetting mechanism, mooting the initial advantage. (p. 229)

**Intuition note.** Semi-gradient TD takes many small steps toward the TD fixed point. LSTD keeps running sums and solves for the fixed point directly, using the data more fully at the price of a $d\times d$ matrix.

### 9.9 Memory-based function approximation (pp. 230–232)
- *Parametric* methods adjust parameters of a fixed functional form, and training examples can be discarded after each update. (p. 230)
- *Memory-based* methods save examples (or a subset) without updating parameters. When a **query state**'s value is needed, retrieved examples are used to compute it. This is *lazy learning*. They are *nonparametric*: the function's form is set by the examples and how they are combined, not by a fixed class. More data is expected to give increasingly accurate approximations of any target function. (p. 230)
- The text focuses on **local-learning** methods. They retrieve examples whose states are most relevant to the query state (usually by distance), then discard the local approximation. (p. 231)
 - *Nearest neighbor* returns the target $g$ of the closest stored example $s'\mapsto g$. (p. 231)
 - *Weighted average* returns a weighted average of several nearest targets, with weights generally falling with distance. (p. 231)
 - *Locally weighted regression* fits a surface to nearby states by a parametric method minimising a distance-weighted error like (9.1), evaluates it at the query state, and discards it. (p. 231)
- Advantages: approximation is not limited to pre-specified forms, so accuracy can improve with data. Methods can focus on neighborhoods visited along real or simulated trajectories (Section 8.6), and experience affects nearby estimates immediately. (p. 231)
- *Curse of dimensionality:* for $k$ state dimensions a global tabular method needs memory exponential in $k$. Memory-based storage needs memory proportional to $k$ per example and linear in the number $n$ of examples. The remaining issue is query speed, which degrades as memory grows. (p. 231)
- Speed-ups: parallel or special hardware, and **k-d trees**, which recursively split $k$-dimensional space into binary-tree regions. Depending on the data, they can quickly eliminate large regions. Locally weighted regression also needs fast local computations, and methods for forgetting entries to bound database size. (p. 232)

### 9.10 Kernel-based function approximation (pp. 232–233)
- The weight-assigning function is a **kernel** $k$. It may take distances, $k:\mathbb R\to\mathbb R$, or more generally $k:\mathcal S\times\mathcal S\to\mathbb R$, where $k(s,s')$ is the weight of data about $s'$ when answering queries about $s$. It measures strength of generalization from $s'$ to $s$. (p. 232)
- Tile coding uses no kernel explicitly but generalises according to one. The strength of generalization from linear parametric approximation can always be described by a kernel. (p. 232)
- **Kernel regression** averages all stored targets with kernel weights. With $\mathcal D$ the stored examples and $g(s')$ the target: (p. 232)

$$\hat v(s,\mathcal D)=\sum_{s'\in\mathcal D}k(s,s')\,g(s')\tag{9.23}$$

 The weighted-average method is the special case where $k(s,s')$ is non-zero only for nearby $s,s'$. (p. 233)
- Kernel regression with a Gaussian RBF kernel differs from the RBF-network method in two ways. It is memory-based (RBFs centred on stored states) and nonparametric (no parameters to learn). (p. 233)
- Any linear parametric method with features $\mathbf x(s)=(x_1(s),\dots,x_d(s))^\top$ can be recast as kernel regression with (justification skipped; see Bishop, 2006): (p. 233)

$$k(s,s')=\mathbf x(s)^\top\mathbf x(s').\tag{9.24}$$

 This gives the same approximation as the linear method with the same data. (p. 233)
- So one can build kernels directly, without feature vectors. Not all kernels are inner products of feature vectors. For many feature sets, (9.24) has a compact form computable without working in the $d$-dimensional space. This is the **"kernel trick"**: effectively working in a high-dimensional feature space while using only the stored examples. (p. 233)

**Intuition note.** A kernel is a similarity score. Storing examples and weighting them by similarity can mimic a huge feature space without ever building it.

### 9.11 Interest and emphasis (pp. 234–235)
- So far all encountered states were treated equally, which gives stronger theoretical results for semi-gradient methods (on-policy distribution). But we may care more about some states, for example early states in discounted episodic problems, or good actions over poor ones when learning action values. Limited approximation resources could be used in a more targeted way. (p. 234)
- The on-policy distribution is generalised: there are many such distributions, all of states met while following the target policy, differing in how trajectories are initiated. (p. 234)
- **Interest** $I_t\ge0$ is a random variable giving how much we care about accurately valuing the state (or state–action pair) at time $t$. Zero means no care; one means full care, though any non-negative value is allowed. It can be set in any causal way. The distribution $\mu$ in VE (9.1) becomes the target-policy state distribution weighted by interest. (p. 234)
- **Emphasis** $M_t\ge0$ multiplies the update at time $t$. The general $n$-step rule, replacing (9.15), uses the return (9.16): (p. 234)

$$\mathbf w_{t+n}\doteq\mathbf w_{t+n-1}+\alpha M_t\left[G_{t:t+n}-\hat v(S_t,\mathbf w_{t+n-1})\right]\nabla\hat v(S_t,\mathbf w_{t+n-1}),\quad 0\le t<T\tag{9.25}$$

$$M_t=I_t+\gamma^nM_{t-n},\quad 0\le t<T,\qquad M_t\doteq0\ \text{for } t<0\tag{9.26}$$

 This includes Monte Carlo: $G_{t:t+n}=G_t$, updates at episode end, $n=T-t$, $M_t=I_t$. (p. 234)
- **Example 9.4.** A four-state chain with reward $+1$ per step, true values $4,3,2,1$. States 1–2 share weight $w_1$ and states 3–4 share $w_2$. Interest is 1 in the leftmost state and 0 elsewhere. (p. 235)
 - Gradient MC without interest/emphasis converges to $\mathbf w_\infty=(3.5,1.5)$. The first state gets 3.5, between the true values of states 1 and 2. With interest and emphasis, $w_1\to4$ and $w_2$ is never updated, since emphasis is zero except at the leftmost state. (p. 235)
 - Two-step semi-gradient TD: without interest/emphasis $\mathbf w_\infty=(3.5,1.5)$. With them, $\mathbf w_\infty=(4,2)$, exact for the first state and for the third (which the first bootstraps from). The second and fourth states are never updated. (p. 235)
 - (added step) With $n=2$, $\gamma=1$: $M_0=1$, $M_1=0$, $M_2=0+M_0=1$, $M_3=0+M_1=0$. So only updates at $t=0$ and $t=2$ are non-zero, matching the text.

**Intuition note.** Emphasis passes "I care about this state" forward to the later states it bootstraps from. Effort goes to the states the valuation actually depends on, not to the rest.

### 9.12 Summary (p. 236)
- RL needs generalization. Supervised function-approximation methods apply by treating each update as a training example. Parametrised approximation is perhaps the most suitable, and $\overline{VE}(\mathbf w)$ ranks approximations under the on-policy distribution $\mu$. (p. 236)
- SGD variants are the most popular. $n$-step semi-gradient TD covers gradient Monte Carlo and semi-gradient TD(0) as special cases. Semi-gradient methods are not true gradient methods, because the weights in the target are ignored in the gradient, so classical SGD results do not apply. (p. 236)
- Linear approximation is best understood theoretically and works well with appropriate features. Choosing features is one of the most important ways of adding prior domain knowledge. Polynomials generalise poorly online. Better choices are Fourier bases and coarse coding. Tile coding is computationally efficient and flexible. RBFs suit one- or two-dimensional tasks needing smooth response. LSTD is the most data-efficient linear TD but costs $O(d^2)$, the others $O(d)$. Nonlinear methods include ANNs trained by backpropagation and SGD variants, which have become very popular under the name deep reinforcement learning. (p. 236)
- Linear semi-gradient $n$-step TD is guaranteed to converge under standard conditions, for all $n$, to a VE within a bound of the optimal error (asymptotically achieved by Monte Carlo). The bound is always tighter for higher $n$ and approaches zero as $n\to\infty$. Very high $n$ learns very slowly in practice, so some bootstrapping is usually preferable. (p. 236)
- Exercises 9.7 (logistic unit learning rule from (9.7) with no gradient notation) and 9.8 (the same with cross-entropy loss, compared in complexity). (p. 237)

### Bibliographical and historical remarks (pp. 237–242, compressed)
- LMS (Widrow & Hoff, 1960) is the prototype incremental gradient method. Semi-gradient TD(0) was first explored by Sutton (1984, 1988), and the term "semi-gradient" is new to this edition. (p. 237)
- Sutton (1988) proved convergence of linear TD(0) in the mean for linearly independent features. Several others proved convergence with probability 1. Dayan (1992) first treated general dependent features. Tsitsiklis and Van Roy (1997) proved the asymptotic-error bound. (pp. 237–238)
- Fourier basis: Konidaris et al. (2011). Coarse coding: Hinton (1984). Tile coding: Albus (1971, 1981), CMAC. RBFs: related to ANNs by Broomhead & Lowe (1988). (p. 238)
- Automatic step-size methods include RMSprop, Adam and Delta-Bar-Delta. (p. 238)
- ANN history runs through threshold units, the Perceptron/ADALINE, backpropagation, and deep learning. Early RL uses include Farley & Clark (1954), Barto et al. (1983, actor–critic pole balancing), and Tesauro's TD-Gammon. AlphaGo and successors used deep convolutional ANNs. (pp. 238–240)
- LSTD is due to Bradtke and Barto. The inverse-update identity has been known at least since 1949 (Sherman & Morrison). (p. 240)
- Memory-based discussion follows Atkeson, Moore, Schaal (1997). k-d trees were introduced by Bentley (1975). (p. 240)
- Kernel regression originates in the method of potential functions of Aizerman et al. (1964), which likened data to point charges. (p. 240)
- Emphatic-TD references are in the notes to Section 11.8. (p. 241)
- Samuel's checkers player (1959, 1967) is the earliest example the authors know of in which function approximation was used for learning value functions, following Shannon's suggestion. Holland's classifier system is discussed as a state-aggregation approach whose classifiers are learned by an evolutionary method. The authors contrast it with their choice of gradient and ANN methods. (pp. 241–242)

## Toy example (ours, not from the text)
LSTD with $d=1$, to check (9.20)–(9.22) by hand. One nonterminal state $S$ with feature $x(S)=1$, terminal $x=0$, $\gamma=1$, $\varepsilon=0.1$. Every episode is $S\to$ terminal with reward $R=1$. Then $x=1$, $x'=0$.

- Start: $\widehat A^{-1}=\varepsilon^{-1}=10$, $\hat b=0$.
- Step 1: $v=10\cdot(1-0)=10$. $\widehat A^{-1}=10-(10\cdot1)\cdot10/(1+10\cdot1)=10-100/11=0.909$. $\hat b=0+1\cdot1=1$. $w=0.909\cdot1=0.909$.
- Direct check from (9.20): $\widehat A_1=1\cdot(1-0)+0.1=1.1$, and $1/1.1=0.909$ ✓. $w_1=\hat b/\widehat A=1/1.1=0.909$ ✓.
- Step 2: $v=0.909$. $\widehat A^{-1}=0.909-(0.909\cdot0.909)/(1+0.909)=0.909-0.826/1.909=0.909-0.433=0.476$. $\hat b=2$. $w=0.476\cdot2=0.952$. Direct: $\widehat A_2=2.1$, $2/2.1=0.952$ ✓.
- As $t$ grows, $w_t=t/(t+0.1)\to1$, the true value $v_\pi(S)=1$. The $\varepsilon$ term biases early estimates downward, which shows why $\varepsilon$ matters.

## Concepts
- [[step-size-parameter]] (new) — SGD's $\alpha$; in the tabular case $\alpha=1/\tau$ means about $\tau$ experiences to approach the mean (p. 222)
- [[linear-sgd-step-size-rule]] (new) — $\alpha=(\tau\mathbb E[\mathbf x^\top\mathbf x])^{-1}$ as a rule of thumb (p. 223)
- [[rbf-network]] (new) — linear approximator whose features are radial basis functions (p. 222)
- [[feedforward-ann]] (new) — loop-free network of weighted units with activation functions (p. 223)
- [[activation-function]] (new) — nonlinear function applied to a unit's weighted sum (p. 224)
- [[backpropagation]] (new) — forward and backward passes giving a gradient estimate per weight (p. 225)
- [[overfitting]] (new) — failing to generalise to unseen cases; remedies include dropout, regularization, weight sharing (pp. 225–226)
- [[convolutional-network]] (new) — weight-sharing feature maps over receptive fields, plus subsampling (p. 227)
- [[lstd]] (new) — directly solves $\widehat{\mathbf A}_t^{-1}\widehat{\mathbf b}_t$; $O(d^2)$ (p. 228)
- [[sherman-morrison-update]] (new) — incremental inverse update (9.22) for a sum of outer products (p. 229)
- [[memory-based-approximation]] (new) — store examples; compute value locally at query time (p. 230)
- [[nonparametric-method]] (new) — function form set by the data, not a fixed class (p. 230)
- [[kernel-function]] (new) — weight $k(s,s')$ giving how strongly data at $s'$ informs $s$ (p. 232)
- [[kernel-trick]] (new) — evaluate $\mathbf x(s)^\top\mathbf x(s')$ compactly without computing in feature space (p. 233)
- [[interest-and-emphasis]] (new) — non-negative weights $I_t$, $M_t$ focusing on-policy learning on chosen states (p. 234)
- [[temporal-difference-learning]] — here, $n$-step semi-gradient TD with function approximation (p. 236)

## Canonical instances
- [[four-state-interest-emphasis]] — Example 9.4: interest/emphasis give exact value of the one state we care about (p. 235)
- [[lecun-digit-convnet]] — Figure 9.15 network for handwritten characters (pp. 227–228)
- [[tile-coding-98-tilings]] — Exercise 9.5 setup, 98 tilings in 7 dimensions (p. 223)

## Bridges (candidates)
- [structural-analogy] LSTD / Sherman–Morrison update ↔ control theory: recursive least squares and covariance-style updates — both maintain a matrix inverse recursively as data arrive.
- [structural-analogy] $\alpha=1/\tau$ averaging ↔ control theory: first-order low-pass filter time constant — both are exponential moving averages that forget over about $\tau$ samples.
- [metaphor] Interest/emphasis ↔ control theory: minimal intervention principle — resources go to deviations that matter for the task.
- [metaphor] "Never forgets" in LSTD ↔ control theory: integral action accumulating past error — both accumulate history, with no built-in forgetting.

## Questions this raises
- When does LSTD's $O(d^2)$ cost pay off, and what forgetting mechanism fits changing policies in control?
- Why do deep-layer gradients decay or explode, and which of the listed remedies attacks which cause?
- Which kernels are inner products of feature vectors, and which are not?
- How should interest $I_t$ be chosen in practice, given that it may depend on the trajectory or learned parameters?

## Exercises worth doing
- Ex. 9.5 (p. 223) — apply (9.19) to a tile-coded 98-tiling feature vector with $\tau=10$ — difficulty: easy
- Ex. 9.6 (p. 223) — prove that (9.19) with $\tau=1$ and $\mathbf x(S_t)^\top\mathbf x(S_t)=\mathbb E[\mathbf x^\top\mathbf x]$, together with (9.7), reduces the error to zero in one update — difficulty: medium
- Ex. 9.7 (p. 237) — derive the learning rule for a single logistic unit from (9.7), with no gradient notation — difficulty: medium
- Ex. 9.8 (p. 237) — repeat the derivation with cross-entropy loss and compare complexity — difficulty: hard

## Reading notes
- This unit is the second half of Chapter 9. It starts mid-section 9.5.5 (the RBF discussion, top of p. 222) and ends with the end of the chapter's Bibliographical and Historical Remarks (p. 242). The source note says the split is at a section boundary, but the pages given begin mid-section. Printed = pdf − 22.
- The text layer garbles symbols (γ, ε, ∞, ≥, hats); equations here were checked against the page images.
- On p. 236 the Summary lists gradient Monte Carlo and semi-gradient TD(0) as special cases of $n$-step semi-gradient TD "respectively". The text layer shows "n = 1 and n = 1", so the ∞ symbol is garbled and I cannot confirm from the text layer which value goes with which method. Section 9.11 (p. 234) sets $n=T-t$ for the Monte Carlo case.
- The Summary on p. 236 says "the policy is parameterized by a weight vector w", though the context is value-function approximation. I have not reproduced this sentence.
- Example 9.4 refers to equations (9.7), (9.15), (9.16) and boxes on pages 202 and 209, which are outside this unit.

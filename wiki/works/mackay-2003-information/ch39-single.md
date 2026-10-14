---
id: mackay-2003-information/ch39-single
work: mackay-2003-information
unit: "38 Introduction to Neural Networks (pp. 468–470) and 39 The Single Neuron as a Classifier (pp. 471–482)"
pages: 468–482
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
# The Single Neuron as a Classifier (with Ch. 38 introduction)

## L0 — One line
A single sigmoid neuron, whose output can be viewed as a class probability, can be trained by gradient descent on an error function built from information contents (relative entropy), optionally with weight decay, to give a simple supervised classifier.

## L1 — The gist (≤ 120 words)
Chapter 38 motivates neural networks by contrasting address-based computer memory with associative, error-tolerant, parallel and (to a degree) distributed biological memory. It also defines architecture, activity rule and learning rule. Chapter 39 studies one neuron: it weights its inputs, sums them into an activation, and passes this through a function such as the logistic sigmoid. For binary labels, the error function is a sum of information contents, and its gradient is the error times the input. On-line and batch gradient descent follow. On separable data the weights grow without bound (overfitting), so a weight-decay penalty is added. The exercises link the neuron to Bayesian posteriors.

**Prerequisites:** vectors and dot products; logarithms and exponentials; partial derivatives and gradients; probability of a binary outcome; relative entropy; Gaussian densities (for the exercises).

## L2 — Key ideas (5–10 bullets)
- Address-based digital memory is not associative, not fault-tolerant and not distributed; biological memory is described as associative, error-tolerant, and parallel and distributed (though not completely distributed), which motivates artificial neural networks (pp. 468–469).
- A neural-network algorithm is described by its architecture, activity rule and learning rule. Algorithms are supervised (inputs plus targets) or unsupervised (inputs only) (p. 470).
- A neuron computes the activation $a=\sum_i w_i x_i$, then an output $y=f(a)$, e.g. the logistic sigmoid (pp. 471–472).
- The linear logistic function already appeared as a posterior probability in section 11.2 (Gaussian channel, pulse detection). Its output can be read as the probability of class 1 (pp. 472, 475).
- Each weight vector $\mathbf w$ is a point in weight space and defines a function of $\mathbf x$. Training means searching weight space to minimize an error function (p. 473).
- For binary targets, $G(\mathbf w)$ is a sum of information contents, and its gradient is $-\sum_n (t^{(n)}-y^{(n)})x^{(n)}_j$. This gives on-line (stochastic) and batch gradient descent (pp. 475–476).
- If the data are linearly separable, the weights diverge, which is an example of overfitting. Regularization, in its simplest form weight decay $M=G+\alpha E_W$, is the more principled fix. Early stopping is an ad hoc one (p. 479).

## L3 — Walkthrough

### Chapter 38: Introduction to Neural Networks
- **Three motivations** (p. 468): biology (how brains compute and remember), engineering (machines that learn or find patterns), and complex systems (adaptive systems interesting in themselves).
- **Caveats** (p. 468): the book gives only a taste of the field. The models are not meant as faithful models of biology; any relevance is abstract. The book does not give the full state of the art.

**38.1 Memories** (pp. 468–470)
- In a digital computer a memory is stored at an address, and the address has nothing to do with the memory's content (p. 468).
- The author lists three properties that address-based memory lacks (pp. 468–469):
  1. *Not associative.* You cannot recall the rest of a memory from half of it without the address. Content-addressability has to be added on with software.
  2. *Not robust.* A one-bit error in the address retrieves a different memory. Error-correcting codes exist in modern memories, but the error tolerance is not intrinsic. Minor damage to certain hardware that implements memory retrieval is likely to lose all functionality.
  3. *Not distributed.* Only a tiny fraction of devices take part in a recall. Present-day parallel computers scarcely differ in this respect.
- Biological memory is the opposite (p. 469):
  1. It is associative: given a name we can often recall the face, and vice versa.
  2. It is error-tolerant. The example is the cue "An American politician who was very intelligent and whose politician father did not like broccoli". The author says many people think of president Bush despite the erroneous cue. Many memories persist unaffected while cells change or are damaged.
  3. It is parallel and distributed, though not completely, since some functional specialization appears to exist. Many neurons seem to participate in storing multiple memories.
- These properties motivate artificial neural networks: parallel distributed systems of many interacting simple elements. The hope is that they give hints about real neural computation (pp. 469–470).

**38.2 Terminology** (p. 470)
- **Architecture:** the variables (e.g. weights and neuron activities) and their topological relationships.
- **Activity rule:** short-time-scale local dynamics of neuron activities. It typically depends on the weights.
- **Learning rule:** how the weights change, on a longer time scale. It usually depends on the activities. It may also depend on teacher-supplied targets and on the current weights.
- The rules are often invented by researchers. Alternatively they may be derived from carefully chosen objective functions.
- *Supervised* networks get inputs and targets. *Unsupervised* networks get only examples $\{x\}$. They may memorize them, generalize, find patterns or extract features. Some can fill in missing variables, so they can also be viewed as supervised.

### Chapter 39: The Single Neuron as a Classifier

**39.1 The single neuron** (pp. 471–472)
- Two reasons to study it: many networks are built from single neurons, and one neuron can itself learn. Various standard statistical methods can be viewed as single neurons (p. 471).
- **Architecture:** $I$ inputs $x_i$, one output $y$, weights $w_i$ ($i=1,\dots,I$). An optional bias $w_0$ is the weight of an input $x_0$ fixed at 1. The neuron is feedforward: connections run from inputs to output (p. 471).
- **Activity rule**, step 1: the *activation* (a weighted sum of inputs)
$$a=\sum_i w_i x_i \tag{39.1}$$
with $i=0,\dots,I$ if there is a bias and $i=1,\dots,I$ otherwise (p. 471).
- Step 2: the output (also called the *activity*, not to be confused with the activation) is $y=f(a)$ (p. 471).
- Deterministic choices (pp. 471–472):
$$y(a)=a \tag{39.2}$$
$$y(a)=\frac{1}{1+e^{-a}}\quad (y\in(0,1)) \tag{39.3}$$
$$y(a)=\tanh(a)\quad (y\in(-1,1)) \tag{39.4}$$
$$y(a)=\Theta(a)\equiv\begin{cases}1 & a>0\\ -1 & a\le 0\end{cases} \tag{39.5}$$
- Stochastic choices: $y$ is chosen at random from $\pm1$ (p. 472).
  - *Heat bath:* $y=1$ with probability $1/(1+e^{-a})$, otherwise $y=-1$ (39.6).
  - *Metropolis rule* (depends on the previous output $y$): compute $\Delta=ay$. If $\Delta\le0$, flip $y$. Otherwise flip $y$ with probability $e^{-\Delta}$.

**39.2 Basic neural network concepts** (pp. 472–473)
- A network implements a function $y(\mathbf x;\mathbf w)$ of inputs $\mathbf x$, parameterized by weights $\mathbf w$. The neuron studied is
$$y(\mathbf x;\mathbf w)=\frac{1}{1+e^{-\mathbf w\cdot\mathbf x}}. \tag{39.7}$$
- *Motivation from section 11.2* (p. 472): one of two signals $\mathbf x_0,\mathbf x_1$ is sent over a Gaussian channel with variance–covariance matrix $\mathbf A^{-1}$. The probability that the source was $s=1$ given the received $\mathbf y$ is
$$P(s=1\,|\,\mathbf y)=\frac{1}{1+\exp(-a(\mathbf y))} \tag{39.8}$$
with $a(\mathbf y)$ linear in the received vector:
$$a(\mathbf y)=\mathbf w^{\mathsf T}\mathbf y+\theta,\quad \mathbf w\equiv\mathbf A(\mathbf x_1-\mathbf x_0). \tag{39.9}$$
The author says the linear logistic function can be motivated in several other ways, via the exercises.
- *Input space and weight space* (p. 473). Take $\mathbf x=(x_1,x_2)$ and $\mathbf w=(w_1,w_2)$:
$$y(\mathbf x;\mathbf w)=\frac{1}{1+e^{-(w_1x_1+w_2x_2)}}. \tag{39.10}$$
For $\mathbf w=(0,2)$ (fig. 39.2), the output is constant on any line perpendicular to $\mathbf w$. Along the direction of $\mathbf w$ it is a sigmoid.
- *Weight space* is the parameter space of the network. Each point in it corresponds to a function of $\mathbf x$ (fig. 39.3). The gain (the slope of the ramp) increases as $|\mathbf w|$ increases.
- *Supervised learning idea* (p. 473): given examples of the relation between input $\mathbf x$ and target $t$, we hope the network learns a model of it. Training means searching weight space for a $\mathbf w$ that fits the training data well.
- An *objective (error) function* of $\mathbf w$ is a sum of terms, one per input/target pair. Each term measures how close $y(\mathbf x;\mathbf w)$ is to $t$. Training is function minimization. Many minimizers also use the gradient with respect to $\mathbf w$. For general feedforward networks, backpropagation efficiently evaluates the gradient of $y$ with respect to $\mathbf w$, and hence of the objective.

> **Intuition note.** Each choice of weights is one specific "ramp" over input space, and learning is moving around the space of weights to find the best ramp. Bigger weights make a steeper ramp.

**39.3 Training the single neuron as a binary classifier** (pp. 475–477)
- Data: inputs $\{\mathbf x^{(n)}\}_{n=1}^N$ with binary labels $\{t^{(n)}\}$, and a neuron with output in $(0,1)$. The error function is
$$G(\mathbf w)=-\sum_n\Big[t^{(n)}\ln y(\mathbf x^{(n)};\mathbf w)+(1-t^{(n)})\ln\big(1-y(\mathbf x^{(n)};\mathbf w)\big)\Big]. \tag{39.11}$$
- Each term is the information content of one outcome. It can also be described as the relative entropy between the empirical distribution $(t^{(n)},1-t^{(n)})$ and the distribution $(y,1-y)$ implied by the neuron. $G$ is bounded below by zero and attains zero only if $y(\mathbf x^{(n)};\mathbf w)=t^{(n)}$ for all $n$ (p. 475).
- Exercise 39.2 asks the reader to show (not derived in the text):
$$g_j=\frac{\partial G}{\partial w_j}=\sum_{n=1}^N-(t^{(n)}-y^{(n)})\,x^{(n)}_j. \tag{39.12}$$
- The *error* on example $n$ is $e^{(n)}\equiv t^{(n)}-y^{(n)}$. The simplest use of a gradient is to descend it. The author notes this is often dimensionally incorrect, since a gradient has dimensions [1/parameter] and a parameter change has dimensions [parameter] (p. 475).
- The gradient is a sum of per-example terms
$$g^{(n)}_j\equiv-(t^{(n)}-y^{(n)})x^{(n)}_j. \tag{39.13}$$
This gives an on-line algorithm: present one input at a time and adjust $\mathbf w$ a little opposite to $\mathbf g^{(n)}$ (p. 475).
- **On-line gradient-descent algorithm** (pp. 475–476):
  - Architecture: as in 39.1.
  - Activity rule: $a=\sum_i w_ix_i$ (39.14), with inputs that may be arbitrary real numbers. Then $y(a)=1/(1+e^{-a})$ (39.15). The output may be viewed as the neuron's probability that the input is in class 1 rather than class 0.
  - Learning rule: the teacher supplies $t\in\{0,1\}$. Error signal $e=t-y$ (39.16). Weight change
$$\Delta w_i=\eta\,e\,x_i \tag{39.17}$$
where $\eta$ is the learning rate. It is commonly set by trial and error, to a constant or to a decreasing function of time $\tau$ such as $\eta_0/\tau$.
  - The rules are repeated for each pair $(\mathbf x,t)$. A fixed data set can be cycled through many times.
- **Batch learning** (p. 476): accumulate the changes of (39.17) over a batch and apply them at its end. For each pair compute $y^{(n)}=1/(1+\exp(-\sum_i w_ix_i^{(n)}))$ (39.18), $e^{(n)}=t^{(n)}-y^{(n)}$, and
$$g_i^{(n)}=-e^{(n)}x_i^{(n)}\tag{39.19}$$
Then
$$\Delta w_i=-\eta\sum_n g_i^{(n)}. \tag{39.20}$$
Batch learning is gradient descent. On-line learning is stochastic gradient descent.
- **Algorithm 39.5** (Octave, p. 478), shapes as the author's comments give them: $\mathbf x$ is $N\times I$ and $\mathbf t$ has length $N$ (so $\mathbf w$ has length $I$, by the matrix product). Each loop runs: `a = x*w` (all $N$ activations), `y = sigmoid(a)`, `e = t - y`, `g = -x'*e` (length $I$), `w = w - eta*(g + alpha*w)`. The `alpha` term is optional weight decay.
- **Figure 39.4** (pp. 476–477): a neuron with bias, $y=1/(1+e^{-(w_0+w_1x_1+w_2x_2)})$ (39.21), is trained on ten labelled examples. The settings are $\eta=0.01$, batch mode, and snapshots after 30, 80, 500, 3000, 10 000 and 40 000 iterations. The drawn contours are $a=0,\pm1$, i.e. $y=0.5,\,0.27,\,0.73$. The larger the weights, the closer together the contours.

> **Intuition note.** The weight update is "error × input": a weight moves more when its input is large and the neuron's answer is far from the target. On-line learning applies this per-example update after each example (a noisy, stochastic version of gradient descent); batch learning accumulates the same per-example terms and applies their sum at the end of the batch.

**39.4 Beyond descent on the error function: regularization** (p. 479)
- With a suitable $\eta$, the algorithm finds a $\mathbf w$ that correctly classifies as many examples as possible. If the examples are linearly separable, the neuron finds the separation and its weights diverge to ever-larger values (fig. 39.4f–k). This is overfitting: the model fits so well that generalization is likely to suffer.
- *Early stopping* is the ad hoc remedy: halt an error-minimizing algorithm before it finishes.
- *Regularization* is the more principled remedy: modify the objective to penalize solutions we dislike. Here we dislike the sharp boundary, which goes with large weights:
$$M(\mathbf w)=G(\mathbf w)+\alpha E_W(\mathbf w),\qquad E_W(\mathbf w)=\tfrac12\sum_i w_i^2. \tag{39.22, 39.23}$$
$E_W$ is the *weight decay* regularizer, and $\alpha$ is the weight decay rate (regularization constant). It is a *hyperparameter*: it plays a role in learning but not in the network's activity rule.
- Exercise 39.3 asks for $\partial M/\partial w_i$ and why the name "weight decay" fits.
- Figure 39.6 uses $\alpha=0.01,0.1,1$ (p. 478). Larger $\alpha$ biases the solution towards broader sigmoids with decision boundaries closer to the origin (p. 479). The caption says weight decay here has an effect very similar to early stopping (p. 478).
- *Note* (p. 479): plain gradient descent is in general not the most efficient minimizer. Momentum improves convergence but is also not recommended. Most experts use more advanced optimizers such as conjugate gradients. Momentum, sometimes also written $\alpha$, must not be confused with weight decay.

> **Intuition note.** Separable data lets the neuron keep lowering $G$ by making its boundary ever sharper, which means ever bigger weights. The penalty $\alpha E_W$ makes large weights costly, so the minimum of $M$ is a compromise between fitting the data and keeping the weights small.

**39.5 Further exercises** (pp. 480–481): see Exercises below. Page 482 lists three warm-up problems for Chapter 40.

## Toy example (ours, not from the text)
One on-line step for a neuron with a bias and one input. Take $\mathbf w=(w_0,w_1)=(0,0)$, input $\mathbf x=(x_0,x_1)=(1,2)$, target $t=1$, $\eta=0.1$.
1. Activation: $a=0\cdot1+0\cdot2=0$, so $y=1/(1+e^0)=0.5$.
2. Error: $e=t-y=0.5$.
3. Updates: $\Delta w_0=\eta e x_0=0.1\cdot0.5\cdot1=0.05$ and $\Delta w_1=0.1\cdot0.5\cdot2=0.10$. So $\mathbf w=(0.05,0.10)$.
4. New activation: $a=0.05+0.10\cdot2=0.25$. Then $y=1/(1+e^{-0.25})\approx1/(1+0.7788)\approx0.562$.
5. The error fell from 0.5 to about 0.438. This example's term of $G$ fell from $-\ln0.5\approx0.693$ to $-\ln0.562\approx0.576$.

## Concepts
- [[neural-network-architecture-activity-learning]] (new) — a network is specified by its variables and topology, its fast activity rule and its slower learning rule (p. 470)
- [[supervised-vs-unsupervised-learning]] (new) — targets supplied by a teacher versus unlabelled examples only (p. 470)
- [[single-neuron]] (new) — weighted sum of inputs, then an activation function, giving the output (p. 471)
- [[logistic-sigmoid]] (new) — $y=1/(1+e^{-a})$, bounded in $(0,1)$; the neuron's output can be viewed as a class-1 probability (pp. 471, 475)
- [[weight-space]] (new) — parameter space of the network, each point being one function of $\mathbf x$ (p. 473)
- [[self-information / surprisal]] — each term of $G$ is the information content of one outcome (p. 475)
- [[relative entropy / KL divergence]] — each term of $G$ is also described as relative entropy between the empirical $(t,1-t)$ and $(y,1-y)$ (p. 475)
- [[gradient-descent-learning]] (new) — adjust $\mathbf w$ opposite to the gradient of $G$; on-line is stochastic, batch is gradient descent (pp. 475–476)
- [[overfitting-regularization-weight-decay]] (new) — fitting so well that generalization is likely to suffer; remedy by adding $\alpha E_W$ to the objective (p. 479)
- [[Posterior distribution]] — $P(s=1|\mathbf y)$ has the logistic form of a neuron (pp. 472, 480)

## Canonical instances
- [[pulse-detection-gaussian-channel]] — the posterior of a binary source given a Gaussian-noise signal is a linear logistic function (p. 472)
- [[biological-vs-address-memory]] — the contrast that motivates neural nets (pp. 468–469)
- [[noisy-led-display]] — exercise: posterior of the displayed character given a noisy 7-segment display (p. 480)
- [[3-1-repetition-style-code-decoder]] — exercise: optimal decoder for a (3,1) code on a binary symmetric channel as a neuron (pp. 480–481)

## Bridges (candidates)
- [same-math] Logistic output of a neuron ↔ Bayesian: posterior $P(s=1|\mathbf y)$ with Gaussian likelihoods and a shared covariance matrix (eqs. 39.8–39.9, section 11.2) — the formulas coincide.
- [same-math] Error function $G(\mathbf w)$ ↔ information theory: cross-entropy / sum of information contents of the labels under the neuron's predictive probability — the text says this directly.
- [structural-analogy] Weight decay $\alpha E_W$ ↔ Bayesian: a prior penalizing large parameters — the penalty adds to the objective as a log-prior would; this unit does not make the link.
- [structural-analogy] Hyperparameter $\alpha$ ↔ Bayesian: parameters of a prior fixed outside the model — it shapes learning but not the activity rule.

## Questions this raises
- How can the weight-decay term be justified probabilistically rather than as a convenience?
- Why does the gradient of $G$ with the sigmoid reduce to "error times input", and does it for other output functions?
- What does the network do when classes are not linearly separable?
- How many labelled points can a single neuron fit?

## Exercises worth doing
- Ex. 39.2 (p. 475) — derive the gradient of $G$, the core of the learning rule — difficulty: medium
- Ex. 39.3 (p. 479) — derivative of $M(\mathbf w)$; why "weight decay" — difficulty: easy
- Ex. 39.4 (p. 480) — two zero-mean Gaussians with different variances also give a logistic posterior, with $x_i=g(z_i)$ — difficulty: medium
- Ex. 39.5 (p. 480) — noisy LED: the posterior of $s$ is logistic (two characters) or a softmax (ten); design a better alphabet — difficulty: medium
- Ex. 39.6 (pp. 480–481) — the optimal decoder of a (3,1) code on a binary symmetric channel as a neuron — difficulty: medium

## Reading notes
- Printed page = pdf page − 12 (pdf 480 = printed 468).
- The unit combines chapter 38 (pp. 468–470) and chapter 39 (pp. 471–481), plus the "Problems to look at before Chapter 40" page (p. 482). Those problems (Exercises 40.1–40.3) are not digested here.
- Figure text (3-D plots, Figures 39.3, 39.4, 39.6) is garbled in the text layer. I read captions and curves from the page images. The numeric labels on the plots were not transcribed.
- Exercise 39.1 is stated on p. 472 and its answer is not given in these pages.
- Table 39.7 (a 15-character LED alphabet) is a small pictorial table; I did not transcribe its glyphs.

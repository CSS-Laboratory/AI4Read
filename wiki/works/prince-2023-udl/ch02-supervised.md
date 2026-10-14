---
id: prince-2023-udl/ch02-supervised
work: prince-2023-udl
unit: "Chapter 2 — Supervised learning"
pages: 17-24
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Supervised learning

## L0 — One line
A supervised model is a parameterised function $y=f[x,\phi]$, trained by choosing the parameters $\phi$ that minimise a loss measuring the mismatch with training pairs, then checked on separate test data.

## L1 — The gist (≤ 120 words)
How can a machine learn a mapping from inputs to outputs from examples? The chapter defines a model as a function with parameters. A loss function scores how badly the parameters fit the training pairs. Training searches for the parameters with the smallest loss. Testing on unseen data shows how well the model generalizes. The author illustrates all this with a straight line fitted by least squares. Later chapters (shallow and deep networks, loss functions, training) expand on these ideas. A simple model such as a line might not capture the true relationship (underfitting), while a very expressive model may fit peculiarities of the training data (overfitting).

**Prerequisites:** functions of one variable; the idea of a slope and a y-intercept; sums ($\sum$); what a gradient (slope of a surface) means.

## L2 — Key ideas (5–10 bullets)
- A model $y=f[x,\phi]$ is a fixed equation; the parameters $\phi$ pick one relation out of a family (p. 18).
- Inference means computing $y$ from $x$; training means finding good $\phi$ from $I$ training pairs (p. 17–18).
- The loss $L[\phi]$ is one number summarising the mismatch; training is $\hat\phi=\operatorname{argmin}_\phi L[\phi]$ (p. 18).
- For 1D linear regression, $y=\phi_0+\phi_1x$ and the loss is a sum of squared deviations (least squares) (p. 19).
- With two parameters, the loss can be drawn as a surface whose lowest point gives the best parameters (p. 21).
- Training walks downhill using the gradient; for linear regression a closed form also exists, but gradient descent works for models without one (p. 22).
- Test data show how well a model generalizes; a model too simple to capture the relation (underfitting) or so expressive that it fits training peculiarities (overfitting) may generalize poorly (p. 22).
- Discriminative models ($y$ from $x$) dominate modern machine learning over generative ones ($x$ from $y$) (p. 24).

## L3 — Walkthrough

### Opening and 2.1 Overview (pp. 17–18)
A supervised model maps inputs to outputs. Example: age and mileage of a used Prius in, estimated price in dollars out (p. 17). The model is a mathematical function. Passing inputs through it is **inference**. The equation holds **parameters**; different values give different input–output relations, so the equation describes a *family* of relations (p. 17).

Inputs $x$ and outputs $y$ are assumed to be vectors of fixed size, with elements always in the same order. This is called structured or tabular data (p. 17).
$$y=f[x]\tag{2.1}$$
$$y=f[x,\phi]\tag{2.2}$$
Training uses a dataset of $I$ pairs $\{x_i,y_i\}$. The **loss** $L$ is a scalar saying how poorly the model predicts the training outputs for parameters $\phi$ (p. 18). Viewed as a function $L[\phi]$, we seek the minimiser:
$$\hat\phi=\operatorname*{argmin}_\phi\big[L[\phi]\big]\tag{2.3}$$
Footnote: strictly, $L$ also depends on the training data (p. 18). Afterwards the model is run on separate **test data** to see how it generalizes to unseen examples. If performance is adequate, it is deployed (p. 18).

*Intuition note:* The model is a machine with adjustable knobs ($\phi$). The loss tells you how wrong the machine is for each knob setting. Learning means turning the knobs to make it least wrong on the examples.

### 2.2.1 1D linear regression model (pp. 18–19)
$$y=f[x,\phi]=\phi_0+\phi_1x\tag{2.4}$$
$\phi_0$ is the y-intercept, $\phi_1$ the slope. Equation 2.4 defines the family of all lines; $\phi$ picks one (Fig. 2.1 shows $\phi=[1.2,-0.1]$, $[0.0,1.0]$ and $[1.0,-0.4]$) (p. 19).

### 2.2.2 Loss (pp. 19–21)
Different lines fit the data better or worse, so a principled score is needed: lower loss means better fit (p. 19). The deviation is the gap between the prediction $f[x_i,\phi]$ and the true $y_i$. The total mismatch (training error, or loss) is the sum of squares:
$$L[\phi]=\sum_{i=1}^{I}\big(f[x_i,\phi]-y_i\big)^2=\sum_{i=1}^{I}(\phi_0+\phi_1x_i-y_i)^2\tag{2.5}$$
This is a **least-squares loss**. Squaring means the direction of the deviation does not matter. The author says there are also theoretical reasons for this choice, to be given in chapter 5 (pp. 19, 21).

Example (Fig. 2.2, $I=12$ points): $\phi=[0.4,0.2]$ gives $L=7.07$; $[1.60,-0.8]$ gives $L=10.28$; $[0.82,0.52]$ gives $L=0.20$. The caption says this last line has the smallest loss of all lines (p. 20).

The goal is:
$$\hat\phi=\operatorname*{argmin}_\phi\Big[\sum_{i=1}^{I}(\phi_0+\phi_1x_i-y_i)^2\Big]\tag{2.6}$$
With only two parameters, the loss can be computed for every combination and drawn as a surface or heatmap (Fig. 2.3). The best parameters lie at its minimum (p. 21).

*Intuition note:* Every pair $(\phi_0,\phi_1)$ is a point on a map, and its height is the loss. Fitting the line means finding the lowest point of the landscape.

### 2.2.3 Training (p. 22)
Training (also called fitting or learning) starts from random parameters and "walks down" the loss surface. At each point, measure the gradient and step in the steepest downhill direction. Repeat until the gradient is flat and no further improvement is possible (p. 22; Fig. 2.4, positions 0→4, p. 23). Footnote: for linear regression this iteration is not necessary, since closed-form expressions exist. Gradient descent is used because it works for complex models with no closed form and too many parameters to evaluate every combination (p. 22).

### 2.2.4 Testing (p. 22)
Loss is computed on separate test data. Generalization depends partly on how representative and complete the training data are, and also on how expressive the model is. A simple model such as a line might not capture the true relationship (**underfitting**). A very expressive model may describe atypical statistical peculiarities of the training data and give unusual predictions (**overfitting**) (p. 22).

### 2.3 Summary (p. 22)
Model $y=f[x,\phi]$; loss over the training set; search for minimising parameters; evaluate on test data. Roadmap: shallow networks (ch. 3) describe a much larger family of relations than a line; deep networks (ch. 4) are just as expressive but can describe complex functions with fewer parameters and work better in practice; ch. 5 loss functions; ch. 6–7 training; ch. 8 performance measurement; ch. 9 regularization (p. 22).

### Notes (pp. 23–24)
- **Loss vs. cost function:** used interchangeably in much of machine learning and in this book. More properly, a *loss* is the term for one data point (each squared term in 2.5), and the *cost* is the whole quantity minimised (all of 2.5), which may contain extra terms. An *objective function* is any function to be maximised or minimised (p. 23).
- **Generative vs. discriminative:** the models here are discriminative ($y=f[x,\phi]$). A generative model computes $x=g[y,\phi]$. Inference then needs the inverse $y=g^{-1}[x,\phi]$, which may be difficult. Its advantage is that prior knowledge of how the data arise can be built in (e.g. car shape and 3D geometry). Yet discriminative models dominate, because flexible models trained on large data usually trump this advantage (pp. 23–24).

## Toy example (ours)
Data: $(x,y)=(0,1),(1,3),(2,5)$. Try $\phi=[0,1]$: predictions $0,1,2$; deviations $-1,-2,-3$; $L=1+4+9=14$. Try $\phi=[1,2]$: predictions $1,3,5$; deviations $0,0,0$; $L=0$. This is the minimum since $L\ge0$. Gradient step (added step): at $\phi=[0,1]$, $\partial L/\partial\phi_0=2\sum(\text{dev})=2(-6)=-12$; $\partial L/\partial\phi_1=2\sum(\text{dev}\cdot x)=2(0-2-6)=-16$. Both negative, so increasing both parameters lowers the loss, towards $[1,2]$.

## Concepts
- [[supervised-learning]] (new) — learning a mapping from inputs to outputs using input/output training pairs (p. 17)
- [[inference]] (new) — computing the prediction $y$ from input $x$ with the model (p. 17–18)
- [[loss-function]] (new) — scalar measuring mismatch between predictions and training outputs, a function of $\phi$ (p. 18)
- [[least-squares-loss]] (new) — sum of squared deviations between predictions and outputs (p. 19)
- [[gradient-descent]] (new) — iteratively stepping downhill on the loss using its gradient (p. 22)
- [[generalization]] (new) — performance on test data not seen in training (p. 18)
- [[underfitting-overfitting]] (new) — model too simple to capture the relation, or so expressive it fits training peculiarities (p. 22)
- [[discriminative-vs-generative-model]] (new) — predicting $y$ from $x$, versus computing $x$ from $y$ (p. 23)

## Canonical instances
- [[1d-linear-regression]] — the line $y=\phi_0+\phi_1x$ fitted by least squares (p. 18)
- [[prius-price-example]] — age and mileage predict price (p. 17)

## Bridges (candidates)
- [structural-analogy] Minimising $L[\phi]$ by gradient steps ↔ LLM pretraining: minimising cross-entropy over parameters — same loop with a different loss (not stated in this unit).
- [structural-analogy] Train/test split and generalization ↔ held-out perplexity for language models.

## Questions this raises
- Why is the squared deviation a good choice, and what does chapter 5 say about it?
- How do we know when a model is under- or overfitting, and how is performance measured (ch. 8)?
- Can gradient descent get stuck when the loss surface is not as simple as this bowl?

## Exercises worth doing
- Problem 2.1 (p. 24) — derive $\partial L/\partial\phi_0$ and $\partial L/\partial\phi_1$ — difficulty: easy
- Problem 2.2 (p. 24) — set the derivatives to zero to get the closed-form fit — difficulty: medium
- Problem 2.3* (p. 24) — reformulate as a generative model $x=\phi'_0+\phi'_1y$; compare predictions with the discriminative fit — difficulty: hard

## Reading notes
- Printed page = pdf − 14.
- The text layer is readable, but display equations (2.3, 2.5, 2.6) are laid out untidily there; they were transcribed from the page images (pp. 18, 19, 21). Footnote 1 is on p. 18, footnote 2 on p. 22.
- The Notes and Problems on pp. 23–24 belong to this chapter.

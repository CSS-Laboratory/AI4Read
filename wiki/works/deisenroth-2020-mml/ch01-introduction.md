---
id: deisenroth-2020-mml/ch01-introduction
work: deisenroth-2020-mml
unit: "1 Introduction and Motivation"
pages: 11–16
fields: [linear-algebra]
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
# Introduction and Motivation

## L0 — One line
Machine learning rests on three things (data, a model, learning), and this book first builds the mathematics for them (Part I) and then applies it to four core problems (Part II).

## L1 — The gist (≤ 120 words)
The chapter asks why a machine learning reader needs mathematics, and how to read this book. Its answer: machine learning means automatically extracting patterns from data. Its three core concepts are data (treated as vectors), a model, and learning (optimizing the model's parameters). The goal is good performance on unseen data. The authors say the maths can help in building new methods, debugging existing ones, and understanding their assumptions and limits. Part I covers the mathematical foundations. Part II covers four applications: regression, dimensionality reduction, density estimation and classification. Readers may go bottom-up or top-down, because the book is modular.

**Prerequisites:** none beyond the idea of a function and a table of numbers.

## L2 — Key ideas (5–10 bullets)
- Machine learning designs general-purpose algorithms that automatically extract information from data. Its core concepts are data, a model and learning (p. 11).
- A model "learns" if its performance on a task improves after the data is taken into account. The aim is to generalize to unseen data (p. 11).
- The authors argue that mathematical foundations can help with creating, debugging and understanding the limits of ML methods (p. 11).
- Words are slippery. "Algorithm" can mean a predictor or the training of a predictor, and "vector" has three views: array, arrow, or object obeying addition and scaling (p. 12).
- Training is compared to hill climbing. Good performance on training data may only mean memorization (pp. 12–13).
- The book summarizes ML as: data as vectors, a model (probabilistic or optimization view), and learning by numerical optimization (p. 13).
- It can be read bottom-up or top-down. Part I chapters mostly build on each other, and Part II chapters can be read in any order (p. 13).
- Part I covers linear algebra, analytic geometry, matrix decomposition, vector calculus, probability and optimization. Part II covers regression, PCA (principal component analysis, for dimensionality reduction), Gaussian mixtures (for density estimation) and SVMs (support vector machines, for classification) (pp. 15–16).

## L3 — Walkthrough

### Opening (p. 11)
Machine learning is about algorithms that automatically extract valuable information from data. "Automatic" means general-purpose methods that apply to many datasets and still give meaningful results (p. 11).

Three concepts are at the core (p. 11):
- **Data.** The aim is to find patterns, ideally without much domain-specific expertise. Example given: finding topics shared across a large corpus of documents (Hoffman et al., 2010) (p. 11).
- **Model.** Models are typically related to the process that generates the data. In regression, a model describes a function from inputs to real-valued outputs. Paraphrasing Mitchell (1997), a model learns if its performance on a task improves after the data is taken into account. The goal is to generalize to yet unseen data (p. 11).
- **Learning.** Learning finds patterns and structure automatically by optimizing the model's parameters (p. 11).

Why the maths matters (the authors' belief): it helps to understand the fundamental principles under complex systems. It can help in creating new solutions, understanding and debugging existing ones, and seeing the assumptions and limitations of methods (p. 11).

### 1.1 Finding Words for Intuitions (pp. 12–13)
- **Ambiguous words.** "Machine learning algorithm" has two senses. Sense 1 is a system that makes predictions from input data, called a *predictor*. Sense 2 is a system that adapts the predictor's internal parameters so it does well on future unseen inputs, called *training*. The book does not resolve this ambiguity and tries to make the context clear (p. 12).
- **Data as vectors.** Not all data is numerical, but the book assumes data is already converted to numbers, so it thinks of data as vectors. There are at least three views of a vector (p. 12):
  - an array of numbers (computer science);
  - an arrow with direction and magnitude (physics);
  - an object that obeys addition and scaling (mathematics).
- **Models.** A model typically describes a process for generating data similar to the dataset at hand. Good models can also be thought of as simplified versions of the real, unknown data-generating process. They capture the relevant aspects and hidden patterns. A good model can predict what would happen in the real world without real-world experiments (p. 12).
- **Learning.** Training means using the available data to optimize model parameters with respect to a utility function. The utility function evaluates how well the model predicts the training data. Most training methods can be thought of as analogous to climbing a hill to its peak, where the peak is a maximum of a performance measure (pp. 12–13).
  - In practice we want good performance on unseen data. Doing well on training data may only mean we found a good way to memorize it, which may not generalize. In practical applications we often need to expose the system to situations it has not encountered before (p. 13).

Summary list of the main concepts (p. 13):
1. Represent data as vectors.
2. Choose a model, using either the probabilistic or the optimization view.
3. Learn from data with numerical optimization, aiming at good performance on data not used for training.

*Intuition note:* A model is a simplified stand-in for the real (unknown) process behind the data. Learning means tuning its knobs (parameters) to score well. The real test is data it has never seen, not the data it was tuned on.

### 1.2 Two Ways to Read This Book (pp. 13–16)
- **Bottom-up** builds from foundations to advanced concepts. Advantage: the reader can always rely on earlier concepts. Drawback: for a practitioner many foundational concepts are not particularly interesting by themselves, and the lack of motivation means most foundational definitions are quickly forgotten (p. 13).
- **Top-down** drills from practical needs to basics. Advantage: the reader knows why a concept is needed. Drawback: the knowledge may rest on shaky foundations, and readers must remember words they cannot yet understand (p. 13).
- The book is modular so it can be read either way. Part I lays mathematical foundations. Part II applies them to four pillars: regression, dimensionality reduction, density estimation and classification (Figure 1.1, p. 14). Part I chapters mostly build on earlier ones, but one can skip and work backward. Part II chapters are loosely coupled and can be read in any order. Many cross-pointers link the parts (pp. 13–14).
- Figure 1.1 shows the pillars standing on six foundations: Linear Algebra, Analytic Geometry, Matrix Decomposition, Vector Calculus, Probability & Distributions, Optimization (p. 14).

**Part I (pp. 14–15).**
- Ch. 2, linear algebra: numerical data are vectors, and a table of data is a matrix (p. 14).
- Ch. 3, analytic geometry: operations taking two vectors and returning a number for similarity and distance. The idea is that similar vectors should get similar outputs from the predictor (p. 14).
- Ch. 4, matrix decomposition: some matrix operations allow intuitive interpretation of the data and more efficient learning (p. 14).
- Ch. 6, probability theory: a language for "noise" (data as noisy observations of a true signal). It also quantifies uncertainty, such as confidence in a prediction at a test point (pp. 14–15).
- Ch. 5, vector calculus: gradients, which tell the direction in which to search for a solution (p. 15).
- Ch. 7, optimization: uses gradients to find maxima/minima of functions (p. 15).

**Part II (pp. 15–16).** Chapters are broadly ordered by ascending difficulty (p. 15).
- Ch. 8 restates data, models and parameter estimation mathematically. It also gives guidelines for experimental set-ups that guard against overly optimistic evaluation (p. 15).
- Ch. 9, linear regression: find functions mapping $x \in \mathbb{R}^D$ to observed values $y \in \mathbb{R}$ (labels). It covers maximum likelihood and maximum a posteriori estimation, and Bayesian linear regression, which integrates the parameters out instead of optimizing them (p. 15).
- Ch. 10, dimensionality reduction via principal component analysis: find a compact, lower-dimensional representation of $x \in \mathbb{R}^D$. There are no labels (p. 15).
- Ch. 11, density estimation via Gaussian mixture models: find a probability distribution describing the dataset, using an iterative scheme for the parameters. There are no labels, and no low-dimensional representation is sought (p. 15).
- Ch. 12, classification via support vector machines: inputs $x$ with labels $y$, as in regression, but the labels are integers, which "requires special care" (pp. 15–16).

*Intuition note:* The book is a two-layer cake. The text says each pillar in Part II needs a mathematical foundation from Part I. In the text, regression, dimensionality reduction, density estimation and classification are contrasted partly by whether labels exist and what kind they are.

### 1.3 Exercises and Feedback (p. 16)
Part I has exercises, mostly pen-and-paper. Part II has programming tutorials (jupyter notebooks). The book is free to download at mml-book.com, where tutorials, errata and extra material are found (p. 16).

## Toy example
*(Our own, not from the text.)* Data as vectors, a model, learning as hill climbing, and generalization.

- Training data (input $x$, label $y$): $(1,2)$, $(2,4)$, $(3,6)$. One unseen point: $x=4$, whose true $y$ we pretend not to know.
- Model: $\hat y = w\,x$, with one parameter $w$.
- Utility: $-\sum (y-\hat y)^2$. Higher is better.

| $w$ | errors $y-wx$ | squares | utility |
|---|---|---|---|
| 1 | $2-1=1$, $4-2=2$, $6-3=3$ | 1, 4, 9 (sum 14) | $-14$ |
| 2 | 0, 0, 0 | 0 | $0$ |
| 3 | $2-3=-1$, $4-6=-2$, $6-9=-3$ | 1, 4, 9 (sum 14) | $-14$ |

Moving $w$ from 1 to 2 raises utility from $-14$ to $0$ (a step uphill). Going on to 3 lowers it again, so $w=2$ is the best of these three values.

Generalization: for the unseen $x=4$, the model predicts $\hat y = 2\cdot 4 = 8$. A pure memorizer (a lookup table of the three pairs) has no entry for $x=4$ and cannot predict at all. It scores perfectly on the training data but does not generalize.

## Concepts
- [[machine-learning-three-components]] (new) — data, a model and learning; the core concepts of ML (p. 11)
- [[vector]] — here, data as vectors; three views: array, arrow, object obeying addition and scaling (p. 12)
- [[predictor]] (new) — a machine learning algorithm in the sense of a system that predicts from input data (p. 12)
- [[training]] (new) — adapting a predictor's parameters to do well on future unseen input (p. 12)
- [[generalization]] (new) — performing well on unseen data, not merely on training data (pp. 11, 13)
- [[utility-function]] (new) — the measure of how well a model predicts the training data; training optimizes it (p. 12)
- [[four-pillars-of-ml]] (new) — regression, dimensionality reduction, density estimation, classification (p. 13)
- [[gradient]] (new) — in this unit, the quantity that gives the direction in which to search for a solution (p. 15)

## Canonical instances
- [[topic-finding-in-documents]] (new) — automatically finding topics shared across a corpus of documents (p. 11)
- [[linear-regression]] (new) — inputs $x\in\mathbb{R}^D$ mapped to real labels $y$ (p. 15)
- [[pca-dimensionality-reduction]] (new) — compact lower-dimensional representation, no labels (p. 15)
- [[gaussian-mixture-density-estimation]] (new) — a probability distribution describing the data, fitted iteratively (p. 15)
- [[svm-classification]] (new) — inputs with integer labels (pp. 15–16)

## Bridges (candidates)
- [metaphor] Training as hill climbing ↔ optimization: following the gradient to a maximum of a performance measure (pp. 13, 15).
- [structural-analogy] "Similar vectors get similar predictions" ↔ linear algebra: inner-product similarity such as cosine similarity (p. 14). The unit does not name the operation.
- [structural-analogy] Memorizing training data without generalizing ↔ statistics: overfitting (canon link; not stated in this unit).

## Questions this raises
- How do the probabilistic and optimization views of a model, and the utility function used in training, fit together (p. 13)?
- Which concrete operations on two vectors give "similarity", and how do they define distance (Ch. 3)?
- How do we build evaluation set-ups that guard against over-optimistic results (Ch. 8)?
- Why does regression with real labels differ from classification with integer labels (p. 16)?

## Reading notes
- Printed page = pdf page − 6. The text layer matched the images and was readable.
- Running footers show the book as a draft dated 2024-01-15, ©2024 by the authors, published by Cambridge University Press (2020). Page 17 (printed 11) carries the free-download notice.
- Figure 1.1 (p. 14) was checked in the image. Its pillar images are tiny and not described here.
- The unit lists exercises in Part I and notebooks in Part II (p. 16) but prints none, so there is no Exercises section.
- Chapter 8 is described as covering "data, models, and parameter estimation" (p. 15). Earlier the three components are "data, a model, and learning" (p. 11).

---
id: prince-2023-udl/ch01-introduction
work: prince-2023-udl
unit: "Chapter 1 — Introduction"
pages: 1-16
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Introduction (Understanding Deep Learning, ch. 1)

## L0 — One line
Deep neural networks are flexible fitted equations that underlie the cutting-edge methods in supervised, unsupervised (generative) and reinforcement learning, so they deserve both technical study and ethical scrutiny.

## L1 — The gist (≤ 120 words)
The chapter maps the field. Machine learning fits mathematical models to data. It splits into supervised learning (learn input→output from labelled pairs), unsupervised learning (learn the structure of unlabelled data, e.g. generative models), and reinforcement learning (an agent learns actions that earn reward). At the time of writing, cutting-edge methods in all three rely on deep networks. The author also lists five ethical concerns (bias, explainability, weapons, concentrated power, existential risk), previews the book's chapters, recommends other books, and explains how to use this one. The chapter matters because it fixes the vocabulary and the taxonomy that later chapters follow.

**Prerequisites:** vectors as lists of numbers; the idea of a function or curve fitted to points; basic probability ("sampling from a distribution").

## L2 — Key ideas
- AI ⊃ machine learning ⊃ (deep learning, which cuts across supervised, unsupervised and reinforcement learning) (p. 1–2).
- Supervised learning maps an input vector to an output vector. Output type decides the task: regression (one continuous number), multivariate regression (several numbers), binary or multiclass classification (probabilities over two, or over $N>2$, categories) (p. 2).
- A model is a *family* of equations. Training means searching that family for the member that best fits labelled input/output pairs (p. 5).
- Structured outputs (translation, image synthesis) are harder because several outputs may be valid and outputs must obey a "grammar". That grammar can be learned without labels (p. 7).
- Generative unsupervised models synthesize new data resembling the training data. Many use latent variables (a smaller number of underlying variables that describe each example) with a simple distribution (p. 7–11).
- Reinforcement learning has an agent, actions, states and rewards, and two difficulties: temporal credit assignment (a reward may come some time after the action that earned it) and exploration vs. exploitation (use what the agent already knows, or try other actions) (p. 11–12).
- Five ethical concerns are named; the list is "far from exhaustive" and the concerns are "not speculative" (p. 13–14).

## L3 — Walkthrough

**Opening (p. 1).** AI builds systems that simulate intelligent behavior, using logic, search or probabilistic reasoning. Machine learning is a subset that learns decisions by fitting mathematical models to observed data. The author says it is now "incorrectly" almost synonymous with AI. A *deep neural network* is a type of machine learning model; fitting it to data is *deep learning*. The book has no proofs and almost no code. It splits machine learning into supervised, unsupervised and reinforcement learning, and says cutting-edge methods in all three use deep learning (p. 1; fig. 1.1, p. 2).

### 1.1 Supervised learning (p. 1–7)
Supervised models define a mapping from input data to an output prediction (p. 1).

**1.1.1 Regression and classification (p. 2–3, fig. 1.2).** A real-world input is encoded as a vector of numbers. The model maps it to an output vector, which is translated back into a real-world prediction. The model is treated as a black box for now (p. 2).
- *Regression*: the output is a continuous number. Example: house price from square footage, bedrooms, etc.
- *Multivariate regression*: more than one output number. Example: a molecule's structure → freezing and boiling points.
- *Binary classification*: two categories. Example: restaurant review → positive/negative. The output vector holds the probability of each category.
- *Multiclass classification*: $N>2$ categories, output a vector of $N$ probabilities. Examples: music genre from audio; object from image (p. 2).

**1.1.2 Inputs (p. 2–4).**
- Tabular data (house prices) has no internal structure. Reordering the inputs and rebuilding the model should leave predictions unchanged (p. 2).
- Text has variable length and word order matters. The author's example is *my wife ate the chicken* versus *the chicken ate my wife*. Text is encoded with a fixed 10,000-word vocabulary by concatenating word indices (p. 3–4).
- Audio is high-dimensional. A 10-second clip at 44.1 kHz with 16-bit integers is 441,000 integers (p. 4).
- Images are huge and have spatial structure. Pixels above and below each other are closely related even though they are not adjacent in the input vector (p. 4).
- Molecules have varying numbers of atoms connected in different ways. The model must take both the geometric structure and the atoms (p. 4).

**1.1.3 Machine learning models (p. 4–5, fig. 1.3).** Example: predict a child's height from age. The model is an equation for how average height varies with age. It predicts 139 cm at age 10 (p. 5). More precisely, the model is a *family* of equations (a family of curves). *Training data* (input/output pairs) select one member. Training or fitting means searching the family for the equation that describes the training data most accurately (p. 5). Labelled pairs act as a teacher or supervisor, hence "supervised learning" (p. 5).

*Intuition note:* A "model" is not one formula but a menu of formulas. Training is picking the item on the menu that matches your labelled examples best.

**1.1.4 Deep neural networks (p. 5).** These are equations that can represent an extremely broad family of input–output relationships, and it is particularly easy to search that family. They can handle inputs that are large, variable-length and structured. Outputs can be one number, several numbers, or class probabilities. The author asks the reader to "suspend disbelief" that equations can have such properties (p. 5).

**1.1.5 Structured outputs (p. 5–7, fig. 1.4).**
- Semantic segmentation (a binary label per pixel: cow or background) and monocular depth estimation (a depth per pixel) have high-dimensional outputs whose structure is closely tied to the input. A neighbouring pixel with a similar RGB value probably has the same label, and this can be exploited (p. 5).
- Audio transcription, translation and caption→image synthesis have outputs with complex structure that is not closely tied to the input (p. 5–7).
- In principle these can be tackled by standard supervised learning, but they are harder for two reasons. (1) The output may be genuinely ambiguous: several valid translations, many images fit a caption. (2) The output has structure: not every word string is a valid sentence, not every set of RGB values is a plausible image. The model must respect the output's "grammar" (p. 7).
- This grammar can be learned without output labels, e.g. from the statistics of a large text corpus. That links to unsupervised learning (p. 7).

### 1.2 Unsupervised learning (p. 7–11)
Unsupervised learning builds a model from inputs *without* output labels. The goal is to describe or understand the structure of the data, not to learn a mapping. Data may be discrete or continuous, low- or high-dimensional, constant or variable length (p. 7).

**1.2.1 Generative models (p. 7–9).**
- The book focuses on models that synthesize new examples statistically indistinguishable from the training data (p. 7).
- Some models describe the probability distribution explicitly and generate by sampling from it. Others only learn a mechanism for generating examples (p. 7).
- Successes: images (fig. 1.5) and text (fig. 1.6). Fig. 1.6's caption says a text model assigns a probability to every output string, and sampling gives strings that follow the training statistics but are new (p. 8).
- *Conditional generation* fixes some outputs in advance, as in image inpainting (fig. 1.7) and text completion (fig. 1.8, produced by GPT-3) (p. 7–9).
- The author says modern text models can appear intelligent. Given text plus a question, the model often fills in the answer by generating the most likely completion. **Author's claim:** "in reality" the model only knows the statistics of language and does not understand the significance of its answers (p. 7).

**1.2.2 Latent variables (p. 9–11).**
- Some (but not all) generative models exploit the fact that data can be lower-dimensional than the raw number of variables suggests. Valid English sentences are far fewer than random word strings. Real images are a tiny subset of all RGB pixel assignments, because physical processes generate them (p. 9).
- Fig. 1.9: the face has roughly 42 muscles, so most variation in images of one person in the same lighting can be described with about 42 numbers (p. 9).
- So each example can be described by fewer underlying *latent variables*. Deep learning describes the mapping from latent variables to data. The latent variables typically have a simple distribution by design (p. 9–11).
- Generation: sample the simple distribution, then pass the sample through the deep model (fig. 1.10, p. 10–11).
- Interpolation: find the latent variables of two real examples, interpolate between them, and map the intermediate points back to data space (fig. 1.11, p. 10–11).

*Intuition note:* The data live on a small "surface" inside a huge space of possible pixel or word combinations. Latent variables are coordinates on that surface, and the network turns coordinates into data.

**1.2.3 Connecting supervised and unsupervised learning (p. 11).** For structured-output tasks such as caption→image, one can learn a relation between latent variables that explain the text and latent variables that explain the image, instead of mapping text directly to an image. Three advantages: (1) fewer text/image pairs may be needed, since inputs and outputs are lower-dimensional; (2) a plausible-looking image is more likely, since any sensible latent values should give a plausible example; (3) adding randomness to either mapping yields multiple images that all fit the caption (fig. 1.12) (p. 11).

### 1.3 Reinforcement learning (p. 11–12)
An *agent* lives in a world and performs actions at each time step. Actions change the state, not necessarily deterministically, and may yield rewards. The goal is to choose actions with high reward on average (p. 11–12). Two complications:
- *Temporal credit assignment*: the reward may arrive some time after the action, so linking them is hard.
- *Exploration vs. exploitation*: should the agent use what it already knows, or try other actions that might do better? (p. 12)

**1.3.1 Two examples (p. 12).**
- Humanoid robot locomotion: it may be rewarded for reaching checkpoints, but many actions precede the reward and it is unclear which mattered (credit assignment). The robot may find that sliding on its side earns slow reward, versus walking, which is faster (exploration/exploitation).
- Chess: moves change the state non-deterministically, since the opponent may reply in many ways. If the only reward is winning at the end, credit assignment is "extreme".
- One way to use deep learning is a *policy network*, a mapping from the observed state to an action. For chess it maps board state to the choice of move (fig. 1.13, p. 13).

### 1.4 Ethics (p. 12–14)
The author says AI will change the world at least as much as electricity, the internal combustion engine, the transistor or the internet. He adds that scientists and engineers are often unrealistically optimistic, and that potential for harm is as great as for benefit (p. 12–13). Five concerns (author's views):
- **Bias and fairness:** a salary predictor trained on historical data will reproduce historical biases (it will probably predict lower pay for women). Reported cases: a face super-resolution system made non-white people look more white; an image generator produced only men for "lawyers" (p. 13).
- **Explainability:** we usually do not know how or on what information deep systems decide. Local explanations of single decisions are "moderately successful". Whether fully transparent complex systems are possible remains unknown (p. 13).
- **Weaponizing AI:** all significant technologies have been applied directly or indirectly toward war. The author says AI will "doubtless" be deployed militarily, and this is already happening (p. 13).
- **Concentrating power:** companies invest for profit. Deep learning is likely to concentrate power in the few organizations that control it. Job automation will disproportionately affect lower-paid, lower-skilled workers. Optimists cite the industrial revolution; the author says we simply do not know the effects (p. 14).
- **Existential risk:** the major existential risks all come from technology (the author cites climate change, nuclear weapons and pandemics). AI adds new ones, and we should be very cautious about building systems more capable and extensible than human beings. In the most optimistic case it puts vast power in its owners' hands; in the most pessimistic we cannot control it or understand its motives (p. 14).

The list is "far from exhaustive": surveillance, disinformation, privacy violations, fraud, market manipulation, and training energy use also matter. The concerns are not speculative, and internet history shows technology can cause unexpected harm (p. 14). The author urges readers to ask how far scientists are accountable for uses of their work, to note that capitalism drives AI development while law and social-good deployment probably lag, and to check whether employers do real ethics work or only "ethics-washing" (p. 14).

### 1.5 Structure of the book (p. 15)
- Ch. 2–9: the supervised pipeline (shallow and deep networks, training, measuring and improving performance).
- Ch. 10–13: architectural variations (convolutional networks, residual connections, transformers), used across all three areas.
- Ch. 14–18: unsupervised learning, with a chapter each on four deep generative models: GANs, VAEs, normalizing flows, diffusion models.
- Ch. 19: brief deep reinforcement learning.
- Ch. 20: open questions (why are deep nets easy to train, why do they generalize, why so large, must they be deep?). Along the way the book explores phenomena such as the structure of the loss function, double descent, grokking and lottery tickets.
- Ch. 21: ethics (p. 15).

### 1.6 Other books (p. 15–16)
The author names Goodfellow et al. (2016) as the book this one succeeds in spirit. He also names Murphy, Bishop, his own earlier Prince (2012), and texts on graphical models, Gaussian processes, maths, coding, vision, graph networks and reinforcement learning (p. 15–16).

### 1.7 How to read this book (p. 16)
Chapters have a main body (self-contained), notes (references, history, further reading, less self-contained) and problems (starred ones have answers online). Notation is in appendix A. Python notebooks are on the website. The author says he tries to make clear where phenomena are poorly understood and when his explanations "should be treated with caution" (p. 16).

## Toy example (ours, not from the text)
Family of "models": $y = 80 + b\,x$, with $x$ = age in years, $y$ = height in cm, and $b \in \{2,4,6\}$. Training pairs: $(2,90),(5,100),(10,120)$. Fit quality is measured by sum of absolute errors (my choice for illustration; the chapter gives no error measure).
- $b=2$: predictions $84, 90, 100$; errors $6, 10, 20$; sum $=36$.
- $b=4$: predictions $88, 100, 120$; errors $2, 0, 0$; sum $=2$.
- $b=6$: predictions $92, 110, 140$; errors $2, 10, 20$; sum $=32$.

Training picks $b=4$. The trained model predicts for age 8: $80 + 4\cdot 8 = 112$ cm. This is the p. 5 idea: a family of curves, training data, search for the best-fitting member.

## Concepts
- [[supervised-learning]] (new) — learn an input→output mapping from labelled input/output pairs (p. 1, 5)
- [[unsupervised-learning]] (new) — build a model from inputs without output labels, to describe the data's structure (p. 7)
- [[reinforcement-learning]] (new) — an agent chooses actions to get high average reward (p. 11)
- [[regression-classification]] (new) — continuous-number outputs versus category-probability outputs (p. 2)
- [[deep-neural-network]] (new) — equation family, broad and easy to search, fitted to data (p. 5)
- [[generative-model]] (new) — model that synthesizes new examples statistically indistinguishable from the training data (p. 7)
- [[latent-variable]] (new) — a few underlying variables, with a simple distribution, that a network maps to data (p. 9)
- [[structured-output]] (new) — output with internal "grammar" and possibly many valid answers (p. 7)
- [[temporal-credit-assignment]] (new) — linking a delayed reward to the earlier actions that caused it (p. 12)
- [[exploration-exploitation]] (new) — trade-off between using known strategies and trying new actions (p. 12)
- [[policy-network]] (new) — deep network mapping the observed state to an action (p. 12)
- [[language-model]] — here only (the text says "generative model of text data"; the term "language model" does not appear): a model that assigns a probability to every output string and can be sampled; no next-token factoring is given (p. 8)

## Canonical instances
- [[house-price-regression]] — a regression example with tabular input (p. 2)
- [[review-sentiment-classification]] — binary classification of text with variable length (p. 2–3)
- [[child-height-curve]] — model as a family of curves, fitted to training points (p. 4–5)
- [[gpt3-text-completion]] — conditional text synthesis (fig. 1.8) (p. 9)
- [[face-latent-variables]] — roughly 42 face muscles; most variation in images of one person in the same lighting can be described with just 42 numbers (fig. 1.9 caption) (p. 9)
- [[image-interpolation]] — interpolating latent variables between two real images (p. 10)
- [[chess-policy-network]] — board state → move; extreme credit assignment (p. 12–13)

## Bridges (candidates)
- [structural-analogy] Conditional text completion (p. 7, 9) ↔ llm: prompting an LM and sampling the most likely continuation — both generate the "missing" part of a document.
- [metaphor] The author's remark that text models know only language statistics (p. 7) ↔ llm: form vs. meaning — a related worry; this unit does not use that framing.
- [structural-analogy] Policy network (p. 12–13) ↔ llm: RLHF policy optimized for reward — both map a state/context to actions under a reward signal (canon link; not stated in this unit).
- [metaphor] Latent-variable interpolation (p. 10) ↔ llm: embedding geometry — moving between points in a learned low-dimensional space.

## Questions this raises
- How does a network "search the family" of equations efficiently (training, loss, optimization)?
- What does "statistically indistinguishable" mean, and how is it measured for text or images?
- Is the claim that text models only know statistics (p. 7) testable, and what would count as evidence for understanding?
- How can credit assignment be handled when rewards are rare, as in chess?

## Reading notes
- Printed page = pdf − 14. Page labels gave printed numbers.
- Odd-numbered pages carry the footer "Draft: please send errata"; even-numbered pages carry the CC-BY-NC-ND license line.
- Figures were checked in the images (fig. 1.2 output vectors, fig. 1.3 curve, fig. 1.9 caption). Only their captions and the author's discussion are digested.
- Ch. 14–18 span five chapters, but the text says "a chapter each" for four models (p. 15). It gives no further breakdown.
- The chapter has no exercises.

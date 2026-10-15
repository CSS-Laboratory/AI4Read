---
id: loss-function
type: concept
fields: [information-theory, linear-algebra, llm, control-theory, political-science]
n_sources: 9
tiers: [core, reference, deep]
grounding: digests
sources: [boyd-2018-vmls/ch18-nonlinear, deisenroth-2020-mml/ch08-when, grimmer-2022-textasdata/ch19-classifying, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, mackay-2003-information/ch36-decision, prince-2023-udl/ch02-supervised, prince-2023-udl/ch05-loss, sarkka-2023-bayesianfiltering/ch02-bayesian]
generated_by: build_kg.py
---

# loss-function

## Definitions in the sources

### information-theory

- [[jaynes-2003-probability/ch13-decision]] (pp. 400, 407): numbers L(D_i, θ_j) for the cost of decision D_i under state θ_j; equals −utility [new]
- [[jaynes-2003-probability/ch14-simple]] (p. 431): $L(D,S)$, the judged seriousness of deciding $D$ when $S$ is present; a loss matrix when discrete [new]
- [[mackay-2003-information/ch36-decision]] (p. 451): the negative-side alternative: minimize expected loss instead [new]

### linear-algebra

- [[boyd-2018-vmls/ch18-nonlinear]] (p. 402): $\ell(u,y)$ rating the continuous prediction $u$ against outcome $y$ [new]
- [[deisenroth-2020-mml/ch08-when]] (p. 260): ℓ(y, ŷ), a non-negative error for one prediction [new]

### llm

- [[prince-2023-udl/ch02-supervised]] (p. 18): scalar measuring mismatch between predictions and training outputs, a function of $\phi$ [new]
- [[prince-2023-udl/ch05-loss]] (p. 56): one number measuring mismatch between model outputs and training targets; training minimizes it [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (p. 21): $C(\theta,a)$; the natural choice is the action minimising posterior expected loss [new]

### political-science

- [[grimmer-2022-textasdata/ch19-classifying]] (pp. 318, 326): the quantity minimized to fit parameters, e.g. squared error or cross-entropy (pp. 318, 326) (new)

## Instances that use it

- [[hurricane-evacuation-loss]] — an asymmetric loss function — from [[mcelreath-2020-rethinking/ch03-sampling]]

## Candidate bridges

- [metaphor] priors vs loss functions in social conflict ↔ economics: gains from trade between agents with different valuations. — from [[jaynes-2003-probability/ch13-decision]] (information-theory → economics-finance)
- [structural-analogy] Loss aversion (steeper loss slope) ↔ asymmetric loss functions in statistics: errors in one direction cost more than in the other. — from [[kahneman-2011-thinking/ch26-prospect]] (decision-game-theory → other)
- [structural-analogy] Liapunov function / gradient potential ↔ optimisation: a loss function that decreases along update steps rules out cycling — both use a strictly decreasing quantity to forbid loops. — from [[strogatz-2024-nonlinear/ch07-limit-p1]] (complex-systems → other)

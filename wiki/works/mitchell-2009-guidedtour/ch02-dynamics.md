---
id: mitchell-2009-guidedtour/ch02-dynamics
work: mitchell-2009-guidedtour
unit: Chapter 2 — Dynamics, Chaos, and Prediction
pages: pdf 33–62 (printed page numbers not visible)
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Dynamics, Chaos, and Prediction

## L0 — One line
Simple deterministic rules, such as the one-line logistic map, can produce behaviour that is impossible to predict in detail over the long term, yet this chaos has universal features that are predictable.

## L1 — The gist (≤ 120 words)
The chapter asks what dynamical systems theory (the study of systems that change over time) can say about prediction. Newton's laws suggested a clockwork universe in which everything could be predicted. Mitchell uses the logistic map, a one-line nonlinear equation, to show that deterministic rules can give behaviour that looks random. In the chaotic regime, tiny errors in the starting value grow, so long-term prediction fails even in principle. Yet chaos has order: the period-doubling route to chaos (a similar route for all one-hump maps) and Feigenbaum's constant (about 4.669, the same for all of them) are universal features. Detailed prediction fails, but some higher-level aspects stay predictable.

**Prerequisites:** repeating a calculation step by step (iteration); reading simple graphs; decimals and ratios. No calculus is needed.

## L2 — Key ideas
- Newtonian mechanics led Laplace to claim that complete prediction is possible in principle (pdf 38). Quantum uncertainty and chaos together showed it is not (pdf 38–39).
- Chaos means sensitive dependence on initial conditions: tiny measurement errors grow into huge long-term prediction errors (pdf 39). Poincaré found the possibility of it while working on the three-body problem (pdf 40).
- Nonlinearity is the key property: in a nonlinear system the whole differs from the sum of its parts (pdf 42). The rabbit examples contrast linear doubling with logistic growth (pdf 44–47).
- The logistic map $x_{t+1}=Rx_t(1-x_t)$ gives fixed points, then periodic oscillations, then chaos as $R$ grows (pdf 48–54). These final behaviours (a fixed point that never changes once reached, or an oscillation that repeats) are called attractors (pdf 50, 54).
- Chaotic behaviour from a deterministic rule looks random, and prediction fails beyond some time however precise the start (pdf 54–55).
- Universal features of chaos: the period-doubling route (the period of the final oscillation doubles as $R$ grows, until chaos) (pdf 56–57) and Feigenbaum's constant ≈ 4.6692016, the rate at which successive doublings come closer together (pdf 59). The constant is the same for all one-hump (unimodal) maps and has been confirmed in experiments (pdf 59–60).
- Prediction of fine detail fails, but some higher-level aspects of chaotic systems remain predictable (pdf 62). "Idea models" such as the logistic map are simple but capture fundamental properties (pdf 62).

## L3 — Walkthrough

### Introduction and early roots (pdf 33–38)
- Dynamical systems theory describes and predicts systems whose complex changing behaviour at the macroscopic (large-scale) level emerges from many interacting components (pdf 33). Examples: solar system, heart, brain, stock market, population, climate (pdf 33–34). It describes how systems can change, what macroscopic behaviours are possible, and what predictions can be made (pdf 34).
- **Aristotle** (view later refuted): earthly motion differs from heavenly motion. On Earth objects move in straight lines, and only when forced. In the heavens objects move in perfect circles around the Earth. Earthly objects move according to their composition, so, presumably, heavier objects (with more earth) fall faster (pdf 34). His method was logic and common sense, not experiment (pdf 35).
- **Copernicus, Kepler, Galileo:** Copernicus put the sun at the centre of planetary motion. Kepler found the orbits are elliptical, and found laws for them. Galileo experimented on Earth (pendula, inclined planes, falling objects) (pdf 35–36). His results contradicted Aristotle: force is needed to stop a moving object, and heavy and light objects fall equally fast in a vacuum. Earthly laws could explain some heavenly motion (pdf 36).
- **Newton** "can be said to have invented, on his own" the science of dynamics, and had to invent calculus along the way (pdf 36). Mechanics has two parts. Kinematics describes how things move (Kepler's laws are an example). Dynamics explains why, using force and mass (pdf 37).
- Newton's three laws: (1) an object subject to no force moves with unchanging speed. (2) The change in motion under a force is inversely proportional to mass. (3) If A exerts a force on B, then B exerts an equal and opposite force on A (pdf 37).
- Newton applied the laws to the planets too. Elliptical orbits need a force, gravity. His universal gravity law says the force is proportional to the product of the masses divided by the square of their distance (pdf 38).
- The result was a "clockwork universe". **Laplace** (1814) asserted that, given the laws and the position and velocity of every particle, everything could be predicted in principle (pdf 38). With electronic computers in the 1940s the "in principle" might have seemed closer to "in practice" (pdf 38).

*Intuition note:* If the universe obeys exact laws and you know the starting state exactly, the future could in principle be predicted exactly (Laplace's claim). The rest of the chapter asks whether "knowing exactly" is possible and whether it is enough.

### Revised views of prediction (pdf 38–41)
- Two twentieth-century discoveries ended Laplace's dream "even in principle". One is Heisenberg's 1927 uncertainty principle: position and momentum cannot both be measured exactly. The more certain one is, the less certain the other (pdf 38). Its effects exist only in the quantum world of tiny particles, and most people viewed it as a curiosity with little implication for prediction at larger scales (pdf 39).
- The other is chaos. In chaotic systems, minuscule uncertainty in the initial position and momentum can cause huge errors in long-term predictions. This is "sensitive dependence on initial conditions" (pdf 39).
- In other systems small uncertainties do not matter. Astronomers predict eclipses almost perfectly despite relatively large uncertainty in planet positions (pdf 39). In chaotic systems (hurricanes "may well be an example") any error, however small, makes long-term prediction vastly inaccurate (pdf 39). Chaos is observed in cardiac disorders, fluid turbulence, electronic circuits and dripping faucets (pdf 39).
- Maxwell (1873) hypothesised that influences too small to measure "may produce results of the highest importance" (pdf 39).
- **Poincaré** possibly gave the first clear example (the text says it is hard to pin down who first realised such systems might exist, pdf 39), in the three-body problem. This asks for the long-term motion of three masses attracting each other under Newton's laws. Newton had solved the two-body problem (pdf 39–40). Poincaré worked on it in 1887 for a prize contest on the many-body problem, which was inspired by the question of whether the solar system is stable (pdf 40).
- He did not fully solve it but won the prize anyway. He invented algebraic topology (an extended form of geometry), and in looking at the geometric consequences of the three-body problem he discovered the possibility of sensitive dependence (pdf 40).
- **Poincaré's view:** even with perfectly known laws we know the initial situation only approximately. If an approximate start gives an approximate prediction, that is all we require. But he says "it is not always so": "it may happen" that small initial differences produce very great final ones, and then "prediction becomes impossible" (pdf 40–41).
- The phenomenon was seen as significant only after electronic computers. Poincaré had guessed it would stymie long-term weather prediction. In 1963 Lorenz found sensitive dependence in simple computer weather models (pdf 41).
- Modern weather predictions are at best reasonably accurate only to about one week. It is not known whether this limit comes from fundamental chaos, or how far it can be extended with more data and better models (pdf 41).

*Intuition note:* Knowing the laws is not enough; you also need the starting values. In a chaotic system, any rounding in those values eventually destroys the forecast.

### Linear versus nonlinear rabbits (pdf 42–47)
- A **linear** system can be understood by understanding its parts and adding them. Flour (2 cups) plus sugar (1 cup) gives 3 cups. In a **nonlinear** system the whole differs from the sum of the parts. Baking soda (2 cups) plus vinegar (1 cup) fizzes into more than 3 cups, because the parts interact (pdf 42).
- **Linear rabbits:** each year all rabbits pair up, and each pair has exactly four offspring and then dies. The population doubles every year without limit (pdf 42–44). Splitting 4 rabbits into 2 + 2 on two islands gives the same total after each year as keeping them together (pdf 44). Plotting next year's population against this year's gives a straight line (pdf 44–45).
- **Nonlinear rabbits** use the logistic model, which includes death from overcrowding (pdf 44). Inputs are the current population, birth rate, death rate (probability of dying from overcrowding) and carrying capacity (maximum population the habitat supports). The chapter does not give the equation; the author says it is given in the notes. Its plot is a parabola (pdf 45–46).
- Examples with birth rate 2, start at 20 rabbits (pdf 45–46):
  - death rate 0.4, capacity 32: 20 → 12 → 12, and the population stays at 12.
  - death rate 0.1, capacity 32: generation 2 has 14.25 and generation 3 has 15.01816.
  - death rate 0.4, capacity 64: by year nine the population is close to 24 and stays there.
- Fractional rabbits are allowed because the model is mathematical (pdf 46). Repeating the calculation from the previous result is called "iterating the model" (pdf 46).
- Non-additivity (pdf 47): 20 rabbits become 12 at year one. But two islands of 10 rabbits each have 11 + 11 = 22 rabbits. The whole is not the sum of the parts.

*Intuition note:* Overcrowding is an interaction among the rabbits. It is why the logistic rule is nonlinear and why splitting a population changes the total.

### The logistic map (pdf 48–55)
- Simplified version: birth and death rates are merged into one number $R$. Population becomes $x$, the fraction of carrying capacity (pdf 48).
$$x_{t+1}=R\,x_t\,(1-x_t)$$
- It is one of the simplest systems to show sensitive dependence. May brought it to biologists' attention in a 1971 *Nature* article. Feigenbaum used it in the 1980s to show universal properties (pdf 48).
- **R = 2:** with $x_0=0.5$, $x$ stays 0.5. With $x_0=0.2$ the trajectory is 0.32, 0.4352, 0.4916019, 0.4998589, then 0.5 (pdf 49–50). Starting at 0.99 also ends at 0.5, by a longer route (pdf 50). A fixed point is a value that, once reached, never changes. For $R=2.5$ the fixed point is 0.6 (pdf 50).
- **R = 3.1** (start 0.2): $x$ settles into an oscillation between 0.5580141 and 0.7645665, whatever $x_0$ is. Fixed points and oscillations are both "attractors": regular final behaviour to which initial conditions are drawn (pdf 50). Up to about $R=3.4$ the final oscillation has period 2 (pdf 52).
- Between $R=3.4$ and $3.5$ the period becomes 4. At $R=3.49$ the values are about 0.872, 0.389, 0.829, 0.494 (pdf 52). Further doublings (pdf 52–53):

| Period | Between R values |
|---|---|
| 8 | 3.54 and 3.55 |
| 16 | 3.564 and 3.565 |
| 32 | 3.5687 and 3.5688 |

- The doublings come after ever smaller increases in $R$, until the period is effectively infinite at $R\approx3.569946$ (pdf 53). Before that, long-term behaviour is roughly predictable from $R$: fixed points for $R$ below about 3.1, period 2 between 3.1 and 3.4, and so on (pdf 53).
- At that $R$ the behaviour becomes **chaotic**. The author calls the series $x_0,x_1,\dots$ a *trajectory*. In chaos, trajectories from very similar $x_0$ progressively diverge (pdf 53).
- With $R=4.0$, $x_0=0.2$ against $x_0=0.2000000001$: they look identical at first, diverge significantly after about 30 iterations, and soon are uncorrelated (pdf 53–54).
- Three attractor classes so far: fixed-point, periodic and chaotic. Chaotic attractors are also called "strange attractors" (pdf 54).
- The map is deterministic: each $x_t$ gives exactly one $x_{t+1}$. Yet chaotic trajectories look random, enough that the map has been used to generate pseudo-random numbers (pdf 54). For any $R$ that yields chaos, uncertainty in any decimal place of $x_0$, however far out, causes unpredictability at some $t$ (pdf 54).
- **May's view:** erratic census fluctuations in an animal population need not come from environment or sampling error. They may come from a rigidly deterministic rule. In the chaotic regime, even with exactly known parameters, long-term prediction is impossible (May, pdf 55).
- Mitchell's conclusion: the presence of chaos in a system implies that perfect Laplacian prediction is impossible in principle as well as in practice, since we can never know $x_0$ to infinitely many decimals (pdf 55).

*Intuition note:* The map has no randomness in it. The unpredictability comes from the fact that, in the chaotic regime, small differences in the starting value grow as the map is iterated until they are large.

### Universals in chaos (pdf 55–61)
- "Chaos" was named by physicists Li and Yorke. Unlike colloquial chaos, mathematical chaos contains order in the form of universal features shared by a wide range of chaotic systems (pdf 55–56).

**First universal feature: the period-doubling route (pdf 56–57)**
- Increasing $R$ from 2.0 to 4.0 gives a fixed point, then periods 2, 4, 8 and so on until chaos. Each abrupt doubling is a **bifurcation** (pdf 56).
- A bifurcation diagram plots the attractor against a "control parameter" such as $R$. For $R=2.9$ the fixed point is $x=0.655$. At $R=3.0$ a period-two attractor appears, and the diagram shows period four between 3.4 and 3.5 (pdf 56).
- History: period doubling was seen in equations in the 1920s, and Myrberg described a cascade in the 1950s. Metropolis, Stein and Stein showed that any one-hump ("unimodal") map follows a similar route (pdf 57).

**Second universal feature: Feigenbaum's constant (pdf 57–61)**
- Feigenbaum computed the $R$ values of the doublings (pdf 58):

| $R_1$ | $R_2$ | $R_3$ | $R_4$ | $R_5$ | $R_6$ | $R_7$ | $R_8$ | $R_\infty$ |
|---|---|---|---|---|---|---|---|---|
| 3.0 | 3.44949 | 3.54409 | 3.564407 | 3.568759 | 3.569692 | 3.569891 | 3.569934 | 3.569946 |

- $R_n$ corresponds to period $2^n$. $R_\infty$ marks the onset of chaos, a trajectory of infinite period (pdf 58–59).
- The bifurcations get closer together. He measured the rate at which the $R$ values converge and found it is approximately 4.6692016. Each new doubling occurs about 4.6692016 times faster than the previous one (pdf 59).
- He then computed the rate for the sine map, a similar map using the sine function, and found the same value. Other unimodal maps gave it too. Nobody, Feigenbaum included, had expected this (pdf 59).
- He developed a theory explaining why the constant is universal, meaning here "the same for all unimodal maps". It uses renormalization, a technique from quantum field theory that had been imported into the study of phase transitions and critical phenomena (pdf 59).
- The theory has been verified in experiments on fluid flow, electronic circuits, lasers and chemical reactions. Measured values agree with 4.6692016 within the margin of error (pdf 60). Kadanoff: "the best thing that can happen to a scientist" is when something in the mind matches something in nature (pdf 60).
- Large systems such as the weather are too hard to test directly, so no one has directly observed period doubling or chaos there. Certain computer models of weather, and models of power systems, the heart and solar variability, have shown the route (pdf 60–61).
- Coullet and Tresser independently found the same result, also with renormalization. Feigenbaum may have been first and spread it more widely, so he gets most credit. Technical papers sometimes say "Feigenbaum-Coullet-Tresser" (pdf 61).

*Intuition note:* The rate at which the $R_n$ bunch up, with each doubling coming about 4.67 times sooner than the last, is the same for all unimodal maps (pdf 59).

### Revolutionary ideas from chaos (pdf 61–62)
- Seemingly random behaviour can emerge from deterministic systems with no external randomness (pdf 61).
- Some simple deterministic systems cannot be predicted in the long term, even in principle (pdf 61).
- There is "order in chaos" in universal properties such as the period-doubling route and Feigenbaum's constant. So some higher-level aspects of chaotic systems are predictable even though detail is not (pdf 62).
- The chapter's summary: changing, hard-to-predict macroscopic behaviour is a hallmark of complex systems (pdf 62). Dynamical systems theory gives complex-systems researchers a vocabulary of bifurcations, attractors and universal properties (pdf 62).
- The logistic map illustrates "idea models": models simple enough to study by mathematics or computer that still capture fundamental properties of natural complex systems (pdf 62). Dynamics is only one step. Later chapters connect it to information processing and adaptation (pdf 62).

## Toy example (ours, not from the text)
**Sensitive dependence at $R=4$.** Iterate $x_{t+1}=4x_t(1-x_t)$ from two close starts:

| t | start 0.20 | start 0.21 | gap |
|---|---|---|---|
| 0 | 0.2 | 0.21 | 0.01 |
| 1 | 4·0.2·0.8 = 0.64 | 4·0.21·0.79 = 0.6636 | 0.0236 |
| 2 | 4·0.64·0.36 = 0.9216 | 4·0.6636·0.3364 = 0.89294 | 0.0287 |
| 3 | 4·0.9216·0.0784 = 0.28901 | 4·0.89294·0.10706 = 0.38239 | 0.0934 |

A gap of 0.01 becomes about 0.09 in three steps, and it keeps growing until the trajectories are unrelated. The same logic with an error of $10^{-10}$ takes about 30 steps (pdf 54).

**Feigenbaum ratio from the printed table (pdf 58).** Gaps between successive $R$ values are $3.44949-3.0=0.44949$, $3.54409-3.44949=0.09460$, $3.564407-3.54409=0.020317$, and $3.568759-3.564407=0.004352$. Ratios of successive gaps are $0.44949/0.09460\approx4.75$, $0.09460/0.020317\approx4.66$ and $0.020317/0.004352\approx4.67$. These approach 4.6692016.

## Concepts
- [[complex system]] — a system whose hallmark is changing, hard-to-predict macroscopic behaviour; dynamical systems theory studies such behaviour emerging from many interacting components (pdf 33, 62)
- [[nonlinearity]] — the whole differs from the sum of the parts, because parts interact (pdf 42)
- [[fixed point and stability]] — a value that, once reached, never changes, e.g. 0.5 at $R=2$ (pdf 50)
- [[attractor / basin of attraction]] — regular final behaviour (fixed point or oscillation) that initial conditions are "attracted to" (pdf 50). Only the attractor half is covered here.
- [[strange attractor / fractal]] — here only "chaotic attractors are sometimes called strange attractors"; no fractal discussion (pdf 54)
- [[bifurcation]] — an abrupt period doubling as the control parameter changes (pdf 56)
- [[period-doubling route to chaos]] — successive bifurcations, periods 2, 4, 8, …, ending in chaos (pdf 56)
- [[deterministic chaos]] — sensitive dependence on initial conditions in a deterministic system, which looks random (pdf 39, 54)
- [[universality]] — here, the same for all unimodal maps (Feigenbaum's constant) (pdf 59)
- [[sensitive-dependence-on-initial-conditions]] (new) — tiny initial differences grow into large long-term differences (pdf 39)
- [[idea-model]] (new) — a model simple enough to study mathematically that captures fundamental properties of complex systems (pdf 62)
- [[unimodal-map]] (new) — a map whose graph has a single hump (parabola-like) (pdf 57)

## Canonical instances
- [[logistic-map]] (new) — $x_{t+1}=Rx_t(1-x_t)$ shows fixed point, periodic and chaotic attractors (pdf 48–54)
- [[rabbit-population-models]] (new) — doubling rabbits are linear; logistic rabbits are nonlinear (pdf 42–47)
- [[three-body-problem]] (new) — Poincaré's context for discovering sensitive dependence (pdf 40)
- [[weather-prediction-limit]] (new) — Lorenz's models; forecasts good to about one week (pdf 41)
- [[feigenbaum-constant]] (new) — ≈ 4.6692016, shared by unimodal maps and seen in experiments (pdf 59–60)

## Bridges (candidates)
- [structural-analogy] Renormalization in Feigenbaum's theory ↔ statistical physics: the same technique is used for phase transitions and critical phenomena (pdf 59).
- [structural-analogy] Logistic map as an "idea model" ↔ many-model thinking: simple models that isolate fundamental properties of complex systems (pdf 62).
- [metaphor] Laplace's clockwork universe ↔ computational social science: the hope that complete data enables complete prediction. The text speaks only of physical systems.

## Questions this raises
- If detailed prediction fails in chaotic systems, which higher-level quantities can still be predicted, and how reliably?
- How can one tell whether weather's one-week limit is fundamental chaos or just limited data and models (pdf 41)?
- Can irregular fluctuations in real data (as May suggests for animal censuses) be told apart from noise?
- Why would the same constant appear for unimodal maps of such different form?

## Reading notes
- No printed page numbers are visible in the text layer or images, so all citations are (pdf N).
- Equations in this chapter are few and clearly legible. The logistic model's own equation is not given in the chapter (it is in the book's notes), so it is not reproduced.
- Possible inconsistency in the source: fixed points are said to be reached when $R$ is below "about 3.1" (pdf 53), but the bifurcation diagram and the table put the first doubling at $R\approx3.0$ (pdf 56, 58).
- Pages 33–62 were read; the figure descriptions (2.1–2.2 population pictures, 2.7–2.8, 2.10) were not all inspected in image form.
- The Feigenbaum ratios in the toy example are our computation from the printed table, not stated in the text.

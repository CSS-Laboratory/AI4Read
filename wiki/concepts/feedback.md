---
id: feedback
type: concept
curated: 2026-10-15
fields: [control-theory, complex-systems, communication-theory, political-science, economics-finance, information-theory]
level: HS
grounding: digests
aliases: [feedback-positive-negative, feedback-loop]
sources: [ashby-1956-cybernetics/ch04-machine, ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch09-transfer-p1, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch05-system, kalman-1960-filtering/main, welch-2004-kalmanintro/main, taylor-1993-discretion/main, wlezien-1995-thermostat/main, mitchell-2009-guidedtour/ch12-information, mitchell-2009-guidedtour/ch16-applying, scheffer-2009-earlywarning/main, schelling-1971-segregation/main-p1, schelling-1971-segregation/main-p2, simon-1962-architecture/main, craig-1999-field/main-p2, habermas-1989-publicsphere/ch07-concept, hall-1973-encoding/main, carey-1989-cultural/ch07-history, carey-1989-cultural/ch08-technology, rogers-2003-diffusion/ch10-innovation, grimmer-2022-textasdata/ch23-prediction, minsky-1992-instability/main, kahneman-2011-thinking/ch13-availability, pierce-1980-introduction/ch11-cybernetics, lippmann-1922-publicopinion/ch26-intelligence]
links: [negative-feedback, positive-feedback, feedforward, homeostasis, state-feedback, open-loop-vs-closed-loop, reference-set-point, law-of-requisite-variety]
generated_version: wiki/kg/hub-sources/feedback.md
---

# Feedback

**Gist.** Feedback means that what a system does comes back, as information, to change what it does next — the output is measured and used to adjust the input, in a closed loop.

35 digests in six fields use this id (`feedback-positive-negative` and `feedback-loop` are merged in). The two signs have their own pages: [[negative-feedback]] (balancing) and [[positive-feedback]] (reinforcing).

## How each field uses it

### Control theory & cybernetics (home field)
- “circularity of action: each of two parts affects the other (p. 53); Ashby says the exact definition is unimportant” — [[ashby-1956-cybernetics/ch04-machine]] (p. 54)
- “two or more dynamical systems coupled so each influences the other; correction based on desired vs actual performance” — [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-1, 1-13)
- “here: a loop in which the controller input is $e=r-y$, the difference between reference and process output” — [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-1)
- “a closed chain of causation from a stock, through level-dependent decisions or rules, back to a flow into or out of that stock” — [[meadows-2008-thinking/ch01-basics]] (pp. 25, 27)
- “the optimal filter is a feedback system, from inspection of Fig. 3” — [[kalman-1960-filtering/main]] (p. 42)
- “author's "feedback rules": instrument settings respond to measured inflation, unemployment or output” (monetary policy) — [[taylor-1993-discretion/main]] (p. 198)

### Complex systems
- “in metabolism, a pathway's speed is regulated by chemicals it produces (e.g., ATP slowing glycolysis); the author also calls ant trail allocation feedback” — [[mitchell-2009-guidedtour/ch12-information]] (pp. 34, 39)
- “positive feedback drives citation growth and failure spread” — [[mitchell-2009-guidedtour/ch16-applying]] (pp. 123, 127)
- “positive feedback drives the system past the threshold toward a contrasting state” — [[scheffer-2009-earlywarning/main]] (p. 53)
- “each exit worsens the ratio for those who stay, producing cumulative evacuation” — [[schelling-1971-segregation/main-p2]] (p. 21)
- “selectivity equals feedback of information from the environment” — [[simon-1962-architecture/main]] (p. 473)

### Communication theory
- “in cybernetics, a process of perverse complexity and unpredictability; reduced to function in semiotic complaints” — [[craig-1999-field/main-p2]] (p. 142)
- “survey soundings returned to government to align the population with policy” — [[habermas-1989-publicsphere/ch07-concept]] (p. 243)
- “"skewed and structured" return of audience and societal input into production” — [[hall-1973-encoding/main]] (p. 3)

### Political science
- “policy outputs "feed back" on public inputs (Easton's model)” — [[wlezien-1995-thermostat/main]] (p. 981)
- “model-guided action produces data that confirms the model” — [[grimmer-2022-textasdata/ch23-prediction]] (p. 392)

## Bridges between fields

- **structural-analogy** (control theory → economics): “Feedback vs feedforward ↔ economics: market-based vs planned economy — the text itself draws the analogy (p. 1-4).” — [[astrom-2021-feedbacksystems/ch01-introduction]]. Justification: the authors' own comparison of correcting by measured results vs planning ahead.
- **structural-analogy** (control theory → economics/biology): “Feedback rule $G_1/(1+G_1G_2)$ ↔ economics/biology models of reinforcing and balancing loops: forward gain divided by one plus loop gain (a loop sign of $-1$ is built into the rule).” — [[astrom-2021-feedbacksystems/ch09-transfer-p1]]. Justification: one loop formula describes loops in any field.
- **structural-analogy** (information theory → control theory): “Feedback gain-stabilization ↔ control engineering: the output feeds back to cancel error, at the risk of instability.” — [[pierce-1980-introduction/ch11-cybernetics]]. Justification: Pierce's account of the amplifier is the control argument.
- **structural-analogy** (communication theory → control theory): “Telegraph as control of railroad ↔ Feedback (cybernetics): information steering a physical process; Carey himself links it to servo mechanisms and systems theory (p. 166).” — [[carey-1989-cultural/ch08-technology]]. Justification: the author makes the link.
- **structural-analogy** (communication theory → control theory): “performance gap as trigger ↔ cybernetics: feedback — a gap between goal and actual output prompts corrective action.” — [[rogers-2003-diffusion/ch10-innovation]]. Justification: organisations correct an error signal like a controller.
- **structural-analogy** (economics → complex systems): “Deviation-amplifying system ↔ complex systems: positive feedback — reactions reinforce, not damp, a movement.” — [[minsky-1992-instability/main]]. Justification: financial instability described as a reinforcing loop.
- **structural-analogy** (decision theory → complex systems): “availability cascade ↔ network science: positive-feedback information cascades — each round of attention raises the next.” — [[kahneman-2011-thinking/ch13-availability]]. Justification: same reinforcing shape in media attention.
- **structural-analogy** (political science → complex systems): “Policing feedback loops ↔ path dependence: early choices shape the data that reinforce them” — [[grimmer-2022-textasdata/ch23-prediction]]. Justification: a prediction model's actions generate its own future training data.
- **metaphor** (communication theory → control theory): “Agencies that hold up a mirror to institutions ↔ feedback: outputs shown back to those who produce them (§3, para 2).” — [[lippmann-1922-publicopinion/ch26-intelligence]]. Justification: no loop dynamics are modelled; an inspiring picture only.

## Where definitions disagree

- **Strict vs. loose definitions.** Åström & Murray define feedback by a measured error, “the controller input is $e=r-y$” — [[astrom-2021-feedbacksystems/ch02-feedback]]. Ashby uses mere circularity and says “the exact definition is unimportant” — [[ashby-1956-cybernetics/ch04-machine]].
- **Information or causation?** Ashby ch12: “information passing from E back to R” — [[ashby-1956-cybernetics/ch12-error]] (p. 223); Meadows: a chain of causation through stocks and flows (quote above).
- **Engineering concept vs. social metaphor.** Craig's digest records that in communication theory feedback is “reduced to function in semiotic complaints” — [[craig-1999-field/main-p2]]; Carey's history mentions it only inside a quotation: “appears in a quoted claim that "feedback" from society will become effective (Westin, p. 146); not developed by the authors” — [[carey-1989-cultural/ch07-history]]. Hall's return of audience input is “"skewed and structured"” — [[hall-1973-encoding/main]], not a corrective loop.
- **Good or bad?** In control and Meadows, missing feedback causes problems: “missing or weak feedback is the cause of the commons trap” — [[meadows-2008-thinking/ch05-system]] (p. 117). In Habermas, feedback steers citizens toward policy (quote above), and in Grimmer it confirms a model's own bias (quote above).
- **Sign.** Many complex-systems uses are positive (reinforcing) feedback (Mitchell, Scheffer, Schelling quotes); control texts mostly mean negative (balancing) feedback. The signs are separate ids: [[positive-feedback]], [[negative-feedback]].

## Digests

Control theory: [[ashby-1956-cybernetics/ch04-machine]], [[ashby-1956-cybernetics/ch12-error]], [[astrom-2021-feedbacksystems/ch01-introduction]], [[astrom-2021-feedbacksystems/ch02-feedback]], [[astrom-2021-feedbacksystems/ch09-transfer-p1]], [[meadows-2008-thinking/ch01-basics]], [[meadows-2008-thinking/ch05-system]], [[kalman-1960-filtering/main]], [[welch-2004-kalmanintro/main]], [[taylor-1993-discretion/main]], [[wlezien-1995-thermostat/main]] ·
Complex systems: [[mitchell-2009-guidedtour/ch12-information]], [[mitchell-2009-guidedtour/ch16-applying]], [[scheffer-2009-earlywarning/main]], [[schelling-1971-segregation/main-p1]], [[schelling-1971-segregation/main-p2]], [[simon-1962-architecture/main]] ·
Communication theory: [[craig-1999-field/main-p2]], [[habermas-1989-publicsphere/ch07-concept]], [[hall-1973-encoding/main]], [[carey-1989-cultural/ch07-history]], [[carey-1989-cultural/ch08-technology]], [[rogers-2003-diffusion/ch10-innovation]], [[lippmann-1922-publicopinion/ch26-intelligence]] ·
Political science: [[grimmer-2022-textasdata/ch23-prediction]] ·
Economics: [[minsky-1992-instability/main]] · Decision theory: [[kahneman-2011-thinking/ch13-availability]] · Information theory: [[pierce-1980-introduction/ch11-cybernetics]]

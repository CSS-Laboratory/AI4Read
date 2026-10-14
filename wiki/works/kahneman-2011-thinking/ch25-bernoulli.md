---
id: kahneman-2011-thinking/ch25-bernoulli
work: kahneman-2011-thinking
unit: "25 Bernoulli's Errors"
pages: pdf 261–269 (printed page numbers unknown)
fields: [decision-game-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Bernoulli's Errors

## L0 — One line
Bernoulli's utility-of-wealth theory explains risk aversion but wrongly judges outcomes by final wealth rather than by change from a reference point, a flaw that, Kahneman suggests, survived for so long because of "theory-induced blindness."

## L1 — The gist (≤ 120 words)
Kahneman recounts how he and his colleague Amos began studying choices between simple gambles, which led to prospect theory (a theory of how people actually choose). The chapter asks what was wrong with expected utility theory, the economists' rational-choice model. Bernoulli's idea was that people value outcomes by their utility, which rises more slowly than wealth, and this explains risk aversion (preferring sure things) and insurance. The flaw is that utility depends only on the final amount of wealth. Real people judge gains and losses relative to a reference point (Jack and Jill, Anthony and Betty). Kahneman blames "theory-induced blindness" for the flaw surviving for so long: once a theory is accepted, its faults are very hard to see.

**Prerequisites:** weighted averages (expected value); percentages; the idea of a logarithm as "equal ratios give equal steps."

## L2 — Key ideas
- Economists' agent ("Econ") is rational, selfish and has stable tastes; psychologists' "Humans" are not (pdf 261). Soon after, Amos suggested studying decision making as their next project.
- Simple gambles are a model system for decisions, since every significant choice in life comes with some uncertainty. Expected utility theory was meant as a logic of rational choice, not as psychology (pdf 261–262).
- Prospect theory is purely descriptive: its goal is to document and explain systematic violations of the axioms of rationality in choices between gambles. It modifies expected utility theory just enough to explain about a dozen observed facts, several of which contradict it (pdf 263).
- Fechner's psychophysics (the study of laws linking physical quantities to subjective experience) proposed that, for many dimensions, subjective intensity is logarithmic in physical intensity. Bernoulli applied this idea earlier to wealth (pdf 264).
- Bernoulli: value a gamble by the probability-weighted average of the utilities of outcomes, not of the dollar outcomes. Diminishing marginal utility of wealth (each extra unit of wealth adds less utility than the previous) then explains risk aversion and insurance (pdf 265–266).
- The flaw: utility is tied to the level of wealth and ignores reference points (the starting levels from which gains and losses are measured). It cannot explain Jack and Jill's different happiness despite equal wealth, nor Betty's risk seeking (it could explain Anthony's risk aversion) (pdf 266–268).
- Kahneman's own explanation for why a theory with obvious counterexamples survived so long is "theory-induced blindness" (pdf 268).

## L3 — Walkthrough

### Opening: Econs and Humans (pdf 261)
- In the early 1970s Amos handed Kahneman an essay by Bruno Frey. Its first sentence: the agent of economic theory is rational, selfish, and his tastes do not change. (pdf 261)
- Kahneman was astonished: to a psychologist, people are neither fully rational nor completely selfish, and their tastes are unstable. Thaler later called the two kinds of agent **Econs** and **Humans**. (pdf 261)
- Humans have a System 1 and are limited by the information available at the moment (WYSIATI), so they are less consistent than Econs. (pdf 261)
- Their question: what rules govern choices between simple gambles, and between gambles and sure things? (pdf 261)
- Simple gambles (e.g. "40% chance to win $300") are to decision researchers what the fruit fly is to geneticists. Even apparently sure outcomes are uncertain. (pdf 261–262)

### Expected utility theory (pdf 262)
- Expected utility theory is the foundation of the rational-agent model. It is a logic of choice built on axioms (elementary rules) of rationality, not a psychological model. (pdf 262)
- Example axiom: if you prefer an apple to a banana, you prefer a 10% chance of an apple to a 10% chance of a banana. (pdf 262)
- Von Neumann and Morgenstern derived their theory of rational choice between gambles from a few axioms. Economists used it both as a prescription and as a description of how Econs choose. (pdf 262)
- Kahneman and Amos set out to learn how Humans actually choose, assuming nothing about rationality. They invented problems and checked their own intuitive choices. Example: a 50% chance of $100 versus $46 for sure. Both would pick the sure thing. (pdf 262–263)
- When they agreed confidently, they believed, almost always correctly, that most people would share the preference. (pdf 263)

### Prospect theory and psychophysics (pdf 263–264)
- After five years they completed "Prospect Theory: An Analysis of Decision under Risk." It was closely modeled on utility theory but departed from it fundamentally. It was purely descriptive, aimed at documenting and explaining systematic violations of the axioms. (pdf 263)
- It was submitted to *Econometrica*; Kahneman says the venue mattered, since the identical paper in a psychological journal would likely have had little impact on economics. Two years later they published an account of framing effects in *Science*. (pdf 263)
- They had established about a dozen facts about risky choices, several in flat contradiction to expected utility theory, and built a theory that modified it just enough. (pdf 263)
- Their approach followed **psychophysics**, founded by Gustav Fechner. It relates a physical quantity (light energy, tone frequency, money) to its subjective experience (brightness, pitch, value). (pdf 263–264)
- Fechner proposed a logarithmic function for many dimensions. An increase of stimulus by a given factor always gives the same increment on the psychological scale. Example: if 10 → 100 units adds 4 psychological units, then 100 → 1,000 also adds 4. (pdf 264)

> **Intuition note:** In a logarithmic scale, equal ratios (not equal differences) feel equally big. Going from 10 to 100 feels like going from 100 to 1,000.

### Bernoulli's Error (pdf 264–268)
- **Bernoulli's utility of wealth.** A gift of 10 ducats has the same utility to someone with 100 ducats as 20 ducats has to someone with 200. We speak of percentage raises, and a 30% raise may feel similar to rich and poor. Response is inversely proportional to initial wealth, so utility is a logarithmic function of wealth. If this function is accurate, $100,000 → $1 million is the same psychological distance as $10 million → $100 million. (pdf 264)
- **Expected value** before Bernoulli: the probability-weighted average of outcomes, e.g. for 80% to win $100 and 20% to win $10: $0.8 \times 100 + 0.2 \times 10 = 82$. Almost everyone prefers $80 for sure over this gamble, so people do not value gambles by expected value. (pdf 264)
- **Risk aversion.** A risk-averse person picks a sure thing equal to expected value, and even a sure thing below it, paying a premium to avoid uncertainty. Bernoulli's explanation: people choose by the utilities of outcomes, so the value of a gamble is the average of the utilities, each weighted by its probability. (pdf 264–265)
- **Table 3** (wealth in millions → utility units): 1→10, 2→30, 3→48, 4→60, 5→70, 6→78, 7→84, 8→90, 9→96, 10→100. Adding 1 million to 1 million gives +20 points; adding it to 9 million gives +4. Bernoulli proposed that this diminishing marginal value of wealth is what explains risk aversion. (pdf 265)
- **Worked example.** Equal chances of 1 million or 7 million versus 4 million for certain. Expected wealth is 4 million for both. From 1 to 4 million utility rises by 50; from 4 to 7 million by only 24. (pdf 265)
  $$U(\text{gamble}) = \frac{10 + 84}{2} = 47, \qquad U(4\text{ million}) = 60.$$
  Since 60 > 47, this decision maker takes the sure thing. (pdf 265)
- **Insurance.** Bernoulli applied "moral expectation" to a merchant insuring a spice shipment, where 5 of 100 ships are usually lost. Losing 1 million costs 4 utility points (100 → 96) at 10 million, but 18 points (48 → 30) at 3 million. The poorer man happily pays a premium to transfer the risk to the richer. He also offered a solution to the St. Petersburg paradox (infinite expected value, yet people pay few ducats). His analysis is still current almost 300 years later. (pdf 266)

> **Intuition note:** An extra million matters less to someone already rich. So a sure amount can beat a gamble with the same average dollar payoff, because the gamble's bad outcome hurts more than its good outcome helps.

- **The flaw.** Kahneman says the theory is seriously flawed: errors of a theory are rarely found in what it asserts explicitly; they hide in what it ignores or tacitly assumes. (pdf 266)
- **Jack and Jill.** Today each has 5 million; yesterday Jack had 1 million and Jill 9 million. Bernoulli's theory says equal wealth means equal happiness, but Jack is elated and Jill despondent. Jack would be much happier than Jill even with 2 million to her 5. (pdf 266)
- Happiness is determined by the recent change relative to reference points (1 million for Jack, 9 million for Jill). **Reference dependence** is ubiquitous in perception: the same sound is loud after a whisper and faint after a roar, and a gray patch looks dark or light depending on its background. (pdf 266–267)
- **Anthony and Betty.** Anthony owns 1 million, Betty 4 million. Each chooses between equal chances of ending with 1 or 4 million, or 2 million for sure. In Bernoulli's account the choice is identical (same final-wealth options), so he predicts the same choice. That prediction is incorrect. (pdf 267)
- Kahneman's imagined thinking: for Anthony the sure thing doubles his wealth, while the gamble is equal chances to quadruple or gain nothing. For Betty the sure thing loses half her wealth, while the gamble is equal chances to lose three-quarters or lose nothing. (pdf 267)
- Anthony thinks of gains, Betty of losses. Betty is much more likely to gamble, "as others do when faced with very bad options". Bernoulli's model could explain Anthony's risk aversion but not Betty's risk seeking, a behavior often observed in entrepreneurs and generals when all their options are bad. (pdf 267–268)

> **Intuition note:** The same final wealth can feel like a win or a loss, depending on where you started. A theory that sees only final wealth cannot tell these apart.

### Theory-induced blindness (pdf 268)
- The mystery is how a theory with such obvious counterexamples survived. Kahneman can explain it only by a weakness of the scholarly mind that he has often observed in himself, which he calls **theory-induced blindness**. Once you accept a theory and use it as a tool, it is extraordinarily difficult to notice its flaws. (pdf 268)
- You assume that an observation that does not fit has a good explanation you are missing, and you trust the community of experts. Many scholars have surely thought of stories like these and casually noted that they did not fit utility theory, but did not pursue the idea to the point of saying that utility depends on the history of one's wealth, not only on present wealth. Daniel Gilbert: disbelieving is hard work, and System 2 is easily tired. (pdf 268)

### Speaking of Bernoulli's Errors (pdf 268–269)
- Sample remarks: a bonus that satisfied three years ago needs to be higher after a 20% raise; two candidates accept the same salary but differ in satisfaction because their reference points differ; in a divorce suit, the one who can only gain is risk averse and the one facing all-bad options takes the risk. (pdf 268–269)

## Toy example (ours, not from the text)
Let utility be $u(w)=\sqrt{w}$ (a diminishing-marginal-utility function we chose).

*Gamble versus sure thing.* Gamble: equal chances to end with 36 or 144. Sure thing: end with 90.
- Gamble utility: $\tfrac12\sqrt{36}+\tfrac12\sqrt{144} = \tfrac12(6)+\tfrac12(12) = 9$.
- Sure thing utility: $\sqrt{90}\approx 9.49 > 9$.
- Expected value of the gamble is $\tfrac12(36)+\tfrac12(144)=90$, the same as the sure amount. So this decision maker is risk averse, as in Bernoulli's account.

*Reference points.* Cara currently has 36, Dan has 144. Both face the same final-wealth options.
- Cara: sure thing is $90-36=+54$. Gamble is $+0$ or $+108$. Neither option can leave him below his starting point.
- Dan: sure thing is $90-144=-54$. Gamble is $-108$ or $0$. Neither option can leave him above his starting point.
- Bernoulli's utility depends only on final wealth, so it gives Cara and Dan identical utilities (9.49 versus 9) and predicts the same choice. By the chapter's argument, Dan is likelier to gamble than Cara, because his sure option is a certain loss.

## Concepts
- [[expected utility]] — value of a gamble as the probability-weighted average of the utilities of outcomes (Bernoulli's "moral expectation") (pdf 265–266)
- [[utility function]] — psychological value of wealth; here it rises with diminishing increments (Table 3) (pdf 265)
- [[risk aversion]] — preferring a sure thing to a gamble of equal or slightly higher expected value, which Bernoulli proposed is explained by diminishing marginal utility (pdf 265)
- [[reference dependence]] — outcomes are judged as changes from a reference point, not as final wealth (pdf 266)
- [[framing effect]] — large changes of preference that are sometimes caused by inconsequential wording changes (only mentioned, pdf 263)
- [[expected value]] (new) — probability-weighted average of dollar outcomes, used before Bernoulli (pdf 264)
- [[diminishing marginal utility]] (new) — each extra unit of wealth adds less utility than the previous (pdf 265)
- [[psychophysics]] (new) — study of laws linking physical quantities to subjective experience; Fechner's logarithmic proposal (pdf 263–264)
- [[theory-induced blindness]] (new) — difficulty of noticing flaws in a theory you have accepted and used (pdf 268)
- [[econs-and-humans]] (new) — Thaler's names for the rational agent of economic theory and the real person (pdf 261)

## Canonical instances
- [[jack-and-jill]] — equal wealth, opposite happiness because of different reference points (pdf 266)
- [[anthony-and-betty]] — same final-wealth options, a gain frame versus a loss frame; risk aversion versus risk seeking (pdf 267–268)
- [[bernoulli-insurance-example]] — a spice shipment insured; poorer pays premium to richer (pdf 266)
- [[st-petersburg-paradox]] — infinite expected value, small willingness to pay; mentioned only (pdf 266)
- [[coin-toss-vs-sure-46]] — intuitive choice of a sure $46 over a 50% chance of $100 (pdf 262–263)

## Bridges (candidates)
- [structural-analogy] Fechner's logarithmic law ↔ Bernoulli's log utility of wealth — both say equal ratios of the stimulus or wealth give equal psychological steps.
- [structural-analogy] Reference-dependent perception (loudness, gray patches) ↔ gains/losses relative to a reference point in choice — context sets the baseline for judgment.
- [metaphor] Theory-induced blindness ↔ the fruit fly as a model system: a model's simplifications can hide what it leaves out.

## Questions this raises
- How should a theory be built so that reference points are explicit? What does prospect theory change?
- Is risk seeking in the domain of losses (Betty) a general pattern, and how large is it?
- If Humans differ so much from Econs, can expected utility theory still serve as a prescriptive logic?
- How can a researcher guard against theory-induced blindness in their own field?

## Reading notes
- Printed page numbers are not visible or given, so all references use (pdf N).
- Parts of the text layer are garbled (pdf 262, 264, 266). The page image was available only for pdf 265, where Table 3 was checked: values match the text (e.g. 10+84 over 2 = 47; 60 for 4 million). I could not check the garbled stretch on pdf 264 against an image. It appears to introduce Bernoulli as an earlier seeker of a function linking utility to money, and I rely only on the readable continuation.
- Page 265's text says "94/2 = 47", which equals $(10+84)/2$. This is consistent with the table.
- The source passage does not name Bernoulli's first name or exact dates. I added none.

---
id: shepsle-2010-analyzing/ch02-rationality
work: shepsle-2010-analyzing
unit: "2 Rationality: The Model of Choice"
pages: 13-38
fields: [political-science]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Rationality: The Model of Choice

## L0 — One line
In Shepsle's model, a rational person has complete, transitive preferences and beliefs about how actions lead to outcomes, and picks the action that serves them best (under risk, the action with the highest expected utility).

## L1 — The gist (≤ 120 words)
Shepsle asks what "rational" must mean if political behavior is to be explained from a few simple premises. His answer: individuals are the basic unit. Each has preferences (wants) and beliefs (hunches about how actions produce outcomes). Preferences must be complete and transitive, so they form an ordering with a top. Under certainty, pick the action leading to the top outcome. Under risk, give outcomes utility numbers and pick the action with the largest expected utility. The assumptions are not claimed to be descriptively true. They are simplifications that make explanation possible. The same logic is meant to cover choices from career moves to national decisions.

**Prerequisites:** weighted averages and simple probabilities; set notation; ordering of real numbers ($>$, $=$).

## L2 — Key ideas
- Rationality here is not brilliance or omniscience. It means acting consistently on one's preferences and beliefs, which is called instrumental rationality (pp. 14, 17).
- Methodological individualism: the individual is the basic unit, and individuals have preferences and beliefs. Groups, classes, firms and states have no minds, so they cannot be said to have preferences or beliefs (pp. 17–18).
- Assumptions are judged by explanatory power, not descriptive accuracy. Economics is the model, and positive political theory aims to do the same for politics (pp. 19–20).
- Rational choice needs two properties of preference: comparability (completeness) and transitivity. Together they give an ordering with a top, and some relations (for example "is the father of") fail them (pp. 24–26).
- The author treats failures of comparability or transitivity as less a critique than a warning about where the model applies (puzzling choices, low stakes) (pp. 27–29).
- Most in this tradition treat rationality as maximizing: actors seek the top of their ordering. This is also the language used for politicians, legislators and bureaucrats (pp. 29–30).
- Beliefs link actions to outcomes. Certainty, risk and uncertainty differ in how well the chooser can assign probabilities. Under risk, rational choice maximizes expected utility (pp. 30–33).

## L3 — Walkthrough

**Opening (pp. 13–14).** The approach is "rational choice", also called formal political theory, positive political theory or political economy. Economists use rationality most, but nothing about it is distinctly economic (p. 13). Shepsle reserves "irrational" for something specific. Rational does not mean brilliant or all-knowing: modelled people are ordinary folks with wants and beliefs (p. 14).

**Preliminaries (pp. 14–18).**
- *Preferences* (wants) can come from survival needs, social learning, religion, morals, ideology, altruism or group identity. The model does not explain where they come from. They are givens and are assumed not to change much in the short run (pp. 14–15). Footnote 3 leaves room for change from learning, experience, persuasion or deliberation.
- "Self-interested" is used in a weak sense. People pursue what they regard as important, which can include family, friends, whales, trees or strangers (p. 15). Hindmoor is cited on this: most accept that some people are always self-interested and everyone sometimes is, but not that everyone always is (p. 15).
- Preferences are an interior world and are not written on a person's forehead and sometimes people are not all they seem, so we often have to make assumptions about them (p. 15).
- The external world holds uncertainty about how things work, about others' preferences and about random events. People choose an *instrument* (an available behavior), not the outcome directly (p. 16). If each instrument led directly to one outcome, the rational choice would be simple: pick the instrument leading to the best outcome (p. 16).
- *Beliefs* are hunches about how effective an instrument is for getting what one wants. They connect instruments to outcomes. Acting on both preferences and beliefs is *instrumental rationality* (pp. 16–17).
- Beliefs can change by learning. On the "steep" part of a learning curve, each experience revises views a lot. On the "flat" part, beliefs have settled (p. 17).
- A rational individual combines beliefs and preferences consistently (p. 17).
- *Methodological individualism*: the individual is the basic unit. Many sociological theories use groups, Marxist ones use classes, and most international relations theories use the nation-state. Groups and states have no minds, so they cannot be said to have preferences or beliefs (pp. 17–18).

**Motivation (pp. 18–20).**
- Economics is described (admittedly simplified) as four actors allocating what is theirs (Display 2.1, p. 19):

| Actor | Endowment | Objective |
|---|---|---|
| consumers | budget | contentment |
| producers | inputs | profits |
| workers | time | purchasing power / leisure |
| investors | wealth | long-run return |

- Shepsle admits these assumptions are flawed as description (consumers may care about more than consumption, etc.). Descriptive accuracy is not their purpose. The aim is to explain variation and regularities with a simple set of assumptions. The commitment is to explanation, not description (pp. 19–20).
- Economic knowledge is cumulative and logically integrated, unlike an encyclopedia of detail or wisdom (which is intuitive and often dies with its holder) (p. 20).
- The question for politics: can we start from simple premises and derive principles of political performance, outcomes and behavior? This is "a daunting challenge" and it motivates the book (p. 20).

*Intuition note.* A model is a deliberately simple machine. Its assumptions are judged by how much they explain, not by whether each one is literally true.

**The simple logic of preference and choice (pp. 20–29).**

*Case 2.1: Claire McCaskill (pp. 21–23).* After losing the 2004 Missouri governor race 48–51 to Matt Blunt, she could challenge Senator Jim Talent in 2006 or Blunt in 2008. Outcomes: $x$ = term as senator, $y$ = term as governor, $z$ = out of politics near-term (p. 22). Shepsle says we can be reasonably confident she preferred $x$ to $y$ and $y$ to $z$ (p. 22). She could not choose among outcomes directly. Her behavioral options were "run for senator," "run for governor" and "run for both"; Shepsle supposes she focused on the first two (p. 22).
- Run for Senate gives $x$ with probability $p$ and $z$ with $1-p$. Waiting to run for governor gives $y$ with probability $q$ and $z$ with $1-q$ (p. 22).
- Her decision depends on how much she prefers $x$ to $y$ and on $p$ versus $q$ (p. 22).
- (added step) In the expected-utility terms of p. 33, the comparison is $p\,u(x)+(1-p)\,u(z)$ against $q\,u(y)+(1-q)\,u(z)$.
- She ran for the Senate in 2006 and won, because her preference for $x$ over $y$ was reinforced by her belief about her chances. She feared Hillary Clinton would head the 2008 Democratic ticket and drag down Democrats in Missouri (p. 23).

*Notation (pp. 23–24).* Mr. $i$ has preferences over *alternatives* $x,y,z$. $xP_iy$ means $x$ is strictly better than $y$ for $i$. $xI_iy$ means $i$ is indifferent between them. A choice is rational if the chosen object is at least as good as any other available one. Equivalently, no available object is better (p. 24). Footnote 7 defines weak preference: $xR_iy$ means $xP_iy$ or $xI_iy$ ("at least as good as").

*Two properties (pp. 24–25).*
- **Property 1, comparability (completeness):** for any $x,y$, either $xP_iy$, or $yP_ix$, or $xI_iy$ (p. 24). Equivalently, $xR_iy$ or $yR_ix$ or both (fn. 8).
- **Property 2, transitivity:** if $xP_iy$ and $yP_iz$ then $xP_iz$. For indifference, $xI_iy$ and $yI_iz$ imply $xI_iz$ (p. 25). Footnote 9 adds that weak preference is transitive if $xR_iy$ and $yR_iz$ imply $xR_iz$.
- If both hold, $i$ has a *preference ordering*, and the rational choice is its top (p. 25). $P_i$ and $I_i$ behave like $>$ and $=$ on real numbers, so real numbers can be ordered by size (p. 25). McCaskill's preferences over $\{x,y,z\}$ were complete and transitive (p. 25).
- These orderings are personal: $P_i$ may differ from $P_j$ (p. 25).

*These properties are not empty (p. 26).* Some relations are transitive but not complete, some complete but not transitive, and some neither.
- "Is the brother of" on all males is transitive but not complete (fn. 10).
- "Is the father of" is neither complete nor transitive (fn. 12).
- Footnote 11 gives a complete but intransitive case: in 1992 Ms. $i$ prefers Clinton to Bush ($CP_iB$), Bush to Perot ($BP_iP$) and Perot to Clinton ($PP_iC$). Different criteria are triggered by different pairs: domestic policy for Clinton–Bush, foreign policy for Bush–Perot, character for Perot–Clinton. Intransitivity may arise when different criteria are used for different pairings (fn. 11).

*Defending comparability (p. 27).* The extreme case is *Sophie's Choice*: a concentration-camp prisoner may save one of her two children but must choose whom; otherwise both die. She does choose, even though she does not regard them as comparable. Failing to choose is also a choice with consequences. The real problem arises when the comparison does not make sense to the chooser. Example: asked in late 2007 or early 2008 about McCain versus Obama, many voters would say "don't know". Shepsle calls this "not a critique of rationality-based models so much as a warning label" about appropriate use (p. 27). A "don't know" could mean the comparison is loony or that the options are nearly indifferent. For prediction it may not matter, since a forced choice is likely random either way (fn. 13).

*Defending transitivity (pp. 28–29).* In psychology experiments with ten saline solutions or gray triangles, there are 45 pairs. Subjects eventually say bottle 2 is saltier than 9, 9 saltier than 7, and 7 saltier than 2, which violates transitivity (p. 28). Shepsle's reading is that this is also less a critique than a warning about the domain of use. When stakes are low, uncertainty high and the choice of little consequence, inconsistency is likely. When choices matter, people are likely to be more intent on consistency. Whether to assume transitivity is a judgment call for the investigator (pp. 28–29). The consistency required is demanding, but simplifying assumptions are needed for progress (p. 29). Footnote 14 compares it to perfectly spherical particles or frictionless planes: known to be false, yet essential to progress and later relaxed.

*Intuition note.* Completeness says you can always compare two options. Transitivity says your comparisons don't go in circles. Together they let you line options up and pick the top one.

**The maximization paradigm (pp. 29–30).** Comparability and transitivity yield an ordering, with ties allowed (p. 29). The existence of a top, and the sense to choose it, is why rationality is treated as maximizing. Instead of listing preferences one may state what the person is trying to maximize (pp. 29–30). Display 2.1 did this. In later political models, elected politicians maximize votes at the next election, legislators maximize pork and policy satisfaction for home constituents, and bureaucrats maximize budgets or turf (p. 30).

**Environmental uncertainty and beliefs (pp. 30–33).**
- Since people choose instruments, the definition is revised: a rational individual chooses the action he or she *believes* will lead to the best outcome (p. 30).
- A *belief* is a probability statement relating an action's effectiveness to various outcomes (p. 30).
- Three conditions (pp. 30–31):
  - **Certainty:** the chooser is highly confident what will happen (a politician running against a "sacrificial" opponent is near certain).
  - **Risk:** unsure, but with a clear sense of the possibilities and their likelihoods (McCaskill's run against Talent).
  - **Uncertainty:** in the chooser's mind the action–outcome link is so imprecise that it is not possible to assign likelihoods.
- *Example (p. 31).* Outcomes $x,y,z$; actions $A,B,C$; preference $x$ first, then $y$, then $z$.
  - Certainty: $A\to x$, $B\to z$, $C\to y$, so choose $A$.
  - Risk: $A$ gives a 50–50 chance of $x$ or $z$; $B$ a 50–50 chance of $y$ or $z$; $C$ an even chance of $x$, $y$ or $z$.
  - Uncertainty: no probabilities can be put on the outcomes.
- *Utility numbers (p. 32).* Assign $u(x),u(y),u(z)$ reflecting relative value. If $x$ is far better than $y$ and $z$, which are close: $u(x)=1,\ u(y)=0.2,\ u(z)=0$. If $x$ is barely first and $z$ trails badly: $u(x)=1,\ u(y)=0.9,\ u(z)=0$. Only relative values matter. It is typical to normalize the best to 1 and the worst to 0, but 100/0 or 1000/−1000 would do as well (fn. 15).
- *Beliefs as probabilities (pp. 32–33).* Action $A$ gives $Pr_A(x)=1/2$, $Pr_A(y)=0$, $Pr_A(z)=1/2$. Probabilities lie between 0 and 1 and sum to 1. This makes $A$ a *lottery*, written $A=(\tfrac12 x,\ 0\,y,\ \tfrac12 z)$ (p. 33).
- *Principle of Expected Utility (p. 33).* Rational choice under risk means choosing the best lottery:
$$EU(A)=Pr_A(x)\cdot u(x)+Pr_A(y)\cdot u(y)+Pr_A(z)\cdot u(z)$$
  This sums the utilities of possible outcomes, each weighted by its likelihood. The same is computed for $B$ and $C$. Rationality requires choosing the action that maximizes expected utility (p. 33).
- Under uncertainty it is hard to be rational if one is utterly confused. But many people have hunches about likelihoods and can be pushed to give them numbers. They can then be treated as if expected utility covered their behavior (p. 33). Footnote 16 notes that other theories handle decisions without probabilities, and they are not reviewed here.

*Intuition note.* Expected utility is a weighted average: multiply how much you like each result by how likely it is, then add. Pick the action with the biggest total.

**Conclusion (p. 34).** Six points:
1. The enterprise is to explain social and political events.
2. The individual is the basic building block.
3. Individuals are described briefly, by preferences and beliefs.
4. They are rational: they act on preferences over outcomes and beliefs about actions.
5. Acting rationally means ranking outcomes, assigning utilities if needed, computing expected utility and choosing the highest.
6. Perhaps most controversial: all rational political choices (careers, voters' candidates, war decisions, pizza toppings) rest on the same comparability-and-transitivity foundation.

Aristotle, Hobbes, Rousseau and others have suggested politics is special. Shepsle answers "Perhaps. Indeed, certainly this must be the case," but adds that rational choosing "bears characteristic markings" in all these contexts and so may be analyzed with the same framework (p. 34).

**Problems (pp. 35–37).** Six problems follow (see Exercises).

## Toy example (ours, not from the text)
Outcomes $x,y,z$ with preference $x$ first, $y$ second, $z$ third. Take $u(x)=1$, $u(z)=0$. Actions as in the p. 31 risk example: $A=(\tfrac12,0,\tfrac12)$, $B=(0,\tfrac12,\tfrac12)$, $C=(\tfrac13,\tfrac13,\tfrac13)$.

*Case 1: $u(y)=0.4$.*
- $EU(A)=0.5(1)+0+0.5(0)=0.5$
- $EU(B)=0+0.5(0.4)+0=0.2$
- $EU(C)=\tfrac13(1)+\tfrac13(0.4)+\tfrac13(0)=1.4/3\approx0.467$
- Choose $A$.

*Case 2: $u(y)=0.9$ (same ranking).*
- $EU(A)=0.5$
- $EU(B)=0.5(0.9)=0.45$
- $EU(C)=1.9/3\approx0.633$
- Choose $C$.

The ranking $xyz$ is identical in both cases, yet the choice changes. Under risk, how much you like $y$ matters, not just the order. This is why the chapter adds utility numbers once beliefs are probabilistic (p. 32).

## Concepts
- [[rationality-instrumental]] (new) — acting in accord with both one's preferences and one's beliefs; not omniscience (p. 17)
- [[preferences-vs-beliefs]] (new) — preferences are wants over outcomes, taken as given. Beliefs are probability statements linking actions to outcomes (pp. 14, 30)
- [[comparability-completeness]] (new) — for any pair, one is preferred or they are indifferent (p. 24)
- [[transitivity-individual-preference]] (new) — $xPy$ and $yPz$ imply $xPz$. Here it is a property of one person's preferences (p. 25). Cross-reference, not from this chapter: compare the canon's "cycling / intransitivity" entry.
- [[preference-ordering]] (new) — preferences that are complete and transitive, so alternatives can be ranked with a top (p. 25)
- [[methodological-individualism]] (new) — the individual is the unit of analysis. Only individuals have preferences and beliefs (p. 17)
- [[maximization-paradigm]] (new) — rationality as seeking the top of one's ordering, or what one is trying to maximize (p. 29)
- [[certainty-risk-uncertainty]] (new) — the chooser can name the outcome, can assign probabilities to outcomes, or cannot assign them (p. 31)
- [[utility-number]] (new) — numerical value of an outcome, relative not absolute (p. 32)
- [[expected-utility-principle]] (new) — choose the action whose outcome utilities, weighted by probabilities, sum highest (p. 33)

## Canonical instances
- [[mccaskill-2006-senate-decision]] — a choice between two lotteries driven by preference and belief (pp. 21–23)
- [[clinton-bush-perot-intransitivity]] — complete but intransitive preferences from shifting criteria (fn. 11, p. 26)
- [[sophies-choice]] — extreme case for comparability; failing to choose is still a choice (p. 27)
- [[saline-solution-experiment]] — transitivity violated when stakes are low (p. 28)
- [[economic-actors-display-2-1]] — four actors, each with an endowment and a maximand (p. 19)

## Bridges (candidates)
- [structural-analogy] intransitive individual preference from different criteria per pair (p. 26 fn. 11) ↔ social choice: majority cycling (canon: cycling / intransitivity), where pairwise comparisons also loop.
- [structural-analogy] preference ordering using $P$ and $I$ like $>$ and $=$ (p. 25) ↔ mathematics: ordering of real numbers, with the author's own analogy to ranking by magnitude.
- [metaphor] transitivity as a "perfectly spherical particle" assumption (fn. 14, p. 29) ↔ philosophy of science: idealization that is false but productive.

## Questions this raises
- If preferences are taken as given and may change with learning, when does assuming they are fixed in the short run become unsafe?
- Who decides when a failure of transitivity is a "warning about domain" rather than a refutation, and what evidence would settle it?
- Can altruistic acts be fully captured by the weak notion of self-interest (Problem 3)?
- When actors face genuine uncertainty rather than risk, how reliable is the "as if" treatment by expected utility?

## Exercises worth doing
- Ex. 1 (p. 35) — define rationality via preferences and behavior, and build a violation of each — difficulty: easy
- Ex. 2 (p. 35) — specify actors, outcomes, instruments and rule for contributors, activists and candidates — difficulty: medium
- Ex. 3 (p. 36) — can rational actors be altruistic? Argue both sides — difficulty: medium
- Ex. 4 (p. 36) — when does a most-preferred choice exist, and how does it relate to transitivity? — difficulty: medium
- Ex. 5 (pp. 36–37) — expected-utility threshold $p$ for Hillary Clinton's Senate-versus-State decision — difficulty: medium
- Ex. 6 (p. 37) — check whether the commonly observed lottery choices fit expected utility — difficulty: hard

## Reading notes
- Printed page = pdf − 13. The unit spans printed pp. 13–38. Printed p. 38 (pdf 51) is blank.
- The source note says printed pp. 251–252 are missing elsewhere in the scan. This does not affect this chapter.
- The OCR text is noisy (e.g. "19.78" for 1978, "b as", "Jess"). I checked the equations and notation against the page images (pp. 25, 32, 35, 37).
- Probable misprint in the Problem 6 text (p. 37, confirmed in the image): the example gives $EU(P_3)=.11u(x)+.89u(z)$. $P_3=(0,.11,.89)$ puts .11 on $y$, so it should read $.11u(y)+.89u(z)$.
- The chapter's conclusion says it summarizes "this chapter and the last". The previous chapter is not in this unit.

---
id: osborne-2004-introduction/ch01-introduction
work: osborne-2004-introduction
unit: 1 Introduction
pages: 1-8
fields: [decision-game-theory]
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
# Introduction (what game theory is; the theory of rational choice)

## L0 — One line
Game theory builds precise models of interacting decision-makers, and many of them rest on rational choice: each person picks an available action that is at least as good, by her own consistent preferences, as every other available action.

## L1 — The gist (≤ 120 words)
The chapter asks what game theory is and what "rational" means in it. Game theory is a collection of models of interaction. Models are judged partly by usefulness for a purpose, not as right or wrong. Rational choice means choosing a best available action according to preferences. Preferences need only be complete (every pair ranked or tied) and consistent, so altruistic tastes are allowed. A payoff function numbers actions to represent preferences; only the order of numbers matters. With unrestricted preferences, no single choice contradicts the theory; given an added assumption about indifference, some sets of choices do. It also has limits. The chapter ends with a map of the book: strategic, extensive and coalitional games, then extensions.

**Prerequisites:** sets and subsets; "if and only if"; comparing numbers. No other mathematics is needed.

## L2 — Key ideas (5–10 bullets)
- Game theory is a collection of models of situations where decision-makers interact. Its scope is much larger than everyday games (pp. 1–2).
- A good model is simple and captures the essence of the situation. Whether it is useful depends, in part, on the purpose, and models cannot be judged by an absolute criterion: none is "right" or "wrong" (pp. 1–2).
- Modeling has two steps. Building the model is an art. Analyzing it must follow strict logic. The results may confirm the original idea or suggest it is wrong (p. 2).
- Rational choice: the decision-maker chooses an action at least as good, by her preferences, as every other available action. Her rationality lies in the consistency of her choices, not in what she likes (pp. 4, 6).
- The model assumes preferences are complete (each pair is ranked or tied) and transitive (if a beats b and b beats c, then a beats c). No other restriction is imposed, so altruism is not ruled out (p. 4).
- A payoff function represents preferences by (5.1). It is purely ordinal (only order matters, not strength), so any increasing function of a representing payoff function also represents the preferences (pp. 5–6).
- With no assumptions about preferences, any single choice is consistent with the theory. If we also assume an indifferent decision-maker sometimes picks one action and sometimes the other, some collections of choices across different available sets are inconsistent with it. It also has limits, for example when an undesirable option is added to the set (pp. 6–7).
- The book's roadmap: Part I (strategic, extensive, coalitional games), Part II (players who do not know others' characteristics or past actions), Part III (further topics) (pp. 7–8).

## L3 — Walkthrough

### 1.1 What is game theory?
- Game theory helps us understand situations in which decision-makers interact. A game in the everyday sense is one example, but the book mainly illuminates economic, political and biological phenomena (p. 1).
- Applications listed include firms competing for business, candidates competing for votes, jury decisions, animals fighting over prey, auctions, siblings' behavior, experts' incentives to diagnose correctly, legislators' voting under interest-group pressure, and threats and punishment in long-term relationships (p. 1).
- A **model** is an abstraction used to understand observations and experiences. "Understanding" partly means seeing relationships between situations and isolating principles that apply to a range of problems (p. 1).
- Example: the lobbed tennis ball is modeled as moving forward at constant velocity and pulled down by a constant gravity force. It fits however hard or in whatever direction the ball is hit, and it fits other missiles too (p. 1).
- A model with assumptions wildly at odds with observation is unlikely to help. A model also gets power from simplicity, so its assumptions should capture the essence and ignore irrelevant details. For the ball, ignore how gravity varies with height (pp. 1–2).
- Models cannot be judged by an absolute criterion. Their usefulness depends partly on the purpose (p. 2).
- Example: Florence to Venice, assume a flat earth. Beijing to Havana, assume a sphere. Climbing the Matterhorn, neither (p. 2).
- Understanding game-theoretic models can help us mold the world. It may also suggest how to change our own behavior to improve our welfare. Analyzing negotiators' incentives may show the advantages and disadvantages of strategies (p. 2).
- Models are precise versions of ideas that could be stated verbally. The author uses mathematical symbols for conciseness and precision, but few concepts. They are described in Chapter 17 (p. 2).
- The modeling process (p. 2):
  1. Start with an idea about some aspect of interaction.
  2. Express it in a model with the relevant features. This is "an art": include enough to get nontrivial insights, not so much that irrelevant complications arise.
  3. Analyze the model. Here we must keep to logic and not add considerations absent from the model.
  4. The analysis may confirm the idea or suggest it is wrong. If wrong, the analysis should help us see why; we may see an inappropriate assumption or a missing element.
  5. Influence runs both ways: model implications help us judge whether ideas make sense, and ideas, in the light of those implications, may show how model assumptions are inappropriate.

*Intuition note:* A model is a deliberately simplified picture. You analyze it with strict logic to see whether the idea holds up, and the results may also show that an assumption is wrong. Whether it is useful depends in part on your purpose.

**Box: outline of the history (p. 3).**
- Some ideas date from the 18th century. Major development began in the 1920s with Emile Borel (1871–1956) and John von Neumann (1903–57).
- The 1944 book *Theory of games and economic behavior* by von Neumann and Oskar Morgenstern was a decisive event.
- The 1950s: use in economic theory and political science; psychologists began studying experimental games.
- The 1970s: first use in evolutionary biology.
- Later: game theory came to dominate microeconomic theory and is used across the social and behavioral sciences.
- The 1994 Nobel prize in economics went to Harsanyi, Nash and Selten.

**Box: John von Neumann (pp. 3–4).**
- Born in Budapest in 1903. He studied chemistry and earned a chemical-engineering degree in 1925, and a mathematics PhD in 1926.
- In 1928 he published a key result on strictly competitive games, "a result that had eluded Borel" (p. 3).
- He wrote the 1944 book with Morgenstern at the Institute for Advanced Study. He also worked on the Manhattan project and on the first electronic computer. He died in 1957 (pp. 3–4).

### 1.2 The theory of rational choice
The theory is a component of many game-theoretic models. A decision-maker chooses the best action according to her preferences among all available actions. No qualitative restriction is placed on preferences: her "rationality" lies in the consistency of decisions across different sets of available actions, not in the nature of her likes and dislikes (p. 4).

**1.2.1 Actions.**
- The model has a set $A$ of all actions that are available under some circumstances, plus a specification of preferences (p. 4).
- In a given situation she faces a subset of $A$ and must choose one element. She knows this subset and takes it as given. Her preferences do not influence it (p. 4).
- Example: $A$ is the set of bundles of goods she can possibly consume. Her income restricts her to the affordable subset (p. 4).

**1.2.2 Preferences and payoff functions.**
- Assumption 1: for any pair of actions she knows which she prefers, or that she is indifferent (p. 4).
- Assumption 2 (consistency): if she prefers $a$ to $b$ and $b$ to $c$, she prefers $a$ to $c$ (p. 4).
- No other restriction is imposed. Altruistic preferences are not ruled out. Theories using rational choice aim for implications that do not depend on any qualitative characteristic of preferences (p. 4).
- Preferences can be described by listing, for each pair, the preferred action or indifference. Alternatively they can be "represented" by a **payoff function** $u$ if, for any $a, b$ in $A$ (p. 5):
$$u(a) > u(b) \text{ if and only if the decision-maker prefers } a \text{ to } b. \tag{5.1}$$
- The author says "preference indicator function" would be a better name. In economics a payoff function representing a consumer's preferences is often called a "utility function" (p. 5).
- **Example 5.2.** She prefers Havana to Paris and Venice, which she regards as equivalent (p. 5). Any payoff function with equal values for Paris and Venice and a higher value for Havana represents this. Examples (p. 5):
  - $u(\text{Havana})=1,\ u(\text{Paris})=u(\text{Venice})=0$
  - $u(\text{Havana})=10,\ u(\text{Paris})=u(\text{Venice})=1$
  - $u(\text{Havana})=0,\ u(\text{Paris})=u(\text{Venice})=-2$
- Preferences convey only **ordinal** information, that is, order and not strength. They do not say "how much" $a$ is preferred to $b$. So a payoff function conveys only ordinal information too (p. 5).
- If $u(a)=0, u(b)=1, u(c)=100$, the *only* conclusion is that she prefers $c$ to $b$ to $a$. It does not follow that $c$ is liked far more than $b$. The function $v$ with $v(a)=0, v(b)=100, v(c)=101$ represents the preferences equally well, as does any $w$ with $w(a)<w(b)<w(c)$ (p. 5).
- So many payoff functions represent the same preferences. If $u$ represents them and $v$ satisfies the following condition, then $v$ also represents them (p. 6):
$$v(a) > v(b) \text{ if and only if } u(a) > u(b).$$
- Equivalently, any increasing function of $u$ also represents the preferences (p. 6).
- Sometimes it is natural to start from preferences and find payoff functions. Sometimes it is natural to start from payoff functions even if the analysis depends only on the underlying preferences (p. 6).

*Intuition note:* Payoff numbers are only labels that put options in order. Rescaling or relabeling them in an order-preserving way leaves the represented preferences unchanged. Do not read the gaps between numbers as how strongly she cares.

**1.2.3 The theory of rational choice.**
- The theory: *the action chosen is at least as good, according to her preferences, as every other available action.* This allows several equally attractive best actions (p. 6).
- For any single action we can design preferences that make it a best one. So with no information or assumptions about preferences, any single choice is consistent with the theory (p. 6).
- Now assume that a decision-maker indifferent between two actions sometimes chooses one and sometimes the other. Then not every collection of choices across different available sets is consistent with the theory (p. 6).
- Example: she always chooses $a$ from $\{a,b\}$, but sometimes chooses $b$ from $\{a,b,c\}$. Always choosing $a$ from $\{a,b\}$ means she prefers $a$ to $b$, since if indifferent she would sometimes pick $b$. From $\{a,b,c\}$ she must then pick $a$ or $c$, never $b$. So her choices are inconsistent (p. 6).
- The author's lunch-menu version: if you always choose the same dish when there are no specials, then regardless of your preferences it is inconsistent to pick *another menu item* on a day with an off-menu special (p. 6).
- In consumer theory the available set is the affordable bundles. In the theory of the firm, the actions are input-output vectors, and $a$ is preferred to $b$ if and only if $a$ yields higher profit (pp. 6–7).

*Intuition note:* With no assumptions about her preferences, one choice cannot contradict the theory. If an indifferent person is assumed to pick sometimes one action and sometimes the other, a pattern of choices across menus can. An option that she strictly disfavors against another available option (b against a) cannot be chosen just because a third option was added.

**1.2.4 Discussion.**
- The theory is "enormously successful" and appears in countless models. It pervades economics so much that arguments count as "economic" partly because they use it (p. 7).
- Still, in some circumstances its implications conflict with observed behavior. The author's small example: adding an undesirable action to a set sometimes significantly changes the action chosen (see Rabin 1998) (p. 7).
- How much this matters depends on the phenomenon. It may be unimportant for how the price–cost markup depends on the number of firms. It may be crucial for how advertising, designed to influence preferences, affects choices (p. 7).
- No general theory currently challenges rational choice theory. Readers should remember its limits: some phenomena they want to explain may lie beyond them. A model serves its purpose if it enhances understanding (p. 7).

### 1.3 Coming attractions
- Part I has three models: **strategic**, **extensive** and **coalitional** games (p. 7).
  - Strategic and extensive games focus on individuals' actions. Coalitional games focus on outcomes achievable by groups.
  - Strategic and coalitional games treat actions as chosen once and for all. Extensive games allow plans to be revised as they are carried out.
- The rational-choice model (actions plus preferences) is tailor-made for that theory. Most game models can admit more than one theory of the outcome, because strategic interaction is complex. A theory that specifies a set of outcomes for a model is called a **solution** (pp. 7–8).
- Chapter by chapter (p. 8):
  - Ch. 2: the strategic game and the solution of Nash equilibrium.
  - Ch. 3: significant applications.
  - Ch. 4: extends Nash equilibrium to allow an indifferent decision-maker not always to choose the same action, or identical players facing the same set to choose differently if more than one action is best.
  - Chs. 5–7: the extensive game, which adds a temporal dimension.
  - Ch. 8: the coalitional game and its solution, the core.
  - Part II, Chs. 9–10: strategic and extensive games where players do not know others' characteristics or past actions.
  - Part III, Chs. 11–12: two alternatives to Nash equilibrium. Ch. 13: evolutionary pressure rather than conscious choice. Chs. 14–15: repeated, long-term relationships. Ch. 16: bargaining.
- Notes: von Neumann and Morgenstern (1944) established the field. Aumann (1985) discusses the aims and achievements of game theory. Rabin (1998) and Elster (1998) discuss limits of rational choice (p. 8).

## Toy example (ours)
Options: tea, coffee, juice. She prefers coffee to tea, and tea to juice. By transitivity (Assumption 2) she prefers coffee to juice.

- Payoff function $u$: $u(\text{coffee})=5$, $u(\text{tea})=3$, $u(\text{juice})=0$. Check (5.1): $5>3$, $3>0$ and $5>0$, matching the three preferences.
- Another function $v=u^2$: $v(\text{coffee})=25$, $v(\text{tea})=9$, $v(\text{juice})=0$. The same order, so $v$ also represents her preferences. The gap tea–juice (9) is smaller than coffee–tea (16) under $v$ but larger (3 vs. 2) under $u$. So gaps carry no meaning.
- Consistency check. Data: from {coffee, tea} she always picks coffee, so she prefers coffee to tea, since indifference would sometimes yield tea. Observation: from {coffee, tea, juice} she sometimes picks tea. The theory says she must pick coffee or juice, never tea, because coffee is better than tea. So the data contradict the theory. The data "coffee from {coffee, tea, juice}, tea from {tea, juice}" are consistent.

## Concepts
- [[model]] (new) — an abstraction, judged partly by usefulness for a purpose and not as right or wrong (pp. 1–2)
- [[preference relation]] — for any pair she knows which is preferred or that she is indifferent, and preferences are transitive (p. 4)
- [[utility function]] — Osborne's "payoff function" $u$ satisfying (5.1); only ordinal information (p. 5)
- [[ordinal-payoff]] (new) — payoff numbers matter only through their order. Any increasing transformation represents the same preferences (pp. 5–6)
- [[rational-choice-theory]] (new) — the chosen action is at least as good, according to her preferences, as every other available action (p. 6)
- [[strategic (normal-form) game]] — model where actions are chosen once and for all, focused on individuals' actions (p. 7)
- [[extensive-form game]] — model that allows plans to be revised as they are carried out (p. 7)
- [[coalitional-game]] (new) — model focused on outcomes achievable by groups (p. 7)
- [[solution-concept]] (new) — a theory that specifies a set of outcomes for a model (pp. 7–8)
- [[Nash equilibrium]] — named as the solution studied for strategic games in Ch. 2 (p. 8)
- [[core]] (new) — a solution concept for coalitional games, named only (p. 8)

## Canonical instances
- [[payoff-function-vacation-packages]] — Example 5.2: Havana, Paris, Venice and several valid payoff functions (p. 5)
- [[choice-inconsistency-lunch-menu]] — the $\{a,b\}$ vs. $\{a,b,c\}$ pattern and the off-menu special (p. 6)
- [[model-purpose-maps]] — flat or spherical earth chosen by purpose (p. 2)
- [[lobbed-tennis-ball-model]] — a simple model that fits many missile paths (p. 1)

## Bridges (candidates)
- [structural-analogy] Model choice by purpose (flat vs. spherical earth) ↔ statistics: choosing a model for the task, not for truth — both judge models by usefulness.
- [structural-analogy] Ordinal payoffs (any increasing transformation) ↔ order-invariant statistics, e.g. rank-based methods — only order matters.
- [metaphor] Adding an undesirable option changes the choice ↔ behavioral-decision research on context effects — the text only mentions the phenomenon.

## Questions this raises
- If payoffs are only ordinal, which game-theoretic results still hold when payoffs are rescaled in an increasing but non-linear way? (The text does not say.)
- How can we check rational choice when a decision-maker's available set is influenced by her preferences, which the model assumes away?
- When is a violation, such as adding an undesirable option, important enough to abandon rational choice?
- Why do strategic models admit several theories of the outcome ("solutions"), while individual choice admits one?

## Exercises worth doing
- Ex. 5.3 (p. 5) — altruistic preferences: ranking outcomes and building a consistent payoff function — difficulty: easy
- Ex. 6.1 (p. 6) — which transformations of $u$ still represent the same preferences (order preserved vs. a tie created) — difficulty: easy

## Reading notes
- Source is an author's draft chapter (version 00/11/6, copyright 1995–2000), not the published 2004 OUP book. The metadata note says chapters 10 and 16 are absent from the draft.
- Page numbers: the page labels give printed 1–10, but the numbers printed on the pages run 1–8 (pdf 15 = p. 1, pdf 22 = p. 8). The label values for pdf 17–22 (5–10) do not match them.
- The page image of pdf 17 (box on history, p. 3) was not supplied. That text was read from the text layer, which looked clean.
- Equation (5.1) and the condition on p. 6 are as printed in the page images.

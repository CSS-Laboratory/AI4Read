---
id: schelling-1960-conflict/ch09-reciprocal
work: schelling-1960-conflict
unit: "9 – The Reciprocal Fear of Surprise Attack"
pages: 239-265
fields: [decision-game-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# The Reciprocal Fear of Surprise Attack

## L0 — One line
If two rational players both know the basic chance that each "irrationally" attacks, fear of the other's fear cannot raise attack gradually: the chance of attack either stays at its basic level or becomes certain; gradual mutual aggravation needs players whose attack probability itself responds to the other's, such as an imperfect warning system.

## L1 — The gist (≤ 120 words)
Schelling asks whether the spiral "he thinks we think he thinks…" can push two rational players into attacking, although neither wants war. In a model with known, exogenous (outside-given) attack probabilities it does not build gradually. The result is all-or-none: either no attack beyond the exogenous risk, or certain joint attack. A gradual "multiplier" appears only if a player's attack probability responds to the other's, as with nervousness, voting bodies, or a warning system whose trigger is loosened when danger rises. The resulting equilibrium is inefficient, like a prisoner's dilemma. Agreements to repair it are hard to enforce, because each side's warning criteria cannot be observed. The same logic fits partners who distrust each other.

**Prerequisites:** probability (complements, weighted averages); 2×2 payoff matrices; best response; basic derivatives and the chain rule.

## L2 — Key ideas
- Preclusive self-defence (striking first to avoid being struck) and partnership distrust (absconding, squealing) have the same payoff structure; the chapter asks whether compounded expectations can be modelled as rational choice (pp. 239–240).
- An infinite series of "he thinks I think" probabilities cannot be projected from a few terms, because nothing generates the series. The model must make each player's expectations a function of the other's (pp. 241–242).
- With known exogenous probabilities $P_c, P_r$ of "irrational" attack, the matrix is recomputed. Joint no-attack stays a strict solution below a critical $P$; above it, attack is chosen (pp. 245–248).
- The effect is all-or-none: the lesser parameter can be ignored, and a longer move-sequence only compounds the exogenous probabilities, still all-or-none (pp. 248–250).
- A genuine multiplier needs a model in which attack probability, not a decision rule, responds to fear: nervousness, voting groups, or a warning system with trade-off $B=f(R)$, where $R$ is the system's reliability and $B$ the chance of attack through false alarm (pp. 251–254).
- Under parametric behaviour (each player takes the other's current $B$ and $R$ as given; the same point is the candidate equilibrium of the tacit game, where each knows the other's trade-off but cannot observe his settings) a stable warning-system equilibrium requires the product of the reaction slopes to be below 1. The equilibrium is inefficient, like a prisoner's dilemma (pp. 257–261).
- Bargaining to lower warning sensitivity is open-ended and hard to enforce, because $R$ and $B$ may not be observable: they depend at least largely on decision criteria (pp. 261–263).

## L3 — Walkthrough

### Introduction (pp. 239–240)
- **Example:** a householder and a burglar, each armed, each may shoot first because he fears the other fears he will shoot (p. 239).
- If surprise pays, striking first averts it. Intuitively, "it looks as though" a modest temptation, too small alone to cause attack, might compound through interacting expectations; this is the idea the chapter goes on to test (p. 239).
- If gains from successful surprise are less desired than no war, there is no "fundamental" basis for attack (p. 239).
- The same game arises among partners who each suspect the other may abscond with joint assets, and among mobsters who fear a squealer (p. 240).
- Aim: test whether the "multiplier" can arise from rational calculation by players who understand their predicament (p. 240).

### Infinite series of probabilities (pp. 241–242)
- $P_1$ = my estimate that the other "really" prefers to attack. $P_2$ = probability he thinks I really would. $P_3$ = he thinks I think he really would, and so on (p. 241).
- Overall probability of his attack: $1-(1-P_1)(1-P_2)(1-P_3)\cdots$ (p. 241).
- Flaw: nothing generates the series. Each term is an ad hoc estimate, so the series is only as long as the player's time and stamina. Special games (roulette-wheel information structures) could generate it but would not illuminate the general case (pp. 241–242).
- Need: few arbitrary parameters, with extra probabilities generated automatically; each player's expectations a function of the other's (p. 242).

### A "strictly soluble" non-cooperative game (pp. 242–248)
- **Behaviour hypothesis, part 1:** if both see joint no-attack as best for both, they recognise it and abstain (Fig. 19) (pp. 242–243).
- **Part 2:** player R attacks with probability $P_r$, and C with $P_c$, even when he "should" not. This may stand for irrationality, a misconceived payoff matrix, or an accidental launch. These parameters are exogenous and fully visible to both; this keeps arbitrary inputs minimal and avoids a new infinite series (pp. 243–244).
- The question is whether the interaction of expectations adds motive for attack (p. 244).
- **Result:** no regular multiplier. Probabilities of attack do not interact to yield a higher probability "except when they yield certainty." The outcome is a pair of decisions, either joint attack or no attack (p. 245).
- **Recomputing the matrix (p. 245):** the upper-left cell is unchanged. The lower-right cell (both choose no-attack) becomes a weighted average of the four cells, with these probabilities:
  - no attack occurs: $(1-P_c)(1-P_r)$;
  - R attacks, C does not: $P_r(1-P_c)$;
  - C attacks, R does not: $P_c(1-P_r)$;
  - both attack: $P_cP_r$.
- A player who elects to attack certainly attacks. A player who elects no-attack attacks with probability $P$ (p. 245).
- **Figs. 20–22 (pp. 246–247):**
  - 0.2 each: innocuous. A strict solution remains at no-attack; value is reduced, but the fear is not aggravated.
  - 0.8 each: symmetric and unstable; each would rather attack. This is a prisoner's dilemma. The only efficient outcome is a binding agreement to no-attack, still worth only 0.04, if binding agreements were institutionally possible and play were forcibly postponed to let the players reach one.
  - 0.8 for C and 0.2 for R: unstable asymmetrically. C's likely irrationality forces R to attack in self-defence, and C, knowing this, attacks too.
- **Limits (p. 247, image p. 248):** with $h$ the value of unilateral surprise attack, $-h$ of being attacked, 0 of simultaneous attack and 1.0 of joint no-attack,
$$P_c < 1-h_r,\qquad P_r < 1-h_c .$$
The source does not say how the subscripts on $h$ are assigned (see Reading notes).
- **Fig. 23 (p. 248–249):** with $P_r=0.2$, the game becomes unstable at $P_c=0.5$ and the value goes to 0 for both. The plotted lines are $V_{r,n\text{-}a}=0.9-1.3P_c$, $V_{r,a}=0.5-0.5P_c$, $V_{c,n\text{-}a}=0.7-0.3P_c$, $V_{c,a}=0.4$ (p. 249).
- Because of the limits, the lesser parameter can be ignored. If both are below the limit, their size does not matter. If one is over it, it does not matter whether the other is 0 or 1.0. Attack likelihood is either the exogenous one or certainty (p. 248).

> **Intuition note.** Fear of the other's fear does not add up slowly. Once the exogenous risk is large enough to make one side attack, both attack; below that point, extra rounds of worry change nothing.

### The game as a sequence of moves in turn (pp. 249–251)
- Players alternate moves (R, C, R, C…) as long as nobody attacks (p. 249).
- Reasoning backward: C's last move, then R's choice given what C will do, and so on. With $n$ moves each, the compounded attack chances are $1-(1-P)^n$ for one player and $1-(1-P)^{n-1}$ for the other. The text layer shows no prime marks (see Reading notes). They are compared with the earlier limits (p. 250).
- If both meet the limits, nobody attacks. If one exceeds its limit, the player with the first turn attacks at once (p. 250).
- Probabilities compound, still all-or-none, and neither player has to combine both players' parameters. If the per-turn probability is $1-(1-P)^{1/n}$, the compounded total is just $P_c$ or $P_r$ and the outcome does not depend on the number of turns (p. 250).
- Read as the "he-thinks-I-think" spiral, successive cycles of fear make no difference (pp. 250–251).

### Reconsideration of the problem (pp. 251–254)
- For the burglar: if we both know the exogenous likelihoods, either they already make one of us shoot (so both), or they are insufficient and we know it. Higher-degree fears are then superfluous (p. 251).
- **Nervousness model:** my nervousness depends on how likely I think he is to shoot; my chance of shooting depends on nervousness; he acts likewise. Each person's nervousness is a function of the other's, giving a pair of simultaneous differential equations that seem to yield the mutual aggravation (pp. 251–252).
- Why it works: it has no decision criterion; it gives the probability of a decision, not a rule for choosing a strategy (p. 252).
- Schelling asks, as an open question, whether a rational player could be conceived as "changing the adjustment on his roulette wheel", and notes that individual and group decisions may differ. A collective with divergent values, a voting system and chance factors (e.g. absentees) could: the probability of a majority for attack rises with the probability of the enemy's attack (pp. 252–253).
- A route for a single rational player: dependence on an imperfect warning system with two kinds of error (p. 253).

### Probability-behaviour generated by an imperfect warning system (pp. 253–256)
- A warning system can mistake an attacker for a seagull, or a seagull for an attacker. For a given expenditure, tightening one kind of error loosens the other (p. 254).
- A rational player responds to higher danger by shifting criteria toward fewer missed attacks and more false alarms. Then each side's attack probability is a rising function of the other's. This is the "rational, mechanical counterpart" of nervousness (p. 254).
- **Setup:** $h$ = value of winning, $-h$ of losing, 0 of simultaneous attack (50-50 chance), 1.0 of no war. Here $h$ may exceed 1 provided $(1-R)h<1$. Successful surprise means attacking when the other does not and his warning fails (pp. 254–255).
- $R$ = reliability, the probability an attack is identified. Fig. 24 gives the payoff matrix (p. 255).
- A player attacks when he "should not" with $P = A + B - AB$. $A$ is the exogenous chance of irrational attack. $B$ is the chance of attack through false alarm. The error trade-off is $B=f(R)$, $f'(R)>0$ (p. 255); the combined form $A+B-AB$ is used on p. 256.
- R maximises $V_r$ subject to $B=f(R)$ (pp. 255–256):
$$V_r=(1-P_c)(1-P_r)+P_r(1-P_c)h(1-R_c)-P_c(1-P_r)h(1-R_r)$$
$$=(1-A_c)(1-B_c)(1-A_r)(1-B_r)+(A_r+B_r-A_rB_r)(1-A_c)(1-B_c)h(1-R_c)-(A_c+B_c-A_cB_c)(1-A_r)(1-B_r)h(1-R_r).$$
- **Joint no-attack stays preferred** (with optimally adjusted systems) if (p. 256):
$$P_c=A_c+B_c-A_cB_c<\frac{1-h(1-R_c)}{1-h(R_r-R_c)},\qquad P_r=A_r+B_r-A_rB_r<\frac{1-h(1-R_r)}{1-h(R_c-R_r)}.$$
With symmetry the denominators equal 1 (p. 256).
- This check may be unnecessary under certain behaviour hypotheses (pp. 256–257). Three hypotheses follow, corresponding to parametric behaviour, a tacit game and a bargaining game (p. 257).

### Dynamic adjustment (parametric behaviour) (pp. 257–260)
- Each player takes the other's $B$ and $R$ as given and picks his own to minimise expected loss. This tends to make his $B$ rise with the other's attack probability. It only tends to, because the other's $R$ may offset. The result is a "multiplier" system, stable or explosive depending on parameters and the shape of $f$ (p. 257).
- Maximising $V_r$ over $R_r$ with $B_r=f(R_r)$, treating $B_c$ and $R_c$ as fixed, gives (p. 258):
$$f'=\frac{P_c h(1-B_r)}{(1-P_c)[1-h(1-R_c)]-P_c h(1-R_r)}$$
The source prints a further condition after this formula; it is garbled in the text layer and only partly clear in the image (see Reading notes) (p. 258).
- Since $f'$ is presumed positive, the denominator must be positive for $V_r$ to be maximised with $R<1$. That is exactly the condition on $P_c$ for R to prefer joint no-attack. So optimal values with $R<1$ are consistent with joint no-attack (p. 258).
- **Slope of R's behaviour function** (p. 258–259), with $B_c=\phi(R_c)$:
$$\frac{dB_r}{dB_c}=\frac{dB_r}{dR_r}\frac{dR_r}{df'}\frac{df'}{dB_c}=\frac{f'}{f''}\frac{df'}{dB_c}=\frac{f'}{f''}\left(\frac{\partial f'}{\partial B_c}+\frac{\partial f'}{\partial R_c}\frac{dR_c}{dB_c}\right)=\frac{f'}{f''}\left(\frac{\partial f'}{\partial B_c}+\frac{\partial f'/\partial R_c}{\phi'}\right).$$
(The last equality uses $dR_c/dB_c=1/\phi'$ — added step.)
- Since $\partial f'/\partial R_c<0$, small $\phi'$ may make $dB_r/dB_c$ negative (p. 259).
- **Stability:** $dB_r/dB_c \cdot dB_c/dB_r<1$, i.e. C's curve cuts R's from below. The multiplier formulas contain 1 minus this product in the denominator (p. 259).
- As $h$ approaches the unstable-matrix condition, the denominator of $f'$ vanishes and $R_r$, $B_r$, $f'$ rise sharply (p. 259).
- $A_r$ drops out of R's optimal $B_r$, $R_r$, because $B$ and $R$ matter only if R does not launch irrational attack. $A_r$ does enter C's stability condition, but projecting C's behaviour would make R non-parametric (pp. 259–260).

> **Intuition note.** Each side loosens its trigger a bit when the other loosens his. Stability requires the reactions to be weak enough (slope product below 1); otherwise the process can run away ("stable or explosive", p. 257). This is the gradual multiplier the all-or-none model lacked.

### A tacit game (pp. 260–261)
- Each knows the other's $R$–$B$ technology but cannot reliably observe how the other has adjusted $R$ and $B$ (his decision rule). This yields a non-cooperative game (p. 260).
- The equilibrium point is at precisely the point, if any, where the parametric-behaviour hypothesis gave a stable equilibrium (p. 261). It is not necessarily unique (p. 261).
- It is inefficient, a prisoner's dilemma: reciprocal increases in the $B$'s raise each side's attack likelihood. Lower $B$'s would help both (p. 261).
- If the $A$'s are equal, an agreement for no warning system, with no false alarm, would be preferred among bargains giving identical systems (p. 261).

### A bargaining game (pp. 261–264)
- With enforceable negotiation over $R$ and $B$ there is no convincing unique solution. With a symmetric game and a common pair of values, the result is $B=0$, even if $R=0$. If $A_r$ and $A_c$ differ enough, a side payment would be needed (pp. 261–262).
- The game is wider open than formulated: players may threaten attack or alter institutions that fix the $A$'s (p. 262).
- **Enforcement problem:** $R$ and $B$ depend on future decision criteria (how long to wait to be "sure"), so they may not be observable. Breach leads to war itself, so recriminations and damage suits are out of the question if the model represents all-out war (p. 262).
- $R=B=0$ might be observable as "no system", but not if $h>1$, because the matrix is then unstable at $R=0$ and some $B$ is needed (pp. 262–263).
- Admitting an $A>0$ may be politically hard (p. 263).
- Alternatives: observably blunt one's own surprise capacity, improve the $f$ and $\phi$ curves (e.g. the richer side finances the other's alert system), or design forces with no surprise-attack potential and improved vulnerability to surprise attack (the source's wording), which "would seem to be indicated" (p. 263).
- Innovations that shift $f$ or $\phi$ are not always stabilising. Those that raise the marginal cost of $R$ may raise $B$; this is analogous to a prisoner's-dilemma payoff change that rewards non-cooperation (p. 263).
- Tactics: if one player acts parametrically and the other knows it, the first displays a "reaction function" that enters the other's $V$. The strategic moves of Chapters 2, 5 and 7 apply (p. 264).

### More than two players (pp. 264–265)
- Possible attack from other quarters reduces the incentive for mutual reduction of alert systems. Any two players can still gain from jointly lowering false-alarm risk, by accounting for the "external diseconomies" they ignore when behaving parametrically (p. 264).
- **Two watchmen:** each subject to some temptation to shoot on sight would gain from an enforceable agreement to be less ready. Here $P_c$, $P_r$ stand for the relative likelihood that a person met in the dark is a burglar rather than the other watchman. Making the burglar a rational third player would add complications (p. 264–265).

## Toy example (ours, not from the text)
Assume symmetric players and the payoffs described on p. 247: joint no-attack 1, unilateral attack $h$, being attacked $-h$, joint attack 0. Take $h=0.5$ (the limit is then $P<1-h=0.5$) and $P_c=P_r=P$. Using the p. 245 weights:
- No-attack against no-attack: $(1-P)^2+P(1-P)h-P(1-P)h=(1-P)^2$.
- Attack against a no-attacker (who still attacks with probability $P$): $h(1-P)$.
- No-attack against a certain attacker: $-h(1-P)$. Attack against a certain attacker: 0.

**$P=0.2$:** 0.64 against $0.5\cdot0.8=0.4$, so no-attack is better. Against a certain attacker, $-0.4<0$, but C is not certain to attack, so no-attack is chosen. Value falls from 1 to 0.64, with no escalation.

**$P=0.8$:** 0.04 against $0.5\cdot0.2=0.1$, so attack is better. Against a certain attacker, $-0.1<0$, so attack is better again. Both attack and each gets 0, below the 0.04 of joint no-attack: a prisoner's dilemma.

(Added step: for either player the difference is $(1-P_r)(1-h-P_c)$. Check: $P=0.2$ gives $0.8\cdot0.3=0.24=0.64-0.4$; $P=0.8$ gives $0.2\cdot(-0.3)=-0.06=0.04-0.1$.) The behaviour flips at $P=0.5$; there is no gradual escalation in between.

## Concepts
- [[reciprocal-fear-of-surprise-attack]] (new) — each side attacks partly because it fears the other fears being attacked; same structure as partnership distrust (pp. 239–240).
- [[exogenous-attack-probability]] (new) — the visible, outside-given chance $P$ that a player attacks though he "should not" (pp. 243–244).
- [[all-or-none-effect]] (new) — below the critical $P$ nothing compounds; above it attack is certain (pp. 245, 248).
- [[prisoners-dilemma]] (new) — each prefers attack although joint no-attack is better; also the warning-system equilibrium (pp. 247, 261).
- [[strategic-normal-form-game]] — the 2×2 payoff matrix recomputed with attack probabilities (pp. 245–246).
- [[dominant-dominated-strategy]] — above the limit, each would rather attack than hope for joint no-attack (p. 247).
- [[backward-induction]] — the sequential version is solved from the last move back (p. 250).
- [[best-response]] — parametric behaviour: choose $B,R$ optimally given the other's observed values (p. 257).
- [[nash-equilibrium]] — in the tacit game, the point, if any, where the parametric-behaviour equilibrium was stable (pp. 260–261).
- [[warning-system-error-tradeoff]] (new) — $B=f(R)$, $f'>0$; fewer missed attacks means more false alarms (pp. 254–255).
- [[parametric-behavior]] (new) — treating the other's behaviour as a given parameter, not projecting it (p. 257).
- [[mutual-vs-common-knowledge]] — the "he thinks I think" regress; the model makes $P_c, P_r$ visible to both to cut it (p. 244).

## Canonical instances
- [[burglar-and-householder]] — mutual fear of shooting first (p. 239).
- [[partnership-confidence]] — partners tempted to abscond; mob members tempted to silence a likely informer (p. 240).
- [[seagull-vs-attacking-plane]] — type-1/type-2 errors in a warning system (p. 254).
- [[two-armed-watchmen]] — two watchmen would gain from an enforceable agreement to shoot less readily (p. 264).

## Bridges (candidates)
- [structural-analogy] Warning-system trade-off $B=f(R)$ ↔ statistics: type-1 vs type-2 error trade-off in a decision threshold — tightening one loosens the other.
- [structural-analogy] Nervousness model (coupled "fear" functions) ↔ dynamics: two-variable positive feedback, stable if loop gain (product of slopes) is below 1.
- [structural-analogy] Both-attack equilibrium of the $B$'s ↔ game theory: prisoner's dilemma / race-to-the-bottom in sensitivity.
- [metaphor] "He thinks I think he thinks…" ↔ epistemic logic: higher-order beliefs; here cut off by making basic parameters visible.

## Questions this raises
- Is the all-or-none result robust if $P_c,P_r$ are not common knowledge, which the author avoids by assumption (p. 244)?
- Which real decision-makers behave like the nervousness model, and which like the calculating players?
- Can institutions make warning criteria observable enough to enforce agreements on $R$ and $B$?
- How does a third, autonomous player change incentives to cut alert sensitivity (p. 264)?

## Reading notes
- Printed page = pdf page − 1.
- Page images were supplied only for pdf 249, 250, 257 and 259; other pages come from the text layer. Figs. 19–22 and 24 (payoff matrices) are not shown in the supplied text; their cell values are not reproduced here.
- Footnote markers {110}–{125} appear in the text; the notes themselves are not in these pages.
- Limits on p. 248 print as $P_c<1-h_r$ and $P_r<1-h_c$. I take the subscripts on $h$ to be the player's own, but the text does not state this. Fig. 23's formulas fit $h=0.5$ for both players, my check.
- On p. 250 the text layer gives "$P_c = 1-(1-P_c)^n$" and "$P_r=1-(1-P_r)^{n-1}$" with no primes (no page image was supplied for this page, so primes may have been lost); presumably a primed left-hand side (compounded probability) is meant.
- p. 258: the condition after the $f'$ formula reads in the image as "$h(1-R_c) <1> h(1-R_r), f' > 0$" (the text layer has "f″ > 0"); the "<1>" part is garbled and I did not reconstruct the condition. In the last line of the $dB_r/dB_c$ derivation (p. 258) the symbol before the $\phi'$ term is garbled in the image (it resembles "⊥" or "±"). The preceding line has "+" and the chain rule gives "+", so I used "+".
- The unit has no exercises.

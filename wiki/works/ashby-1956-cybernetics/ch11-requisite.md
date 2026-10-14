---
id: ashby-1956-cybernetics/ch11-requisite
work: ashby-1956-cybernetics
unit: "11 Requisite Variety"
pages: 202–218
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 5
---
# Requisite Variety

## L0 — One line
When no outcome repeats within a column of the game table, a regulator can reduce the variety (number of distinct states) of outcomes caused by disturbances only by having variety of its own: in logarithmic form, $V_O \ge V_D - V_R$.

## L1 — The gist (≤ 120 words)
Ashby asks what all regulators have in common and how much regulation can be achieved. He models regulation as a game: a disturbance D moves, a regulator R replies, a fixed table T gives the outcome E. If no outcome repeats within a column, the variety of outcomes cannot fall below D's variety divided by R's variety. In logarithms, $V_O \ge V_D - V_R$. Only variety in R can destroy variety due to D. The law is a fact about table arrangements, not about machines, and it matches Shannon's Theorem 10. Ashby then applies it to biology, suggests that control may depend on regulation, and argues that compound disturbances, noise, initial states and complex targets all fit the same table.

**Prerequisites:** reading a two-way table; logarithms (log of a ratio = difference of logs); the idea of entropy as uncertainty (only for §11/8).

## L2 — Key ideas (5–10 bullets)
- Regulation can be studied as a game on a table: D picks a row, R picks a column, the cell is the outcome. R "wins" if the outcome is the target (pp. 202–203).
- If no column repeats an outcome, R must change his move whenever D changes his. The outcome set then has variety at least $r/c$, or D's variety divided by R's variety (pp. 204–206).
- Logarithmic form: $V_O \ge V_D - V_R$. This is the law of Requisite Variety: "variety can destroy variety" (p. 207).
- An essentially identical result holds for entropies (measures of uncertainty) when variety is spread out in time: $H(E) \ge H(D) + H_D(R) - H(R)$, with minimum $H(D)-H(R)$ when R is a function of D (pp. 207–208).
- The law is a statement about possible arrangements in a table. It owes nothing to experiment or to the properties of machines (p. 209).
- Regulation can be interpreted in terms of communication. R's capacity as a regulator cannot exceed its capacity as a channel of communication (a route that carries information), which Ashby relates to Shannon's Theorem 10 on correction channels removing noise (pp. 210–211).
- In biology, natural selection has shown the advantage of taking variety into the system as information, which can then be used to block disturbance from the gene-pattern (Ashby's term from S.10/6, not in this unit). By the law, disturbance reaching the gene-pattern can be diminished only by the amount of information so transmitted (p. 212).
- Perfect regulation gives a controller C complete control of the outcome, so control may depend on regulation (pp. 213–214).
- Ashby argues that vector-valued D and E, noise in T, initial states and interacting regulations can all be fitted into the basic table by redefining D, E or the boundaries. "Constant" targets include tracking targets (pp. 215–218).

## L3 — Walkthrough

### 11/1–11/2 Aim
The chapter examines regulation itself, develops ways to measure the degree of regulation, and shows that the amount has an upper limit (p. 202). Regulators are very varied, so Ashby looks for what is common to all. To do this he starts afresh, with no reference to regulation, and links back later (p. 202).

### 11/3 Play and outcome
Two players, R and D, share a table (Table 11/3/1, columns α β γ):

| D \ R | α | β | γ |
|---|---|---|---|
| 1 | b | a | c |
| 2 | a | c | b |
| 3 | c | b | a |

D plays first by choosing a row. R, knowing the row, chooses a column. The cell is the outcome. R wins if it is a (p. 203). With this table R can always win: choose β if D picks 1, α if 2, γ if 3. This is the transformation $1\to\beta,\ 2\to\alpha,\ 3\to\gamma$ (p. 203). R could equally force b or c, so he has complete control of the outcome (p. 203). Exercises (p. 203) include forcing c, $E=R-2D$ with target 37, and the skidding car.

### 11/4 Other tables
Table 11/4/1 gives D five moves and R four (columns α β γ δ):

| D \ R | α | β | γ | δ |
|---|---|---|---|---|
| 1 | b | d | a | a |
| 2 | a | d | a | d |
| 3 | d | a | a | a |
| 4 | d | b | a | b |
| 5 | d | a | b | d |

Every row has an a, so R can always force a (p. 203). Target b cannot always be forced: if D picks 3, no move gives b. Target c is hopeless for R, since D always wins (p. 203). The arrangement of the table and the numbers of moves give many different situations for R (p. 204). The butler exercise (p. 204) asks whether any drink in the cellar suits every possible guest.

### 11/5 A restricted class of tables
Full generality allows too many arbitrary tables to say much. Ashby therefore excludes tables where a column repeats an outcome, because then R need not discriminate between D's moves (p. 204). He considers only tables with no repeated outcome in any column. Then R must choose his move with full knowledge of D's move: any change in D's move needs a change in R's (p. 204). (Nothing is assumed about how columns relate to each other (p. 204).)

Table 11/5/1 (9 rows, columns α β γ) is the example. Its rows are 1: f f k; 2: k e f; 3: m k a; 4: b b b; 5: c q c; 6: h h m; 7: j d d; 8: a p j; 9: l n h (p. 205). Whatever his target, R must specify exactly one reply to each move of D. This is a single-valued transformation, e.g. $1\to\gamma,\ 2\to\alpha,\ 3\to\beta,\ \dots,\ 9\to\alpha$ (p. 205). It fixes the set of outcomes: $(1,\gamma)\to k$, $(2,\alpha)\to k$, $(3,\beta)\to k$, …, $(9,\alpha)\to l$ (p. 205). The claim is that the variety in this set cannot be less than

$$\frac{D\text{'s variety}}{R\text{'s variety}},$$

here $9/3$ (p. 205).

*Proof (key steps).* R marks one element per row and tries to keep the variety of marked elements as small as possible (target ignored) (pp. 205–206).
1. In row 1 he marks any element.
2. In row 2 he must move to a new column. In the column already used all elements differ, so staying would add a new element (p. 206).
3. He must change column at every row to stay at variety one. This is the best he can do, and it may not even suffice (p. 206).
4. With $n$ moves, at row $n$ all columns are used. At row $n+1$ some column must be reused, so a second outcome enters. In Table 11/5/1, the k's in rows 1–3 keep variety at one, but row 4 forces a second element (p. 206).

General statement: if no two elements in a column are equal, and R selects one outcome from each row, then for $r$ rows and $c$ columns the variety of the selected outcomes cannot be fewer than $r/c$ (p. 206).

*Intuition note.* In any one column all outcomes differ, so a given outcome value can appear in at most one row per column. With only $c$ columns, one outcome value can then cover at most $c$ rows. So if D has many more moves than R has columns, the outcomes must spread over several values (given the no-repeat condition).

### 11/6 The law (verbal form)
Keep the no-repetition condition. If R's move never varies, the outcome variety equals D's variety, so D has full control (p. 206). If R has two moves, outcome variety can be reduced to a half, but not lower. With three moves, to a third, and so on (p. 206). To reach an assigned fraction of D's variety, R's variety must be at least the corresponding minimum. Only variety in R's moves can force down the variety in the outcomes (p. 206).

### 11/7 Logarithmic form
Let $V_D$, $V_R$, $V_O$ be the varieties of D, R and the outcome, measured logarithmically. Under the same conditions, $V_O$ cannot be less than $V_D - V_R$, so its minimum is $V_D - V_R$ (p. 207). If $V_D$ is fixed, the minimal outcome variety can be lowered only by a matching increase in $V_R$ (p. 207). This is the **law of Requisite Variety**: only variety in R can force down the variety due to D; "variety can destroy variety" (p. 207).

*Intuition note.* In logs, dividing becomes subtracting. Each unit of variety R has cancels at most one unit of D's variety.

### 11/8 Entropy form (omit at first reading)
Essentially the same theorem is proved for variety spread over time, in Shannon's notation. D, R and E are treated as information sources (not necessarily independent). Entropies such as $H(D,R,E)$, $H_D(E)$ and $H_{ED}(R)$ can be defined (p. 207). The no-repeat condition becomes: if R is fixed, the entropy of E is at least that of D,

$$H_R(E) \ge H_R(D).$$

By algebraic necessity, both sides of the following equal $H(R,D)$ (p. 207):

$$H(D) + H_D(R) = H(R) + H_R(D).$$

Substituting $H_R(E)$ for $H_R(D)$ gives (p. 207)

$$H(D) + H_D(R) \le H(R) + H_R(E) \le H(R,E).$$

Always, by algebraic necessity, $H(R,E) \le H(R) + H(E)$ (p. 208). Hence $H(D)+H_D(R) \le H(R)+H(E)$, i.e.

$$H(E) \ge H(D) + H_D(R) - H(R).$$

(The printed line has misprints; see Reading notes.) The minimum is lowest when $H_D(R)=0$, i.e. when R is a determinate function of D. Then the minimum of $H(E)$ is $H(D)-H(R)$ (p. 208). So the minimal value of $E$'s entropy can be forced below $D$'s only by an equal increase in $R$'s (p. 208).

### 11/9 Extension: outcomes already limited
Suppose that even when R does nothing, the outcome variety is less than D's. In Table 11/4/1, R answering α throughout gives outcomes a, b or d: variety 3, against D's 5 (p. 208). Suppose each element is repeated $k$ times within each column, so that $kn$ rows may give only one outcome. The same argument gives (as printed, varieties logarithmic)

$$V_O \ge V_D - \log k - \log V_R$$

(p. 208). The entropy version replaces the condition by $H_R(E) \ge H_R(D) - K$, and the minimum of $H(E)$ becomes

$$H(D) - K - H(R)$$

(p. 208).

### 11/10 Where the impossibility comes from
The law says certain events are impossible. Its source is not the properties of matter or of machines. A "No machine can …" version cannot be overthrown by a new device, circuit or element (pp. 208–209). It comes from the table, which says only that certain D–R combinations lead to certain outcomes, whatever produces those outcomes. Experiments can only provide such tables (p. 209). The theorem concerns possible arrangements in a rectangular table. It is no more dependent on machines than "four objects can form a square, three cannot". It therefore owes nothing to experiment (p. 209).

### 11/11 Regulation again
Set-up. Disturbances D threaten to drive the essential variables E out of their proper range. E's values are the "outcomes". Only a few, the set η, are compatible with life or acceptable (p. 209). The table T is the hard external world, or internal matters the regulator must take for granted (p. 209). The process runs: D takes a value, R takes a value determined by D's, T gives an outcome, and it is in η or not. This usually repeats, as with a water-bath over a day (p. 209). A well-made regulator is a transformation of D such that all outcomes lie in η. Then R and T together act as the barrier F of S.10/5 (p. 209).

Diagram of immediate effects: arrows $D\to T$, $D\to R$, $R\to T$, $T\to E$. D's variety determines R's, and T's is determined by both (p. 210). Time steps of any machine behind T are essentially independent of the discrete steps of D, R and T used here (p. 210).

Interpretation: if R does nothing, D's variety threatens to pass through T to E. T may block some of it (S.11/9), occasionally enough for survival. Usually a further suppression is needed, and it can be achieved only by more variety in R (S.11/6) (p. 210). Focusing on $D\to R\to T$, with R as transmitter: the law says R's capacity as a regulator cannot exceed R's capacity as a channel of communication (p. 211).

Link to Shannon: his Theorem 10 says the noise removable by a correction channel is limited to the information that channel can carry. Shannon's "noise" corresponds to Ashby's disturbance, his "correction channel" to R, and his "message of entropy H" here becomes a message of entropy zero, since constancy is what is transmitted. Using a regulator for homeostasis and a correction channel to suppress noise are therefore homologous (p. 211). Exercises 1–4 (p. 211) ask for capacity estimates (insect, ship, general).

*Intuition note.* Regulation is like sending a message "stay constant" through a noisy line. As Ashby reports Shannon's Theorem 10, the noise removable by a correction channel is limited to the information that channel can carry. Likewise R's capacity as a regulator cannot exceed its capacity as a channel.

### 11/12 Sommerhoff
Ashby states, with "if I am not misinterpreting him", this equivalence with Sommerhoff's "directive correlation" (pp. 211–212): coenetic variable ↔ disturbance (D); response ↔ response (R); environmental circumstances ↔ table (T); subsequent occurrence ↔ outcome (E) (p. 212).

### 11/13 Biology and the law
A species continues to exist primarily because its members can block the flow of variety (as disturbance) to the gene-pattern. Natural selection favours taking much variety, as information, partly into the system, and using it so that the flow via R blocks the flow through T (p. 212). This resolves an apparent paradox: higher organisms have sensitive skins and nervous systems, and curiosity that brings in more variety than needed. Would avoiding variety not help survival? (p. 212). Ashby's answer: variety arrives in two forms (p. 212).
- One form threatens the gene-pattern by direct transmission via T from D to E. It must be blocked at all costs (p. 212).
- The other can be re-coded through R and used to block the remainder. This information is useful and, if a regulator can be provided, should be as large as possible. By the law, disturbance reaching the gene-pattern can be lessened only by the amount of information transmitted (p. 212).

Value of the law: in simple cases it is obvious. If a press photographer's twenty subjects are distinct (for exposure and distance), his camera needs at least twenty distinct settings if all the negatives are to be brought to a uniform density and sharpness (pp. 212–213). Its quantitative form matters in large systems. Ashby asks how much a dictator can control a country. It is commonly said that Hitler's control was total (voice: common opinion). Ashby says that, as power of regulation (S.10/6), the law makes it "just 1 man-power". He adds that this must be tested by the future, and its virtue is that it is exact (p. 213).

### 11/14 Control
Regulation and control are intimately related. In Table 11/3/1, R can force a, b or c at will (p. 213). Let a controller C decide the target and R obey. The diagram is $D\to T\to E$, $C\to R$, $D\to R$, $R\to T$, so the system has two independent inputs, C and D (p. 213). If R is a perfect regulator, E takes whatever value C sets, whatever D does. This holds for single targets and for sequences such as a, b, a, c, c, a (assuming components move in step) (pp. 213–214). So perfect regulation by R makes complete control by C possible (p. 214). Viewed another way, if an attempt $C\to E$ is disturbed by an independent D, a suitable R taking information from both C and D, and placed between C and T, may form with T a compound channel that transmits fully from C and nothing from D (p. 214). Control may thus depend necessarily on regulation (p. 214). Exercises 1–4 (p. 214) concern the transformations R needs and channel capacities.

### 11/15 Constancy versus change
Regulation reduces outcome variety, and its limit is a rigorously constant outcome (p. 215). This seems to clash with the naive view that organisms are not immobile. But "constant" or "varying" depends on which variable is meant (p. 215). Examples: a searchlight tracking an aircraft moves through a great range of angles to the earth, yet its angle to the aircraft stays at zero. A driver on a winding lane moves the wheel a lot while keeping the distance to the verge nearly constant (p. 215). Further cases: keeping $x-y$ constant at zero forces $x$ to copy $y$. Keeping $x+y$ constant makes $x$ do the opposite of $y$. Keeping $w-2\,dv/dt$ constant makes $w$ twice $v$'s rate of change (p. 215). It is convenient to treat all targets as "keep the outcome constant at a", but the theory is not only about immobility (p. 215).

### 11/16–11/21 Variations: the basic table is more general than it looks
The author's claim (11/16) is that the table of S.11/4 covers apparently harder cases (p. 216).
- **11/17 Compound disturbance.** D may be a vector with any number of components, so several simultaneous disturbances (traffic and gusts for a cyclist) are included (p. 216).
- **11/18 Noise in T.** D, T and E are defined functionally ("D" is "that which disturbs"). If T is noisy, redraw the boundaries so that T's noise input becomes a component of D. T then has no third input, and the formulation agrees with S.11/4 (p. 216). This is not a magic allowance for noise. D now has more components, so the new transformation will have to be more complex (p. 217).
- **11/19 Initial states.** If T's initial state can be standardised, there is no difficulty. If not, D, as a vector, can be redefined to include T's initial state (p. 217).
- **11/20 Compound target.** The thermostat must (i) usually stay in 36–37°C and (ii) return to the allowed range within one minute if displaced by ±10°. E can be a vector, with η specified per component. This covers complex, conditional or qualified targets (p. 217).
- **11/21 Internal complexity.** A signalman handling several trains is still covered, since D, R, T or E may be made of interrelated parts (p. 218). D is the pattern of arriving trains. E is the pattern of train movements. η includes "no collision". R is the pattern of signal and point movements. T is geography, mechanics and signalling techniques, which lead determinately to the outcome (p. 218). The basic formulation can therefore include cases of any internal complexity, in principle (p. 218).

## Toy example (ours, not from the text)
Let D have 4 moves $\{1,2,3,4\}$ and R have 2 moves $\{0,1\}$. The outcome is $E=(D+R)\bmod 4$, giving this table:

| D \ R | 0 | 1 |
|---|---|---|
| 1 | 1 | 2 |
| 2 | 2 | 3 |
| 3 | 3 | 0 |
| 4 | 0 | 1 |

Each column has no repeated outcome (column 0: 1,2,3,0; column 1: 2,3,0,1). The law's condition holds.
- If R always plays 0, the outcomes are 1,2,3,0, so variety is 4.
- The bound is $r/c = 4/2 = 2$. In logs base 2: $V_D=\log_2 4=2$, $V_R=\log_2 2=1$, so $V_O\ge 2-1=1$ bit, i.e. at least 2 outcomes.
- R can reach it: play 1 against D=1 (outcome 2), 0 against D=2 (2), 1 against D=3 ($3+1=4\to 0$), 0 against D=4 ($4\to 0$). Outcomes are $\{2,0\}$, variety 2, which meets the minimum.
- Getting to variety 1 would need R to hold one outcome for D=1 (needs 1 or 2) and D=3 (needs 3 or 0). Those sets are disjoint, so impossible with two moves.

## Concepts
- [[variety]] — number of distinct elements in a set; used for outcomes and moves, measured as a count or logarithmically (pp. 205–207)
- [[law of requisite variety]] — if outcomes do not repeat in a column, $V_O \ge V_D - V_R$; only R's variety reduces D's (p. 207)
- [[disturbance and noise]] — D, "that which disturbs"; noise in T can be absorbed into D (pp. 209, 216)
- [[homeostasis]] — keeping essential variables E within the acceptable set η; here homologous to noise-suppression by a correction channel (pp. 209, 211)
- [[plant]] — roughly T, the given table of the external world (Ashby's own term is "Table") (p. 209)
- [[regulation-as-communication]] (new) — R's capacity as a regulator cannot exceed its capacity as a channel (p. 211)
- [[control-via-regulation]] (new) — C achieves complete control of E when R is a perfect regulator (pp. 213–214)
- [[acceptable-set]] (new) — the set η of outcome values compatible with survival or the target (p. 209)
- [[vector-valued-variables]] (new) — D or E treated as vectors to absorb compound disturbances, initial states and compound targets (pp. 216–217)

## Canonical instances
- [[table-11-3-1-game]] — R has complete control of the outcome (p. 203)
- [[table-11-4-1]] — R can force a but not always b or c (p. 203)
- [[table-11-5-1]] — no repeats in columns; variety at least 9/3 (p. 205)
- [[press-photographer]] — twenty distinct subjects need at least twenty settings if all negatives are to reach uniform density and sharpness (pp. 212–213)
- [[hitler-control-example]] — "1 man-power" by the law (p. 213)
- [[searchlight-and-aircraft]] — "constant" or "varying" depends on the variable (p. 215)
- [[thermostat-compound-target]] — vector E with two conditions (p. 217)
- [[signalman-trains]] — complex interacting regulation fits the basic table (p. 218)

## Bridges (candidates)
- [structural-analogy] Law of requisite variety ↔ control-theory: a controller needs enough distinct responses to cover the distinct disturbances it must absorb — echoes "only variety in the regulator can absorb variety".
- [same-math] Ashby's entropy form ($H(E)\ge H(D)-H(R)$ when $H_D(R)=0$) ↔ information theory: limit on noise removable by a correction channel (Shannon's Theorem 10, as stated on p. 211).
- [structural-analogy] Control via regulation ($C$ with perfect $R$) ↔ control-theory: reference tracking as keeping $x-y$ constant at zero.

## Questions this raises
- The law assumes no repeated outcome in a column. How does the bound change when the table has many repeats (cf. §11/9)?
- How can the "variety" of a real regulator (a nervous system, an institution) be measured in practice, as in the exercises on channel capacity?
- If constancy can be redefined as tracking, which regulation problems cannot be written as "keep E in η"?
- Is the "1 man-power" claim about dictators testable? The author says only that the future must test it (p. 213).

## Exercises worth doing
- Ex. 11/3/2 (p. 203) — solve $E=R-2D$ for $R$ with target 37; a numeric version of a regulating transformation — easy
- Ex. 11/3/3 (p. 203) — build a 2×2 table for the skidding car; the table as model of regulation — easy
- Ex. 11/4/4 (p. 204) — the butler's choice; checks "can R always hit the target set?" — easy
- Ex. 11/11/1 (p. 211) — insect optic nerve vs ten dangers; capacity compared with variety — medium
- Ex. 11/11/3 (p. 211) — general's intelligence channel; compares channel capacity with the variety to be regulated — medium
- Ex. 11/14/2 (p. 214) — channel capacities needed for complete control against noise — medium

## Reading notes
- Printed page numbers are not in the page labels (they show "?"), but the page images show printed numbers, two per image (a spread). Offset: pdf 108 = pp. 202–203, pdf 109 = pp. 204–205, and so on; pdf 116 = p. 218. All citations use these printed numbers.
- Ashby's printed text has misprints: Ex. 11/14/1 refers to "Table 31/3/1", which should be 11/3/1. In §11/8 the final line prints $H_D(E)$ where the derivation needs $H_D(R)$. The line "so $H(D)+H_D(R)\le H(R)+H_R(E)$" needs $H(E)$ on the right to follow from the previous step.
- In §11/9, the printed formula $V_O \ge V_D - \log k - \log V_R$ is copied as printed. The text says varieties are measured logarithmically, so "log $V_R$" reads oddly.
- OCR errors in the text layer: "I et us", "acceptable set 17" for η on p. 209 (the page image itself prints "17", so this is a misprint in the typesetting, not only an OCR error), "beat' only" (probably "bears only"), and the symbols ≤/≥ often appear as < / >. The images were used to check.
- The reference "S.x/y" means Ashby's cross-references to other sections (S.10/5, S.10/6, S.10/14, S.9/19, S.7/25, S.4/1). These sections are not in this unit.

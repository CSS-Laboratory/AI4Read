---
id: osborne-2004-introduction/ch17-mathematics
work: osborne-2004-introduction
unit: "17 Appendix: Mathematics"
pages: 443–455
fields: [decision-game-theory]
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
# Appendix: Mathematics (Osborne, draft ch. 17)

## L0 — One line
The appendix collects the basic mathematical tools of the book (sums, sets, functions, profiles, geometric sums, probability with expected value and Bayes' rule, and the vocabulary of proofs) in informal form.

## L1 — The gist (≤ 120 words)
The chapter asks which elementary mathematics a reader needs for the rest of the book, and gives informal definitions rather than a full course. It covers sigma notation, sets and partitions, affine and quadratic functions, continuity, set-valued functions, and profiles such as $(b_i, a_{-i})$. It also gives the geometric-sum formulas, probability (independence, expected value, cumulative distributions), and conditional probability with Bayes' rule. A gene-test example shows how a prior belief of $\tfrac1{10}$ becomes a posterior of $\tfrac13$. A final section explains what lemmas, propositions and proofs are. The material matters because later chapters use it, for example in the chapters on mixed strategies and Bayesian games.

**Prerequisites:** High-school algebra; the idea of a graph of a function; proportions and percentages.

## L2 — Key ideas (5–10 bullets)
- Sigma notation $\sum_{i=k}^n x_i$ and $\sum_{i\in S} x_i$ shortens sums, including sums over non-consecutive index sets (pp. 443–445).
- A partition splits a set so that each member lies in exactly one part. The set {Paris, Venice, Havana} has five partitions (p. 444).
- Affine ($ax+b$) and quadratic ($ax^2+bx+c$) functions have simple graphs. A quadratic's extremum (its minimum or maximum) lies midway between two points at the same height, e.g. at $-\tfrac12 b/a$ (pp. 445–446).
- Some functions take sets as values. A profile assigns one object (e.g. an action) to each player, and $(b_i,a_{-i})$ changes only player $i$'s component (pp. 447–449).
- Geometric sums have closed forms (449.1) and (449.2). The infinite one needs $-1<r<1$ (p. 449).
- Probabilities are nonnegative, at most 1, and sum to 1. Independent events have $\Pr(E\text{ and }F)=\Pr(E)\Pr(F)$, and the expected value of a lottery (a probability distribution over outcomes) with numerical outcomes $x_i$ is $\sum p_ix_i$ (pp. 450–451).
- A cumulative distribution $F(x)$ (the probability of values at most $x$) is the useful description when there are infinitely many events, since a single event typically has probability zero (p. 451).
- Conditional probability (453.1) leads to Bayes' rule (453.2)/(454.2), a rule for revising a belief after new evidence. The author uses it in Bayesian games with states and signals (pp. 453–454).
- Lemma, Proposition and Corollary are labels for a result's role in the book. A good proof convinces and explains why (pp. 454–455).

## L3 — Walkthrough

### 17.1 Introduction
The chapter gives informal definitions of the mathematical concepts used in the text. Some may be new to the reader (p. 443).

### 17.2 Numbers
- "Number" is taken as basic. The integers are $\dots,-2,-1,0,1,2,\dots$ (p. 443).
- For a number $x$: positive if $x>0$; nonnegative if $x\ge0$; negative if $x<0$; nonpositive if $x\le0$. So $0$ is both nonnegative and nonpositive, and neither positive nor negative (p. 443).
- $\sum_{i=1}^4 x_i$ means $x_1+x_2+x_3+x_4$. The index letter is arbitrary (p. 443).
- $\sum_{i=k}^n x_i$ means: set $i=k$ and take $x_i$; raise $i$ by one and add the new $x_i$; continue until $i=n$ (p. 444).

### 17.3 Sets
- A **set** is a collection of objects. It is **finite** if counting its members eventually exhausts them. Order and repeats in a listing do not matter: $\{\text{Paris, Venice, Havana}\}=\{\text{Paris, Venice, Paris, Havana}\}$, which has three members (p. 444).
- $a\in A$ reads "$a$ is in $A$". $B$ is a **subset** of $A$ if every member of $B$ is in $A$. A set is a subset of itself, so "subset" does not rule out equality (p. 444).
- A **partition** of $A$ is a collection $\{A_1,\dots,A_k\}$ of subsets such that every member of $A$ is in exactly one $A_j$. The three-city set has five partitions: all singletons; $\{$Paris, Venice$\},\{$Havana$\}$; $\{$Paris, Havana$\},\{$Venice$\}$; $\{$Paris$\},\{$Venice, Havana$\}$; and the whole set as one part (p. 444).
- Infinite sets are of two kinds. The positive integers can be counted, but the counting never ends. The numbers between 0 and 1 cannot be counted. Both have infinitely many members (p. 444).
- Such sets are described by a property: $\{a\in A: a>1\}$ is "the set of $a$ in $A$ such that $a$ exceeds 1". If $A$ is the set of all numbers it is omitted, so $\{p:0\le p\le1\}$ is the set of nonnegative numbers that are at most 1 (pp. 444–445).
- $\sum_{i\in S}x_i$ is the sum of $x_i$ over all $i$ in $S$. Example: the total population of the cities in $S$ (p. 445).

### 17.4 Functions
- A **function** is a rule relating two variables, usually given by a formula: $f(x)=2x$, $g(x)=x^2$. For numerical variables it can be drawn as a graph, with the independent variable on the horizontal axis (Figure 446.1: $f(2)=4$ for $f(x)=x^2$) (pp. 445–446).
- **Affine:** $f(x)=ax+b$ with constants $a,b$. The author calls it **linear** when $b=0$. Its graph is a straight line with slope $a$ through $(0,b)$ and $(-b/a,0)$, because $a\cdot0+b=b$ and $a\cdot(-b/a)+b=0$. The slope is positive if $a>0$ and negative if $a<0$ (p. 445).
- **Quadratic:** $f(x)=ax^2+bx+c$. The graph is U-shaped if $a>0$ and an inverted U if $a<0$ (Figure 447.1) (p. 446).
- The graph is symmetric about a vertical line through the extremum, which is a minimum when U-shaped and a maximum when inverted. If the graph meets a horizontal line at $x_0$ and $x_1$, the extremum is at the midpoint $\tfrac12(x_0+x_1)$ (p. 446).
- Write $ax^2+bx+c=x(ax+b)+c$. Its value is $c$ at $x=0$ and at $x=-b/a$. So the extremum (maximum if $a<0$, minimum if $a>0$) is at the midpoint $-\tfrac12 b/a$ (p. 446).

> **Intuition note.** A parabola is mirror-symmetric. If you find two points at the same height, the peak or valley sits exactly halfway between them. Factoring out $x$ gives such a pair for free.

- **Continuous:** for every $x$, choosing $x'$ close enough to $x$ makes $f(x')$ as close to $f(x)$ as we wish. The graph may be steep but has no jumps or holes. In graphs of discontinuous functions a small disk marks an included point and a small circle an excluded point (Figure 447.2) (p. 447).
- **Set-valued functions:** the value at $x$ is a set. The author's example is the set of best routes to city hall from a starting point $x$. If a single route $A$ is best, the value is $\{A\}$ (pp. 447–448).
- Graphs of set-valued functions use gray shading for sets of points, and lines for included boundaries. In Figure 448.1, $f(x_1)=\{y:y_2<y\le y_3\}$ and $f(x_2)=\{y:y=y_0\text{ or }y_1<y\le y_4\}$ (p. 448).

### 17.5 Profiles
- A **profile** is a function that associates an object with each player. Example: $a(\text{Ernesto})=R$, $a(\text{Hilda})=S$, written $(a_{\text{Ernesto}},a_{\text{Hilda}})=(R,S)$. The order of writing is irrelevant if names are given (p. 448).
- With players named $1,2,3,\dots$, the first entry belongs to player 1, the second to player 2, and so on. For $n$ players the profile is $(a_1,\dots,a_n)$ (p. 448).
- $(b_i,a_{-i})$ is the profile that differs from $(a_1,\dots,a_n)$ only in that player $i$ plays $b_i$. The subscript $-i$ means "except $i$". Example: if $(a_1,a_2,a_3)=(T,L,M)$ and $b_2=R$, then $(b_2,a_{-2})=(T,R,M)$ (pp. 448–449).

### 17.6 Sequences
- A **sequence** is an ordered list. Here the elements are events unfolding over time. It is infinite if it continues indefinitely, finite if it ends (p. 449).
- The formulas are used in Chapters 14 and 15 (p. 449). For $r\ne1$ and $r\ne-1$:
$$a+ar+ar^2+\cdots+ar^T=\frac{a(1-r^{T+1})}{1-r}\tag{449.1}$$
  The exponent in the numerator equals the number of terms (p. 449).
- For $-1<r<1$:
$$a+ar+ar^2+\cdots=\frac{a}{1-r}\tag{449.2}$$
  (p. 449).

> **Intuition note.** A sum where each term is a fixed fraction of the previous one adds up to a finite number, if that fraction is between $-1$ and $1$. Here the terms shrink by a constant factor each step, and (449.2) gives the finite total $a/(1-r)$ (p. 449).

### 17.7 Probability

**17.7.1 Basic concepts.**
- We may model events as "random": if the event occurs many times it takes different values in no regular pattern. The proportion of times it takes a value is its **probability** (p. 449).
- A coin toss is modeled as heads with probability $\tfrac12$ and tails with $\tfrac12$. Over a large number $n$ of tosses the number of heads is likely to be close to $n/2$ (p. 449).
- A **probability distribution** assigns probabilities to events, e.g. $\tfrac13$ to $A$, $\tfrac12$ to $B$, $\tfrac16$ to $C$. The probabilities sum to 1, and each is nonnegative and at most 1 (pp. 449–450).
- Positive probability means some chance of occurring. Probability zero means it will never occur. Probability less than one means some chance of not occurring. Probability one means certain to occur. $\Pr(E)$ denotes the probability of $E$ (p. 450).
- If $E$ and $F$ cannot both occur, $\Pr(E\text{ or }F)=\Pr(E)+\Pr(F)$. Die example, each side $\tfrac16$: $\Pr(3\text{ or }4)=\tfrac16+\tfrac16=\tfrac13$ (p. 450).

**17.7.2 Independence.**
- $E$ and $F$ are **independent** if $\Pr(E\text{ and }F)=\Pr(E)\Pr(F)$. This is sensible to assume when one event has no bearing on the other. An election outcome may be modeled as independent of a coin toss, but not of the weather on polling day (p. 450).
- In a strategic game the players' choices are modeled as independent. The probability that player 1 chooses $a_1$ and player 2 chooses $a_2$ is the product of the two probabilities (p. 450).

**17.7.3 Lotteries and expected values** (used in Chapters 4, 7.6, 9, 10, 11, 12) (p. 450).
- A **lottery** over outcomes is a probability distribution over outcomes. Example: an offer accepted with probability $\tfrac13$ and rejected with $\tfrac23$ (p. 450).
- For numerical outcomes, the lottery giving $x_i$ with probability $p_i$ ($i=1,\dots,n$) has **expected value** $p_1x_1+\cdots+p_nx_n=\sum_{i=1}^n p_ix_i$ (p. 451).
- Example: $\$12$ with probability $\tfrac13$, $\$4$ with $\tfrac12$, $\$6$ with $\tfrac16$ gives $\tfrac13\cdot12+\tfrac12\cdot4+\tfrac16\cdot6=7$. No single play yields $\$7$, but the average over many plays is likely to be close to $\$7$ (p. 451).

> **Intuition note.** The expected value is the average over many plays, weighting each outcome by its probability. It need not be a value you see on one play: in the 12/4/6 dollar example no single play pays 7.

**17.7.4 Cumulative probability distributions** (used in Section 4.11, Chapter 9) (p. 451).
- For numerical events, the **cumulative probability distribution** $F$ gives, for each $x$, the total probability of all numbers at most $x$. For a die: $F(1)=\tfrac16$, $F(2)=\tfrac13$, $F(3)=\tfrac12$, … (p. 451).
- Probabilities can be recovered: the probability of $x$ is $F(x)-F(x')$, where $x'$ is the next smaller event (p. 451).
- With infinitely many events, only the cumulative form is useful, because a single event typically has probability zero. On the numbers from $\underline a$ to $\overline a$, $F$ is nondecreasing, $F(x)=0$ for $x<\underline a$, and $F(\overline a)=1$ (p. 451).
- Examples on $[0,1]$: $F(x)=x$ is uniform randomization (sets of equal size have equal probability). $F(x)=x^2$ gives lower probability to sets near 0 than to sets near 1 (p. 451).

**17.7.5 Conditional probability and Bayes' rule** (used in Section 9.8, Chapter 10) (pp. 451–452).
- Probability can describe a person's belief where an event cannot be repeated (jury, carrying a gene). Beliefs may be tightly or loosely tied to numerical evidence. The theory gives a specific rule for revising them. The initial belief is the **prior belief**; the revised one is the **posterior belief** (p. 452).
- **Gene example.** Prior: 10% carry $X$, so $0.1$. The test is positive for 90% of carriers and 20% of non-carriers. You test positive (p. 452).
  - Of 100 people, on average 10 carry $X$ and 90 do not. Positive: $9$ of the 10 and $18$ of the 90, so $9+18=27$ (p. 452).
  - The fraction of positives who carry $X$ is $9/27=\tfrac13$. The posterior is $\tfrac13$, up from $\tfrac1{10}$ (p. 453).
- **Conditional probability.** For events $E,F$ with $\Pr(F)>0$:
$$\Pr(E\mid F)=\frac{\Pr(E\text{ and }F)}{\Pr(F)}\tag{453.1}$$
  In Figure 452.1, with $E$ = carry $X$ and $F$ = test positive, this is the shaded area right of the line divided by the total shaded area (p. 453).
- If $E$ and $F$ are independent, $\Pr(E\mid F)=\Pr(E)$ (with $\Pr(F)>0$), or alternatively $\Pr(F\mid E)=\Pr(F)$ (with $\Pr(E)>0$) (p. 453).
- The data given were $\Pr(E)$, $\Pr(F\mid E)$, $\Pr(F\mid\text{not }E)$. **Bayes' rule** expresses $\Pr(E\mid F)$ in terms of these:
$$\Pr(E\mid F)=\frac{\Pr(E)\Pr(F\mid E)}{\Pr(E)\Pr(F\mid E)+\Pr(\text{not }E)\Pr(F\mid\text{not }E)}\tag{453.2}$$
  with $\Pr(\text{not }E)=1-\Pr(E)$ (p. 453).
- *Derivation (author's):* (i) Interchanging $E,F$ in (453.1) gives $\Pr(E)\Pr(F\mid E)=\Pr(E\text{ and }F)$, the numerator. (ii) By (453.1) the denominator equals $\Pr(E\text{ and }F)+\Pr((\text{not }E)\text{ and }F)$. (iii) Exactly one of $E$, not $E$ occurs, so this sum is $\Pr(F)$ (p. 453).
- *(added step)* Check on the example: $\dfrac{0.1\cdot0.9}{0.1\cdot0.9+0.9\cdot0.2}=\dfrac{0.09}{0.27}=\tfrac13$.
- **General form.** Let $E_1,\dots,E_n$ be events exactly one of which must occur. Then
$$\Pr(E_k\mid F)=\frac{\Pr(F\mid E_k)\Pr(E_k)}{\sum_{j=1}^n\Pr(F\mid E_j)\Pr(E_j)}\tag{454.2}$$
  Here $F$ = positive test, $n=2$, $E_1$ = carry, $E_2$ = do not carry. The rule is named after Thomas Bayes (1702–61) (p. 454).
- In a Bayesian game the $E_k$ are the states and $F$ is a signal. Each $\Pr(F\mid E_k)$ is then one or zero, depending on whether state $E_k$ generates signal $F$ (p. 454).

> **Intuition note.** Bayes' rule asks: among all the ways the evidence could have come about, what share come from the hypothesis? In the gene example the posterior is only $\tfrac13$, because most positives (18 of 27) come from the large group of non-carriers.

### 17.8 Proofs
- Results are named Lemma, Proposition or Corollary. The names have no formal logical meaning. A lemma is mainly a step toward further results, a proposition is a main result, and a corollary is a more or less direct implication of a main result (p. 454).
- A result is a series of statements "if $A$ then $B$", sometimes not written that way. If it claims both "if $A$ then $B$" and "if $B$ then $A$", it is stated compactly as "$A$ if and only if $B$" (p. 454).
- A **proof** of "if $A$ then $B$" is a series of arguments from $A$ to $B$, each following from a known fact, including earlier steps. Except for proofs of very simple results, most proofs are not, and sensibly should not be, complete, since full detail would be very long and hard to read. Judging what to leave out is an art (pp. 454–455).
- A good proof convinces the reader and shows why the result is true: which features of $A$ matter and which do not (p. 455).

## Toy example (ours)
Players 1 and 2 choose independently. Player 1 plays $T$ with probability $0.6$ and $B$ with $0.4$. Player 2 plays $L$ and $R$ with $0.5$ each. Player 1's payoffs are $(T,L)=4$, $(T,R)=0$, $(B,L)=1$, $(B,R)=3$.

- Independence: $\Pr(T,L)=0.6\cdot0.5=0.3$, $\Pr(T,R)=0.3$, $\Pr(B,L)=0.4\cdot0.5=0.2$, $\Pr(B,R)=0.2$. Sum $=1.0$.
- Expected value for player 1: $0.3\cdot4+0.3\cdot0+0.2\cdot1+0.2\cdot3=1.2+0+0.2+0.6=2.0$.
- Profile notation: for $a=(T,L)$ and $b_1=B$, $(b_1,a_{-1})=(B,L)$.
- Geometric sum: a payoff stream $2,\,2\cdot\tfrac12,\,2\cdot\tfrac14,\dots$ has $a=2$, $r=\tfrac12$. By (449.2) its sum is $2/(1-\tfrac12)=4$. Check: $2+1+0.5+0.25+\cdots\to4$.
- Bayes: prior $0.5$; a signal appears with probability $0.8$ in state $E$ and $0.2$ in not-$E$. Then $\Pr(E\mid F)=\dfrac{0.5\cdot0.8}{0.5\cdot0.8+0.5\cdot0.2}=\dfrac{0.4}{0.5}=0.8$.

## Concepts
- [[expected-value]] (new) — probability-weighted average $\sum p_ix_i$ of a lottery's numerical outcomes (p. 451)
- [[lottery]] (new) — a probability distribution over outcomes (p. 450)
- [[probability-distribution]] (new) — assignment of probabilities to events; each in $[0,1]$, total 1 (pp. 449–450)
- [[independent-events]] (new) — $\Pr(E\text{ and }F)=\Pr(E)\Pr(F)$; used for players' choices in a strategic game (p. 450)
- [[cumulative-distribution]] (new) — $F(x)$ = probability of values at most $x$; useful when there are infinitely many events and single events typically have probability zero (p. 451)
- [[conditional-probability]] (new) — $\Pr(E\mid F)=\Pr(E\text{ and }F)/\Pr(F)$ (p. 453)
- [[bayes-rule]] (new) — formulas (453.2) and (454.2) for updating a prior given evidence (pp. 453–454)
- [[prior-posterior-belief]] (new) — belief before and after evidence (p. 452)
- [[geometric-sum]] (new) — closed forms (449.1) and (449.2) for $a+ar+ar^2+\cdots$ (p. 449)
- [[action-profile]] (new) — one action per player; $(b_i,a_{-i})$ changes only player $i$'s action (pp. 448–449)
- [[set-valued-function]] (new) — a function whose values are sets, e.g. sets of optimal routes (pp. 447–448)
- [[affine-quadratic-functions]] (new) — $ax+b$ and $ax^2+bx+c$; extremum of the quadratic at $-\tfrac12 b/a$ (pp. 445–446)
- [[continuous-function]] (new) — no jumps: nearby inputs give nearby values (p. 447)
- [[partition]] (new) — subsets with every member of the set in exactly one part (p. 444)

## Canonical instances
- [[gene-test-example]] (new) — prior $\tfrac1{10}$ becomes posterior $\tfrac13$ after a positive imperfect test (pp. 452–453)
- [[coin-and-die-examples]] (new) — fair coin gives $\tfrac12$ each; $\Pr(3\text{ or }4)=\tfrac13$ on a die (pp. 449–450)
- [[lottery-12-4-6]] (new) — expected value 7 for $\$12$, $\$4$, $\$6$ with probabilities $\tfrac13,\tfrac12,\tfrac16$ (p. 451)
- [[uniform-and-square-cdf]] (new) — $F(x)=x$ (uniform) versus $F(x)=x^2$ on $[0,1]$ (p. 451)
- [[three-city-partitions]] (new) — five partitions of $\{$Paris, Venice, Havana$\}$ (p. 444)

## Bridges (candidates)
- [same-math] Expected value $\sum p_ix_i$ ↔ decision-game-theory: expected utility — the same weighted average, with utilities as the numbers.
- [same-math] Bayes' rule with states and signals ↔ Bayesian game / Bayesian Nash equilibrium: beliefs about types updated on a signal.
- [structural-analogy] Geometric sum $a/(1-r)$ ↔ repeated game / shadow of the future: a stream of payoffs shrinking by a constant factor each period.
- [structural-analogy] $(b_i,a_{-i})$ ↔ best response / Nash equilibrium: it is the notation for one player's deviation, holding others fixed.
- [structural-analogy] Cumulative distribution on a continuum ↔ mixed strategy over a continuum of actions: the chapter points to Section 4.11 for this use.

## Questions this raises
- Why is the condition $-1<r<1$ needed for (449.2), and what happens to the partial sums when $r\ge1$?
- How does the posterior in Bayes' rule change as the prior $p$ falls? (Exercise 454.1 asks this.)
- Why must a single outcome have probability zero in many continuous distributions, and how can the probabilities of intervals still be positive?
- What exactly does a proof leave out, and how does a reader judge that a "good" proof has left out the right things?

## Exercises worth doing
- Ex. 446.1 (p. 446) — maximizer of $x(\alpha-x)$ using the midpoint-of-roots idea — difficulty: easy
- Ex. 449.3 (p. 449) — sums $1+\delta^2+\delta^4+\cdots$ and $1+2\delta+\delta^2+2\delta^3+\cdots$ using (449.2) — difficulty: medium
- Ex. 454.1 (p. 454) — how the posterior falls with the base rate $p$; the cases $p=0.001$ and the 99%-accurate test — difficulty: medium

## Reading notes
- The pdf page labels give no printed number, but the page images show printed numbers 443–455. So printed = pdf + 44 (pdf 399 = p. 443). All references here use printed numbers.
- The source is an author's draft chapter (version 00/11/6, copyright 1995–2000), not the published 2004 book. Page 450 refers to Chapter 10, which is absent from this draft.
- The text layer garbles several symbols. The images show: $\ne$ in the conditions of (449.1); and $p_ix_i$, not $p_nx_n$, in the compact sum on p. 451.
- The proofs section (p. 454) uses "all prime numbers are odd" as an example of a result's form. As an arithmetic fact it is false, since 2 is prime and even. It illustrates only the "if … then" form.
- In the text layer the fraction in "$\tfrac12(x_0+x_1)$" is split across lines, and primes and bars (e.g. $x'$, $\underline a$, $\overline a$) are lost; all were read from the page images, and no equation was unreadable.

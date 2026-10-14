---
id: lupia-1998-dilemma/app-ch03
work: lupia-1998-dilemma
unit: Appendix to Chapter 3
pages: 240-256
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Appendix to Chapter 3: A formal model of persuasion

## L0 — One line
In a speaker–principal signalling game, persuasion needs a principal who thinks it more likely than not that the speaker shares her interests (c > .5) and who thinks the speaker may be knowledgeable (k > 0). Verification, penalties for lying, or costly effort can replace the c > .5 requirement.

## L1 — The gist (≤ 120 words)
The appendix gives the formal game behind Chapter 3's conditions for persuasion. A speaker sends the signal "x is better" or "x is worse" to a principal, who then chooses x or y. In the basic model, a nonbabbling (informative), non-neologistic (words keep their usual meaning) equilibrium exists only if the principal's prior probability of common interests exceeds .5 and her prior probability that the speaker is knowledgeable exceeds 0. Three extensions (verification, penalties for lying, costly effort) remove the c > .5 requirement, so these external forces substitute for common interests. Theorem 3.3 states the result: persuasion needs a trusted speaker, a speaker seen as knowledgeable, and a signal showing that the prior is insufficient for reasoned choice.

**Prerequisites:** extensive-form games and information sets; Bayes' rule; expected utility; the idea of a Nash equilibrium.

## L2 — Key ideas (5–10 bullets)
- The basic game has three hidden moves by nature: the state (x better or worse), whether the speaker knows it (prob. k), and whether interests are common (prob. c). The speaker signals B or W, then the principal chooses x or y (pp. 240–241).
- The solution concept is sequential equilibrium (each player acts optimally at every information set, i.e. every point where she cannot tell which node she is at, given beliefs that fit the strategies) plus a refinement: at an information set reached with probability zero, the principal ignores the signal. Babbling equilibria (the signal is ignored or carries no information) are acknowledged but not pursued, and neologistic ones (B means "worse", W means "better") are excluded by assuming words have focal meanings (pp. 245–246).
- Proposition 3.1 gives the only nonbabbling, non-neologistic equilibrium: the principal follows the signal, and knowledgeable speakers with common interests tell the truth while those with conflicting interests lie. It requires Conditions A and B (p. 246).
- Theorem 3.1 shows this equilibrium exists only if c > .5. Theorem 3.2 shows it needs k > 0. Neither needs the speaker actually to be common-interest or knowledgeable (pp. 249–250).
- Verification (Prop. 3.2) and penalties for lying (Prop. 3.3) each remove the c > .5 requirement (pp. 251–253).
- Costly effort with continuous types (Prop. 3.4) also removes the c > .5 requirement (p. 255). Paying the cost lets the principal infer something about where x lies, which can change her beliefs (p. 255). The printed range for this inference looks like a misprint (see Reading notes).
- Theorem 3.3: trust, perceived knowledge, and a signal that shows the prior is insufficient are individually necessary and collectively sufficient. External forces substitute for common interests (pp. 255–256).

## L3 — Walkthrough

### The basic model (pp. 240–241)
Two players: a speaker and a principal. The principal chooses x or y. Nature makes three probabilistic choices $n=\{n_b,n_c,n_k\}$, in any order (p. 240).

- **State.** $n_b\in\{better,worse\}$: x is better for the principal with probability $b$, worse with $1-b$. The principal does not observe it. Her prior belief is $b$ (p. 240).
- **Principal's payoff.** She gets $U\ge0$ from x if better, $\underline U\le0$ from x if worse, and 0 from y (normalization) (p. 240).
- **Speaker's knowledge.** $n_k\in\{n_b,\emptyset\}$. The speaker learns the state with probability $k$ and nothing with $1-k$. He knows $n_k$; she does not (p. 241).
- **Interests.** $n_c\in\{common,conflicting\}$ with probabilities $c$ and $1-c$. The speaker knows $n_c$; she does not (p. 241).
- **Speaker's payoff.** Common: $Z\ge0$ when the principal gets $U$, and $\underline Z\le0$ when she gets $\underline U$. Conflicting: $\underline Z\le0$ when she gets $U$, and $Z\ge0$ when she gets $\underline U$. Speaker utility is normalized to 0 when the principal chooses y (p. 241).
- **Moves.** The speaker sends $s\in\{B,W\}$, "x is better" or "x is worse". He need not tell the truth. The principal then chooses x or y (p. 241).

### The equilibrium concept (pp. 241–246)
- A sequential equilibrium is a strategy profile $\pi$ plus a belief system $\mu$ (probabilities over the decision nodes of each information set, summing to 1). It must be sequentially rational and consistent (p. 242).
- **Sequential rationality** is optimal play from every information set, given beliefs and others' strategies. It is necessary but not enough, because it puts no restriction on beliefs, so nonsensical beliefs can support equilibria (p. 242).
- **Consistency** requires beliefs and strategies to fit together. At a minimum, beliefs must follow from strategies by Bayes' rule wherever an information set is reached with positive probability (Kreps, p. 243). It is hard to define at zero-probability sets. Kreps–Wilson consistency (limits of totally mixed strategies) is "far too strong" for the authors' purposes (p. 243).
- **Refinement chosen** (Fudenberg–Tirole): a deviation to a zero-probability set is not treated as informative about things the deviator does not know. Here that reduces to: if the principal is at a zero-probability set, she ignores the signal (p. 244).
  - It is innocuous because the principal has only two information sets (after B, after W). If one has probability 0, the other has probability 1. The speaker then acts as if he does not condition his signal on $n_b,n_c,n_k$, so nothing can be inferred from his deviation (p. 244).
- **Strategies.** $\pi_s(s;h_j)$ is the probability that the speaker signals $s$ at his information set $h_j$, $j=1,\dots,6$, summing to 1. The principal's information sets are $h_B,h_W$, with $\pi_r(x;s)$ the probability of choosing x after $s$ (p. 244). The speaker's sets are, by nature's choices (as I read the weights, p. 248):
  - $h_1$: common, knows, better.
  - $h_2$: common, knows, worse.
  - $h_3$: conflicting, knows, better.
  - $h_4$: conflicting, knows, worse.
  - $h_5$: common, ignorant.
  - $h_6$: conflicting, ignorant.
- **Definition (p. 245).** $(\pi_r,\pi_s)$ is a sequential equilibrium if:
  - (a) $\pi_s(s;h_s)$ maximizes the speaker's expected utility given $\pi_r$.
  - (b) For each $s$ on the path of play, $\pi_r(x;s)$ maximizes her expected utility given $\mu(better|s)$ and $\mu(worse|s)$ from Bayes' rule.
  - (c) For $s$ off the path, $\pi_r$ maximizes her utility given $\mu(better|s)=b$ and $\mu(worse|s)=1-b$.
- **Equilibrium selection (pp. 245–246).**
  - Babbling equilibria (the speaker's signal ignores $n_b$, or the principal's response ignores $s$) exist in the model. They are set aside because they promise zero benefit, and if communication has any cost, players expecting them should make no attempt to communicate.
  - The authors agree with Farrell that babbling is implausible in cases where both players would gain from a signal.
  - Non-neologistic means that "better" and "worse" have focal meanings. A neologistic equilibrium would need both players to agree that B means "worse" and W means "better". The authors call this focus "quite unrestrictive" because lying is allowed.

**Intuition note.** The authors keep only equilibria where talk is informative and the words keep their ordinary meaning (speakers may still lie). If a signal could change nothing, then, the authors say, people who face communication costs should make no attempt to communicate.

### Proposition 3.1 (basic model, p. 246)
Notation: $\pi_{14}=(\pi_s(B;h_1),\dots,\pi_s(B;h_4))$, $\pi_5=\pi_s(B;h_5)$, $\pi_6=\pi_s(B;h_6)$, $\pi_r=(\pi_r(x;B),\pi_r(x;W))$.

**Proposition 3.1.** The only nonbabbling, non-neologistic sequential equilibrium is:
- $\pi_{14}=(1,0,0,1)$.
- $\pi_5=1$ if $bZ+(1-b)\underline Z\ge0$, and $0$ otherwise.
- $\pi_6=1$ if $b\underline Z+(1-b)Z\ge0$, and $0$ otherwise.
- $\pi_r=(1,0)$.

It requires, with $R\equiv \frac{b\,U}{(b-1)\underline U}$ (the underline assignment is mine; see Reading notes):

$$\text{Condition A: }\frac{(1-c)k+(1-k)[\pi_5c+\pi_6(1-c)]}{ck+(1-k)[\pi_5c+\pi_6(1-c)]}\le R$$
$$\text{Condition B: }\frac{ck+(1-k)[(1-\pi_5)c+(1-\pi_6)(1-c)]}{(1-c)k+(1-k)[(1-\pi_5)c+(1-\pi_6)(1-c)]}\ge R$$
with at least one inequality strict (p. 246).

**Meaning of the strategies.** Knowledgeable common-interest speakers tell the truth ($h_1$ signals B, $h_2$ signals W). Knowledgeable conflicting-interest speakers lie ($h_3$ signals W, $h_4$ signals B). The principal follows the signal (pp. 246, 252).

**Proof outline (pp. 246–249).**
1. *Speaker's pure-strategy values.* If $\pi_r(x;B)\ge\pi_r(x;W)$:
   - $h_1$: B is best (value $\pi_r(x;B)Z$ vs $\pi_r(x;W)Z$).
   - $h_2$: W is best (values with $\underline Z$).
   - $h_3$: W is best.
   - $h_4$: B is best.
   - $h_5$: B yields $b\pi_r(x;B)Z+(1-b)\pi_r(x;B)\underline Z$, and W yields the same with $\pi_r(x;W)$. So W is best if $bZ+(1-b)\underline Z\le0$.
   - $h_6$: the same with $b\underline Z+(1-b)Z$ (p. 247).
2. **Lemma 1: all mixed-strategy sequential equilibria are babbling.**
   - A mixed equilibrium needs each player to make the other indifferent. The necessary and sufficient condition for making the speaker indifferent at $h_1$–$h_4$ is to set $\pi_r(x;B)=\pi_r(x;W)$, which means the principal ignores the signal. The same holds at $h_5$ and $h_6$ unless the relevant sum is 0.
   - The speaker may then choose any strategy; these either make the principal indifferent between her pure strategies (babbling) or give no equilibrium.
   - If a sum is 0, any principal strategy makes that speaker indifferent. But the principal has an incentive to choose a mixed strategy other than $0<\pi_r(x;B)=\pi_r(x;W)<1$ only if she can induce the speakers at $h_5,h_6$ to take distinct, knowledge-transferring actions. They have no useful private information, so this cannot be met, and the only equilibrium that could result is babbling (pp. 247–248).
3. All equilibria with $\pi_r(x;B)=\pi_r(x;W)$ are babbling. $\pi_r=(0,1)$ requires neologisms. So $\pi_r=(1,0)$, and then step 1 gives $\pi_{14}=(1,0,0,1)$ uniquely. The candidates are $\pi=(1,0,0,1,\{0,1\},\{0,1\},1,0)$ (p. 248).
4. *Principal's expected utility after B* (all eight nature-cells weighted, p. 248):
$$\frac{ckb\pi_1U+ck(1-b)\pi_2\underline U+(1-c)kb\pi_3U+(1-c)k(1-b)\pi_4\underline U+c(1-k)b\pi_5U+c(1-k)(1-b)\pi_5\underline U+(1-c)(1-k)b\pi_6U+(1-c)(1-k)(1-b)\pi_6\underline U}{ckb\pi_1+ck(1-b)\pi_2+(1-c)kb\pi_3+(1-c)k(1-b)\pi_4+c(1-k)b\pi_5+c(1-k)(1-b)\pi_5+(1-c)(1-k)b\pi_6+(1-c)(1-k)(1-b)\pi_6}$$
   with $\pi_j=\pi_s(B;h_j)$. After W, the same expression holds with every $\pi_j$ replaced by $1-\pi_j$ (p. 248).
5. $\pi_r(x;B)=1$ is a best response only if the B-value is $\ge0$, and $\pi_r(x;W)=0$ only if the W-value is $\le0$. A nonbabbling equilibrium needs one of these strict, hence one of A or B strict (pp. 248–249).
6. *Check the case $\pi=(1,0,0,1,0,0,1,0)$.* The other three cases for $(\pi_5,\pi_6)$ follow equivalent logic.
   - Sequential rationality at $h_5,h_6$ needs $bZ+(1-b)\underline Z\le0$ and $b\underline Z+(1-b)Z\le0$ (p. 249).
   - W-value numerator: $ck(1-b)\underline U+(1-c)kbU+c(1-k)bU+c(1-k)(1-b)\underline U+(1-c)(1-k)bU+(1-c)(1-k)(1-b)\underline U$. This is $\le0$ iff $\frac{1-k+ck}{1-ck}\ge R$, which is Condition B (p. 249).
   - (added step) Grouping terms: $bU(1-ck)+(1-b)\underline U(1-k+ck)\le0$. Divide by the positive $(b-1)\underline U$.
   - B-value numerator: $ckbU+(1-c)k(1-b)\underline U$. This is $\ge0$ iff $R\ge\frac{1-c}{c}$, which is Condition A (p. 249).
7. *Consistency.* Beliefs are consistent iff
$$\mu(better|B)=\frac{b\cdot P(s{=}B\mid better)}{b\cdot P(s{=}B\mid better)+(1-b)\cdot P(s{=}B\mid worse)}$$
   (my corrected form; the printed denominator differs, see Reading notes). The author argues that in the proposed equilibrium $\mu(better|B)=1$ and that the other three beliefs follow equivalently. So the beliefs are consistent (p. 249).

### Theorem 3.1: the equilibrium exists only if c > .5 (pp. 249–250)
- Let $f=(1-k)[\pi_5c+\pi_6(1-c)]$ and $g=(1-k)[(1-\pi_5)c+(1-\pi_6)(1-c)]$.
- A and B are necessary (not sufficient), and they together require $\frac{k-ck+f}{ck+f}\le\frac{ck+g}{k-ck+g}$ (p. 249).
- Multiply each side by its denominator and divide by $k>0$: $k+f+g\le 2ck+2fc+2gc$. Divide by $2k+2f+2g$ to get $c>.5$ (p. 250).
- (added step) The printed chain gives $\le$. Strictness comes from the requirement that at least one of A, B is strict.

**Theorem 3.2: the equilibrium exists only if k > 0.** If $k=0$, both expected utilities equal 0, so neither inequality can be strict (p. 250).

**Corollaries.** The equilibrium does not require $n_c=common$ (Thm 3.1) or $n_k=n_b$ (Thm 3.2). It is $c$ and $k$, the principal's beliefs, that matter, not the speaker's actual type (p. 250).

**Intuition note.** Whether the principal follows a message depends on how she weighs the chance that it comes from a helpful or a harmful speaker, together with the stakes (the ratio $R$). Combining Conditions A and B leaves $c>.5$ as a necessary requirement: she must think common interests more likely than not. If $k=0$ the speaker certainly knows nothing, so his signal gives her nothing to learn.

### Extension 1: Verification (pp. 250–251)
- **Premise.** After the signal, nature replaces it with the true state $n_b$ with probability $0<v<1$ and does nothing with probability $1-v$. Neither player observes this draw. The speaker's strategy becomes $\pi_s(s;h_s,v)$, and the principal's and the beliefs likewise depend on $v$.
- $v=0$ is the basic model. $v=1$ is trivial. A principal who knows whether verification occurred is a trivial variant (p. 250).
- **Proposition 3.2.** The only nonbabbling, non-neologistic equilibria have the strategy rules as printed for Proposition 3.1 (the source says differences from Proposition 3.1 are in bold, which I cannot distinguish in the page image). They require (with $R$ as above) (p. 251):

$$\text{A': }\frac{(1-v)[(1-c)k+(1-k)(\pi_5c+\pi_6(1-c))]}{(v/b)+(1-v)[ck+(1-k)(\pi_5c+\pi_6(1-c))]}\le R$$
$$\text{B': }\frac{(v/(1-b))+(1-v)[ck+(1-k)((1-\pi_5)c+(1-\pi_6)(1-c))]}{(1-v)[(1-c)k+(1-k)((1-\pi_5)c+(1-\pi_6)(1-c))]}\ge R$$
at least one strict (p. 251).
- **Corollary 1:** the equilibria do not require $c>.5$. The authors summarize: "verification is a substitute for common interests" (p. 251).
- **Corollary 2:** if $\underline Z\ne0$, increases in $v$ make participation less valuable for speakers with an incentive to deceive, but not for other speakers (p. 251).
- The proofs are moved to the authors' website. They are analogous to Proposition 3.1 (p. 251).

**Intuition note.** When the true state is sometimes revealed anyway, a liar's message is sometimes overwritten. The principal can then rely on the signal even if she doubts the speaker's motives.

### Extension 2: Penalties for lying (pp. 251–253)
- **Premise.** A false signal costs the speaker $pen\ge0$, subtracted from the payoffs in the lying cases. Truthful speakers have the basic payoffs (pp. 251–252).
- **Equilibria with $\pi_{14}=(1,0,0,1)$ and $\pi_r=(1,0)$** (knowledgeable common-interest speakers truthful, conflicting ones lying) are possible only if the penalty is below the smaller of $U$ and $|\underline U|$, "i.e., all possible lies are worthwhile" (p. 252). This is as printed (see Reading notes).
- Penalties also create a second set of equilibria in which the penalty makes the speaker at $h_3$ and/or $h_4$ truthful (p. 252). Notation: $\pi_{12}=(\pi_s(B;h_1),\pi_s(B;h_2))$, $\pi_3=\pi_s(B;h_3)$, $\pi_4=\pi_s(B;h_4)$.
- **Proposition 3.3 (Type I: penalties can affect persuasion).** The only Type I equilibria have (p. 252):
  - $\pi_{12}=(1,0)$.
  - $\pi_3=1$ if $\underline Z\ge-pen$, else 0.
  - $\pi_4=1$ if $Z\ge pen$, else 0.
  - $\pi_5=1$ if $bZ+(1-b)(\underline Z-pen)+b\,pen\ge0$, else 0.
  - $\pi_6=1$ if $b\underline Z+(1-b)(Z-pen)+b\,pen\ge0$, else 0.
  - $\pi_r=(1,0)$.

 They require (with $\pi_5,\pi_6$ in the brackets as before):
$$\frac{(1-c)k\pi_4+(1-k)[\pi_5c+\pi_6(1-c)]}{ck+(1-c)k\pi_3+(1-k)[\pi_5c+\pi_6(1-c)]}\le R,\quad \frac{ck+(1-c)k(1-\pi_4)+(1-k)[(1-\pi_5)c+(1-\pi_6)(1-c)]}{(1-c)k(1-\pi_3)+(1-k)[(1-\pi_5)c+(1-\pi_6)(1-c)]}\ge R$$
 with at least one strict (p. 252, continued on p. 253).
- **Corollary 1:** these equilibria do not require $c>.5$. Even a penalty that keeps speakers at some information sets from lying is sufficient to induce persuasion in a range of cases where it is not otherwise possible (p. 253).
- **Corollary 2 (Type II: speaker strategies change, but the principal may ignore him).** Written $\pi=(\pi_{12},\pi_3,\pi_4,\pi_5,\pi_6,\pi_r)$, the only Type II equilibria are (p. 253):
  - $(1,0,1,0,1,1,0,0)$ iff $pen>0$, $R\le1-k$ and $b\ge1/2$.
  - $(1,0,1,0,0,0,1,1)$ iff $pen>0$, $R\ge1/(1-k)$ and $b\le1/2$.
  - The following require $b=1/2$ (with $pen>0$):
    - $(1,0,1,0,0,1,0,0)$ if $R\le\min\big(\frac{k}{c-ck}+1,\ \frac{(1-k)(1-c)}{k+(1-k)(1-c)}\big)$.
    - $(1,0,1,0,0,1,1,1)$ if $R\ge\max$ of the same two terms.
    - $(1,0,1,0,0,0,0,0)$ if $R\le\min\big(1+\frac{k}{(1-k)(1-c)},\ \frac{c-ck}{c+k-ck}\big)$.
    - $(1,0,1,0,0,0,1,1)$ if $R\ge\max$ of those two terms.
- Proofs are on the website, analogous to Proposition 3.1 (p. 253).

**Intuition note.** A lying fee shrinks the gain from deceiving, so some would-be liars tell the truth. In some cases that makes persuasion possible even when the principal does not think the speaker is probably friendly ($c\le .5$).

### Extension 3: Costly effort with continuous types (pp. 253–255)
- **Purpose.** Signalling through actions, not words. Types are drawn from continua, and earlier theorems also hold in the continuous case (p. 253).
- **Premises (p. 254).**
  - Ideal points: principal $p\in[0,1]$, speaker $sp\in[0,1]$. Alternatives $x,y\in[0,1]$.
  - Nature draws $n_b=x$ from a distribution $X$ with known support, and $n_c=sp$ from a distribution $SP$. It is common knowledge that $x$ is drawn from $X$; the principal knows that $sp$ is drawn from $SP$.
  - The speaker knows both draws, i.e. $k=1$. The principal does not know where x lies, so she may not know whether x or y is closer to $p$.
  - The speaker chooses $s\in\{cost,0\}$. If he pays, the principal chooses x or y. If not, the outcome is y.
  - Utilities: speaker $-|x-sp|-cost$ (pays, x chosen), $-|y-sp|-cost$ (pays, y chosen), $-|y-sp|$ (does not pay). Principal $-|x-p|$ or $-|y-p|$.
  - Tie-breaks: the speaker does not pay if indifferent (the printed sentence says "the principal does not pay"; I read it as the speaker). The principal chooses y if indifferent (pp. 254–255).
  - Beliefs are now $\mu(x|cost)$. There is only one nonbabbling equilibrium, and neologisms have no meaning (p. 255).
- **Logic.** The speaker wants the alternative closest to $sp$. Paying is worthwhile only if it changes the outcome and $|y-sp|-|x-sp|>cost$. The text says that if $x\in[y-cost,y+cost]$ influence is not worthwhile, and then says that on seeing payment the principal can infer $x\in[y-cost,y+cost]$ (p. 255; see Reading notes). If the inference differs from her priors, persuasion can occur (p. 255).
- **Proposition 3.4.** In the only nonbabbling equilibrium, the speaker pays and the principal chooses x iff both of these hold (p. 255):
$$-\int_{\min(0,y-cost)}^{y-cost}|x-p|\,dX-\int_{\min(y-cost,1)}^{1}|x-p|\,dX>-|y-p|\quad\text{and}\quad -|x-sp|-cost>-|y-sp|.$$
 Otherwise the speaker does not pay and the outcome is y. (Integral limits as printed; the leading minus is as I read it; see Reading notes.)
- **Corollary:** persuasion here does not require probability of common interests > .5. The proof is on the authors' website (http://polisciexplab.ucsd.edu), analogous to Lupia (1992) (p. 255).

**Intuition note.** Effort is a signal because the speaker finds it worth paying only if it would change the outcome and x is closer to his ideal point than y by more than the cost. The principal can use that fact to update her beliefs about where x lies, and persuasion can occur if the inference differs from her priors; no probability of common interests above .5 is required.

### Theorem 3.3 (p. 255–256)
- The following are **individually necessary and collectively sufficient** for persuasion: the principal perceives the speaker to be trustworthy; she perceives the speaker to be knowledgeable; and the signal, if true, implies that her prior beliefs are insufficient for reasoned choice (p. 255).
- With no external forces, persuasion requires perceived common interests ($c>.5$) and perceived knowledge ($k>0$). As verification likelihood, lying penalty or costly effort rises, the required common interest falls ($c$ can be below .5). External forces are substitutes for common interests (p. 256).
- **Proof (as given):** necessity and sufficiency are proven in Propositions 3.1–3.4. The no-force statement is Theorems 3.1 and 3.2. The external-force statement is Corollary 1 to Propositions 3.2, 3.3 and 3.4 (p. 256).

**Intuition note.** A listener needs a reason to believe a message. In the basic model that reason is her belief that common interests are more likely than not. The appendix shows that verification, penalties for lying, or costly effort can lower how much of this is required ($c$ can be below .5). Theorem 3.3 still lists perceived trustworthiness as individually necessary.

## Toy example (ours, not from the text)
Take $b=.5$, $U=1$, $\underline U=-1$, so $R=\frac{.5\cdot1}{(-.5)(-1)}=1$. Take $Z=1$, $\underline Z=-2$. Then $bZ+(1-b)\underline Z=.5-1=-.5<0$ and $b\underline Z+(1-b)Z=-1+.5=-.5<0$, so ignorant speakers send W ($\pi_5=\pi_6=0$). Let $k=.5$.

*Case c = .6.*
- Condition A: $\frac{(1-c)k}{ck}=\frac{.2}{.3}=.667\le1$ ✓.
- Condition B: $\frac{ck+(1-k)}{(1-c)k+(1-k)}=\frac{.3+.5}{.2+.5}=\frac{.8}{.7}=1.143\ge1$ ✓, strict.
- The persuasion equilibrium exists.
- Direct check, signal B: $ckb\,U+(1-c)k(1-b)\underline U=.6(.5)(.5)(1)+.4(.5)(.5)(-1)=.15-.1=.05\ge0$, so x after B.

*Case c = .4, no verification.*
- Condition A: $\frac{.6\cdot.5}{.4\cdot.5}=1.5\le1$? ✗.
- Signal B: $.4(.5)(.5)(1)+.6(.5)(.5)(-1)=.1-.15=-.05<0$, so she would not follow B.
- No nonbabbling equilibrium of this form.

*Case c = .4 with verification v = .5.*
- Verified signals add $v\cdot b\cdot U=.25$ to the B-value, so the B-value is $(1-v)(-.05)+.25=.225\ge0$ ✓.
- The W-value is $(1-v)(.05)+v(1-b)\underline U=.025-.25=-.225\le0$ ✓. Here $.05=bU(1-ck)+(1-b)\underline U(1-k+ck)=.4-.35$.
- Persuasion works again with $c<.5$, as in Corollary 1 to Proposition 3.2 (my direct calculation, consistent with A' and B').

## Concepts
- [[conditions for persuasion (Lupia–McCubbins)]] — trusted speaker, perceived knowledge, and a signal showing the prior is insufficient: individually necessary, collectively sufficient (Thm 3.3, p. 255)
- [[sequential equilibrium]] (new) — strategy profile plus belief system, sequentially rational and consistent; refined so the principal ignores off-path signals (pp. 242–245)
- [[babbling equilibrium]] (new) — equilibrium where the signal is uninformative or ignored; acknowledged but not pursued (p. 245)
- [[neologistic equilibrium]] (new) — equilibrium where signals have reversed meanings; excluded by assuming focal meanings (p. 246)
- [[verification (external force)]] (new) — nature reveals the true state with probability $v$ in place of the signal; substitutes for common interests (p. 250)
- [[penalty for lying]] (new) — a cost $pen$ paid by the speaker for a false signal (p. 251)
- [[costly effort signalling]] (new) — the speaker's action, not words, as signal, informative because it is only worth the cost under some conditions (p. 253)
- [[principal–agent problem / delegation]] — the principal is uncertain about the speaker's knowledge and interests, though the unit does not use these terms (pp. 240–241)

## Canonical instances
- [[lupia-mccubbins-communication-game]] (new) — speaker signals B/W to a principal choosing x or y, with hidden state, knowledge and interests (p. 240)
- [[spatial-signalling-game]] (new) — continuous-type model where the principal infers the location of x from the speaker's costly action (p. 254)

## Bridges (candidates)
- [structural-analogy] babbling and non-neologistic equilibria ↔ game theory: cheap-talk signalling games — the text itself cites Crawford–Sobel and Farrell for this class (p. 245)
- [structural-analogy] costly effort as signal ↔ costly signalling: an action is informative because it is worth its cost only for some types (p. 253)
- [metaphor] verification and penalties as "external forces" ↔ institutional design: external rules and monitoring replace trust between parties

## Questions this raises
- If only c matters (not the speaker's real type), how do real principals form beliefs about c and k?
- Can the three external forces be combined, and do their effects add up?
- What happens with many speakers or a principal receiving conflicting messages?
- Is the focal-meaning (non-neologistic) assumption as harmless as claimed when signals are actions or cultural cues?

## Reading notes
- Printed page = pdf − 16 (pdf 256 = p. 240). Source pages 240–256.
- The text layer garbles the underbars on $U,Z$ (so $U$ vs $\underline U$ is lost) and many fractions. I read them from the images. In Prop. 3.1 and 3.3, I assigned the underbars on the $\pi_5,\pi_6$ sums from the information-set logic of p. 247. The printed underbars are hard to see.
- p. 246: Condition B's lower numerator prints "(−k)"; context requires $(1-k)$.
- p. 249: the printed Bayes denominator reads "$(1-b)\times$ probability that $s=W$ if $n_b=better$". Bayes' rule needs $P(s{=}B\mid worse)$. With the corrected denominator, $\mu(better|B)$ would be below 1 in the equilibrium whenever liars at $h_4$ send B, which seems at odds with the author's claim that it equals 1 (my observation).
- p. 248: in each principal-utility sum, the fifth and sixth terms are both labelled $h_5$ and the seventh and eighth both $h_6$. These are the two states within $h_5$ and $h_6$, so this is not an error.
- p. 252: the penalty bound says "the smaller of $U$ and $|\underline U|$". From the Prop. 3.3 conditions ($\underline Z\ge-pen$, $Z\ge pen$), it is probably $Z,\underline Z$ that is meant (my inference).
- p. 253: Corollary 1 text reads "Unlike the equilibria in the basic model, but the equilibrium of the verification extension". It presumably means "like" (my inference). The text layer shows "b−3" in one Type II condition. I took it as $b-1$.
- p. 255: the text says that if the speaker pays, the principal infers $x\in[y-cost,y+cost]$. This contradicts the preceding sentence and is probably a misprint for "outside". The second integral's lower limit also prints as $\min(y-cost,1)$, probably $y+cost$. The leading minus sign before the first integral is not clearly visible.
- Proofs of Props. 3.2, 3.3 and 3.4 (with corollaries) are not in the print; they are on the authors' website (pp. 251, 253, 255).

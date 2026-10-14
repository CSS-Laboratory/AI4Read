---
id: lupia-1998-dilemma/app-ch02
work: lupia-1998-dilemma
unit: "Afterword and Appendix to Chapter 2 (formal model of attention)"
pages: 229–239
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Afterword and Appendix to Chapter 2: the formal model of attention

## L0 — One line
In a decision-theoretic model, a person pays for information only when its net expected value after cost is positive, and more information is neither necessary nor sufficient for reasoned choice; the Afterword concludes that reasoned choice needs accurate predictions, not knowledge of every detail.

## L1 — The gist (≤ 120 words)
The Afterword says people can choose well without knowing every detail. They need accurate predictions; earlier chapters name conditions under which persuasive, enlightening speakers help uninformed people choose well. The appendix formalizes the Chapter 2 theory of attention. One principal with an ideal point chooses between two uncertain alternatives. She may pay a cognitive cost to learn where $x$ is, or where both are, and each payment works only with some probability. Proposition 2.1 gives her payment rule. Theorem 2.1 says more information is neither necessary nor sufficient for reasoned choice; its corollaries are proved with the rule. Theorem 2.2 (not proved in detail here) says people have an incentive to ignore many stimuli when attention is costly.

**Prerequisites:** expected utility; integrals over probability distributions; proof by contradiction; the idea of an ideal point in a one-dimensional policy space.

## L2 — Key ideas (5–10 bullets)
- Reasoned choice needs the ability to predict consequences, not knowledge of all pertinent details (p. 229).
- The appendix builds three small models in a hierarchy: attention, then communication, then delegation. The authors say smaller models should let more readers follow each conclusion (p. 233).
- The attention model has a single actor, so it uses decision theory and not game theory (p. 234).
- Information is worth buying only if it can prevent a costly mistake. Incomplete information can also cause a mistake (pp. 235–236).
- Proposition 2.1 is a payment rule that compares the net value of full information, partial information and none (p. 236).
- Theorem 2.1: more information is neither necessary nor sufficient for reasoned choice (pp. 237–238).
- Corollaries 1–3 say how attention responds to changes in the parameters: a higher expected cost of a mistake, or a higher chance that attention prevents one, either induces attention or has no effect. If the chance that attention causes a mistake rises by more than the chance that it prevents one, attention is reduced or unchanged (p. 238).
- Theorem 2.2 (people have an incentive to ignore many stimuli) needs two extra premises, which the model represents by making $c_x$ and $c_{xy}$ high relative to all other parameters; the authors say it then follows straightforwardly (p. 239).

## L3 — Walkthrough

### Afterword (p. 229)
- The authors decline to write a nostalgic or sprawling conclusion. They cite the Chapter 2 lesson: when many stimuli compete, attending to any one has a high opportunity cost, so people should attend only to stimuli very likely to avert very costly mistakes (p. 229).
- Their conclusion: people who want to choose in a reasoned way need not know all pertinent details of their actions' consequences. They need the ability to generate accurate predictions (p. 229).
- Earlier chapters identified conditions under which speakers, whose attributes or institutional contexts make their statements persuasive and enlightening, let uninformed people choose in a reasoned way (p. 229).
- The book is said to show how basic cognition interacts with the incentive-altering effects of institutions to determine each person's capacity for reasoned choice. Its stated use is to help tell competent voters, jurors and legislators from incompetent ones (p. 229).

*Intuition note:* The Afterword's point is that reasoned choice depends on accurate prediction, not on knowing every detail. It says earlier chapters identified speakers and institutional settings that can help people who lack information.

### Appendix intro (p. 233)
- The appendix gives a formal version of the theory to show that conclusions follow from premises. Some proofs are on a web site, at the publisher's request (p. 233).
- The models are small and focused, not one all-encompassing model. The delegation model rests on the communication models, and both rest on the attention model (p. 233).
- Each section states assumptions about player objectives, opportunities and knowledge, then conclusions. Unless stated otherwise, all elements of every model are assumed to be common knowledge (pp. 233–234); these pages do not define the term.

### 1. A model of attention: premises (pp. 234–235)
- A principal has an ideal point $p\in[0,1]$, her most preferred location. She chooses between two exogenous, independently determined alternatives $x,y\in[0,1]$. This is without loss of generality for points in any finite-dimensional space (p. 234).
- There is one actor, so the analysis is decision-theoretic (p. 234).
- Objective: maximize expected utility. *Ex ante* means choosing before exhausting pre-payoff chances to get information. *Ex post* means choosing after exhausting them (p. 234).
- Utility is $-|x-p|$ from $x$ and $-|y-p|$ from $y$. Conclusions hold, or hold in trivial variants, for a large class of quasi-concave utility functions. They only need utility to fall weakly monotonically as distance, or cost, rises (p. 234).
- Beliefs: the true location of $x$ is one draw from distribution $X$, with support on a known subset of $[0,1]$. Likewise $y$ is drawn from $Y$. She does not know which location was drawn (p. 234).
- Sequence: she decides whether to acquire information, then chooses $x$ or $y$, then the game ends and she is paid (p. 235).
- Three options (p. 235):
  - Pay nothing and learn nothing.
  - Pay $c_{xy}>0$ to learn both $x$ and $y$ with probability $q_{xy}$, and nothing with probability $1-q_{xy}$. This is the most detailed information.
  - Pay $c_x>0$ to learn $x$ with probability $q_x$, and nothing with probability $1-q_x$. This is a vaguer signal.
- $c_x,c_{xy}$ are cognitive opportunity costs: the scarce energies needed to acquire information. $q_x,q_{xy}$ are cognitive transaction costs; the $1-q$ terms are frictions in processing a stimulus into a helpful form. All four ($c_x,c_{xy},q_x,q_{xy}$) are fixed and exogenous (p. 235).
- Tie-breaks: if $x,y$ give equal expected utility, she picks $y$. If paying and not paying are equal, she does not pay. If two pieces of information are equal, she pays for the cheaper (p. 235).

### Derivation of the information values (pp. 235–236)
- $CL_p(x)$ is the set of $y$ closer to $p$ than $x$. $CL_p(y)$ is the set of $x$ closer to $p$ than $y$ (p. 235).
- Expected return from learning $x$, given a value of $y$: $\int_{CL_p(y)} |y-p|-|x-p|\,dX$. Given beliefs $Y$: $\iint_{CL_p(y)} |y-p|-|x-p|\,dX\,dY$. The integral runs only over $x$ closer to $p$ than $y$. Paying can help only if it prevents choosing $y$ when $x$ is closer (p. 235).
- Return from paying $c_{xy}$ (p. 235):
  - If $-\!\int|y-p|dY \ge -\!\int|x-p|dX$: $q_{xy}\times\iint_{CL_p(y)}|y-p|-|x-p|\,dX\,dY$.
  - Otherwise: $q_{xy}\times\iint_{CL_p(x)}|x-p|-|y-p|\,dY\,dX$.
- $CL_p(Y)$ is the set of $x$ with $-|x-p|\ge-\!\int|y-p|dY$, so $x$ beats the expected value of $y$. If she knows $y$, $CL_p(y)=CL_p(Y)$. $\neg CL_p(Y)$ is the set of $x$ with $-|x-p|\le-\!\int|y-p|dY$ (p. 236).
- With integrand $|y-p|-|x-p|$ and $dX\,dY$, and regions read from the page (p. 236):
$$B_x=q_x\iint_{CL_p(y),\,CL_p(Y)},\quad L_y=q_x\iint_{CL_p(x),\,CL_p(Y)},\quad B_y=q_x\iint_{CL_p(x),\,\neg CL_p(Y)},\quad L_x=q_x\iint_{CL_p(y),\,\neg CL_p(Y)}.$$
- $B_x$ is the expected benefit of seeing an $x$ that correctly suggests $x$ is closer to $p$ than $y$. $L_y$ is the expected loss from an $x$ that wrongly suggests this. $B_y$ and $L_x$ parallel these. $L_x$ and $L_y$ show when partial information can cause a costly mistake, which is one rational reason not to buy more (p. 236).
- The expected benefit of paying $c_x$ is $B_x-L_y$ if $-\!\int|y-p|dY\ge-\!\int|x-p|dX$, and $B_y-L_x$ otherwise (p. 236).

**Proposition 2.1 (action rule)** (p. 236). Write $E_y=-\!\int|y-p|dY$ and $E_x=-\!\int|x-p|dX$.
- If $E_y\ge E_x$:
  - she pays $c_{xy}$ if $\big[q_{xy}\iint_{CL_p(y)}|y-p|-|x-p|\,dX\,dY\big]-c_{xy}>\max(B_x-L_y-c_x,\,0)$;
  - she pays $c_x$ if $B_x-L_y-c_x\ge[\text{that bracket}]-c_{xy}$ and $B_x-L_y-c_x>0$.
- If $E_x>E_y$: the same two rules hold with $B_y-L_x$ in place of $B_x-L_y$. The bracket is then $q_{xy}\iint_{CL_p(x)}|x-p|-|y-p|\,dY\,dX$.
- Otherwise she does not pay.
- Choice after paying:
  - Having observed both, she chooses $y$ iff $-|y-p|>-|x-p|$.
  - Having observed $x$, she chooses $y$ iff $E_y\ge-|x-p|$.
  - Having observed neither, she chooses $y$ iff $E_y\ge E_x$.
  - Otherwise she chooses $x$.
- The proof is called trivial, because the game is decision-theoretic. To falsify it one must contradict utility maximization or change a definition or the sequence of events (pp. 236–237).

*Intuition note:* She compares three net values: full information, partial information, and none. She buys the best one only if it beats not buying. Partial information can mislead, so it is not always worth buying.

### Conclusions: mapping the model to Chapter 2 (p. 237)
- Expected cost of a mistake: $\iint_{CL_p(y)}|y-p|-|x-p|\,dX\,dY$ if $E_y\ge E_x$, otherwise $\iint_{CL_p(x)}|x-p|-|y-p|\,dY\,dX$ (p. 237).
- Attention to a stimulus is the decision to pay $c_{xy}$ or $c_x$. Inducing attention is a switch from not paying to paying, and reducing attention is the reverse (p. 237).
- The probability that attention suffices to prevent a mistake is $q_{xy}\iint_{CL_p(y)}dXdY$ or $q_x\int_{CL_p(y)}\int_{CL_p(Y)}dXdY$ if $E_y\ge E_x$. Otherwise it is $q_{xy}\iint_{CL_p(x)}dXdY$ or $q_x\int_{CL_p(x)}\int_{\neg CL_p(Y)}dXdY$ (p. 237).
- The probability that attention suffices to cause a mistake is $q_x\int_{CL_p(x)}\int_{CL_p(Y)}dXdY$ if $E_y\ge E_x$, and otherwise $q_x\int_{CL_p(y)}\int_{\neg CL_p(Y)}dXdY$ (p. 237).

**Theorem 2.1: more information is neither necessary nor sufficient for reasoned choice** (pp. 237–238).
- *Not necessary.* Suppose it were necessary and $Y$ had all its support in $CL_p(x)$. By supposition she then could not make a reasoned choice without learning the precise location of $y$. But, also by supposition, she can infer that $y$ is closer to $p$ than $x$ without learning $y$. So learning $y$ is not necessary (p. 237).
- *Not sufficient.* Since she may choose not to learn, sufficiency would require that knowing $x$ or $y$ alone suffice. Take $p=.3$, $x=.8$, $Y$ uniform. Then the expected utility of $y$ exceeds that of $x$, so she chooses $y$ after learning $x$. If $y=.9$, learning $x$ was not enough for a reasoned choice (p. 238).
- (added step) $E|y-.3|=(.3^2+.7^2)/2=.29<|.8-.3|=.5$, and the true $|.9-.3|=.6>.5$, so $y$ was the mistake.

**Corollaries 1 and 2:** an increase in the expected cost of a mistake, or in the probability that attention is sufficient to prevent a mistake, either induces attention or has no effect (p. 238).
- Proof for the case $E_y\ge E_x$; the other case is said to follow straightforwardly. A rise in the expected cost of a mistake raises both the integral and the bracketed $q_{xy}$ term minus $c_{xy}$ (printed on p. 238 with region $CL_p(x)$). By Proposition 2.1 this could only induce her to pay for full information (p. 238). Similar reasoning is said to give the same effect for a rise in the probability that attention prevents a mistake.

**Corollary 3:** if an increase in the probability that attention is sufficient to *cause* a mistake exceeds the consequent increase in the probability that it is sufficient to *prevent* one, attention is reduced or unchanged (p. 238).
- Proof: this means $\int_{CL_p(x)}\int_{CL_p(Y)}dXdY-\int_{CL_p(y)}\int_{CL_p(Y)}dXdY$ rises. That lowers $B_x-L_y-c_x$, so she could only stop paying $c_x$; otherwise the increase has no effect (p. 238).

*Intuition note:* A higher expected cost of a mistake, or a better chance that the information prevents one, can only induce attention or leave it unchanged. If the chance that information misleads rises by more than the chance that it helps, attention can only fall or stay the same.

**Theorem 2.2: people have an incentive to ignore many stimuli** (pp. 238–239).
- It needs two extra premises. First, thousands of stimuli compete for attention. Second, the opportunity cost of attention is much higher than when only one or two stimuli compete. In the model this means $c_x$ and $c_{xy}$ are high relative to all other parameters. The theorem and its corollary "follow straightforwardly" (p. 239).
- The section on communication and the section on delegation lie outside these pages.

## Toy example (ours, not from the text)
Let $p=.5$. Only the option of paying $c_x$ to learn $x$ is available (no $c_{xy}$ option). The alternative $y$ is known to be at $.7$, so $|y-p|=.2$. The alternative $x$ is at $.5$ with probability $.3$ (distance $0$) or at $.9$ with probability $.7$ (distance $.4$).
1. $E|x-p|=.3(0)+.7(.4)=.28$, so $E_x=-.28<E_y=-.2$. With no information she chooses $y$.
2. Choosing $y$ is a mistake only if $x=.5$. The cost is $.2-0=.2$ with probability $.3$, so the expected cost of a mistake is $.06$.
3. Because $y$ is known, $CL_p(Y)=CL_p(y)$, so $L_y=0$ (added step). With $q_x=.8$, $B_x-L_y=.8\times.06=.048$.
4. If $c_x=.02$: net $.028>0$, so she pays. If $c_x=.05$: net $-.002<0$, so she ignores the stimulus.
5. Raise $q_x$ to $1$ (Corollary 2): benefit $.06>.05$, so she now pays. Attention is induced.

## Concepts
- [[reasoned-choice]] (new) — the kind of choice that, the authors conclude, requires the ability to generate accurate predictions, not knowledge of all pertinent details; these pages do not define it (p. 229).
- [[attention-model]] (new) — decision-theoretic model in which a principal pays to learn alternatives' locations (p. 234).
- [[cognitive-opportunity-cost]] (new) — $c_x,c_{xy}$: scarce energy needed to acquire information (p. 235).
- [[cognitive-transaction-cost]] (new) — $q_x,q_{xy}$ (the $1-q$ terms are frictions in processing a stimulus into a helpful form) (p. 235).
- [[expected-cost-of-a-mistake]] (new) — in the model, $\iint_{CL_p(y)}|y-p|-|x-p|\,dX\,dY$ if $E_y\ge E_x$, and the mirror integral otherwise (p. 237).
- [[spatial-model-of-voting]] — here, utility is minus distance from an ideal point on $[0,1]$ (p. 234).
- [[common-knowledge]] (new) — the authors assume all elements of every model are common knowledge, unless stated otherwise; the term is not defined on these pages (pp. 233–234).

## Canonical instances
- [[theorem-2-1-counterexample]] (new) — $p=.3$, $x=.8$, $y=.9$, $Y$ uniform: learning $x$ alone does not secure a good choice (p. 238).

## Bridges (candidates)
- [structural-analogy] Theorem 2.2 (ignore stimuli when attention is costly) ↔ political-science: [[rational-ignorance]] — both say ignorance can be rational when information costs exceed its expected value.
- [structural-analogy] Proposition 2.1 payment rule ↔ decision theory: value of information — both compare expected gain from learning with its cost.
- [structural-analogy] Distance-based utility on $[0,1]$ ↔ [[spatial-model-of-voting]] — the same setup with the principal as voter, but used here for information choice.

## Questions this raises
- How do speakers' credibility and institutions change $q_x$ or the beliefs $X,Y$ in the later communication model?
- Are $c_x$ and $q_x$ really exogenous? What changes if they depend on prior knowledge?
- How would the rule change if utility were not distance-based but only quasi-concave, as the authors claim?
- Can the model's predictions about which stimuli people ignore be tested empirically?

## Reading notes
- Page offset: printed = pdf − 16. Pdf 246 and 248 are blank. Pdf 247 holds only the heading "Appendices".
- This unit includes the Afterword (p. 229; p. 230 is blank) and only the attention section of the appendix. The communication and delegation sections are not in these pages.
- The text layer for pp. 235–238 is badly garbled. I checked the equations against the page images.
- The integration regions of $B_x,L_y,B_y,L_x$ are legible in the p. 236 image and match the probability definitions on p. 237. In the Corollaries 1–2 proof (p. 238) the printed region is $CL_p(x)$, whereas the Proposition 2.1 bracket for the same case uses $CL_p(y)$; the source does not comment.
- The printed definition of $L_x$ has "$q_x =$" where "$q_x\times$" is clearly meant.
- Proposition 2.1 says she chooses $y$ iff $-|y-p|>-|x-p|$ after observing both. This is a strict inequality, while the tie-break rule (p. 235) says ties go to $y$. These pages do not address this.
- In the Theorem 2.1 proof (p. 238), "expected value of $x$" appears where the expected utility of $x$ is meant.

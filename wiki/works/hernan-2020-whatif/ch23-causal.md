---
id: hernan-2020-whatif/ch23-causal
work: hernan-2020-whatif
unit: 23 Causal mediation
pages: 323-331
fields: [bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Causal mediation

## L0 — One line
The standard "pure direct / total indirect" mediation effects are cross-world quantities that no experiment can verify, so the authors prefer to reframe mediation as the effect of interventions on separable components of treatment, whose assumptions can in principle be tested in a randomized trial.

## L1 — The gist (≤ 120 words)
How can we split a treatment's effect into a part through a mediator and a part not through it? The standard answer defines pure direct and total indirect effects. These involve cross-world counterfactuals (outcomes under two treatment values at once), and the proof that the mediation formula identifies them needs an unverifiable cross-world independence (assumed in the NPSEM-IE model). The authors instead imagine that treatment splits into separable components, one acting on the mediator and one on the outcome. Effects of intervening on these components can be identified, and they can be checked in a future randomized trial. The identifying formula is the same mediation formula. The approach does not need well-defined interventions on the mediator itself.

**Prerequisites:** counterfactual (potential-outcome) notation; exchangeability, consistency, positivity; g-formula; causal DAGs and SWIGs; the front-door formula (Fine Point 9.5).

## L2 — Key ideas (5–10 bullets)
- The total effect splits into a pure direct effect and a total indirect effect. Both are cross-world quantities, because they use outcomes indexed by two different treatment values at once (p. 324).
- The mediation formula $\sum_m E[Y|A=1,M=m]\Pr[M=m|A=0]$ identifies the cross-world mean, but its proof needs a cross-world independence. This independence is assumed under an NPSEM-IE and not under an FFRCISTG model (two kinds of counterfactual model). The authors privilege the FFRCISTG (pp. 324–325).
- Skeptics say a cross-world parameter matches no intervention. NPSEM-IE advocates answer with a nicotine-free-cigarette story, which splits $A$ into separable components $N$ and $O$ (pp. 325–326).
- Under that story, the mediation formula is the g-formula for $E[Y^{n=0,o=1}]$. Positivity fails, but identification can still hold, because the g-formula is a function of the observed data; this follows from the deterministic arrows and the no-direct-effect assumptions (i) and (ii) (p. 326, Technical Point 23.2).
- A new three-arm trial can refute the story: compare $E[Y|N=0,O=1]$ with the mediation formula. Follow-up checks help investigate which of assumptions (i)–(iii) failed; separating (i) from (iii) needs a further trial that also intervenes on $M$ (pp. 327–328).
- Interventionist mediation does not need well-defined interventions on the mediator, and it supports talk with subject-matter experts (p. 330).
- The front-door formula can be derived in the same way, with a deterministic copy of a variable (Technical Point 23.3, p. 331).
- Real mediation analyses are observational and rest on "more heroic assumptions" than non-mediation analyses (p. 331).

## L3 — Walkthrough

### Introduction (p. 323)
Part III gave effects of time-varying treatments. It did not ask *how* treatment acts. Mediation is a special case of time-varying treatment: two variables, treatment and mediator, at different times (p. 323). The chapter builds on hypothetical interventions that map into a target trial. The authors claim that, unlike approaches based on pure direct and total indirect effects, this framework opens the door to empirical verification of the causal estimates (p. 323).

### 23.1 Mediation analysis under attack (pp. 323–325)
**Setting.** A randomized trial of smokers: $A=0$ cessation, $A=1$ continued smoking. Adherence is perfect. The outcome $Y$ is myocardial infarction at 1 year, and $E[Y|A=1]>E[Y|A=0]$ (p. 323). The mediator $M$ is hypertension at 6 months. No one has $Y$ before 6 months. Figure 23.1 is $A\to M\to Y$ plus $A\to Y$, assuming interventions on $M$ are well defined (p. 323).

**Definitions (Robins–Greenland).**
- Pure direct effect: $E[Y^{a=1,M^{a=0}}]-E[Y^{a=0,M^{a=0}}]$. It is the effect of $A$ if each person's $M$ were set to the value $M^{a=0}$ it would take under $A=0$ (pp. 323–324).
- Total indirect effect: $E[Y^{a=1,M^{a=1}}]-E[Y^{a=1,M^{a=0}}]$ (p. 324).
- Their sum is, by consistency, the total effect $E[Y^{a=1}]-E[Y^{a=0}]$ (p. 324).
- Pearl calls these the natural direct and natural indirect effects (margin, p. 324).

**Cross-world.** $M^{a=0}$ is unknown for people who actually continued smoking. $E[Y^{a=1,M^{a=0}}]$ involves $a=1$ and $a=0$ for the same person in the same world, which cannot happen, so it is a *cross-world quantity* (p. 324).

**Identification.** With no unmeasured common causes of $M$ and $Y$ (Figure 23.1), the mediation formula identifies $E[Y^{a=1,M^{a=0}}]$ (p. 324), where the mediation formula is:
$$\sum_m E[Y\mid A=1,M=m]\,\Pr[M=m\mid A=0]$$
If unmeasured common causes of $M$ and $Y$ were present, no direct effects could be identified, controlled or pure (p. 324).

**Technical Point 23.1 (proof, p. 324).**
$$E[Y^{a=1,M^{a=0}}]=\sum_m E[Y^{a=1,m}\mid M^{a=0}=m]\Pr[M^{a=0}=m]\quad\text{(laws of probability)}$$
$$=\sum_m E[Y^{a=1,m}]\Pr[M^{a=0}=m]\quad\text{(cross-world independence } Y^{a=1,m}\perp\!\!\!\perp M^{a=0})$$
$$=\sum_m E[Y|A=1,M=m]\Pr[M=m|A=0]\quad\text{(exchangeability and consistency)}.$$

**The catch (pp. 324–325).** The cross-world independence cannot be seen for one individual in one world, so no experiment that randomizes $A$ and $M$, singly or jointly, can verify it (p. 325). It is assumed under an NPSEM-IE but not under an FFRCISTG model. The FFRCISTG is the model used throughout the book (p. 324). The authors privilege the FFRCISTG because they want methods whose results are, in principle, verifiable (p. 325). Under an FFRCISTG, the pure direct and total indirect effects are not point identified, but sharp bounds exist (Robins and Richardson 2010; margin, p. 325). In a few unusual cases a crossover trial could identify the cross-world value (margin, p. 324). **Objection of some policy makers:** they find a cross-world parameter to be without policy or public health importance because it does not correspond to any intervention (p. 325).

> *Intuition note.* The mediation formula looks like a free lunch: it identifies something no experiment can reach. The price is an independence assumption about outcomes in two worlds that never co-exist, so the data cannot check it.

### 23.2 A defense of mediation analysis (pp. 325–327)
**NPSEM-IE advocates' argument (the investigators).** Suppose nicotine-free cigarettes become available in a year, and the policy goal is their effect on heart disease. Suppose strong experimental evidence for (i) all of nicotine's effect on $Y$ goes through $M$, and (ii) non-nicotine components have no direct effect on $M$. Then a smoker of nicotine-free cigarettes would have hypertension status equal to that under no cigarettes. So $E[Y^{a=1,M^{a=0}}]$ would be the risk if all smokers switched, and the mediation formula computes it (p. 325).

**Authors' comment.** The story is about an intervention on nicotine content that does not mention $M$. Assumptions (i) and (ii) concern variables absent from Figure 23.1 (p. 325).

**Separable components.** $A$ is decomposed into $N$ (nicotine) and $O$ (other components). $N$ affects $M$ but not $Y$ directly. $O$ affects $Y$ directly but not $M$. Each can in principle be intervened on separately, and $Y^{n=0,o=1}$ is the outcome with only nicotine removed (pp. 325–326).

**Figure 23.2** (FFRCISTG). $N$ and $O$ are binary. The arrows $A\to N$ and $A\to O$ are deterministic, since in the trial $A=N=O$ (p. 326). The missing arrow $N\to Y$ encodes (i). The missing arrow $O\to M$ encodes (ii). These are "no controlled direct effect" assumptions (p. 326). Figure 23.3 is the SWIG. If $O$ is not a cause of $M$ for every individual, $M^{n,o}$ can be written $M^n$ (p. 326).

**Technical Point 23.2 (p. 326): the mediation formula is a g-formula.**
- Exchangeability holds for $N,O$ by Figure 23.3. No one has $(N=0,O=1)$, so positivity fails.
- Given exchangeability and consistency, positivity is sufficient, not necessary, for g-formula identification. What is needed is that the g-formula be a function of the observed data distribution.
- With $N$ and $O$ data, the g-formula would be
$$\sum_m E[Y|O=1,M=m]\Pr(M=m|N=0).$$
This is because $N$ is not a parent of $Y$ and $O$ is not a parent of $M$.
- Since $O=1$ iff $A=1$ and $N=0$ iff $A=0$, it can be rewritten as $\sum_m E[Y|A=1,M=m]\Pr(M=m|A=0)$, the mediation formula.
- The derivation is somewhat heuristic because of null sets caused by determinism. Robins et al. (2022) give a rigorous proof via the SWIG Markov property (p. 326).

**Lessons (pp. 326–327).**
- For someone who already accepts an NPSEM-IE, the story does not help identification. It only shows that the cross-world mean encodes the public-health parameter $E[Y^{n=0,o=1}]$ (p. 327).
- For an FFRCISTG believer, the story gives the interventional meaning and also identification, by the g-formula or equivalently the mediation formula (p. 327).
- If absent arrows mean no direct effect for all individuals, $Y^{a=1,M^{a=0}}$ and $Y^{n=0,o=1}$ are equal for every individual (p. 327).
- Separable direct effect of $N$: $E[Y^{n=1,o=1}]-E[Y^{n=0,o=1}]$. It is a controlled direct effect for $N$ and equals the total indirect effect $E[Y^{a=1}]-E[Y^{a=1,M^{a=0}}]$ (p. 327).
- The text also states that $E[Y^{n=1,o=1}]-E[Y^{n=1,o=0}]$ equals the pure direct effect $E[Y^{a=1,M^{a=0}}]-E[Y^{a=0}]$ (p. 327; see Reading notes).

> *Intuition note.* The cross-world "nicotine-free" world becomes a real world if nicotine can be removed. Then the strange quantity equals an ordinary counterfactual under a real intervention, and ordinary g-formula reasoning applies. Positivity can fail and identification can still hold, because the formula only needs observed data.

### 23.3 Empirically verifiable mediation (pp. 327–329)
The interventional reading holds only if the $N$/$O$ story is correct and Figure 23.3 is an FFRCISTG. Its advantage is that the story can in principle be refuted (p. 327).

**New trial.** Three arms: cessation ($A=N=O=0$), standard cigarettes ($A=N=O=1$), nicotine-free cigarettes ($N=0,O=1$). The first two arms repeat the original trial. With no temporal trends and negligible sampling variability, their means should match the original trial (p. 327). By randomization, $E[Y|N=0,O=1]=E[Y^{n=0,o=1}]$. If the story is right, it equals the mediation formula from the first trial (p. 327).

**If they differ,** at least one assumption is wrong: (i) no direct effect of nicotine on $Y$; (ii) no direct effect of non-nicotine components on $M$; (iii) no unmeasured common cause $U$ of $M$ and $Y$ (p. 327). Follow-up checks:
- $E[M|N=0,O=1]-E[M|N=0,O=0]\ne0$ refutes (ii). Add arrow $O\to M$ (pp. 327–328).
- $E[Y|N=1,O=1,M=m]-E[Y|N=0,O=1,M=m]\ne0$ for some $m$ means (i) is refuted (add $N\to Y$) or a common cause $U$ of $M$ and $Y$ exists (p. 328).

**Fine Point 23.1 (p. 328).**
- To tell (i) from (iii), run an 8-arm trial that also intervenes on $M$. If $N$ has no direct effect except through $M$, then $N\perp\!\!\!\perp Y\mid M,O$ in that trial. If $M$ and $Y$ share no unmeasured common cause, the distribution of $Y$ given $M$ within levels of $N,O$ is the same in the 3-arm and 8-arm trials.
- Puzzle: Figure 23.1 can be an FFRCISTG with no common cause of $M$ and $Y$ while Figure 23.2 has one. Explanation: common causes may be active only under interventions that assign different values of $N$ and $O$ to each person. The FFRCISTG of Figure 23.1 considers only interventions with $A=N=O$.
- If such a $U$ is the only reason for the discrepancy, $Y^{n=0,o=1}=Y^{a=1,M^{a=0}}$ still holds for every individual. But $E[Y^{n=0,o=1}]=E[Y^{a=1,M^{a=0}}]$ is then not identified by the mediation formula. Robins et al. (2022) give a river-blindness example.

**Reactions if only the third arm differs (pp. 328–329).**
- **NPSEM-IE believer and FFRCISTG believer:** both agree the story was wrong and that $E[Y^{n=0,o=1}]$ is estimated by the third arm (p. 328).
- **NPSEM-IE believer:** may still hold that $E[Y^{a=1,M^{a=0}}]$ equals the mediation formula, but cannot justify its policy interest as the effect of nicotine-free cigarettes (p. 328).
- **FFRCISTG believer:** may have little interest in the original formula. They care about the new trial's result and about which of (i)–(iii) failed (pp. 328–329).
- Continuing to assume Figure 23.1 is an FFRCISTG and that $E[Y^{n=0,o=1}]$ in the future trial differs from the mediation formula: can $A$ *always* be decomposed into some components $N',O'$ so that Figure 23.2 holds and $E[Y^{n'=0,o'=1}]=E[Y^{a=1,M^{a=0}}]$ equals the mediation formula? **No.** Otherwise $E[Y^{a=1,M^{a=0}}]$ would always be point identified by the mediation formula, which would violate the Robins–Richardson sharp bounds (p. 329).

> *Intuition note.* The test is a prediction: the old data forecast the outcome of the nicotine-free arm. A wrong forecast shows that some assumption failed, and extra measurements can help narrow down which one.

### 23.4 An interventionist theory of mediation (pp. 329–331)
This theory (Robins and Richardson 2010; Robins, Richardson, Shpitser 2022) was developed in response to perceived deficiencies of the standard theory and can be viewed as autonomous, without reference to cross-world counterfactuals (p. 329). It has been extended to survival analysis, competing risks and interference (margin, p. 329).

**Six-arm future trial (p. 329):** (1) $a=1$; (2) $a=0$; (3) $n=1,o=1$; (4) $n=0,o=0$; (5) $n=0,o=1$; (6) $n=1,o=0$. If $N,O$ are separable effects of $A$:
- Mean $Y$ in arm 1 equals arm 3, and arm 2 equals arm 4.
- $E[Y^{n=0,o=1}]$ is identified as the mean in arm 5, and $E[Y^{n=1,o=0}]$ as the mean in arm 6, regardless of whether $E[Y^{n=0,o=1}]$ is identified from the observed data.
- Stensrud et al. (2021) stress the arm equalities (margin, p. 329).

With currently available $(A,M,Y)$ data, the separable effects are identified under (i) no unmeasured common cause of $M$ and $Y$ and (ii) no direct effect of $O$ on $M$ or of $N$ on $Y$. Then $E[Y^{n=0,o=1}]$ equals the mediation formula (p. 329).

**Fine Point 23.2: surrogate mediator (p. 330).**
- An arrow $M\to Y$ is causally interpretable only if well-defined interventions on $M$ exist. If not, $M$ is a surrogate for an unknown true mediator $H$ (Figure 23.4: $A\to H$, $H\to M$, $H\to Y$, $A\to Y$).
- Figure 23.5 adds $N$ and $O$. Here $N$ and $Y$ are *not* d-separated given $M$ and $O$.
- If we nevertheless see $N\perp\!\!\!\perp Y\mid M,O$ in the three-arm data, there are 4 readings: (a) Figure 23.1 is the true diagram and $M$ is the true mediator; (b) $M$ is a one-to-one deterministic function of $H$; (c) a non-deterministic faithfulness violation in Figure 23.4; (d) the trial was too small to detect the dependence.
- Causal-discovery advocates would tend to adopt (a) if the three-arm sample was large.

**Further advantage (p. 330).** Often interventions on the putative mediator are not well defined, so $Y^{a,m}$ is not meaningful. Then neither pure nor controlled direct effects based on $M$ exist. Separable effects still exist if meaningful components $N,O$ exist and can be intervened on (p. 330).

**Summary of the interventionist approach (p. 330):**
- Treatment decomposes into meaningful, separable components that can in principle be intervened on independently.
- Identifying assumptions are in principle verifiable in future trials.
- Interventions on a purported mediator need not exist.
- It supports better communication with subject-matter experts.
- When assumptions hold, the g-formula equals the mediation formula, but the identified effects refer to interventions on components.
- It extends to more than two components, including time-varying ones.

**Technical Point 23.3 (p. 331): path-specific effects and the front-door formula.**
- Under Figure 23.6 (Figure 9.14 plus an $L\to Y$ edge), the total effect of $L$ on $Y$ is not identified. The $L\to Y$ pathway cannot be separated from confounding by $H$. Without that edge, the front-door formula identifies it (Fine Point 9.5).
- Interventionist question: is the effect of $L$ along $L\to A\to Y$ identified by the front-door formula even with $L\to Y$?
- Figure 23.7: $N$ is the BMI $L$ reported to the prescribing physician. $O$ is the $L$ used for referral. The arrows from $L$ to $N$, $O$ are deterministic, since $L=N=O$ in the data.
- Figure 23.8 (SWIG): an unethical intervention reports a false value $n$ to the physician but uses the true $L=O$ for referrals. Only $N$ is intervened on, and, as was the goal, the effect of $n$ on $Y$ is restricted to the path through $A$.
- Since $L\equiv O$ even in the intervened world, $O$ is dropped and $Y$ is again a child of $L$. With $Y^n\perp\!\!\!\perp N\mid L$ on Figure 23.8,
$$E[Y^n]=\sum_{l,a}E[Y|A=a,L=l]\Pr[L=l]\Pr[A=a|N=n]=\sum_a\Big\{\sum_l E[Y|A=a,L=l]\,\Pr[L=l]\Big\}\Pr[A=a|L=n].$$
The last equality uses $L\equiv N$ in the data. The right side is the front-door formula.
- The derivation is heuristic (null sets from determinism). A rigorous proof combines determinism with Technical Point 21.12.
- Substantively, $N$ and $O$ would not be called separable components of $L$, but that does not matter. What matters is that the story implies an expanded graph with a new intervention variable deterministically tied to $L$ (Stensrud et al. 2023).
- Wen et al. (2023) obtained essentially equivalent results. Fulcher et al. (2020) had shown that this formula identifies a cross-world quantity under the NPSEM-IE of Figure 23.6.

**Closing (p. 331).** Without randomized trials that actually intervene on the mediator or on treatment components, all these methods rely on observational data and exchangeability. A valid analysis needs adjustment for confounders of the treatment effect and of the mediator effect, plus the other assumptions. Figure 23.1 is a teaching device. Practical mediation analyses rest on "more heroic assumptions" than non-mediation analyses (p. 331). If a measured cause of $M$ and $Y$ is a child of $N$ and $O$, additional issues arise for separable effects (margin, p. 331).

## Toy example (ours, not from the text)
Binary $A$, $M$, $Y$ in a randomized trial with no confounding of $M$–$Y$. Assume:
- $\Pr[M=1|A=0]=0.2$ and $\Pr[M=1|A=1]=0.6$.
- $E[Y|A=1,M=1]=0.30$, $E[Y|A=1,M=0]=0.10$, $E[Y|A=0,M=1]=0.20$, $E[Y|A=0,M=0]=0.05$.

Mediation formula: $0.30\times0.2+0.10\times0.8=0.06+0.08=0.14$. Under the needed assumptions, this is the estimate of $E[Y^{a=1,M^{a=0}}]$, or of $E[Y^{n=0,o=1}]$ under the separable-component story.

Other means:
- $E[Y^{a=1}]=0.30\times0.6+0.10\times0.4=0.18+0.04=0.22$.
- $E[Y^{a=0}]=0.20\times0.2+0.05\times0.8=0.04+0.04=0.08$.

Effects:
- Total effect: $0.22-0.08=0.14$.
- Pure direct effect: $0.14-0.08=0.06$.
- Total indirect effect: $0.22-0.14=0.08$.
- Check: $0.06+0.08=0.14$.

Test (our illustration): the story predicts $E[Y|N=0,O=1]=0.14$ in a new nicotine-free arm. If the new trial shows 0.17, the story is refuted. Then (i), (ii) or (iii) is false, and the follow-up contrasts on $M$ and $Y$ say which.

## Concepts
- [[pure-direct-effect]] (new) — effect of $A$ with $M$ set to its $a=0$ value: $E[Y^{a=1,M^{a=0}}]-E[Y^{a=0,M^{a=0}}]$ (pp. 323–324)
- [[total-indirect-effect]] (new) — $E[Y^{a=1,M^{a=1}}]-E[Y^{a=1,M^{a=0}}]$ (p. 324)
- [[cross-world-counterfactual]] (new) — outcome indexed by two treatment values that cannot co-occur for one person (p. 324)
- [[mediation-formula]] (new) — $\sum_m E[Y|A=1,M=m]\Pr[M=m|A=0]$; identifies the cross-world mean under assumptions (p. 324)
- [[npsem-ie]] (new) — counterfactual model that assumes cross-world independencies; not the book's model (pp. 324–325)
- [[ffrcistg]] (new) — the book's model, which does not assume cross-world independencies (pp. 324–325)
- [[separable-effects]] (new) — effects of intervening on components $N,O$ of treatment that can be set separately (pp. 325–327)
- [[g-formula]] (new) — identification formula needing exchangeability and consistency. Here positivity is shown sufficient, not necessary (p. 326)
- Back-door / front-door criterion — the front-door formula is re-derived via a deterministic copy of $L$ (p. 331)
- Causal DAG — Figures 23.1–23.8, with SWIGs for the interventions (pp. 323, 326–327, 330–331)
- Potential outcomes — the nested notation $Y^{a,m}$ and $M^{a}$ (p. 323)

## Canonical instances
- [[smoking-cessation-hypertension-trial]] — $A$ cessation, $M$ hypertension, $Y$ MI. Illustrates pure and indirect effects (p. 323)
- [[nicotine-free-cigarettes]] — the $N/O$ story and the three-arm trial that tests it (pp. 325–328)
- [[bmi-drug-front-door-example]] — front-door formula re-derived by intervening on a deterministic copy $N$ of BMI $L$; the text notes that $N$ and $O$ would not usually be called separable components of $L$ (p. 331)
- [[river-blindness-study]] — only mentioned: Figure 23.1 an FFRCISTG but Figure 23.2 not (p. 328)

## Bridges (candidates)
- [metaphor] pure direct effect via $M^{a=0}$ ↔ Bayesian hierarchical modelling: a counterfactual that depends on a latent value from a different "world" is not checkable from observed data alone.
- [same-math] mediation formula as a g-formula ↔ potential outcomes: a standardization (mixing over $\Pr[M|A=0]$) of a conditional mean.
- [same-math] front-door formula in Technical Point 23.3 ↔ Back-door / front-door criterion: the same formula under an expanded graph.

## Questions this raises
- Which real treatments split into components that can be intervened on separately, and who judges "meaningful"?
- How big must the three-arm trial be to refute the story, given that the book ignores sampling variability?
- What does the FFRCISTG-based sharp-bounds result give in practice, and how wide are the bounds?
- When a measured cause of $M$ and $Y$ is a child of $N$ and $O$, what changes (p. 331)?

## Reading notes
- Printed = pdf − 9 (pdf 332–340 = printed 323–331).
- The PDF is the online revision dated 2026-08-19, not the 2020 print; chapter numbering may differ from older citations.
- Possible cross-reference misprints in the text: p. 327 says "DAG in Figure 22.1" and p. 328 says "Figure 22.3", where Figures 23.1 and 23.3 are apparently meant. p. 331 says "Figure 23" for Figure 23.1. In the p. 329 list, item 6 ends with a stray closing parenthesis.
- p. 327 prints $E[Y^{n=1,o=1}]-E[Y^{n=1,o=0}]$ as the pure direct effect. By the chapter's own identification $Y^{a=1,M^{a=0}}=Y^{n=0,o=1}$, the matching contrast looks like $E[Y^{n=0,o=1}]-E[Y^{n=0,o=0}]$ (with $n=0$). I report the printed form and mark it as a possible misprint.
- Technical Point 23.3 writes $pr[L=l]$ in lower case in one place. In the p. 329 summary, assumption (i) and (ii) are numbered differently from those on pp. 325–327.
- No exercises appear in this unit.

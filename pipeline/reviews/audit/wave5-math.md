# Independent audit, wave 5: math digests (Spielman ch. 23, Särkkä & Svensson ch. 10, Kelly 1956)

Auditor: Claude Opus 5.5. I did not write these digests. Date: 2026-10-15.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2. All three digests are `verified: repaired`.
Ground truth: the page images of the three extracts in `/home/claude/audit/w5/`. I read every page: 7 + 25 + 10. Kelly is a scan with no text layer. I re-rendered pp. 919 and 925 at 200 dpi to check the misprints.
Recomputation (python3):
- the Spielman toy example and its added step $\alpha_1-\alpha_2=nq$;
- $\sqrt2\cdot12$ squared $=288$;
- $288\cdot\tfrac14/(17^2/n)=72n/289\approx0.249n$;
- $\|\delta\|=2\sin(\theta/2)\le\sqrt2\sin\theta$ for $\theta\le\pi/2$;
- both iterations of the Särkkä toy example, in exact fractions;
- the Kelly toy example: $G$ at $\ell=0.8$ and $\ell=0.5$, and $R$.

Targets come from `pipeline/state/units.jsonl`.

Severity scale (as briefed; same as waves 2–4):
- **Critical:** a wrong equation, number or statement; a strengthened or weakened claim, including a dropped condition; a claim not in the source.
- **Major:** a wrong page ref; a missing key result; a dropped hedge; 3 or more undefined terms.
- **Minor:** notation, format, length, small coverage gaps.

"Low impact" marks an error that is real but unlikely to mislead a later post, usually because L3 states the point correctly.

## Summary

| Digest | Checks (approx.) | Critical | Major | Minor | Coverage of L3 | Toy / added steps | Length (body words; source / target; ×target) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Spielman ch. 23 (pp. 189–195) | ~35 (every display: $A$, $M$, $R$, eigenpairs, Thm 23.1.1, Cor. 23.1.2, (23.1), Thm 23.2.1, §23.3 chain, §23.4 proof; 8 reading notes; Concepts and Instances) | 1 (low impact) | 1 (glossary) | 6 | §§23.1–23.4 complete; §23.5 omitted | all correct | 1,805; 2,469 / 1,037 (**1.74×**) | good; too long; fix L0 |
| Särkkä & Svensson ch. 10 (pp. 204–228) | ~65 (equations (10.1)–(10.53) symbol by symbol, Algs 10.6–10.17, Examples 10.5/10.7/10.13/10.14 numbers, §10.6 claims, exercise refs, 5 reading notes) | 0 | 2 (1 glossary) | 4 | complete (§§10.1–10.7) | all correct (exact fractions) | 3,444; 9,283 / 3,899 (0.88×) | very good |
| Kelly 1956 (pp. 917–926) | ~50 (every display, (1)–(3), KKT conditions, $F_t$ rule, procedure (a)–(c), $G_{\max}$, all conclusion claims, voice tags, misprints) | 0 | 2 (1 glossary) | 2 | complete (every section) | all correct | 2,335; 4,500 / 1,890 (1.24×) | very good |

**Totals:** 1 critical, 5 major (3 of them glossary), 12 minor across 3 units.

**Estimate of surviving errors per unit:**
- **Critical:** 0.33. The one item is low impact and borderline; L1 and L3 state the point correctly.
- **Major:** 1.67. If the glossary items are excluded, 0.67.
- **Minor:** 4.0.

**Equations.** Every displayed equation I checked matches the image, symbol by symbol. The digests also caught and correctly flagged several source problems. I confirmed each one against the image.

Spielman:
- the $n/4$ that should be $72n/289$;
- "$c_i=0$" that should be $\alpha_i=0$;
- $\beta_i$ that should be $|\beta_i|$;
- "nullspace of $B$" holds only if $\beta_i=0$;
- the gap between $3\sqrt{pn}$ and $3\sqrt{p(1-p)n}$;
- the sign convention.

Särkkä:
- the $+\mathbf Q$ in the $\mathbf y$ block of (10.6). For a GSLR model the consistent form is $\mathbf{APA}^\mathsf T+\boldsymbol\Lambda$; the digest flags this as a possible misprint, hedged;
- $\mathbf h(\mathbf x_k,\mathbf q_k)$ and the missing $(i-1)$ in (10.17);
- $\sum_{i=1}$ in (10.39) and (10.45).

Kelly:
- "or error" on p. 919;
- "$p(1)\alpha_r$" on p. 925.

**Toy examples and added steps.** All recompute exactly:
- **Spielman.** $\alpha_1=1.6$, $\alpha_2=0.8$, row check $0.4$, $\cos\theta=\tfrac12$, $\sqrt2\sin60^\circ=1.2247\ge1$. The added step ($\alpha_1-\alpha_2=nq\ge\tfrac n2(p-q)\iff q\ge p/3$) is true.
- **Särkkä.** Iteration 1: $A=2$, $b=0$, $\Lambda=3$, $m^{(1)}=11/7$, $P^{(1)}=3/7$. Iteration 2: $A=22/7$, $b=-100/49$, $\Lambda=1921/343-1452/343=469/343=67/49$, $K=154/551$, $m^{(2)}=1.8100$, $P^{(2)}=0.1216$.
- **Kelly.** $G(0.8)=0.53101=R$ and $G(0.5)=0.42647$.

**Pattern.** As in waves 2–4:
- The only critical item is a summary-level line (L0) that is stronger than L3.
- The glossary rule ("≥ 3 undefined terms") failed in all three digests. **This is the sixth wave in a row.**
- The length cap (1.3× target) was again not enforced after repair: Spielman is at 1.74×, at 73% of the source's length.

**Verdict: OK to continue the batch.**
- Fix Spielman L0.
- Fix the two dropped hedges (Särkkä p. 227, Kelly p. 918).
- Trim Spielman, or accept it as dense math: the source is short, and the overage is mostly the Reading notes and full equation chains.

---

## 1. Spielman, *Spectral and Algebraic Graph Theory*, ch. 23 "Spectral Partitioning in a Stochastic Block Model" (printed pp. 189–195)

### A. What I checked
- **p. 189:** the probability model and expected crossing edges $q|X||Y|$; the $17/\sqrt n$ and $\epsilon/\sqrt n$ statements; McSherry.
- **p. 190:** the matrix $A$ including $-pI_n$; the definition of $M$ and $\mathbb E[M]=A$; the algorithm $S=\{a:\psi_2(a)<0\}$; the Warning.
- **p. 191:** $\widehat M$, $\widehat A$, rank 2, $R$; $\alpha_1$; $\phi_2$; $\alpha_2$; the entry distributions of $R$.
- **p. 192:** the Chapter 8 / (8.2) remark; Thm 23.1.1 (both terms and the condition $p\ge c_2\ln^4n/n$); Cor. 23.1.2; AKV; the ordering of $\mu$ and $\alpha$; (23.1); the Davis–Kahan statement.
- **p. 193:** the 2×2 examples (90°, 45°); Thm 23.2.1 ($\sin2\theta_i$, ±, the π/2 remark, the weaker $\theta$ version); §23.3 multiplicity, the assignment rule, $\delta$, $|\delta(a)|\ge1/\sqrt n$, $\|\delta\|\ge\sqrt{k/n}$, $\|\delta\|\le\sqrt2\sin\theta$.
- **p. 194:** $q>p/3$ and the gap; the $\sin\theta$ chain; $\sqrt{k/n}$; $k\le288p(1-p)/(p-q)^2$; the constant case; the $n/4$ case; the refinement remark; the proof set-up (shift, multiplicity, $|\beta_i|\le\|R\|$, expansion, $\delta$).
- **p. 195:** the six-line chain for $\|A\psi_i\|^2$; the upper bound; the conclusion; §23.5.
- **Other sections:** all L2 bullets and the L1 claims; the intuition notes; 8 Concepts; 2 Instances; 2 Bridges; 8 reading notes.

### B. Coverage
| Source part | In L3? |
|---|---|
| Intro: model, McSherry, Warning | yes. Omitted: "partition will not be the smallest" as the reason for unsolvability; McSherry's more general models; "Nevertheless, some of them are" |
| §23.1: $A$, $M$, algorithm, shift, eigenpairs, $R$ entries, Thm 23.1.1, Cor. 23.1.2 | yes |
| §23.2: Weyl (23.1), Davis–Kahan, 2×2 examples, Thm 23.2.1 | yes |
| §23.3: misclassification bound, $k\le288p(1-p)/(p-q)^2$, $n/4$ case | yes |
| §23.4: weak Davis–Kahan proof | yes, every step |
| §23.5 Further Reading ([Ver10], [Tro12]) | **no** |

### C. Findings

**P1. Critical (low impact, borderline). L0 (line 20): "its signs are expected to recover the hidden partition up to a bounded number of errors".**
- **Evidence:** p. 194. The bound $k\le288p(1-p)/(p-q)^2$ gives "a constant number of vertices" only "if $p$ and $q$ remain constant as $n$ grows large". For the chapter's own featured case ($p=1/2$, $q=p-17/\sqrt n$, pp. 189, 191, 194) the bound is $\approx n/4$: "a constant fraction of the vertices".
- **Problem:** "Bounded number" reads as O(1). That is true only in the constant-$p,q$ case, so the line strengthens the result for the case the chapter highlights. L1 and L3 (line 82) are correct.
- **Fix:** "…recover the hidden partition with at most $288p(1-p)/(p-q)^2$ errors: a constant number for fixed $p,q$, a constant fraction when $p-q\sim1/\sqrt n$."

**P2. Major (glossary). Terms used without a definition at first use or in Concepts:**
- **Courant–Fischer theorem** (Prerequisites, line 64);
- **multiplicity** of an eigenvalue (lines 74, 77, 89);
- **eigenspace** (line 76);
- **information-theoretically unsolvable** (line 41);
- **spectral norm** (Prerequisites). The Concept `[[norm]]` says only "matrix norm measures noise size" and never says which norm.

**P3. Minor (length).** The body is 1,805 words against a target of 1,037 (1.74×) and a 2,469-word source (73%). This breaks the 1.3× cap. The Reading notes alone are ~250 words.

**P4. Minor (page ref). Line 74: "Why the gap matters (p. 193)".** The two diagonal matrices are printed on p. 192; only their eigenvectors and the 45° matrix are on p. 193. Concepts gives the correct "pp. 192–193". The Concept `[[norm]]` cites p. 192, but $\|R\|$ is first used on p. 191.

**P5. Minor (omission). L2 bullet 7 and L3 line 41: the Warning.**
- **Evidence:** p. 190 ends: "There is no reason to believe that algorithms that are optimized for these models will be useful in practice. Nevertheless, some of them are."
- **Problem:** The digest keeps only "real data rarely resembles these models" and drops both halves of the author's verdict on practical usefulness.

**P6. Minor (coverage).**
- §23.5 Further Reading is not mentioned.
- In the intro, the "unsolvable" sentence loses its premise. The source says that when $p$ is too close to $q$, "the partition given by X and Y will not be the smallest" (p. 189).

**P7. Minor (toy example).**
- **What it shows:** The toy illustrates only the step from misclassification to $\|\delta\|$. It does not show the main result (a noise bound and gap giving an angle bound, which gives a $k$ bound).
- **Boundary case:** It sits exactly at $q=p/3$ ($0.2=0.6/3$), where the chapter's assumption $q>p/3$ fails. There $\alpha_1-\alpha_2=\alpha_2=0.8$, so the gap identity still holds, but only as a tie.
- **Unmentioned:** The $k$ bound would be $288\cdot0.24/0.16=432\gg n=4$, which is vacuous.
- **Arithmetic:** All of it is correct.

**P8. Minor (bridge label). Bridge 2.** It is labelled `structural-analogy`, yet it says "the theorem is the same statement", and both sides are in linear algebra. Either relabel it or drop it.

---

## 2. Särkkä & Svensson, *Bayesian Filtering and Smoothing* (2nd ed.), ch. 10 "Posterior Linearization Filtering" (printed pp. 204–228)

### A. What I checked
- **Definitions and results:** Def. 10.1 / (10.1)–(10.2); Thm 10.2 / (10.3); Cor. 10.3 / (10.4)–(10.6); the p. 206 "key thing" paragraph; the SL/SLR restriction (p. 207); Def. 10.4; prior vs posterior SLR; (10.7); the p. 208 KL remark.
- **Examples 10.5 and 10.7:** $x\sim N(1,0.1)$, $q\sim N(0,0.1)$, $y=5$, centre ≈1.7, $\sqrt\Lambda\simeq0.45/0.01$, "At least in this example"; Ex. 10.7 iterations 1/2/3.
- **Algorithm 10.6:** (10.9)–(10.11) index by index, including $\mathbf S^{-1}$ printed without $(i)$; "updates the *prior*".
- **p. 211 remarks:** all four.
- **Algorithms 10.8–10.11:** (10.12)–(10.21), including which terms add $\mathbf Q$/$\mathbf R_k$ and which do not; the 8.3/9.20/9.21 relations; the IEKF comparison; (9.68), (A.55)/(A.63)/(A.56)/(A.64); the closed-form remark.
- **Algorithms 10.12–10.17:** (10.22)–(10.45). These include the augmented $\tilde{\mathbf m}$, $\tilde{\mathbf P}$ and the $n$ / $n_q$ / $n_r$ splits; (10.36) and (10.39) with the conditional covariances added; the Monte Carlo convergence caveat (p. 223).
- **Examples 10.13 and 10.14:** 0.14 vs 0.17, "it appears that…"; 0.032 vs 0.031, "marginally lower", start-up.
- **§10.6:** (10.46)–(10.53), "page 174", P→0, "strictly speaking only makes sense", MKL, GSLR with π, "not correct" generalization, the PL optimality paragraph, the IEKF-as-PL remark, Chapter 14.
- **Exercises:** 10.1–10.4 and 10.7, with their page numbers.
- **Other sections:** all 8 L2 bullets; L1 (98 words); 10 Concepts; 3 Instances; 5 Reading notes.

### B. Coverage
Complete: intro, §§10.1–10.6, every algorithm (10.6, 10.8–10.12, 10.15–10.17) with its equation numbers, all four examples, and §10.7 via "Exercises worth doing" (5 of 7 listed). Proofs: the source has only "same as Theorem 9.12", which the digest keeps.

### C. Findings

**S1. Major (dropped hedge, low impact). L3 §10.6, line 159: "The IEKF linearization is a type of PL that linearizes at the MAP estimate."**
- **Evidence:** p. 227: "the linearization used in the IEKF in Section 7.4 *can be seen as* a type of posterior linearization that maximizes the accuracy of Taylor series expansion under this same philosophy by linearizing at the MAP estimate".
- **Problem:** The authors' interpretive framing becomes a classification.
- **Fix:** "can be seen as a type of PL…"

**S2. Major (glossary). Terms used without a definition:**
- **EKF** (lines 142, 144);
- **CKF / GHKF / UKF** (lines 140, 144);
- **RMSE** (lines 142, 185);
- **MAP estimate** (line 159);
- **Gauss–Newton method** (line 103);
- **sigma points** and **cubature** (Prerequisites only, never defined).

(IEKF is defined in Concepts.)

**S3. Minor (hedge). Intro, line 39: "How we linearize matters".**
- **Evidence:** p. 204: "How we linearize the models *may significantly influence* the filter performance".
- **Fix:** "may strongly affect performance". This is the chapter's motivating premise, so it is low impact.

**S4. Minor (aim stated as result). L2 bullet 2: "The linearization is then accurate where the state is expected to be after measuring".**
- **Evidence:** p. 207: PL "*seeks* a linearization that is accurate in the support of the posterior density". p. 208 supports "maximally accurate when x is distributed according to the posterior", but only in the sense of §10.6.
- **Fix:** "aims to be accurate…"

**S5. Minor (format). Line 90: the shapes are labelled "this is added bookkeeping" rather than with the prescribed `(added step)` tag.** The content is correct ($\mathbf A^{(i)}\in\mathbb R^{d\times n}$).

**S6. Minor (vague paraphrase). Line 130: "A closed form also exists for models with state-dependent covariance".**
- **Evidence:** p. 216: "we sometimes also encounter *non-additive noise models* for which the *conditional moments* take closed-form expressions. Important examples … are the dynamic models from Chapter 4 …".
- **Problem:** The digest does not say what has a closed form, and it drops "non-additive".

No critical errors. L0, L1, the other 6 L2 bullets, every intuition note and every Concepts and Instances line match the source. Kept hedges include:
- "At least in this example" (p. 208);
- "it appears that, in this model (and data)" (p. 220);
- "in some contexts" (p. 214);
- "likely to produce similar results" (p. 211).

---

## 3. Kelly 1956, "A New Interpretation of Information Rate", *BSTJ* 35 (printed pp. 917–926)

### A. What I checked
- **pp. 917–918:** the abstract claims and the coding-theorem framing; "many workers…some have even proceeded"; radar and minimum equivocation; "unjustified"; "seems to have but one solution"; the cost function and von Neumann; "generally … external"; "too general"; the distinguishing feature; "arbitrary combination … does not necessarily constitute".
- **p. 919:** baseball; even money; "probably all he had"; $2^N$; the definition of $G$, base 2, $G=1$; the noisy channel; $\langle V_N\rangle=(2q)^N V_0$; "probably be broke … with probability one if he continued indefinitely"; $V_N=(1+\ell)^W(1-\ell)^L V_0$; the $G$ limit "with probability one"; the $Z=\sum X_i\log Y_i$ lemma.
- **p. 920:** convexity; $1\pm\ell$; $G_{\max}=1+p\log p+q\log q=R$; the objection and reply, with its voice; the notation list.
- **pp. 921–922:** independence; fair odds; $\sum1/\alpha_s=1$; insure a profit; parimutuel; "probably" for the stock market; $\sum a=1$ without loss of generality; $V_N$, (1); $G$ at fair odds; $a(s/r)=q(s/r)$; $H(X)-H(X/Y)$; unfair odds; $H(\alpha)$; (a).
- **p. 923:** (b) and (c), "minimized (at zero)"; the track take; $b_r$; (2); the constraint; $G_r$.
- **p. 924:** (3); $\lambda$, $\lambda'$; all three derivative conditions including $\log e$ and ≤; $k$, $b$, $a(s)$; $p$, $\sigma$; the three determining conditions; the ordering.
- **p. 925:** "$t$ a positive integer or zero"; $F_t$, $p_t$, $\sigma_t$, $F_0$; both monotonicity cases; the minimum positive value and the smallest $t$; procedure (a)–(c), "sum to $1-b$"; $G_{\max}$; the no-bet case; negative-expectation bets.
- **p. 926:** the conclusion: value function vs additivity and the LLN; the wife example; the limit of proof; "it is possible that it could apply"; the requirements; "might correspond"; the three-part summary.
- **Other sections:** L0 and L1 (99 words); 8 L2 bullets; 2 intuition notes; skip path; 5 Concepts; 3 Instances; 5 Reading notes, including the printed = pdf + 916 offset. Both misprints confirmed at 200 dpi.

### B. Coverage
Complete: Introduction, the gambler with a private wire, the general case, unfair odds, the track take, and the conclusion. Every equation is kept. The acknowledgments are omitted, which is fine.

### C. Findings

**K1. Major (dropped hedge, low impact). L3 Introduction, line 41: "That cost would depend on things outside the system".**
- **Evidence:** p. 918: "*Generally* this cost function would depend on things external to the system".
- **Fix:** "Generally, that cost would depend…"

**K2. Major (glossary). Terms used without a definition (level UG):**
- **equivocation** (line 40);
- **$H(X/Y)$ / conditional entropy.** It is used in L1, L2 and L3 but never defined; only "Shannon entropy $H$" appears in the Prerequisites;
- **parimutuel betting** (line 59);
- **von Neumann utility theory** (line 41);
- **coding theorem** (L1; only partly glossed on line 40).

**K3. Minor (dropped clause in a definition). Line 57: "$\alpha_s$ is the odds, that is, dollars returned per one-dollar bet".**
- **Evidence:** p. 920: "the number of dollars returned for a one-dollar bet *(including that one dollar)*".
- **Problem:** The clause is what makes $\alpha_s=1/p(s)$ "fair" and makes even money equal $\alpha=2$. A reader who takes net odds would misread every formula.

**K4. Minor (compression). L2 bullet 7: "the optimal bets come from setting the derivatives of $G$ equal to a constant $k$".**
- **Problem:** This holds only on $\lambda$. For $s\in\lambda'$ the condition is $\partial G/\partial a(s)\le k$ (p. 924). L3 line 88 is correct.

No critical errors. Every other L0–L2 sentence, intuition note, and Concepts and Instances line matches the source. Kept hedges include:
- "seems to have but one solution";
- "probably operates" (stock market);
- "it is possible that it could apply";
- "in what sense, if any".

---

## Fix list (critical + non-glossary major)
1. **Spielman L0** (P1): replace "up to a bounded number of errors" with the $288p(1-p)/(p-q)^2$ bound and its two regimes.
2. **Särkkä line 159** (S1): "can be seen as a type of PL".
3. **Kelly line 41** (K1): restore "Generally".

## Pipeline notes
- Glossary rule: failed in 3 of 3 digests (sixth consecutive wave). The verifier is still not checking it.
- Length cap: Spielman passed verification at 1.74× target. As in wave 4, the cap is not enforced after repair. Short sources (2.5k words) seem to overshoot most, because Reading notes and full derivation chains do not scale down.
- Source-error detection is strong. It found 11 genuine misprints or inconsistencies across the three units, and none were false alarms.

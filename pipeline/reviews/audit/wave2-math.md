# Independent audit, wave 2: math and formal digests (Gelman BDA3 ch. 5, Åström & Murray ch. 7, Bellman 1957 ch. III, Kalman 1960)

Auditor: Claude Opus 5.5. I did not write these digests. Date: 2026-10-14.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2. All four digests are `verified: repaired`.
Ground truth: the page images of the four extracts in `/home/claude/audit/w2/`. I read every page: 38 + 36 + 35 + 11. I zoomed to 250 dpi on Kalman pp. 42–44 to check (37), Example 1, Example 2 condition 2 and the p. 44 matrices.
Recomputation: the scripts are `scratchpad/w2/recompute.py` and `scratchpad/w2/recompute2.py`. They re-run every worked number, toy example and "(added step)" that can be computed, and several of the source's own numbers.
Page offsets were checked against `pipeline/units.csv`.

Severity scale (as briefed):
- **Critical:** a wrong equation, number or statement; a strengthened or weakened claim (including a dropped condition); a claim not in the source.
- **Major:** a wrong page ref; a missing key result; a dropped hedge; 3 or more undefined terms.
- **Minor:** notation, format, small coverage gaps.

"Low impact" marks an error that is real but unlikely to mislead a later post.

## Summary

| Digest | Checks (approx.) | Critical | Major | Minor | Toy / added steps | Length (words: digest; source / target) | Verdict |
|---|---|---|---|---|---|---|---|
| Gelman et al. BDA3 ch. 5 (pp. 101–138) | ~95 (eqs 5.1–5.24, ANOVA table, Tables 5.2/5.3/5.5 cell by cell, ~45 claims, 6 exercises, refs) | 0 | 2 | 6 | all correct | 7,277; 20,714 / 6,000 (1.21×) | very good |
| Åström & Murray ch. 7 (pp. 7-1–7-36) | ~90 (eqs 7.1–7.33, Thms 7.1–7.3, Tables 7.1–7.2, Examples 7.1–7.10, 6 exercises) | 0 | 2 | 3 | all correct | 5,278; 14,571 / 6,000 (0.88×) | excellent |
| Bellman 1957 ch. III (pp. 81–115) | ~60 (§§1–10 eqs, the principle, both procedures, bibliography, 94-problem map, 6 exercises) | 1 | 1 | 4 | all correct | 3,920; 11,118 / 6,000 (0.65×) | good after 1 fix |
| Kalman 1960 (pp. 35–45) | ~100 (eqs 1–44, Thms 1–5, Table 1, both examples incl. 3×3 matrices, ~40 claims) | 3 | 2 | 3 | all correct | 5,876; 11,920 / 6,000 (0.98×) | good after 4 fixes |

These counts cover only errors that survived verification. Four of the "major" findings (one per digest: G2, A2, B4, K5) are the usefulness item "3 or more undefined terms". They are not faithfulness errors.

**Estimate of surviving errors per unit:** about **1.0 critical**, **1.75 major** (about 0.75 if the undefined-term finding is excluded) and **4 minor**. Wave 1 had 0.5 critical, 1 major and 4 minor. The rise in critical errors comes entirely from Kalman and Bellman. All four critical errors are local and fixable in one line:
- one wrong symbol in prose;
- two conditions dropped in the summaries (L2 only; L3 is correct in both cases);
- one false mathematical claim in an intuition note.

Every numbered equation was checked symbol by symbol against the image. All of them match, with one exception: Kalman (37), where the transcription is mathematically equivalent but not what is printed. Every toy example and every "(added step)" recomputes correctly.

**Error patterns that survive v2.2**
1. **The summaries are stronger than L3.**
   - Bellman L2 attributes monotone convergence to "guess $f$". In the source it holds only because $f_0$ is the return of an initial policy.
   - Kalman L2 drops the zero-mean hypothesis of Theorem 2.
   - Åström L1 drops "in general".
   - Gelman L3 drops "Perhaps".

   In each case the L3 passage is right; the compression introduced the error.
2. **Single-symbol substitutions in prose** that the image check did not catch:
   - Kalman: $\tilde x_1(1)$ instead of $x_2(1)$.
   - Kalman: $\hat\Phi^{*\prime}$ instead of $\hat\Phi'$ in (37).
3. **Intuition notes that make their own mathematical claims.** Kalman's note says "$\Delta^*$ grows with $P^*M'$". This is false: $\Delta^*$ does not change when $P^*$ is multiplied by a constant (checked numerically).
4. **Silent misprint corrections.** Kalman p. 44 prints "$C_1(t)-tC_3(t)$". Remark (o) prints "$\hat M(t)$ in Problem I". The digest corrects both silently. By contrast, it flags (18) and (24) well.
5. **Undefined terms.** All four digests use 3 or more unglossed technical terms. For a reader starting at high-school level, the glossary rule (≤ 15-word gloss at first use) is still not enforced.

**Verdict: OK to continue the batch.** Fix the 4 critical items listed below. The grad-level math digests are faithful in their equations and examples. The remaining risk sits in L1/L2 compression and in intuition notes.

---

## 1. Gelman et al. 2013, *Bayesian Data Analysis* (3rd ed.), ch. 5 "Hierarchical models" (printed pp. 101–138)

### A. Math and faithfulness
I checked the following against the images:
- **Equations:** (5.1)–(5.24), symbol by symbol. This includes the Jacobian claims (5.9)/(5.10), which I verified numerically: $|\partial(\tfrac{\alpha}{\alpha+\beta},(\alpha+\beta)^{-1/2})/\partial(\alpha,\beta)|=\tfrac12(\alpha+\beta)^{-5/2}$ and $|\partial(\log\tfrac\alpha\beta,\log(\alpha+\beta))/\partial(\alpha,\beta)|=1/(\alpha\beta)$.
- **Tables:** the ANOVA table, and Tables 5.2, 5.3 and 5.5, cell by cell.
- **Numbers:**
  - rat tumor: 0.136 / 0.103, (1.4, 8.6), Beta(5.4, 18.6), 0.223 / 0.083, the grid ranges, $(-1.75, 2.8)\to(2.4, 14.0)$, $E(\alpha|y)=2.4$, $E(\beta|y)=14.3$;
  - eight schools: 7.7 / 16.6 / 4.1, [−0.5, 15.9], 4.6, 13, the order statistics, 93% and the other seven probabilities, 22/200, 141/200;
  - beta-blockers: 0.060 / 0.071, [0.69, 0.90], [0.70, 0.85], "just over 10%", "about 25% lower";
  - 5.7: $J\ge3$, $J\ge4$, $s^2=\beta/\alpha$, $\nu=2\alpha$, 100, $A=25$, $\tau<50$.
- **Claims:** all claims in L0–L3. I paid special attention to the voice of "empirical Bayes" and to the conditions in 5.7 ($J\ge3$, "can, but do not necessarily").

All copied equations are exact.
- The hedges are mostly kept: "presumably", "perhaps misguidedly", "it would appear imprudent" and "inherently provisional".
- Question 3 on p. 103 is correctly kept as a question.
- The reading note on 0.223 vs $5.4/24=0.225$ is right. A method-of-moments fit to Table 5.1 gives (1.36, 8.62), and Beta(5.36, 18.62) has mean 0.2235.
- The reading note on the $\sigma_i^2$ misprint (p. 120) is real.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| G1 | L3 §5.2, divorce example, Mountain-states bullet | "so the prior needs wide tails". The source says "**Perhaps**, given your expectation of outliers …, your prior distribution **should** have wide tails". The hedge is dropped and the modal is strengthened. | p. 106 | **major** (dropped hedge; low impact) |
| G2 | Whole digest (usefulness) | These terms are used without a gloss: Jacobian (5.3), logit (5.3), scaled inverse-$\chi^2$ / inverse-gamma (5.4, 5.7), highest-posterior-density interval (5.6), order statistics (5.5), random-effects model (5.4), half-$t$ (5.7). The Prerequisites line covers neither change of variables nor logit. | pp. 110, 113, 117, 120, 127, 129–130 | **major** (≥3 undefined terms) |
| G3 | L3 §5.3, "Hyperprior choice" | "The choice is uniform on …". The source says "**One reasonable** choice of diffuse hyperprior density". | p. 110 | minor |
| G4 | L3 §5.6 Results, last two bullets; Model bullet | "The data suggest $\tau$ near zero" (the source says "$\tau$ **might be** close to zero"). "5 or 10 studies are **quite** informative" (the source says "relatively informative"). Both are slight strengthenings. | pp. 126–127 | minor |
| G5 | L3 §5.2, divorce example, first bullet | "model them exchangeably, with a fairly vague distribution". This drops the condition "**Unless you are familiar with divorce statistics** … should be fairly vague". It also drops the suggested beta / logit-normal on [0, 1]. | p. 105 | minor |
| G6 | L3 §5.5, Discussion, first bullet | It is cited as p. 123, but the "median-centred between 5 and 10 / largely overlap" half is on p. 122. | p. 122 | minor (page ref across a page break) |
| G7 | L3 §5.1–5.2 (coverage) | Omitted: "Other systematic differences, such as a time trend, can be incorporated in a more extensive model" (p. 103); the divorce example with $x_j$ = last year's rate, a covariate example (p. 106); "both kinds of replications can be used to assess model adequacy" (p. 108). | pp. 103, 106, 108 | minor |
| G8 | L3 §5.5, Discussion (coverage) | Omitted: "we use only 200 draws … to illustrate that a small simulation gives adequate inference" (p. 123), and the closing claim that the model "is flexible enough to adapt to the data" (p. 124). | pp. 123–124 | minor |

### B. Toy example and added steps (Python)
- **Toy (two groups):** $\hat\theta_1=8$, $V_1=2$, $\hat\theta_2=5.6$, $V_2=3.2$, own-mean weights 0.5 and 0.2 ✓. $\hat\mu=8.2857$, $V_\mu=5.714$ ✓. It illustrates the main idea (partial pooling, with noisier groups pulled harder).
- **Added step (5.6)/(5.7)→(5.8):** the $\theta_j$ factors cancel ✓.
- **Added step for (5.21):** $\mathrm N(\hat\mu|\hat\mu,V_\mu)\propto V_\mu^{-1/2}$ ✓.
- **Source numbers re-derived:**
  - full-grid posterior over all 71 groups with prior (5.9): $E(\alpha|y)=2.40$, $E(\beta|y)=14.32$ ✓;
  - $p(\tau{=}10|y)/p(\tau{=}0|y)=0.40$ ("less than half") ✓;
  - $\Pr(\tau>25)\approx0.01$ ✓;
  - $\Phi(13.5/9.1)=0.931$ ✓;
  - $\sqrt{\text{mean }\sigma_j^2}=12.9$ ✓.

  (Observation, not counted: the $\chi^2$ statistic recomputes to 4.71, not the printed 4.6, and the printed interval uses ±2 se. These are source-side roundings, and the digest copies the source faithfully.)

### C. Coverage
- §§5.1–5.9 are covered in order with every equation and example.
- Table 5.4's posterior columns and Table 5.1 are not reproduced; a reading note says so.
- The exercise map (1–17) is correct.
- Exercises worth doing: Ex. 2, 3, 4, 5, 10 and 12. The numbers, pages and descriptions are correct, and no solutions are given. Ex. 5's line states the result to be proved, but that result is the exercise statement itself.

### D. Usefulness
- The Prerequisites line is accurate but incomplete (see G2).
- The intuition notes are good and faithful, especially the 5.4 weight formula and 5.7.
- No derivation exceeds ~10 steps, so no skip path is needed.
- At 1.21× the target, the length is acceptable for this density.
- This is the strongest digest of the set apart from the glossary gap.

---

## 2. Åström & Murray 2021, *Feedback Systems* (2nd ed.), ch. 7 "State Feedback" (pp. 7-1 to 7-36)

### A. Math and faithfulness
I checked the following against the images:
- **Equations:** (7.1)–(7.33), $\mathcal R_{eq}$, the impulse argument, the Cayley–Hamilton expansion, (7.5) and $\det W_r$. I verified the last numerically at the Example 7.7 parameters: the $W_r$ computed from $A,B$ equals the printed (7.5), and $\det=-4.265\times10^{-7}$ equals the closed form. I also confirmed $\mu=MJ+mJ+Mml^2$.
- **Example 7.3:** $T$.
- **Statements:** Theorems 7.1–7.3 (including "if and only if", "single input and single output", and the $\tilde W_r^{-1}$ form). The step and natural responses for all three $\zeta$ regimes, (7.25), $M_p$ and $T_r$.
- **Tables 7.1 and 7.2:** recomputed (1.83/2.19/2.72; 16%/4.3%/0; 8.0/5.7/4.0; 1.54/1.27/1.00; 5.03/1.15/1.00; 0.99/0.707/0) ✓.
- **Examples 7.4–7.10.**
- **(7.28)** and the $b_n=-a_nCA^{-1}B$ step.
- **Exercises** 7.4, 7.9, 7.10, 7.13, 7.15 and 7.17.

All are exact, and the voice handling is good. All six reading notes on source inconsistencies are real:
- Example 7.6: $\omega_0=0.22$, $\zeta=1/\sqrt2$ gives $-0.156\pm0.156i$, not the printed $-0.2\pm0.096i$.
- Example 7.7: the "frequency 1" vs modulus 0.25.
- Example 7.8: the sign of $-b/a$.
- Figure 7.15: "k = 10 ms" vs "t = 10 s".
- Figure 7.7: $L_e=30$ vs 29.5.
- Exercise 7.15: $Fd$ vs $v$. Exercise 7.9: $\det(sI-BK)$.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A1 | L1 | "fast eigenvalues **need** large control signals". The source says "Large eigenvalues will **in general** require large control signals". The hedge is kept in L2 bullet 5 and in L3, but dropped in L1. | p. 7-22 | **major** (dropped hedge; low impact) |
| A2 | Whole digest (usefulness) | These terms are used without a gloss: Jordan form (p. 7-22), positive (semi)definite and the $\succeq/\succ$ notation (7.29), Cayley–Hamilton theorem (p. 7-4; named, never stated), impulse function $\delta$ and its derivatives (p. 7-3), and frequency response / bandwidth / resonant peak / $Q$-value (Table 7.2). Prerequisites list none of them. | pp. 7-3, 7-4, 7-20, 7-22, 7-28 | **major** (≥3 undefined terms) |
| A3 | L2 bullet 3 | It cites "Theorems 7.2, 7.3; pp. 7-9, 7-13, 7-14", but Theorem 7.3 is on p. 7-15. | p. 7-15 | minor |
| A4 | L1, last sentence | "later design chapters build on it". The source names specific follow-ups: Chapter 8 for estimation, Chapter 13 for robustness, Chapters 9–13 for frequency design, Chapters 12–14 for actuators. It makes no general claim, so this is a mild unsupported gloss. | pp. 7-17, 7-22, 7-24 | minor |
| A5 | L0 (format) | L0 has two sentences; the spec asks for one. | — | minor |

Observation (not counted): Example 7.4 prints "settling times 3 to 6 normalized time units, which corresponds to about 2–4 s at $v_0=15$ m/s" with $b=3$ m. Since normalized time is $v_0t/b$, this should be 0.6–1.2 s. The digest copies it faithfully but does not flag it, although it flags six other source inconsistencies.

### B. Toy example and recomputation (Python)
- **Toy, reachable case:** $\det W_r=-1$, $K=(2\ 3)$, closed-loop eigenvalues $\{-1,-2\}$, $k_f=2$, $x_e=(r,0)$ ✓.
- **Toy, unreachable case:** $\det W_r=0$, characteristic polynomial $(s+1)(s+1+\sigma)$. The numeric check with $K=(1,2)$ gives $\{-1,-4\}$, and with $K=(-3,7)$ gives $\{-1,-5\}$ ✓. $HB=0$ and $HA=-H$ ✓. The digest correctly notes that this is not the exact constant-combination case.
- **Example 7.5:** `place` gives $K=(0.025,\ -0.052)$ and $k_f=0.002$ ✓.
- **Example 7.7:**
  - open-loop eigenvalues $0,\ -0.0011,\ \pm2.68$ ✓;
  - $\omega_0=2.087$ ✓;
  - `place` gives $K=(-15.3,\ 1730,\ -50.0,\ 443)$ and $k_f=-15.3$ (printed −15.6 / −50.1, so the source rounds or uses slightly different values; the digest copies the print) ✓;
  - redesign pair $-0.33\pm0.66i$ has $\zeta=0.45$ ✓.
- **Example 7.3:** $T$ recomputed ✓.

### C. Coverage
- §§7.1–7.6 are complete and in order, with all ten examples and both theorems' gains.
- The exercise selection is good: 7.4, 7.10 and 7.13 build intuition, and 7.17 is the LQR proof. No solutions are given.

### D. Usefulness
- There is one intuition note per major result, and all are faithful.
- The toy pairs a reachable and an unreachable case, which is excellent.
- The Reading notes are the best in the batch.
- The only gap is A2. A UG reader with HS start needs one-line glosses for Jordan form, positive definite, Cayley–Hamilton and frequency response.

---

## 3. Bellman 1957, *Dynamic Programming*, ch. III "The Structure of Dynamic Programming Processes" (printed pp. 81–115; scan)

### A. Math and faithfulness
I checked the following against the scan:
- **Equations:** §4 (1)–(5), §5 (1)–(4), §6 (1)–(3), §9 (1)–(4) and §10 (1)–(5).
- **The principle of optimality** (wording and the "intuitive:" oddity).
- **The two existence cases** in §4.
- **Voice:** "a proof by contradiction is immediate"; the duality between $f$ and the policy; footnotes 2, 3 and 5.
- **The bibliography**, item by item.
- **The exercise map** (94 problems; 1–7, 8–11, 12–13 and 89–92, …).
- **The six suggested exercises:** numbers, pages and content.

All equations match the image except for the missing integration domain in B2. The handling of §10 (2) is good: it is printed without a return term, and the digest flags it. So is the reading note on "monotone convergence" promised but not delivered.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| B1 | L2 bullet 8 (and the §10 intuition note) | "One can start … in function space (**guess $f$**) or in policy space … **The function-space scheme is monotone increasing**; the policy-space scheme is left to later treatment." In the source, the monotone procedure (10.4)–(10.5) starts from $f_0$, the return of an initial *policy* $q_0$ via (10.2). That initial policy is what makes "$f_1\ge f_0$" immediate, and it is itself an initial approximation in policy space. With an arbitrary guess $f_0$, (10.1) need not be monotone. The digest's own "(added step)" in L3 uses exactly this condition, so the L2 bullet drops the condition and mislabels the scheme. The intuition note ("You can improve your guess for the value function directly … $f_1\ge f_0$ in Procedure B") invites the same misreading. | p. 89 | **critical** (dropped condition in summary) |
| B2 | L3 §5, eqs (1)–(2), and the parenthetical note | (5.1) and (5.2) are written without the domain $z\in D$. The note says "In (1) and (2) on p. 85 the text layer shows no domain". The p. 85 image prints $\int_{z\,\varepsilon\,D}$ in both. | p. 85 | minor |
| B3 | L2 bullet 6 | "Because a maximum **may fail to exist** for infinite processes". The source speaks of "the difficulty of **establishing** the existence of an actual maximum rather than a supremum". That is a difficulty of proof, not an assertion that the maximum fails to exist. L3 has it right. | p. 86 | minor |
| B4 | Whole digest (usefulness) | These terms are used without a gloss: Banach space (§8), calculus of variations (§6, §10), the Stieltjes integral $dG_q(p,z)$ (Prerequisites only say "expectation as an integral against a distribution function"), "finite closed region / jointly continuous" (§4), and Huygens' principle and branching processes (bibliography). | pp. 84, 86, 87, 115 | **major** (≥3 undefined terms) |
| B5 | Concepts, `[[hamilton-jacobi-bellman-equation]]` | It is called "mentioned only", but the name never appears. The page only says that the limit is "a nonlinear partial differential equation". The tag "(canon link; not stated in this unit)" is missing. | p. 86 | minor |
| B6 | L3 §2, §10 (coverage and wording) | Omitted: "Experience alone, combined with often laborious trial and error, will yield suitable formulations" (p. 82), and footnote 4 (the main difficulty of an existence proof is showing that the limit satisfies the *original* equation, p. 88). Also, "Making this exact is **easy** for deterministic processes"; the source says "not too difficult". | pp. 82, 88 | minor |

### B. Toy example and added steps (by hand and Python)
- **$R=(0,3,4,3,0)$:** $f_1=(3,4,3,4,3)$ and $f_2=(4,3,4,3,4)$; all 10 table cells ✓.
- **Brute force from $p=0$:** UU=4, UD=0, DU=3, DD=0 ✓. The tie claims are correct.
- **The toy illustrates the main result**: the recurrence, imbedding, and unique $f$ with non-unique policy.
- **Added step (monotonicity by induction):** correct as written. It explicitly assumes $f_0$ is the policy return, which is the condition B1 drops.

### C. Coverage
- §§1–10 and the bibliography are covered in order.
- The 94 exercises are mapped correctly by topic.
- The six "Exercises worth doing" (2, 18, 20, 21, 69, 85) have correct numbers and pages, and no solutions are given. Ex. 18's line quotes the target equation, but the exercise itself prints it.
- The length is 0.65× the target. This is appropriate, because about 70% of the source is exercise statements.

### D. Usefulness
- The Prerequisites line is close but thin (see B4).
- The intuition notes for §4, §6 and §9 are good.
- The §10 note needs the fix in B1.
- The reading notes are honest about which pages had images.

---

## 4. Kalman 1960, "A New Approach to Linear Filtering and Prediction Problems" (J. Basic Eng., pp. 35–45)

### A. Math and faithfulness
I checked the following against the images (250 dpi for pp. 42–44):
- **Equations:** (1)–(44), Theorems 1, 1-a, 2, 3, 4 and 5.
- **The proof chain** (18)–(25), including the printed switch from $\Phi^{*\prime}$ to $\Phi'$ in (24).
- **(31)–(32)**, Problem II with (33)–(37), and Table 1 row by row.
- **Examples 1–2:** all matrices, (38) and (39), and the large-$t$ limits.
- **The appendix.**

The digest's reading notes on the following are all real and correct, as is its reading of Example 2 condition 2 ($Ex_2(0)=0$, $Ex_2^2(0)=a^2$):
- the swapped proof labels (A)/(B) in Theorem 2;
- "Theorem 2-a";
- $\Phi(t+1;t)$ in (18);
- $\Phi(t+s;t+r)$ in the sum on p. 41;
- the $n\times p$ shape of $M$ in (12).

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K1 | L3 Applications, Example 1, second bullet | "$x_1(0)=0$ is known, so neither $x_1(1)$ nor **$\tilde x_1(1)$** can be predicted from $y_1(0)$." The page prints "neither $x_1(1)$ nor **$x_2(1)$**" (zoomed at 250 dpi). This is a wrong variable in a statement of the example. | p. 43 | **critical** (wrong symbol) |
| K2 | L3 "Theorem 3", intuition note | "By (28), $\Delta^*$ grows with $P^*M'$, i.e. with the prior error as seen through the measurement." This is not in the source and is false as stated. $\Delta^*=\Phi P^*M'[MP^*M']^{-1}$ is homogeneous of degree 0 in $P^*$. I checked numerically: $\Delta^*(P)=\Delta^*(10P)=(1.5,0.5)'$ in the digest's own toy. | p. 41, eq. (28) | **critical** (own claim not in the source, and false; low impact) |
| K3 | L2 bullet 3 | "The conditional mean equals the orthogonal projection onto the span of the observations if the processes are gaussian." This drops Theorem 2's hypothesis "random processes with **zero mean**". With non-zero means, $E[x|y]$ is affine and not in $\mathcal Y(t)$. L3 keeps the condition. | p. 38 | **critical** (dropped condition in summary; low impact, because every model in the paper is zero-mean) |
| K4 | L3 Dual Problem, eq. (37) | It is transcribed as $\hat P^*(t-1)=\hat\Phi^{*\prime}(t+1;t)\hat P^*(t)\hat\Phi^*(t+1;t)+\hat Q(t)$. The page prints **$\hat\Phi'(t+1;t)$** (no star) as the first factor. The two are equal by the dual of the identity the digest proves for (24), but the change is unflagged. For (24) the digest flagged the analogous switch. | p. 42 | **major** (unflagged transcription change; mathematically equivalent) |
| K5 | Whole digest (usefulness) | These terms are used without a gloss: Wiener–Hopf integral equation, spectral factorization, rational spectra, impulse response (L1 and Introduction), Hilbert space (Remark d), Schmidt orthogonalization (p. 38), "linear manifold", "realizable". Prerequisites cover inner-product spaces but none of these. | pp. 35, 38, 42 | **major** (≥3 undefined terms) |
| K6 | L3 Example 2 (p. 44 matrix); L3 Remark (o) | There are two silent misprint corrections. The page prints "$C_1(t)-tC_{\mathbf 3}(t)$" in entry (1,2) of $\Phi(t;t+1)\Phi^*\Phi$ (and "$\phi_{3s}$" in entry (3,3)). Remark (o) prints "represented by the matrix **$\hat M(t)$** in Problem I". The digest writes $C_2$ and $M$, which is correct, but the reading note says the matrix was "transcribed" from the image without noting the misprint. | pp. 43–44 | minor |
| K7 | L3 Remarks (a)–(c), Remark (b) | This omits the first half of the remark: "Aside from the note of Sherman, Theorem 1 apparently has never been stated explicitly in the control systems literature". | p. 37 | minor |
| K8 | L3 Example 2, after $P^*(t)$ | This omits "This is true also in Example 1" (that the results hold for time-varying $\phi$). | p. 43 | minor |

Observation (not counted): in Example 1, (29) gives $\Phi^*_{12}=-\phi_{11}C(t)\neq0$ (checked numerically: −0.18, −0.26, …). The printed $\Phi^*$ has 0 there, because the paper sets $\phi^*_{12}=0$ on the grounds that $x_2^*\equiv0$. The digest repeats the paper's claim that these matrices "satisfy (28–30)" and then gives the paper's justification. This is faithful, but a note would help.

### B. Toy example and added steps (Python)
- **Toy (position–velocity):**
  - $\Delta^*=(1,0)'$, then $(1.5,0.5)'$ ✓;
  - $P^*=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, then $\begin{bmatrix}2.5&1.5\\1.5&2.5\end{bmatrix}$ ✓;
  - traces 2, 4, 5 ✓;
  - check by (32) ✓;
  - data update $(2,0)\to(3.5,0.5)$ and the innovation form ✓.

  The toy illustrates the main result (recursive gain and covariance) well.
- **Added steps:**
  - (23) algebra ✓;
  - $\Phi^*P\Phi^{*\prime}=\Phi^*P\Phi'$ via $\Phi^*PM'=0$ ✓;
  - (32) from (28)–(30) ✓;
  - Example 1: $C=p/(p+b^2)$ reproduces (38) ✓; recursion run for $t=0..5$ matches (38) exactly ✓;
  - Example 2: $P^*(1)$ from the general formula at $t=1$ ✓;
  - (39) by integrating $C_2^2$ ✓ (the exact $C_1(200)$ / approx = 1.007);
  - $E\tilde x_1^2\cong a^2b^2t^2/(b^2+a^2t^3/3)$ ✓.
- **Source formulas verified by running (28)–(30) from $P^*(1)$** for $t=1..11$, with $\phi_{33}=0.4$, $a^2=1.69$, $b^2=0.49$. The closed forms for $P^*(t)$, $\Phi^{-1}\Delta^*$, $\Phi^{-1}\Phi^*\Phi$ and $\operatorname{cov}\tilde x(t|t)$ all match to $10^{-15}$ ✓.

### C. Coverage
- Every section is covered in order, including all remarks (a)–(q), Table 1, both examples and the appendix.
- There are no exercises, and the section is correctly omitted.
- The skip path is present.
- Shapes are given.

### D. Usefulness
- The Prerequisites line is good for the core.
- The derivation steps are numbered with a skip path; this is the clearest presentation of (18)–(25) I have seen in the batch.
- The Theorem 1 intuition note correctly marks "sufficient, not necessary".
- The Theorem 3 note needs K2 fixed.
- Length 0.98× the target, which is good.

---

## Fixes to apply (critical first)

1. **B1 (Bellman):** rewrite L2 bullet 8 as follows: "Both of Bellman's procedures start from an initial policy $q_0$ and its return $f_0$. Procedure B then iterates $f_{N+1}=\max_q f_N(T_q)$; because $f_0$ is a policy's return, $f_1\ge f_0$ and $\{f_N\}$ is monotone increasing. Procedure A (policy improvement) is 'more natural' but not treated here." Adjust the §10 intuition note in the same way.
2. **K1 (Kalman):** replace $\tilde x_1(1)$ with $x_2(1)$.
3. **K2 (Kalman):** replace the sentence with: "By (28), $\Delta^*$ depends on how the predicted error $P^*$ projects onto what is measured ($P^*M'$) relative to its size in measurement space ($MP^*M'$)." Or simply delete it.
4. **K3 (Kalman):** add "zero-mean" to L2 bullet 3.
5. **K4:** restore the printed $\hat\Phi'$ in (37), with a note "(equal to $\hat\Phi^{*\prime}$ by the same identity as (24))".
6. **G1, A1:** restore "Perhaps … should" and "in general".
7. **G2, A2, B4, K5:** add ≤15-word glosses at first use, or extend the Prerequisites lines.

## Improvements to the pipeline (up to 3)

1. **Check L1/L2 against the hypotheses of the matching L3 passage.** For every L1 sentence and L2 bullet that cites a theorem, procedure or example, the verifier should:
   - extract the hypotheses and hedges from the L3 passage it summarises (for example "zero mean", "$f_0$ = return of $q_0$", "in general", "perhaps");
   - require each one to appear in the summary, or require the summary to say "under conditions".

   Three of the four critical-or-hedge errors in this wave (B1, K3, A1) were introduced in compression, with L3 correct.
2. **Treat intuition notes as claims.** Any intuition note that states a mathematical relationship ("grows with", "is proportional to", "always") must either quote the source or pass a quick check. The verifier can do this with a scaling test or a toy-instance check, as was done here for K2. Otherwise, rephrase it as qualitative.
3. **An "as printed" lint for equations and symbols.** Whenever an L3 equation or a symbol in prose differs from what the verifier reads off the image, the verifier should require one of two forms: "(as printed)" with a note, or "(corrected; page prints …)". This covers K1, K4 and K6, and it makes the good behaviour already shown for (18), (24) and (10.2) systematic. The glossary pass from the wave-1 recommendation (3c) is still needed: all four digests failed it.

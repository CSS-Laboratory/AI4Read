# Blind judgement: Lens 3 · Bayesian inference (Xie et al. 2022)

Judge: blind (versions shown as A and B; key read only after scoring). Date: 2026-10-16.
Rubric: WRITING.md v0.3, CHARTER §5–6. Facts checked against the Xie PDF (pdftotext, pp. 1–12), plus the source brief, the digest, Gelman BDA3 PDF p. 7 and Brown et al. 2020 PDF pp. 4, 24, 34. All toy numbers were rerun in Python.

Length (visible words, excluding the dev-spec comment): A 554, B 993.

## Scores (1–5)

| Criterion | A | B |
|---|---|---|
| 1. Factual accuracy and hedges | 4 | 4 |
| 2. Ladder for a high-school reader | 3 | 5 |
| 3. Clarity, B2–C1 English | 4 | 4 |
| 4. Insight and connections | 3 | 4 |
| 5. Illustration / interactive, buildability | 1 | 4 |
| 6. Concision | 5 | 3 |
| **Mean** | **3.3** | **4.0** |

**Overall preference: B**, confidence about 80%. A is cleaner and shorter, but it gives the reader no numbers, no check and no picture. These are steps the house rules require, and B supplies all three, with correct numbers.

## Error lists

### A: 0 critical, 0 major, 3 minor

1. **Minor (dropped conditions).** “the language model fits the training distribution exactly, and the concepts are distinguishable enough. Under these conditions, prediction reaches the best possible accuracy …” (Theorem 1, p. 7). Theorem 1 needs *all* the assumptions in §2.1 (pp. 4–5): delimiter states, bounded delimiter transitions, prompt-start shift, regularity, and **well-specification (Assumption 4: the prompt concept θ\* is in Θ)**. “Under these conditions” makes three of them look like the full list. Well-specification is exactly the condition behind the unseen-concept failure that A reports two sentences later, and A does not link the two.
2. **Minor (wording, slightly strengthened).** “prediction *reaches* the best possible accuracy as the number of examples grows.” Theorem 1 is a limit (n → ∞): “lim L0-1(fn) = inf L0-1(f)” (p. 7). “Approaches” would be more accurate.
3. **Minor (attribution).** The Einstein/Gandhi/Curie → “Polish” example is given as the model's answer without saying the source: “GPT-3 places the largest probability on the correct output” (p. 1).

Checked and correct: the formula and the “marginalizes out the latent concepts” claim (p. 2); “selects” (p. 3); unseen concepts fail (p. 10, Fig. 4 right on p. 9); 10–40% order sensitivity (p. 10, in GINC); zero-shot sometimes better than few-shot (pp. 10–11, Fig. 7); “a first step” (p. 12). The one number A uses (10–40%) matches p. 10.

### B: 0 critical, 0 major, 5 minor

1. **Minor (borderline major; wrong direction in the figure caption).** “Interactive (toy numbers): add examples and watch belief move **from A to B**.” In B's own toy, belief moves *toward* A, the true concept (0.5 → 0.8 → 0.941 …). A reader who trusts the caption reads the figure backwards. One-word fix.
2. **Minor (mislabelled equation).** Link-type line: “the model's prediction is Bayes' rule written out (p. 2)”. Eq. (1) on p. 2 is the *posterior predictive*, which marginalizes over concepts. Bayes' rule appears explicitly only in eq. (5), p. 6 (“Bayes' rule, drop the constant”). B gets the distinction right later in the text, so this is only a labelling slip.
3. **Minor (our judgement given a page).** “It does not show that real LLMs compute posteriors (pp. 7, 10).” The paper never says this. It is our reading of p. 7 (theorem inside the model) and p. 10 (synthetic data), and it should be labelled “ours”. The source brief also gives it without a page, under “Careful!”.
4. **Minor (attribution).** “The most likely next word is ‘Polish’ (p. 1)” after “Give a model this prompt”. The paper says GPT-3 (p. 1).
5. **Minor (misleading simplification in the toy, ours).** The table and the “0.9 ceiling” show the *predictive probability* of the right answer. Xie's theorem is about the *argmax* predictor fn (p. 4, p. 7), which in this toy is already right from n = 1 (P(right) = 0.74 > 0.5). In GINC the target is the argmax, “so that the intrinsic error is 0” (p. 10). The ceiling is still coherent if the label is sampled from p_prompt (then 0.9 is the Bayes-optimal accuracy). But the text does not say this, and the lens summary turns the 0.9 into a general claim (“it cannot rise above what that concept itself can answer”).

Also noted, not counted: “our world W4” is internal jargon a reader does not know. The Gelman et al. 2013 citation is outside the source brief, but I checked it: BDA3 printed p. 7 has eq. (1.2), p(θ|y) ∝ p(θ)p(y|θ).

Checked and correct: e^{n·r_n(θ)} p(θ) and r_n as the average log-likelihood ratio (p. 6, eq. 6); assumptions of a mixture of HMMs and an exact fit (pp. 2–3); “selects” (p. 3); Theorem 1 “under the assumptions and distinguishability” (p. 7); distinguishability as per-example KL signal against mismatch error terms at the start and delimiter tokens (Condition 1, eqs. 13–14, p. 7; mismatch p. 4); a 4-layer Transformer in the ablations (p. 10); one concept or unseen concepts make ICL fail (p. 10); larger models do better at equal loss, 1.33 val loss (p. 10, Table 6 on p. 11); “a first step” (p. 12). Brown et al.: terms “agnostic” (p. 4), scrambling “appear to learn … cannot confirm” (p. 24), the spectrum (p. 34): all verified.

Numbers rerun in Python: 0.5×0.2 = 0.10, 0.5×0.05 = 0.025, total 0.125, posterior 0.8. P(A) for n = 0..4: 0.500, 0.800, 0.941, 0.985, 0.996 (= 4ⁿ/(4ⁿ+1)). P(right): 0.500, 0.740, 0.853, 0.888, 0.897. Check at n = 2: 0.02 / 0.02125 = 0.941 = 16/17. ln(0.05/0.2) = −1.386, and e^{−1.386n} = 4^{−n}. **All correct**, and all consistent with toyworlds.md W4.

## The 3 most important differences

1. **The ladder, with real numbers and a check.** B runs a two-concept toy: prior → likelihood → posterior → odds that grow ×4 per example → marginalized P(right) → table → formula → explicit check (n = 2 gives 0.941). It also ties Xie's e^{n·r_n} to the toy (r = ln 0.25, so e^{rn} = 4^{−n}). A's instance (a library of document styles) builds good intuition and defines prior, likelihood and posterior, but it has no numbers and no check. It sends the reader to “rung 8” for the arithmetic, so the lens cannot stand alone (WRITING §2, steps 1 and 5).
2. **Illustration.** B gives a complete, buildable dev spec: three sliders, fixed toy values, the formulas, four outputs including live arithmetic, an edge case for prior = 0, and 375 px. Setting the prior to 0 turns Xie's unseen-concept failure into something the reader can see happen. A has no figure (WRITING §5).
3. **What the lens says the model knows.** B: a menu of pretraining concepts with prior weights; a prompt is *evidence, not teaching*; the answer is a weighted vote; it is capped by the best concept in the menu. B then notes what the posterior story does not explain (larger models beat equal-loss models) and links to GPT-3's own agnosticism. A's summary (a prior over kinds of documents, plus narrowing it down) is correct and well hedged, but thin. A's real advantage is concision and a smoother read.

## What A needs to reach B

- Add numbers to the library instance (e.g. two or three styles, prior 1/3 each, a likelihood for each line), with an odds-per-example pattern and one explicit check against the formula. Or give the section a short version of rung 8's toy, so the lens stands alone.
- Name all of Theorem 1's assumptions, at least “and the prompt concept is one the model has seen (well-specification)”. Link that to the unseen-concept failure. Change “reaches” to “approaches, in the limit”.
- Add a small figure or interactive (posterior bars that move with n, and a prior slider that shows a zero prior never recovers).
- Expand the lens summary: a prompt as evidence rather than teaching, the weighted vote, the cap set by the best concept, and what the theory does not explain (scaling at equal loss, p. 10).

(For B to be publishable: fix the caption direction, relabel eq. (1) as “posterior predictive”, label the “does not show” sentence as ours, name GPT-3, say whether “P(right)” means sampling or argmax, and cut about 15% of the text: the link-type paragraph and the dense e^{n·r_n} paragraph could be shortened or moved into a “Look inside” fold-out.)

Key: A=P B=Q (from /tmp/claude-0/judge_key.txt, read after scoring. P = the current post section, Q = phase2/test0/lens3-sonnet.html.)

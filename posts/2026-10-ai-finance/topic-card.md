---
name: post02-topic-card
description: S0 topic card for post 02, "Can AI invent a new kind of finance, and what would that do to a human-centred system?" Planner output, 2026-10-17.
---

# Topic card, post 02

## 1. The question
**High-school version.** If machines invent money contracts that no person can understand, who can still check them, and what happens to a society built on people checking money?

**Research version.** Under what conditions would AI-made financial instruments become opaque to every human overseer? Which failure channels follow (information asymmetry, correlated model use, cascades)? Which institutional layers (regulation, delegation, money's status) would be stressed?

**Framing decision.** Harari says "AI", never "LLMs". Post 01 is about LLMs. I propose a sentence in the hook: "Harari says AI. We ask what an LLM-based system could and could not do." See Decision 1.

## 2. Why it matters for 3C
- **Computation:** LLM agents in our own social simulations are correlated by construction. The "effective number of independent agents" below is a check we should run on them.
- **Communication:** Harari's thesis is that money is a story. This links to narrative economics (Shiller) and to the "fake money" theme.
- **Collaboration:** who invents new instruments is an innovation question (DeFi, open-source communities).

## 3. What the post will and will not claim
**Harari, exactly** (quotes ≤25 words; machine transcripts must be checked against audio before printing):
- BIS, 7 May 2024, [9:54]: "Now imagine a situation maybe in 10 years when AIs create a new financial device, which is orders of magnitude more complicated than CDOs."
- WEF Davos, Jan 2026, [31:54–31:59]: "Maybe nobody in the room, no human in the room, understands the financial system anymore, because it's dominated by AIs."
- *Nexus* (2024), p. xxxii: asks what happens "if the financial system is increasingly controlled by AI and the very meaning of money comes to depend on inscrutable algorithms."

**Paraphrase check (stated in the post).** The 10-year line merges two talks. He frames it as "imagine", "maybe" and "suppose". His worry is incomprehension, then unregulatable crises, then lost democratic accountability. He calls an AI financial crisis "catastrophic" but "by itself" not existential (Guardian, 2023). Kunhao's "LLMs will replace our human-centred society" is stronger than anything in the record.

**Will claim:** what each lens implies if the scenario happens (conditionals). The strongest critics get a fair hearing: Poole (credulous about AI's creativity), Narayanan & Kapoor (slow, human-controlled), FSB (existing frameworks cover much), Skingsley (we trust planes we don't understand), Fox (firms' profit motives missing).
**Will not claim:** that it will happen, or that LLMs can invent instruments today. That evidence is **UNSEEN**: I used no network. S1 must search for 2025–26 evidence.

## 4. Decomposition and lenses
| Sub-claim | Lens | Likely verdict |
|---|---|---|
| (a) AI can invent "new finance" | none; a definition plus critics | open |
| (b) it could be beyond human understanding | 1 Information theory | conditional |
| (c) so regulators lose control | 2 Cybernetics | conditional |
| (c') failures become correlated | 3 Decision, game & Bayes | supported in theory |
| (d) "taking over" money itself | 4 Philosophy | depends on institutions |

*"New" for (a):* a payoff table not in the human catalogue that a counterparty will pay for. It is a short definition box, not a lens. Humans already invented CDOs, so "new" does not mean "incomprehensible".

**Lens 1 · Information theory (links back to post 01).**
- *Works:* `wiki/works/shannon-1948-mathematical/main-p1.md`, `cover-2006-elements/ch02`, `mackay-2003-information/ch04` (all audited); `hayek-1945-knowledge/main.md`; gap Arora et al. 2011.
- *Link type:* the counting is same-math. Hayek's "prices compress knowledge" is a metaphor (wiki bridge). "Understanding = short description" is ours (structural analogy).
- *Only this lens shows:* incomprehension is the typical case. A village with 4 weather states (W1) and payouts 0–9 has 10^4 contracts; a table needs 13.3 bits, and at most 2^k tables have a k-bit description. Novelty is cheap; explainable novelty is rare.
- *Limit:* short description does not mean easy valuation. A CDO's rules are short, yet hard to price. That gap is Arora's computational-hardness result, which is not information theory.

**Lens 2 · Control & cybernetics.**
- *Works:* `ashby-1956-cybernetics/ch11-requisite.md` and `ch10-regulation.md` (audited), `ch13-regulating.md`, wiki `law-of-requisite-variety`.
- *Link type:* variety and entropy are same-math (Ashby, pp. 207–211). Regulator = supervisor is a structural analogy (ours).
- *Only this lens shows:* control needs variety. V_outcome ≥ V_disturbance − V_regulator. The two levers are raising the regulator's variety (AI supervisors) or cutting the variety of allowed instruments (standardised contracts).
- *Limit:* Ashby's table has a passive disturbance. Finance is adaptive and adversarial (Lucas, Goodhart; both gaps). It also does not say who regulates the AI regulator.

**Lens 3 · Decision & game theory, with one Bayesian step.**
- *Works:* `keynes-1936-general/ch12-state.md` (audited), `morris-2002-public/main.md`, `xie-2022-icl/main.md` (audited, toy W4), `minsky-1992-instability/main.md`, `granovetter-1978-threshold`, `mitchell-2009-guidedtour/ch16`.
- *Link type:* the effective-sample formula is same-math. Morris–Shin to markets is a structural analogy. Keynes ↔ post 01 theory of mind (level-k) is a historical link.
- *Only this lens shows:* failure needs no error. If ten banks use one model, their mistakes coincide. The effective number of independent opinions is N/(1+(N−1)ρ); N=10, ρ=0.9 gives 1.1 (code-checked). A Bayesian who counts a shared signal n times jumps from 0.8 to 0.996 (W4 ratio 4, reused arithmetic, new story).
- *Limit:* a stylised toy. It says nothing about how widely LLMs are actually adopted. Collusion (Calvano 2020) can be a fold-out on Axelrod ch02 (audited).

**Lens 4 · Analytic philosophy of social reality.**
- *Works:* `dennett-1987-intentional-stance/ch02-true.md` (audited), wiki `speech-act`, `performative-utterance`, `convention`, `keynes ch17` (money); gap Searle.
- *Link type:* conceptual analysis, no math. Status functions ↔ post 01's speech acts is a structural analogy. Intentional stance ↔ legal personhood is a metaphor.
- *Only this lens shows:* "taking over" splits in two. An AI can write contracts. Money is "X counts as Y": it needs collective acceptance, which includes who counts as a legal person (Harari's AI-person worry, WEF 2026).
- *Limit:* not empirical. Without Searle, claims stay thin. Delegation (Lupia `ch05-delegation`, `ch10-institutions`; Stiglitz) enters in the synthesis: we do not need to understand a plane if verification and penalties exist.

**Synthesis (four layers, certain to contested):** (1) the contract space is huge; (2) opacity favours the better-informed side (Akerlof, Arora); (3) a shared model correlates failures; (4) whether this changes who rules depends on rules of acceptance and liability.

## 5. Hook, guess-first, toy world
**Hook: "Two contracts".** A village (W1) offers two contracts. A: "pay 5 coins if it rains or snows". B: a table of 30 payouts that look random. Which can you explain in one sentence? Then the BIS exchange: Harari says maybe 1% of people understand finance, and Skingsley replies that we board planes we don't understand. What is different about money?

**Guess-first:**
1. How many contracts can the 4-weather village write if each state pays 0–9? (10,000)
2. Ten banks each run a model right 99% of days. How often are all ten wrong together if the models are independent? And if it is the same model? (10^-20, vs 1%)
3. An AI invents "new money". What decides whether it is money? (acceptance, not code)

**Toy worlds.** W1 for contracts and the Ashby table. W4 arithmetic for the double-count. New world W5, a six-bank network (to be added to `toyworlds.md`).

## 6. Interactives (library widgets only)
1. **`cascade`, six banks.** The reader taps one bank, then three banks that run the same model, then raises the `capMult` slider. Edge case: more capital should stop the spread. The writer must tune the toy exposures so that one failure is contained and three simultaneous failures are not, and confirm it with `check.mjs`.
2. **`iterate`, share m on one model.** Price gap: p(t+1) = p + A·m·(p − p_prev) − G·(1−m)·p, shock −1 at t=3. Toy A=1.5, G=0.5 (to be rerun in `check.mjs`). It is stable at m=0.2; at 0.67 it tips; at 0.9 it blows up. A clamp stands for a circuit breaker. The reader moves m. Not LLM-specific.
3. **`stepper`** (not interactive): the Ashby table with W1, V_D = 2 bits.
Optional `lab`: N_eff versus ρ.

## 7. Sources
**In KB:** audited digests are marked above. Verify against pages in S1: hayek, akerlof (page-checked only), grossman, morris, minsky, granovetter, lupia, mitchell ch16, ashby ch13.
**Harari record:** `phase2/post02/harari-claims.md`; transcripts in `posts/2026-10-ai-finance/sources/`.
**Gaps, free sources (all URLs to verify):**
- Arora, Barak, Brunnermeier & Ge 2011 (CACM): authors' pages (Barak, Princeton CS). **Priority.**
- FSB 2024: https://www.fsb.org/uploads/R14112024.pdf
- Narayanan & Kapoor 2025: https://knightcolumbia.org/content/ai-as-normal-technology
- Gensler & Bailey 2020 (SSRN); Danielsson et al. 2022 (SSRN/VoxEU); Calvano et al. 2020 (author copy).
- Social ontology: SEP "Social Institutions", "Social Ontology".
- Diamond & Dybvig: https://www.minneapolisfed.org/research/qr/qr2412.pdf (in the free manifest).
- Financial Crisis Inquiry Report 2011 for the CDO facts (govinfo).

**Request from Kunhao:** *Nexus* PDF (for page numbers), Searle 1995 or 2010 (or accept SEP), Haldane & May 2011 (paywalled).
**Not used:** claim 20 (El Economista). Treat claims 17–19 as secondary.

## 8. Decisions for Kunhao
1. **"AI" or "LLMs"?** Keep Harari's "AI" and add an LLM section, or narrow to LLM agents.
2. **Scope:** all four lenses (long), or cut Lens 4 and the collusion fold-out and keep Harari's money-as-story for post 03?
3. **Verdict tone:** conditionals only, or end with our own estimate of what is most likely?

---
## Meta-manager review (2026-10-17)
**Gate: pass, with the edits below.** The record of Harari's claims is faithful and the hedges are kept. Each lens states its "only this lens shows" and its limit. All numbers were rechecked in Python:
- log₂10⁴ = 13.29 bits;
- N_eff = 1.099;
- 256/257 = 0.996;
- 0.01¹⁰ = 10⁻²⁰;
- iterate toy: the largest root modulus is 0.548 at m = 0.2, 1.002 at m = 0.67, and 1.162 at m = 0.9, so it tips where A·m = 1, i.e. m = 2/3.

**Edits for S1/S3:**
1. **Add a "home field" section (CHARTER §5.3).** Cover what finance already looks like with algorithms: CDOs and 2008 (FCIC report), algorithmic and high-frequency trading, the 2010 Flash Crash (Kirilenko et al.), Q-learning pricing agents that learn to collude (Calvano et al.), LLM trading-agent studies (Lopez-Lira & Tang; Scheurer et al. on deception), and AI agents holding crypto wallets (2024–25). Sub-claim (a) can only be answered from this evidence. S1 must fetch it.
2. **Iterate toy:** say plainly that it models *trend-following* by the share m that uses one model. Shared models do not imply trend-following, so the widget shows the correlation-and-amplification channel, labelled "toy, ours".
3. **Lens 1:** AI-made instruments are optimised, not random, so the counting argument shows only that explainable novelty is *rare among possible* contracts. The step from rarity to opacity is Arora's (computational hardness plus information asymmetry), and it must be cited from the paper itself.
4. **Lens 4** should carry Kunhao's actual question: what "human-centred" institutions rely on. That means acceptance (money as a status function), accountability (delegation, Lupia) and legal personhood (Harari, WEF 2026; Milei/FT is secondary only).
5. Add W5 (six banks) to `toyworlds.md` when the writer fixes its numbers.

## Kunhao's decisions (2026-10-17) — S0 GO
1. Keep Harari's "AI" and add one section on what LLM agents add (natural-language contracts, agents with wallets, shared foundation models).
2. All four lenses; Lens 4 compact; collusion as an optional fold-out.
3. End with conditionals plus a short reading labelled "ours", with signs to watch that would change it.
4. Kunhao will add *Nexus* (2024), Searle's *The Construction of Social Reality*, and Haldane & May 2011 to the library. Their units are added in an S1b pass.

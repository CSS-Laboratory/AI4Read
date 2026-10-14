---
id: wei-2022-cot/main-p2
work: wei-2022-cot
unit: paper (part 2/2) — Appendices C–H
pages: 24-43
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models — Appendices C–H

## L0 — One line
The appendices place chain-of-thought prompting among related work, check by hand that its reasoning chains are mostly sound when answers are right, show how they fail when answers are wrong, and print every prompt used.

## L1 — The gist (≤ 120 words)
This part asks how far the generated chains of thought can be trusted and how the results can be reproduced. The authors compare their method with related work (prompting, explanations, program execution, intermediate steps). They read 50 correct and 50 incorrect chains from the language model LaMDA 137B on GSM8K math word problems. In that sample, almost all correct answers rested on sound reasoning. Wrong answers mix small fixable errors with deeper misunderstanding. They say that generated reasoning has no guarantee of being coherent or factual. They also test the number of exemplars, list datasets and compute, give input/output examples, and print all few-shot prompts, including prompts written by other annotators.

**Prerequisites:** few-shot prompting (exemplars placed in the prompt); the idea of a chain of thought as a series of reasoning steps written before the answer; basic arithmetic.

## L2 — Key ideas (5–10 bullets)
- Chain-of-thought (CoT) prompting augments the model's *outputs* with reasoning. Instructions augment the *inputs*, and natural-language explanations (NLEs) usually come with or after the answer (p. 24).
- In the authors' view, prior intermediate-step work mostly needs finetuning on annotated or synthetic data. CoT elicits steps from off-the-shelf models by prompting alone (p. 25).
- Of 50 correct GSM8K chains from LaMDA 137B, 49 had correct logic and math, and only 1 was correct by chance (p. 25).
- The authors think this is likely because free-response answers are hard to hit by coincidence. For multiple-choice or binary tasks, a right answer from wrong reasoning is much more likely (p. 25–26).
- Of 50 wrong chains, 8% had only a calculator error, 16% a symbol-mapping error and 22% a missing step. 54% needed substantial edits (p. 27–28).
- Adding a Python calculator raised LaMDA 137B's GSM8K solve rate from 14.3% to 17.3% (p. 27).
- The authors state there are no guarantees that generated reasoning is coherent or factual. They name verifier-based scoring of several sampled paths as one possible remedy that needs a trained verifier (p. 28).
- The CoT gain over standard prompting appears robust to the number of exemplars (p. 28–29).
- The appendices give everything needed to re-run the work: prompts (Tables 20–28), dataset sources, compute, and alternate annotators' chains (p. 30–43).

## L3 — Walkthrough

### C. Extended Related Work (p. 24–25)
The authors say CoT is inspired by prompting, natural language explanations, program synthesis/execution, numeric and logical reasoning, and intermediate language steps (p. 24).

**C.1 Prompting.** The paper belongs to general prompting approaches, where input prompts are optimized so one model does many tasks (p. 24). *Instruction* work augments input–output pairs with meta-data, but instructions are typically prepended to the input. CoT augments the model's outputs (p. 24). Separate HCI work (Wu et al. 2022a,b) found that chaining sequential model generations improves outcomes in a 20-person user study (p. 24).

**C.2 Natural language explanations (NLEs).** NLE work often aims at interpretability and usually targets natural language inference. It produces explanations at the same time as, or after, the prediction. CoT comes *before* the final answer (p. 24). The authors' goal is to let models split multi-hop reasoning into steps; interpretability is only a side effect, not the aim (p. 24). Marasović et al. (2022) show prompt-based finetuning with NLEs improves NLI and classification, but mostly study explanation plausibility. This paper instead covers arithmetic, commonsense and symbolic tasks (p. 24).

**C.3 Program synthesis and execution.** Intermediate steps have a long history here. Perhaps closest is Nye et al. (2021): large LMs can do up to 10-digit addition, evaluate polynomials and execute Python programs (p. 24). The authors say they generalize such domain-specific primitives to natural language, which is open-domain and relevant in principle to any text-to-text NLP task (p. 24).

**C.4 Numeric and logical reasoning.** Prior work injects numeric skill with executable operations on BERT, a graph neural network, or specialized training (Andor 2019; Ran 2019; Piękos 2021). Logical reasoning is often handled by verbalizing rules in natural language (p. 24). Recchia (2021) shows finetuning enables longhand "module" operations (wording as printed) (p. 25). The authors say such work is often task-specific and uses finetuning. They show CoT prompting works across many tasks without finetuning (p. 25).

**C.5 Intermediate language steps.** Prior work shows that natural-language intermediate steps can improve performance and robustness, speed up training, and mitigate bias, and can help in image and RL settings (p. 25). Prior work typically finetunes on manually annotated or synthetic step datasets. The authors show such abilities can be elicited in off-the-shelf models of sufficient scale by prompting. They stress this allows intermediate-step reasoning without a large number of labeled annotations, and one model can do many reasoning tasks with no gradient updates (p. 25).

### D. Additional Analysis (p. 25–29)

**D.1 Correct chains.** The authors analyzed 50 chains from LaMDA 137B that reached correct GSM8K answers (p. 25).
- Only 1 reached the answer through incorrect reasoning ("correct by chance"). The other 49 had correct logic and math (p. 25).
- Five of the 49 had minor imperfections but still coherent logic (p. 25): one with underspecified statements, one with an unrelated but correct statement, two with correct logic but omitted equation steps, and one with correct math but inverted semantics (p. 25).
- Examples (Table 8): James runs 60 meters × 3 sprints × 3 times, so 60 × 9 = 540. Brandon's phone is 4 × 2 = 8 times older than Suzy's, so 8 × 1 = 8 years. Jean has 30 − 2 = 28 lollipops, so 28 / 2 = 14 bags (p. 25).
- Table 9 examples: in the penguin problem (36 penguins, one-third swim, one-third go inside) the chain gets 12 and 12 and then answers 12 without showing the subtraction ("correct by chance"). In the gas problem the cashback equation mixes cents and dollars (20 x 10 = 2 dollars). In the Nissa elves problem the equation 60 - 1/3 = 40 is imperfect, though the final answer is right (p. 26).
- **Limitation (authors):** the high correctness is likely because free-response questions are hard to answer correctly by coincidence. For multiple-choice or binary problems, a right answer via a wrong path is much more likely, e.g. on all commonsense datasets they evaluate. Future work should analyze the factuality of such chains (p. 25–26).
- Table 9's caption says "7 salient cases" and "other 43", while the text counts 1 + 5 = 6 imperfect chains (see Reading notes) (p. 26).

*Intuition note:* In this small sample, when the model's final answer was right, its reasoning was usually right too. That check works best for open-ended numeric answers, because a guess is rarely right by luck.

**D.2 Incorrect chains.** The authors read 50 randomly sampled wrong LaMDA 137B outputs on GSM8K. Because error design is non-trivial, they classify errors by *what edit would make the chain correct*, to see how models might improve (p. 27).
- **Calculator error only: 8%.** The chain is fully correct except for arithmetic, so an external calculator (as in Cobbe et al. 2021) would fix it. With a Python calculator, the GSM8K solve rate for LaMDA 137B rose from 14.3% to 17.3% (Table 2, in the other part of the paper). A further 34% had calculator errors *plus* other errors. The rest of the categorization ignores calculator errors (p. 27).
- **Symbol mapping error: 16%.** The chain is correct except for number symbols, and fixing only the equations (not the words) makes the whole reasoning process correct. This is limited to chains that can become fully correct, not just correct in the final answer. The authors anticipate the objection that one could paste the right equation into any chain (p. 27). Example: for Jill's salary the model wrote "15 x 30" where "15 x 50" was needed (p. 27).
- **One step missing: 22%.** Adding one missing step makes the chain correct. Example: Kelian's two recipes; the model finds 40 instructions for the second and answers 40, but must add 20 + 40 (p. 27).
- **Remaining 54% (27 of 50)** need substantial edits. Almost all involve some semantic-understanding error. 8 of the 27 also had incoherent chains, with statements not following from earlier ones or violating basic world knowledge (p. 28). Examples (Table 11): Gretchen's 110 coins, where the model computes 110 − 30 = 80 silver and then 110 − 80 = 30 gold, missing that 110 is the total. In the dance-class problem, the model derives the equation (25 + 20) − (25 + 20) = 100% (p. 28).
- **Conclusion (authors):** there are no guarantees that LLM-generated reasoning is coherent or factually correct. Wrong reasoning can give wrong answers or accidentally right ones, with accidental success more likely in binary classification than in free response. Better factuality could be expected to potentially improve multi-step reasoning. 28).

*Intuition note:* About half the errors (calculator, symbol, missing step: 8 + 16 + 22 = 46%) look like small repairs. The other half (54%) need substantial edits, and almost all of those involve some semantic-understanding error.

**D.3 Robustness to number of exemplars.** The main experiments use 8 exemplars, limited by the 1024-token input length. The authors compare CoT with standard prompting for LaMDA 137B on the five datasets where standard prompting had a mostly flat scaling curve. Figure 11 shows the CoT improvement remains as the number of exemplars varies (p. 28). In the figure, GSM8K, MultiArith, Sports and Coin Flip vary 1–8 exemplars, and Last Letter Concatenation varies 1–4 (p. 29).

**Table 12 (benchmarks, evaluation sizes N):** GSM8K 1,319; SVAMP 1,000; ASDiv 2,096; AQuA 254; MAWPS: SingleOp 562, SingleEq 508, AddSub 395, MultiArith 600 (p. 29).

### E. Additional Details (p. 30–31)
- **Version control:** V1→V2 added PaLM (V1 had only LaMDA). V2→V3 added GPT-3, SVAMP, AQuA, SayCan, the extended related work, ablations (Table 7), FAQ (Appendix A) and raw results (Appendix B). V3→V4 and V5→V6 fixed typos in Figure 3. V4→V5 added Codex and UL2 results (p. 30).
- **E.1 Reproducibility:** LaMDA and PaLM are not public, so the authors give exact prompts (Tables 20–27 in their text; the prompt tables printed here run to Table 28), use the public GPT-3 API at four scales (text-ada-001, text-babbage-001, text-curie-001, text-davinci-002), and release LaMDA 137B inputs, targets and predictions in the supplement. No finetuning was done (p. 30).
- **E.2 Compute:** inference only. LaMDA 137B: TPU v3 (8×8, 64 chips / 128 cores). PaLM 540B: TPU v4 (4×4×12, 192 chips / 384 cores). GPT-3 via the public API (p. 30).
- **E.3 Datasets:** arithmetic: AddSub and MultiArith (Math Word Problem Repository), ASDiv, AQuA, GSM8K (MIT licence), SVAMP (MIT licence). Commonsense: CSQA, StrategyQA (open-domain question-only setting from BIG-bench), Date and Sports understanding (BIG-bench, Apache v2), SayCan (CC BY 4.0). Symbolic datasets were created synthetically (p. 30–31).

### F. Input/Output Examples (p. 32–34)
Tables 13–19 show correct and incorrect LaMDA 137B chains (PaLM 540B for SayCan). The incorrect ones show these failure types:
- Letter concatenation: a wrong last letter ("m" for "Friedman") (p. 32).
- Coin flip: the chain claims "flipped by Kristian" although Kristian does not flip, so it counts 1 flip and answers "no" (p. 32).
- CSQA: chooses "bone" where the ground truth is (d) (p. 32).
- StrategyQA: the chain reasons that Harry Potter is fictional, so he can do anything, and answers yes although the ground truth is no (p. 33).
- Date understanding: wrong date arithmetic, e.g. one week before the day after "today" (p. 33).
- Sports understanding: attributes "backhanded a shot" to basketball; ground truth is hockey (p. 33).
- SayCan: plans for a "sprite" that is not in the scene, and calls lime soda salty (p. 34).

### G. Full Prompts (p. 35–41)
Few-shot exemplars, each with a chain of thought before the answer (blue shading in the images marks the chain). Counts: math word problems 8 (all datasets except AQuA; Table 20), AQuA 4 (Table 21), last letter 4 (Table 22), coin flip 8 (Table 23), CSQA 7 (Table 24), StrategyQA 6 (Table 25), date 6 (Table 26), sports 8 (Table 27), SayCan 7 (Table 28). Formats:
- Math: each chain restates the quantities, shows the equation (for the first exemplar, 21 - 15 = 6), and ends with a fixed closing sentence giving the answer (p. 35)
- Coin flip uses a parity argument: count the flips, say whether odd or even, then give the result (p. 37).
- CSQA: each chain states what the answer must be, says which listed choice fits (usually using the word only), then ends with the chosen letter (p. 38)
- SayCan: lists locations and objects, the allowed actions pick/put/find, then gives "Explanation" and a numbered "Plan" ending in done() (p. 41).

### H. Alternate Annotators for MWP (p. 42–43)
Tables 29 and 30 give the same 8 math exemplars as Table 20 with chains rewritten by "Annotator B" and "Annotator C". Table 20 was by Annotator A. All annotators were co-authors familiar with the goal of CoT prompting (p. 42). For example, for the Shawn toys problem, B writes "2 * 2 = 4 more, now he will have 5 + 4 = 9", while C splits it into 5 + 2 = 7 and 7 + 2 = 9 (p. 42–43).

## Toy example (ours, not from the text)
Question: "A shop has 4 boxes with 12 pens each. 10 pens are sold. How many are left?"

Correct chain: 4 × 12 = 48 pens; 48 − 10 = 38. The answer is 38.

Using the D.2 categories on three wrong chains:
1. "4 × 12 = 46; 46 − 10 = 36." The setup is right and only the arithmetic is wrong (4 × 12 = 48). A calculator repairs it: 48 − 10 = 38. This is *calculator error only*.
2. "4 boxes of 12 pens, so 4 × 10 = 40; 40 − 12 = 28." The words are right, but the numbers in the equations are in the wrong slots. Changing only the equations to 4 × 12 and 48 − 10 gives 38. This is a *symbol mapping error*.
3. "4 × 12 = 48. The answer is 48." The chain stops one step early. Adding "48 − 10 = 38" repairs it. This is a *one step missing error*.

A chain such as "4 + 12 = 16, so 16 pens" shows no grasp of the problem. It would need rewriting from scratch, which is the 54% group.

## Concepts
- [[chain-of-thought]] — reasoning steps the model writes before its answer; here contrasted with instructions (input) and NLEs (with or after the answer) (p. 24)
- [[zero-shot-few-shot-prompting]] — the method uses a fixed few-shot prompt (8 exemplars in the main experiments per p. 28; the printed prompts in Tables 20–28 have 4 to 8), with no finetuning (p. 28, p. 30)
- [[supervised-fine-tuning]] — prior intermediate-step work trains on annotated or synthetic steps; CoT needs no gradient updates (p. 25)
- [[cot-error-taxonomy]] (new) — wrong chains classed by the edit that fixes them: calculator error, symbol mapping, one step missing, or substantial edits (semantic or incoherence) (p. 27–28)
- [[correct-by-chance]] (new) — right final answer from flawed reasoning; more likely for multiple choice and binary tasks (p. 25–26)
- [[verifier-reranking]] (new) — a possible remedy: sample several reasoning paths and score each with a trained verifier (p. 28)

## Canonical instances
- [[gsm8k]] (new) — math word problems used for the correct and incorrect chain analysis (p. 25–28)
- [[saycan-planning]] (new) — robot planning task with an Explanation and Plan prompt (p. 34, p. 41)
- [[strategyqa]] (new) — yes/no commonsense questions; chains can reach wrong answers (p. 33, p. 39)
- [[coin-flip-last-letter]] (new) — synthetic symbolic tasks with parity and letter-extraction chains (p. 32, p. 36–37)

## Bridges (candidates)
- [structural-analogy] CoT error taxonomy by minimal edit ↔ software testing: classifying bugs by the smallest patch that fixes them — both sort failures by repair cost.
- [structural-analogy] Calculator tool lifting 14.3% → 17.3% ↔ tool use in LLM agents: delegating exact computation to an external program.
- [metaphor] Correct-by-chance answers ↔ right answer, wrong working in an exam: the final answer alone does not show understanding.

## Questions this raises
- How can one measure the factuality of chains of thought at scale, beyond reading 50 samples by hand?
- Would a trained verifier that scores many sampled paths fix the semantic-understanding errors that make up most failures?
- Do chain-of-thought gains depend on who writes the exemplars? What do Tables 29–30 imply for results (these pages show no results for them)?
- How often do wrong reasoning paths give right answers on multiple-choice commonsense tasks?

## Reading notes
- This unit is part 2 of 2. It starts at Appendix C (printed p. 24) and ends at Table 30 in Appendix H (p. 43). Printed = pdf page number; offset 0.
- Appendices A and B (FAQ, raw results) and the main text fall in the other part. Tables 2 and 7 and Figure 3 are cited here but not shown.
- Table 9's caption says "7 salient cases" and "other 43", but the text and the table show 6 imperfect chains (1 chance + 5 minor) and 44 others.
- Table 24, fox example: the chain says "natural habitat" (option c), but the printed answer is "(b)". Table 23's first question begins "Q: Q:" (a duplicate).
- Table 27 prints the question as "Jamel Murray" and the answer as "Jamal Murray". Table 29 contains a double space in the second answer.
- Text of the C.4 passage on Recchia (2021) reads "module operations" and "performers"; the wording is odd in the source, so it is reproduced here as printed.
- E.1 refers to "Table 20–Table 27" for the prompts. The prompts in Appendix G run through Table 28.
- Table 17's incorrect palindrome example gives ground truth "02/03/2020", as printed.
- The printed prompts in Tables 20–28 have 4 to 8 exemplars each, while p. 28 describes the main experiments as using 8.

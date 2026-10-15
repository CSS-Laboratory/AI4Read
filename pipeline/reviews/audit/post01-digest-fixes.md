# Post 01 fact-check → digest, source-brief and KG fixes (2026-10-15)

Input: `posts/2026-10-llm-next-word/review/verify.md` (C1, M1–M9, minor 1–24 and its Resolution).
For each finding I searched the relevant digest(s) in all sections (L0–L3, toy example, Concepts,
Instances, Bridges, Reading notes) and the source brief, then re-checked every fix at the source page
(staged library under `/mnt/user-data/uploads/AI4Read/library/`; Shannon 1951 pp. 56–57 checked on the
page image, the rest with `pdftotext` or the HTML). Digests changed got `post_fixes: N` and
`post_fixed: 2026-10-15` in the frontmatter. For cover-2006-elements/ch02-entropy both the `.md` and the
`.pipeline.md` (read by `build_kg.py`) were checked.

## 1. Digest changes (5 digests)

| # | finding | file | section | old → new | source |
|---|---|---|---|---|---|
| D1 | minor 7 | `wiki/works/kosinski-2024-llm-tom/main.md` | L2, L3, Concepts (13 refs); L3 heading; Reading notes | `(§ "Introduction")` → `(§ "Abstract")` (all 13); heading `### Significance, Abstract, Introduction` → `### Significance, Abstract (with the untitled opening text)`; reading note "The opening text before the first heading is cited as "Introduction", but it has no heading in the source." → "The source has no "Introduction" heading: the untitled opening text follows the Abstract under the same heading, so both are cited as § "Abstract". The popcorn example and its prompts are in § "Study 1.1"." | HTML heading list: Significance, Abstract, then Study 1.1 …; the by-product hypothesis, 8-scenario rule, 11 models, Aug 2021 / Feb 2023 dates and the Turing remark all sit under "Abstract" |
| D2 | minor 1 (risky wording) | `wiki/works/shannon-1951-prediction/main.md` | Canonical instances | `[[shannon-guessing-game]] (new) — human next-letter prediction, 69% first-guess success on 129 letters (p. 55)` → `… — human next-letter prediction: 89 of 129 letters (69%) right in the single-guess version (Experiment 1, p. 55); 79 of 102 right at the first guess in the guess-until-right version (Experiment 2, p. 56)` | pp. 55, 56 (page image p. 56: "Out of 102 symbols the subject guessed right on the first guess 79 times") |
| D3 | minor 2 | `wiki/works/shannon-1948-mathematical/main-p1.md` | L3 §10 | `**Example 1.** Letters A, B, C, D` → `**A simple example** (Shannon's words; the examples here are not numbered). Letters A, B, C, D`; `**Example 2.** A's with probability` → `**A second example.** A's with probability` | p. 18 "As a simple example of some of these results …"; p. 19 "As a second example …" |
| D4 | minor 13 | `wiki/works/xie-2022-icl/main.md` | Concepts | `[[example-order-sensitivity]] — 10–40% accuracy spread across permutations of 4 examples (p. 10)` → `… — in GINC (synthetic data, 4-layer Transformer), 10–40% accuracy spread across permutations of 4 examples, similar to GPT-3 per Zhao et al. (p. 10)` | p. 10: "the 4 layer Transformer trained on GINC … Similarly to the behavior of GPT-3 (Zhao et al., 2021) … (10–40% difference)" |
| D5 | minor 18 | `wiki/works/mahowald-2024-dissociating/main.md` | L2 bullet 2; Concepts | `… non-language-specific cognition (p. 3).` → `(pp. 2–3).`; `[[formal-vs-functional-competence]] … (p. 3)` → `(pp. 2–3)` | arXiv v3 p. 2: "formal linguistic competence—the knowledge of rules and statistical regularities of language—and functional linguistic competence—the ability to use language in real-world situations"; longer definition p. 3 |

None of the changed text is quoted on a curated hub page (checked), so no hub edit was needed.

## 2. Findings checked in the digests and found correct there (post-only or brief-only)

| finding | digest(s) checked | result |
|---|---|---|
| C1 Bengio 321 vs 312, mixed MLP10 | bengio-2003-nplm/main | Digest correct: table lists KN 321 and best class-based 312, MLP10 "(same, mixed)", caption's 24% vs class-based (p. 1149), AP Table 2 p. 1150. Brief needed a fix (B6). |
| M1 Cover "minimum number of questions" | cover ch02 `.md` and `.pipeline.md` | Both say 1.75 is the minimum *for the example* and that Ch. 5 puts the minimum between H and H+1 (p. 15). Brief fixed (B5, B31). |
| M2/M3 Kaplan "must break down near L*" | kaplan-2020-scaling/main | Digest says "at or before" (p. 17) and marks the entropy reading as the authors' speculative conjecture (p. 18); "trends must eventually level off … non-zero entropy" is verbatim p. 17. Brief fixed (B14, B29). |
| M4 Shannon Table I columns | shannon-1951-prediction/main | Digest defines column N = known letters + 1 and says columns 1–2 were calculated from frequencies (pp. 57–58). Brief fixed (B3). |
| M5 Bengio softmax page | bengio-2003-nplm/main | Digest puts softmax under "(pp. 1142–1143)" and cites eq. 1 / W on p. 1143, softmax concept p. 1142: correct. Brief fixed (B7). |
| M6 Kosinski failures | kosinski-2024-llm-tom/main | Digest: "failures do not prove inability" (Kosinski's own wording, § Discussion) with the swan analogy; no "prove nothing". Brief fixed (B23, B28). |
| M7 Mikolov 2013b not staged | mikolov-2013-regularities/main | Resolved by the quality lead; digest pages (748 test set, 749 Table 2) agree. Brief page sharpened (B10). |
| M8 Alice/Bob output | brown-2020-gpt3/main-p1 | Digest says "The format is …" (p. 12): correct. Brief fixed (B13). |
| M9 Ullman multiplication subject | ullman-2023-trivial-alterations/main | Digest says "a machine" (p. 2): correct. Brief fixed (B25). |
| minor 3 Bengio zeros | bengio-2003-nplm/main | Digest says back-off avoids zero (p. 1138): correct. Brief toy T2 fixed (B32). |
| minor 4 GPT-2 TL;DR | radford-2019-gpt2/main | Digest: "adds `TL;DR:` … generates 100 tokens with top-k random sampling, k = 2 … first 3 generated sentences" (pdf 6): correct. Brief fixed (B12). |
| minor 5 Kaplan test vs training loss | kaplan-2020-scaling/main | Digest L1 "cross-entropy test loss"; eq. 1.1 "trained to convergence, large data": correct. Brief fixed (B15). |
| minor 6 Bender & Koller splice | bender-2020-octopus/main | Digest keeps the two sentences apart (§9 "probably" learned something about meaning; §10 "some reflection of meaning into the linguistic form", p. 5193). Brief fixed (B18). |
| minor 8 Strachan headings | strachan-2024-llm-humans/main | Digest cites § "Irony", "Hinting", "Strange stories", "Faux Pas": correct. Brief fixed (B26, B27). |
| minor 9 Ullman transparent bag | ullman-2023-trivial-alterations/main | Digest gives both prompts (95%; 58/36%, p. 3). Brief already noted it. |
| minor 10 Jefferson page | shannon-1951-prediction/main | Digest pp. 56–57: correct. Brief fixed (B4). |
| minor 11 bits-per-letter conversion | shannon-1951, kaplan | Our own conversion, only in the brief/post. Brief fixed (B30). |
| minor 12 "one third" | mikolov-2013-efficient, -regularities | Digests give 65.6 and 39.6: correct. Brief clarified (B9). |
| minor 14 Xie "proportional to", r_n < 0 | xie-2022-icl/main | Digest gives eq. 6 exactly and says r_n → negative constant "under distinguishability": correct. Brief marked (B17). |
| minor 15 Bengio hedge | bengio-2003-nplm/main | Digest "expected to get nearby vectors": correct (audio-only error). |
| minor 16 F₀ as measured | shannon-1951-prediction/main | Digest "F_0 = log2 26 = 4.7 by definition", tables "calculated": correct (audio-only). |
| minor 17 Vaswani mask | vaswani-2017-transformer/main | Digest: decoder mask "to keep the auto-regressive property": correct. Brief clarified (B11). |
| minor 19 Mahowald version | mahowald-2024-dissociating/main | Reading notes already say pages are arXiv v3. Brief header fixed (B19). |
| minor 23 "Shannon measured F_N" | shannon-1951-prediction/main | Digest "Table-based values", "calculated": correct. |
| minor 20, 21, 22, 24 | — | Post-only (notebook code, exercise denominator, glossing, prediction wording). |

## 3. Source-brief changes (`posts/2026-10-llm-next-word/source-brief.md`)

31 substantive edits (B8 is the punctuation half of B7). Frontmatter gained `post_fixes: 31`, `post_fixed: 2026-10-15`.

| # | finding | section | old | new | source |
|---|---|---|---|---|---|
| B1 | minor 2 | §1 Shannon 1948, Numbers | Example 1: $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)\Rightarrow H=\tfrac74$ bits, code 0/10/110/111 (p. 18). | Worked example (unnumbered; Shannon: "a simple example"): $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)\Rightarrow H=\tfrac74$ bits, code 0/10/110/111 (p. 18). | Shannon 1948 p. 18 |
| B2 | minor 1 | §2 Shannon 1951, Numbers | Exp. 1: 89/129 (69%) right first time (p. 55); Exp. 2: 79/102 (p. 56). | Exp. 1 (single guess, told the letter if wrong): 89/129 (69%) right (p. 55); Exp. 2 (guess until right): 79/102 (77%) right at the first guess (p. 56). Do not mix the two. | Shannon 1951 pp. 55–56 |
| B3 | M4 | §2 Shannon 1951, Numbers (Table I) | First-guess %, N = 1…15, 100: 18.2, 29.2, 36, 47, 51, 58, 48, 66, 66, 67, 62, 58, 66, 72, 60, 80 (p. 57). | Table I first-guess row (per 100), columns $N$ = 1…15, 100: 18.2, 29.2, 36, 47, 51, 58, 48, 66, 66, 67, 62, 58, 66, 72, 60, 80 (p. 57). Column $N$ means $N-1$ letters known (column 1 = no letters known); the last test had 100 letters known. Columns 1–2 were computed from letter and digram frequency tables, not from the subject's guesses (p. 57). | Shannon 1951 p. 57 (page image) |
| B4 | minor 10 | §2 Shannon 1951, Careful | from human guessers on one book (*Jefferson the Virginian*, p. 56) | from human guessers on one book (*Jefferson the Virginian*, named on p. 57; experiment described pp. 56–57) | Shannon 1951 p. 57 |
| B5 | M1 | §3 Cover & Thomas, Numbers | 7/4 bits = 1.75 yes/no questions (p. 15). | 7/4 bits (p. 14) = 1.75 yes/no questions for this source (p. 15). In general the minimum expected number of binary questions lies between $H$ and $H+1$ (p. 15); it equals $H$ here only because the probabilities are powers of ½. | Cover & Thomas pp. 14–15 |
| B6 | C1 | §4 Bengio, Numbers | Brown: MLP10 252, KN 321, class-based 312; AP: 109 vs KN 117 (pp. 1149–1150). | Brown test perplexity: MLP10 (mixed 0.5/0.5 with an interpolated trigram) 252; best n-gram = class-based back-off, 500 classes, 312 (gives the caption's 24%); best word-level Kneser–Ney 321 (Table 1, p. 1149). AP: MLP10 (mixed) 109 vs KN 117 (Table 2, p. 1150). | Bengio Table 1 p. 1149, Table 2 p. 1150 |
| B7 | M5 | §4 Bengio, equations | \ \ y=b+Wx+U\tanh(d+Hx)\ (\text{p. 1143})$$ | \ (\text{p. 1142}),\ \ y=b+Wx+U\tanh(d+Hx)\ (\text{eq. 1, p. 1143})$$ | Bengio pp. 1142–1143 |
| B8 | M5 (check) | §4 Bengio, equations | \hat P(w_t\mid\cdot)=\frac{e^{y_{w_t}}}{\sum_ie^{y_i}}, | \hat P(w_t\mid\cdot)=\frac{e^{y_{w_t}}}{\sum_ie^{y_i}} | (punctuation only, to fit the split citation) |
| B9 | minor 12 | §5 Mikolov 2013a, Careful | Best totals are about two thirds. | Best totals are about two thirds (65.6%); with 2013b's 39.6% the range is about 40–66%, not "one third". | Mikolov 2013a p. 9; 2013b p. 749 |
| B10 | M7 / resolution | §6 Mikolov 2013b, Claims | - RNN-1600: 39.6% of 8,000 syntactic questions vs best LSA 16.5% (p. 749). | - RNN-1600: 39.6% of 8,000 syntactic questions vs best LSA 16.5% (test set p. 748; Table 2 p. 749). | Mikolov 2013b pp. 748–749 (verify.md Resolution) |
| B11 | minor 17 | §8 Vaswani, Claims | - Masking ($-\infty$ before softmax) makes position $i$ depend only on positions $<i$ (pp. 3, 5). | - Masking ($-\infty$ before softmax) in the translation *decoder* makes position $i$ depend only on positions $<i$, "to preserve the auto-regressive property" (pp. 3, 5). | Vaswani p. 5 |
| B12 | minor 4 | §9 GPT-2, Instance | **Instance.** "TL;DR:" turns prediction into summarization (pdf 6). | **Instance.** Adding "TL;DR:" after an article and generating 100 tokens with top-$k$ sampling ($k=2$) induces summary-like text; the first 3 sentences are taken as the summary (pdf 6). The model *tends to* continue with a summary; it is not "the most likely continuation". | GPT-2 pdf 6 |
| B13 | M8 | §10 GPT-3, Instance | **Instance.** "Alice was friends with Bob. Alice went to visit her friend ____. → Bob" (p. 12). | **Instance.** "Alice was friends with Bob. Alice went to visit her friend ____. → Bob" (p. 12): the fill-in-the-blank *format* shown to the model, with its answer; not a reported model output. | Brown p. 12 |
| B14 | M2/M3 | §11 Kaplan, Claims | - *Conjecture:* the laws must break near $N^*\sim10^{12}$, $L^*\sim1.7$ nats/token, which *might* estimate entropy per token; uncertain by an order of magnitude (pp. 17–18). | - Trends must flatten out eventually before zero loss (p. 3), since language has non-zero entropy (p. 17). Extrapolated $L(D(C_{\min}))$ and $L(C_{\min})$ contradict each other near $N^*\sim10^{12}$, $L^*\sim1.7$ nats/token; the "most obvious interpretation" is that the laws break down *at or before* this point; numbers uncertain by an order of magnitude (p. 17). *Further conjecture:* $L^*$ *might* give a rough estimate of the entropy per token (p. 18). | Kaplan pp. 3, 17–18 |
| B15 | minor 5 | §11 Kaplan, Careful | **Careful!** Fits of *loss* on WebText2, not ability. | **Careful!** Fits of *test* loss on WebText2 (p. 6), not ability; $L(N)$ is for models trained to convergence on large data (p. 4). Not "training loss". | Kaplan pp. 4, 6 |
| B16 | minor 13 | §12 Xie, Claims | Order shifts accuracy 10–40%; zero-shot can beat few-shot (pp. 10–11). | In GINC (4-layer Transformer, synthetic data) order shifts accuracy 10–40%, similar to GPT-3 per Zhao et al.; zero-shot can beat few-shot (pp. 10–11). | Xie p. 10 |
| B17 | minor 14 | §12 Xie, equations | \quad \text{weight}(\theta)\propto e^{n\,r_n(\theta)}p(\theta), | \quad \text{weight}(\theta)\propto e^{n\,r_n(\theta)}p(\theta)\ \text{(proportional to, not grows like)}, | Xie p. 6 |
| B18 | minor 6 | §13 Bender & Koller, Claims | - BERT has "probably" learned "some reflection of meaning", useful but incomplete (p. 5193). | - BERT has "probably learned something about meaning" (§9); LMs learn "some reflection of meaning into the linguistic form" (§10); useful but incomplete (both p. 5193). Two separate sentences: do not splice. | Bender & Koller p. 5193 |
| B19 | minor 19 | §15 Mahowald, heading | ### 15. Mahowald et al. (2024), *Dissociating language and thought* (pp. 1–18) | ### 15. Mahowald et al. (2024), *Dissociating language and thought* (pp. 1–18 of arXiv:2301.06627v3, "A PREPRINT"; not the *TiCS* typeset pages) | Mahowald pdf p. 1 |
| B20 | minor 18 | §15 Mahowald, Claims | - Formal competence = rules and statistical regularities; functional = using language in the world (p. 3). | - Formal competence = rules and statistical regularities; functional = using language in the world (short definitions p. 2; longer p. 3). | Mahowald pp. 2–3 |
| B21 | minor 7 | §16 Kosinski, Claims | - ToM *may* emerge as a by-product of training (§ "Introduction"). | - ToM *may* emerge as a by-product of training (§ "Abstract"; the source has no "Introduction" heading). | Kosinski HTML heading list |
| B22 | minor 7 | §16 Kosinski, Claims | all 16 correct (§ "Introduction", § "Study 3"). | all 16 correct (§ "Abstract", § "Study 3"). | Kosinski § Abstract |
| B23 | M6 | §16 Kosinski, Claims | - Failures do not prove inability; successes do not prove ToM (§ "Discussion"). | - Failures do not *necessarily* indicate inability ("do not prove their inability"); successes do not prove ToM; failures can still give "valuable insights" (§ "Discussion"). | Kosinski § Discussion |
| B24 | minor 7 | §16 Kosinski, Instance | revealed sentence by sentence (§ "Study 1"). | revealed sentence by sentence (§ "Study 1.1", § "Study 1.4"). | Kosinski § Study 1.1, 1.4 |
| B25 | M9 | §17 Ullman, Claims | - One failure outweighs averages: 213×261 after 100 easy products (p. 2). | - One failure outweighs averages: a *machine* that answers 100 easy products but fails 213×261 has probably not learned a general multiplication algorithm (p. 2). | Ullman p. 2 |
| B26 | minor 8 | §18 Strachan, Claims | - GPT-4 above humans on irony, hinting, strange stories; below on faux pas (§ results). | - GPT-4 above humans on irony, hinting, strange stories; below on faux pas (§ "Irony", § "Hinting", § "Strange stories", § "Faux Pas", under "Performance across theory of mind tests"). | Strachan HTML headings |
| B27 | minor 8 | §18 Strachan, Numbers | faux pas P = 5.42×10⁻⁵, r = 0.55 (§ results) | faux pas P = 5.42×10⁻⁵, r = 0.55 (§ "Irony", § "Faux Pas") | Strachan § Irony, § Faux Pas |
| B28 | M6 | Cross-source tension 3 | vs failures prove nothing (Kosinski § "Discussion") | vs a failure does not *necessarily* show inability (Kosinski § "Discussion") | Kosinski § Discussion |
| B29 | M2/M3 | Cross-source tension 6 | vs Kaplan $L^*\approx1.7$ nats/token, a conjecture (pp. 17–18). | vs Kaplan $L^*\approx1.7$ nats/token, where two trends contradict (laws break down at or before it, p. 17); reading it as entropy is a further conjecture (p. 18). | Kaplan pp. 17–18 |
| B30 | minor 11 | Cross-source tension 6 | ≈ 0.78 bits/letter. Different corpora and tokenizers: a talking point only. | ≈ 0.78 bits/letter. This mixes alphabets (Shannon's ~1 bit is for 27 symbols with space; 4.5 letters/word excludes spaces). Kaplan's own fn. 7 (4.3 characters per token on WebText2) gives 2.45/4.3 ≈ 0.57 bits/character (p. 18). Different corpora and tokenizers: a talking point only. | Kaplan p. 18 fn. 7; Shannon p. 53 |
| B31 | M1 | Toy T1 | **T1. 4-word language.** True $p=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ (Cover p. 15). | **T1. 4-word language.** True $p=(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ (Cover pp. 14–15). | Cover pp. 14–15 |
| B32 | minor 3 | Toy T2 | The zero cells show Bengio's unseen-pair problem (p. 1138). | The zero cells are true zeros in this language. In real text many possible sequences are merely unseen; n-grams avoid zero by back-off/smoothing (p. 1138), and Bengio's vectors target generalization through word similarity (p. 1139). | Bengio pp. 1138–1139 |

## 4. Knowledge graph (same date)

`scripts/build_kg.py` now skips `wiki/works/<work>/index.md` work maps; record-level splits of
`value-function`, `priming`, `paradox-of-voting`, `stereotype` (`wiki/kg/splits.json`); Kelly work-id alias
(`wiki/kg/work-aliases.json`); ML / deep learning → `llm` kept and recorded. Details, before/after counts and
the hub verification (299/299 quotes, 196/196 page refs) are in `wiki/kg/PHASE2.md` ("Update 2026-10-15").

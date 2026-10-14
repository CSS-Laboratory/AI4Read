---
id: piantadosi-2022-meaning/main
work: piantadosi-2022-meaning
unit: paper
pages: pdf 1–8 (printed page numbers not visible)
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Meaning without reference in large language models

## L0 — One line
Text-only language models likely capture important aspects of meaning, because meaning plausibly comes from how concepts relate to each other (conceptual role), rather than from reference to the world alone.

## L1 — The gist (≤ 120 words)
Critics (Bender & Koller) argue that large language models (LLMs) trained on text alone cannot have meaning, because they lack reference to real objects. Piantadosi & Hill reply that this assumes reference determines meaning, which cognitive science and philosophy have found problematic. On conceptual role theory, meaning comes from relations among internal states. Text carries clues to those relations, so prediction training might discover them, which the authors call an empirical question. They cite empirical successes and analogies (embedding theorems, AlphaFold) as support. They do not claim LLMs match human meaning perfectly. They treat reference as one optional part of conceptual role, and they think LLMs likely already share the foundation of human meaning.

**Prerequisites:** the idea of next-word prediction; basic logic (TRUE/FALSE, AND); a loose notion of "vector geometry" of representations.

## L2 — Key ideas (5–10 bullets)
- **Target:** the claim that LLMs "necessarily" cannot acquire meaning, because they lack reference (Bender & Koller's "octopus test": an octopus that only eavesdrops on conversation) (pdf 1).
- **Reference does not fix meaning:** abstract, non-existent and impossible concepts are meaningful, and even "postage stamp" is not tied to its possible referents (pdf 2).
- **Conceptual role theory:** on this view, a concept's meaning comes mainly from its relations to other concepts, as in f = m·a. Having the right relations allows you to determine reference (pdf 2).
- **Consequence for evaluation:** if conceptual role theory is right, meaning cannot be read off an LLM's architecture, training data or objective, but only found by examining how its internal states relate (pdf 1, 3).
- **Evidence offered:** human-like relational geometry that improves with scale, brain-data fits, and success on tasks that need conceptual relations. Limits are acknowledged, e.g. multimodal models fit human judgements better (pdf 3).
- **Why text may carry enough clues:** human conceptual roles generated the text. Embedding theorems (results on recovering a system's geometry from a one-dimensional projection) and AlphaFold (a protein-structure network) are offered as analogies suggesting latent structure can sometimes be inferred from limited views. The authors call this plausible and the question empirical (pdf 4–5).
- **Intentions:** critics call LLMs "stochastic parrots" (auto-complete without intentions). The authors see a key difference: LLMs have rich, causal, structured internal states, and they consider some implicit planning probable (pdf 5).
- **Scope:** reference is one optional aspect of conceptual role, and richer input (agency, a perceptual environment) may lead to richer, more human-like understanding (pdf 4).

## L3 — Walkthrough
The paper has no numbered sections. I follow its bold run-in headings.

**Introduction (pdf 1).** The authors aim to contest claims that LLMs are *necessarily* incapable of meaning. They suggest LLM meanings may already be similar to human meaning "in many (but not all) ways." LLMs are trained to predict words from context on massive text. This differs from human acquisition in data scale and format. Word prediction is nonetheless a central part of human language processing and can provide a learning signal from which structure and semantic categories emerge (Elman 1990).
- **Bender & Koller's view:** an octopus eavesdrops on two people's conversation and learns to use words correctly. If it must find a coconut, its skill with "coconut" does not help. Co-occurrence statistics do not help either, because it knows nothing about the referents of the other words. On this view, no amount of predictive savvy gives text-only models knowledge of reference (pdf 1).

**Meaning and reference (pdf 1–2).** The authors say the octopus test *assumes* that reference determines meaning, and that this view has problems.
- Meaningful terms with no discernible referent: "justice", "wit". Terms with no referent: "aphid-sized accordion", "king of San Francisco". Terms with no possible referent: "perpetual motion machine". We can still reason about these, e.g. a King of San Francisco would live in the Presidio (pdf 2).
- Reference decouples from meaning. A treaty is still valid if the paper is destroyed. Frege's "morning star" and "evening star" both name Venus but were once conceived as different entities (pdf 2).
- Many concrete terms also seem not to get their key semantic properties from reference: no physical feature of a typical postage stamp seems necessary (glass, microscopic, online, RFID, pheromone stamps). We cannot have considered every possible referent, so reference cannot be what determines the concept (pdf 2).
- Wittgenstein argued similarly about "water", concluding that reference plays little or no role in the general case (pdf 2).
- **Proposed explanation:** the meaning of "postage stamp" is mainly its role in a larger mental theory, tied to "payment", "letter", "delivery". If "payment" changes (credit cards), the meaning of "stamp" comes along. On this view such relations are the essential, defining aspects of meaning. Having them also lets you determine the reference (pdf 2).

*Intuition note:* You can use and understand a word without ever having seen all the things it could apply to. One explanation the authors offer is that what you know is mainly how the idea connects to other ideas.

**Conceptual role theory (pdf 2–3).**
- Following Block (1998): f = m·a is not exactly a definition of f (force), m (mass) or a (acceleration), but a statement about how they interrelate. Most people say little about the ultimate physical reference of force or mass, yet their thoughts about the equation are not meaningless (pdf 2).
- Murphy & Medin (1985) argue that categories rest on theories of structured domains, not simple features. "Prime numbers or apples" seems incoherent. "Topics of conversation with Wilma" (a number theorist raised on an apple farm) seems fine. What is natural depends on how we conceive the pieces to relate (pdf 2).
- Concepts can be assembled ad hoc and context-dependently (Barsalou; Casasanto & Lupyan). Theory-based accounts have been explored in learning models and in children's exploration (pdf 2–3).
- The authors note that many believe conceptual roles are among the most promising ways to characterize human concepts in general. In philosophy of mind, versions of this approach are called "conceptual role theory" (pdf 2).

**Conceptual role in LLMs (pdf 3–4).** If this view is right, one should study how a system's internal states relate to each other. Once a model finds it probable that stamps are affixed to letters to be delivered, it has acquired some conceptual role for these terms. On this view, training data or architecture alone cannot tell us what meanings a system has, since they may not be informative about those relations (pdf 3).
- Evidence listed by the authors (pdf 3):
  - Word-vector geometry in analogy tasks and in match to human similarity; graded scales such as small–big (Grand et al.).
  - Unsupervised alignment across languages for translation.
  - Text-only models recovering key colour-space geometry; with a few grounded examples they align with the grounded structure (Abdou et al.), suggesting that they already possess the right relations (the authors cite Patel & Pavlick here).
  - Human-likeness of the geometry has increased as models improved. Larger models show more human-like content effects in reasoning.
  - fMRI studies find that the semantic models best accounting for human brain data are LLMs trained on the most data.
  - Success on narrative, factual QA, Winograd schemas, quantitative reasoning, and estimating whether they can answer correctly. Each of these requires, in some way, sensitivity to conceptual roles (pdf 3).
- **Limits (pdf 3–4):** Lake & Murphy stress needs for reference, inference, robust compositionality and abstract reasoning. Multimodal models match human judgements better than text-only ones, yet still lack many aspects of semantics (e.g. simulating effects on their environment, knowing goals and desires).
- **Scope of the claim (pdf 4):** LLMs do not perfectly capture human concepts. Unlike Wittgenstein or Quine, the authors do not say reference should play no role. They treat it as one *optional* aspect of conceptual role, relevant for some concepts (Putnam) and not others.
- **Progressive enrichment:** learning that water is H₂O enriched the concept and even revised its reference. There was no hard switch from meaningless to meaningful, since "water" had a conceptual role beforehand. Likewise, they see no reason to call the world of a single-modality system meaningless, though extra sensors would enrich it (pdf 4).

*Intuition note:* Meaning comes in degrees. A system can have part of a concept's web of relations and gain more later. Missing one part, such as appearance, does not mean having nothing.

**Discovering conceptual role (pdf 4–5).**
- A symbol like AND means logical conjunction only if it composes appropriately with symbols like TRUE and FALSE, i.e. has the right conceptual role (pdf 4).
- **Church-encoding:** a representation is built in one system (lambda calculus, a neural network) to mimic another system (boolean logic), so that representations interact to give the desired roles. Piantadosi (2021) shows how such a learner could acquire logic, lists, trees, hierarchies, numbers, quantifiers and recursion without having them at the start. Networks would tune parameters so their internal dynamics church-encode a domain's roles (pdf 4).
- **Key question:** can predicting text support discovery of conceptual roles? The authors call it empirical and believe task successes give a "promising, partial affirmative" (pdf 4).
- **Why text can carry the clues:** human conceptual roles generated the text. Analogy: gravity generated the moon's movements, so a gravity theory can be built from them. Inductive learning generally inverts from observations to generating processes. Entailment relations among sentences are often related to patterns in thought, so a model that captures how sentences relate might capture how thoughts relate (pdf 4).
- **Embedding theorems:** Packard et al. (1980) show one can sometimes reconstruct a multi-dimensional system's geometry from a one-dimensional projection of its state. People use concepts based on their meaning, and text is a low-dimensional projection of some of these patterns of use, so the authors say it is plausible that some properties of the real meaning could be inferred. At the least, embedding theorems illustrate that there may be no simple way to intuit what a learner can or cannot deduce about the underlying mental states from text alone (pdf 5).
- **AlphaFold:** trained on single proteins only, it often perfectly infers a zinc ion's location (never seen as such) and often infers the number and placement of copies for homomers. This suggests single-protein prediction let it infer non-trivial facts about chemistry and biology (pdf 5).

*Intuition note:* A thin trace of a rich process can sometimes still contain the process's structure. The authors suggest text may be such a trace of human thought. They offer this as plausibility, not proof.

**Communicative intentions (pdf 5).**
- **Critics' view (Bender et al.):** LLMs, because they are trained only on sequence prediction, are argued to be "stochastic parrots" or sophisticated auto-complete. They cannot access the intentions of the people who wrote their data, and themselves produce language without intending anything in particular (pdf 5).
- **Authors' reply:** the key difference is that LLMs have rich, causal, structured internal states (pdf 5).
  - *Semantic intent:* language arising from an internal representation of intended meaning. Converting internal states to language is the essential function of LLMs. The authors argue that LLM internal states have some notions of conceptual role, so LLM utterances have the semantic intent corresponding to these roles.
  - *Pragmatic intent:* goal-directed planning. The authors "consider it probable" that multi-layer LLMs implicitly plan through repeated self-attention. They cite work on belief-like structures (Hase et al.) and updated representations of situations (Li et al.). These states causally determine output.
  - *Caveat:* LLM planning is less explicit and sophisticated than human planning, e.g. more error-prone in counterfactual reasoning.

**Conclusion (pdf 5).** Bender & Koller *assume* rather than demonstrate that reference is key to meaning. This is hard to reconcile with cognitive theories, since people think about referentless concepts and often lack detail on reference. Meaning instead seems to come from relations among concepts, and LLMs know something about these because their internal geometries and trajectories approximate humans'. The octopus lacks some conceptual role (e.g. physical appearance), as people who don't know water is H₂O lack its chemical role. Both the octopus and people know other parts of conceptual role that are sophisticated in their own right. If conceptual role theories are correct, LLMs likely already share the foundation of how our concepts get meaning.

## Toy example
*(Ours, not from the text.)* Church-encode TRUE and FALSE as two-argument functions that pick an argument: TRUE(a,b) = a and FALSE(a,b) = b. Define AND(p,q) = p(q,p).
- AND(TRUE,TRUE) = TRUE(TRUE,TRUE) = first argument = TRUE.
- AND(TRUE,FALSE) = TRUE(FALSE,TRUE) = first argument = FALSE.
- AND(FALSE,TRUE) = FALSE(TRUE,FALSE) = second argument = FALSE.
- AND(FALSE,FALSE) = FALSE(FALSE,FALSE) = second argument = FALSE.

The result is the AND truth table. The functions have no "referent" outside the system. They play the roles of TRUE, FALSE and AND because of how they interact. This is the sense of "conceptual role" in pdf 4.

## Concepts
- [[conceptual-role-semantics]] — meaning comes from a representation's relations to other representations; reference is one optional aspect (pdf 2, 4)
- [[symbol-grounding]] — the "reference" problem the critics raise: connecting symbols to real-world objects (pdf 1)
- [[form-vs-meaning]] — the worry (Bender & Koller) that models trained only on text cannot acquire realistic meanings because they lack reference (pdf 1)
- [[language-model]] — here, a system trained to predict words from surrounding context (pdf 1)
- [[self-attention]] — mentioned as the repeated analysis of current and past inputs, which may support implicit planning (pdf 5)
- [[church-encoding]] (new) — building representations in one system whose interactions mimic another system's roles (pdf 4)
- [[embedding-theorem]] (new) — results showing a system's geometry can sometimes be recovered from a low-dimensional projection (pdf 4–5)
- [[communicative-intention]] (new) — semantic intent (language from an intended-meaning representation) or pragmatic intent (goal-directed planning) (pdf 5)
- [[stochastic-parrot]] (new) — the critics' label for LLMs as auto-complete without intentions (pdf 5)

## Canonical instances
- [[octopus-test]] — Bender & Koller's thought experiment against meaning without reference (pdf 1)
- [[postage-stamp-argument]] — no physical feature of typical stamps seems necessary, so reference cannot be what determines the concept (pdf 2)
- [[force-equals-mass-times-acceleration]] — an equation as an example of conceptual role (pdf 2)
- [[morning-star-evening-star]] — Frege's case separating reference from meaning (pdf 2)
- [[wilma-category]] — "topics of conversation with Wilma" as an ad hoc coherent category (pdf 2)
- [[water-h2o]] — meaning enriched gradually, not switched on (pdf 4)
- [[alphafold-latent-inference]] — a transformer inferring unseen structure (zinc ions, homomers) (pdf 5)

## Bridges (candidates)
- [structural-analogy] Text as a low-dimensional projection of thought ↔ dynamical systems: Packard/Takens delay-embedding reconstruction — both recover hidden structure from a limited view; the paper itself says "analogy".
- [structural-analogy] Church-encoded conceptual roles ↔ lambda calculus/logic: functions mimic boolean behaviour through interaction.
- [metaphor] Octopus eavesdropping ↔ language-only training: the thought experiment illustrates the grounding worry.
- [structural-analogy] Inferring conceptual roles from text ↔ inductive inference of gravity from the moon's motion: inverting observations to generating processes.

## Questions this raises
- What concrete test would show that a model's internal states have the "right" relations, beyond task success and similarity to human data?
- If larger models fit human brains better, does that show shared conceptual role, or only shared predictive statistics?
- Which concepts depend heavily on reference (the paper cites Putnam for some), and can text-only models handle them?
- How could implicit planning in LLMs be measured, separately from fluent continuation?

## Reading notes
- Printed page numbers are not visible, so citations use pdf numbers. The unit is pdf 1–8, with pdf 6–8 holding acknowledgements and references. arXiv:2208.02957v2, 12 Aug 2022. The authors call it a "short comment" (pdf 1).
- The only formula is the inline equation f = m·a (pdf 2). There are no derivations.
- Typos in the source: "it we should therefore consider" (pdf 4); "LLMs posses" (pdf 5); "have the letter to be delivered" (pdf 2); "as wholly new a form" (pdf 2).
- Footnote 1 (pdf 5) gives a URL for the "auto-complete" claim; the linked page is not part of this source.

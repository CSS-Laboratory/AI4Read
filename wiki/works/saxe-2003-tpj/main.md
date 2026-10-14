---
id: saxe-2003-tpj/main
work: saxe-2003-tpj
unit: paper
pages: 1835–1842 (printed 1–8 in the supplied PDF)
fields: [theory-of-mind]
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
# People thinking about thinking people: the role of the temporo-parietal junction in "theory of mind"

## L0 — One line
Using fMRI with written stories, Saxe and Kanwisher find a region in the temporo-parietal junction (TPJ-M) that responds selectively to reasoning about other people's mental states, not to the mere presence of a person.

## L1 — The gist (≤ 120 words)
Does a region of the temporo-parietal junction (TPJ) respond to mental states specifically, or just to the presence of a person? In two fMRI experiments, readers saw stories about beliefs and desires and several control stories. A region called TPJ-M responded more to belief stories than to mechanical-inference and false-photograph stories, and more to desire stories than to descriptions of nonhuman objects or physical descriptions of people. It is separate from the nearby extrastriate body area (EBA), which responds to body photographs but not to stories. The authors conclude that the TPJ-M is selectively involved in reasoning about other minds. This matters because some authors had suggested the TPJ is involved only in preliminary stages that "aid" theory of mind.

**Prerequisites:** BOLD signal and percent signal change in fMRI; the idea of a control condition; false-belief tasks; paired t tests (basic idea).

## L2 — Key ideas (5–10 bullets)
- The authors separate two representations needed for theory of mind (ToM): a representation of a person per se, and a representation of that person's mental states. They argue the TPJ-M supports the second (pp. 1–2).
- Earlier studies compared false-belief stories with true-belief stories and found a high TPJ response to both. The authors say this does not show the TPJ is non-selective, since true-belief stories also invite reasoning about minds (p. 2).
- They propose two tests for a ToM-selective region. It must respond more to ToM-inviting stimuli than to logically similar non-social controls. It must also not respond merely because a person is present (p. 2).
- Experiment 1: the TPJ-M responds more to ToM stories than to mechanical-inference stories. It is distinct from the EBA, which did not respond to any stories (pp. 3–4).
- Experiment 2: the TPJ-M responds more to false-belief than to false-photograph stories, which are logically matched but not about minds. Responses to physical-description stories about people and about nonhuman objects were low and did not differ (pp. 5–6).
- Desire stories also drove the TPJ-M more than physical-people or nonhuman stories. So the response is not restricted to false beliefs (p. 6).
- The authors judge it unlikely that the effect is imagery of biological motion, citing unpublished data (p. 6).
- Neighbouring cortical subregions differ in function, so within-subject comparisons are needed (p. 6).

## L3 — Walkthrough

### Introduction (pp. 1–2)
- Regions near the TPJ have been linked to many social tasks. They also respond preferentially to faces, bodies and biological motion (p. 1).
- Several studies found higher TPJ response to stories or cartoons needing inferences about (false) beliefs than to physical controls (p. 1).
- The authors use "theory of mind" broadly: any reasoning about another person's representational mental states. They do not mean the narrower "theory-theory" claim (footnote 1, p. 1).
- ToM needs at least two representations: of another person per se, and of that person's mental states. The first is a likely prerequisite, but the second is "the core responsibility" of ToM (pp. 1–2).
- **Opposing view (Gallagher & Frith, 2003):** the TPJ is involved only in preliminary stages that "aid" ToM. The authors present evidence against this (p. 2).
- Previous work (Fletcher et al., 1995; Gallagher et al., 2000) compared false-belief stories with "non-ToM" stories about true beliefs, and with unrelated sentences. The TPJ was high in both ToM and non-ToM stories, and those authors concluded it is not selective for ToM (p. 2).
- **Authors' reply:** this "does not follow". The true-belief stories invite inferences about a character's true beliefs. A region for reasoning about minds should therefore respond to them too (p. 2).
- **Two tests** for a ToM-selective region (p. 2):
  1. Increased response to tasks that invite ToM reasoning (about true or false beliefs), compared with logically similar non-social controls.
  2. Response specifically when subjects reason about a person's mental states, not whenever a person is present.
- The new stimuli were not accompanied by any cue or instruction to attend to mental states (p. 2).

*Intuition note:* A brain region that tracks other minds should also respond when a story is about what someone truly believes. So, on the authors' argument, a high response in true-belief stories does not show that the region is non-selective. A fair comparison is with logically similar non-social stories.

### Experiment 1 (pp. 2–4)
**Design (p. 2).** Four story types:
- false belief (action caused by a false belief);
- human action (analysis of mental causes, no false belief);
- mechanical inference (MI; infer a hidden physical process, such as melting);
- nonhuman description.

The EBA, a region near posterior superior temporal cortex that prefers images of human bodies (Downing et al., 2001), was tested directly against the TPJ-M. Photographs of people and of objects were used for this.

**Methods (pp. 2–3).**
- 25 right-handed adults (12 women), scanned at 1.5 T (9) and 3.0 T (16). TR = 2 s; twenty 5-mm near-coronal slices covered occipital lobe and posterior temporal and parietal lobes (p. 2).
- Stories averaged 36 words and were shown for 9500 ms each. A scan had four 40-s epochs, each with one story per condition, plus 20-s fixations. Subjects pressed a button when finished reading. They read 8 (4 subjects) or 12 (21 subjects) stories per condition (p. 2).
- 14 of these subjects also did an EBA localizer at 3.0 T. It used 20 grayscale photographs of whole human bodies, 20 photographs of inanimate objects, and a one-back task (pp. 2–3).

**Results (p. 3).**
- Reading times did not differ: ToM 6.4 s, MI 6.5 s, P > 0.2.
- A random-effects analysis (n = 25, P < 0.05 corrected) found five loci for ToM > MI (Table 1):

| Region | MNI (max voxel) | Z | Voxels |
|---|---|---|---|
| left TPJ-M | [−54 −60 21] | 5.88 | 63 |
| left aSTS | [−57 −27 −12] | 5.40 | 55 |
| precuneus | [−9 −51 33] | 5.20 | 41 |
| right TPJ-M | [51 −54 27] | 5.10 | 10 |
| right aSTS | [66 −18 −15] | 4.91 | 2 |

  (aSTS = anterior superior temporal sulcus.)
- The precuneus was deactivated below fixation in all story conditions, and less so for ToM than MI. Its meaning was unclear, so it was not analysed further.
- In individual subjects (fixed effects, P < 0.0001 uncorrected), TPJ voxels were found in 22 of 25 subjects (bilaterally in 14, left only in 5, right only in 3). The aSTS was found in 10 of 25. The TPJ-M was the most consistent region and the focus of the prior hypothesis, so it was analysed further.
- TPJ-M ROIs were defined per subject as contiguous voxels with false belief > MI (P < 0.0001). They also responded more to human-action stories than to nonhuman descriptions. Percent signal change (PSC) from fixation, right: 0.22 vs 0.02; left: 0.35 vs 0.10; both P < 0.0001. So the response generalizes beyond false beliefs.
- EBA ROIs (bodies > objects, P < 0.0001) were found bilaterally in 13 subjects and right only in 1. They did not discriminate between any story conditions (all P > 0.4, story PSCs below 0.01; Fig. 2).
- **Photographs and the TPJ-M:**
  - Left TPJ-M: people −0.04 vs objects −0.09, P > 0.4.
  - Right TPJ-M: a trend, people 0.24 vs objects 0.10, P < 0.10.
- An ANOVA (content × modality × hemisphere) gave:
  - main effects of person > object (P < 0.001) and stories > photographs (P < 0.05);
  - a modality × hemisphere interaction (photograph response only on the right, P < 0.005);
  - a trend toward a three-way interaction (P < 0.1).

**Discussion of Exp. 1 (pp. 3–4).**
- The TPJ-M bilaterally responds more to ToM than MI stories. This replicates earlier work with new stimuli, no cue, and stricter statistics. The response extends to human actions based on true beliefs (p. 3).
- The EBA, the TPJ-M's neighbour, did not respond to any verbal condition. The TPJ-M response to nonverbal stimuli seemed lateralized: left TPJ-M selective for verbal descriptions, right TPJ-M possibly generalizing to photographs (pp. 3–4).

*Intuition note:* The "TPJ-M" and the "EBA" lie close together but behave differently. The EBA did not respond to stories, while the TPJ-M did. The EBA responded strongly to body photographs, while the TPJ-M responded weakly (only the right TPJ-M showed a trend). The authors stress that neighbouring subregions can have different functional profiles, so careful within-subject comparisons are necessary (p. 6).

### Experiment 2 (pp. 4–6)
**Rationale (p. 4).** Experiment 1 compared people-and-mental-state stories with stories having neither. Experiment 2 asks which component drives the response. The ToM stories also differed logically from controls: only false-belief stories require the notion of a false representation. The developmental solution is the "false photograph" story (Zaitchik, 1990). It requires representing the false content of a physical representation, such as a photograph or map.

**Stimuli (p. 5).** Five story types:
- false belief (FB);
- false photograph (FP);
- desires (goals or intentions; rely on ToM);
- nonhuman descriptions (plants, cars, planets);
- physical people (clothing, hair colour, facial markings).

**Prediction.** A region specific to ToM should respond equally low to nonhuman and physical-people stories, and higher to desire stories. A region for any representation of other people should respond highly to physical-people stories (p. 5).

**Methods (p. 5).**
- 21 naive right-handed subjects (11 women) at 1.5 T, 20 axial 5-mm slices, whole brain. Seven additional Exp. 1 subjects took part in part of the experiment at 3.0 T.
- Each story was followed by a 4-s two-alternative fill-in-the-blank question. For FB, FP and desire stories, 50% of questions probed mental states and 50% probed the actual outcome, to prevent formulaic responding.
- 14 subjects saw only FB and FP stories. The other 14 saw all five conditions. Fixations of 12 s separated blocks.

**Results (pp. 5–6).**
- Questions about FP stories were answered more slowly than FB (FB 2.6 s, FP 2.8 s, P < 0.01). So FB inferences were unlikely to be simply harder (p. 5).
- A whole-brain random-effects analysis of 21 subjects (FB > FP, P < 0.0001 uncorrected) found:
  - TPJ bilaterally (right (54 −51 18), left (−48 −63 33));
  - precuneus/posterior cingulate (3 −54 30);
  - right aSTS (54 −18 −15);
  - medial superior frontal gyrus (6 57 18) (p. 5).
- In the 7 subjects scanned in both experiments, the Exp. 1 TPJ-M overlapped strikingly with the FB > FP region (Fig. 3a). Voxels defined in Exp. 1 (ToM > MI) responded more to FB than FP in Exp. 2 (mean PSC 1.6 vs 0.7, P < 0.02) (p. 5).
- The authors say this reliability makes it unlikely that Exp. 1 reflected stimulus confounds or logical differences (p. 5).
- In the 14 subjects with all five conditions, ROIs combined two criteria. A voxel had to be significant (FB > FP, P < 0.0001) in at least half of the subjects. It also had to lie within 15 mm of a group-analysis peak. This gave ROIs in the TPJ-M bilaterally and the right aSTS (p. 5).
- In these ROIs, desire stories gave a significantly larger response than physical-people or nonhuman stories (both P < 0.05). The latter two did not differ from each other (Fig. 4). Left and right TPJ-M did not differ (p. 6).
- At a lower threshold (P < 0.001 uncorrected), physical people > nonhuman descriptions showed only frontal regions: dorsal medial prefrontal (−3 57 39) and right lateral frontal (39 15 54) (p. 6).

*Intuition note:* The false-photograph control stories were logically similar to the false-belief stories (and, if anything, harder) but were not about minds. The TPJ-M still did not respond to them. Describing a person's physical appearance also gave no more response than describing nonhuman objects such as planets. Among the story types tested, the TPJ-M was driven by those about mental states.

### Discussion of Exp. 2 and General discussion (p. 6)
- Right and left TPJ-M responses to physical-people stories did not differ, which the authors say resolves the ambiguity of the apparently lateralized response to photographs of bodies in Exp. 1 (p. 6).
- The TPJ-M response is robust across subjects, tasks and stimuli. It is not an effect of difficulty or of the logical structure of false-belief stories, because the harder FP stories did not drive it (p. 6).
- The TPJ-M is anatomically and functionally distinct from the EBA, suggesting at least two regions involved in social information processing (p. 6).
- **Key innovation:** the physical-people stories. Earlier "physical" stories described acting people and gave a larger TPJ response than scrambled sentences. Here, physical-people stories gave no larger a response than nonhuman descriptions, and a significantly lower response than desire stories (p. 6).
- **Imagery objection:** the authors think it unlikely that the response reflects imagery of biological motion or goal-directed action. Their unpublished data show a much lower TPJ-M response to a movie of a walking person than to FB stories. Imagery would predict the opposite. The pSTS-VA (visual analysis of action) is doubly dissociated from the TPJ-M, since it responds more to movies than to stories (p. 6).
- **Conclusion:** a region of the TPJ is involved in reasoning about other minds, not just in understanding stories with people per se. Neighbouring subregions have different profiles, so careful within-subject comparisons are needed (p. 6).
- The TPJ-M "may play a broad role in social and even moral cognition" (pp. 6–7).
- **Footnote 2 (attention):** selective attention increases TPJ activity in social perception tasks and decreases it in visual attention tasks. One possibility is that others' mental states are a category of "behaviourally relevant" stimuli (Downar et al., 2001). Another is that these results reflect distinct subregions. Direct testing is "an important avenue for future work" (p. 6).

### Appendix (p. 7)
Sample stories are given for the Exp. 1 ToM, MI and human-action conditions and for all five Exp. 2 conditions (the nonhuman-description sample is listed under Exp. 2). Examples are the Porsche/Ford false-belief story, and the apple-photograph FP story where the apple is blown to the ground.

## Toy example (ours, not from the paper)
Two imaginary regions A and B give these percent signal changes:

| Condition | Region A | Region B |
|---|---|---|
| desire stories | 0.40 | 0.30 |
| mechanical-inference control | 0.10 | 0.30 |
| physical people | 0.05 | 0.35 |
| nonhuman description | 0.05 | 0.30 |

- **Test 1** (mental-state stimuli > matched non-social control): A: 0.40 − 0.10 = 0.30 → passes. B: 0.30 − 0.30 = 0.00 → fails.
- **Test 2** (person present but no mental states > nonhuman): A: 0.05 − 0.05 = 0.00 → no response to mere presence of a person. B: 0.35 − 0.30 = 0.05, slightly above equal.
- Only A passes both tests, matching the profile the authors predicted for a ToM-specific region (p. 5). B responds about equally to all conditions (0.30–0.35), so it shows neither pattern; its small test-2 difference of 0.05 would need a statistical test.

## Concepts
- [[theory of mind / mentalizing / mindreading]] — here: any reasoning about another person's representational mental states, also called belief-desire psychology; broader than the narrow "theory-theory" sense (p. 1, footnote 1)
- [[theory-theory]] — the narrower claim that mental knowledge is structured like a scientific theory; mentioned in a footnote, not used (p. 1)
- [[temporo-parietal junction (TPJ)]] — cortical region; the TPJ-M subregion is proposed to be selective for mental-state reasoning (p. 1)
- [[mentalizing network]] — other regions found for ToM > control: aSTS, precuneus, medial prefrontal (pp. 3, 5)
- [[false-belief vs false-photograph contrast]] — controls for the logical need to represent false content, so belief-specific activity can be isolated (pp. 4–5)
- [[first-order false belief]] — a story where a character's action rests on a false belief (Wimmer & Perner, 1983) (p. 2)
- [[functional ROI (individually defined region)]] (new) — a region defined within each subject by a contrast (e.g. ToM > MI), then tested on other conditions (p. 3)
- [[double dissociation]] (new) — two regions each respond to one stimulus type and not the other; used for TPJ-M vs EBA (abstract, p. 1)
- [[extrastriate body area (EBA)]] (new) — region near posterior superior temporal cortex preferring images of human bodies (p. 2)
- [[physical-people control]] (new) — stories describing people's physical appearance, a control for mere presence of a person (p. 5)

## Canonical instances
- [[false-belief story task]] — the Porsche/Ford story as the ToM stimulus (p. 7)
- [[false-photograph task]] — the apple-photograph story as the logically matched non-mental control (pp. 4–5, 7)
- [[TPJ-M vs EBA dissociation]] — stories drive the TPJ-M and not the EBA; body photographs drive the EBA more than the TPJ-M (pp. 3–4)

## Bridges (candidates)
- [structural-analogy] Matching logical structure so a control differs only in the target feature (false photograph) ↔ construct validity in LLM evaluation: control items that isolate the capacity being claimed.
- [structural-analogy] Rejecting the explanation "it's a response to person presence" via the physical-people control ↔ Clever Hans effect: ruling out a superficial cue that could produce the same result.
- [metaphor] Within-subject functional localizer for neighbouring regions ↔ mentalizing network: separating nearby regions that group averages blur.

## Questions this raises
- Does the TPJ-M respond to ToM in non-verbal forms, such as cartoons? The paper hints at a hemisphere difference (pp. 3–4).
- Is the TPJ-M's role a general response to "behaviourally relevant" events, or a distinct subregion for mental states (footnote 2, p. 6)?
- What are the roles of the aSTS and medial prefrontal regions that also appeared (pp. 3, 5)?
- What does "broad role in social and even moral cognition" mean for what the TPJ-M computes (pp. 6–7)?

## Reading notes
- Printed page numbers equal the PDF page numbers (pdf N = printed N); the journal pages are 1835–1842.
- Possible inconsistencies in the source:
  - The text gives right TPJ-M body vs object as a trend (P < 0.10, p. 3). The Fig. 2 caption says P < 0.05 (p. 4).
  - The text says EBA story PSCs were "below 0.01" (p. 3). In the Fig. 2 image the left EBA story bars look a little above zero (roughly 0.05 by eye); no exact values are printed.
  - Exp. 2 Methods say 70 stories "12 each of" five conditions, which is 60 (p. 5).
  - The Exp. 2 whole-brain result cites "Fig. 2" (p. 5), but Fig. 2 shows Exp. 1 data.
- "Voegely" (p. 1) vs "Vogeley" in the references (p. 8); "Green and Haidt" (p. 1) vs "Greene" in the references (p. 8). A closing parenthesis is missing in the intro citation list (p. 1).
- Figures 3 and 4 are printed on pp. 4 and 6; Fig. 3 appears before Fig. 2 in the layout of p. 4.
- Some evidence is "unpublished data" or "submitted" (Saxe, Xiao et al.), so it could not be checked here (pp. 6, 8).
- In Fig. 4, the desire response looks smaller than the false-belief response. The text does not compare them (p. 6).
- No exercises in the source.

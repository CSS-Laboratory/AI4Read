# Prompt for the AI4Read agent · passage-centred English packs (v2)

Copy everything below the line into the agent that builds AI4Read's English packs (`~/code/AI4Read`, `scripts/english_pack.py`, `posts/<slug>/english/english.json`).

---

You build the English pack for each AI4Read post. Kunhao is changing how he studies these packs in Margin, and the pack format needs to follow.

## Why this is changing

Until now, each pack was a list of separate items: 16–17 expressions (each with its own example sentence), 4 patterns, 4 fixes, 2 tips and one "loop paragraph". In Margin these became separate cards in separate places.

From now on, **the loop paragraph is the centre**. Kunhao will:
1. loop the recording and shadow it until he can follow it easily;
2. notice the expressions and patterns *inside* it;
3. rebuild it from memory, gap by gap, until he can say it;
4. use its expressions and patterns in new sentences of his own.

So every expression and pattern must live **inside the passage**, and the passage needs enough structure (sentence boundaries, audio timings, a few questions) for Margin to drive those four steps. Today only about half the expressions appear in the loop paragraph (8 of 16 in post 01, 9 of 17 in post 02), and the loop lists its targets as plain strings without offsets.

## The new format: `ai4read.english-pack/2`

Keep everything that still applies from `/1`: `post`, `levels: "C1-C2"`, `externalId` stability, `source`, `tags`, CEFR `level` on every non-tip item. Change or add:

```jsonc
{
  "schema": "ai4read.english-pack/2",
  "post": { "slug": "...", "title": "...", "url": "https://khyang-lab.org/ai4read/<slug>/" },
  "levels": "C1-C2",
  "passage": {
    "externalId": "ai4read:<slug>:passage",
    "level": "C2",
    "text": "…",                       // 140–190 words, faithful to the post, natural spoken British English
    "sentences": [ { "start": 0, "end": 112 }, … ],   // UTF-16 offsets into text; cover it exactly, in order, no gaps except single spaces
    "core": [0, 2, 4],                // indexes of 3–4 sentences worth memorising word for word (60–90 words together)
    "audio": {
      "file": "audio/<slug>-passage.mp3",
      "voice": "<British English voice>",   // en-GB, see below
      "segments": [ { "sentence": 0, "startMs": 0, "endMs": 7400 }, … ]  // one per sentence, in order, within the file's duration
    },
    "gist": [                         // 2 questions that check understanding, answerable from the passage alone
      { "question": "…", "answer": "…" }
    ],
    "retell": {                       // one speaking/writing task that uses the passage's language
      "instruction": "In 2–3 sentences, explain … to a colleague.",
      "mustUse": ["ai4read:<slug>:<expression-id>", …],   // 3 expression externalIds
      "modelAnswer": "…"
    }
  },
  "items": [ … ]
}
```

### Items

- **expression** (8–12 per pack, all inside the passage):
  - `anchor: { "start", "end", "text" }` — UTF-16 offsets into `passage.text`; `text` must equal the slice exactly.
  - Keep `headword`, `definition`, `partOfSpeech`, `level`, `register`.
  - Keep `sentence` + `target` as a **second context** (a different, natural sentence using the expression in the same sense). Margin uses it to practise transfer, so it must not copy the passage.
- **pattern** (2–4, all inside the passage): `anchor` on the sentence or clause that uses the pattern, plus `headword`, `definition`, `level`. Keep `sentence` + `target` as a second example if you have one.
- **fix** (3–4): base each one on a passage sentence. `anchorSentence` = index into `passage.sentences`; `wrong` = that sentence with one typical C1-learner error (only one); `right` = the passage sentence exactly; `definition` = the rule in one line. Choose errors Kunhao is likely to make (article use, verb patterns such as *discuss about*, uncountables, tense in reported findings), not trick errors.
- **tip**: optional, at most 2. Margin shows tips but does not make cards from them.
- Remove the old `shadowing` item; the passage replaces it. Margin will retire the old `loop-paragraph-c1c2` ids itself.

### Voice

Margin's shadowing guide marks **British** connected speech (weak forms, linking, elision), but the current recordings use a US voice (Kokoro `af_heart`). Shadowing a US recording against a British guide gives mixed signals. Please record the passage with a British English voice (for example Kokoro `bf_emma` or `bm_george`, or whichever en-GB voice sounds most natural), at a natural pace (about 150–160 words per minute), with a clear pause between sentences so each segment can be looped on its own. Keep the "AI4Read from CSS Lab" tag.

## Rules

- Write the passage first, then choose expressions and patterns that occur in it naturally. Do not force an expression into a sentence where a native writer would not use it.
- The passage must say what the post says; no new claims.
- C1–C2 only. Every expression should be worth learning for someone who already reads *The Economist* comfortably.
- Keep `externalId`s for expressions that survive from the current packs. List any ids you drop in a new `retired-<date>.json`, as before.
- Do not change the post pages.

## Validation (fail the build if any check fails)

1. `passage.text.slice(a.start, a.end) === a.text` for every anchor (UTF-16), and every anchor lies inside one sentence.
2. `sentences` cover `text` in order, without overlap; each fix's `right` equals its anchored sentence.
3. Every `mustUse` id exists and is an expression in this pack.
4. `audio.segments`: one per sentence, increasing, non-overlapping, within the file's duration (measure it).
5. Word counts: passage 140–190 words; `core` sentences together 60–90 words.
6. Every non-tip item has `level` in the pack's `levels`.
7. Each expression's second-context `sentence` differs from every passage sentence.

## Deliverables

For posts 01 (`2026-10-llm-next-word`) and 02 (`2026-10-ai-finance`):
- `site/mewiki/packs/<slug>.json` in the `/2` format, plus the readable `.md` preview;
- `site/mewiki/packs/audio/<slug>-passage.mp3` (British voice) with segment timings in the pack;
- `site/mewiki/packs/retired-<date>.json` if any ids were dropped;
- a short note in `site/mewiki/HANDOFF-margin.md` §0 describing `/2`.

Then tell Kunhao the item counts per pack, the passage word counts, the audio durations, and anything you could not satisfy.

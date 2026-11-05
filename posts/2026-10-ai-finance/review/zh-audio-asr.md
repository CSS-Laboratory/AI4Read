# Chinese audio check by speech recognition (2026-10-ai-finance)

faster-whisper `small`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).

| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard | heard runs not in the script (≥ 10 chars more) |
|---|---|---|---|---|---|
| hook | 0.932 | 943 | 964 | — | ENGLISHNAMESANDTERMSINENGLISH |
| guess | 0.931 | 331 | 318 | — | — |
| home | 0.958 | 1244 | 1235 | — | — |
| llm | 0.959 | 663 | 663 | — | — |
| lens-control | 0.964 | 1184 | 1182 | — | — |
| lens-decision | 0.891 | 683 | 670 | — | — |
| lens-cascade | 0.922 | 1272 | 1261 | — | — |
| lens-social | 0.970 | 940 | 939 | — | — |
| lens-answer | 0.948 | 883 | 883 | — | — |
| play | 0.925 | 168 | 167 | — | — |
| turn | 0.907 | 239 | 233 | — | — |
| work | 0.972 | 250 | 250 | — | — |
| answer | 0.971 | 1089 | 1084 | — | — |
| recall | 0.924 | 301 | 294 | — | — |

Flagged for listening: hook.

Verified 2026-11-05 with the medium model: `hook` 18–22 s says “English names and terms in English” (part of the style instruction, read aloud after the short line 文中引用的原话都是我们的中文翻译。). Re-record `hook`.

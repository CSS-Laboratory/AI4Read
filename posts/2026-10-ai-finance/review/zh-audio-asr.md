# Chinese audio check by speech recognition (2026-10-ai-finance)

faster-whisper `small`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).

| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard |
|---|---|---|---|---|
| hook | 0.932 | 943 | 964 | — |
| guess | 0.931 | 331 | 318 | — |
| home | 0.958 | 1244 | 1235 | — |
| llm | 0.959 | 663 | 663 | — |
| lens-control | 0.964 | 1184 | 1182 | — |
| lens-decision | 0.652 | 683 | 670 | — |
| lens-cascade | 0.922 | 1272 | 1261 | — |
| lens-social | 0.969 | 940 | 939 | — |
| lens-answer | 0.631 | 883 | 883 | — |
| play | 0.925 | 168 | 167 | — |
| turn | 0.907 | 239 | 233 | — |
| work | 0.972 | 250 | 250 | — |
| answer | 0.971 | 1089 | 1084 | — |
| recall | 0.924 | 301 | 294 | — |

Flagged for listening: lens-decision, lens-answer.

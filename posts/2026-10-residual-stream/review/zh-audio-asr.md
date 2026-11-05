# Chinese audio check by speech recognition (2026-10-residual-stream)

faster-whisper `small`, int8, CPU. Similarity on characters only; ≥ 0.85 is normal (homophones, digits).

| chapter | similarity | script chars | heard chars | script runs of ≥ 15 chars not heard |
|---|---|---|---|---|
| hook | 0.904 | 587 | 643 | — |
| guess | 0.958 | 543 | 540 | — |
| sum | 0.913 | 2283 | 2242 | — |
| bets | 0.935 | 1393 | 1382 | — |
| rw | 0.876 | 1177 | 1159 | — |
| dir | 0.849 | 2007 | 1945 | — |
| answer | 0.914 | 695 | 684 | — |
| lens-linalg | 0.909 | 642 | 630 | — |
| lens-info | 0.915 | 1069 | 1051 | — |
| turn | 0.900 | 1027 | 1013 | — |
| work | 0.837 | 545 | 664 | — |
| recall | 0.863 | 658 | 642 | — |

Flagged for listening: none.

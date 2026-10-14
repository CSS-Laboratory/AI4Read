"""Gate CC report: Claude Code route vs batch on the same units (reviews/wave-4.md, CLAUDE_CODE_ROUTE.md).

python -m pipeline.gatecc_report [--meter-before X --meter-after Y]  -> prints markdown (also written to pipeline/GATE-CC.md)
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from . import PIPE, REPO
from .build import target_words, units
from .run import parse_verdict

PARITY = ["kuhn-1962-structure/ch09-nature", "gelman-2013-bda3/ch05-hierarchical",
          "dennett-1987-intentional-stance/ch02-true"]
RECHECK = ["meadows-2008-thinking/ch02-note", "popper-1959-logic/front-preface-2"]
NAMES = {"A": "faithfulness", "B": "math", "C": "pages", "D": "coverage", "E": "numbers", "F": "labels",
         "G": "format", "H": "strength/voice"}


def jl(p):
    return [json.loads(l) for l in open(p) if l.strip()] if Path(p).exists() else []


def latest(recs, uid):
    out = {}
    for r in recs:
        if r["unit_id"] == uid:
            out.update(r)
    return out


def body_words(path):
    t = (REPO / path).read_text()
    return len(re.sub(r"^---.*?---\s*", "", t, count=1, flags=re.S).split())


def issues_summary(txt):
    v = parse_verdict(txt)
    c = Counter((i.get("check"), i.get("severity")) for i in v["issues"] or [] if isinstance(i, dict))
    sev = Counter(i.get("severity") for i in v["issues"] or [] if isinstance(i, dict))
    hc = [h for h in (v["h_checks"] or []) if isinstance(h, dict)]
    bad = sum(1 for h in hc if h.get("ok") is False)
    by = ", ".join(f"{NAMES.get(k, k)} {sum(n for (kk, s), n in c.items() if kk == k)}"
                   for k in "ABCDEFGH" if any(kk == k for (kk, _) in c))
    return (f"{v['verdict']} · {sev.get('critical', 0)}c/{sev.get('major', 0)}M/{sev.get('minor', 0)}m"
            f" ({by or '—'})", f"{bad}/{len(hc)} ({100 * bad / max(len(hc), 1):.0f}%)")


def unit_row(uid, state_log, spend_log, out_dir, timing, isolate):
    U = units()
    rec = latest(jl(state_log), uid)
    sp = [s for s in jl(spend_log) if s.get("unit_id") == uid and s.get("route") == "claude-code"]
    tm = [t for t in jl(timing) if t["unit_id"] == uid and t.get("isolate") == isolate]
    loop = rec.get("loop", 0) or 0
    p2 = sorted(out_dir.glob(f"{uid.replace('/', '__')}.p2-*.txt"), key=lambda p: p.stat().st_mtime)
    first_iss, first_h = issues_summary(p2[0].read_text()) if p2 else ("—", "—")
    last_iss, last_h = issues_summary(p2[-1].read_text()) if p2 else ("—", "—")
    words = rec.get("words") or (body_words(rec["path"]) if rec.get("path") else None)
    tw = target_words(U[uid])
    secs = sum(s.get("seconds") or 0 for s in sp)
    kinds = Counter(s["what"].replace("cc-", "") for s in sp)
    tok = defaultdict(int)
    for s in sp:
        for k, v in (s.get("usage") or {}).items():
            tok[k] += v
    return {"uid": uid, "final": rec.get("state"), "verified": rec.get("verified"), "path": rec.get("path"),
            "loops": loop, "sessions": dict(kinds), "n_sessions": len(sp), "wall_min": round(secs / 60, 1),
            "unit_wall_min": round(sum(t["seconds"] for t in tm) / 60, 1) if tm else None,
            "words": words, "target": tw, "ratio": round(words / tw, 2) if words else None,
            "first_p2": first_iss, "first_h": first_h, "last_p2": last_iss, "last_h": last_h,
            "tokens": dict(tok)}


def batch_row(uid):
    """Batch version for comparison: accepted file length, last batch P2 issues."""
    from . import state
    L = state.latest()
    rec = L.get(uid, {})
    p = rec.get("path")
    words = body_words(p) if p and (REPO / p).exists() else None
    loop = rec.get("loop", 0) or 0
    f = PIPE / "_work" / "out" / f"{uid.replace('/', '__')}.p2-{loop}.txt"
    iss, h = issues_summary(f.read_text()) if f.exists() else ("—", "—")
    audited = bool(p and (REPO / p).exists() and re.search(r"^audited:", (REPO / p).read_text(), re.M))
    return {"words": words, "p2": iss, "h": h, "audited": audited}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--meter-before")
    ap.add_argument("--meter-after")
    a = ap.parse_args(argv)
    timing = PIPE / "results" / "cc_timing.jsonl"
    lines = ["# Gate CC — Claude Code route parity test", "",
             "Route: every pass = a fresh `claude -p --model sonnet` session (Read-only tools, restricted, no MCP), "
             "subscription auth; same prompts v2.2, length target, checks, edit handling and state machine as the "
             "batch path. Parity outputs: `*.cc.md` next to the batch files (nothing overwritten).", ""]
    rows = []
    lines += ["## Parity units (also done in batch and hand-audited)", "",
              "| Unit | Result | Sessions | Wall time | Words vs target | Verifier, first pass | h_checks not ok (first) | Batch: words · verifier | Batch audited |",
              "|---|---|---|---|---|---|---|---|---|"]
    for uid in PARITY:
        r = unit_row(uid, PIPE / "state" / "gatecc_units.jsonl", PIPE / "state" / "gatecc_spend.jsonl",
                     PIPE / "_work" / "out_gatecc", timing, "gatecc")
        b = batch_row(uid)
        rows.append(r)
        lines.append(f"| `{uid}` | {r['final']} ({r['verified']}) | {r['n_sessions']} ({', '.join(f'{k}×{v}' for k, v in r['sessions'].items())}) | "
                     f"{r['wall_min']} min | {r['words']} / {r['target']} = {r['ratio']}× | {r['first_p2']} | {r['first_h']} | "
                     f"{b['words']} words · {b['p2']} | {'yes' if b['audited'] else 'no'} |")
    lines += ["", "## needs-review re-checks (normal route; written in place only if all checks pass)", "",
              "| Unit | Result | Sessions | Wall time | Words vs target | Verifier, first pass | h_checks not ok |",
              "|---|---|---|---|---|---|---|"]
    for uid in RECHECK:
        r = unit_row(uid, PIPE / "state" / "units.jsonl", PIPE / "state" / "spend.jsonl",
                     PIPE / "_work" / "out", timing, None)
        rows.append(r)
        lines.append(f"| `{uid}` | {r['final']} ({r['verified']}) | {r['n_sessions']} ({', '.join(f'{k}×{v}' for k, v in r['sessions'].items())}) | "
                     f"{r['wall_min']} min | {r['words']} / {r['target']} = {r['ratio']}× | {r['first_p2']} | {r['first_h']} |")
    tot_min = sum(r["wall_min"] for r in rows)
    tot = defaultdict(int)
    for r in rows:
        for k, v in r["tokens"].items():
            tot[k] += v
    lines += ["", "## Totals", f"- Sessions: {sum(r['n_sessions'] for r in rows)} · model wall time {tot_min:.0f} min "
              f"(≈ {tot_min / len(rows):.0f} min per unit, sequential)",
              f"- Tokens reported by Claude Code: input {tot['input']:,} · cache read {tot['cache_read']:,} · "
              f"cache write {tot['cache_write']:,} · output {tot['output']:,}"]
    if a.meter_before and a.meter_after:
        lines.append(f"- **Weekly usage meter (Kunhao): {a.meter_before} → {a.meter_after}**")
    else:
        lines.append("- **Weekly usage meter: to be filled in by Kunhao (before → after)**")
    text = "\n".join(lines) + "\n"
    print(text)
    return text, rows


if __name__ == "__main__":
    main()

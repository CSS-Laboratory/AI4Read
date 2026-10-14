"""Claude Code route (pipeline/CLAUDE_CODE_ROUTE.md): deep + reference tiers on the Claude subscription.

Same pipeline as the batch path — units.csv, request builder (prompts, {{MANDATORY_ITEMS}}, {{TARGET_WORDS}},
page text + 1200/1500 px images, printed labels), deterministic checks, edit application, fix pass, residue
stripping, state log — only the model call differs: every pass is a FRESH headless Claude Code process
(`claude -p --model sonnet`), so P1 and P2 never share context.

python -m pipeline cc-run [--until 20:30] [--units a/b c/d] [--suffix .cc.md] [--max-units N] [--dry-run]

Notes
- Each pass gets a work folder OUTSIDE the repo (~/.cache/ai4read-cc/...) holding system.md, task.md and the page
  images; the subagent may only Read files there (--tools Read --restricted --strict-mcp-config, dontAsk).
- Never uses --bare: that would switch auth to an API key instead of the subscription.
- Units are processed one by one; an accepted unit is committed and pushed at once. A unit interrupted mid-way
  is redone from P1 next run (nothing partial is written to wiki/).
- Stops at --until, on control.json pause/stop, or when Claude Code reports a usage limit.
"""
import argparse
import base64
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

from . import PIPE, REPO, control, state
from .build import PROMPT_VERSION, SPEC_VERSION, p1_request, p2_request, units
from .run import (FIX_NOTE, OUT, OUT_ROOT, handle_p1, handle_p2, handle_p2fix, latest_digest, log, next_pass,
                  usage_parts)

ROUTE = "claude-code"
WORK = Path(os.path.expanduser("~/.cache/ai4read-cc"))
CLAUDE = shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")
MODEL = "sonnet"
PASS_TIMEOUT_S = 45 * 60
USAGE_LIMIT = re.compile(r"usage limit|limit reached|rate limit|quota|out of (extra )?usage|try again (at|in)", re.I)
TIER_ORDER = ["deep", "reference"]
SUFFIX = [None]                       # e.g. ".cc.md" for the parity test (never overwrite batch outputs)


class UsageLimit(Exception):
    pass


# ------------------------------------------------------------------ request -> files

def materialize(uid, kind, req):
    """Write system prompt, task (all text blocks) and images of a built request into a fresh folder."""
    d = WORK / uid.replace("/", "__") / f"{kind}-{time.strftime('%Y%m%d-%H%M%S')}"
    d.mkdir(parents=True, exist_ok=True)
    system = "".join(b["text"] for b in req["system"])
    parts, n_img = [], 0
    for b in req["messages"][0]["content"]:
        if b["type"] == "text":
            parts.append(b["text"])
        elif b["type"] == "image":
            n_img += 1
            name = f"img_{n_img:03d}.jpg"
            (d / name).write_bytes(base64.b64decode(b["source"]["data"]))
            parts.append(f"(image file: {name} — read it with the Read tool)")
    task = "\n\n".join(parts)
    header = ("All source material for this task is in this folder. The page images are separate files; "
              "a line '(image file: NAME)' follows each image label. Read EVERY image file with the Read tool "
              "before writing — the images are the ground truth. Then output only what the instructions ask for, "
              "with no preamble.\n\n")
    (d / "system.md").write_text(system)
    (d / "task.md").write_text(header + task)
    return d, system, header + task, n_img


def call_claude(workdir, system, task, dry_run=False):
    """One fresh headless Claude Code session (Sonnet). Returns (text, meta)."""
    cmd = [CLAUDE, "-p", "Do the task described in task.md in this folder. Read task.md first.",
           "--model", MODEL, "--system-prompt", system,
           "--tools", "Read", "--restricted", "--strict-mcp-config", "--permission-mode", "dontAsk",
           "--add-dir", str(workdir), "--no-session-persistence", "--output-format", "json"]
    if dry_run:
        return "", {"dry_run": True, "cmd": cmd[:4] + ["…"] + cmd[5:6] + ["<system>"] + cmd[7:], "cwd": str(workdir)}
    t0 = time.time()
    p = subprocess.run(cmd, cwd=workdir, capture_output=True, text=True, timeout=PASS_TIMEOUT_S)
    meta = {"exit": p.returncode, "seconds": round(time.time() - t0)}
    try:
        out = json.loads(p.stdout)
    except json.JSONDecodeError:
        out = {"result": p.stdout, "is_error": True}
    text = out.get("result") or ""
    meta.update({k: out.get(k) for k in ("is_error", "subtype", "num_turns", "duration_ms", "usage",
                                         "total_cost_usd") if k in out})
    if (out.get("is_error") or p.returncode != 0) and USAGE_LIMIT.search(text + p.stderr):
        raise UsageLimit(text[:200] or p.stderr[:200])
    if out.get("is_error") or p.returncode != 0:
        raise RuntimeError(f"claude exit {p.returncode}: {(text or p.stderr)[:300]}")
    return text, meta


def as_resp(text, meta):
    """Shape a Claude Code result like a Messages API response for the shared handlers."""
    u = meta.get("usage") or {}
    return {"content": [{"type": "text", "text": text}], "stop_reason": "end_turn",
            "usage": {"input_tokens": u.get("input_tokens", 0), "output_tokens": u.get("output_tokens", 0),
                      "cache_read_input_tokens": u.get("cache_read_input_tokens", 0),
                      "cache_creation_input_tokens": u.get("cache_creation_input_tokens", 0)}}


# ------------------------------------------------------------------ one unit

def build(uid, kind):
    st = state.latest().get(uid, {})
    if kind == "p1":
        return p1_request(uid)
    if kind == "p3":
        return p1_request(uid, issues=st.get("issues"))
    req, stats = p2_request(uid, latest_digest(uid, st.get("loop", 0)))
    if kind == "p2fix":
        req["messages"][0]["content"].append({"type": "text", "text": FIX_NOTE})
    return req, stats


def process_unit(uid, dry_run=False):
    """Run passes until the unit is accepted / needs_human. Returns final state."""
    for _ in range(8):                                   # P1, P2, fix/P3, P2, fix/P3, P2 at most
        st = state.latest().get(uid, {})
        kind = next_pass(uid, st)
        if kind is None:
            return st.get("state")
        req, stats = build(uid, kind)
        wd, system, task, n_img = materialize(uid, kind, req)
        state.record(uid, "p2_submitted" if kind in ("p2", "p2fix") else "p1_submitted", kind=kind,
                     loop=st.get("loop", 0), route=ROUTE, batch_job_id=ROUTE, spec_version=SPEC_VERSION,
                     prompt_version=PROMPT_VERSION, workdir=str(wd), **stats)
        log(f"  {uid} {kind}: {n_img} images, {len(task):,} chars -> claude -p ({MODEL})")
        text, meta = call_claude(wd, system, task, dry_run=dry_run)
        if dry_run:
            log(f"  dry run: {meta}")
            state.record(uid, {"p1": "planned", "p3": "p3_queued", "p2": "p1_done", "p2fix": "p2_fix_queued"}[kind],
                         note="cc dry run", route=ROUTE)
            return "dry-run"
        resp = as_resp(text, meta)
        state.add_spend(0.0, f"cc-{kind}", unit_id=uid, route=ROUTE, usage=usage_parts(resp["usage"]),
                        seconds=meta.get("seconds"), num_turns=meta.get("num_turns"))
        state.record(uid, state.latest()[uid]["state"], **{f"{kind}_usage": usage_parts(resp["usage"]),
                                                          f"{kind}_seconds": meta.get("seconds")})
        {"p2": handle_p2, "p2fix": handle_p2fix}.get(kind, handle_p1)(uid, resp, state.latest()[uid])
    return state.latest().get(uid, {}).get("state")


# ------------------------------------------------------------------ selection, commit, main loop

def pick_units(explicit=None):
    if explicit:
        return explicit
    L = state.latest()
    rows = [r for r in csv.DictReader(open(PIPE / "units.csv")) if r["action"] == "digest"]
    prio = []
    pf = PIPE / "waves" / "priority.txt"
    if pf.exists():
        prio = [l.split("#")[0].strip() for l in pf.read_text().splitlines() if l.split("#")[0].strip()]
    todo = []
    for tier in TIER_ORDER:
        for r in rows:
            u = f"{r['work_id']}/{r['unit_id']}"
            if r["tier"] == tier and L.get(u, {}).get("state") not in ("accepted", "needs_human", "skipped"):
                todo.append(u)
    first = [u for u in todo if u in prio or u.split("/")[0] in prio]
    rc = PIPE / "waves" / "cc_recheck.txt"           # accepted as 'needs-review' on Vertex: re-check first
    recheck = [l.split("#")[0].strip() for l in rc.read_text().splitlines() if l.split("#")[0].strip()] if rc.exists() else []
    recheck = [u for u in recheck if L.get(u, {}).get("verified") == "needs-review"]
    return recheck + first + [u for u in todo if u not in first and u not in recheck]


def reset_interrupted(ids):
    """A unit left in a *_submitted state by an earlier Claude Code run is redone from P1."""
    L = state.latest()
    for u in ids:
        r = L.get(u, {})
        if r.get("route") == ROUTE and r.get("state") in ("p1_submitted", "p2_submitted"):
            state.record(u, "planned", note="cc: interrupted run -> redo from P1", route=ROUTE, loop=0)


def commit_unit(uid, msg):
    paths = ["pipeline/state", "pipeline/STATUS.md", "wiki/works"]
    subprocess.run(["git", "-C", str(REPO), "add", *paths], check=False)
    r = subprocess.run(["git", "-C", str(REPO), "commit", "-qm",
                        msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"], capture_output=True)
    if r.returncode == 0:
        subprocess.run(["git", "-C", str(REPO), "pull", "--rebase", "--autostash", "-q"], check=False)
        subprocess.run(["git", "-C", str(REPO), "push", "-q"], check=False)


def status_block(done, started, stop_reason):
    L = state.latest()
    rows = [r for r in csv.DictReader(open(PIPE / "units.csv")) if r["action"] == "digest" and r["tier"] in TIER_ORDER]
    total = len(rows)
    acc = sum(1 for r in rows if L.get(f"{r['work_id']}/{r['unit_id']}", {}).get("state") == "accepted")
    block = (f"### Claude Code route\n- This run: {len(done)} units accepted ({', '.join(done[:6])}"
             f"{'…' if len(done) > 6 else ''}) · started {started} · stop: {stop_reason}\n"
             f"- Deep + reference: {acc} / {total} accepted\n")
    (PIPE / "results" / "cc_status.md").write_text(block)
    return block


def cc_run(until=None, explicit=None, max_units=None, dry_run=False, suffix=None):
    started = time.strftime("%Y-%m-%d %H:%M")
    if suffix:
        SUFFIX[0] = suffix
        _patch_wiki_suffix(suffix)
    deadline = None
    if until:
        hh, mm = map(int, until.split(":"))
        now = time.localtime()
        deadline = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, hh, mm, 0, 0, 0, -1))
    ids = pick_units(explicit)
    reset_interrupted(ids)
    for u in ids:                                       # needs-review re-checks restart from P1 on this route
        if state.latest().get(u, {}).get("verified") == "needs-review":
            state.record(u, "planned", note="cc: re-check of a needs-review unit", route=ROUTE, loop=0, p2_reruns=0)
    done, stop = [], "queue empty"
    for uid in ids:
        if deadline and time.time() > deadline - 20 * 60:       # do not start a unit in the last 20 minutes
            stop = f"time ({until})"
            break
        ctl = control.read(do_pull=not dry_run)
        if ctl["mode"] in ("pause", "stop"):
            stop = f"control.json mode={ctl['mode']}"
            break
        if max_units and len(done) >= max_units:
            stop = f"max_units={max_units}"
            break
        log(f"cc unit {uid}")
        try:
            final = process_unit(uid, dry_run=dry_run)
        except UsageLimit as e:
            stop = f"usage limit: {e}"
            log(stop)
            break
        except Exception as e:                                  # one bad unit must not stop the run
            log(f"  {uid} error: {str(e)[:300]}")
            state.record(uid, "planned", note=f"cc error: {str(e)[:200]}", route=ROUTE, loop=0)
            continue
        if final == "accepted":
            done.append(uid)
            if not dry_run:
                commit_unit(uid, f"digest (claude-code): {uid}")
        if dry_run:
            stop = "dry run (one unit)"
            break
    log(f"cc-run finished: {len(done)} accepted, stop: {stop}")
    print(status_block(done, started, stop))
    return done, stop


def _patch_wiki_suffix(suffix):
    """Parity test: write accepted digests as <unit><suffix> (e.g. ch09.cc.md) — never overwrite batch outputs."""
    from . import run as runmod

    def wiki_path(uid):
        work, unit = uid.split("/", 1)
        return OUT_ROOT[0] / work / f"{unit}{suffix}"
    runmod.wiki_path = wiki_path


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pipeline cc-run")
    ap.add_argument("--until", help="local time HH:MM to stop starting new units (default: none)")
    ap.add_argument("--units", nargs="*", help="explicit unit ids (parity test)")
    ap.add_argument("--max-units", type=int)
    ap.add_argument("--suffix", help="write accepted digests as <unit><suffix>, e.g. .cc.md")
    ap.add_argument("--dry-run", action="store_true", help="build + materialize the first pass, no model call")
    a = ap.parse_args(argv)
    cc_run(a.until, a.units, a.max_units, a.dry_run, a.suffix)


if __name__ == "__main__":
    main()

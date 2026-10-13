"""Resumable wave runner (DESIGN.md "State machine", "Pause / resume", "Budget control").

python -m pipeline run <wave> [--once] [--online]
  <wave> = pipeline/waves/<wave>.txt (one unit id per line)

Loop: git pull + read control.json -> collect finished jobs -> (mode == run) submit next pass
-> write STATUS.md / commit (<= every 15 min) -> sleep. Safe to kill at any time.
"""
import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

from google.cloud import storage

from . import PIPE, REPO, control, state
from .build import PROMPT_VERSION, SPEC_VERSION, content_hash, p1_request, p2_request, target_words, units
from .checks import check, errors, fix_math
from .vertex import CFG, batch_create, batch_get, cost, online

WAVES = PIPE / "waves"
OUT = PIPE / "_work" / "out"
JOBS = PIPE / "state" / "jobs.jsonl"
MAX_JOBS = 4                    # Vertex default concurrent batch jobs per project
MAX_LOOPS = 2                   # P3 re-digests before needs_human
PIPELINE_VERSION = "0.1"
REFERENCE_UNITS = {"akerlof-1970-lemons/main", "cover-2006-elements/ch02-entropy"}
TERMINAL = {"accepted", "needs_human", "skipped"}
ONLINE_MODE = [False]
FIX_NOTE = ("Your edits could not be applied exactly. Return the same verdict and issues, leave <edits> empty, "
            "and give the COMPLETE corrected digest in <corrected>.")


# ------------------------------------------------------------------ helpers

def log(*a):
    print(time.strftime("%H:%M:%S"), *a, flush=True)


def wave_units(wave):
    ids = [l.split("#")[0].strip() for l in (WAVES / f"{wave}.txt").read_text().splitlines()]
    ids = [i for i in ids if i]
    U = units()
    missing = [i for i in ids if i not in U]
    if missing:
        sys.exit(f"unknown unit ids in wave {wave}: {missing}")
    return ids


def jobs():
    out = {}
    if JOBS.exists():
        for l in JOBS.read_text().splitlines():
            if l.strip():
                r = json.loads(l)
                out[r["job"]] = {**out.get(r["job"], {}), **r}
    return out


def job_record(**r):
    JOBS.parent.mkdir(parents=True, exist_ok=True)
    with open(JOBS, "a") as f:
        f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), **r}) + "\n")


def bucket():
    return storage.Client(project=CFG["project"]).bucket(CFG["bucket"].removeprefix("gs://"))


def usage_parts(u):
    det = u.get("output_tokens_details") or {}
    return {
        "input": u.get("input_tokens", 0),
        "cache_read": u.get("cache_read_input_tokens", 0),
        "cache_write": u.get("cache_creation_input_tokens", 0),
        "output": u.get("output_tokens", 0),
        "thinking": det.get("thinking_tokens", 0),
    }


def text_of(resp):
    return "".join(c.get("text", "") for c in resp.get("content", []) if c.get("type") == "text").strip()


def strip_fence(md):
    m = re.match(r"^```(?:markdown|md)?\s*\n(.*)\n```\s*$", md.strip(), re.S)
    return m.group(1) if m else md.strip()


# ------------------------------------------------------------------ P2 parsing

def parse_verdict(txt):
    def tag(name):
        m = re.search(rf"<{name}>(.*?)</{name}>", txt, re.S)
        return m.group(1).strip() if m else None

    def js(s):
        if not s:
            return []
        s = re.sub(r"^```(?:json)?\s*|\s*```$", "", s.strip())
        try:
            v = json.loads(s)
            return v if isinstance(v, list) else []
        except json.JSONDecodeError:
            return None
    verdict = (tag("verdict") or "").lower()
    h = tag("h_checks")
    return {"verdict": verdict if verdict in ("pass", "repair", "fail") else None,
            "h_checks": js(h) if h is not None else None,      # None = block missing -> rerun P2
            "issues": js(tag("issues")), "edits": js(tag("edits")),
            "corrected": strip_fence(tag("corrected") or "")}


def apply_edits(md, edits):
    """Each find must occur exactly once. If the exact text is not found, retry with whitespace
    differences ignored (LaTeX spacing); still exactly one match required. Returns (new_md, failures)."""
    fails = []
    for e in edits or []:
        f, r = e.get("find", ""), e.get("replace", "")
        n = md.count(f) if f else 0
        if n == 1:
            md = md.replace(f, r, 1)
            continue
        if n == 0 and f.strip():
            pat = r"\s*".join(re.escape(ch) for ch in re.sub(r"\s+", "", f))
            hits = list(re.finditer(pat, md))
            if len(hits) == 1:
                h = hits[0]
                md = md[:h.start()] + r + md[h.end():]
                continue
            n = len(hits)
        fails.append({"find": f[:80], "count": n})
    return md, fails


RESIDUE_TAGS = r"</?(verdict|h_checks|issues|edits|corrected)>"


def strip_residue(md):
    """Remove verifier residue from a digest: text before the frontmatter, stray tags, JSON fragments, fences."""
    md = strip_fence(md)
    i = md.find("---")
    if i > 0:
        md = md[i:]
    md = re.sub(RESIDUE_TAGS, "", md)
    lines, out = md.splitlines(), []
    for l in lines:
        s = l.strip()
        if re.match(r'^(\[\s*\{|\{\s*"(find|replace|severity|item)"|"(find|replace)"\s*:|\]\s*$|```json\s*$)', s):
            continue
        out.append(l)
    md = "\n".join(out)
    # verifier chatter left inside the prose by an edit (audit J7): drop just that sentence
    chatter = (r"[^.!?\n]*\b(?:is correct as printed|as printed is correct|the digest (?:says|states|has|is)"
               r"|this digest|the verifier|verifier note)\b[^.!?\n]*[.!?]")
    md = re.sub(r"(?<=[.!?:)])[ \t]+" + chatter, "", md, flags=re.I)        # mid-paragraph sentence
    md = re.sub(r"(?m)^(\s*(?:[-*>]\s*)?)" + chatter + r"[ \t]*", r"\1", md, flags=re.I)  # sentence at line start
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def add_frontmatter(md, extra):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", md, re.S)
    if not m:
        return md
    fm = m.group(1)
    for k, v in extra.items():
        fm = re.sub(rf"^{k}:.*\n?", "", fm, flags=re.M).rstrip("\n")
        fm += f"\n{k}: {v}"
    return f"---\n{fm}\n---\n" + md[m.end():]


# ------------------------------------------------------------------ outputs

OUT_ROOT = [REPO / "wiki" / "works"]      # run(..., out_dir=...) redirects accepted digests (regression tests)


def wiki_path(uid):
    work, unit = uid.split("/", 1)
    name = f"{unit}.pipeline.md" if uid in REFERENCE_UNITS else f"{unit}.md"
    return OUT_ROOT[0] / work / name


def accept(uid, md, verified, n_issues):
    md = fix_math(strip_residue(md))
    md = add_frontmatter(md, {"spec_version": SPEC_VERSION, "prompt_version": PROMPT_VERSION, "verified": verified,
                              "verifier_issues": n_issues, "pipeline_version": PIPELINE_VERSION})
    p = wiki_path(uid)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(md.rstrip() + "\n")
    body_words = len(re.sub(r"^---.*?---\s*", "", md, count=1, flags=re.S).split())
    state.record(uid, "accepted", verified=verified, verifier_issues=n_issues, path=str(p.relative_to(REPO)),
                 words=body_words, target_words=target_words(units()[uid]),
                 spec_version=SPEC_VERSION, prompt_version=PROMPT_VERSION)


def handle_p1(uid, resp, rec):
    md = strip_fence(text_of(resp))
    OUT.mkdir(parents=True, exist_ok=True)
    loop = rec.get("loop", 0)
    (OUT / f"{uid.replace('/', '__')}.p{1 if loop == 0 else 3}-{loop}.md").write_text(md)
    iss = check(md, units()[uid], uid)
    state.record(uid, "p1_done", loop=loop, det_errors=len(errors(iss)), det_issues=iss[:20],
                 stop_reason=resp.get("stop_reason"))
    if resp.get("stop_reason") == "max_tokens":
        state.record(uid, "needs_human", reason="P1 hit max_tokens: split the unit")


def handle_p2(uid, resp, rec):
    txt = text_of(resp)
    loop = rec.get("loop", 0)
    (OUT / f"{uid.replace('/', '__')}.p2-{loop}.txt").write_text(txt)
    v = parse_verdict(txt)
    digest = latest_digest(uid, loop)
    issues = v["issues"] if isinstance(v["issues"], list) else []
    if v["verdict"] is not None and v["h_checks"] is None:       # gate2 review: missing <h_checks> = rerun P2
        n = rec.get("p2_reruns", 0) + 1
        if n > 2:
            return state.record(uid, "needs_human", reason="verifier omitted <h_checks> 3 times", loop=loop)
        return state.record(uid, "p1_done", loop=loop, p2_reruns=n, note="rerun P2: <h_checks> missing")
    if resp.get("stop_reason") == "max_tokens" or v["verdict"] is None or v["edits"] is None:
        return requeue(uid, loop, issues or [{"severity": "major", "problem": "verifier output unparseable"}],
                       "verifier output unparseable or truncated")
    n_crit = sum(1 for i in issues if i.get("severity") in ("critical", "major"))
    if v["verdict"] == "fail":
        return requeue(uid, loop, issues, "verifier verdict fail")
    if v["corrected"]:
        new, fails = v["corrected"], []
    else:
        new, fails = apply_edits(digest, v["edits"])
    if fails:
        state.record(uid, "p2_done", loop=loop, verdict=v["verdict"], edit_failures=fails,
                     n_issues=len(issues))
        if ONLINE_MODE[0]:
            return fix_online(uid, loop, digest, issues, fails)
        return state.record(uid, "p2_fix_queued", loop=loop, issues=issues[:40])
    new = fix_math(new)
    det = errors(check(new, units()[uid], uid))
    hc = v["h_checks"] or []
    state.record(uid, "p2_done", loop=loop, verdict=v["verdict"], n_issues=len(issues), n_major=n_crit,
                 n_h=len(hc), n_h_fail=sum(1 for h in hc if isinstance(h, dict) and h.get("ok") is False),
                 n_edits=len(v["edits"] or []), rewrite=bool(v["corrected"]), det_errors_after=len(det))
    if det:
        return requeue(uid, loop, issues + [{"severity": "major", "check": "G", "problem": d["msg"]} for d in det],
                       "deterministic checks fail after P2")
    verified = "pass" if v["verdict"] == "pass" and not (v["edits"] or v["corrected"]) else "repaired"
    accept(uid, new, verified, len(issues))


def handle_p2fix(uid, resp, rec):
    loop = rec.get("loop", 0)
    txt = text_of(resp)
    (OUT / f"{uid.replace('/', '__')}.p2fix-{loop}.txt").write_text(txt)
    v = parse_verdict(txt)
    issues = v["issues"] if isinstance(v["issues"], list) else []
    if not v["corrected"]:
        return requeue(uid, loop, issues, "fix pass returned no corrected digest")
    v["corrected"] = fix_math(v["corrected"])
    if errors(check(v["corrected"], units()[uid], uid)):
        return requeue(uid, loop, issues, "deterministic checks fail after fix pass")
    accept(uid, v["corrected"], "repaired", len(issues))


def latest_digest(uid, loop):
    p = OUT / f"{uid.replace('/', '__')}.p{1 if loop == 0 else 3}-{loop}.md"
    return p.read_text()


def requeue(uid, loop, issues, why):
    if loop >= MAX_LOOPS:
        state.record(uid, "needs_human", reason=why, loop=loop)
    else:
        state.record(uid, "p3_queued", reason=why, loop=loop + 1, issues=issues[:40])


def fix_online(uid, loop, digest, issues, fails):
    """Edits did not apply: ask the verifier online for the full corrected digest (reviews/gate0.md)."""
    req, _ = p2_request(uid, digest)
    req["messages"][0]["content"].append({"type": "text", "text":
        FIX_NOTE})
    resp = online(req)
    u = resp.get("usage", {})
    usd = cost(u, "online_global")
    state.add_spend(usd, "p2-online-fix", unit_id=uid, usage=usage_parts(u))
    v = parse_verdict(text_of(resp))
    if not v["corrected"]:
        return requeue(uid, loop, issues, "online fix returned no corrected digest")
    det = errors(check(v["corrected"], units()[uid], uid))
    if det:
        return requeue(uid, loop, issues, "deterministic checks fail after online fix")
    accept(uid, v["corrected"], "repaired", len(issues))


# ------------------------------------------------------------------ submit / collect

def next_pass(uid, st):
    s = (st or {}).get("state", "planned")
    if s in ("planned",):
        return "p1"
    if s == "p1_done":
        return "p2"
    if s == "p3_queued":
        return "p3"
    if s == "p2_fix_queued":
        return "p2fix"
    return None


def forecast_usd(uids, kind):
    """Planner estimate x calibration (measured / estimated on finished units; 1.5 until measured)."""
    U = units()
    est = sum(float(U[u]["est_cost_usd"] or 0) for u in uids)
    share = {"p1": 0.55, "p2": 0.45, "p3": 0.55, "p2fix": 0.6}[kind]
    done = [r for r in state.latest().values() if r.get("est_usd") and r.get("actual_usd")]
    f = (sum(r["actual_usd"] for r in done) / sum(r["est_usd"] for r in done)) if done else 1.5
    return est * share * f


def submit(wave, kind, uids, ctl):
    reqs = []
    for uid in uids:
        st = state.latest().get(uid, {})
        if kind == "p1":
            req, stats = p1_request(uid)
        elif kind == "p3":
            req, stats = p1_request(uid, issues=st.get("issues"))
        else:
            loop = st.get("loop", 0)
            digest = latest_digest(uid, loop)
            req, stats = p2_request(uid, digest)
            if kind == "p2fix":
                req["messages"][0]["content"].append({"type": "text", "text": FIX_NOTE})
            det = st.get("det_issues") or []
            if det:
                req["messages"][0]["content"].append({"type": "text", "text":
                    "Note: an automatic format checker also reported: "
                    + "; ".join(d["msg"] for d in det[:15])})
        reqs.append((uid, req, stats))
    spent = state.spent()
    fc = forecast_usd([u for u, _, _ in reqs], kind)
    inflight = sum(j.get("forecast_usd", 0) for j in jobs().values() if j.get("status") == "submitted")
    if spent + inflight + fc > ctl.get("max_spend_usd", CFG["max_spend_usd"]):
        log(f"BUDGET STOP: spent ${spent:.2f} + in flight ${inflight:.2f} + forecast ${fc:.2f} > cap")
        return None
    stamp = time.strftime("%Y%m%d-%H%M%S")
    name = f"ai4read-{wave}-{kind}-{stamp}"
    blob = f"{CFG['gcs_prefix']}/{wave}/{kind}-{stamp}/input.jsonl"
    lines = [json.dumps({"custom_id": uid.replace("/", "__"), "request": req}) for uid, req, _ in reqs]
    bucket().blob(blob).upload_from_string("\n".join(lines) + "\n")
    out = f"gs://{bucket().name}/{CFG['gcs_prefix']}/{wave}/{kind}-{stamp}/output"
    job = batch_create(name, f"gs://{bucket().name}/{blob}", out)
    job_record(job=job["name"], status="submitted", kind=kind, wave=wave, units=[u for u, _, _ in reqs],
               output=out, forecast_usd=round(fc, 4))
    loop_of = {u: state.latest().get(u, {}).get("loop", 0) for u, _, _ in reqs}
    for uid, req, stats in reqs:
        state.record(uid, "p2_submitted" if kind in ("p2", "p2fix") else "p1_submitted", kind=kind, loop=loop_of[uid],
                     batch_job_id=job["name"], content_hash=content_hash(req), spec_version=SPEC_VERSION,
                     prompt_version=PROMPT_VERSION, **stats)
    log(f"submitted {kind} for {len(reqs)} units: {job['name'].split('/')[-1]} (forecast ${fc:.2f})")
    return job


def handle_result(uid, kind, resp, price_kind, job=None):
    u = usage_parts(resp.get("usage", {}))
    usd = cost(resp.get("usage", {}), price_kind)
    state.add_spend(usd, kind, unit_id=uid, job=job, usage=u)
    rec = state.latest().get(uid, {})
    est = float(units()[uid]["est_cost_usd"] or 0) * {"p1": 0.55, "p2": 0.45, "p3": 0.55, "p2fix": 0.6}[kind]
    if price_kind == "online_global":
        est *= 2          # compare like with like: online costs twice batch
    state.record(uid, rec["state"], actual_usd=round(rec.get("actual_usd", 0) + usd, 5),
                 est_usd=round(rec.get("est_usd", 0) + est, 5),
                 **{f"{kind}_usage": u, f"{kind}_stop": resp.get("stop_reason")})
    {"p2": handle_p2, "p2fix": handle_p2fix}.get(kind, handle_p1)(uid, resp, state.latest()[uid])


def run_online(kind, uids, ctl):
    """Synchronous fallback (global endpoint, 2x batch price)."""
    for uid in uids:
        st = state.latest().get(uid, {})
        if kind == "p1":
            req, stats = p1_request(uid)
        elif kind == "p3":
            req, stats = p1_request(uid, issues=st.get("issues"))
        else:
            req, stats = p2_request(uid, latest_digest(uid, st.get("loop", 0)))
        fc = forecast_usd([uid], kind) * 2
        if state.spent() + fc > ctl.get("max_spend_usd", CFG["max_spend_usd"]):
            log("BUDGET STOP (online)")
            return
        state.record(uid, "p2_submitted" if kind == "p2" else "p1_submitted", kind=kind, loop=st.get("loop", 0),
                     batch_job_id="online", content_hash=content_hash(req), spec_version=SPEC_VERSION,
                     prompt_version=PROMPT_VERSION, **stats)
        t = time.time()
        try:
            resp = online(req)
        except Exception as e:
            log(f"  {uid} {kind} online error: {str(e)[:300]}")
            state.record(uid, {"p1": "planned", "p3": "p3_queued", "p2": "p1_done"}[kind], note=str(e)[:300])
            continue
        log(f"  {uid} {kind} online {time.time() - t:.0f}s usage={usage_parts(resp.get('usage', {}))}")
        handle_result(uid, kind, resp, "online_global", "online")


def collect():
    for jn, j in jobs().items():
        if j.get("status") != "submitted":
            continue
        info = batch_get(jn)
        st = info["state"]
        if st in ("JOB_STATE_PENDING", "JOB_STATE_RUNNING", "JOB_STATE_QUEUED"):
            continue
        log(f"job {jn.split('/')[-1]} ({j['kind']}) -> {st}")
        got = set()
        prefix = j["output"].removeprefix(f"gs://{bucket().name}/")
        for bl in bucket().list_blobs(prefix=prefix):
            # final results only; incremental_predictions/ repeats the same rows
            if not bl.name.endswith(".jsonl") or "incremental_predictions" in bl.name:
                continue
            for line in bl.download_as_text().splitlines():
                if not line.strip():
                    continue
                r = json.loads(line)
                uid = r.get("custom_id", "").replace("__", "/")
                if uid in got:
                    continue
                resp = r.get("response") or r.get("prediction") or {}
                if isinstance(resp, str):
                    try:
                        resp = json.loads(resp)
                    except json.JSONDecodeError:
                        resp = {}
                if not resp.get("content"):
                    log(f"  {uid}: no response ({str(r.get('status'))[:200]})")
                    continue
                got.add(uid)
                handle_result(uid, j["kind"], resp, "batch_us", jn)
        for uid in j["units"]:
            if uid not in got:      # failed rows go back to their previous state
                prev = {"p1": "planned", "p3": "p3_queued", "p2": "p1_done", "p2fix": "p2_fix_queued"}[j["kind"]]
                state.record(uid, prev, note=f"no result from {jn.split('/')[-1]} ({st})")
        job_record(job=jn, status="done", state=st, error=info.get("error"), n_results=len(got))


# ------------------------------------------------------------------ status

def write_status(wave, ids, ctl):
    L = state.latest()
    c = Counter(L.get(u, {}).get("state", "planned") for u in ids)
    allc = state.counts()
    running = [j for j in jobs().values() if j.get("status") == "submitted"]
    lines = [
        "# Digest pipeline — status", "",
        f"- **Wave:** `{wave}` — {len(ids)} units · " + " · ".join(f"{k} {v}" for k, v in sorted(c.items())),
        f"- **Mode:** {ctl['mode']}",
        f"- **Spent:** ${state.spent():.2f} of ${ctl['max_spend_usd']} cap",
        f"- **Jobs running:** {len(running)}" + (" (" + ", ".join(j['kind'] for j in running) + ")" if running else ""),
        f"- **All units:** " + " · ".join(f"{k} {v}" for k, v in sorted(allc.items())),
        f"- **Updated:** {time.strftime('%Y-%m-%d %H:%M')}",
    ]
    notes = PIPE / "STATUS_NOTES.md"            # hand-written notes survive the runner's rewrites
    if notes.exists():
        lines += [""] + notes.read_text().strip().splitlines()
    (PIPE / "STATUS.md").write_text("\n".join(lines) + "\n")


def commit(msg):
    subprocess.run(["git", "-C", str(REPO), "add", "pipeline/STATUS.md", "pipeline/STATUS_NOTES.md", "pipeline/state", "wiki/works",
                    str(OUT_ROOT[0])], check=False)
    r = subprocess.run(["git", "-C", str(REPO), "commit", "-qm",
                        msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"],
                       capture_output=True)
    if r.returncode == 0:
        subprocess.run(["git", "-C", str(REPO), "pull", "--rebase", "-q"], check=False)
        subprocess.run(["git", "-C", str(REPO), "push", "-q"], check=False)


# ------------------------------------------------------------------ main loop

def run(wave, once=False, sleep_s=120, use_online=False, out_dir=None):
    ONLINE_MODE[0] = use_online
    if out_dir:
        OUT_ROOT[0] = Path(out_dir).resolve()
    ids = wave_units(wave)
    last_commit = 0
    while True:
        ctl = control.read(do_pull=True)
        if ctl["mode"] == "stop":
            log("control: stop")
            break
        collect()
        L = state.latest()
        if ctl["mode"] == "run":
            busy = {u for j in jobs().values() if j.get("status") == "submitted" for u in j["units"]}
            for kind in ("p1", "p2", "p2fix", "p3"):
                if sum(1 for j in jobs().values() if j.get("status") == "submitted") >= MAX_JOBS:
                    break
                todo = [u for u in ids if u not in busy and next_pass(u, state.latest().get(u)) == kind]
                if todo and use_online:
                    run_online(kind, todo, ctl)
                    continue
                if todo:
                    if submit(wave, kind, todo, ctl) is None:
                        break
                    busy |= set(todo)
        write_status(wave, ids, ctl)
        L = state.latest()
        done = all(L.get(u, {}).get("state") in TERMINAL for u in ids)
        if time.time() - last_commit > 900 or done or once:
            commit(f"digest: {wave} status ({sum(1 for u in ids if L.get(u, {}).get('state') == 'accepted')} accepted)")
            last_commit = time.time()
        if done:
            log("wave complete")
            break
        if once:
            break
        time.sleep(sleep_s)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pipeline run")
    ap.add_argument("wave")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--sleep", type=int, default=120)
    ap.add_argument("--online", action="store_true", help="synchronous global endpoint (2x price)")
    ap.add_argument("--out", help="write accepted digests here instead of wiki/works (regression tests)")
    a = ap.parse_args(argv)
    run(a.wave, once=a.once, sleep_s=a.sleep, use_online=a.online, out_dir=a.out)


if __name__ == "__main__":
    main()

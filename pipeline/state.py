"""Append-only unit state log (pipeline/state/units.jsonl). Latest line per unit wins."""
import json
import time
from collections import Counter

from . import PIPE

LOG = PIPE / "state" / "units.jsonl"
SPEND = PIPE / "state" / "spend.jsonl"

STATES = ["planned", "p1_submitted", "p1_done", "p2_submitted", "p2_done",
          "p3_queued", "accepted", "needs_human", "skipped"]


def _append(path, rec):
    path.parent.mkdir(parents=True, exist_ok=True)
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), **rec}
    with open(path, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def record(unit_id, state, **fields):
    assert state in STATES, state
    return _append(LOG, {"unit_id": unit_id, "state": state, **fields})


def latest():
    out = {}
    if LOG.exists():
        for line in LOG.read_text().splitlines():
            if line.strip():
                r = json.loads(line)
                out[r["unit_id"]] = {**out.get(r["unit_id"], {}), **r}
    return out


def counts():
    return Counter(r["state"] for r in latest().values())


def add_spend(usd, what, **fields):
    return _append(SPEND, {"usd": round(usd, 6), "what": what, **fields})


def spent():
    if not SPEND.exists():
        return 0.0
    return sum(json.loads(l)["usd"] for l in SPEND.read_text().splitlines() if l.strip())

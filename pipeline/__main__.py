"""python -m pipeline <command>"""
import argparse

from . import state, control


def cmd_status(_):
    c = control.read(do_pull=False)
    print(f"mode: {c['mode']}  next_wave: {c.get('next_wave')}")
    print(f"spent: ${state.spent():.2f} of ${c['max_spend_usd']} cap")
    for s, n in sorted(state.counts().items()):
        print(f"  {s:14s} {n}")


def cmd_plan(_):
    import json
    from . import planner
    rows = planner.plan()
    print(json.dumps(planner.summary(rows), indent=1))


def main():
    ap = argparse.ArgumentParser(prog="pipeline")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    sub.add_parser("plan").set_defaults(fn=cmd_plan)
    r = sub.add_parser("run")
    r.add_argument("wave")
    r.add_argument("--once", action="store_true")
    r.add_argument("--sleep", type=int, default=120)
    r.set_defaults(fn=lambda a: __import__("pipeline.run", fromlist=["run"]).run(a.wave, a.once, a.sleep))
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

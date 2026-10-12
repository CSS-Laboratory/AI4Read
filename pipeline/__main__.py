"""python -m pipeline <command>"""
import argparse

from . import state, control


def cmd_status(_):
    c = control.read(do_pull=False)
    print(f"mode: {c['mode']}  next_wave: {c.get('next_wave')}")
    print(f"spent: ${state.spent():.2f} of ${c['max_spend_usd']} cap")
    for s, n in sorted(state.counts().items()):
        print(f"  {s:14s} {n}")


def main():
    ap = argparse.ArgumentParser(prog="pipeline")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

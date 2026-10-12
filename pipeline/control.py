"""Read pipeline/control.json after a git pull (DESIGN.md 'Pause / resume')."""
import json
import subprocess

from . import PIPE, REPO


def pull():
    subprocess.run(["git", "-C", str(REPO), "pull", "--ff-only", "-q"], check=False)


def read(do_pull=True):
    if do_pull:
        pull()
    return json.loads((PIPE / "control.json").read_text())

from __future__ import annotations

from bazzite_auto_switch.config import load_config
from bazzite_auto_switch.decision import decide_mode
from bazzite_auto_switch.drm import read_gpus


def run() -> int:
    gpus = read_gpus()
    config = load_config()

    mode = decide_mode(
        gpus,
        config,
    )

    print("Status")
    print()

    if mode is None:
        print("Current mode: Unknown")
    else:
        print(f"Current mode: {mode.value.capitalize()}")

    return 0

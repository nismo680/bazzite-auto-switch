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

    print(
        "Current mode:",
        mode.value.capitalize() if mode is not None else "Unknown",
    )
    print()

    print("Active displays:")
    print()

    found = False

    for gpu in gpus:
        for connector in gpu.connectors:
            if not connector.active:
                continue

            fingerprint = connector.display_fingerprint
            if fingerprint is None:
                continue

            for display in config.displays:
                if display.display_fingerprint != fingerprint:
                    continue

                found = True

                print(display.name)
                print(f"  Fingerprint: {display.display_fingerprint}")
                print(f"  Mode:        {display.mode.value.capitalize()}")
                print()

                break

    if not found:
        print("None")
        print()

    return 0

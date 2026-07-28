from __future__ import annotations

from sessionflipper.config import load_config
from sessionflipper.decision import decide_mode
from sessionflipper.drm import read_gpus
from sessionflipper.modes import Mode
from sessionflipper.session import (
    is_gamescope_running,
    is_plasma_running,
)


def run() -> int:
    config = load_config()
    gpus = read_gpus()

    desired_session = decide_mode(
        gpus,
        config,
    )

    if is_plasma_running():
        current_session = Mode.DESKTOP
    elif is_gamescope_running():
        current_session = Mode.CONSOLE
    else:
        current_session = None

    print("Status")
    print()

    print("Current session:")
    if current_session is None:
        print("  Unknown")
    else:
        print(f"  {current_session.value.capitalize()}")

    print()

    print("Desired session:")
    print(f"  {desired_session.value.capitalize()}")

    print()

    print("Automatic switching:")
    print("  Enabled" if config.automatic_switching else "  Disabled")

    print()

    print("Display settle time:")
    print(f"  {config.display_settle_time:.1f} s")

    print()

    print("Configured displays:")
    print(f"  {len(config.displays)}")

    print()

    print("Detected displays:")

    found = False

    for gpu in gpus:
        for connector in gpu.connectors:
            if connector.display_fingerprint is None:
                continue

            found = True

            print(f"  {connector.monitor_name or connector.drm_id}")
            print(f"    Fingerprint: {connector.display_fingerprint}")

    if not found:
        print("  None")

    return 0

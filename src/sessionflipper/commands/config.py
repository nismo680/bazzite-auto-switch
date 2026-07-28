from __future__ import annotations

from sessionflipper.config import load_config


def run() -> int:
    config = load_config()

    print("Configuration")
    print()

    print("Session priority:")
    print("  " + " > ".join(mode.value.capitalize() for mode in config.session_priority))
    print()

    print("Display settle time:")
    print(f"  {config.display_settle_time:.1f} seconds")
    print()

    count = len(config.displays)

    print(f"Configured display{'s' if count != 1 else ''}: {count}")
    print()

    if count == 0:
        print("No displays configured.")
        return 0

    for index, display in enumerate(config.displays, start=1):
        print(f"{index}. {display.name}")
        print(f"   Fingerprint: {display.display_fingerprint}")
        print(f"   Mode:        {display.mode.value.capitalize()}")
        print()

    return 0

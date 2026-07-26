from __future__ import annotations

from bazzite_auto_switch.config import Config, load_config, save_config
from bazzite_auto_switch.modes import Mode


def run() -> int:
    print("Preferred session priority:\n")
    print("  1) Desktop")
    print("  2) Console")
    print()

    while True:
        choice = input("> ").strip()

        if choice == "1":
            priority = (
                Mode.DESKTOP,
                Mode.CONSOLE,
            )
            break

        if choice == "2":
            priority = (
                Mode.CONSOLE,
                Mode.DESKTOP,
            )
            break

        print("Invalid selection.\n")

    config = load_config()

    save_config(
        Config(
            session_priority=priority,
            displays=config.displays,
        )
    )

    print("\nConfiguration saved.")

    return 0

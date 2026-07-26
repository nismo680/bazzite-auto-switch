from __future__ import annotations

from bazzite_auto_switch.config import Config, load_config, save_config
from bazzite_auto_switch.modes import Mode


def run() -> int:
    config = load_config()

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

    print()
    print("Display settle time (seconds)")
    print(f"Current: {config.display_settle_time}")
    print()

    while True:
        value = input("> ").strip()

        if value == "":
            display_settle_time = config.display_settle_time
            break

        try:
            display_settle_time = float(value)

            if display_settle_time <= 0:
                raise ValueError

            break

        except ValueError:
            print("Please enter a number greater than 0.\n")

    save_config(
        Config(
            session_priority=priority,
            display_settle_time=display_settle_time,
            displays=config.displays,
        )
    )

    print("\nConfiguration saved.")

    return 0

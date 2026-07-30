from __future__ import annotations

from sessionflipper.config import Config, load_config, save_config
from sessionflipper.modes import Mode


def run() -> int:
    try:
        config = load_config()

        print()
        print("Session priority:")
        print()
        print("When both Desktop and Console profiles match,")
        print("this setting determines which session is selected.")
        print()
        print("Current: " + " > ".join(mode.value.capitalize() for mode in config.session_priority))
        print()
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
        print()
        print("Time to wait after a DRM hotplug event before detecting")
        print("the current display configuration.")
        print()
        print(f"Current: {config.display_settle_time}")
        print()

        while True:
            value = input("> ").strip()

            if value == "":
                display_settle_time = config.display_settle_time
                print("No change")

                break

            try:
                display_settle_time = float(value)

                if display_settle_time <= 0:
                    raise ValueError

                break

            except ValueError:
                print("Please enter a number greater than 0.\n")

        print()
        print("Debounce time (seconds)")
        print()
        print("Time to wait after display detection before")
        print("discarding queued DRM hotplug events generated")
        print("by the session switch itself.")
        print()
        print(f"Current: {config.debounce_time}")
        print()

        while True:
            value = input("> ").strip()

            if value == "":
                debounce_time = config.debounce_time
                print("No change")
                break

            try:
                debounce_time = float(value)

                if debounce_time <= 0:
                    raise ValueError

                break

            except ValueError:
                print("Please enter a number greater than 0.\n")

        save_config(
            Config(
                session_priority=priority,
                display_settle_time=display_settle_time,
                debounce_time=debounce_time,
                displays=config.displays,
            )
        )

        print("\nConfiguration saved.")
        return 0

    except KeyboardInterrupt:
        print("\nSettings cancelled.")
        return 1

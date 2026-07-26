from __future__ import annotations

from bazzite_auto_switch.config import (
    DisplayConfig,
    load_config,
    save_config,
    update_display,
)
from bazzite_auto_switch.drm import read_gpus
from bazzite_auto_switch.modes import Mode

MODE_MAP = {
    "1": Mode.HANDHELD,
    "2": Mode.DESKTOP,
    "3": Mode.CONSOLE,
}


def select_mode() -> Mode:
    while True:
        print("Select mode:")
        print("  1) Handheld")
        print("  2) Desktop")
        print("  3) Console")
        print()

        choice = input("> ").strip()

        mode = MODE_MAP.get(choice)
        if mode is not None:
            return mode

        print("Invalid selection.\n")


def run() -> int:
    try:
        config = load_config()

        displays = [
            connector
            for gpu in read_gpus()
            for connector in gpu.connectors
            if connector.display_fingerprint is not None
        ]

        if not displays:
            print("No displays found.")
            return 1

        count = len(displays)

        print(f"Found {count} display{'s' if count != 1 else ''}.")
        print()
        print("Press Ctrl+C at any time to cancel.")
        print()

        for index, connector in enumerate(displays, start=1):
            fingerprint = connector.display_fingerprint
            assert fingerprint is not None

            print("-" * 50)
            print()
            print(f"Display {index} of {count}")
            print()

            name = connector.monitor_name or connector.drm_id

            print(f"Name:         {name}")
            print(f"Fingerprint:  {connector.display_fingerprint}")
            print()

            mode = select_mode()

            config = update_display(
                config,
                DisplayConfig(
                    display_fingerprint=fingerprint,
                    name=name,
                    mode=mode,
                ),
            )

            print()

        save_config(config)

        print("Configuration saved.")

        return 0

    except KeyboardInterrupt:
        print("\nSetup cancelled.")
        return 1

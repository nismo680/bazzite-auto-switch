from __future__ import annotations

import time

from sessionflipper.config import load_config
from sessionflipper.events import DisplayEvents
from sessionflipper.once import once


def run() -> int:
    print("============================================================")
    print("SessionFlipper daemon")
    print("============================================================")

    events = DisplayEvents()

    while True:
        print()
        print("Waiting for DRM hotplug event...")

        events.wait()

        print()
        print("Reloading configuration...")
        config = load_config()

        print(f"Display settle time : {config.display_settle_time:.1f} s")
        print("Waiting...")
        time.sleep(config.display_settle_time)

        print()
        print("Running display detection...")

        try:
            once()
            print("Display detection finished.")
        except Exception:
            import traceback

            traceback.print_exc()

    return 0

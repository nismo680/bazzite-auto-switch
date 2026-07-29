from __future__ import annotations

import time
import traceback

from sessionflipper.config import load_config
from sessionflipper.debug import debug_print
from sessionflipper.events import DisplayEvents
from sessionflipper.once import once


def run(
    debug: bool = False,
    run_once: bool = False,
) -> int:
    if debug:
        print("============================================================")
        print("SessionFlipper daemon")
        print("============================================================")

    events = DisplayEvents(
        debug=debug,
    )
    try:
        while True:
            if not run_once:
                if debug:
                    print()
                    debug_print("Waiting for DRM hotplug event...")

                events.wait()

            if debug:
                print()
                print("Reloading configuration...")

            config = load_config()

            if debug:
                print(f"Display settle time : {config.display_settle_time:.1f} s")
                print("Waiting...")

            time.sleep(config.display_settle_time)

            if debug:
                print()
                print("Running display detection...")

            try:
                switched = once(debug=debug)

                if switched:
                    print("Switch")

                if debug:
                    print(f"Ignoring DRM events for {config.debounce_time:.1f} s...")

                time.sleep(config.debounce_time)

                if debug:
                    print("Display detection finished.")

            except Exception:
                traceback.print_exc()

            if run_once:
                break

    except KeyboardInterrupt:
        if debug:
            print()
            print("Daemon stopped.")

    return 0

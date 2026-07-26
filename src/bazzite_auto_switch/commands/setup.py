from __future__ import annotations

from bazzite_auto_switch.drm import read_gpus


def run() -> int:
    print("Found displays:\n")

    found = False

    for gpu in read_gpus():
        for connector in gpu.connectors:
            if connector.display_fingerprint is None:
                continue

            found = True

            name = connector.monitor_name or connector.drm_id

            print(name)
            print(f"Fingerprint: {connector.display_fingerprint}")
            print()

    if not found:
        print("No displays found.")

    return 0

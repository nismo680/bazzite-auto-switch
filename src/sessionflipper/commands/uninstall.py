from __future__ import annotations

from sessionflipper.systemd import (
    daemon_reload,
    disable_service,
    remove_service,
)


def run() -> int:
    disable_service()
    remove_service()
    daemon_reload()

    print("Service removed.")

    return 0

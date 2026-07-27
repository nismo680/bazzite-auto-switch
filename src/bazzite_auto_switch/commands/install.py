from __future__ import annotations

from bazzite_auto_switch.systemd import (
    daemon_reload,
    enable_service,
    write_service,
)


def run() -> int:
    write_service()
    daemon_reload()
    enable_service()

    print("Service installed and started.")

    return 0

from __future__ import annotations

import subprocess
from pathlib import Path

SERVICE_NAME = "sessionflipper.service"


def service_path() -> Path:
    return Path.home() / ".config/systemd/user" / SERVICE_NAME


def write_service() -> None:
    path = service_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    path.write_text(
        """[Unit]
Description=Bazzite Auto Switch

[Service]
Type=simple
ExecStart=sessionflipper daemon
Restart=on-failure

[Install]
WantedBy=default.target
""",
        encoding="utf-8",
    )


def remove_service() -> None:
    path = service_path()

    if path.exists():
        path.unlink()


def daemon_reload() -> None:
    subprocess.run(
        ["systemctl", "--user", "daemon-reload"],
        check=True,
    )


def enable_service() -> None:
    subprocess.run(
        ["systemctl", "--user", "enable", "--now", SERVICE_NAME],
        check=True,
    )


def disable_service() -> None:
    subprocess.run(
        ["systemctl", "--user", "disable", "--now", SERVICE_NAME],
        check=True,
    )

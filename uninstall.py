#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

INSTALL_DIR = Path.home() / ".local" / "share" / "sessionflipper"
LOCAL_BIN = Path.home() / ".local" / "bin"
SYSTEMD_DIR = Path.home() / ".config" / "systemd" / "user"

LAUNCHER = LOCAL_BIN / "sessionflipper"
SERVICE = SYSTEMD_DIR / "sessionflipper.service"


def run(*args: str) -> None:
    subprocess.run(
        args,
        check=False,
    )


def main() -> int:
    print("Removing SessionFlipper...")

    print("Stopping systemd service...")
    run(
        "systemctl",
        "--user",
        "disable",
        "--now",
        "sessionflipper.service",
    )

    if SERVICE.exists():
        SERVICE.unlink()
        print(f"Removed {SERVICE}")

    print("Reloading systemd...")
    run(
        "systemctl",
        "--user",
        "daemon-reload",
    )

    if LAUNCHER.exists():
        LAUNCHER.unlink()
        print(f"Removed {LAUNCHER}")

    if INSTALL_DIR.exists():
        shutil.rmtree(INSTALL_DIR)
        print(f"Removed {INSTALL_DIR}")

    print()
    print("SessionFlipper has been uninstalled.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

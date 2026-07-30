#!/usr/bin/env python3

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

INSTALL_DIR = Path.home() / ".local" / "share" / "sessionflipper"

EXCLUDE = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
}


def ignore(directory: str, names: list[str]) -> set[str]:
    ignored: set[str] = set()

    for name in names:
        if name in EXCLUDE:
            ignored.add(name)
            continue

        if name.endswith(".pyc"):
            ignored.add(name)

    return ignored


def main() -> int:

    source = Path(__file__).resolve().parent

    print(f"Installing to {INSTALL_DIR}")

    if INSTALL_DIR.exists():
        shutil.rmtree(INSTALL_DIR)

    shutil.copytree(
        source,
        INSTALL_DIR,
        ignore=ignore,
    )

    print("Project copied successfully.")

    venv = INSTALL_DIR / ".venv"

    print("Creating virtual environment...")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "venv",
            str(venv),
        ],
        check=True,
    )

    python = venv / "bin" / "python"

    print("Installing SessionFlipper...")

    subprocess.run(
        [
            str(python),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
        ],
        check=True,
    )

    subprocess.run(
        [
            str(python),
            "-m",
            "pip",
            "install",
            ".",
        ],
        cwd=INSTALL_DIR,
        check=True,
    )

    LOCAL_BIN = Path.home() / ".local" / "bin"

    LOCAL_BIN.mkdir(
        parents=True,
        exist_ok=True,
    )

    launcher = LOCAL_BIN / "sessionflipper"

    launcher.write_text(
        f"""#!/bin/sh
    exec "{INSTALL_DIR}/.venv/bin/sessionflipper" "$@"
    """,
        encoding="utf-8",
    )

    launcher.chmod(0o755)

    print(f"Installed launcher: {launcher}")

    SYSTEMD_DIR = Path.home() / ".config" / "systemd" / "user"

    SYSTEMD_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    service = SYSTEMD_DIR / "sessionflipper.service"

    service.write_text(
        f"""[Unit]
    Description=SessionFlipper daemon
    After=graphical-session.target

    [Service]
    Type=simple
    ExecStart={LOCAL_BIN}/sessionflipper daemon
    Restart=on-failure
    RestartSec=2

    [Install]
    WantedBy=default.target
    """,
        encoding="utf-8",
    )

    print(f"Installed service: {service}")

    print("Reloading systemd...")

    subprocess.run(
        [
            "systemctl",
            "--user",
            "daemon-reload",
        ],
        check=True,
    )

    subprocess.run(
        [
            "systemctl",
            "--user",
            "enable",
            "--now",
            "sessionflipper.service",
        ],
        check=True,
    )

    print()
    print("Installation completed successfully.")
    print()
    print("Verify")
    print("  systemctl --user status sessionflipper.service")
    print("  sessionflipper --help")
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

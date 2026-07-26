from __future__ import annotations

import subprocess


def is_plasma_running() -> bool:
    return (
        subprocess.run(
            ["pgrep", "-x", "kwin_wayland"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def is_gamescope_running() -> bool:
    return (
        subprocess.run(
            ["pgrep", "-x", "gamescope-wl"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        ).returncode
        == 0
    )


def switch_to_desktop() -> None:
    subprocess.run(
        ["steamos-session-select", "plasma"],
        check=True,
    )


def switch_to_console() -> None:
    subprocess.run(
        ["steamos-session-select", "gamescope"],
        check=True,
    )

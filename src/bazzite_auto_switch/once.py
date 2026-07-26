from __future__ import annotations

from bazzite_auto_switch.config import load_config
from bazzite_auto_switch.decision import decide_mode
from bazzite_auto_switch.drm import read_gpus
from bazzite_auto_switch.modes import Mode
from bazzite_auto_switch.session import (
    is_gamescope_running,
    is_plasma_running,
    switch_to_console,
    switch_to_desktop,
)


def run() -> int:
    gpus = read_gpus()
    config = load_config()

    desired_mode = decide_mode(
        gpus,
        config,
    )

    if desired_mode is Mode.DESKTOP:
        if not is_plasma_running():
            switch_to_desktop()

    elif desired_mode is Mode.CONSOLE:
        if not is_gamescope_running():
            switch_to_console()

    return 0

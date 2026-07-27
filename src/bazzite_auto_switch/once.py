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

    if not config.automatic_switching:
        return 0

    desired_session = decide_mode(
        gpus,
        config,
    )

    match desired_session:
        case Mode.DESKTOP:
            if is_plasma_running():
                return 0

            switch_to_desktop()

        case Mode.CONSOLE:
            if is_gamescope_running():
                return 0

            switch_to_console()

    return 0

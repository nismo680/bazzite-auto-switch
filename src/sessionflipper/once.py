from __future__ import annotations

from sessionflipper.config import load_config
from sessionflipper.decision import decide_mode
from sessionflipper.drm import read_gpus
from sessionflipper.modes import Mode
from sessionflipper.session import (
    is_gamescope_running,
    is_plasma_running,
    switch_to_console,
    switch_to_desktop,
)


def once(
    debug: bool = False,
    dry_run: bool = False,
) -> bool:
    gpus = read_gpus()
    config = load_config()

    if not config.automatic_switching:
        return False

    desired_session = decide_mode(
        gpus,
        config,
    )
    if debug:
        print(f"Desired mode: {desired_session.name}")

    match desired_session:
        case Mode.DESKTOP:
            if is_plasma_running():
                if debug:
                    print("Already in DESKTOP mode.")
                return False

            print("Switching to DESKTOP.")

            if dry_run:
                return False

            switch_to_desktop()
            return True

        case Mode.CONSOLE:
            if is_gamescope_running():
                if debug:
                    print("Already in CONSOLE mode.")
                return False

            print("Switching to CONSOLE.")

            if dry_run:
                return False

            switch_to_console()
            return True

    return False

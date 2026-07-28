from __future__ import annotations

from sessionflipper.config import Config
from sessionflipper.models import GPU
from sessionflipper.modes import Mode


def get_active_modes(
    gpus: tuple[GPU, ...],
    config: Config,
) -> set[Mode]:
    active_modes: set[Mode] = set()

    for gpu in gpus:
        for connector in gpu.connectors:
            if not connector.active:
                continue

            fingerprint = connector.display_fingerprint
            if fingerprint is None:
                continue

            for display in config.displays:
                if display.display_fingerprint != fingerprint:
                    continue

                if display.mode is Mode.UNCONFIGURED:
                    break

                active_modes.add(display.mode)
                break

    return active_modes


def decide_mode(
    gpus: tuple[GPU, ...],
    config: Config,
) -> Mode:
    """Return the preferred mode for the active displays."""

    active_modes = get_active_modes(gpus, config)

    for mode in config.session_priority:
        if mode in active_modes:
            return mode

    return config.session_priority[0]

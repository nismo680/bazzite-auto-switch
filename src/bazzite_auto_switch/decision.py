from __future__ import annotations

from dataclasses import dataclass

from bazzite_auto_switch.models import GPU
from bazzite_auto_switch.modes import Mode


@dataclass(slots=True, frozen=True)
class Decision:
    mode: Mode
    reason: str


def decide(gpus: tuple[GPU, ...]) -> Decision:
    """
    Determine the desired operating mode.

    Currently:
    - no active external display -> HANDHELD
    - active external display -> not implemented
    """
    for gpu in gpus:
        for connector in gpu.connectors:
            if not connector.active:
                continue

            if connector.connector_type.name != "EDP":
                raise NotImplementedError("External display handling not implemented yet.")

    return Decision(
        mode=Mode.HANDHELD,
        reason="no_active_external_display",
    )

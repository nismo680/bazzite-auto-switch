from __future__ import annotations

from dataclasses import dataclass

from bazzite_auto_switch.modes import Mode


@dataclass(slots=True, frozen=True)
class Decision:
    mode: Mode
    reason: str

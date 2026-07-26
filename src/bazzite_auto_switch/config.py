from __future__ import annotations

from dataclasses import dataclass, field

from bazzite_auto_switch.modes import Mode


@dataclass(slots=True, frozen=True)
class DisplayConfig:
    display_fingerprint: str
    mode: Mode
    priority: int


@dataclass(slots=True, frozen=True)
class Config:
    displays: tuple[DisplayConfig, ...] = field(default_factory=tuple)

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

from bazzite_auto_switch.modes import Mode

CONFIG_DIR = Path.home() / ".config" / "bazzite-auto-switch"
CONFIG_FILE = CONFIG_DIR / "config.yaml"


@dataclass(slots=True, frozen=True)
class DisplayConfig:
    display_fingerprint: str
    mode: Mode
    priority: int


@dataclass(slots=True, frozen=True)
class Config:
    displays: tuple[DisplayConfig, ...] = field(default_factory=tuple)


def load_config() -> Config:
    if not CONFIG_FILE.exists():
        return Config()

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    displays: list[DisplayConfig] = []

    for fingerprint, values in data.get("displays", {}).items():
        displays.append(
            DisplayConfig(
                display_fingerprint=fingerprint,
                mode=Mode(values["mode"]),
                priority=int(values["priority"]),
            )
        )

    return Config(tuple(displays))


def save_config(config: Config) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "displays": {
            display.display_fingerprint: {
                "mode": display.mode.value,
                "priority": display.priority,
            }
            for display in config.displays
        }
    }

    with CONFIG_FILE.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            sort_keys=False,
        )

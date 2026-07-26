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
    name: str
    mode: Mode


@dataclass(slots=True, frozen=True)
class Config:
    mode_priority: tuple[Mode, ...] = (
        Mode.DESKTOP,
        Mode.CONSOLE,
    )
    displays: tuple[DisplayConfig, ...] = field(default_factory=tuple)


def load_config() -> Config:
    if not CONFIG_FILE.exists():
        return Config()

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    mode_priority = tuple(
        Mode(mode)
        for mode in data.get(
            "preferences",
            {},
        ).get(
            "mode_priority",
            [
                "desktop",
                "console",
                "handheld",
            ],
        )
    )

    displays: list[DisplayConfig] = []

    for fingerprint, values in data.get("displays", {}).items():
        displays.append(
            DisplayConfig(
                display_fingerprint=fingerprint,
                name=values["name"],
                mode=Mode(values["mode"]),
            )
        )

    return Config(
        mode_priority=mode_priority,
        displays=tuple(displays),
    )


def save_config(config: Config) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "preferences": {"mode_priority": [mode.value for mode in config.mode_priority]},
        "displays": {
            display.display_fingerprint: {
                "name": display.name,
                "mode": display.mode.value,
            }
            for display in config.displays
        },
    }

    tmp = CONFIG_FILE.with_suffix(".tmp")

    with tmp.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            data,
            file,
            sort_keys=False,
        )

    tmp.replace(CONFIG_FILE)


def update_display(
    config: Config,
    display: DisplayConfig,
) -> Config:
    displays = [d for d in config.displays if d.display_fingerprint != display.display_fingerprint]

    displays.append(display)

    return Config(
        mode_priority=config.mode_priority,
        displays=tuple(displays),
    )

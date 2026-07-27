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
    automatic_switching: bool = True
    session_priority: tuple[Mode, ...] = (
        Mode.DESKTOP,
        Mode.CONSOLE,
    )
    display_settle_time: float = 2.0
    displays: tuple[DisplayConfig, ...] = field(default_factory=tuple)


def load_config() -> Config:
    if not CONFIG_FILE.exists():
        return Config()

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}

    preferences = data.get("preferences", {})

    automatic_switching = bool(
        preferences.get(
            "automatic_switching",
            True,
        )
    )

    session_priority = tuple(
        Mode(mode)
        for mode in preferences.get(
            "session_priority",
            [
                "desktop",
                "console",
            ],
        )
    )

    display_settle_time = float(
        preferences.get(
            "display_settle_time",
            2.0,
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
        automatic_switching=automatic_switching,
        session_priority=session_priority,
        display_settle_time=display_settle_time,
        displays=tuple(displays),
    )


def save_config(config: Config) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    data = {
        "preferences": {
            "automatic_switching": config.automatic_switching,
            "session_priority": [mode.value for mode in config.session_priority],
            "display_settle_time": config.display_settle_time,
        },
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
        automatic_switching=config.automatic_switching,
        session_priority=config.session_priority,
        display_settle_time=config.display_settle_time,
        displays=tuple(displays),
    )


def set_automatic_switching(
    config: Config,
    enabled: bool,
) -> Config:
    return Config(
        automatic_switching=enabled,
        session_priority=config.session_priority,
        display_settle_time=config.display_settle_time,
        displays=config.displays,
    )


def set_session_priority(
    config: Config,
    session_priority: tuple[Mode, ...],
) -> Config:
    return Config(
        automatic_switching=config.automatic_switching,
        session_priority=session_priority,
        display_settle_time=config.display_settle_time,
        displays=config.displays,
    )


def set_display_settle_time(
    config: Config,
    display_settle_time: float,
) -> Config:
    return Config(
        automatic_switching=config.automatic_switching,
        session_priority=config.session_priority,
        display_settle_time=display_settle_time,
        displays=config.displays,
    )

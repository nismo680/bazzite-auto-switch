"""
Functions for discovering DRM devices.
"""

from __future__ import annotations

from pathlib import Path

DRM_PATH = Path("/sys/class/drm")

_STATUS_MAP: dict[str, bool | None] = {
    "connected": True,
    "disconnected": False,
    "unknown": None,
}

_ENABLED_MAP: dict[str, bool | None] = {
    "enabled": True,
    "disabled": False,
}


def find_drm_cards(base_path: Path = DRM_PATH) -> tuple[Path, ...]:
    """
    Return all DRM card directories.
    """
    if not base_path.exists():
        return ()

    return tuple(
        sorted(
            entry
            for entry in base_path.iterdir()
            if entry.is_dir() and entry.name.startswith("card") and "-" not in entry.name
        )
    )


def find_connectors(card: Path) -> tuple[Path, ...]:
    """
    Return all connector directories belonging to a DRM card.
    """
    drm_path = card.parent
    prefix = f"{card.name}-"

    return tuple(
        sorted(
            entry
            for entry in drm_path.iterdir()
            if entry.is_dir() and entry.name.startswith(prefix)
        )
    )


def read_text(path: Path, filename: str) -> str | None:
    """
    Read a text file below *path*.

    Returns None if the file does not exist or cannot be read.
    """
    try:
        return (path / filename).read_text(encoding="utf-8").strip()
    except OSError:
        return None


def _read_mapped_value(
    path: Path,
    filename: str,
    mapping: dict[str, bool | None],
) -> bool | None:
    """
    Read a sysfs attribute and map its value.
    """
    value = read_text(path, filename)

    if value is None:
        return None

    return mapping.get(value)


def read_status(connector: Path) -> bool | None:
    """
    Return the connector status.
    """
    return _read_mapped_value(connector, "status", _STATUS_MAP)


def read_enabled(connector: Path) -> bool | None:
    """
    Return whether the connector is enabled.
    """
    return _read_mapped_value(connector, "enabled", _ENABLED_MAP)

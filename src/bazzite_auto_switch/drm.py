"""
Functions for discovering DRM devices.
"""

from __future__ import annotations

from pathlib import Path

DRM_PATH = Path("/sys/class/drm")


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

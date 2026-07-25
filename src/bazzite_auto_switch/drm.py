"""
Functions for discovering DRM devices.
"""

from __future__ import annotations

from pathlib import Path

DRM_PATH = Path("/sys/class/drm")


def find_drm_cards(base_path: Path = DRM_PATH) -> tuple[Path, ...]:
    """
    Return all DRM card directories.

    Example:
        (
            Path("/sys/class/drm/card0"),
            Path("/sys/class/drm/card1"),
        )
    """
    if not base_path.exists():
        return ()

    cards = tuple(
        sorted(
            entry
            for entry in base_path.iterdir()
            if entry.is_dir() and entry.name.startswith("card") and "-" not in entry.name
        )
    )

    return cards

"""
EDID parsing.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class MonitorInfo:
    """Information extracted from an EDID."""

    manufacturer: str | None = None
    monitor_name: str | None = None

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


def decode_manufacturer(raw: bytes) -> str:
    """
    Decode the 2-byte EDID manufacturer ID.

    Returns the three-letter PNP identifier.
    """
    if len(raw) != 2:
        raise ValueError("Manufacturer ID must be exactly 2 bytes.")

    value = int.from_bytes(raw, byteorder="big")

    return "".join(chr(((value >> shift) & 0x1F) + ord("A") - 1) for shift in (10, 5, 0))

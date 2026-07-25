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


def parse_monitor_name(edid: bytes) -> str | None:
    """
    Extract the monitor name from an EDID.

    Returns None if no monitor name descriptor is present.
    """
    if len(edid) < 128:
        raise ValueError("EDID must be at least 128 bytes.")

    for offset in range(54, 126, 18):
        descriptor = edid[offset : offset + 18]

        if descriptor[:3] != b"\x00\x00\x00":
            continue

        if descriptor[3] != 0xFC:
            continue

        name = descriptor[5:18]
        return name.rstrip(b" \x00\n").decode("ascii", errors="replace").strip()

    return None


def parse_edid(edid: bytes) -> MonitorInfo:
    """
    Parse the information needed from an EDID.
    """
    if len(edid) < 128:
        raise ValueError("EDID must be at least 128 bytes.")

    return MonitorInfo(
        manufacturer=decode_manufacturer(edid[8:10]),
        monitor_name=parse_monitor_name(edid),
    )

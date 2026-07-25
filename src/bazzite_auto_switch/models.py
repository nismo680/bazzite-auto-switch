"""
Immutable data models used throughout Bazzite Auto Switch.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ConnectorType(StrEnum):
    INTERNAL = "internal"
    DISPLAYPORT = "displayport"
    HDMI = "hdmi"
    DVI = "dvi"
    VGA = "vga"
    USB_C = "usb-c"
    UNKNOWN = "unknown"


@dataclass(slots=True, frozen=True)
class Connector:
    """Represents a single display connector."""

    drm_id: str
    connector_type: ConnectorType
    number: int

    connected: bool | None
    enabled: bool | None

    monitor_name: str | None = None
    manufacturer: str | None = None
    serial_number: str | None = None

    @property
    def active(self) -> bool:
        return self.connected is True and self.enabled is True


@dataclass(slots=True, frozen=True)
class GPU:
    """Represents one graphics adapter."""

    drm_id: str
    name: str

    connectors: tuple[Connector, ...] = field(default_factory=tuple)

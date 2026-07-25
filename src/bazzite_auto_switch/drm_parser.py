"""
Helper functions for parsing DRM connector names.
"""

from __future__ import annotations

from bazzite_auto_switch.models import ConnectorType


def parse_connector_name(name: str) -> tuple[ConnectorType, int]:
    """
    Parse a DRM connector name.

    Examples:
        card0-DP-1      -> (DISPLAYPORT, 1)
        card0-HDMI-A-1  -> (HDMI, 1)
        card1-eDP-1     -> (INTERNAL, 1)
    """
    connector = name.split("-", 1)[1]

    if connector.startswith("eDP-"):
        return ConnectorType.INTERNAL, int(connector[4:])

    if connector.startswith("DP-"):
        return ConnectorType.DISPLAYPORT, int(connector[3:])

    if connector.startswith("HDMI-A-"):
        return ConnectorType.HDMI, int(connector[7:])

    if connector.startswith("DVI-"):
        return ConnectorType.DVI, int(connector[4:])

    if connector.startswith("VGA-"):
        return ConnectorType.VGA, int(connector[4:])

    return ConnectorType.UNKNOWN, 0

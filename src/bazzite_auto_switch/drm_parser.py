"""
Helper functions for parsing DRM connector names.
"""

from __future__ import annotations

from bazzite_auto_switch.models import ConnectorType

_CONNECTOR_TYPES: dict[str, ConnectorType] = {
    "DP": ConnectorType.DISPLAYPORT,
    "HDMI-A": ConnectorType.HDMI,
    "HDMI-B": ConnectorType.HDMI,
    "eDP": ConnectorType.INTERNAL,
    "LVDS": ConnectorType.INTERNAL,
    "DSI": ConnectorType.INTERNAL,
    "DVI": ConnectorType.DVI,
    "DVI-D": ConnectorType.DVI,
    "DVI-I": ConnectorType.DVI,
    "DVI-A": ConnectorType.DVI,
    "VGA": ConnectorType.VGA,
}


def parse_connector_name(name: str) -> tuple[ConnectorType, int]:
    """
    Parse a DRM connector name.

    Examples:
        >>> parse_connector_name("card0-DP-1")
        (<ConnectorType.DISPLAYPORT: 'displayport'>, 1)

        >>> parse_connector_name("card0-HDMI-A-2")
        (<ConnectorType.HDMI: 'hdmi'>, 2)

        >>> parse_connector_name("card1-eDP-1")
        (<ConnectorType.INTERNAL: 'internal'>, 1)
    """
    try:
        connector = name.split("-", 1)[1]
    except IndexError:
        return ConnectorType.UNKNOWN, 0

    connector_name, _, connector_number = connector.rpartition("-")

    try:
        number = int(connector_number)
    except ValueError:
        return ConnectorType.UNKNOWN, 0

    connector_type = _CONNECTOR_TYPES.get(
        connector_name,
        ConnectorType.UNKNOWN,
    )

    return connector_type, number

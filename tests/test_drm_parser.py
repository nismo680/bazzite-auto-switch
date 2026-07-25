from bazzite_auto_switch.drm_parser import parse_connector_name
from bazzite_auto_switch.models import ConnectorType


def test_parse_displayport() -> None:
    connector_type, number = parse_connector_name("card0-DP-1")

    assert connector_type is ConnectorType.DISPLAYPORT
    assert number == 1


def test_parse_hdmi() -> None:
    connector_type, number = parse_connector_name("card0-HDMI-A-2")

    assert connector_type is ConnectorType.HDMI
    assert number == 2


def test_parse_internal() -> None:
    connector_type, number = parse_connector_name("card1-eDP-1")

    assert connector_type is ConnectorType.INTERNAL
    assert number == 1


def test_parse_unknown() -> None:
    connector_type, number = parse_connector_name("card0-FOO-1")

    assert connector_type is ConnectorType.UNKNOWN
    assert number == 0

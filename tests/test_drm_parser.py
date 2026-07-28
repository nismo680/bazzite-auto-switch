from sessionflipper.drm_parser import parse_connector_name
from sessionflipper.models import ConnectorType


def test_parse_displayport() -> None:
    connector_type, number = parse_connector_name("card0-DP-1")

    assert connector_type is ConnectorType.DISPLAYPORT
    assert number == 1


def test_parse_hdmi_a() -> None:
    connector_type, number = parse_connector_name("card0-HDMI-A-2")

    assert connector_type is ConnectorType.HDMI
    assert number == 2


def test_parse_hdmi_b() -> None:
    connector_type, number = parse_connector_name("card0-HDMI-B-1")

    assert connector_type is ConnectorType.HDMI
    assert number == 1


def test_parse_internal_edp() -> None:
    connector_type, number = parse_connector_name("card1-eDP-1")

    assert connector_type is ConnectorType.INTERNAL
    assert number == 1


def test_parse_internal_lvds() -> None:
    connector_type, number = parse_connector_name("card0-LVDS-1")

    assert connector_type is ConnectorType.INTERNAL
    assert number == 1


def test_parse_dvi() -> None:
    connector_type, number = parse_connector_name("card0-DVI-D-1")

    assert connector_type is ConnectorType.DVI
    assert number == 1


def test_parse_vga() -> None:
    connector_type, number = parse_connector_name("card0-VGA-1")

    assert connector_type is ConnectorType.VGA
    assert number == 1


def test_parse_unknown() -> None:
    connector_type, number = parse_connector_name("card0-FOO-1")

    assert connector_type is ConnectorType.UNKNOWN
    assert number == 1


def test_parse_invalid_name() -> None:
    connector_type, number = parse_connector_name("invalid")

    assert connector_type is ConnectorType.UNKNOWN
    assert number == 0

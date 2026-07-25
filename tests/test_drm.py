from pathlib import Path

from bazzite_auto_switch.drm import (
    find_connectors,
    find_drm_cards,
    read_connector,
    read_enabled,
    read_status,
    read_text,
)
from bazzite_auto_switch.models import ConnectorType


def test_find_drm_cards_empty(tmp_path: Path) -> None:
    assert find_drm_cards(tmp_path) == ()


def test_find_single_card(tmp_path: Path) -> None:
    (tmp_path / "card0").mkdir()

    assert find_drm_cards(tmp_path) == (tmp_path / "card0",)


def test_find_multiple_cards(tmp_path: Path) -> None:
    (tmp_path / "card1").mkdir()
    (tmp_path / "card0").mkdir()

    assert find_drm_cards(tmp_path) == (
        tmp_path / "card0",
        tmp_path / "card1",
    )


def test_ignore_non_cards(tmp_path: Path) -> None:
    (tmp_path / "card0").mkdir()
    (tmp_path / "card0-DP-1").mkdir()
    (tmp_path / "renderD128").mkdir()

    assert find_drm_cards(tmp_path) == (tmp_path / "card0",)


def test_find_connectors_empty(tmp_path: Path) -> None:
    card = tmp_path / "card0"
    card.mkdir()

    assert find_connectors(card) == ()


def test_find_connectors(tmp_path: Path) -> None:
    card = tmp_path / "card0"
    card.mkdir()

    dp = tmp_path / "card0-DP-1"
    hdmi = tmp_path / "card0-HDMI-A-1"

    dp.mkdir()
    hdmi.mkdir()

    (tmp_path / "card1").mkdir()
    (tmp_path / "card1-DP-1").mkdir()
    (tmp_path / "renderD128").mkdir()

    assert find_connectors(card) == (
        dp,
        hdmi,
    )


def test_read_text(tmp_path: Path) -> None:
    (tmp_path / "status").write_text("connected\n")

    assert read_text(tmp_path, "status") == "connected"


def test_read_text_missing_file(tmp_path: Path) -> None:
    assert read_text(tmp_path, "status") is None


def test_read_status_connected(tmp_path: Path) -> None:
    (tmp_path / "status").write_text("connected\n")

    assert read_status(tmp_path) is True


def test_read_status_disconnected(tmp_path: Path) -> None:
    (tmp_path / "status").write_text("disconnected\n")

    assert read_status(tmp_path) is False


def test_read_status_unknown(tmp_path: Path) -> None:
    (tmp_path / "status").write_text("unknown\n")

    assert read_status(tmp_path) is None


def test_read_enabled_enabled(tmp_path: Path) -> None:
    (tmp_path / "enabled").write_text("enabled\n")

    assert read_enabled(tmp_path) is True


def test_read_enabled_disabled(tmp_path: Path) -> None:
    (tmp_path / "enabled").write_text("disabled\n")

    assert read_enabled(tmp_path) is False


def test_read_enabled_missing(tmp_path: Path) -> None:
    assert read_enabled(tmp_path) is None


def test_read_connector(tmp_path: Path) -> None:
    (tmp_path / "status").write_text("connected\n")
    (tmp_path / "enabled").write_text("enabled\n")

    connector = read_connector(tmp_path)

    assert connector.drm_id == tmp_path.name
    assert connector.connector_type is ConnectorType.UNKNOWN
    assert connector.connected is True
    assert connector.enabled is True
    assert connector.active is True

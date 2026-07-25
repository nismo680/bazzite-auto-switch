from pathlib import Path

from bazzite_auto_switch.drm import find_connectors, find_drm_cards


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

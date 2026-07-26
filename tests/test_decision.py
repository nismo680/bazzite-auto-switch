from __future__ import annotations

from bazzite_auto_switch.config import Config, DisplayConfig
from bazzite_auto_switch.decision import decide_mode
from bazzite_auto_switch.models import GPU, Connector, ConnectorType
from bazzite_auto_switch.modes import Mode


def make_connector(
    fingerprint: str | None,
    *,
    connected: bool = True,
    enabled: bool = True,
) -> Connector:
    return Connector(
        drm_id="card0-DP-1",
        connector_type=ConnectorType.DISPLAYPORT,
        number=1,
        connected=connected,
        enabled=enabled,
        display_fingerprint=fingerprint,
        manufacturer=None,
        monitor_name=None,
    )


def make_gpu(*connectors: Connector) -> GPU:
    return GPU(
        drm_id="card0",
        name="GPU",
        connectors=connectors,
    )


def make_display(
    fingerprint: str,
    mode: Mode,
    name: str = "Monitor",
) -> DisplayConfig:
    return DisplayConfig(
        display_fingerprint=fingerprint,
        name=name,
        mode=mode,
    )


def test_no_active_displays_fall_back_to_priority() -> None:
    gpu = make_gpu()

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_desktop_display_is_selected() -> None:
    gpu = make_gpu(make_connector("desktop"))

    config = Config(
        displays=(make_display("desktop", Mode.DESKTOP),),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_console_display_is_selected() -> None:
    gpu = make_gpu(make_connector("console"))

    config = Config(
        displays=(make_display("console", Mode.CONSOLE),),
    )

    assert decide_mode((gpu,), config) is Mode.CONSOLE


def test_unconfigured_display_falls_back_to_priority() -> None:
    gpu = make_gpu(make_connector("internal"))

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
        displays=(make_display("internal", Mode.UNCONFIGURED),),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_desktop_has_priority_over_console() -> None:
    gpu = make_gpu(
        make_connector("desktop"),
        make_connector("console"),
    )

    config = Config(
        displays=(
            make_display("desktop", Mode.DESKTOP),
            make_display("console", Mode.CONSOLE),
        ),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_console_has_priority_when_configured() -> None:
    gpu = make_gpu(
        make_connector("desktop"),
        make_connector("console"),
    )

    config = Config(
        session_priority=(
            Mode.CONSOLE,
            Mode.DESKTOP,
        ),
        displays=(
            make_display("desktop", Mode.DESKTOP),
            make_display("console", Mode.CONSOLE),
        ),
    )

    assert decide_mode((gpu,), config) is Mode.CONSOLE


def test_unknown_display_falls_back_to_priority() -> None:
    gpu = make_gpu(make_connector("unknown"))

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_disconnected_display_falls_back_to_priority() -> None:
    gpu = make_gpu(
        make_connector(
            "desktop",
            connected=False,
        )
    )

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
        displays=(make_display("desktop", Mode.DESKTOP),),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_disabled_display_falls_back_to_priority() -> None:
    gpu = make_gpu(
        make_connector(
            "desktop",
            enabled=False,
        )
    )

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
        displays=(make_display("desktop", Mode.DESKTOP),),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP


def test_display_without_fingerprint_falls_back_to_priority() -> None:
    gpu = make_gpu(make_connector(None))

    config = Config(
        session_priority=(
            Mode.DESKTOP,
            Mode.CONSOLE,
        ),
        displays=(make_display("desktop", Mode.DESKTOP),),
    )

    assert decide_mode((gpu,), config) is Mode.DESKTOP

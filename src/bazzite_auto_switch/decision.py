from __future__ import annotations

from dataclasses import dataclass

from bazzite_auto_switch.models import GPU, Connector, ConnectorType
from bazzite_auto_switch.modes import Mode


@dataclass(slots=True, frozen=True)
class Decision:
    mode: Mode
    reason: str


def get_active_connectors(gpus: tuple[GPU, ...]) -> tuple[Connector, ...]:
    connectors: list[Connector] = []

    for gpu in gpus:
        for connector in gpu.connectors:
            if connector.active:
                connectors.append(connector)

    return tuple(connectors)


def get_active_external_connectors(
    gpus: tuple[GPU, ...],
) -> tuple[Connector, ...]:
    return tuple(
        connector
        for connector in get_active_connectors(gpus)
        if connector.connector_type is not ConnectorType.INTERNAL
    )


def decide(gpus: tuple[GPU, ...]) -> Decision:
    external = get_active_external_connectors(gpus)

    if not external:
        return Decision(
            mode=Mode.HANDHELD,
            reason="no_active_external_display",
        )

    raise NotImplementedError("External display handling not implemented yet.")

from __future__ import annotations

from bazzite_auto_switch.drm import read_gpus
from bazzite_auto_switch.models import Connector


def _yes_no_unknown(value: bool | None) -> str:
    if value is True:
        return "yes"

    if value is False:
        return "no"

    return "unknown"


def _print_connector(connector: Connector) -> None:
    print(f"  {connector.drm_id}")
    print(f"    Connected     {_yes_no_unknown(connector.connected)}")
    print(f"    Enabled       {_yes_no_unknown(connector.enabled)}")
    print(f"    Active        {_yes_no_unknown(connector.active)}")
    print(f"    Manufacturer  {connector.manufacturer or '-'}")
    print(f"    Monitor       {connector.monitor_name or '-'}")


def run() -> int:
    """
    List all detected GPUs and connectors.
    """
    for gpu in read_gpus():
        print(f"GPU: {gpu.drm_id}")
        print()

        for connector in gpu.connectors:
            _print_connector(connector)
            print()

    return 0

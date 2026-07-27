from __future__ import annotations

from bazzite_auto_switch.config import (
    load_config,
    save_config,
    set_automatic_switching,
)


def run() -> int:
    config = load_config()

    save_config(
        set_automatic_switching(
            config,
            True,
        )
    )

    return 0

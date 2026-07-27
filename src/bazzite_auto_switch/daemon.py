from __future__ import annotations

import logging
import time

from bazzite_auto_switch.config import load_config
from bazzite_auto_switch.events import DisplayEvents
from bazzite_auto_switch.once import run as run_once


def run() -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    events = DisplayEvents()

    logging.info("Daemon started.")

    try:
        run_once()

        while True:
            events.wait()

            config = load_config()

            time.sleep(config.display_settle_time)

            run_once()

    except KeyboardInterrupt:
        logging.info("Daemon stopped.")

    return 0

from __future__ import annotations

from datetime import datetime


def debug_print(*args: object) -> None:
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(timestamp, *args)

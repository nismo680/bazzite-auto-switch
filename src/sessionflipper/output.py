from __future__ import annotations

_DEBUG = False


def set_debug(enabled: bool) -> None:
    global _DEBUG
    _DEBUG = enabled


def info(message: str) -> None:
    print(message)


def debug(message: str) -> None:
    if _DEBUG:
        print(message)

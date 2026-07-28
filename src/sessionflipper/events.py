from __future__ import annotations

import pyudev


class DisplayEvents:
    def __init__(self) -> None:
        context = pyudev.Context()

        self._monitor = pyudev.Monitor.from_netlink(context)
        self._monitor.filter_by(subsystem="drm")
        self._monitor.start()

    def wait(self) -> None:
        for device in self._monitor:
            print(device.action, device.subsystem, dict(device))
            return

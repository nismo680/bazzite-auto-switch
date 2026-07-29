from __future__ import annotations

import pyudev


class DisplayEvents:
    def __init__(
        self,
        debug: bool = False,
    ) -> None:
        self._debug = debug

        context = pyudev.Context()

        self._monitor = pyudev.Monitor.from_netlink(context)
        self._monitor.filter_by(subsystem="drm")

    def wait(self) -> None:
        for action, device in self._monitor:
            if self._debug:
                print()
                print("------------------------------------------------------------")
                print("DRM hotplug event")
                print(f"action    : {action}")
                print(f"subsystem : {device.subsystem}")
                print(f"device    : {device.device_node}")
                print(f"sys_path  : {device.sys_path}")

                connector = device.get("CONNECTOR")
                if connector is not None:
                    print(f"connector : {connector}")

                hotplug = device.get("HOTPLUG")
                if hotplug is not None:
                    print(f"hotplug   : {hotplug}")

            return

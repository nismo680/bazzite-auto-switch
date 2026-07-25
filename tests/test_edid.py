from bazzite_auto_switch.edid import MonitorInfo


def test_monitor_info_defaults() -> None:
    info = MonitorInfo()

    assert info.manufacturer is None
    assert info.monitor_name is None


def test_monitor_info_values() -> None:
    info = MonitorInfo(
        manufacturer="DEL",
        monitor_name="DELL U2723QE",
    )

    assert info.manufacturer == "DEL"
    assert info.monitor_name == "DELL U2723QE"

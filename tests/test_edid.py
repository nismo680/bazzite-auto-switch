from sessionflipper.edid import (
    MonitorInfo,
    decode_manufacturer,
    parse_edid,
    parse_monitor_name,
)


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


def test_decode_manufacturer_del() -> None:
    assert decode_manufacturer(bytes.fromhex("10 AC")) == "DEL"


def test_decode_manufacturer_len() -> None:
    assert decode_manufacturer(bytes.fromhex("30 AE")) == "LEN"


def test_decode_manufacturer_invalid_length() -> None:
    import pytest

    with pytest.raises(ValueError):
        decode_manufacturer(b"\x10")


def test_parse_edid_manufacturer() -> None:
    edid = bytearray(128)

    # DEL
    edid[8:10] = bytes.fromhex("10 AC")

    info = parse_edid(bytes(edid))

    assert info.manufacturer == "DEL"
    assert info.monitor_name is None


def test_parse_edid_too_short() -> None:
    import pytest

    with pytest.raises(ValueError):
        parse_edid(b"\x00" * 127)


def test_parse_monitor_name() -> None:
    edid = bytearray(128)

    descriptor = bytearray(18)
    descriptor[3] = 0xFC
    descriptor[5:] = b"DELL U2723QE\n"

    edid[54:72] = descriptor

    assert parse_monitor_name(bytes(edid)) == "DELL U2723QE"


def test_parse_monitor_name_missing() -> None:
    edid = bytes(128)

    assert parse_monitor_name(edid) is None

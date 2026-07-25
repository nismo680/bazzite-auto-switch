from bazzite_auto_switch.models import GPU, Connector, ConnectorType


def test_create_connector() -> None:
    connector = Connector(
        drm_id="card0-DP-1",
        connector_type=ConnectorType.DISPLAYPORT,
        number=1,
        connected=True,
        monitor_name="Dell U2723QE",
    )

    assert connector.connected
    assert connector.monitor_name == "Dell U2723QE"


def test_create_gpu() -> None:
    connector = Connector(
        drm_id="card0-DP-1",
        connector_type=ConnectorType.DISPLAYPORT,
        number=1,
        connected=True,
    )

    gpu = GPU(
        drm_id="card0",
        name="AMD Radeon RX 5700 XT",
        connectors=(connector,),
    )

    assert len(gpu.connectors) == 1
    assert gpu.name == "AMD Radeon RX 5700 XT"

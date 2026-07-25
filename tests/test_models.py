from bazzite_auto_switch.models import GPU, Connector, ConnectorType


def test_create_connector() -> None:
    connector = Connector(
        drm_id="card0-DP-1",
        connector_type=ConnectorType.DISPLAYPORT,
        number=1,
        connected=True,
        enabled=True,
        monitor_name="Dell U2723QE",
    )

    assert connector.drm_id == "card0-DP-1"
    assert connector.connector_type is ConnectorType.DISPLAYPORT
    assert connector.number == 1
    assert connector.connected is True
    assert connector.enabled is True
    assert connector.active is True
    assert connector.monitor_name == "Dell U2723QE"


def test_create_gpu() -> None:
    connector = Connector(
        drm_id="card0-DP-1",
        connector_type=ConnectorType.DISPLAYPORT,
        number=1,
        connected=True,
        enabled=True,
    )

    gpu = GPU(
        drm_id="card0",
        name="Intel Arc",
        connectors=(connector,),
    )

    assert gpu.drm_id == "card0"
    assert gpu.name == "Intel Arc"
    assert len(gpu.connectors) == 1

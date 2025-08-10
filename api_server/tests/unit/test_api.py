import pytest
from api_server.app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_detect_mock(client):
    resp = client.post("/v1/detect/")
    assert resp.status_code == 200
    j = resp.get_json()
    assert "frame_id" in j
    assert isinstance(j["detections"], list)

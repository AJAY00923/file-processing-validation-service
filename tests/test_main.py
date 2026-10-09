from fastapi.testclient import TestClient
from file_validator.main import app


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_unknown_endpoint():
    response = client.get("/unknown")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
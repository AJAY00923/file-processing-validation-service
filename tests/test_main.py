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

def test_validate_customer_invalid_age():
    response = client.post(
        "/validate",
        json = {
            "customer_id": "123",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "age": "abc",
            "country": "USA"
        }
    )

    assert response.status_code == 400

def test_validate_customer_success():
    response = client.post(
        "/validate",        json={
            "customer_id": "101",
            "name": "John",
            "email": "john@gmail.com",
            "age": "25",
            "country": "USA"
        }
    )

    assert response.status_code == 200
    assert response.json() ["age"] == 25

def test_vallidate_customer_invalid_email():
    response = client.post("/validate",json={
            "customer_id": "102",
            "name": "Jane",
            "email": "janeexample.com",
            "age": "30",
            "country": "USA"
        }
    )

    assert response.status_code == 400
    assert response.json() == {"detail": ["email must be a valid email address."]}
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_homepage_loads():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello World" in response.text


def test_add_endpoint():
    response = client.post("/add", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 15.0}


def test_subtract_endpoint():
    response = client.post("/subtract", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 10, "b": 5})
    assert response.status_code == 200
    assert response.json() == {"result": 50.0}


def test_divide_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_divide_by_zero_endpoint():
    response = client.post("/divide", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero!"}


def test_add_invalid_input():
    response = client.post("/add", json={"a": "hello", "b": 5})
    assert response.status_code == 400
    assert "error" in response.json()


def test_missing_field():
    response = client.post("/multiply", json={"a": 10})
    assert response.status_code == 400
    assert "error" in response.json()
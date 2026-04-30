# Tests for the Flask app — pytest auto-discovers files named test_*.py
from app import app


# Verify the root route returns 200 and the expected greeting
def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


# Intentionally broken test — used to demonstrate CI pipeline failure
def test_broken():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Goodbye, World!"

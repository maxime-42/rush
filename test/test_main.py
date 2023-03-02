"""include"""
from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    """test"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello"}
    
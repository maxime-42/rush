"""include"""
from fastapi import status
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    """test"""
    response = client.get("/api")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg": "Hello"}

def test_get_sensors():
    """test"""
    response = client.get("http://localhost:8000/api/sensors/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'sensor': ['a', 'b', 'c']}


def test_get_occpancy_at_instant():
    """test to get occupancy at give time"""
    url = "http://localhost:8000/api/sensors/c/occupancy?atInstant=2021-05-01T16:01:00"
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"sensor": "c","inside": 2}

def test_get_occpancy():
    """test occupancy"""
    response = client.get("http://localhost:8000/api/sensors/c/occupancy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'inside': 2, 'sensor': 'c'}


# def test_get_webhook():
#     """test to insert """
#     response = client.get("http://localhost:8000/api/sensors/c/occupancy")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == {'inside': 2, 'sensor': 'c'}

"""include"""
import unittest
from datetime import datetime
from fastapi import status
from fastapi.testclient import TestClient
from app.models.basemodel import fake_db, SensorEntry
from main import app


class SensorTestCase(unittest.TestCase):
    """this class help to test every functions"""

    def setUp(self):
        """setup database"""
        self.client = TestClient(app)
        self.client.base_url = "http://localhost:8000/api"

        fake_db["a"] = [SensorEntry(ts = datetime.fromisoformat("2021-05-01T10:00:00+00:00"),\
                        in_count=10, out_count=2)]
        fake_db["b"] = [SensorEntry(ts = datetime.fromisoformat("2021-05-01T10:00:00+00:00"),\
                        in_count=15, out_count=2)]
        fake_db["c"] = [
            SensorEntry(ts =
                datetime.fromisoformat("2021-05-01T09:00:00+00:00"), in_count=5, out_count=0), #5
            SensorEntry(ts =
                datetime.fromisoformat("2021-05-01T10:00:00+00:00"), in_count=1, out_count=5), #1
            SensorEntry(ts =
                datetime.fromisoformat("2021-05-01T12:00:00+00:00"), in_count=1, out_count=1), #1
            SensorEntry(ts =
                datetime.fromisoformat("2021-05-01T16:01:00+00:00"), in_count=6, out_count=5), #2
        ]

    def tearDown(self):
        fake_db.clear()

    def test_get_sensors(self):
        """test"""
        response = self.client.get("sensors")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'sensor': ['a', 'b', 'c']}

    def test_get_occpancy_at_instant(self):
        """test to get occupancy at give time"""
        url = "sensors/c/occupancy?atInstant=2021-05-01T16:01:00"
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"sensor": "c","inside": 2}

    def test_get_occpancy(self):
        """test occupancy"""
        response = self.client.get("sensors/c/occupancy")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {'inside': 2, 'sensor': 'c'}

    def test_get_webhook(self):
        """test to insert """
        json_data={"sensor":"abc","ts":"2023-10-10T13:00:00+00:00","in":3,"out":2}
        response = self.client.post("webhook", json=json_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == json_data

"""unitest file"""
import unittest
from datetime import datetime
from app.models.shape_data import fake_db, SensorEntry, NewEntry
from app.service.service_sensors import calculate_people_inside, get_list_sensor
from app.service.service_webhook import create_sensor_entry


class SensorTestCase(unittest.TestCase):
    """this class help to test every functions"""

    def setUp(self):
        """setup database"""
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

    def test_calculate_people_inside(self):
        """test people inside room"""
        self.assertEqual(calculate_people_inside("a")['inside'], 8)
        self.assertEqual(calculate_people_inside("b")['inside'], 13)
        self.assertEqual(
            calculate_people_inside("c",
                datetime.fromisoformat("2021-05-01T16:00:00+00:00"))['inside'], 1
        )
        self.assertEqual(
            calculate_people_inside("c",
                datetime.fromisoformat("2021-05-01T16:01:00+00:00"))['inside'], 2
        )

    def test_get_list_sensor(self):
        """test"""
        print(get_list_sensor())
        self.assertEqual(get_list_sensor(), {'sensor': ['a', 'b', 'c']})

    def test_create_sensor_entry(self):
        """test create new sensor"""
        new_sensor = NewEntry.parse_obj({
            "sensor":"d",
            "ts": "2023-01-01T00:00:00+00:00",
            "in":"5",
            "out":"3",
        })
        actual = create_sensor_entry(new_sensor)
        self.assertEqual(actual, new_sensor)

""" Square Sense assignment """
from datetime import datetime
from pydantic import BaseModel # pylint: disable=no-name-in-module
from pydantic import Field # pylint: disable=no-name-in-module

class SensorEntry(BaseModel):
    "Sensor Entry object "
    ts: datetime
    in_count: int
    out_count: int

class NewEntry(BaseModel):
    "forma of new entry"
    sensor:str
    ts: datetime
    in_count:int = Field(..., alias='in')
    out:int

SensorDb: dict[str, list[SensorEntry]] = {
    "a": [
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T10:00:00+00:00"), in_count=10, out_count=2),
    ],
    "b": [
        SensorEntry(ts = datetime.fromisoformat("2021-04-30T16:00:00+00:00"), in_count=5, out_count=35),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T10:00:00+00:00"), in_count=10, out_count=5),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T12:00:00+00:00"), in_count=20, out_count=10),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T16:00:00+00:00"), in_count=5, out_count=20),
    ],
    "c": [
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T09:00:00+00:00"), in_count=5, out_count=0),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T10:00:00+00:00"), in_count=1, out_count=5),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T12:00:00+00:00"), in_count=1, out_count=1),
        SensorEntry(ts = datetime.fromisoformat("2021-05-01T16:01:00+00:00"), in_count=6, out_count=5),
    ]
}

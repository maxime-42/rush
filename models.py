""" Square Sense assignment """
# from datetime import date
from pydantic import BaseModel


class SensorEntry(BaseModel):
    "sensort models  Sensor Entry object "
    id : str
    ts: str
    inCount: int
    outCount: int


SensorDb = {
  "abc": SensorEntry(id = "abc", 
                    ts = "2018-11-14T13:34:49Z",
                    inCount=1,
                    outCount=2),
  "efg": SensorEntry(id = "efg", 
                    ts = "2018-11-14T13:34:49Z",
                    inCount=1, 
                    outCount=2)
}

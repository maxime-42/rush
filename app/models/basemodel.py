""" Square Sense assignment """
from datetime import datetime
from pydantic import BaseModel # pylint: disable=no-name-in-module
from pydantic import Field # pylint: disable=no-name-in-module

class SensorEntry(BaseModel):
    """Sensor Entry object """
    ts: datetime
    in_count: int
    out_count: int

class NewEntry(BaseModel):
    """format of new entry"""
    sensor:str
    ts: datetime
    in_count:int = Field(..., alias='in')
    out_count:int  = Field(..., alias='out')

fake_db: dict[str, list[SensorEntry]] = {}

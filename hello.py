#!/usr/bin/env python

""" Square Sense assignment """
from datetime import date
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorEntry(BaseModel):
    """
    Sensor Entry object 
    """
    ts: date
    inCount: int
    outCount: int

class Sensor(BaseModel):
    """
    Sensor object 
    """
    id: str
    entries: list[SensorEntry] | None = None

sensorsDB: list[Sensor] = [
    Sensor(id='abc'),
    Sensor(id='def')
]

@app.get("/sensors")
async def get_sensors():
    """
    Return all sensor id 
    """
    return {
        'sensors': [x.id for x in sensorsDB]
    }

@app.post("/webhook")
async def create_sensor_entry(payload: dict = Body()):
    """
    Create an entry to a given sensor
    """
    sensorsDB[payload['id']].append(SensorEntry(payload['ts'], payload['in'], payload['out']))
    return payload

@app.get("/sensors/{sensor_id}/occupancy")
async def get_sensor_occupancy(sensor_id: str):
    """
    Return the occupancy of a specific sensor 
    """
    return {
        'sensor': sensor_id,
        'inside': calculate_inside(sensor_id)
    }

def calculate_inside(sensor_id: str):
    """
    Calculate number of people inside
    """
    
   # sensor_id = sensor_id
    return 10

# tests
# def test_calculate_inside():
#     assert calculate_inside('abc') == 5

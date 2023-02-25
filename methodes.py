"methods"
from datetime import datetime
from typing import Optional
from fastapi import HTTPException, status
from models import SensorDb, NewEntry, SensorEntry

def get_list_sensor() -> {str,list[str]}: # type: ignore
    "return list of knew sensor"
    sensor_list : list[str] = []
    for item in SensorDb:
        sensor_list.append(item)
    return {"sensor" : sensor_list}


def create_sensor_entry(payload:NewEntry)->NewEntry:
    "insert new enty into database"
    new_sensor = SensorEntry(ts=payload.ts,
                            in_count = payload.in_count, out_count = payload.out)
    sensor_name:str = payload.sensor
    if sensor_name in SensorDb:
        SensorDb[sensor_name].append(new_sensor)
    else:
        SensorDb[sensor_name] = [new_sensor]
    return payload


def calculate_people_inside(sensor_id: str, at_instant: Optional[datetime] = None):
    "return the number of people in the room"
    if sensor_id not in SensorDb:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Sensor id '{sensor_id}' not found"
        )
    room_list = SensorDb[sensor_id]
    if at_instant is None:
        sensor_list = room_list
    else:
        sensor_list = [x for x in room_list if x.ts <= at_instant]
    return {
        "sensor": sensor_id,
        "inside": sum(x.in_count - x.out_count for x in sensor_list)
    }

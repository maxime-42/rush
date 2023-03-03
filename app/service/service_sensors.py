"""methods"""
from typing import Dict, Optional
from datetime import datetime
from fastapi import HTTPException, status
from app.models.shape_data import fake_db

def get_list_sensor() -> Dict[str,list[str]]:
    """return list of knew sensor"""
    sensor_list : list[str] = []
    for item in fake_db:
        sensor_list.append(item)
    return {"sensor" : sensor_list}

def calculate_people_inside(sensor_id: str, at_instant: Optional[datetime] = None):
    """return the number of people in the room"""

    if sensor_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Sensor id '{sensor_id}' not found"
        )
    room_list = fake_db[sensor_id]
    if at_instant is None:
        sensor_list = room_list
    else:
        sensor_list = [x for x in room_list if x.ts <= at_instant]
    return {
        "sensor": sensor_id,
        "inside": sum(x.in_count - x.out_count for x in sensor_list)
    }

"methods"
from datetime import datetime
from typing import Optional
from fastapi import HTTPException, status, APIRouter
from app.models.models import fake_db, NewEntry, SensorEntry

router = APIRouter(prefix="/api")

@router.post("/webhook", status_code=status.HTTP_201_CREATED)
def create_sensor_entry(payload:NewEntry)->NewEntry:
    "insert new enty into database"
    new_sensor = SensorEntry(ts=payload.ts,
                            in_count = payload.in_count, out_count = payload.out)
    assert new_sensor.ts.tzinfo is not None

    sensor_name:str = payload.sensor
    if sensor_name in fake_db:
        fake_db[sensor_name].append(new_sensor)
    else:
        fake_db[sensor_name] = [new_sensor]
    return payload

@router.get("/sensors/{sensor_id}/occupancy")
def calculate_people_inside(sensor_id: str, at_instant: Optional[datetime] = None):
    "return the number of people in the room"
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

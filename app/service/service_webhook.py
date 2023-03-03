"methods"
from fastapi import status, APIRouter
from app.models.shape_data import fake_db, NewEntry, SensorEntry

router = APIRouter()

@router.post("/webhook", status_code=status.HTTP_201_CREATED)
def create_sensor_entry(payload:NewEntry)->NewEntry:
    "insert new enty into database"
    new_sensor = SensorEntry(ts=payload.ts,
                            in_count = payload.in_count, out_count = payload.out_count)
    assert new_sensor.ts.tzinfo is not None

    sensor_name:str = payload.sensor
    if sensor_name in fake_db:
        fake_db[sensor_name].append(new_sensor)
    else:
        fake_db[sensor_name] = [new_sensor]
    return payload

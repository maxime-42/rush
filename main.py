"included modules"
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, APIRouter, status, HTTPException
from methodes import get_list_sensor, create_sensor_entry
from models import NewEntry, SensorDb

app = FastAPI()

router = APIRouter(prefix="/api")

@router.get("/sensors")
def get_sensors():
    "This method return all sensors"
    return get_list_sensor()

@router.post("/webhook", status_code=status.HTTP_201_CREATED)
async def create_user(payload: NewEntry) -> NewEntry:
    "create sensor entry in database"
    return create_sensor_entry(payload)

@router.get("/sensors/{sensor_id}/occupancy")
async def get_sensor_occupancy(sensor_id: str, atInstant: Optional[datetime] = None):  # pylint: disable=invalid-name
    "get number of people in room"
    return calculate_people_inside(sensor_id, atInstant)


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


app.include_router(router)

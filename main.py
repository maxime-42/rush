"included modules"
from datetime import datetime
from typing import Optional
from fastapi import FastAPI, APIRouter, status
from methodes import get_list_sensor, create_sensor_entry, calculate_people_inside
from models import NewEntry

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




app.include_router(router)

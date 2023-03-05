"methods"
from typing import Dict, Optional
from datetime import datetime
from fastapi import APIRouter
from app.service.service_peopleCounter import get_list_sensor, calculate_people_inside
router = APIRouter(prefix="/sensors")

@router.get("/")
def service_get_list_sensor() -> Dict[str,list[str]]:
    "return list of knew sensor"
    return get_list_sensor()

@router.get("/{sensor_id}/occupancy")
def service_get_people_inside(sensor_id: str, at_instant: Optional[datetime] = None):
    """return the number of people in the room"""
    return calculate_people_inside(sensor_id, at_instant)

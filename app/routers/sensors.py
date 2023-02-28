"methods"
from typing import Dict
from fastapi import APIRouter
from app.models.models import SensorDb

router = APIRouter(prefix="/api")
@router.get("/sensors")
def get_list_sensor() -> Dict[str,list[str]]:
    "return list of knew sensor"
    sensor_list : list[str] = []
    for item in SensorDb:
        sensor_list.append(item)
    return {"sensor" : sensor_list}

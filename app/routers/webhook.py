"methods"
from fastapi import status, APIRouter
from app.models.basemodel import NewEntry
from app.service.service_webhook import create_sensor_entry

router = APIRouter()

@router.post("/webhook", status_code=status.HTTP_201_CREATED)
def service_sensor_entry(payload:NewEntry)->NewEntry:
    """test"""
    return create_sensor_entry(payload)

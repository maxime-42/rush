"""included modules"""
from fastapi import FastAPI
from app.routers import sensors, webhook


app = FastAPI()
# router = APIRouter(prefix="/api")

app.include_router(sensors.router)
app.include_router(webhook.router)
# app.include_router(router)

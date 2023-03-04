"""included modules"""
from fastapi import FastAPI, APIRouter
from app.routers import sensors, webhook

app = FastAPI(docs_url="/api/documentation")

router_base = APIRouter(prefix="/api")

router_base.include_router(sensors.router)
router_base.include_router(webhook.router)

app.include_router(router_base)

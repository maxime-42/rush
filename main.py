"""included modules"""
from fastapi import FastAPI, APIRouter
from app.routers import sensors, webhook

app = FastAPI()

router_base = APIRouter(prefix="/api")

@router_base.get("/")
async def hello_world():
    """test"""
    return {"msg": "Hello world"}

router_base.include_router(sensors.router)
router_base.include_router(webhook.router)

app.include_router(router_base)

"""included modules"""
from fastapi import FastAPI, APIRouter
from app.routers import peopleCounter, webhook

app = FastAPI(docs_url="/api/docs")

router_base = APIRouter(prefix="/api")

router_base.include_router(peopleCounter.router)
router_base.include_router(webhook.router)

app.include_router(router_base)

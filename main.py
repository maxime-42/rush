"""included modules"""
from fastapi import FastAPI
from app.routers import sensors, webhook

app = FastAPI()

@app.get("/")
async def read_main():
    """test"""
    return {"msg": "Hello"}

app.include_router(sensors.router)
app.include_router(webhook.router)

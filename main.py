"included modules"
from fastapi import FastAPI
from models import SensorDb, SensorEntry

app = FastAPI()


@app.get("/")
def read_root():
    "hello"
    return {"Hello": "World"}

@app.get("//hostname/api/sensors")
def get_coppancy():
    "This method return all occupancy"
    return SensorDb


@app.post("/")
async def create_user(sensor : SensorEntry) -> str:
    "insert user une database"
    SensorDb[sensor.id] = sensor
    return sensor.id

@app.get("/api/sensors/{sensor_id}/occupancy")
async def get_sensor_occupancy(sensor_id: str):
    "retrieved a sensor"
    sensor = SensorDb[sensor_id]
    return {
        "sensor" :sensor.id,
        "inside" :sensor.inCount
    }

@app.get("/sensors/{sensor_id}/{atInstant}")
async def get_nb_occupancy(sensor_id: str, atInstant:str):
    "retrieved a sensor"
    # sensor = SensorDb[sensor_id]
    return "occccuuupation"
    
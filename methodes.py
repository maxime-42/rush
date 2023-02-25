"include"
from models import SensorDb, NewEntry, SensorEntry

def get_list_sensor() -> {str,list[str]}: # type: ignore
    "return list of knew sensor"
    sensor_list : list[str] = []
    for item in SensorDb:
        sensor_list.append(item)
    return {"sensor" : sensor_list}


def create_sensor_entry(payload:NewEntry)->NewEntry:
    "insert new enty into database"
    new_sensor = SensorEntry(ts=payload.ts,
                            in_count = payload.in_count, out_count = payload.out)
    sensor_name:str = payload.sensor
    if sensor_name in SensorDb:
        SensorDb[sensor_name].append(new_sensor)
    else:
        SensorDb[sensor_name] = [new_sensor]
    return payload

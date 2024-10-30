from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Sensor, Unit, Device
from Schemas.Schema_Sensor import SensorResponse, SensorCreate

sensor_R = APIRouter(tags=["Sensores"])


@sensor_R.get("/sensors", response_model=list[SensorResponse])
def list_sensors():
    sensores = db.query(Sensor).all()
    
    if not sensores:
        raise HTTPException(status_code=404, detail="No hay sensores disponibles")
    
    return sensores


@sensor_R.get("/sensor/{id}", response_model=SensorResponse)
def search_sensor(id: int):
    sensor_b = db.query(Sensor).filter(Sensor.id == id).first()
    
    if sensor_b is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    
    return sensor_b


@sensor_R.post("/sensor", response_model=SensorResponse)
def create_sensor(sensor_data: SensorCreate):
    unidad = db.query(Unit).filter(Unit.id == sensor_data.unit_id).first()
    dispositivo = db.query(Device).filter(Device.id == sensor_data.device_id).first()

    if (unidad is None) or (dispositivo is None):
        raise HTTPException(status_code=404, detail="Error en llaves foráneas")

    new_sensor = Sensor(
        sensor_name = sensor_data.sensor_name,
        function = sensor_data.function,
        device_id = sensor_data.device_id,
        unit_id = sensor_data.unit_id
    )

    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    
    return new_sensor


@sensor_R.put("/sensor/{id}", response_model=SensorResponse)
def update_sensor(id: int, sensor_data: SensorCreate):
    db_sensor = db.query(Sensor).filter(sensor_data.id == id).first()
    unidad = db.query(Unit).filter(Unit.id == sensor_data.unit_id).first()
    dispositivo = db.query(Device).filter(Device.id == sensor_data.device_id).first()
    
    if (db_sensor is None) or (unidad is None) or (dispositivo is None):
        raise HTTPException(status_code=404, detail="Elemento no encontrado")

    db_sensor.sensor_name = sensor_data.sensor_name
    db_sensor.function = sensor_data.function
    db_sensor.device_id = sensor_data.device_id
    db_sensor.unit_id = sensor_data.unit_id
    
    db.commit()
    db.refresh(db_sensor)
    
    return db_sensor


@sensor_R.delete("/sensor/{id}", response_model=dict)
def delete_sensor(id: int):
    sensor = db.query(Sensor).filter(Sensor.id == id).first()
    
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    
    db.delete(sensor)
    db.commit()
    
    return sensor

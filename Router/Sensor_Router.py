from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Sensor, Unit, Device
from Schemas.Schema_Sensor import SensorResponse, SensorCreate

sensor_R = APIRouter(tags=["Sensores"])

# Obtener todos los sensores
@sensor_R.get("/sensors", response_model=list[SensorResponse])
def list_sensors():
    sensors = db.query(Sensor).all()
    # Comprobar si hay sensores disponibles
    if not sensors:
        raise HTTPException(status_code=404, detail="No hay sensores disponibles")
    return sensors

# Obtener un sensor por ID
@sensor_R.get("/sensor/{id}", response_model=SensorResponse)
def search_sensor(id: int):
    sensor = db.query(Sensor).filter(Sensor.id == id).first()
    # Comprobar si el sensor existe
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return sensor

# Crear un nuevo sensor
@sensor_R.post("/sensor", response_model=SensorResponse)
def create_sensor(sensor: SensorCreate):

    unit = db.query(Unit).filter(Unit.id == sensor.unit_id).first()
    device = db.query(Device).filter(Device.id == sensor.device_id).first()

    if (unit is None) or (device is None):
        raise HTTPException(status_code=404, detail="Error en llaves foráneas")

    new_sensor = Sensor(
        sensor_name = sensor.sensor_name,
        function = sensor.function,
        device_id = sensor.device_id,
        unit_id = sensor.unit_id
    )

    db.add(new_sensor)
    db.commit()
    db.refresh(new_sensor)
    
    return new_sensor

# Actualizar un sensor
@sensor_R.put("/sensor/{id}", response_model=SensorResponse)
def update_sensor(id: int, sensor: SensorCreate):
    db_sensor = db.query(Sensor).filter(Sensor.id == id).first()
    # Verifica si el sensor existe
    if db_sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")

    # Actualiza los valores del sensor
    db_sensor.sensor_name = sensor.sensor_name
    db_sensor.function = sensor.function
    db_sensor.device_id = sensor.device_id
    db_sensor.unit_id = sensor.unit_id
    
    # Confirma los cambios
    db.commit()
    db.refresh(db_sensor)
    
    return db_sensor

# Eliminar un sensor
@sensor_R.delete("/sensor/{id}", response_model=dict)
def delete_sensor(id: int):
    sensor = db.query(Sensor).filter(Sensor.id == id).first()
    # Comprobar si el sensor existe
    if sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    
    db.delete(sensor)
    db.commit()
    
    return {"detail": "Sensor eliminado exitosamente"}

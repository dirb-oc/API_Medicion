from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Sensor, Unit, Device
from Schemas.Schema_Sensor import SensorResponse, SensorCreate

sensor = APIRouter(tags=["Sensores"])

# Obtener los usuarios
@sensor.get("/sensors", response_model=list[SensorResponse])
def list_Sensor():
    Sensores = db.query(Sensor).all()
    # Comprobar si el usuario exite
    if not Sensores:
        raise HTTPException(status_code=404, detail="No hay sensores disponibles")
    
    return Sensores

# Obtener un usuario por ID
@sensor.get("/sensor/{id}", response_model=SensorResponse)
def Search_Sensor(id: int):
    Sensor = db.query(Sensor).filter(Sensor.id == id).first()
    # Comprobar si el usuario exite
    if Sensor is None:
        raise HTTPException(status_code=404, detail="Sensor no encontrado")
    return Sensor

# Crear un nuevo usuario
@sensor.post("/sensor", response_model=SensorResponse)
def Create_Sensor(sensor: SensorCreate):

    Unidad = db.query(Unit).filter(Sensor.unit_id == id).first()
    Dispositivo = db.query(Device).filter(Sensor.device_id == id).first()
    if (Unidad is None) or (Dispositivo is None):
        raise HTTPException(status_code=404, detail="Error en llaves Foraneas")
    
    new_Sensor = sensor(
        sensor_name = sensor.sensor_name,
        function = sensor.function,
        device_id = sensor.device_id,
        unit_id = sensor.unit_id
    )

    db.add(new_Sensor)
    db.commit()
    db.refresh(new_Sensor)
    
    return new_Sensor

# Actualizar usuario
@sensor.put("/sensor/{id}", response_model=SensorResponse)
def update_Device(id: int, sensor: SensorCreate):
    # Busca al usuario existente
    db_Sensor = db.query(Sensor).filter(Sensor.id == id).first()
    # Verifica si el usuario existe
    if db_Sensor is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    # Actualiza los valores del usuario

    db_Sensor.sensor_name = sensor.sensor_name,
    db_Sensor.function = sensor.function,
    db_Sensor.device_id = sensor.device_id,
    db_Sensor.unit_id = sensor.unit_id
    # Confirma los cambios
    db.commit()
    db.refresh(db_Sensor)
    
    return db_Sensor

# Eliminiar Usuario
@sensor.delete("/sensor/{id}", response_model=SensorResponse)
def delete_Device(id: int):
    Dispositivo = db.query(Sensor).filter(Sensor.id == id).first()
    # Comprobar si el usuario exite
    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    
    db.delete(Dispositivo)
    db.commit()
    
    return Dispositivo
from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Device
from Schemas.Schema_Device import DeviceResponse, DeviceCreate

device = APIRouter(tags=["Dispositivos"])

# Obtener los usuarios
@device.get("/devices", response_model=list[DeviceResponse])
def list_devices():
    Dispositvos = db.query(Device).all()
    # Comprobar si el usuario exite
    if Dispositvos is None:
        raise HTTPException(status_code=404, detail="No hay Lugares")
    
    return Dispositvos

# Obtener un usuario por ID
@device.get("/device/{id}", response_model=DeviceResponse)
def Search_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Comprobar si el usuario exite
    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return Dispositivo

# Crear un nuevo usuario
@device.post("/device", response_model=DeviceResponse)
def Create_Device(Dispositivo: DeviceCreate):
    new_Dispositivo = Device(
        device_name = Dispositivo.device_name,
        installation_date = Dispositivo.installation_date,
        location_id = Dispositivo.location_id
    )

    db.add(new_Dispositivo)
    db.commit()
    db.refresh(new_Dispositivo)
    
    return new_Dispositivo

# Actualizar usuario
@device.put("/device/{id}", response_model=DeviceResponse)
def update_Device(id: int, Dispositivo: DeviceCreate):
    # Busca al usuario existente
    db_Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Verifica si el usuario existe
    if db_Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    # Actualiza los valores del usuario
    db_Dispositivo.device_name = Dispositivo.device_name,
    db_Dispositivo.installation_date = Dispositivo.installation_date,
    db_Dispositivo.location_id = Dispositivo.location_id
    # Confirma los cambios
    db.commit()
    db.refresh(db_Dispositivo)
    
    return db_Dispositivo

# Eliminiar Usuario
@device.delete("/device/{id}", response_model=DeviceResponse)
def delete_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Comprobar si el usuario exite
    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    
    db.delete(Dispositivo)
    db.commit()
    
    return Dispositivo
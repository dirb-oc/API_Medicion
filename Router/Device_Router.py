from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Device, Location
from Schemas.Schema_Device import DeviceResponse, DeviceCreate

device_R = APIRouter(tags=["Dispositivos"])

# Obtener los usuarios
@device_R.get("/devices", response_model=list[DeviceResponse])
def list_devices():
    Dispositvos = db.query(Device).all()
    # Comprobar si el usuario exite
    if Dispositvos is None:
        raise HTTPException(status_code=404, detail="No hay Lugares")
    
    return Dispositvos

# Obtener un usuario por ID
@device_R.get("/device/{id}", response_model=DeviceResponse)
def Search_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Comprobar si el usuario exite
    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return Dispositivo

# Crear un nuevo usuario
@device_R.post("/device", response_model=DeviceResponse)
def Create_Device(Dispositivo_data: DeviceCreate):

    Lugar = db.query(Location).filter(Location.id == Dispositivo_data.location_id).first()
    # Comprobar si el usuario exite
    if Lugar is None:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")

    new_Dispositivo = Device(
        device_name = Dispositivo_data.device_name,
        location_id = Dispositivo_data.location_id,
        installation_date = Dispositivo_data.installation_date
    )

    db.add(new_Dispositivo)
    db.commit()
    db.refresh(new_Dispositivo)
    
    return new_Dispositivo

# Actualizar usuario
@device_R.put("/device/{id}", response_model=DeviceResponse)
def update_Device(id: int, Dispositivo_data: DeviceCreate):
    # Busca al usuario existente
    db_Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Verifica si el usuario existe
    if db_Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    # Actualiza los valores del usuario
    db_Dispositivo.device_name = Dispositivo_data.device_name,
    db_Dispositivo.installation_date = Dispositivo_data.installation_date,
    db_Dispositivo.location_id = Dispositivo_data.location_id
    # Confirma los cambios
    db.commit()
    db.refresh(db_Dispositivo)
    
    return db_Dispositivo

# Eliminiar Usuario
@device_R.delete("/device/{id}", response_model=DeviceResponse)
def delete_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()
    # Comprobar si el usuario exite
    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    
    db.delete(Dispositivo)
    db.commit()
    
    return Dispositivo
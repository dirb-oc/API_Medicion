from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Device, Location
from Schemas.Schema_Device import DeviceResponse, DeviceCreate

device_R = APIRouter(tags=["Dispositivos"])


@device_R.get("/devices", response_model=list[DeviceResponse])
def list_devices():
    Dispositvos = db.query(Device).all()

    if Dispositvos is None:
        raise HTTPException(status_code=404, detail="No hay Lugares")
    
    return Dispositvos


@device_R.get("/device/{id}", response_model=DeviceResponse)
def Search_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()

    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    return Dispositivo


@device_R.post("/device", response_model=DeviceResponse)
def Create_Device(Dispositivo_data: DeviceCreate):
    Lugar = db.query(Location).filter(Location.id == Dispositivo_data.location_id).first()

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


@device_R.put("/device/{id}", response_model=DeviceResponse)
def update_Device(id: int, Dispositivo_data: DeviceCreate):
    Lugar = db.query(Location).filter(Location.id == Dispositivo_data.location_id).first()
    db_Dispositivo = db.query(Device).filter(Device.id == id).first()

    if (db_Dispositivo is None) or (Lugar is None):
        raise HTTPException(status_code=404, detail="Elemento no encontrado")

    db_Dispositivo.device_name = Dispositivo_data.device_name,
    db_Dispositivo.installation_date = Dispositivo_data.installation_date,
    db_Dispositivo.location_id = Dispositivo_data.location_id

    db.commit()
    db.refresh(db_Dispositivo)
    
    return db_Dispositivo


@device_R.delete("/device/{id}", response_model=DeviceResponse)
def delete_Device(id: int):
    Dispositivo = db.query(Device).filter(Device.id == id).first()

    if Dispositivo is None:
        raise HTTPException(status_code=404, detail="Dispositivo no encontrado")
    
    db.delete(Dispositivo)
    db.commit()
    
    return Dispositivo
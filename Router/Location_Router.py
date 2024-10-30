from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Location
from Schemas.Schema_Location import LocationResponse, LocationCreate

location_R = APIRouter(tags=["Ubicación"])


@location_R.get("/locations", response_model=list[LocationResponse])
def List_Locations():
    Lugares = db.query(Location).all()
    
    if Lugares is None:
        raise HTTPException(status_code=404, detail="No hay Lugares")
    
    return Lugares


@location_R.get("/location/{id}", response_model=LocationResponse)
def Search_Locations(id: int):
    lugar = db.query(Location).filter(Location.id == id).first()
    
    if lugar is None:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return lugar


@location_R.post("/location", response_model=LocationResponse)
def Create_Location(lugar_data: LocationCreate):

    new_lugar = Location(
        latitude = lugar_data.latitude,
        longitude = lugar_data.longitude,
        name_place = lugar_data.name_place
    )

    db.add(new_lugar)
    db.commit()
    db.refresh(new_lugar)
    
    return new_lugar


@location_R.put("/location/{id}", response_model=LocationResponse)
def update_Location(id: int, lugar_data: LocationCreate):
    db_lugar = db.query(Location).filter(Location.id == id).first()
    
    if db_lugar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db_lugar.latitude = lugar_data.latitude,
    db_lugar.longitude = lugar_data.longitude,
    db_lugar.name_place = lugar_data.name_place
    
    db.commit()
    db.refresh(db_lugar)
    
    return db_lugar


@location_R.delete("/location/{id}", response_model=LocationResponse)
def delete_Location(id: int):
    lugar = db.query(Location).filter(Location.id == id).first()
    
    if lugar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(lugar)
    db.commit()
    
    return lugar
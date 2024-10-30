from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Location
from Schemas.Schema_Location import LocationResponse, LocationCreate

location_R = APIRouter(tags=["Ubicación"])

# Obtener los usuarios
@location_R.get("/locations", response_model=list[LocationResponse])
def List_Locations():
    Lugares = db.query(Location).all()
    # Comprobar si el usuario exite
    if Lugares is None:
        raise HTTPException(status_code=404, detail="No hay Lugares")
    
    return Lugares

# Obtener un usuario por ID
@location_R.get("/location/{id}", response_model=LocationResponse)
def Search_Locations(id: int):
    lugar = db.query(Location).filter(Location.id == id).first()
    # Comprobar si el usuario exite
    if lugar is None:
        raise HTTPException(status_code=404, detail="Lugar no encontrado")
    return lugar

# Crear un nuevo usuario
@location_R.post("/location", response_model=LocationResponse)
def Create_Location(Lugar: LocationCreate):
    new_lugar = Location(
        latitude = Lugar.latitude,
        longitude = Lugar.longitude,
        name_place = Lugar.name_place
    )

    db.add(new_lugar)
    db.commit()
    db.refresh(new_lugar)
    
    return new_lugar

# Actualizar usuario
@location_R.put("/location/{id}", response_model=LocationResponse)
def update_Location(id: int, Lugar: LocationCreate):
    # Busca al usuario existente
    db_lugar = db.query(Location).filter(Location.id == id).first()
    # Verifica si el usuario existe
    if db_lugar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Actualiza los valores del usuario
    db_lugar.latitude = Lugar.latitude,
    db_lugar.longitude = Lugar.longitude,
    db_lugar.name_place = Lugar.name_place
    # Confirma los cambios
    db.commit()
    db.refresh(db_lugar)
    
    return db_lugar

# Eliminiar Usuario
@location_R.delete("/location/{id}", response_model=LocationResponse)
def delete_Location(id: int):
    lugar = db.query(Location).filter(Location.id == id).first()
    # Comprobar si el usuario exite
    if lugar is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(lugar)
    db.commit()
    
    return lugar
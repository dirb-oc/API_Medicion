from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Unit
from Schemas.Schema_Unit import UnitResponse, UnitCreate

unit_R = APIRouter(tags=["Unidad de Medida"])

# Obtener los usuarios
@unit_R.get("/units",  response_model=list[UnitResponse])
def List_Units():
    unidades = db.query(Unit).all()
    # Comprobar si el usuario exite
    if unidades is None:
        raise HTTPException(status_code=404, detail="No existen unidades de medida")
    
    return unidades

# Obtener un usuario por ID
@unit_R.get("/unit/{id}", response_model=UnitResponse)
def Search_Unit(id: int):
    unidad = db.query(Unit).filter(Unit.id == id).first()
    # Comprobar si el usuario exite
    if unidad is None:
        raise HTTPException(status_code=404, detail="unidad de medida no encontrada")
    return unidad

# Crear un nuevo usuario
@unit_R.post("/unit", response_model=UnitResponse)
def Create_Unit(unidad: UnitCreate):
    new_unit = Unit(
        unit = unidad.unit,
    )

    db.add(new_unit)
    db.commit()
    db.refresh(new_unit)
    
    return new_unit

# Actualizar usuario
@unit_R.put("/unit/{id}", response_model=UnitResponse)
def update_Unit(id: int, unidad: UnitCreate):
    # Busca al usuario existente
    db_unidad = db.query(Unit).filter(Unit.id == id).first()
    # Verifica si el usuario existe
    if db_unidad is None:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrado")
    # Actualiza los valores del usuario
    db_unidad.unit = unidad.unit
    # Confirma los cambios
    db.commit()
    db.refresh(db_unidad)
    
    return db_unidad

# Eliminiar Usuario
@unit_R.delete("/unit/{id}", response_model=UnitResponse)
def delete_Unit(id: int):
    unidad = db.query(Unit).filter(Unit.id == id).first()
    # Comprobar si el usuario exite
    if unidad is None:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrado")
    
    db.delete(unidad)
    db.commit()
    
    return unidad
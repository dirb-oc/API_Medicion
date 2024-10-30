from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Unit
from Schemas.Schema_Unit import UnitResponse, UnitCreate

unit_R = APIRouter(tags=["Unidad de Medida"])


@unit_R.get("/units", response_model=list[UnitResponse])
def List_Units():
    unidades = db.query(Unit).all()
    
    if unidades is None:
        raise HTTPException(status_code=404, detail="No existen unidades de medida")
    
    return unidades


@unit_R.get("/unit/{id}", response_model=UnitResponse)
def Search_Unit(id: int):
    unidad = db.query(Unit).filter(Unit.id == id).first()
    
    if unidad is None:
        raise HTTPException(status_code=404, detail="unidad de medida no encontrada")
    return unidad


@unit_R.post("/unit", response_model=UnitResponse)
def Create_Unit(unit_data: UnitCreate):
    new_unidad = Unit(
        unit = unit_data.unit,
    )

    db.add(new_unidad)
    db.commit()
    db.refresh(new_unidad)
    
    return new_unidad


@unit_R.put("/unit/{id}", response_model=UnitResponse)
def update_Unit(id: int, unit_data: UnitCreate):
    db_unidad = db.query(Unit).filter(Unit.id == id).first()
    
    if db_unidad is None:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrado")
    
    db_unidad.unit = unit_data.unit

    db.commit()
    db.refresh(db_unidad)
    
    return db_unidad


@unit_R.delete("/unit/{id}", response_model=UnitResponse)
def delete_Unit(id: int):
    unidad = db.query(Unit).filter(Unit.id == id).first()
    
    if unidad is None:
        raise HTTPException(status_code=404, detail="Unidad de medida no encontrado")
    
    db.delete(unidad)
    db.commit()
    
    return unidad
from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Record, Sensor
from Schemas.Schema_Record import RecordResponse, RecordCreate

record_R = APIRouter(tags=["Registros"])


@record_R.get("/records", response_model=list[RecordResponse])
def list_Record():
    Registros = db.query(Record).all()
    
    if not Registros:
        raise HTTPException(status_code=404, detail="No hay registros disponibles")
    
    return Registros


@record_R.get("/record/{id}", response_model=RecordResponse)
def Search_Record(id: int):
    Registro = db.query(Record).filter(Record.id == id).first()
    
    if Registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return Registro


@record_R.post("/record", response_model=RecordResponse)
def Create_Record(record_data: RecordCreate):
    sen = db.query(Sensor).filter(Sensor.id == record_data.sensor_id).first()

    if sen is None:
        raise HTTPException(status_code=404, detail="Error en llaves foráneas: sensor no encontrado")

    new_registro = Record(
        value=record_data.value,
        time=record_data.time,
        sensor_id=record_data.sensor_id
    )

    db.add(new_registro)
    db.commit()
    db.refresh(new_registro)
    
    return new_registro


@record_R.put("/record/{id}", response_model=RecordResponse)
def update_Record(id: int, record_data: RecordCreate):
    db_Record = db.query(Record).filter(Record.id == id).first()
    
    if db_Record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
        
    db_Record.value = record_data.value,
    db_Record.time = record_data.time,
    db_Record.sensor_id = record_data.sensor_id
    
    db.commit()
    db.refresh(db_Record)
    
    return db_Record


@record_R.delete("/record/{id}", response_model=RecordResponse)
def delete_Device(id: int):
    Registro = db.query(Record).filter(Record.id == id).first()
    
    if Registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    db.delete(Registro)
    db.commit()
    
    return Registro
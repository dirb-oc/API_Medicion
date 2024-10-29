from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import Record, Sensor
from Schemas.Schema_Record import RecordResponse, RecordCreate

record_R = APIRouter(tags=["Registros"])

# Obtener los usuarios
@record_R.get("/records", response_model=list[RecordResponse])
def list_Record():
    Registros = db.query(Record).all()
    # Comprobar si el usuario exite
    if not Registros:
        raise HTTPException(status_code=404, detail="No hay registros disponibles")
    
    return Registros

# Obtener un usuario por ID
@record_R.get("/record/{id}", response_model=RecordResponse)
def Search_Record(id: int):
    Registro = db.query(Record).filter(Record.id == id).first()
    # Comprobar si el usuario exite
    if Registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    return Registro

# Crear un nuevo usuario
@record_R.post("/record", response_model=RecordResponse)
def Create_Record(record_data: RecordCreate):

    # Verifica si el sensor asociado existe en la base de datos
    sen = db.query(Sensor).filter(Sensor.id == record_data.sensor_id).first()

    if sen is None:
        raise HTTPException(status_code=404, detail="Error en llaves foráneas: sensor no encontrado")
    
    # Crea el nuevo registro en la tabla Record
    new_record = Record(
        value=record_data.value,
        time=record_data.time,
        sensor_id=record_data.sensor_id
    )

    # Añade y guarda el nuevo registro en la base de datos
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    
    return new_record

# Actualizar usuario
@record_R.put("/record/{id}", response_model=RecordResponse)
def update_Record(id: int, record_data: RecordCreate):
    # Busca al usuario existente
    db_Record = db.query(Record).filter(Record.id == id).first()
    # Verifica si el usuario existe
    if db_Record is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    # Actualiza los valores del usuario
        
    db_Record.value = record_data.value,
    db_Record.time = record_data.time,
    db_Record.sensor_id = record_data.sensor_id
    # Confirma los cambios
    db.commit()
    db.refresh(db_Record)
    
    return db_Record

# Eliminiar Usuario
@record_R.delete("/record/{id}", response_model=RecordResponse)
def delete_Device(id: int):
    Registro = db.query(Record).filter(Record.id == id).first()
    # Comprobar si el usuario exite
    if Registro is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")
    
    db.delete(Registro)
    db.commit()
    
    return Registro
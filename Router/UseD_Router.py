from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import UserDevice, User, Device
from Schemas.Schema_USE import Use_DCreate, Use_DResponse

relation_R = APIRouter(tags=["Relacion Usuarios y Dispositivos"])


@relation_R.get("/relations", response_model=list[Use_DResponse])
def list_Relations():
    relaciones = db.query(UserDevice).all()

    if not relaciones:
        raise HTTPException(status_code=404, detail="No hay relaciones de usuarios y dispositivos.")
    
    return relaciones


@relation_R.get("/relation/{id}", response_model=Use_DResponse)
def search_Relation(id: int):
    relacion = db.query(UserDevice).filter(UserDevice.id == id).first()

    if relacion is None:
        raise HTTPException(status_code=404, detail="Relación de usuario y dispositivo no encontrada.")
    
    return relacion


@relation_R.post("/relation", response_model=Use_DResponse)
def create_Relation(relation_data: Use_DCreate):
    user = db.query(User).filter(User.id == relation_data.user_id).first()
    dispositivo = db.query(Device).filter(Device.id == relation_data.device_id).first()

    if (user is None) or (dispositivo is None):
        raise HTTPException(status_code=404, detail="Error en llaves foráneas")

    new_relation = UserDevice(
        user_id=relation_data.user_id,
        device_id=relation_data.device_id
    )

    db.add(new_relation)
    db.commit()
    db.refresh(new_relation)
    
    return new_relation


@relation_R.put("/relation/{id}", response_model=Use_DResponse)
def update_user(id: int, relation_data: Use_DCreate):
    db_relation = db.query(UserDevice).filter(UserDevice.id == id).first()
    user = db.query(User).filter(User.id == relation_data.user_id).first()
    dispositivo = db.query(Device).filter(Device.id == relation_data.device_id).first()

    if (db_relation is None) or (user is None) or (dispositivo is None):
        raise HTTPException(status_code=404, detail="Elemento no encontrada")

    db_relation.user_id = relation_data.user_id
    db_relation.device_id = relation_data.device_id

    db.commit()
    db.refresh(db_relation)
    
    return db_relation


@relation_R.delete("/relation/{id}", response_model=Use_DResponse)
def delete_user(id: int):
    usuario = db.query(UserDevice).filter(UserDevice.id == id).first()
    
    if usuario is None:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    
    db.delete(usuario)
    db.commit()
    
    return usuario

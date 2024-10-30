from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import User
from Schemas.Schema_User import UserResponse, UserCreate

user_R = APIRouter(tags=["Usuario"])


@user_R.get("/users",  response_model=list[UserResponse])
def List_Users():
    usuarios = db.query(User).all()

    if usuarios is None:
        raise HTTPException(status_code=404, detail="No hay Usuarios")
    
    return usuarios


@user_R.get("/user/{id}", response_model=UserResponse)
def Search_User(id: int):
    usuario = db.query(User).filter(User.id == id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@user_R.post("/user", response_model=UserResponse)
def Create_User(usuario_data: UserCreate):
    new_usuario = User(
        name = usuario_data.name,
        email = usuario_data.email,
        secondname = usuario_data.secondname,
        person = usuario_data.person
    )

    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    
    return new_usuario


@user_R.put("/user/{id}", response_model=UserResponse)
def update_User(id: int, usuario_data: UserCreate):
    db_usuario = db.query(User).filter(User.id == id).first()
    
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db_usuario.name = usuario_data.name,
    db_usuario.email = usuario_data.email,
    db_usuario.secondname = usuario_data.secondname,
    db_usuario.person = usuario_data.person
    
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario


@user_R.delete("/user/{id}", response_model=UserResponse)
def delete_User(id: int):
    usuario = db.query(User).filter(User.id == id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    
    return usuario
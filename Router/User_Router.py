from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model import User
from Schemas.Schema_User import UserResponse, UserCreate

user = APIRouter(tags=["Usuario"])

# Obtener los usuarios
@user.get("/users",  response_model=list[UserResponse])
def List_Users():
    usuarios = db.query(User).all()
    # Comprobar si el usuario exite
    if usuarios is None:
        raise HTTPException(status_code=404, detail="No hay Usuarios")
    
    return usuarios

# Obtener un usuario por ID
@user.get("/user/{id}", response_model=UserResponse)
def Search_User(id: int):
    usuario = db.query(User).filter(User.id == id).first()
    # Comprobar si el usuario exite
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear un nuevo usuario
@user.post("/user", response_model=UserResponse)
def Create_User(usuario: UserCreate):
    new_usuario = User(
        name = usuario.name,
        email = usuario.email,
        secondname = usuario.secondname,
        person = usuario.person
    )

    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    
    return new_usuario

# Actualizar usuario
@user.put("/user/{id}", response_model=UserResponse)
def update_User(id: int, usuario: UserCreate):
    # Busca al usuario existente
    db_usuario = db.query(User).filter(User.id == id).first()
    # Verifica si el usuario existe
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Actualiza los valores del usuario
    db_usuario.name = usuario.name,
    db_usuario.email = usuario.email,
    db_usuario.secondname = usuario.secondname,
    db_usuario.person = usuario.person
    # Confirma los cambios
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario

# Eliminiar Usuario
@user.delete("/user/{id}", response_model=UserResponse)
def delete_User(id: int):
    usuario = db.query(User).filter(User.id == id).first()
    # Comprobar si el usuario exite
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    
    return usuario
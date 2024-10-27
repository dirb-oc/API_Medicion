from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model_User import Usuario
from Schemas.Schema_User import UsuarioResponse, UsuarioCreate

user = APIRouter(tags=["Usuario"])

# Obtener los usuarios
@user.get("/users",  response_model=list[UsuarioResponse])
def List_Users():
    usuarios = db.query(Usuario).all()
    db.close()
    if usuarios is None:
        raise HTTPException(status_code=404, detail="No hay Usuarios")
    return usuarios

# Obtener un usuario por ID
@user.get("/user/{id}", response_model=UsuarioResponse)
def Search_User(id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    db.close()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear un nuevo usuario
@user.post("/user", response_model=UsuarioResponse)
def Create_User(usuario: UsuarioCreate):
    new_usuario = Usuario(nombre=usuario.nombre, correo=usuario.correo)
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    db.close()
    return new_usuario

# Actualizar usuario
@user.put("/user/{id}", response_model=UsuarioResponse)
def update_User(id: int, usuario: UsuarioCreate):
    # Busca al usuario existente
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    
    # Verifica si el usuario existe
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Actualiza los valores del usuario
    db_usuario.nombre = usuario.nombre
    db_usuario.correo = usuario.correo
    
    # Confirma los cambios
    db.commit()
    db.refresh(db_usuario)
    
    return db_usuario

# Eliminiar Usuario
@user.delete("/user/{id}", response_model=UsuarioResponse)
def delete_User(id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    
    return usuario
from fastapi import APIRouter, HTTPException
from Database.Base import db
from Models.Model_User import Usuario
from Schemas.Schema_User import UsuarioResponse, UsuarioCreate

user = APIRouter()

@user.get("/")
def HelloWorld():
    return {"message": "Funcionando"}

# Obtener un usuario por ID
@user.get("/usuarios/",  response_model=list[UsuarioResponse])
def List_Usuarios():
    usuarios = db.query(Usuario).all()
    db.close()
    if usuarios is None:
        raise HTTPException(status_code=404, detail="No hay Usuarios")
    return usuarios

# Obtener un usuario por ID
@user.get("/usuario/{usuario_id}", response_model=UsuarioResponse)
def Search_Usuario(usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.close()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear un nuevo usuario
@user.post("/usuario/", response_model=UsuarioResponse)
def Create_Usuario(usuario: UsuarioCreate):
    new_usuario = Usuario(nombre=usuario.nombre, correo=usuario.correo)
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    db.close()
    return new_usuario
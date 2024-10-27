from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from Database.Base import Base, engine, db

# Configuración de la base de datos


# Definición del modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear la instancia de FastAPI
app = FastAPI()

# Pydantic model para crear un usuario
class UsuarioCreate(BaseModel):
    nombre: str
    correo: str

# Pydantic model para mostrar un usuario
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str

    class Config:
        from_attributes = True

@app.get("/")
def HelloWorld():
    return {"message": "Funcionando"}

# Obtener un usuario por ID
@app.get("/usuarios/",  response_model=list[UsuarioResponse])
def List_Usuarios():
    usuarios = db.query(Usuario).all()
    db.close()
    if usuarios is None:
        raise HTTPException(status_code=404, detail="No hay Usuarios")
    return usuarios

# Obtener un usuario por ID
@app.get("/usuario/{usuario_id}", response_model=UsuarioResponse)
def Search_Usuario(usuario_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.close()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear un nuevo usuario
@app.post("/usuario/", response_model=UsuarioResponse)
def Create_Usuario(usuario: UsuarioCreate):
    new_usuario = Usuario(nombre=usuario.nombre, correo=usuario.correo)
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    db.close()
    return new_usuario
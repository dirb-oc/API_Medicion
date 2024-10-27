from fastapi import FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Configuración de la base de datos
DATABASE_URL = "postgresql://postgres:1005185673@localhost:5432/Medidor"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear una clase base
Base = declarative_base()

# Definición del modelo Usuario
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, nullable=False)

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

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
        orm_mode = True

# Crear un nuevo usuario
@app.post("/usuarios/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate):
    db: Session = SessionLocal()
    new_usuario = Usuario(nombre=usuario.nombre, correo=usuario.correo)
    db.add(new_usuario)
    db.commit()
    db.refresh(new_usuario)
    db.close()
    return new_usuario

# Obtener un usuario por ID
@app.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def read_usuario(usuario_id: int):
    db: Session = SessionLocal()
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    db.close()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/")
def read_root():
    return {"message": "Funcionando"}
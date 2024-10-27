from pydantic import BaseModel

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
from pydantic import BaseModel

class User(BaseModel):
    Id: int
    Nombre: str
    Apellido: str
    Email: str
    Password: str
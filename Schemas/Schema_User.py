from pydantic import BaseModel

# Pydantic model para crear un usuario
class UserCreate(BaseModel):
    name: str
    email: str
    secondname: str
    person: int

# Pydantic model para mostrar un usuario
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    secondname: str
    person: int

    class Config:
        from_attributes = True
from pydantic import BaseModel

# Pydantic model para crear un usuario
class UnitCreate(BaseModel):
    unit: str
    description: str

# Pydantic model para mostrar un usuario
class UnitResponse(BaseModel):
    id: int
    unit: str
    description: str

    class Config:
        from_attributes = True
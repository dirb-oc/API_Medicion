from pydantic import BaseModel

# Pydantic model para crear un usuario
class LocationCreate(BaseModel):
    latitude: int
    longitude: int
    name_place: str

# Pydantic model para mostrar un usuario
class LocationResponse(BaseModel):
    id: int
    latitude: int
    longitude: int
    name_place: str

    class Config:
        from_attributes = True

from pydantic import BaseModel

# Pydantic model para crear un usuario
class Use_DCreate(BaseModel):
    user_id: int
    device_id: int

# Pydantic model para mostrar un usuario
class Use_DResponse(BaseModel):
    id: int
    user_id: int
    device_id: int

    class Config:
        from_attributes = True
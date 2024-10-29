from pydantic import BaseModel
from datetime import datetime

# Pydantic model para crear un dispositivo
class RecordCreate(BaseModel):
    value: int
    time: datetime
    sensor_id: int

# Pydantic model para mostrar un dispositivo
class RecordResponse(BaseModel):
    id: int
    value: int
    time: datetime
    sensor_id: int

    class Config:
        from_attributes = True

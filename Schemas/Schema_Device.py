from pydantic import BaseModel
from datetime import datetime   

# Pydantic model para crear un dispositivo
class DeviceCreate(BaseModel):
    device_name: str
    installation_date: datetime  # Anotación correcta para el tipo datetime
    location_id: int              # Anotación correcta para el tipo int

# Pydantic model para mostrar un dispositivo
class DeviceResponse(BaseModel):
    id: int
    device_name: str
    installation_date: datetime  # Anotación correcta para el tipo datetime
    location_id: int              # Anotación correcta para el tipo int

    class Config:
        from_attributes = True

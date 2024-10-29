from pydantic import BaseModel

# Pydantic model para crear un dispositivo
class SensorCreate(BaseModel):
    sensor_name: str
    function: str
    device_id: int
    unit_id: int

# Pydantic model para mostrar un dispositivo
class SensorResponse(BaseModel):
    id: int
    sensor_name: str
    function: str
    device_id: int
    unit_id: int

    class Config:
        from_attributes = True

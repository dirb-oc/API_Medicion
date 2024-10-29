from fastapi import FastAPI
from Router.User_Router import user
from Router.Unit_Router import unit
from Router.Location_Router import location
from Router.Device_Router import device
from Router.Sensor_Router import sensor_R
from Router.Record_Router import record_R

app = FastAPI()
@app.get("/")
def START():
    return {"System": "Operation"}

app.include_router(user)
app.include_router(device)
app.include_router(sensor_R)
app.include_router(record_R)
app.include_router(location)
app.include_router(unit)
from fastapi import FastAPI
from Router.User_Router import user_R
from Router.Unit_Router import unit_R
from Router.UseD_Router import relation_R
from Router.Device_Router import device_R
from Router.Sensor_Router import sensor_R
from Router.Record_Router import record_R
from Router.Location_Router import location_R

app = FastAPI()
@app.get("/")
def START():
    return {"System": "Operation"}

app.include_router(user_R)
app.include_router(unit_R)
app.include_router(device_R)
app.include_router(sensor_R)
app.include_router(record_R)
app.include_router(location_R)
app.include_router(relation_R)
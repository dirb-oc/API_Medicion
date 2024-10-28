from fastapi import FastAPI
from Router.User_Router import user
from Router.Unit_Router import unit

app = FastAPI()
@app.get("/")
def START():
    return {"System": "Operation"}

app.include_router(user)
app.include_router(unit)
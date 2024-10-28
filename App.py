from fastapi import FastAPI
from Router.User_Router import user

app = FastAPI()
@app.get("/")
def Strar():
    return {"System": "Operation"}

app.include_router(user)
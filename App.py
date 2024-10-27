from fastapi import FastAPI
from Router.User_Router import user

app = FastAPI()
@app.get("/")
def Home():
    return {"System": "Operation"}

app.include_router(user)
from fastapi import FastAPI
from Router.User_Router import user

app = FastAPI()
app.include_router(user)
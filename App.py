from fastapi            import FastAPI
from Routes.Route_User  import *

app = FastAPI()
A
app.include_router(Route_user)
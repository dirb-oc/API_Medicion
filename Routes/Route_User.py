from fastapi import APIRouter

Route_user = APIRouter()

@Route_user.get('/')
def HelloWorld():
    return "Hello world"

@Route_user.get('/user/')
def Users():
    return "Hello world"

@Route_user.post('/user/')
def Create_User():
    return "Hello world"

@Route_user.put('/user/')
def Update_User():
    return "Hello world"

@Route_user.delete('/user/')
def Eliminate_User():
    return "Hello world"
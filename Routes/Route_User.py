from fastapi import APIRouter

Route_user = APIRouter()

@Route_user.get('/')
def Users():
    return "Hello world"

@Route_user.post('/')
def Create_User():
    return "Hello world"

@Route_user.put('/')
def Update_User():
    return "Hello world"

@Route_user.delete('/')
def Eliminate_User():
    return "Hello world"
from fastapi import APIRouter
from Database.Base import conn
from Models.Model_User import Model_User as M_User

Route_user = APIRouter()

@Route_user.get('/')
def HelloWorld():
    return "Hello world"

@Route_user.get('/users/')
def Users():
    return conn.execute(M_User.select()).fetchall()

@Route_user.post('/user/')
def Create_User():
    return "Hello world"

@Route_user.put('/user/')
def Update_User():
    return "Hello world"

@Route_user.delete('/user/')
def Eliminate_User():
    return "Hello world"
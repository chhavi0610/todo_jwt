from pydantic import BaseModel

class ReisterUser(BaseModel):
    name:str
    email:str
    password: str

class LoginUser(BaseModel):
    email:str
    password: str

class AddTask(BaseModel):
    title: str


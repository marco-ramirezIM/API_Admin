from pydantic import BaseModel
from pydantic import Field
from datetime import datetime


class SuperAdmin(BaseModel):
    nombres:str=Field(...)
    correo:str=Field(...)
    role:str=Field(...)
    password:str=Field(...)
    state:int=Field(default=1)
    createdAt:datetime=datetime.now()




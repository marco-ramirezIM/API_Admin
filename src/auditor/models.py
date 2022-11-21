import pydantic
from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field


class User(BaseModel):
    nombre:str=Field(...)
    correo:str=Field(...)
    password:str=Field(...)
    state:int=Field(default=1)
    clusters:List[str]
    campaigns:List[str]
    createdBy:str=Field(...,description="Admin id")
    role:str=Field(...)
    conversacion:bool
    createdAt:datetime=datetime.now()
    




    
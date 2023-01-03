from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field

class AdminCreate(BaseModel):
    first_name:str=Field(...)
    last_name :str=Field(...)
    phone :str=Field(...)
    identification:str=Field(...)
    email :str=Field(...)
    password :str=Field(...)
    photo :str=Field(...)
    company_name:str=Field(...)
    
    
    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    id:str
    role_id :str=Field(...)
    first_name:str=Field(...)
    last_name :str=Field(...)
    phone :str=Field(...)
    identification:str=Field(...)
    email :str=Field(...)
    state :int=Field(default=1)
    photo :str=Field(...)
    company_name:str=Field(...)
    created_at:datetime=datetime.now()

    class Config:
        orm_mode = True

class AdminUpdate(BaseModel):
    first_name:str=Field(...)
    last_name :str=Field(...)
    phone :str=Field(...)
    identification:str=Field(...)
    email :str=Field(...)
    password :str=Field(...)
    state :int=Field(default=1)
    photo :str=Field(...)
    company_name:str=Field(...)


    



    



    
     
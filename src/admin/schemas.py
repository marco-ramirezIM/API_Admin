from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field

class AdminCreate(BaseModel):
    phone:str=Field(...)
    photo:str=Field(...)
    company_name:str=Field(...)
    identification:str=Field(...)
    minute_value:Optional[float]=0
    user_id:str

    class Config:
        orm_mode = True

class AdminBase(BaseModel):
    id:str
    phone:str=Field(...)
    photo:str=Field(...)
    company_name:str=Field(...)
    created_at:datetime=datetime.now()
    identification:str=Field(...)
    minute_value:Optional[float]=0
    user_id:str

    class Config:
        orm_mode = True

class AdminUpdate(BaseModel):
    phone:str=Field(...)
    photo:str=Field(...)
    company_name:str=Field(...)
    minute_value:Optional[float]=0

class UserBase(BaseModel):
    id:str
    email: str=Field(...)
    password : str=Field(...)
    first_name : str=Field(...)
    last_name : str=Field(...)
    state :int=Field(default=1)
    photo : str=Field(...)
    role_id :str
    



    



    
     
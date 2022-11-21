from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field



class Customer(BaseModel):
    id:str
    photo:str=Field(...)
    name:str=Field(...)
    created_by:str
    state:int=Field(default=1)
    created_at:datetime=datetime.now()

    class Config:
        orm_mode = True

class AuditorBase(BaseModel):
    user_id:str=Field(...)
    created_by:str=Field(description="Admin id")
    created_at:datetime=datetime.now()

    class Config:
        orm_mode = True

class AuditorCreate(AuditorBase):
    pass

class Auditor(AuditorBase):
    id:str
    
class CustomerCreate(Customer):
    pass


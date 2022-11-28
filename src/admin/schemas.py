from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field



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



    



    
     
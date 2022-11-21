from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field



class Campaign(BaseModel):
  id:str
  name :str=Field(...)
  photo:str=Field(...)
  state:int=Field(default=1)
  country:str=Field(...)
  is_conversation:int=Field(default=0)
  is_mac:int=Field(default=0)
  created_at:datetime=datetime.now()
  client_id:str
  created_by:str
  
  class Config:
    orm_mode = True



    


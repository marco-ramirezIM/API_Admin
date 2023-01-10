from typing import List
from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class GroupingBase(BaseModel):
    id: str
    name: str = Field(...)
    photo: str = Field(...)
    state: bool = Field(...)
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True

class GroupingCreate(BaseModel):
    name: str = Field(...)
    state: bool = Field(...)
    users: List[str] = Field(...)
    
    class Config:
        orm_mode = True
from typing import List, Union
from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class GroupingManagementBase(BaseModel):
    id: str
    name: str = Field(...)
    photo: str = Field(...)
    state: bool = Field(...)
    company_id: str = Field(...)
    list_audits: Union[str, None] = None

    class Config:
        orm_mode = True

class GroupingBase(BaseModel):
    id: str
    name: str = Field(...)
    photo: str = Field(...)
    state: bool = Field(...)
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True

class GroupingCreate(BaseModel):
    name: str = Field(..., min_length=5)
    state: bool = Field(...)
    associated_company: str = Field(...)
    users: Union[List[str], None] = None
    
    class Config:
        orm_mode = True
    
class GroupingUpdate(BaseModel):
    name: str = Field(..., min_length=5)
    state: bool = Field(...)
    users: Union[List[str], None] = None
    
    class Config:
        orm_mode = True
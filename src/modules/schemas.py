from pydantic import BaseModel
from pydantic import Field


class ModuleBase(BaseModel):
    id: str
    module: str = Field(...)
    category_id: str = Field(...)

    class Config:
        orm_mode = True


class ModuleList(BaseModel):
    id: str
    module: str = Field(...)
    category_id: str = Field(...)

    class Config:
        orm_mode = True


class ModuleUpdateOrCreate(BaseModel):
    module: str = Field(...)
    category_id: str = Field(...)
    campaign_id: str = Field(...)

    class Config:
        orm_mode = True

from pydantic import BaseModel
from pydantic import Field
from datetime import datetime


class CategoryBase(BaseModel):
    id: str = Field(...)
    category: str = Field(...)
    campaign_id: str = Field(...)
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True


class CategoryUpdateOrCreate(BaseModel):
    category: str = Field(..., min_length=5)
    campaign_id: str = Field(...)

    class Config:
        orm_mode = True

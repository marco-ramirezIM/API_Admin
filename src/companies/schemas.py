from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class CompanyCreate(BaseModel):
    first_name: str = Field(...,min_length=4)
    last_name: str = Field(...,min_length=4)
    phone: str = Field(...,min_length=4)
    identification: str = Field(...,min_length=4)
    email: str = Field(...,min_length=6)
    password: str = Field(...,min_length=8)
    photo: str = Field(...)
    company_name: str = Field(...,min_length=3)

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    id: str
    phone: str = Field(...)
    identification: str = Field(...)
    email: str = Field(...)
    state: int = Field(default=1)
    company_name: str = Field(...)
    full_name: str = Field(...)

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    id: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone: str = Field(...)
    identification: str = Field(...)
    email: str = Field(...)
    state: int = Field(default=1)
    photo: str = Field(...)
    company_name: str = Field(...)
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True


class CompanyUpdate(BaseModel):
    first_name: str = Field(...,min_length=4)
    last_name: str = Field(...,min_length=4)
    phone: str = Field(...,min_length=4)
    identification: str = Field(...,min_length=4)
    email: str = Field(...,min_length=6)
    password: str = Field(...,min_length=8)
    state: int = Field(default=1)
    photo: str = Field(...)
    company_name: str = Field(...,min_length=3)

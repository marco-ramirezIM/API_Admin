from pydantic import BaseModel
from datetime import datetime
from pydantic import Field


class CompanyCreate(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone: str = Field(...)
    identification: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    photo: str = Field(...)
    company_name: str = Field(...)

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
    first_name: str = Field(...)
    last_name: str = Field(...)
    phone: str = Field(...)
    identification: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
    state: int = Field(default=1)
    photo: str = Field(...)
    company_name: str = Field(...)

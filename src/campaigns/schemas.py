from pydantic import BaseModel, validator, Field
from datetime import datetime
from typing import List, Union
import re


class Campaign(BaseModel):
    id: str
    name: str = Field(...)
    photo: str = Field(...)
    state: bool = Field(...)
    country: str = Field(...)
    is_conversation: bool = Field(...)
    is_mac: bool = Field(...)
    grouping_id: str = Field(...)
    created_at: datetime = datetime.now()

    class Config:
        orm_mode = True


class CampaingCreate(BaseModel):
    name: str = Field(...)
    state: bool = Field(...)
    country: str = Field(...)
    users : Union[List[str], None] = None
    is_conversation: bool = Field(...)
    is_mac: bool = Field(...)
    grouping_id: str = Field(...)

    class Config:
        orm_mode = True

    @validator("name")
    def validate_name(cls, name: str):
        nm = name.strip()
        if bool(re.match("^[a-zA-Z]+( [a-zA-Z]+)*$", nm)) == False:
            raise ValueError(
                "The name of the campaign can't contain special characters or numbers and can't be empty"
            )
        return nm

    @validator("state")
    def validate_state(cls, state: int):
        if state != 1 and state != 0:
            raise ValueError("The state of the campaign can't be different from 1 or 0")
        return state

    @validator("country")
    def validate_country(cls, country: str):
        co = country.strip()
        if co == "":
            raise ValueError("The country of the campaign can't be empty")
        return co

    @validator("is_conversation")
    def validate_is_conversation(cls, is_conversation: int):
        if is_conversation != 1 and is_conversation != 0:
            raise ValueError(
                "The campaign's conversation state can't be different from 1 or 0"
            )
        return is_conversation

    @validator("is_mac")
    def validate_is_mac(cls, is_mac: int):
        if is_mac != 1 and is_mac != 0:
            raise ValueError("The campaign's mac state can't be different from 1 or 0")
        return is_mac

    @validator("grouping_id")
    def validate_grouping_id(cls, grouping_id: str):
        gp = grouping_id.strip()
        if gp == "":
            raise ValueError("The grouping_id of the campaign can't be empty")
        return gp


class UpdateCampaign(BaseModel):
    state: bool = Field(...)
    users: List[str] = Field(...)
    is_conversation: bool = Field(...)
    is_mac: bool = Field(...)

    class Config:
        orm_mode = True

    @validator("state")
    def validate_state(cls, state: bool):
        if state != True and state != False:
            raise ValueError("The state of the campaign can't be different from 1 or 0")
        return state

    @validator("is_conversation")
    def validate_is_conversation(cls, is_conversation: bool):
        if is_conversation != True and is_conversation != False:
            raise ValueError(
                "The campaign's conversation state can't be different from 1 or 0"
            )
        return is_conversation

    @validator("is_mac")
    def validate_is_mac(cls, is_mac: bool):
        if is_mac != True and is_mac != False:
            raise ValueError("The campaign's mac state can't be different from 1 or 0")
        return is_mac


class CampaignAccess(BaseModel):
    id: str = Field(...)
    user_id: str = Field(...)
    grouping_id: str = Field(...)
    campaign_id: str = Field(...)

    class Config:
        orm_mode = True

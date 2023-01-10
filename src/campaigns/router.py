from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from src.campaigns import service
from src.campaigns.schemas import Campaign, CampaingCreate, UpdateCampaign
from config.db import Session
from typing import List, Union
import src.campaigns.exceptions as campaign_exceptions
import dependencies as dp
import exceptions

campaignRouter = APIRouter(tags=["Campañas"])

# Create Campaigns
@campaignRouter.post("/campaigns")
async def create_campaign(
    name: str = Form(...),
    state: bool = Form(...),
    country: str = Form(...),
    users: Union[List[str], None] = None,
    is_conversation: bool = Form(...),
    is_mac: bool = Form(...),
    grouping_id: str = Form(...),
    file: Union[UploadFile, None] = None,
    session: Session = Depends(dp.get_db),
):
    try:
        if not file:
            raise exceptions.file_not_found_exception

        data = await file.read()
        dp.validate_file(file.content_type, data)

        if users[0] != "" or users != None:
            split_users = users[0].split(",")

        campaign = CampaingCreate(
            name=name,
            state=state,
            country=country,
            users=split_users if split_users else users,
            is_conversation=is_conversation,
            is_mac=is_mac,
            grouping_id=grouping_id,
        )

        return service.create_campaign(campaign, data, session)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise exceptions.entity_error_exception("crear la campaña")


# Update Campaign
@campaignRouter.put("/campaigns/{campaign_id}")
async def update_campaign(
    campaign_id: str,
    name: str = Form(...),
    state: bool = Form(...),
    users: Union[List[str], None] = None,
    is_conversation: bool = Form(...),
    is_mac: bool = Form(...),
    file: Union[UploadFile, None] = None,
    session: Session = Depends(dp.get_db),
):
    try:
        data = ""
        if file:
            data = await file.read()
            dp.validate_file(file.content_type, data)

        if not users:
            raise campaign_exceptions.users_list_exception

        if users[0] != "" or users != None:
            split_users = users[0].split(",")

        campaign = UpdateCampaign(
            name=name,
            state=state,
            users=split_users if split_users else users,
            is_conversation=is_conversation,
            is_mac=is_mac,
        )

        return service.edit_campaign(session, campaign_id, data, campaign)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("actualizar la campaña")


# Get all Campaigns
@campaignRouter.get("/campaigns", response_model=List[Campaign])
async def get_campaigns(session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaigns(session)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener las campañas")


# Get campaign by ID
@campaignRouter.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaign(session, campaign_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener la campaña")


# Get campaigns by grouping ID
@campaignRouter.get("/campaigns/grouping/{grouping_id}", response_model=List[Campaign])
async def get_campaigns_grouping(
    grouping_id: str, session: Session = Depends(dp.get_db)
):
    try:
        return service.get_campaigns_grouping(session, grouping_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception(
            "obtener las campañas asociadas a un grupo"
        )


# Get campaigns by agent ID
@campaignRouter.get("/campaigns/agents/{agent_id}", response_model=List[Campaign])
async def get_campaigns_agent(agent_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaings_agent(session, agent_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception(
            "obtener las campañas asociadas a un agente"
        )

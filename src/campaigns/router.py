from fastapi import APIRouter, Depends, HTTPException
from src.campaigns import service
from src.campaigns.schemas import Campaign, CampaingCreate, UpdateCampaign
from config.db import Session
from typing import List
import dependencies as dp
import exceptions

campaignRouter=APIRouter(tags=["Campañas"])

# Create Campaigns
@campaignRouter.post("/campaigns")
async def create_campaign(
    campaing: CampaingCreate, session: Session = Depends(dp.get_db)
):
    try:
        return service.create_campaign(campaing, session)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise exceptions.entity_error_exception("crear la campaña")


# Update Campaign
@campaignRouter.put("/campaigns")
async def update_campaign(
    campaign: UpdateCampaign, id: str, session: Session = Depends(dp.get_db)
):
    try:
        return service.edit_campaign(session, id, campaign)
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
        raise exceptions.entity_error_exception("obtener las campañas asociadas a un grupo")


# Get campaigns by agent ID
@campaignRouter.get("/campaigns/agents/{agent_id}", response_model=List[Campaign])
async def get_campaigns_agent(agent_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaings_agent(session, agent_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise exceptions.entity_error_exception("obtener las campañas asociadas a un agente")

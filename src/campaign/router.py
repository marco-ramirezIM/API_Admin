from fastapi import APIRouter, Depends, HTTPException
from src.campaign import service
import src.campaign.exceptions as campaign_exceptions
from src.campaign.schemas import Campaign, CampaingCreate, UpdateCampaign
from config.db import Session
from typing import List
import dependencies as dp

campaignRouter = APIRouter(tags=["Campaign"])

# Create Campaigns
@campaignRouter.post("/campaigns")
async def create_campaign(
    campaing: CampaingCreate, session: Session = Depends(dp.get_db)
):
    try:
        return service.create_campaign(campaing, session)
    except HTTPException as e:
        raise e
    except Exception:
        raise campaign_exceptions.create_campaign_exception


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
        raise campaign_exceptions.update_campaign_exception


# Get all Campaigns
@campaignRouter.get("/campaigns", response_model=List[Campaign])
async def get_campaigns(session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaigns(session)
    except HTTPException as e:
        raise e
    except Exception:
        raise campaign_exceptions.get_campaigns_exception


# Get campaign by ID
@campaignRouter.get("/campaigns/{campaign_id}", response_model=Campaign)
async def get_campaign(campaign_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaign(session, campaign_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise campaign_exceptions.get_campaign_by_id_exception


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
        raise campaign_exceptions.get_groupings_campaigns_exception


# Get campaigns by agent ID
@campaignRouter.get("/campaigns/agents/{agent_id}", response_model=List[Campaign])
async def get_campaigns_agent(agent_id: str, session: Session = Depends(dp.get_db)):
    try:
        return service.get_campaings_agent(session, agent_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise campaign_exceptions.get_agents_campaigns_exception

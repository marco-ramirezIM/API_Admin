from fastapi import APIRouter,Depends
from src.campaign import service
from src.campaign.schemas import Campaign
from config.db import Session
from typing import List
from src.campaign import dependencies as dp

campaignRouter=APIRouter(tags=["Campaign"])

@campaignRouter.get('/campaigns',response_model=List[Campaign])
async def get_campaigns(session:Session=Depends(dp.get_db)):
    return service.get_campaigns(session)

@campaignRouter.get('/campaigns/{campaign_id}',response_model=Campaign)
async def get_campaign(campaign_id:str,session:Session=Depends(dp.get_db)):
    return service.get_campaign(session,campaign_id)

@campaignRouter.get('/campaigns/admin/{admin_id}',response_model=List[Campaign])
async def get_campaigns_admin(admin_id:str,session:Session=Depends(dp.get_db)):
    return service.get_campaigns_admin(session,admin_id)

@campaignRouter.get('/campaigns/client/{client_id}',response_model=List[Campaign])
async def get_campaigns_client(client_id:str,session:Session=Depends(dp.get_db)):
    return service.get_campaigns_client(session,client_id)
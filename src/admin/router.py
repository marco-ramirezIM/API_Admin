from fastapi import APIRouter,Depends
from src.admin import service
from src.admin.schemas import AdminBase
from config.db import Session
from typing import List
from src.admin import dependencies as dp

adminRouter=APIRouter(tags=["Admin"])

@adminRouter.get('/administrators',response_model=List[AdminBase])
async def get_administrators(session:Session=Depends(dp.get_db)):
    return service.get_administrators(session)
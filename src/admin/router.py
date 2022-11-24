from fastapi import APIRouter,Depends
from src.admin import service
from src.admin.schemas import AdminBase,AdminUpdate
from config.db import Session
from typing import List
import dependencies as dp

adminRouter=APIRouter(tags=["Admin"])

@adminRouter.get('/administrators',response_model=List[AdminBase])
async def get_administrators(session:Session=Depends(dp.get_db)):
    return service.get_administrators(session)

@adminRouter.get('/administrators/{admin_id}',response_model=AdminBase)
async def get_admin(admin_id:str,session:Session=Depends(dp.get_db)):
    return service.get_admin(session,admin_id)

@adminRouter.put('/administrators/{admin_id}',response_model=AdminBase)
async def update_admin(admin_id:str,admin:AdminUpdate,session:Session=Depends(dp.get_db)):
    return service.update_admin(session,admin_id,admin)
    
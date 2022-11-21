from fastapi import APIRouter
from src.auditor.service import AuditorService

auditorRouter=APIRouter(tags=["Auditor"])

@auditorRouter.get('/auditors')
async def get_auditors():
    return AuditorService().get_auditors()
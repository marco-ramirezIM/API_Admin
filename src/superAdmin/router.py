from fastapi import APIRouter
from src.superAdmin.service import SuperAdminService

superAdminRouter=APIRouter(tags=["Super_Admin"])

@superAdminRouter.get('/superAdmins')
async def get_super_admins():
    return SuperAdminService().get_super_admins()

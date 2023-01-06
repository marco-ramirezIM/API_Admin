from fastapi import FastAPI
from config.tags import tags_metadata
from src.admin.router import adminRouter
from src.campaign.router import campaignRouter
from src.customer.router import customerRouter
from src.superAdmin.router import superAdminRouter
from config.setup import settings


app=FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    openapi_tags=tags_metadata,
    docs_url=settings.URL_PREFIX + '/docs',
    redoc_url=settings.URL_PREFIX + '/redoc',
    openapi_url=settings.URL_PREFIX + '/openapi.json'
)

app.include_router(adminRouter, prefix=settings.URL_PREFIX)
app.include_router(campaignRouter, prefix=settings.URL_PREFIX)
app.include_router(customerRouter, prefix=settings.URL_PREFIX)
app.include_router(superAdminRouter, prefix=settings.URL_PREFIX)
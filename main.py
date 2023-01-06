from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.tags import tags_metadata
from src.companies.router import companyRouter
from src.campaign.router import campaignRouter
from src.customer.router import customerRouter
from config.setup import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    openapi_tags=tags_metadata,
    docs_url=settings.URL_PREFIX + "/docs",
    redoc_url=settings.URL_PREFIX + "/redoc",
    openapi_url=settings.URL_PREFIX + "/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companyRouter, prefix=settings.URL_PREFIX)
app.include_router(campaignRouter, prefix=settings.URL_PREFIX)
app.include_router(customerRouter, prefix=settings.URL_PREFIX)

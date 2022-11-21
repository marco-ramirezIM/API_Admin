import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME = "ISA 2 - Administration API"
    PROJECT_DESCRIPTION = "REST API for iMetrix Admin using FastAPI and Postgresql"
    PROJECT_VERSION ="0.0.1"
    PROJECT_DB=os.getenv('MONGODB_URI')
    DB_HOST=os.getenv('DB_HOST')
    DB_USER=os.getenv('DB_USER')
    DB_PASSWORD=os.getenv('DB_PASSWORD')
    DB_NAME=os.getenv('DB_NAME')
    URL_PREFIX="/api/v1"

settings = Settings()
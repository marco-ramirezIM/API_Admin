import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class B2C_Settings:
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    AUTHORITY = os.getenv("AUTHORITY")
    SCOPE = os.getenv("SCOPE")
    BASE_URL_GRAPH = os.getenv("BASE_URL_GRAPH")

class AZURE_Blob_Settings:
    STRING_CONNECTION = os.getenv("AZURE_BLOB_STORAGE_STRING_CONNECTION")

class DB_Settings:
    HOST = os.getenv("DB_HOST")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    NAME = os.getenv("DB_NAME")


class Settings:
    PROJECT_NAME = "ISA 2 - API"
    PROJECT_DESCRIPTION = "REST API for ISA 2 - Imetrix"
    PROJECT_VERSION = "0.0.2"
    URL_PREFIX = "/api/v1"
    DB_CONNECTION = DB_Settings()
    AZURE_B2C = B2C_Settings()
    AZURE_BLOB_STORAGE = AZURE_Blob_Settings()


settings = Settings()

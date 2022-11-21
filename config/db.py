from pymongo import MongoClient
from config.setup import settings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://" + settings.DB_USER + ":" + settings.DB_PASSWORD + "@" + settings.DB_HOST + "/" + settings.DB_NAME)
meta_data = MetaData()
conn=MongoClient(settings.PROJECT_DB)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


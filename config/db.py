from config.setup import settings
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(
    "postgresql://"
    + settings.DB_CONNECTION.USER
    + ":"
    + settings.DB_CONNECTION.PASSWORD
    + "@"
    + settings.DB_CONNECTION.HOST
    + "/"
    + settings.DB_CONNECTION.NAME
)
meta_data = MetaData()
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

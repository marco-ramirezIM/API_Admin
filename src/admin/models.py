from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field
from config.db import engine, meta_data
from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import String,Float,Boolean,DateTime
from sqlalchemy.orm import relationship
from config.db import Base



class Admin(Base):
    __tablename__ = "administrators"
    id = Column(String, primary_key=True)
    phone = Column(String(15), nullable=False)
    photo = Column(String(500),nullable=False )
    identification= Column(String(20),nullable=False )
    company_name=Column(String(50) ,nullable=False)
    minute_value=Column(Float, nullable=True)
    created_at=Column(DateTime,nullable=False)
    user_id=Column(String(24) ,nullable=False)
    


    
   
  
from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field
from config.db import engine, meta_data
from sqlalchemy import Table, Column,ForeignKey, SMALLINT
from sqlalchemy.sql.sqltypes import String,Float,Boolean,DateTime,Integer
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
    user_id=Column(String(24),ForeignKey("users.id") ,nullable=False)
    user=relationship("User")

class User(Base):
    __tablename__ = "users"
    id = Column(String(24), primary_key=True)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    state = Column(SMALLINT, nullable=False)
    photo = Column(String(500), nullable=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    description = Column(String(50), nullable=False)
    


    
   
  
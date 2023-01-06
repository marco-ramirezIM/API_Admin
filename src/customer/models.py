from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field
from config.db import engine, meta_data
from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import String,Boolean,DateTime, SMALLINT
from sqlalchemy.orm import relationship
from config.db import Base


clients_auditors = Table(
    "clients_auditors",
    Base.metadata,
    Column("client_id", ForeignKey("clients.id"), primary_key=True),
    Column("auditor_id", ForeignKey("auditors.id"), primary_key=True),
)

class Client(Base):
    __tablename__ = "clients"
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(500),nullable=False )
    state= Column(SMALLINT, nullable=False) 
    created_at=Column(DateTime,nullable=False)
    auditors=relationship("Auditor",secondary=clients_auditors,back_populates="clients")

class Auditor(Base):
    __tablename__ = "auditors"
    id = Column(String, primary_key=True)
    user_id=Column(String(24) ,nullable=False)
    created_by=Column(String(24) ,nullable=False)
    created_at=Column(DateTime,nullable=False)
    clients=relationship("Client",secondary=clients_auditors,back_populates="auditors")



            

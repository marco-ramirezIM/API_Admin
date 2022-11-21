from pydantic import BaseModel
from datetime import datetime
from typing import Optional,List
from pydantic import Field
from config.db import engine, meta_data
from sqlalchemy import Table, Column,ForeignKey
from sqlalchemy.sql.sqltypes import String,Boolean,DateTime
from sqlalchemy.orm import relationship
from config.db import Base


campaigns_auditors = Table(
    "campaigns_auditors",
    Base.metadata,
    Column("campaign_id", ForeignKey("campaigns.id"), primary_key=True),
    Column("auditor_id", ForeignKey("auditors.id"), primary_key=True),
)

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(500),nullable=False )
    state= Column(Boolean,nullable=False )
    country = Column(String(5),nullable=False )
    is_conversation= Column(Boolean,nullable=False )
    is_mac= Column(Boolean,nullable=False )
    created_at=Column(DateTime,nullable=False)
    client_id=Column(String(24) ,nullable=False)
    created_by=Column(String(24) ,nullable=False)
    auditors=relationship("Auditor",secondary=campaigns_auditors,back_populates="campaigns")



 
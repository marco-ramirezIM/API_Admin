from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, DateTime, SMALLINT
from config.db import Base
from sqlalchemy.orm import relationship


class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(String, primary_key=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(500), nullable=False)
    state = Column(SMALLINT, nullable=False)
    country = Column(String(5), nullable=False)
    is_conversation = Column(SMALLINT, nullable=False)
    is_mac = Column(SMALLINT, nullable=False)
    grouping_id = Column(String(24), ForeignKey("clients.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    campaing_access = relationship("CampaingAccess")


class CampaingAccess(Base):
    __tablename__ = "campaigns_access"
    id = Column(String, primary_key=True)
    user_id = Column(String(24), ForeignKey("administrators.id"), nullable=False)
    campaing_id = Column(String(24), ForeignKey("campaigns.id"), nullable=False)
    user = relationship("Company")

from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, DateTime, SMALLINT
from config.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(500), nullable=False)
    state = Column(SMALLINT, nullable=False)
    country = Column(String(5), nullable=False)
    is_conversation = Column(SMALLINT, nullable=False)
    is_mac = Column(SMALLINT, nullable=False)
    grouping_id = Column(UUID, ForeignKey("groupings.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    campaign_access = relationship("CampaignAccess")


class CampaignAccess(Base):
    __tablename__ = "campaigns_access"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    campaign_id = Column(UUID, ForeignKey("campaigns.id"), nullable=False)

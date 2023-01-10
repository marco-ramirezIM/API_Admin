from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, DateTime
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID

class Category(Base):
    __tablename__ = "categories"
    id = Column(UUID, primary_key=True)
    campaign_id = Column(UUID, ForeignKey("campaigns.id"), nullable=False)
    category = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=True)
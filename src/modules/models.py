from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from config.db import Base


class Module(Base):
    __tablename__ = "modules"
    id = Column(UUID, primary_key=True)
    campaign_id = Column(UUID, ForeignKey("campaigns.id"), nullable=False)
    category_id = Column(UUID, ForeignKey("categories.id"), nullable=False)
    module = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=True)

from sqlalchemy import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, TIMESTAMP, SMALLINT
from config.db import Base
from sqlalchemy.dialects.postgresql import UUID

class Grouping(Base):
    __tablename__ = "groupings"
    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False)
    photo = Column(String(500), nullable=False)
    state = Column(SMALLINT, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)


class UserGrouping(Base):
    __tablename__ = "user_groupings"
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    grouping_id = Column(UUID, ForeignKey("groupings.id"), nullable=False)


class GroupingManagement(Base):
    __tablename__ = "grouping_management"
    id = Column(UUID, primary_key=True)
    company_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    name = Column(String(50), nullable=False)
    photo = Column(String(500), nullable=False)
    state = Column(SMALLINT, nullable=False)
    list_audits = Column(String, nullable=False)
from sqlalchemy import Column
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

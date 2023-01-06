from sqlalchemy import Column, ForeignKey, SMALLINT
from sqlalchemy.sql.sqltypes import String, DateTime, Integer
from config.db import Base


class Company(Base):
    __tablename__ = "administrators"
    id = Column(String, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)
    identification = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    state = Column(SMALLINT, nullable=False)
    photo = Column(String(500), nullable=False)
    company_name = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=True)


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    description = Column(String(50), nullable=False)

from sqlalchemy import (
    Column, String, Text, Integer,
)

from db.database import Base


class Manager(Base):
    __tablename__ = 'manager'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String)
    branch = Column(String)

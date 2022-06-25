from sqlalchemy import (
    Column, String, Text, Integer,
)

from db.database import Base


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    code = Column(Integer)
    name = Column(String)

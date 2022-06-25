from sqlalchemy import (
    Column, String, Text, Integer, ForeignKey
)
from sqlalchemy.orm import relationship

from db.database import Base


class Tables(Base):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    table_name = Column(String, index=True)
    project_id = Column(Integer, ForeignKey('project.id', ondelete='CASCADE'))

    project = relationship('Project', back_populates='tables')


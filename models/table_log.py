from datetime import datetime

from sqlalchemy import (
    Column, String, DateTime,
    Integer, ForeignKey, BigInteger
)
from sqlalchemy.orm import relationship

from db.database import Base


class Log(Base):
    __tablename__ = 'log'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    project_id = Column(Integer, ForeignKey('project.id', ondelete='CASCADE'))
    table_id = Column(Integer, ForeignKey('tables.id', ondelete='CASCADE'))
    row_id = Column(BigInteger)
    created_date = Column(DateTime, default=datetime.utcnow)
    manager_id = Column(Integer, ForeignKey('manager.id', ondelete='CASCADE'))
    new_value = Column(String)

    project = relationship('Project', back_populates='log')
    tables = relationship('Tables', back_populates='log')
    manager = relationship('Manager', back_populates='log')


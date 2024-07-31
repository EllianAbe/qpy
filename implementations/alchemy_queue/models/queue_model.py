from ..base import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class QueueModel(Base):
    __tablename__ = 'alchemy_queue'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    items = relationship('alchemy_item', back_populates='queue',
                         cascade='all, delete-orphan')

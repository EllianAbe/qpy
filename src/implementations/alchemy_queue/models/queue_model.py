from ..base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class QueueModel(Base):
    __tablename__ = 'alchemy_queue'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    items = relationship('ItemModel', back_populates='queue',
                         cascade='all, delete-orphan')
    max_retry_count = Column(Integer, default=3)

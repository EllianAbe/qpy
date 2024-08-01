from ..base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, JSON, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
import enum


class ItemStatus(enum.Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    ERROR = 'error'
    REMOVED = 'removed'


class ItemModel(Base):
    __tablename__ = 'alchemy_item'
    id = Column(Integer, primary_key=True)
    queue_id = Column(Integer, ForeignKey('alchemy_queue.id'), nullable=False)
    queue = relationship('QueueModel', back_populates='items')
    creation_datetime = Column(DateTime, default=datetime.now())
    status = Column(Enum(ItemStatus), default=ItemStatus.PENDING)
    retry_count = Column(Integer, default=0)

    data = Column(JSON)
    output_data = Column(JSON)

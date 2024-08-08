from ..base import Base
from datetime import datetime
from sqlalchemy import Column, Integer, JSON, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from .item_status import ItemStatus


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

from ..utils import named_instance
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, JSON, ForeignKey, DateTime, Enum


Base = named_instance.get('Base', declarative_base())


class ItemStatus(Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    SUCCESS = 'success'
    ERROR = 'error'


class ItemModel(Base):
    __tablename__ = 'alchemy_item'
    id = Column(Integer, primary_key=True)
    queue_id = Column(Integer, ForeignKey('alchemy_queue.id'), nullable=False)
    creation_datetime = Column(DateTime, default=DateTime())
    status = Column(ItemStatus, default=ItemStatus.PENDING)
    retry_count = Column(Integer, default=0)

    data = Column(JSON)
    output_data = Column(JSON)

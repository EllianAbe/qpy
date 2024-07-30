from ..utils import named_instance
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, JSON, ForeignKey


Base = named_instance.get('Base', declarative_base())


class ItemModel(Base):
    __tablename__ = 'alchemy_item'
    id = Column(Integer, primary_key=True)
    queue_id = Column(Integer, ForeignKey('alchemy_queue.id'), nullable=False)
    data = Column(JSON)

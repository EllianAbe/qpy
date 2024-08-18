from src.base_classes import AbstractQueueItem
from datetime import datetime
from .item_status import MongoItemStatus


class MongoQueueItem(AbstractQueueItem):
    def __init__(self, data: dict, output_data: dict = None,
                 status: MongoItemStatus = MongoItemStatus.PENDING,
                 creation_date: datetime = datetime.now(),
                 retry_count: int = 0,
                 id=None, eligible_date: datetime = datetime.now()):
        self.data = data
        self.status = status
        self.output_data = output_data
        self.creation_date = creation_date
        self.retry_count = retry_count
        self.id = id
        self.eligible_date = eligible_date

    def to_dict(self) -> dict:
        return {
            'data': self.data,
            'output_data': self.output_data,
            'status': self.status,
            'creation_date': self.creation_date,
            'retry_count': self.retry_count,
            'eligible_date': self.eligible_date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MongoQueueItem":
        item = cls(data['data'], data['output_data'], data['status'],
                   data['creation_date'], data['retry_count'], data['_id'],
                   data.get('eligible_date', datetime.now()))

        return item

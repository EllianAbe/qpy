from pymongo.database import Database
from typing import Sequence
from abstractions import AbstractQueue, AbstractQueueItem
from .item import MongoQueueItem
from .item_status import MongoItemStatus


class MongoQueue(AbstractQueue):
    def __init__(self, db: Database, name):
        self._db = db
        self._collection = db.get_collection(name)

    def add(self, data: dict) -> MongoQueueItem:

        item = MongoQueueItem(data)

        result = self._collection.insert_one(item.to_dict())
        item.id = result.inserted_id

        return item

    def enqueue_item(self, item: MongoQueueItem | dict):

        raise NotImplementedError()

    def get_next(self) -> MongoQueueItem:
        next_item = self._collection.find_one_and_update(
            {'status': MongoItemStatus.PENDING},
            {'$set': {'status': MongoItemStatus.PROCESSING}},
            sort=[('creation_date', 1)]
        )

        if not next_item:
            return None

        item = MongoQueueItem.from_dict(next_item)

        return item

    def get_items(self, filters={}) -> Sequence[MongoQueueItem]:
        if 'id' in filters:
            filters['_id'] = filters.pop('id')

        items = self._collection.find(filters)
        items = [MongoQueueItem.from_dict(item) for item in items]

        return items

    def is_empty(self):
        return self._collection.find_one() is None

    def has_pending_items(self):
        return self._collection.find_one({'status': MongoItemStatus.PENDING}) is not None

    def remove_item(self, item: AbstractQueueItem):
        self.update_item(item, MongoItemStatus.REMOVED)

    def update_item(self, item: MongoQueueItem, status: MongoItemStatus):
        item.status = status

        self._collection.update_one(
            {'_id': item.id}, {'$set': item.to_dict()})

    def dispatcher(self, func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)

            item = self.add(data)

            return item

        return wrapper

    def __str__(self) -> str:
        return '\n'.join(f'{index} {str(item)}' for index, item in enumerate(self.data, 1))

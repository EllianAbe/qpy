from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abstractions import AbstractQueue
from implementations.alchemy_queue.models import QueueModel, ItemModel
from implementations.alchemy_queue.models.item_model import ItemStatus
from ..repository import QueueRepository, ItemRepository


class AlchemyQueue(AbstractQueue):
    def __init__(self, queue_repository: QueueRepository, item_repository: ItemRepository, name: str):
        self._queue_repository = queue_repository
        self._item_repository = item_repository
        self.name = name

        self.queue = self._queue_repository.get_by_name(name)

        if not self.queue:
            self.queue = QueueModel(name=self.name)
            self._queue_repository.add(self.queue)

    def add(self, data):
        item = ItemModel(data=data, queue_id=self.queue.id)
        self._item_repository.add(item)

    def enqueue_item(self, item):
        raise NotImplementedError()

    def get_next(self):
        return self._item_repository.get_next_by_queue(self.queue)

    def get_items(self) -> list:
        return self._queue_repository.get_items(self.name)

    def is_empty(self) -> bool:
        return not self.get_items()

    def has_pending_items(self) -> bool:
        return self._item_repository.has_pending_items(self.queue)

    def remove_item(self, item):
        self._item_repository.remove(item)

    def update_item(self, item, status):
        item.status = status

        if item.status == ItemStatus.ERROR:
            item.retry_count += 1
            item.status = \
                ItemStatus.PENDING \
                if item.retry_count < self.queue.max_retry_count \
                else ItemStatus.ERROR

        if item.retry_count > self.queue.max_retry_count:
            item.status = ItemStatus.ERROR

        self._item_repository.update(item)

    def dispatcher(self, func):
        pass

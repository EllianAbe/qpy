from datetime import datetime
from base_classes import AbstractQueue
from implementations.alchemy_queue.models import QueueModel, ItemModel
from implementations.alchemy_queue.models.item_model import AlchemyItemStatus
from ..repository import QueueRepository, ItemRepository
from sqlalchemy.orm import Session


class AlchemyQueue(AbstractQueue):
    def __init__(self, queue_repository: QueueRepository, item_repository: ItemRepository, name: str, max_retry_count=3):
        self._queue_repository = queue_repository
        self._item_repository = item_repository
        self.name = name

        self.queue = self._queue_repository.get_by_name(name)

        if not self.queue:
            self.queue = QueueModel(
                name=self.name, max_retry_count=max_retry_count)
            self._queue_repository.add(self.queue)

        self.max_retry_count = self.queue.max_retry_count

    @classmethod
    def from_session(cls, session: Session, name: str, max_retry_count=3):
        return cls(QueueRepository(session), ItemRepository(session), name, max_retry_count)

    def add(self, data, eligible_date=datetime.now()):
        item = ItemModel(data=data, queue_id=self.queue.id,
                         eligible_date=eligible_date)
        self._item_repository.add(item)

        return item

    def enqueue_item(self, item):
        raise NotImplementedError()

    def get_next(self):
        return self._item_repository.get_next_by_queue(self.queue)

    def get_item_by_id(self, item_id):
        return self._item_repository.get_item_by_id(item_id)

    def get_items(self, **filters) -> list[ItemModel]:
        if not filters:
            filters = {}

        filters['queue_id'] = self.queue.id

        return self._item_repository.get_items_by_filters(filters)

    def is_empty(self) -> bool:
        return not self.get_items()

    def has_pending_items(self, ignore_eligibility: bool = False) -> bool:
        return self._item_repository.has_pending_items(self.queue, ignore_eligibility)

    def remove_item(self, item_id):
        item = self.get_item_by_id(item_id)
        self._item_repository.remove(item)

    def update_item(self, item_id, status, output_data=None):
        item = super().update_item(item_id, status, output_data)

        self._item_repository.update()

    def postpone_item(self, item_id, eligible_date: datetime):
        item = self.get_item_by_id(item_id)

        item.eligible_date = eligible_date
        item.status = AlchemyItemStatus.PENDING

        self._item_repository.update()

    def dispatcher(self, func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)

            item = self.add(data)

            return item

        return wrapper

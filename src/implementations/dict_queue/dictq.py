from src.base_classes import AbstractQueue, AbstractQueueItem, ItemStatus
from typing import Sequence
from datetime import datetime
from .qitem import Item


class ChangeStatusError(Exception):
    pass


class DictQueue(AbstractQueue):
    def __init__(self, name, max_retry_count=0):
        self.name = name
        self.data = []
        self.max_retry_count = max_retry_count

    def add(self, data: dict, eligible_date=datetime.now()):
        item = Item(data, eligible_date=eligible_date)

        self.data.append(item)

        return item

    def enqueue_item(self, item: AbstractQueueItem):
        raise NotImplementedError('this queue does not support enqueue_item')

    def get_next(self) -> Item:

        next_item = next(
            (item for item in self.data
             if item.status == 'pending' and
             datetime.now() >= item.eligible_date), None)

        if not next_item:
            return next_item

        next_item.status = "processing"

        return next_item

    def get_items(self) -> Sequence[Item]:
        return self.data

    def is_empty(self):
        return len(self.data) == 0

    def has_pending_items(self, ignore_eligibility: bool = False):
        if ignore_eligibility:
            return any(item.status == 'pending' for item in self.data)

        return any(item.status == 'pending' and item.eligible_date <= datetime.now()
                   for item in self.data)

    def remove_item(self, item: Item):
        item.status = ItemStatus.REMOVED

    def update_item(self, item, status, output_data=None):
        if ItemStatus.is_final(item.status):
            raise ChangeStatusError(
                f'Cannot change status when status is {item._status}')

        item.status = status

        if output_data:
            item.output_data = output_data

        if item.status == ItemStatus.ERROR:
            item.retry_count += 1
            item.status = \
                ItemStatus.PENDING \
                if item.retry_count < self.max_retry_count \
                else ItemStatus.ERROR

            if self.max_retry_count == 0 or item.retry_count > self.max_retry_count:
                item.status = ItemStatus.ERROR

        return item

    def postpone_item(self, item, eligible_date: datetime):
        item.eligible_date = eligible_date
        item.status = ItemStatus.PENDING

    def get_item_by_id(self, item_id):
        raise NotImplementedError('this queue does not support get_item_by_id')

    def dispatcher(self, func):
        return super().dispatcher(func)

    def __str__(self) -> str:
        return '\n'.join(f'{index} {str(item)}' for index, item in enumerate(self.data, 1))

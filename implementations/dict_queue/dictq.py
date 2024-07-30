from abstractions import AbstractQueue, AbstractQueueItem
from typing import Sequence


class DictQueue(AbstractQueue):
    def __init__(self, data: list):
        self.data = data

    def add(self, item: AbstractQueueItem):
        self.enqueue_item(item)
        self.data.append(item)

    def enqueue_item(self, item: AbstractQueueItem):
        return super().enqueue_item(item)

    def get_next(self) -> AbstractQueueItem:

        next_item = next(
            (item for item in self.data if item.status == 'pending'), None)

        if not next_item:
            return None

        next_item.status = "processing"

        return next_item

    def get_items(self) -> Sequence[AbstractQueueItem]:
        return self.data

    def is_empty(self):
        return len(self.data) == 0

    def has_pending_items(self):
        return any(item.status == 'pending' for item in self.data)

    def remove_item(self, item: AbstractQueueItem):
        self.data.remove(item)

    def update_item(self, item: AbstractQueueItem, status):
        item.status = status

    def dispatcher(self, func):
        return super().dispatcher(func)

    def __str__(self) -> str:
        return '\n'.join(f'{index} {str(item)}' for index, item in enumerate(self.data, 1))

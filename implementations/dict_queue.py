from typing import Any, Sequence, Literal
from abstractions import AbstractQueue, AbstractQueueItem
from datetime import datetime


class DictQueue(AbstractQueue):
    def __init__(self, data: list):
        self.data = data

    def add(self, item: AbstractQueueItem):
        self.data.append(item)

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


class Item(AbstractQueueItem):
    def __init__(self, data: dict, output_data: dict = None,
                 status: Literal['pending', 'processing',
                                 'success', 'error'] = 'pending',
                 creation_date: datetime = datetime.now()):
        self.data = data
        self._status = status
        self.output_data = output_data
        self.creation_date = creation_date

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value: Literal['pending', 'processing', 'success', 'error']):
        self._status = value

    def validate_data(self, data_definition):
        pass

    def __str__(self) -> str:
        return f'Item: {self.data}, Status: {self.status}, creation_date: {self.creation_date}'

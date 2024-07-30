from typing import Literal
from abstractions import AbstractQueueItem
from datetime import datetime


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

    def enqueue(self, queue):
        super().enqueue(queue)

    def validate_data(self, data_definition):
        pass

    def __str__(self) -> str:
        return f'Item: {self.data}, Status: {self.status}, creation_date: {self.creation_date}'

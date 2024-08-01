from abc import ABC, abstractmethod
from typing import Literal
from datetime import datetime


class AbstractQueueItem(ABC):
    def __init__(self, data: dict, output_data: dict = None,
                 status: Literal['pending', 'processing',
                                 'success', 'error'] = 'pending',
                 creation_date: datetime = datetime.now(), retry_count: int = 0):
        self.data = data
        self._status = status
        self.output_data = output_data
        self.creation_date = creation_date
        self.retry_count = retry_count

from typing import Literal
from src.base_classes import AbstractQueueItem
from datetime import datetime


class Item(AbstractQueueItem):

    def __str__(self) -> str:
        return f'Item: {self.data}, Status: {self.status}, creation_date: {self.creation_date}'

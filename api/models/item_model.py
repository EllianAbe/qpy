from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class ItemStatus(str, Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    ERROR = 'error'
    SUCCESS = 'success'
    REMOVED = 'removed'


class ItemModel(BaseModel):
    id: int
    creation_datetime: datetime
    status: ItemStatus
    retry_count: int
    data: dict | None
    output_data: dict | None

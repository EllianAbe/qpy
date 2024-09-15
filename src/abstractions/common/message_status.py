from enum import Enum
from functools import cache


class ItemStatus(str, Enum):
    PENDING = 'pending'
    PROCESSING = 'processing'
    ERROR = 'error'
    SUCCESS = 'success'
    REMOVED = 'removed'
    __final_statuses__ = [ERROR, SUCCESS]

    @classmethod
    def is_final(cls, status):
        return status in cls.__final_statuses__

    @classmethod
    def is_valid(cls, status):
        return status in cls.__members__.values()


pass

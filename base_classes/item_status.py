class ItemStatus():
    PENDING = 'pending'
    PROCESSING = 'processing'
    ERROR = 'error'
    SUCCESS = 'success'
    REMOVED = 'removed'
    __final_statuses__ = [ERROR, SUCCESS]

    @classmethod
    def is_final(cls, status):
        return status in cls.__final_statuses__

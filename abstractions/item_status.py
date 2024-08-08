class ItemStatus():
    PENDING = 'pending'
    PROCESSING = 'processing'
    ERROR = 'error'
    SUCCESS = 'success'
    REMOVED = 'removed'

    @classmethod
    def is_final_status(cls, status):
        return status in [cls.SUCCESS, cls.ERROR]

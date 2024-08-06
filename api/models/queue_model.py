from pydantic import BaseModel


class QueueModel(BaseModel):
    name: str
    max_retry_count: int
    has_pending_items: bool
    is_empty: bool

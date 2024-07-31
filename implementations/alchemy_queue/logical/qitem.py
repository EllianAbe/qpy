from abstractions import AbstractQueueItem
from ..models.item_model import ItemModel


class Item(AbstractQueueItem, ItemModel):
    pass

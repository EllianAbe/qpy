from typing import Any
from ..models import ItemModel
from ..models.item_model import AlchemyItemStatus
from datetime import datetime


class ItemRepository():

    def __init__(self, session):
        self.session = session

    def add(self, item: ItemModel):
        self.session.add(item)
        self.session.commit()

    def remove(self, item: ItemModel):
        item.status = AlchemyItemStatus.REMOVED
        self.session.commit()

    def hard_remove(self, item: ItemModel):
        self.session.delete(item)
        self.session.commit()

    def update(self):
        self.session.commit()

    def get_all(self):
        return self.session.query(ItemModel)

    def get_items_by_filters(self, filters):
        return self.session.query(ItemModel).filter_by(**filters).all()

    def get_next_by_queue(self, queue):
        item = self.session.query(ItemModel).filter(
            ItemModel.eligible_date <= datetime.now(),
            ItemModel.queue_id == queue.id,
            ItemModel.status == AlchemyItemStatus.PENDING).first()

        if item:
            item.status = AlchemyItemStatus.PROCESSING
            self.session.commit()

        return item

    def get_item_by_id(self, item_id):
        return self.session.query(ItemModel).filter_by(id=item_id).first()

    def has_pending_items(self, queue, ignore_eligibility: bool = False):
        if ignore_eligibility:
            return self.session.query(ItemModel).filter(queue_id=queue.id, status=AlchemyItemStatus.PENDING).first() is not None

        return self.session.query(ItemModel).filter(
            ItemModel.eligible_date <= datetime.now(),
            ItemModel.queue_id == queue.id,
            ItemModel.status == AlchemyItemStatus.PENDING).first() is not None

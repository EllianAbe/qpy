from ..models import ItemModel


class ItemRepository():

    def __init__(self, session):
        self.session = session

    def add(self, item: ItemModel):
        self.session.add(item)
        self.session.commit()

    def remove(self, item: ItemModel):
        item.status = "removed"
        self.session.commit()

    def hard_remove(self, item: ItemModel):
        self.session.delete(item)
        self.session.commit()

    def update(self):
        self.session.commit()

    def get_all(self):
        return self.session.query(ItemModel)

    def get_next_by_queue(self, queue):
        return self.session.query(ItemModel).filter_by(queue_id=queue.id, status='pending').first()

    def has_pending_items(self, queue):
        return self.session.query(ItemModel).filter_by(queue_id=queue.id, status='pending').first()

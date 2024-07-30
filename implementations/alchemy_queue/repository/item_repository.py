from models import ItemModel


class ItemRepository():

    def __init__(self, session):
        self.session = session

    def add(self, item: ItemModel):
        self.session.add(item)
        self.session.commit()

    def remove(self, item: ItemModel):
        self.session.delete(item)
        self.session.commit()

    def update(self, item: ItemModel):
        self.session.commit()

    def get_all(self):
        return self.session.query(ItemModel)

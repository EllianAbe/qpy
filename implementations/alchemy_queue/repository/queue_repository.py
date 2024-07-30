from models import QueueModel
from sqlalchemy.orm import Session


class QueueRepository:
    def __init__(self, session: Session):
        self.session = session

    def get(self, name):
        return self.session.query(QueueModel).filter_by(name=name).first()

    def add(self, queue: QueueModel):
        self.session.add(queue)
        self.session.commit()

    def remove(self, queue: QueueModel):
        self.session.delete(queue)
        self.session.commit()

    def update(self, queue: QueueModel):
        self.session.commit()

    def get_items(self, name):
        return self.session.query(QueueModel).filter_by(name=name).first().items

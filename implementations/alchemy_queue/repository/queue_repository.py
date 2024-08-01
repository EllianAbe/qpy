from ..models import QueueModel
from sqlalchemy.orm import Session


class QueueRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_name(self, name):
        return self.session.query(QueueModel).filter_by(name=name).first()

    def add(self, queue: QueueModel):
        self.session.add(queue)
        self.session.commit()

    def remove(self, queue: QueueModel):
        self.session.delete(queue)
        self.session.commit()

    def update(self):
        self.session.commit()

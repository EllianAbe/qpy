from src.implementations.alchemy_queue.base import Base
from src.implementations.alchemy_queue import AlchemyQueue, QueueRepository, ItemRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def instantiate_queue() -> AlchemyQueue:

    engine = create_engine('sqlite:///test/alchemy_queue/local.db')

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    queue_repository = QueueRepository(session)
    item_repository = ItemRepository(session)

    queue = AlchemyQueue(queue_repository, item_repository, 'queue1')

    return queue

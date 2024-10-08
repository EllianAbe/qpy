
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.implementations.alchemy_queue import AlchemyQueue, QueueRepository, ItemRepository
from src.implementations.alchemy_queue.models.item_model import AlchemyItemStatus
from src.implementations.alchemy_queue.base import Base
from datetime import datetime, timedelta


class TestAlchemyQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        engine = create_engine('sqlite:///test/alchemy_queue/local.db')

        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine)

        queue_repository = QueueRepository(session)
        item_repository = ItemRepository(session)

        cls.queue = AlchemyQueue(queue_repository, item_repository, 'queue1')

    def test_add(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.assertIn(item, self.queue.get_items())

    def test_get_next(self):
        item = self.queue.get_next()

        self.assertIsNotNone(item)

    def test_get_items(self):
        items = self.queue.get_items()

        self.assertGreater(len(items), 0)

    def test_is_empty(self):
        self.assertFalse(self.queue.is_empty())

    def test_has_pending_items(self):
        self.queue.add({'a': 1, 'b': 2})
        self.assertTrue(self.queue.has_pending_items())

    def test_remove_item(self):

        before = len(self.queue.get_items(status=AlchemyItemStatus.REMOVED))

        self.queue.remove_item(self.queue.get_next().id)

        after = len(self.queue.get_items(status=AlchemyItemStatus.REMOVED))

        self.assertGreater(after, before)

    def test_update_item(self):
        self.queue.add({'a': 1, 'b': 2})

        sucess_before = len(self.queue.get_items(
            status=AlchemyItemStatus.SUCCESS))
        self.queue.update_item(self.queue.get_next().id,
                               AlchemyItemStatus.SUCCESS)

        sucess_after = len(self.queue.get_items(
            status=AlchemyItemStatus.SUCCESS))

        self.assertGreater(sucess_after, sucess_before)

    def test_postpone_item(self):
        item = self.queue.add({'a': 1, 'b': 2})

        eligible_date = datetime.now() + timedelta(days=3)

        self.queue.postpone_item(item.id, eligible_date)

        item = self.queue.get_item_by_id(item.id)

        self.assertEqual(item.eligible_date, eligible_date,
                         'eligible date not updated by postpone')
        self.assertEqual(item.status, AlchemyItemStatus.PENDING,
                         'status not equal pending after postpone')

    def test_with_decorator(self):
        @ self.queue.dispatcher
        def new_item():
            return {'a': 1, 'b': 2}

        item = new_item()

        self.assertIn(item, self.queue.get_items())


if __name__ == '__main__':
    unittest.main(verbosity=2)

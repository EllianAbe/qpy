
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from implementations.alchemy_queue import AlchemyQueue, QueueRepository, ItemRepository
from implementations.alchemy_queue.models.item_model import ItemStatus
from implementations.alchemy_queue.base import Base


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

        self.assertEqual(self.queue.queue.id, item.queue_id)

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

        before = len(self.queue.get_items(status=ItemStatus.REMOVED))

        self.queue.remove_item(self.queue.get_next())

        after = len(self.queue.get_items(status=ItemStatus.REMOVED))

        self.assertGreater(after, before)

    def test_update_item(self):
        self.queue.add({'a': 1, 'b': 2})

        sucess_before = len(self.queue.get_items(status=ItemStatus.SUCCESS))
        self.queue.update_item(self.queue.get_next(), ItemStatus.SUCCESS)

        sucess_after = len(self.queue.get_items(status=ItemStatus.SUCCESS))

        self.assertGreater(sucess_after, sucess_before)


if __name__ == '__main__':
    unittest.main(verbosity=2)

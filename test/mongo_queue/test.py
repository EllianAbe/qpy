

import unittest
from pymongo import MongoClient
from src.implementations.mongo_queue import MongoQueue, MongoItemStatus
from datetime import datetime, timedelta


class TestMongoQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        client = MongoClient('localhost', 27017)

        db = client.get_database('test')

        cls.queue = MongoQueue(db, 'queue1')

    def test_add(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.assertTrue(self.queue.get_items({'id': item.id}))

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

        before = len(self.queue.get_items({'status': MongoItemStatus.REMOVED}))

        self.queue.remove_item(self.queue.get_next().id)

        after = len(self.queue.get_items({'status': MongoItemStatus.REMOVED}))

        self.assertGreater(after, before)

    def test_update_item(self):
        self.queue.add({'a': 1, 'b': 2})

        sucess_before = len(self.queue.get_items(
            {'status': MongoItemStatus.SUCCESS}))
        self.queue.update_item(self.queue.get_next().id,
                               MongoItemStatus.SUCCESS)

        sucess_after = len(self.queue.get_items(
            {'status': MongoItemStatus.SUCCESS}))

        self.assertGreater(sucess_after, sucess_before)

    def test_postpone_item(self):
        item = self.queue.add({'a': 1, 'b': 2})

        eligible_date = datetime.now() + timedelta(days=3)
        timedelta(milliseconds=1)
        self.queue.postpone_item(item.id, eligible_date)

        item = self.queue.get_item_by_id(item.id)

        self.assertEqual(item.eligible_date.replace(microsecond=0), eligible_date.replace(microsecond=0),
                         'eligible date not updated by postpone')
        self.assertEqual(item.status, MongoItemStatus.PENDING,
                         'status not equal pending after postpone')

    def test_with_decorator(self):
        @ self.queue.dispatcher
        def new_item():
            return {'a': 1, 'b': 2}

        item = new_item()

        self.assertTrue(self.queue.get_items({'id': item.id}))


if __name__ == '__main__':
    unittest.main(verbosity=2)

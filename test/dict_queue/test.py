import unittest
from src.implementations import DictQueue, Item
from src.base_classes import ItemStatus


class TestDictQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queue = DictQueue([])

    def test_is_empty(self):
        self.queue.add({'a': 1, 'b': 2})
        self.assertFalse(self.queue.is_empty(), 'queue should be empty')

    def test_add(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.assertIn(item, self.queue.get_items(),
                      'item should be in the queue')

    def test_dispatcher_decorator(self):
        @self.queue.dispatcher
        def new_item():
            return {'a': 1, 'b': 2}

        item = new_item()

        in_queue = item in self.queue.get_items()

        self.assertTrue(in_queue, 'item should be in the queue')

    def test_remove_item(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.queue.remove_item(item)

        self.assertTrue(item.status == ItemStatus.REMOVED)

    def test_update_item(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.queue.update_item(item, ItemStatus.SUCCESS)

        self.assertEqual(item.status, ItemStatus.SUCCESS)

    def test_get_next(self):
        item = self.queue.add({'a': 1, 'b': 2})

        self.assertIsInstance(item, Item)

    def test_has_pending_items(self):
        self.queue.add({'a': 1, 'b': 2})

        self.assertTrue(self.queue.has_pending_items())


if __name__ == '__main__':
    unittest.main(verbosity=2)

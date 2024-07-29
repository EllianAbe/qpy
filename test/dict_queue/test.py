import unittest
from implementations import DictQueue, Item
from data import initial


class TestDictQueue(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queue = DictQueue([])

    def test_init(self):
        self.assertTrue(self.queue.is_empty, 'queue should be empty')

    def test_add(self):
        for item in initial:
            self.queue.add(Item(**item))

        self.assertFalse(self.queue.is_empty(), 'queue should not be empty')
        has_pending_items = self.queue.has_pending_items()

        self.assertTrue(has_pending_items, 'queue should have pending items')

    def test_dispatcher_decorator(self):
        @self.queue.dispatcher
        def new_item():
            return Item(**initial[0])

        item = new_item()

        in_queue = item in self.queue.get_items()

        self.assertTrue(in_queue, 'item should be in the queue')


if __name__ == '__main__':
    unittest.main(verbosity=2)

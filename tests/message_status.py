import unittest
from src.abstractions.common.message_status import ItemStatus


class TestItemStatus(unittest.TestCase):
    def test_is_final(self):
        self.assertTrue(ItemStatus.is_final(ItemStatus.ERROR))
        self.assertTrue(ItemStatus.is_final(ItemStatus.SUCCESS))
        self.assertFalse(ItemStatus.is_final(ItemStatus.PENDING))
        self.assertFalse(ItemStatus.is_final(ItemStatus.PROCESSING))

    def test_is_valid(self):
        self.assertTrue(ItemStatus.is_valid(ItemStatus.ERROR))
        self.assertTrue(ItemStatus.is_valid(ItemStatus.SUCCESS))
        self.assertTrue(ItemStatus.is_valid(ItemStatus.PENDING))
        self.assertTrue(ItemStatus.is_valid(ItemStatus.PROCESSING))
        self.assertFalse(ItemStatus.is_valid('invalid_status'))

    def test_enum_values(self):
        self.assertEqual(ItemStatus.PENDING.value, 'pending')
        self.assertEqual(ItemStatus.PROCESSING.value, 'processing')
        self.assertEqual(ItemStatus.ERROR.value, 'error')
        self.assertEqual(ItemStatus.SUCCESS.value, 'success')
        self.assertEqual(ItemStatus.REMOVED.value, 'removed')


if __name__ == '__main__':
    unittest.main(verbosity=2)

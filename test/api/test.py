
import unittest
from fastapi.testclient import TestClient
from api import app


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_add(self):
        response = self.client.post('/queue/items', json={'a': 1, 'b': 2})

        item = response.json()
        self.assertIn(item, self.client.get('/queue/items').json())

    def test_get_next(self):
        item = self.client.get('/queue/next_item').json()

        self.assertTrue(item)

    def test_get_items(self):
        items = self.client.get('/queue/items').json()

        self.assertGreater(len(items), 0)

    def test_get_queue_info(self):
        info: dict = self.client.get('/queue/').json()

        self.assertTrue('is_empty' in info)

    def test_remove_item(self):
        item = self.client.post('/queue/items', json={'a': 1, 'b': 2}).json()
        before = len(self.client.get('/queue/items/?status=removed').json())
        self.client.delete(f'/queue/items/{item["id"]}')

        after = len(self.client.get('/queue/items/?status=removed').json())

        self.assertGreater(after, before)

    def test_update_item(self):
        self.client.post('/queue/items', json={'a': 1, 'b': 2})

        sucess_before = len(self.client.get(
            '/queue/items/?status=success').json())

        next_item = self.client.get('/queue/next_item').json()
        self.client.put(
            f'/queue/items/{next_item["id"]}?status=success')

        sucess_after = len(self.client.get(
            '/queue/items/?status=success').json())

        self.assertGreater(sucess_after, sucess_before)


if __name__ == '__main__':
    unittest.main(verbosity=2)
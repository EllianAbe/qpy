**Mongo Queue README**
=======================

**Overview**
------------

The Mongo Queue is a Python library that provides a simple and efficient way to manage queues using MongoDB. It allows you to add, retrieve, and update items in a queue, as well as check the status of the queue.

**Basic Usage**
---------------

### Installing the Library

To use the Mongo Queue library, you need to install it using pip:
```bash
pip install mongo-queue
```
### Creating a Queue

To create a queue, you need to import the `MongoQueue` class and create an instance of it, passing in a MongoDB database and a queue name:
```python
from src.implementations.mongo_queue import MongoQueue

client = MongoClient('localhost', 27017)
db = client.get_database('test')

queue = MongoQueue(db, 'queue1')
```
### Adding Items to the Queue

To add an item to the queue, you can use the `add` method:
```python
item = queue.add({'a': 1, 'b': 2})
```
### Retrieving Items from the Queue

To retrieve an item from the queue, you can use the `get_next` method:
```python
item = queue.get_next()
```
### Updating Items in the Queue

To update an item in the queue, you can use the `update_item` method:
```python
queue.update_item(item.id, 'status', 'new_status')
```
### Checking the Status of the Queue

To check if the queue is empty, you can use the `is_empty` method:
```python
if queue.is_empty():
    print("The queue is empty")
```
You can also check if the queue has pending items using the `has_pending_items` method:
```python
if queue.has_pending_items():
    print("The queue has pending items")
```
**Example Use Case**
--------------------

Here is an example of how you can use the Mongo Queue library to manage a queue:
```python
from src.implementations.mongo_queue import MongoQueue

client = MongoClient('localhost', 27017)
db = client.get_database('test')

queue = MongoQueue(db, 'queue1')

# Add some items to the queue
queue.add({'a': 1, 'b': 2})
queue.add({'c': 3, 'd': 4})

# Retrieve an item from the queue
item = queue.get_next()
print(item)

# Update the item
queue.update_item(item.id, 'status', 'new_status')

# Check if the queue is empty
if queue.is_empty():
    print("The queue is empty")
```
Note that this is just a basic example, and you can use the Mongo Queue library in more complex scenarios as well.
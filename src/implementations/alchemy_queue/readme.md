**Alchemy Queue README**
=======================

**Overview**
------------

The Alchemy Queue is a Python library that provides a simple and efficient way to manage queues using SQLAlchemy. It allows you to add, retrieve, and update items in a queue, as well as check the status of the queue.

**Basic Usage**
---------------

### Installing the Library

To use the Alchemy Queue library, you need to install it using pip:
```bash
pip install qpy[alchemy]
```
### Creating a Queue

To create a queue, you need to import the `AlchemyQueue` class and create an instance of it, passing in a SQLAlchemy session and a queue name:
```python
from src.implementations.alchemy_queue import AlchemyQueue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test/alchemy_queue/local.db')
Session = sessionmaker(bind=engine)
session = Session()

queue = AlchemyQueue.from_session(session, 'queue1')
```
### Adding Items to the Queue

To add an item to the queue, you can use the `add` method:
```python
queue.add({'a': 1, 'b': 2})
```
### Retrieving Items from the Queue

To retrieve an item from the queue, you can use the `get_next` method:
```python
item = queue.get_next()
```
### Updating Items in the Queue

To update an item in the queue, you can use the `update_item` method:
```python
queue.update_item(item.id, AlchemyItemStatus.SUCCESS)
```
### Checking the Status of the Queue

To check if the queue is empty, you can use the `is_empty` method:
```python
if queue.is_empty():
    print("The queue is empty")
```
**Example Use Case**
--------------------

Here is an example of how you can use the Alchemy Queue library to manage a queue:
```python
from src.implementations.alchemy_queue import AlchemyQueue
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test/alchemy_queue/local.db')
Session = sessionmaker(bind=engine)
session = Session()

queue = AlchemyQueue.from_session(session, 'queue1')

# Add some items to the queue
queue.add({'a': 1, 'b': 2})
queue.add({'c': 3, 'd': 4})

# Retrieve an item from the queue
item = queue.get_next()
print(item)

# Update the item
queue.update_item(item.id, AlchemyItemStatus.SUCCESS)

# Check if the queue is empty
if queue.is_empty():
    print("The queue is empty")
```
Note that this is just a basic example, and you can use the Alchemy Queue library in more complex scenarios as well.

**Testing**
------------

The Alchemy Queue library comes with a set of unit tests that you can run to verify its functionality. To run the tests, you can use the following command:
```bash
python -m unittest test/alchemy_queue/test.py
```
This will run the tests and report any failures or errors.
# QPY
Queue management for Python.

QPY provides task queues for software and automation. It allows developers to store transactional tasks, persist their data (both input and output), and control their statuses. The library includes a robust auto-retry mechanism to avoid momentary interruptions on necessary dependencies.

## Features

* Task queues for software and automation
* Persistent data storage for input and output
* Status control for tasks
* Auto-retry mechanism for robustness
* Support for multiple queue implementations (e.g., MongoDB, SQLAlchemy)
* Distributed architecture: Each queue can have multiple producers and multiple consumers, which can run anywhere, allowing for scalable and fault-tolerant distributed systems.
## Installation

To install QPY, use pip:
```bash
pip install qpy
```
For specific queue implementations, use the following commands:

* MongoDB: `pip install qpy[mongo]`
* SQLAlchemy: `pip install qpy[alchemy]`
* API: `pip install qpy[api]`

## Creating Your Own Queue Implementation

To create your own QPY queue implementation, consider the following steps:

1. Choose a data storage solution (e.g., memory, disk, SQL DB, NoSQL, file).
2. Determine if a ready-to-use queue meets your requirements.
3. Decide on a flexible or schema-based structure for your queue items.

## Example Use Case

Here's an example of using the Mongo Queue library to manage a queue:
```python
from implementations.mongo_queue import MongoQueue

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
queue.update_item(item.id, 'failed')

# Check if the queue is empty
if queue.is_empty():
    print("The queue is empty")
```
## Checking the Status of the Queue

To check if the queue is empty, use the `is_empty` method:
```python
if queue.is_empty():
    print("The queue is empty")
```
You can also check if the queue has pending items using the `has_pending_items` method:
```python
if queue.has_pending_items():
    print("The queue has pending items")
```
Note that this is just a basic example, and you can use the QPY library in more complex scenarios as well.

<!-- 
## API Documentation

For more information on the QPY API, please refer to the [API documentation](link-to-api-docs TODO).
-->

## Contributing

Contributions are welcome! Please submit a pull request with your changes, and we'll review them as soon as possible.

## License

QPY is licensed under the [MIT License](/LICENSE).

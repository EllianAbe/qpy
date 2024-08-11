# QPY
Queue management for Python.

QPY provides task queues for software and automation.

QPY allows developers to store transactional tasks, persist their data (both input and output), and control their statuses. It includes a robust auto-retry mechanism to avoid momentary interruptions on necessary dependencies.

You can choose between a ready-to-use option or create your own queue using the provided base classes.

Deploying any queue using REST APIs based on FastAPI provides easy integration with applications, workflows, and services. You can add and consume queue items anywhere you need.

## Installation
### Self-Developed
Use the default installation to implement your own queue.

```
pip install qpy
```

### Ready-to-Use
To use a ready-to-use queue or tool:

```
pip install qpy[mongo]
pip install qpy[alchemy]
pip install qpy[api]
```

## Creating Your Own Queue Implementation
To create your own QPY queue implementation, you must consider the base_classes package.

Following the method signatures allows for easy integration with ready-to-use tools, such as the REST API server.

Consider these questions when starting an implementation:

* Where will the data be stored? (memory, disk, SQL DB, NoSQL, file)
* Does a ready-to-use queue meet my requirements? (partially, completely)
* Will the items have a flexible structure or be schema-based?
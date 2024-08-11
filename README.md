# QPY
Queue management for Python.

QPY provides task queues for software and automation.

QPY allows developers to store transactional tasks, persist their data (both input and output), and control their statuses. It includes a robust auto-retry mechanism to avoid momentary interruptions on necessary dependencies.

You can choose between a ready-to-use option or create your own queue using the provided base classes.

Deploying any queue using REST APIs based on FastAPI, ~~provide easy integrations with applications, workflows and services ~~ you can add and consume queue items anywhere you need.

## Instalation
### self-developed
use the default instalation to implement your own queue.

`pip install qpy`

### ready-to-use
to use a ready-to-use queue:
```
pip install qpy[mongo]
pip install qpy[alchemy]
```

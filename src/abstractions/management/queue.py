from src.abstractions.message import Message


class Queue:
    def __init__(self, name, durable=False):
        self.name = name
        self.durable = durable
        self.messages = []

    def enqueue(self, message: Message):
        self.messages.append(message)

    def dequeue(self):
        if self.messages:
            return self.messages.pop(0)
        else:
            return None

from .exchange import Exchange
from .queue import Queue


class Broker:
    def __init__(self):
        self.exchanges = {}
        self.queues = {}

    def create_exchange(self, name, exchange_type):
        exchange = Exchange(name, exchange_type)
        self.exchanges[name] = exchange
        return exchange

    def create_queue(self, name, durable=False):
        queue = Queue(name, durable)
        self.queues[name] = queue
        return queue

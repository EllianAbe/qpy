from .exchange import Exchange
from ..common.queue import Queue


class Broker:
    """
    A message broker that manages exchanges and queues.

    Attributes:
        exchanges (dict): A dictionary of exchanges, keyed by name.
        queues (dict): A dictionary of queues, keyed by name.

    Methods:
        create_exchange(name, exchange_type): Creates a new exchange with the given name and type.
        create_queue(name, durable=False): Creates a new queue with the given name and durability.
    """

    def __init__(self):
        self.exchanges = {}
        self.queues = {}

    def create_exchange(self, name, exchange_type):
        """
        Creates a new exchange with the given name and type.

        Args:
            name (str): The name of the exchange.
            exchange_type (str): The type of the exchange.

        Returns:
            Exchange: The newly created exchange.
        """
        exchange = Exchange(name, exchange_type)
        self.exchanges[name] = exchange
        return exchange

    def create_queue(self, name, durable=False):
        """
        Creates a new queue with the given name and durability.

        Args:
            name (str): The name of the queue.
            durable (bool, optional): Whether the queue is durable. Defaults to False.

        Returns:
            Queue: The newly created queue.
        """
        queue = Queue(name, durable)
        self.queues[name] = queue
        return queue

    def get_queue(self, name):
        """
        Retrieves a queue by its name.

        Args:
            name (str): The name of the queue to retrieve.

        Returns:
            Queue: The queue with the given name, or None if it does not exist.
        """
        return self.queues.get(name)

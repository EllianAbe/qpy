from datetime import datetime
from typing import Literal


class MessageHeaders:
    def __init__(self,
                 timestamp=datetime.now(),
                 priority=Literal['low', 'medium', 'high'],
                 routing_key=None,
                 message_id=None):
        """
        Initializes the message headers with optional values.

        :param content_type: Type of the content (e.g., application/json).
        :param timestamp: Time when the message is created.
        :param priority: Priority of the message (e.g., 0 for low, 10 for high).
        :param routing_key: Key used to route the message to a specific queue.
        :param message_id: Unique ID for the message.
        """
        self.timestamp = timestamp
        self.priority = priority
        self.routing_key = routing_key
        self.message_id = message_id

    def set_header(self, key, value):
        """Dynamically sets any additional header."""
        setattr(self, key, value)

    def get_header(self, key):
        """Gets the value of a specific header."""
        return getattr(self, key, None)

    def __repr__(self):
        """Returns a string representation of the headers."""
        return (f"MessageHeaders("
                f"timestamp={self.timestamp}, priority={self.priority}, "
                f"routing_key={self.routing_key}, message_id={self.message_id})")

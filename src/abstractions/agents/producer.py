from ..message.message import Message


class Producer:
    def __init__(self, exchange, routing_key):
        self.exchange = exchange
        self.routing_key = routing_key

    def send_message(self, message_body, headers=None):
        message = Message(message_body, headers)
        self.exchange.route_message(message, self.routing_key)



class Exchange:
    def __init__(self, name, exchange_type):
        self.name = name
        self.exchange_type = exchange_type
        self.bindings = {}

    def bind(self, queue, routing_key):
        self.bindings[routing_key] = queue

    def route_message(self, message, routing_key):
        if routing_key in self.bindings:
            self.bindings[routing_key].enqueue(message)
        else:
            print(f"No binding for routing key: {routing_key}")

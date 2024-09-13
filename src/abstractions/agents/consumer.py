class Consumer:
    def __init__(self, queue, auto_ack=True):
        self.queue = queue
        self.auto_ack = auto_ack

    def consume_message(self):
        message = self.queue.dequeue()
        if message:
            self.process_message(message)
            if self.auto_ack:
                self.acknowledge(message)
        else:
            print("No messages to consume.")

    def process_message(self, message):
        print(f"Processing message: {message.content}")

    def acknowledge(self, message):
        print(f"Acknowledged message: {message.content}")

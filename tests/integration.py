from src import Broker, Producer, Consumer
# 1. Set up the broker
broker = Broker()

# 2. Create an exchange
exchange = broker.create_exchange("logs", "direct")

# 3. Create queues
error_queue = broker.create_queue("error_queue")
info_queue = broker.create_queue("info_queue")

# 4. Bind queues to exchange with routing keys
exchange.bind(error_queue, "error")
exchange.bind(info_queue, "info")

# 5. Set up producer and consumers
producer = Producer(exchange, "error")
consumer = Consumer(error_queue)

# 6. Send a message
producer.send_message("An error occurred")

# 7. Consumer consumes message
consumer.consume_message()

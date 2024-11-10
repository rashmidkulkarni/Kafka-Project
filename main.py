import json
from kafka import KafkaProducer
from fake import generate_pizza_details
from kafka import KafkaConsumer


folderName = "/Users/rash/Documents/KAFKA/"
producer = KafkaProducer(
    bootstrap_servers="kafka-demo-apache-kafka-project-01-rashmi.j.aivencloud.com:16265",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v: json.dumps(v).encode('ascii'),
    key_serializer=lambda v: json.dumps(v).encode('ascii')
)
pizza_details_list = generate_pizza_details()

# Send pizza orders to Kafka
for pizza_details in pizza_details_list:
    producer.send("order-topic", value=pizza_details)
    print(pizza_details)

#the message has a key-value pair where the key is {"key": 1} and the value is {"message": "hello-world"}.

producer.flush()
# It's good practice to call flush() to make sure no messages are lost.


consumer = KafkaConsumer('order-topic',
                         bootstrap_servers='kafka-demo-apache-kafka-project-01-rashmi.j.aivencloud.com:16265',
                         security_protocol='SSL',
                         ssl_cafile='/Users/rash/Documents/KAFKA/ca.pem',
                         ssl_certfile='/Users/rash/Documents/KAFKA/service.cert',
                         ssl_keyfile='/Users/rash/Documents/KAFKA/service.key',
                         group_id='my-group')
orders = []
try:
    for i, message in enumerate(consumer):
        if i >= 10:  # Limit to processing only 1000 messages
            break
        order_details = json.loads(message.value.decode('utf-8'))
        orders.append(order_details)
except KeyboardInterrupt:
    print("Stopped by user.")

print("Sampled consumer data:")
print(orders[:10])

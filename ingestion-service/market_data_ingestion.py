import os
from kafka import KafkaProducer
import json
import time
import random



#Kafka producer
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'quantstream-cluster-kafka-bootstrap:9092')
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', 'market-data')

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    acks='all',
    retries=3,
    retry_backoff_ms=1000,
    max_in_flight_requests_per_connection=1,
    compression_type='gzip'
)


def get_market_data():
    # In a real scenario, you would fetch data from your market data provider
    # This is a simplified example
    return {
        'symbol': 'AAPL',
        'price': round(random.uniform(150, 160), 2),
        'volume': random.randint(1000, 10000),
        'timestamp': int(time.time())
    }

def publish_market_data():
    while True:
        data = get_market_data()
        producer.send(KAFKA_TOPIC, value=data)
        print(f"Published: {data}")
        time.sleep(1)  # Publish every second

if __name__ == "__main__":
    publish_market_data()

# --- producer.py ---
from kafka import KafkaProducer
import json
import time
import random

# Sample tweets
tweets = [
    "I'm so happy with this product!",
    "This is terrible, I want a refund.",
    "Amazing service, loved it!",
    "Worst experience ever...",
    "I'm feeling okay about this."
]

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    tweet = {"text": random.choice(tweets)}
    producer.send('tweets', tweet)
    print(f"Sent: {tweet}")
    time.sleep(1)
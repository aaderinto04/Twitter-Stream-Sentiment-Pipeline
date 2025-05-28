from kafka import KafkaConsumer
from textblob import TextBlob
from elasticsearch import Elasticsearch
from datetime import datetime, timezone
import json

# ✅ Pass headers directly to Elasticsearch (supported in 8.13.2)
es = Elasticsearch(
    ["http://localhost:9200"],
    headers={
        "Accept": "application/vnd.elasticsearch+json; compatible-with=8",
        "Content-Type": "application/vnd.elasticsearch+json; compatible-with=8"
    }
)

# Kafka Consumer setup
consumer = KafkaConsumer(
    'tweets',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Sentiment analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    return 'neutral'

# Process messages
for msg in consumer:
    tweet = msg.value['text']
    sentiment = get_sentiment(tweet)
    print(f"Tweet: {tweet} | Sentiment: {sentiment}")

    es.index(index="tweet-sentiment", document={
        "text": tweet,
        "sentiment": sentiment,
        "timestamp": datetime.now(timezone.utc)
    })

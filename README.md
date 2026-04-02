# Twitter Sentiment Analysis Pipeline

A real-time sentiment analysis pipeline that processes Twitter-like data streams using Apache Kafka for messaging and Elasticsearch for data storage.

## Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline for sentiment analysis:

- **Producer**: Simulates a Twitter stream by generating and sending sample tweets to a Kafka topic
- **Consumer**: Processes incoming tweets, performs sentiment analysis using TextBlob, and indexes results in Elasticsearch
- **Infrastructure**: Uses Docker Compose to run Kafka (with Zookeeper) and Elasticsearch services

## Features

- Real-time tweet processing via Kafka messaging
- Sentiment analysis using TextBlob (positive, negative, neutral classification)
- Data persistence in Elasticsearch for querying and analytics
- Docker-based infrastructure for easy setup and deployment
- Sample tweet data for testing and demonstration

## Technologies Used

- **Python**: Core application logic
- **Apache Kafka**: Message queuing and streaming
- **Elasticsearch**: Document storage and search
- **TextBlob**: Natural language processing for sentiment analysis
- **Docker & Docker Compose**: Containerized infrastructure

## Prerequisites

- Docker and Docker Compose installed
- Python 3.7+ (for local development)
- Virtual environment (recommended)

## Setup and Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Set up Python environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Start infrastructure services**:
   ```bash
   docker-compose up -d
   ```
   This will start:
   - Zookeeper on port 2181
   - Kafka on port 9092
   - Elasticsearch on port 9200

4. **Verify services are running**:
   - Kafka: Check if port 9092 is accessible
   - Elasticsearch: Visit http://localhost:9200 in your browser

## Usage

1. **Start the producer** (in one terminal):
   ```bash
   python producer.py
   ```
   This will begin sending sample tweets to the 'tweets' Kafka topic every second.

2. **Start the consumer** (in another terminal):
   ```bash
   python consumer.py
   ```
   This will:
   - Consume tweets from the Kafka topic
   - Analyze sentiment of each tweet
   - Index the results in Elasticsearch

3. **Monitor the pipeline**:
   - Producer terminal will show sent tweets
   - Consumer terminal will show processed tweets with sentiment analysis
   - Data is stored in Elasticsearch index 'tweet-sentiment'

## Architecture

```
Sample Tweets → Producer → Kafka Topic → Consumer → Sentiment Analysis → Elasticsearch
```

- **Producer**: Generates mock Twitter data and publishes to Kafka
- **Kafka**: Acts as a message buffer between producer and consumer
- **Consumer**: Processes messages, performs NLP analysis, stores results
- **Elasticsearch**: Provides search and analytics capabilities on processed data

## Configuration

- Kafka topic: `tweets`
- Elasticsearch index: `tweet-sentiment`
- Kafka broker: `localhost:9092`
- Elasticsearch endpoint: `http://localhost:9200`

## Development

To modify the sentiment analysis logic, edit the `get_sentiment()` function in `consumer.py`. The current implementation uses TextBlob's polarity score to classify sentiments as positive (>0), negative (<0), or neutral (=0).

## Troubleshooting

- **Kafka connection issues**: Ensure Docker containers are running and ports are accessible
- **Elasticsearch errors**: Check if Elasticsearch is healthy at http://localhost:9200/_cluster/health
- **Import errors**: Make sure all dependencies are installed via `pip install -r requirements.txt`

## Future Enhancements

- Integration with real Twitter API
- Advanced NLP models (BERT, GPT)
- Dashboard for real-time sentiment visualization
- Alerting system for sentiment trends
- Multi-language support



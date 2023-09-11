import os
import json
import time

from kafka import KafkaConsumer

from db import PostgresDB
from consumer_csv import callback_csv
from consumer_weather import callback_weather
from consumer_coin import callback_coin
from consumer_market import callback_market


class MessageConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            bootstrap_servers=os.getenv("KAFKA_BROKERS").split(","),
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            group_id=os.getenv("KAFKA_CONSUMER_GROUP"),
            enable_auto_commit=True,
        )
        self.events = {}
        self.db = PostgresDB()

    def regist_event(self, topic, callback):
        self.events[topic] = callback

    def start(self):
        self.consumer.subscribe(list(self.events.keys()))
        for message in self.consumer:
            try:
                self.events[message.topic](message, self.db)
            except Exception as e:
                print(e)
                continue


if __name__ == "__main__":
    time.sleep(5)
    consumer = MessageConsumer()
    consumer.regist_event("flask-postgres-csv", callback_csv)
    consumer.regist_event("flask-postgres-weather", callback_weather)
    consumer.regist_event("flask-postgres-coin", callback_coin)
    consumer.regist_event("flask-postgres-market", callback_market)
    consumer.start()

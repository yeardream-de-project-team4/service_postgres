import os
import json
from kafka import KafkaConsumer
from db import PostgresDB


class MessageConsumer:
    def __init__(self, brokers, topics, group_id):
        self.consumer = KafkaConsumer(
            bootstrap_servers=brokers,
            value_deserializer=lambda x: x.decode("utf-8"),
            group_id=group_id,
            enable_auto_commit=True,
        )
        self.consumer.subscribe(topics)

    def receive_message(self):
        try:
            for message in self.consumer:
                if message.topic == topics[0]:
                    data = json.loads(message.value)
                    if data:
                        sql = f"""
                            INSERT INTO weather_data (timestamp, temperature, precipitation)
                            VALUES ('{data.get("time", None)}', {data.get("temp", 0)}, {data.get("rain", 0)});
                        """
                        db = PostgresDB()
                        db.execute(sql)
        except Exception as exc:
            raise exc


if __name__ == "__main__":
    brokers = os.getenv("KAFKA_BROKERS").split(",")
    group_id = os.getenv("KAFKA_CONSUMER_GROUP")
    topics = ["taehoon-topic3"]
    cs = MessageConsumer(brokers, topics, group_id)
    cs.receive_message()

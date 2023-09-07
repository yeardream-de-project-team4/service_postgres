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
            auto_offset_reset="earliest",
            enable_auto_commit=True,
        )
        self.consumer.subscribe(topics)
        self.db = PostgresDB()
        self.topics = topics 

    def receive_message(self):
        try:
            for message in self.consumer:
                if message.topic == self.topics[0]:
                    data = json.loads(message.value)
                    fields = (
                        data["market"], data["trade_date_utc"],data["trade_time_utc"], data["timestamp"], data["trade_price"], data["trade_volume"], data["prev_closing_price"], data["change_price"],
                        data["ask_bid"], data["sequential_id"]
                        )
                    sql = """
                        INSERT INTO trade_table (market, trade_date_utc, trade_time_utc, timestamp, trade_price, trade_volume, prev_closing_price, change_price, ask_bid, sequential_id) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                    """
                    self.db.execute(sql, fields)
        except Exception as exc:
            raise exc
    
    # def receive_message(self):
    #     try:
    #         for message in self.consumer:
    #             if message.topic == topics[0]:
    #                 data = json.loads(message.value)
    #                 fields = (data["name"], data["age"])
    #                 sql = """
    #                     INSERT INTO example_table (name, age) VALUES (%s, %s);
    #                 """
    #                 self.db.execute(sql, fields)
    #     except Exception as exc:
    #         raise exc


if __name__ == "__main__":
    brokers = os.getenv("KAFKA_BROKERS").split(",")
    group_id = os.getenv("KAFKA_CONSUMER_GROUP")
    topics = ["eom-topic"]
    cs = MessageConsumer(brokers, topics, group_id)
    cs.receive_message()

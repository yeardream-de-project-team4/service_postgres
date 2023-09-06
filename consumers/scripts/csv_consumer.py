import os
import json
from kafka import KafkaConsumer
from db import PostgresDB

db = PostgresDB()
consumer = KafkaConsumer(
    bootstrap_servers=os.getenv("KAFKA_BROKERS").split(","),
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    group_id="consumer-load-csv",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
)
consumer.subscribe(["topic-load-csv"])

for message in consumer:
    try:
        data = message.value
        fields = (
            data["source"],
            data["symbol"],
            data["link"],
            data["date"],
            data["title"],
            data["content"],
        )
        sql = """
            INSERT INTO table_csv
            (source, symbol, link, date, title, content)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        db.execute(sql, fields)
    except Exception:
        continue

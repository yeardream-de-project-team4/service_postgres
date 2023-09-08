from db import PostgresDB
from kafka import KafkaConsumer
import time
import json
import os


class MessageConsumer:

    def __init__(self, broker, topics, group_id, batch_size ,insert_interval):
        self.broker = broker
        self.consumer = KafkaConsumer(
            bootstrap_servers=self.broker,
            value_deserializer=lambda x: x.decode(
                "utf-8"
            ),  # Decode message value as utf-8
            group_id=group_id,  # Consumer group ID
            # Start consuming from earliest available message
            # auto_offset_reset="earliest",
            enable_auto_commit=True,  # Commit offsets automatically
        )
        self.consumer.subscribe(topics)
        self.batch_size = batch_size
        self.batch = []
        self.insert_interval = insert_interval
        self.last_insert_time = time.time()
        
    def receive_message(self):
        try:
            for message in self.consumer:
                
                
                self.process_message(json.loads(message.value))
                print(message.value)
                if len(self.batch) >= self.batch_size or time.time() - self.last_insert_time >= self.insert_interval:
                    self.bulk_insert()
                    
        except Exception as exc:
            raise exc
        
    def process_message(self, message):
        # 데이터 처리 필요시 해당함수 사용
        print(tuple(message.values()))
        self.batch.append(tuple(message.values()))
       

    def bulk_insert(self):
        sql = """
        INSERT INTO coin_realtime_trade (coin_code, trade_price, trade_yymmddhms, opening_price, high_price, low_price, acc_volume, acc_price, acc_ask_volume, acc_bid_volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        db.execute_many(sql, self.batch)
        # 배치 비우기
        self.batch = []
        # 시간 초기화
        self.last_insert_time = time.time()
        
        print("================================== INSERT ==================================")
        
# 브로커와 토픽명을 지정한다.
broker = os.getenv("KAFKA_BROKERS").split(",")
group_id = os.getenv("KAFKA_CONSUMER_GROUP")
topics = ["coin"]

db = PostgresDB()

init_coin_info_sql = """
INSERT INTO coin (coin_code, coin_name) VALUES (%s, %s) ON CONFLICT (coin_code) DO NOTHING;;
"""

init_coin_name=[('KRW-BTC', '비트코인'),('KRW-ETH', '이더리움'),('KRW-XRP', '도지')]
db.execute_many(init_coin_info_sql, init_coin_name)
cs = MessageConsumer(broker, topics, group_id, 1000, 10)
cs.receive_message()
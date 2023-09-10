import time
from db import PostgresDB

time.sleep(5)

postgres = PostgresDB()

create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature NUMERIC,
    precipitation NUMERIC
);
"""

postgres.execute(create_table_query)

create_table_query = """
CREATE TABLE coin (
    coin_code VARCHAR(20) PRIMARY KEY,
    coin_name VARCHAR(20) NOT NULL
);
"""
postgres.execute(create_table_query)

init_coin_info_sql = """
INSERT INTO coin (coin_code, coin_name) VALUES (%s, %s) ON CONFLICT (coin_code) DO NOTHING;;
"""

init_coin_name = [("KRW-BTC", "비트코인"), ("KRW-ETH", "이더리움"), ("KRW-XRP", "도지")]
postgres.execute_many(init_coin_info_sql, init_coin_name)

create_table_query = """
CREATE TABLE coin_realtime_trade(
    coin_code VARCHAR(20),
    trade_price FLOAT,
    trade_yymmddhms VARCHAR(12),
    opening_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    acc_volume FLOAT,
    acc_price FLOAT,
    acc_ask_volume FLOAT,
    acc_bid_volume FLOAT,
    FOREIGN KEY (coin_code) REFERENCES coin (coin_code) ON DELETE CASCADE
);
"""
postgres.execute(create_table_query)

create_table_query = """
CREATE TABLE IF NOT EXISTS table_csv (
    id SERIAL PRIMARY KEY,
    source VARCHAR(30) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    link VARCHAR(255) NOT NULL,
    date VARCHAR(20) NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
"""
postgres.execute(create_table_query)

time.sleep(5)

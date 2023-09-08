import time
from db import PostgresDB

time.sleep(10)

postgres = PostgresDB()

create_table_query = """
CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature NUMERIC,
    precipitation NUMERIC
);
"""
create_table_query1 = """

CREATE TABLE coin (
    coin_code VARCHAR(20) PRIMARY KEY,
    coin_name VARCHAR(20) NOT NULL
);
"""

create_table_query2 = """
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
postgres.execute(create_table_query1)
postgres.execute(create_table_query2)
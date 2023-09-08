import time
from db import PostgresDB

time.sleep(10)

postgres = PostgresDB()

create_table_query = """
CREATE TABLE IF NOT EXISTS trade_table (
    id SERIAL PRIMARY KEY,
    market VARCHAR(20),
    trade_date_utc DATE,
    trade_time_utc TIME,
    timestamp BIGINT,
    trade_price NUMERIC(20, 8),
    trade_volume NUMERIC(20, 8),
    prev_closing_price NUMERIC(20, 8),
    change_price NUMERIC(20, 8),
    ask_bid VARCHAR(5),
    sequential_id BIGINT UNIQUE
);
"""
# create_table_query = """
# CREATE TABLE IF NOT EXISTS example_table (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INT
# );
# """

postgres.execute(create_table_query)

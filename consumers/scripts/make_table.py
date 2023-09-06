import time
from db import PostgresDB

time.sleep(10)

postgres = PostgresDB()

create_table_query = """
CREATE TABLE IF NOT EXISTS example_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT
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

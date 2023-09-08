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

postgres.execute(create_table_query)

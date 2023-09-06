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

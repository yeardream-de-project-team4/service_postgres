import psycopg2


class PostgresDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="pgpool",
            dbname="customdatabase",
            user="postgres",
            password="adminpassword",
            port=5432,
        )

    def execute(self, sql, data=None):
        with self.conn:
            with self.conn.cursor() as curs:
                curs.execute(sql, data)

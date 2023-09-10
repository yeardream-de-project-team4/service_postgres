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

    def execute_many(self, sql, data_list):
        try:
            with self.conn:
                with self.conn.cursor() as curs:
                    curs.executemany(sql, data_list)
        except Exception as e:
            self.conn.rollback()
            print(f"Error while bulk inserting: {e}")
            raise e

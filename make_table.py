import psycopg2


# 데이터베이스에 연결
conn = psycopg2.connect(
    host="localhost",
    dbname="customdatabase",
    user="postgres",
    password="adminpassword",
    port=5432,
)

# 커서 객체 생성
cur = conn.cursor()

# SQL 쿼리를 작성하여 테이블 생성
create_table_query = """
CREATE TABLE IF NOT EXISTS example_table2 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT
);
"""

# 쿼리 실행
cur.execute(create_table_query)

# 변경사항 커밋
conn.commit()

# 커서와 연결 종료
cur.close()
conn.close()

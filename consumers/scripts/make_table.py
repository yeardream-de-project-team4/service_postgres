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

CREATE TABLE IF NOT EXISTS keum_coin_candle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    market VARCHAR(255) NOT NULL, # 코인명
    candle_date_time_utc DATETIME NOT NULL, # 캔들 기준 시각(UTC 기준)
    candle_date_time_kst DATETIME NOT NULL, # 캔들 기준 시각(KST 기준)
    opening_price DOUBLE NOT NULL, # 시가
    high_price DOUBLE NOT NULL, # 고가
    low_price DOUBLE NOT NULL, # 저가
    trade_price DOUBLE NOT NULL, # 종가
    timestamp BIGINT NOT NULL, # 해당 캔들에서 마지막 틱이 저장된 시각
    candle_acc_trade_price DOUBLE NOT NULL, # 누적 거래 금액
    candle_acc_trade_volume DOUBLE NOT NULL, # 누적 거래량
    unit INT NOT NULL # 분 단위(유닛)
);

"""

postgres.execute(create_table_query)

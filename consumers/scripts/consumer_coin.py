import time


def callback_coin(
    message,
    db,
    batch=[],
    batch_size=1000,
    insert_interval=10,
    last_insert_time=[time.time()],
):
    batch.append(tuple(message.values()))
    if (
        len(batch) >= batch_size
        or time.time() - last_insert_time[-1] >= insert_interval
    ):
        sql = """
        INSERT INTO coin_realtime_trade (coin_code, trade_price, trade_yymmddhms, opening_price, high_price, low_price, acc_volume, acc_price, acc_ask_volume, acc_bid_volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        db.execute_many(sql, batch)
        # 배치 비우기
        batch = []
        # 시간 초기화
        last_insert_time.pop()
        last_insert_time.append(time.time())

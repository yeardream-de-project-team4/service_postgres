def callback_market(message, db):
    data = message.value
    fields = (
        data["market"],
        data["trade_date_utc"],
        data["trade_time_utc"],
        data["timestamp"],
        data["trade_price"],
        data["trade_volume"],
        data["prev_closing_price"],
        data["change_price"],
        data["ask_bid"],
        data["sequential_id"],
    )
    sql = """
        INSERT INTO trade_table (market, trade_date_utc, trade_time_utc, timestamp, trade_price, trade_volume, prev_closing_price, change_price, ask_bid, sequential_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    db.execute(sql, fields)

def callback_csv(message, db):
    data = message.value
    fields = (
        data["source"],
        data["symbol"],
        data["link"],
        data["date"],
        data["title"],
        data["content"],
    )
    sql = """
        INSERT INTO table_csv
        (source, symbol, link, date, title, content)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    db.execute(sql, fields)

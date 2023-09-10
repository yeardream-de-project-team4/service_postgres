def callback_weather(message, db):
    data = message.value
    fields = (
        data["time"],
        data.get("temp", 0),
        data.get("rain", 0),
    )
    sql = """
        INSERT INTO weather_data
        (timestamp, temperature, precipitation)
        VALUES (%s, %s, %s);
    """
    db.execute(sql, fields)

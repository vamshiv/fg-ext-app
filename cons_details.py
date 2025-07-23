def get_consumer_details(conn, consumer_sql, consumer_id):
    params = (consumer_id,)
    consumer_rows = execute_query(conn, consumer_sql, params)
    if not consumer_rows:
        return None
    return consumer_rows[0]  # Assuming one row per consumer_id

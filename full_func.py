def get_producer_with_consumers(conn, producer_sql, consumer_sql):
    producer_row = execute_query(conn, producer_sql)  # Assume single row
    producer_data = producer_row[0]  # First row of result

    # Dynamically build producer dict (ignore nulls)
    producer_dict = {
        key: value
        for key, value in producer_data.items()
        if key != "CONSUMERS" and value not in (None, "", "NULL")
    }

    # Process comma-separated consumers
    consumer_ids = producer_data["CONSUMERS"].split(",")
    consumers = []
    for cid in consumer_ids:
        consumer_details = get_consumer_details(conn, consumer_sql, cid.strip())
        if consumer_details:
            consumers.append(consumer_details)

    producer_dict["Consumers"] = consumers

    return {"Producer": producer_dict}

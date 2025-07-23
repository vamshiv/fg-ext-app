def get_producer_with_consumers(conn, producer_sql, consumer_sql):
    producer_row = execute_query(conn, producer_sql)  # Assume single row
    producer_data = producer_row[0]  # First row of result

    # Extract producer details
    producer_dict = {
        key: value
        for key, value in producer_data.items()
        if key != "CONSUMERS" and value not in (None, "", "NULL")
    }

    # Split consumers (comma-separated string)
    consumer_ids = producer_data["CONSUMERS"].split(",")

    # Fetch details for each consumer
    consumers = []
    for cid in consumer_ids:
        consumer_details = get_consumer_details(conn, consumer_sql, cid.strip())
        if consumer_details:
            consumers.append(consumer_details)

    # Add consumers to producer dict
    producer_dict["Consumers"] = consumers

    return {"Producer": producer_dict}

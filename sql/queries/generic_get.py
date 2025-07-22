def fetch_table_details(table_name, where_clause, params, cursor):
   
    try:
        query = f"SELECT * FROM {table_name} WHERE {where_clause}"
        cursor.execute(query, params)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        result = []
        for row in rows:
            row_data = {}
            for col_name, value in zip(columns, row):
                if value not in (None, "", "NULL"):  # skip null/empty
                    row_data[col_name] = str(value)
            if row_data:  # only include if there's at least one non-null field
                result.append({table_name: row_data})

        return result

    except Exception as e:
        print(f"[GenericFetcher] Error fetching from {table_name}: {e}")
        return []

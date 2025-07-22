from sql.db_adapter import execute_query

def fetch_table_details(conn, table_name, where_clause, params):
    """
    Fetch all non-null columns from a table.
    """
    query = f"SELECT * FROM {table_name} WHERE {where_clause}"
    results = execute_query(conn, query, params)

    if not results:
        return None

    clean_results = []
    for row in results:
        clean_row = {col: val for col, val in row.items() if val not in (None, "", "NULL")}
        if clean_row:
            clean_results.append({table_name: clean_row})
    return clean_results
